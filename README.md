# Hunk Diff

Herdr plugin for opening Hunk diffs in a split pane or tab.

## Install

```bash
herdr plugin install edmundmiller/herdr-plugin-hunk
```

## Actions

- `hunk.diff.worktree-split`
- `hunk.diff.worktree-tab`
- `hunk.diff.staged-split`
- `hunk.diff.staged-tab`
- `hunk.diff.branch-split`
- `hunk.diff.branch-tab`
- `hunk.diff.commit-split`
- `hunk.diff.commit-tab`

On Windows the action ids carry a `-windows` suffix (for example
`hunk.diff.commit-split-windows`), because Herdr rejects duplicate action ids
across platforms. Bind those ids in the Windows config.

## Requirements

- Herdr `0.7.0` or newer
- `python3` (Linux/macOS) or `python` (Windows)
- `hunk` or `bunx hunkdiff`

## Theme

Set `HUNK_THEME` to pass an explicit Hunk theme:

```bash
HUNK_THEME=catppuccin-mocha
```
