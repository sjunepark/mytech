# Go for Operational Services and Repository Tooling

**Status:** Draft — owner review required  
**Initial evidence:** OpenDART, Creo

## Tentative preference

Prefer Go for long-lived private repository tooling and narrow network or data
plane services when the dominant needs are operational robustness, explicit
concurrency, portable binaries, standard protocols, and low framework overhead.

Keep command entry points thin. Put parsing, policy, provider integration,
database access, validation, and reporting behind internal packages. Prefer the
standard library at process and network boundaries; add focused dependencies
only when they remove protocol or infrastructure complexity the project should
not own.

Confine third-party models behind project-owned interfaces. A private Go module
does not become a public consumer API merely because it produces public
artifacts.

## Why this is uncertain

The source projects use Go for different roles: one for contract and repository
tooling, another for a provider gateway data plane. That may reveal a broad
language preference, or it may only show that Go fit two independent problems.

The evidence does not establish Go as the default for application domains,
workers, public SDKs, desktop code, or all command-line tools.

## Promotion questions

- Is Go the preferred default for substantial repository-owned tooling, or was
  it selected only because of the available OpenAPI ecosystem?
- Is Go the preferred default for independently deployed network data planes?
- Should a Go service remain standard-library-first even when a small framework
  would reduce meaningful operational complexity?
- Which signals should choose Go over Rust or TypeScript for a new internal
  executable?

## If accepted

Promote a role-based decision, not a universal Go stack. Exact Go versions,
OpenAPI libraries, database drivers, telemetry packages, and hosting choices
should remain project-specific.
