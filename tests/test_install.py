from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
INSTALLER = REPO_ROOT / "scripts" / "install.py"


class InstallerTests(unittest.TestCase):
    def run_installer(self, project: Path, *arguments: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [
                sys.executable,
                str(INSTALLER),
                "--scope",
                "project",
                "--project-dir",
                str(project),
                *arguments,
            ],
            check=False,
            capture_output=True,
            text=True,
        )

    def test_default_installs_all_hosts_and_is_idempotent(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            first = self.run_installer(project)
            self.assertEqual(first.returncode, 0, first.stderr)

            expected = (
                ".agents/skills/right-problem",
                ".claude/skills/right-problem",
            )
            for relative in expected:
                installed = project / relative
                self.assertTrue((installed / "SKILL.md").is_file())
                metadata = (installed / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn("name: right-problem", metadata)
                self.assertTrue((installed / "references" / "examples.md").is_file())
                self.assertFalse((installed / "scripts" / "install.py").exists())
            self.assertFalse((project / ".cursor/skills/right-problem").exists())
            self.assertFalse((project / ".gemini/skills/right-problem").exists())

            second = self.run_installer(project)
            self.assertEqual(second.returncode, 0, second.stderr)
            self.assertIn("already installed", second.stdout)

    def test_all_retires_redundant_host_specific_copies(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            cursor = self.run_installer(project, "--agent", "cursor")
            gemini = self.run_installer(project, "--agent", "gemini")
            self.assertEqual(cursor.returncode, 0, cursor.stderr)
            self.assertEqual(gemini.returncode, 0, gemini.stderr)

            combined = self.run_installer(project)
            self.assertEqual(combined.returncode, 0, combined.stderr)
            self.assertTrue((project / ".agents/skills/right-problem/SKILL.md").is_file())
            self.assertTrue((project / ".claude/skills/right-problem/SKILL.md").is_file())
            self.assertFalse((project / ".cursor/skills/right-problem").exists())
            self.assertFalse((project / ".gemini/skills/right-problem").exists())
            self.assertEqual(combined.stdout.count("removed redundant copy"), 2)

    def test_different_install_requires_force_and_force_keeps_backup(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            target = project / ".claude/skills/right-problem"
            first = self.run_installer(project, "--agent", "claude")
            self.assertEqual(first.returncode, 0, first.stderr)

            marker = "locally changed\n"
            (target / "SKILL.md").write_text(marker, encoding="utf-8")
            conflict = self.run_installer(project, "--agent", "claude")
            self.assertEqual(conflict.returncode, 2)
            self.assertEqual((target / "SKILL.md").read_text(encoding="utf-8"), marker)

            forced = self.run_installer(project, "--agent", "claude", "--force")
            self.assertEqual(forced.returncode, 0, forced.stderr)
            self.assertTrue((target / "SKILL.md").read_text(encoding="utf-8").startswith("---\n"))
            backups = list((project / ".right-problem-backups").rglob("SKILL.md"))
            self.assertEqual(len(backups), 1)
            self.assertEqual(backups[0].read_text(encoding="utf-8"), marker)

    def test_dry_run_and_uninstall(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            dry_run = self.run_installer(project, "--agent", "cursor", "--dry-run")
            self.assertEqual(dry_run.returncode, 0, dry_run.stderr)
            self.assertIn("would copy", dry_run.stdout)
            self.assertFalse((project / ".cursor").exists())

            installed = self.run_installer(project, "--agent", "cursor")
            self.assertEqual(installed.returncode, 0, installed.stderr)
            removed = self.run_installer(project, "--agent", "cursor", "--uninstall")
            self.assertEqual(removed.returncode, 0, removed.stderr)
            self.assertFalse((project / ".cursor/skills/right-problem").exists())

    @unittest.skipIf(os.name == "nt", "Directory symlink permissions vary on Windows")
    def test_link_install_and_uninstall_never_remove_source(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            project = Path(temporary)
            installed = self.run_installer(project, "--agent", "gemini", "--method", "link")
            self.assertEqual(installed.returncode, 0, installed.stderr)
            target = project / ".gemini/skills/right-problem"
            self.assertTrue(target.is_symlink())
            self.assertEqual(target.resolve(), REPO_ROOT)

            removed = self.run_installer(project, "--agent", "gemini", "--uninstall")
            self.assertEqual(removed.returncode, 0, removed.stderr)
            self.assertFalse(target.exists())
            self.assertTrue((REPO_ROOT / "SKILL.md").is_file())


if __name__ == "__main__":
    unittest.main()
