---
status: draft
---

# Go for Operational Services and Repository Tooling

**Initial evidence:** OpenDART, Creo

## Tentative preference

Prefer Go for long-lived private repository tooling and narrow network or data
plane services when the dominant needs are operational robustness, explicit
concurrency, portable binaries, standard protocols, and low framework overhead.

Prefer the standard library at process and network boundaries; add focused
dependencies only when they remove protocol or infrastructure complexity the
project should not own. Apply the project-owned interfaces and dependency
containment in
[Boundary-Owned Contracts and Pure Cores](../../architecture/boundary-owned-contracts-and-pure-cores.md).

## Why this is uncertain

The source projects use Go for contract tooling and a provider gateway. The
unresolved question is when a separately owned Go executable is better than
keeping a capability in its consuming application's language. Explicit
concurrency and portable binaries are useful only when the role needs them.

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
