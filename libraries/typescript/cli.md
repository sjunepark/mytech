---
status: accepted
---

# Effect CLI for TypeScript Command-Line Interfaces

**Initial evidence:** Effect v4 CLI in fs and htmlview; Commander in Darty,
KASB, and Landprice

## Decision

For a TypeScript CLI already using Effect, prefer the CLI library compatible
with its chosen Effect major version. Share its existing resource, error, and
runtime model rather than introducing another composition root.

For Effect v4, this is `effect/unstable/cli`; the separate `@effect/cli` package
belongs to the v3 ecosystem. Follow the
[upstream migration guide](https://github.com/Effect-TS/effect/blob/main/MIGRATION.md)
when changing majors. Do not adopt or upgrade Effect solely to obtain a command
parser. Existing v3 applications can keep their compatible CLI integration
until a deliberate application migration.

Keep unstable parser APIs at the CLI boundary. Pin a compatible exact package
set when using prereleases, and treat unstable-module upgrades as explicit
compatibility work. CLI selection does not require a prerelease runtime.

For a CLI that does not otherwise benefit from Effect, prefer Commander with
`@commander-js/extra-typings`. Use oclif when concrete plugin, hook, or command
platform requirements outweigh a smaller parser's simplicity.

Keep application operations separate from parser construction. Follow
[Effect runtime guidance](effect.md) for composition and
[Automation-Facing CLI Contracts](../../practices/automation-facing-cli-contracts.md)
for output, errors, artifacts, and automation.

## Revisit when

Change parsers when required command behavior or recurring compatibility work
outweighs the existing integration. Evaluate the application's need for Effect
separately from the quality of its CLI parser.
