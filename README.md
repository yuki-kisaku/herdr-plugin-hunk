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

## Requirements

- Herdr `0.7.0` or newer
- `python3`
- `hunk` or `bunx hunkdiff`

## Theme

Set `HUNK_THEME` to pass an explicit Hunk theme:

```bash
HUNK_THEME=catppuccin-mocha
```
