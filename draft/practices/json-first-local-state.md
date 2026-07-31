---
status: draft
---

# JSON-First Local Application State

**Initial evidence:** Creo

## Tentative preference

For small, document-shaped local application state, begin with versioned JSON
instead of an embedded database.

Validate the complete record at read and write boundaries. Use one owning
writer, publish with same-directory temporary files and atomic replacement, and
preserve the last valid state on failure.

Keep portable authored documents separate from execution history, caches,
secrets, renderer state, and machine-local profiles.

Introduce SQLite or another embedded database only when concrete needs for
indexed queries, relational integrity, concurrent writers, transaction breadth,
or data volume outweigh whole-document simplicity.

## Why this is uncertain

The decision is implemented and well tested in one desktop product, but the
other scanned repositories do not provide comparable local application-state
requirements.

## Promotion questions

- Is JSON the preferred starting point for all small local-first application
  state, or only for portable authored documents?
- What kinds of data must use a database immediately even at small scale?
- Is a single owning process or writer a required condition?
- Should migrations rewrite documents eagerly, lazily, or only through explicit
  user action?
- What recovery and backup guarantees should exist before this becomes a
  general default?

## If accepted

Promote a storage-selection rule based on access patterns and invariants. Avoid
turning the current desktop directory layout or document schema into reusable
guidance.
