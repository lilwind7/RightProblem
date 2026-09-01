#!/usr/bin/env python3
"""Install RightQuestion for one or more Agent Skills hosts."""

from __future__ import annotations

import argparse
import hashlib
import os
import shutil
import sys
import tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence


SKILL_NAME = "right-question"
SOURCE_ROOT = Path(__file__).resolve().parents[1]
RUNTIME_ENTRIES = ("SKILL.md", "agents", "references", "LICENSE")
AGENT_DIRS = {
    "universal": ".agents/skills",
    "codex": ".agents/skills",
    "claude": ".claude/skills",
    "cursor": ".cursor/skills",
    "gemini": ".gemini/skills",
}
ALL_AGENTS = ("codex", "claude", "cursor", "gemini")


class InstallError(RuntimeError):
    """Raised for a user-actionable installation failure."""


@dataclass(frozen=True)
class Destination:
    agent: str
    path: Path


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Install the RightQuestion skill for Codex, Claude Code, Cursor, Gemini CLI, or the portable .agents path."
    )
    parser.add_argument(
        "--agent",
        action="append",
        choices=("all", "universal", *ALL_AGENTS),
        help="Target host. Repeat to install for several hosts. Default: all.",
    )
    parser.add_argument(
        "--scope",
        choices=("user", "project"),
        default="user",
        help="Install globally for the current user or into a project. Default: user.",
    )
    parser.add_argument(
        "--project-dir",
        type=Path,
        default=Path.cwd(),
        help="Project root used with --scope project. Default: current directory.",
    )
    parser.add_argument(
        "--method",
        choices=("copy", "link"),
        default="copy",
        help="Copy a portable runtime package or symlink this checkout. Default: copy.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Replace a different existing installation after moving it to a backup.",
    )
    parser.add_argument(
        "--uninstall",
        action="store_true",
        help="Remove the selected installations. This never removes the source checkout or backups.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print the operations without changing files.",
    )
    return parser.parse_args(argv)


def expanded_agents(requested: Sequence[str] | None) -> list[str]:
    raw = list(requested or ["all"])
    expanded: list[str] = []
    for agent in raw:
        candidates = ALL_AGENTS if agent == "all" else (agent,)
        for candidate in candidates:
            if candidate not in expanded:
                expanded.append(candidate)
    return expanded


def destinations(args: argparse.Namespace) -> list[Destination]:
    if args.scope == "project":
        base = args.project_dir.expanduser().resolve()
        if not base.is_dir():
            raise InstallError(f"Project directory does not exist: {base}")
    else:
        base = Path.home()

    result: list[Destination] = []
    seen_paths: set[Path] = set()
    for agent in expanded_agents(args.agent):
        target = base / AGENT_DIRS[agent] / SKILL_NAME
        if target not in seen_paths:
            result.append(Destination(agent=agent, path=target))
            seen_paths.add(target)
    return result


def path_exists(path: Path) -> bool:
    return path.exists() or path.is_symlink()


def file_digest(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def trees_match(source: Path, target: Path) -> bool:
    if source.is_file():
        return target.is_file() and file_digest(source) == file_digest(target)
    if not source.is_dir() or not target.is_dir():
        return False

    source_files = sorted(path.relative_to(source) for path in source.rglob("*") if path.is_file())
    target_files = sorted(path.relative_to(target) for path in target.rglob("*") if path.is_file())
    if source_files != target_files:
        return False
    return all(file_digest(source / path) == file_digest(target / path) for path in source_files)


def payload_matches(target: Path) -> bool:
    if target.is_symlink():
        try:
            return target.resolve() == SOURCE_ROOT
        except OSError:
            return False
    if not target.is_dir():
        return False
    return all(
        not (SOURCE_ROOT / entry).exists() or trees_match(SOURCE_ROOT / entry, target / entry)
        for entry in RUNTIME_ENTRIES
    )


def copy_payload(destination: Path) -> None:
    destination.mkdir()
    for entry in RUNTIME_ENTRIES:
        source = SOURCE_ROOT / entry
        target = destination / entry
        if not source.exists():
            continue
        if source.is_dir():
            shutil.copytree(source, target)
        else:
            shutil.copy2(source, target)


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
    elif path.is_dir():
        shutil.rmtree(path)


def backup_root(args: argparse.Namespace) -> Path:
    base = args.project_dir.expanduser().resolve() if args.scope == "project" else Path.home()
    return base / ".right-question-backups"


def install_one(
    destination: Destination,
    args: argparse.Namespace,
    backup_stamp: str,
) -> str:
    target = destination.path
    if path_exists(target) and payload_matches(target):
        return f"already installed: {target}"

    if path_exists(target) and not args.force:
        raise InstallError(
            f"A different installation already exists at {target}. "
            "Re-run with --force to replace it while keeping a backup."
        )

    action = "link" if args.method == "link" else "copy"
    if args.dry_run:
        replacement = " (existing installation will be backed up)" if path_exists(target) else ""
        return f"would {action}: {SOURCE_ROOT} -> {target}{replacement}"

    target.parent.mkdir(parents=True, exist_ok=True)
    saved: Path | None = None
    if path_exists(target):
        saved = backup_root(args) / backup_stamp / destination.agent / SKILL_NAME
        saved.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(target), str(saved))

    try:
        if args.method == "link":
            target.symlink_to(SOURCE_ROOT, target_is_directory=True)
        else:
            staging_root = Path(tempfile.mkdtemp(prefix=f".{SKILL_NAME}-", dir=target.parent))
            staged = staging_root / SKILL_NAME
            try:
                copy_payload(staged)
                os.replace(staged, target)
            finally:
                shutil.rmtree(staging_root, ignore_errors=True)
    except OSError as exc:
        if saved is not None and path_exists(saved) and not path_exists(target):
            shutil.move(str(saved), str(target))
        raise InstallError(f"Could not {action} {target}: {exc}") from exc

    return f"installed for {destination.agent}: {target}"


def uninstall_one(destination: Destination, dry_run: bool) -> str:
    target = destination.path
    if not path_exists(target):
        return f"not installed: {target}"
    if dry_run:
        return f"would remove: {target}"
    remove_path(target)
    return f"removed: {target}"


def validate_source() -> None:
    missing = [entry for entry in ("SKILL.md", "LICENSE") if not (SOURCE_ROOT / entry).is_file()]
    if missing:
        raise InstallError(f"Incomplete source checkout; missing: {', '.join(missing)}")


def run(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        validate_source()
        targets = destinations(args)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S.%fZ")
        for destination in targets:
            message = (
                uninstall_one(destination, args.dry_run)
                if args.uninstall
                else install_one(destination, args, stamp)
            )
            print(message)
        if not args.dry_run:
            print("Done. Reload skills or restart any agent that was already running.")
        return 0
    except InstallError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
