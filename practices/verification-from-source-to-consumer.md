---
status: accepted
---

# Verification from Source to Consumer

**Initial evidence:** OpenDART, Creo, Seoro, Unslide

## Decision

Build a layered verification portfolio that follows the real path from
authoritative source to distributed consumer behavior. No implementation should
be its own only oracle.

Expose one discoverable repository-level command interface for local work and
CI. It may delegate to language-native tools; a polyglot repository does not
need to pretend it is one language project.

## Verification layers

Select only the layers needed for the product's risks:

- validate canonical schemas, contracts, migrations, configuration, manifests,
  and references;
- test deterministic logic and generation against independent evidence,
  committed freshness, and exact identity-set coverage rather than copied
  totals;
- exercise the real boundary closest to the claim, such as a browser, database,
  external process, local server, filesystem, IPC bridge, or operating-system
  behavior; and
- install the actual distributable into a clean consumer through its supported
  surface, then inspect the final package, binary, document, or deployed schema
  recipients receive.

Mocks remain useful inside a boundary, but cannot replace the engine,
serialization, packaging, or platform behavior the claim depends on.

## Adversarial evidence

A safeguard test should prove it can distinguish the unsafe behavior. Include a
positive control when testing retry suppression, proxy isolation, bounds,
redaction, feature unification, rollback, or cleanup.

Inject failures across staging, commit, cleanup, interruption, and recovery.
Assert both the primary failure and the state left for users or operators.

Renew focused evidence after dependency upgrades that can change wire behavior,
resource lifetimes, database mapping, credential handling, or another tested
boundary.

## Execution

Expose focused edit, complete pre-push, and exhaustive or platform-specific
tiers when needed. Fetch dependencies explicitly, run reproducible gates
offline when practical, and have CI invoke the same repository-owned contracts
as local work.

## Distribution and release

Before release, inspect exact artifact contents and public exports, verify the
absence of private or secret material, exercise a clean consumer, bind artifacts
to source and canonical-input provenance, and reconcile the tag, declared
version, and checkout identity. Prefer short-lived trusted publishing over
retained registry tokens. Version independently supported contracts
independently.

## Live checks

Keep credentialed or network-dependent checks separate from ordinary merge
verification so contributors do not need production access, and treat failures
as owned evidence rather than best-effort noise. Follow
[External Provider Qualification](external-provider-qualification.md) for
bounded preflight, sanitization, rate limits, evidence handling, and production
authority.

## Revisit when

Remove redundant tests when a stronger interface-level test replaces an
obsolete implementation path. Add a layer only for a real risk or compatibility
claim; verification breadth is not a goal by itself.
