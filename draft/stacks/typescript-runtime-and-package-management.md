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

The repositories use Bun for a private application monorepo and pnpm with Node
for public-package and accepted web-stack roles. This may be a durable
role-based policy or merely current project history. The evidence does not
establish one universal test runner.

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
