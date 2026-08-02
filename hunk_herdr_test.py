import json
import os
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parent))

import hunk_herdr


class Completed:
    def __init__(self, returncode: int, stdout: str = "") -> None:
        self.returncode = returncode
        self.stdout = stdout


class HunkHerdrTest(unittest.TestCase):
    def test_worktree_command_uses_hunk_when_available(self) -> None:
        with patch("shutil.which", return_value="/usr/bin/hunk"), patch.dict(os.environ, {}, clear=True):
            self.assertEqual(hunk_herdr.shell_command("/repo", "worktree"), "hunk diff --no-transparent-bg")

    def test_staged_command_uses_bunx_fallback(self) -> None:
        with patch("shutil.which", return_value=None), patch.dict(os.environ, {}, clear=True):
            self.assertEqual(hunk_herdr.shell_command("/repo", "staged"), "bunx hunkdiff diff --staged --no-transparent-bg")

    def test_commit_command_uses_hunk_show(self) -> None:
        with patch("shutil.which", return_value="/usr/bin/hunk"), patch.dict(os.environ, {}, clear=True):
            self.assertEqual(hunk_herdr.shell_command("/repo", "commit"), "hunk show --no-transparent-bg")

    def test_theme_env_is_passed_to_hunk(self) -> None:
        with patch("shutil.which", return_value="/usr/bin/hunk"), patch.dict(os.environ, {"HUNK_THEME": "catppuccin-mocha"}):
            self.assertEqual(
                hunk_herdr.shell_command("/repo", "worktree"),
                "hunk diff --theme catppuccin-mocha --no-transparent-bg",
            )

    def test_branch_command_prefers_upstream(self) -> None:
        calls = {
            ("branch", "--show-current"): "feature\n",
            ("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{upstream}"): "origin/feature\n",
        }

        def fake_run(cmd, **kwargs):
            key = tuple(cmd[1:])
            return Completed(0, calls[key])

        with patch("subprocess.run", side_effect=fake_run), patch("shutil.which", return_value="/usr/bin/hunk"), patch.dict(os.environ, {}, clear=True):
            self.assertEqual(hunk_herdr.shell_command("/repo", "branch"), "hunk diff origin/feature..feature --no-transparent-bg")

    def test_missing_workspace_id_exits(self) -> None:
        with patch.dict(os.environ, {"HERDR_PLUGIN_CONTEXT_JSON": json.dumps({})}, clear=True):
            with self.assertRaises(SystemExit) as err:
                hunk_herdr.target_context()
            self.assertEqual(str(err.exception), "missing Herdr workspace id")


if __name__ == "__main__":
    unittest.main()
