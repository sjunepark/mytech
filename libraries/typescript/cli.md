---
status: accepted
---

# Effect CLI for TypeScript Command-Line Interfaces

**Initial evidence:** Effect v4 CLI in fs and htmlview; Commander in Darty,
KASB, and Landprice

## Decision

For TypeScript command-line applications using Effect v4, use
`effect/unstable/cli` as the default command parser and runtime integration. Its
typed arguments, flags, subcommands, handlers, prompts, help, and completion fit
the same Effect program and error model described in
[Effect for TypeScript Application Runtimes](effect.md).

Do not use the separate `@effect/cli` package for Effect v4. Pin the compatible
Effect v4 beta version exactly and keep parser construction behind the CLI
boundary: Effect v4 remains prerelease and `effect/unstable/*` APIs may change in
minor releases.

For a standalone CLI that should not adopt Effect, use Commander with
`@commander-js/extra-typings`. Use oclif only when the product concretely needs a
larger extensible CLI platform such as plugins, hooks, generators, installers,
or auto-update infrastructure.

Keep process output separate from library logging and presentation help. For
commands used by agents or automation, follow
[Automation-Facing CLI Contracts](../../practices/automation-facing-cli-contracts.md).

## Revisit when

Reconsider the unstable Effect CLI default if migration churn exceeds the value
of sharing Effect's typed configuration, errors, services, and lifecycle. When
Effect v4 and its CLI API stabilize, relax exact pins only under the repository's
normal lockfile and upgrade policy.
