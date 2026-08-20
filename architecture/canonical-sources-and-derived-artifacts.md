---
status: accepted
---

# Canonical Sources and Derived Artifacts

**Initial evidence:** OpenDART, Creo, Seoro, Unslide

## Decision

Give each durable concern one canonical source. Treat alternate representations
as generated projections, delivery artifacts, runtime state, or inspection
evidence with explicit ownership and freshness rules.

The format is not the decision. The project must be able to name which
representation is authoritative and explain how every other representation
follows from it.

## Authority

A canonical source must be:

- intentionally authored or changed through one reviewed path;
- sufficient to regenerate or reconcile its derivatives;
- explicit about unknown, inferred, and externally sourced facts.

Executable code may be canonical when all current consumers use it and an
independent standard artifact has no concrete purpose. Pair an executable
authority with independently justified evidence rather than letting it certify
itself.

External HTTP contracts follow
[External HTTP Contracts and Handwritten Clients](external-http/external-http-contracts-and-handwritten-clients.md).

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

Every derivative needs a named canonical input, one owning generator or
projection path, a freshness or reconciliation check, and a rule for whether it
is committed, cached, or built on demand. Preserve enough provenance to identify
the input and generator contract.

Do not repair poor generated output with a permanent handwritten compatibility
layer. Correct the canonical model, normalized model, or generator so every
consumer receives the same fix.

Migration may use temporary parity checks, but its target has one authority and
one final path. After cutover, remove superseded sources, generators,
validators, projections, and tests.

## Safe publication

Build a complete candidate in same-filesystem staging, validate it
independently, then replace the declared atomic unit where the platform permits
it. Reject broad, ambiguous, or symlink-escaped targets and preserve unrelated
files. Restore the last known-good state when replacement fails; preserve
recovery evidence when restoration cannot complete safely.

When outputs publish independently, report partial success truthfully and
publish any completion manifest last. Do not claim a transaction broader than
the unit the system can replace atomically.

## Verification

Use the portfolio in
[Verification from Source to Consumer](../practices/verification-from-source-to-consumer.md).
Every derivative must identify its input and generator, reconcile
deterministically with exact identity coverage, and rely on independent evidence
where an authority and its projection could share the same mistaken assumption.

## Revisit when

Split an authority only when distinct consumers genuinely require independent
ownership or compatibility. If regeneration is impossible by design, document
the reconciliation and recovery contract instead of calling the copy derived.
