---
status: accepted
---

# Canonical Sources and Derived Artifacts

**Initial evidence:** OpenDART, Creo, Seoro, Unslide

## Decision

Give each durable concern one canonical source. Treat alternate representations
as generated projections, delivery artifacts, runtime state, or inspection
evidence with explicit ownership and freshness rules.

Examples of a canonical concern include an API contract, workflow document,
database schema history, standalone report, or package manifest. The reusable
decision is not the format. It is that the project can name which representation
is authoritative and explain how every other representation follows from it.

## Authority

A canonical source must be:

- intentionally authored or changed through one reviewed path;
- sufficient to regenerate or reconcile its derivatives;
- paired with independently justified evidence when it is also the executable
  implementation of the concern; and
- explicit about unknown, inferred, and externally sourced facts.

Executable code may be canonical when all current consumers use that code and
an independent standard artifact has no concrete purpose. For example, a Rust
protocol module may own a Rust-only provider contract while external source
material and independently authored fixtures verify compatibility without
becoming a second contract authority.

Do not let generated code, database mappings, screenshots, caches, runtime
projections, or deployed copies silently become parallel authorities.

Separate authorities by concern when necessary. A provider specification may
own wire facts while an application database owns product identity and current
domain decisions. One source of truth does not mean one file or one system for
the entire product.

## Derivatives

Derivatives should be deterministic whenever their inputs and environment are
controlled. They may be committed when reviewability, consumer builds, release
packaging, or offline verification benefits from it.

Every derivative needs:

- a named canonical input;
- one owning generator or projection path;
- a freshness or reconciliation check;
- a rule for whether it is committed, cached, or built on demand; and
- provenance sufficient to identify the input and generator contract.

Do not repair poor generated output with a permanent handwritten compatibility
layer. Correct the canonical model, normalized model, or generator so every
consumer receives the same fix.

## Safe publication

Never replace the last known-good artifact before the complete candidate has
been produced and validated.

For files or managed trees:

1. validate the destination and ownership boundary;
2. build the complete candidate in same-filesystem staging;
3. validate the staged candidate independently;
4. publish the declared atomic unit through replacement where the platform
   permits it;
5. restore the last known-good state if publication of that unit fails; and
6. preserve recovery evidence when restoration cannot complete safely.

Managed-tree replacement must preserve unrelated files and reject broad,
symlink-escaped, or ambiguously owned targets. Partial success must be reported
truthfully. In a composed workflow, preserve independently published valid
artifacts, publish any completion manifest last, and report exactly which units
completed. Do not claim a multi-artifact transaction when outputs actually
publish independently.

## Verification

Use the portfolio in
[Verification from Source to Consumer](../practices/verification-from-source-to-consumer.md).
This architecture contributes three specific invariants:

- every derivative identifies its canonical input and owning generator;
- regeneration reconciles deterministically with exact identity coverage,
  rather than copied counts; and
- independent evidence exists where a source, derivative, or implementation
  could otherwise certify the same mistaken assumption.

## Migration

During a migration, temporary dual implementations may establish parity. The
target state still has one authority and one final path. Cut over once, then
remove superseded models, generators, validators, projections, and tests.

## Revisit when

Split an authority only when distinct consumers genuinely require independent
ownership or compatibility. If regeneration is impossible by design, document
the reconciliation and recovery contract instead of calling the copy derived.
