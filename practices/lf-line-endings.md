---
status: accepted
---

# LF Line Endings

## Decision

Store and check out text files with LF line endings on every platform. Each
repository owns this in a committed `.gitattributes`, so the result does not
depend on a contributor's Git configuration:

```gitattributes
* text=auto eol=lf
```

`text=auto` leaves files Git detects as binary untouched. Add a narrower
`eol=crlf` rule only for a file whose consumer requires CRLF, such as a Windows
`.bat` or `.cmd` script. When adding the file to an existing repository, run
`git add --renormalize .` and commit the result.

Add an `.editorconfig` with `end_of_line = lf` so editors create new files that
already match. On Windows machines, set `core.autocrlf` to `false` globally so
Git does not rewrite files outside what the repository declares.

Byte-sensitive outputs such as installers, embedded help text, fixtures, and
snapshot tests otherwise differ by platform, and conversion warnings hide
real changes in diffs.

Initial evidence: `cpaikr/darty` and this repository.

## Revisit when

Reconsider when a project's primary consumers or tooling require CRLF, or when
Git changes its default line-ending handling enough that repository attributes
no longer add control.
