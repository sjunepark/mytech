---
status: draft
---

# JSON-First Local Application State

**Initial evidence:** Creo

## Tentative preference

For portable authored documents or small configuration records with one owning
writer, begin with versioned JSON. For relational operational state, begin by
evaluating SQLite even when the data set is small. Size alone does not decide
the storage contract.

Validate the complete record at read and write boundaries. Use one owning
writer, publish with same-directory temporary files and atomic replacement, and
preserve the last valid state on failure. Atomic replacement prevents partial
visibility; crash durability still needs an explicit flush, backup, and recovery
policy appropriate to the filesystem. Multiple application instances must not
silently invalidate the single-writer assumption.

Keep portable authored documents separate from execution history, caches,
secrets, renderer state, and machine-local profiles.

Introduce SQLite or another embedded database only when concrete needs for
indexed queries, relational integrity, concurrent writers, transaction breadth,
or data volume outweigh whole-document simplicity.

## Why this is uncertain

The originating product used document-shaped state. That does not establish a
default for relational run history or concurrent local applications. The
unresolved boundary is the required transaction, recovery, and writer model.

## Promotion questions

- Which state must remain a portable, user-editable document?
- What cross-record invariants and concurrent access must the storage support?
- What loss, recovery, backup, and migration guarantees must survive a crash?

## If accepted

Promote a storage-selection rule based on access patterns and invariants. Avoid
turning the current desktop directory layout or document schema into reusable
guidance.
