---
status: draft
---

# Safe Local Tool Packages

**Initial evidence:** Creo

## Tentative preference

Treat locally installed extension or tool packages as untrusted content before
execution.

Discover and import a package without running its code. Validate its archive,
paths, manifest, declared entry points, and size bounds before accepting it.
Reject ambiguous ownership, path traversal, and content that escapes the
declared package boundary.

Store accepted package content immutably under a content-derived identity.
Keep installation records and runtime environments as separate derived state so
the same package content is not silently changed in place.

Invoke tools through a supervised process contract with bounded structured
stdin and stdout, diagnostic-only stderr, explicit time and output budgets, and
explicit cancellation behavior.

Whether execution must also use an allowlisted environment and explicit grants
for credentials, network access, filesystem access, and subprocess creation is
unresolved. The current evidence does not implement that isolation.

Static validation and a manifest do not make executable code safe. When the
threat model includes hostile code, add an operating-system sandbox or do not
execute the package.

## Why this is uncertain

Package validation and supervised execution establish different guarantees.
The unresolved decision is whether packages are trusted owner-authored code or
potentially hostile third-party code, and which platforms can enforce the
promised execution restrictions. A manifest declaration is not enforcement.

## Promotion questions

- Should immutable content-addressed storage be required or merely preferred?
- Which capabilities may a tool receive by default?
- Is a real operating-system sandbox required before third-party packages are
  supported?
- Which package formats and runtime-environment strategies should remain
  project-specific?

## If accepted

Promote the trust and lifecycle boundary, not the current package layout,
manifest fields, managed runtime, or desktop-specific implementation.
