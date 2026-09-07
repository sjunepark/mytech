---
status: accepted
---

# Code Rewrites

## Decision

Rewrite when the existing structure prevents a required improvement and a
bounded refactor would retain the same underlying problem. Prefer the smallest
replacement that fixes ownership, correctness, or a demonstrated operating
constraint. A favored language or framework is not sufficient justification.

Before replacing implementation, state which observable behavior and persisted
contracts must survive, which behavior intentionally changes, and how the
replacement will be judged. Use independent examples and real consumer paths
so the new implementation cannot define its own success.

Preserve a working comparison or recovery path until the replacement has the
required evidence. Use staged cutover when live data, independent consumers,
or continuous service require coexistence. A disposable internal tool may
support a direct replacement without a compatibility framework.

After cutover, remove superseded implementation and temporary migration
machinery within the authorized scope. Update the owning documentation and
release contracts rather than preserving two nominally canonical paths.

The [Claude Code Migration Kit](https://github.com/anthropics/code-migration-kit-with-claude-code)
is reference material for large language migrations, not a maintained general
rewrite framework. Its default is structure-preserving translation; a redesign
needs different work units and comparison criteria. The adopting project's
contracts and verification decide what success means.

## Revisit when

Stop or narrow the rewrite when it cannot show a concrete advantage over
repairing the existing path, when preserved behavior is still unknown, or when
migration risk exceeds the problem being solved. Expand its scope only when
new evidence exposes a necessary dependency.
