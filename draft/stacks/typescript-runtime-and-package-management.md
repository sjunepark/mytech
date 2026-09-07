---
status: draft
---

# TypeScript Runtime and Package Management

**Initial evidence:** Creo, Seoro, Unslide

## Tentative preference

Use modern ESM TypeScript with strict checking and an explicitly pinned runtime,
package manager, and lockfile. Prefer Node for deployable web applications,
public packages, and consumer-facing runtime contracts. Use Bun when its
workspace runner and development ergonomics materially simplify a private
application repository.

Prefer pnpm for reproducible Node dependency preparation, public-package
consumer workflows, and environments where Node compatibility is itself part
of the contract.

## Why this is uncertain

Runtime compatibility and dependency installation are separate contracts.
Using Bun to run development commands does not establish that a package works
in Node; using pnpm does not itself select a runtime. The unresolved preference
is whether the ergonomic benefit of an additional tool justifies maintaining
both paths. The evidence does not establish one universal test runner.

## Promotion questions

- Is Node the required production runtime even when Bun owns local commands?
- Is pnpm the default for new TypeScript repositories, with Bun reserved for
  application monorepos that benefit from it?
- Should public packages always test a clean Node consumer regardless of the
  repository's package manager?
- Is exact tool pinning required only for prerelease or behavior-defining tools,
  or for the entire JavaScript toolchain?

## If accepted

Document a decision matrix by delivery role. Do not combine Bun, Node, and pnpm
into one nominal stack unless the boundary between them is explicit.
