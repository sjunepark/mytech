# Verification from Source to Consumer

**Status:** Accepted  
**Initial evidence:** OpenDART, Creo, Seoro, Unslide

## Decision

Build a layered verification portfolio that follows the real path from
authoritative source to distributed consumer behavior. No implementation should
be its own only oracle.

Expose one discoverable repository-level command interface for local work and
CI. It may delegate to language-native tools; a polyglot repository does not
need to pretend it is one language project.

## Verification layers

Select the layers the product actually needs:

1. **Source checks** validate schemas, contracts, migrations, configuration,
   manifests, and local references.
2. **Pure logic tests** cover normalization, policy, transformations, and
   deterministic projections.
3. **Independent fixtures** establish externally justified examples without
   using generated output as the oracle.
4. **Generation checks** prove deterministic output, complete identity coverage,
   and committed freshness.
5. **Boundary integration tests** exercise real process, IPC, HTTP, filesystem,
   database, or browser behavior.
6. **Packaged-consumer tests** install the actual distributable into a clean
   consumer and use only its supported surface.
7. **Target-native inspection** examines the artifact recipients receive, such
   as a produced PDF, package archive, binary file, or deployed schema.
8. **Bounded live probes** detect provider drift without becoming the sole
   merge gate.

Use exact identity-set comparison instead of copied totals. A new canonical
item should fail verification wherever coverage is incomplete.

## Real boundaries

Choose the closest practical test to the user-visible risk:

- pure tests for deterministic logic;
- a real browser for interaction and layout;
- a disposable real database for database semantics;
- an external process for CLI contracts;
- a local server or transport adapter for HTTP behavior;
- a packed package for exports, peer dependencies, and install behavior; and
- the final rendered format for delivery correctness.

Mocks remain useful inside a boundary. They must not replace the engine,
serialization, packaging, or operating-system behavior the claim depends on.

## Adversarial evidence

A safeguard test should prove it can distinguish the unsafe behavior. Include a
positive control when testing retry suppression, proxy isolation, bounds,
redaction, feature unification, rollback, or cleanup.

Inject failures across staging, commit, cleanup, interruption, and recovery.
Assert both the primary failure and the state left for users or operators.

Behavior-defining dependency upgrades require renewed focused evidence when they
can change wire bytes, retries, TLS, DNS, parsing, resource lifetime, database
mapping, or credential handling.

## Command tiers

Provide tiers with clear purposes:

- a focused edit loop;
- a complete pre-push or pull-request contract; and
- an exhaustive, scheduled, or platform-specific portfolio.

Fetch dependencies explicitly, then run reproducible gates offline when
practical. CI should invoke the same repository-owned contracts as local work
rather than reimplementing policy in workflow YAML.

## Distribution and release

Before release:

- inspect the exact package or archive contents;
- verify public exports and absence of private or secret material;
- install and exercise it from a clean consumer;
- bind artifacts to source revision and canonical input provenance; and
- verify tag, declared version, and checkout identity before publication.

Prefer short-lived trusted-publishing credentials over retained registry tokens.
Version independently supported contracts independently, even when one
repository produces them from the same source.

## Live checks

Credentialed or network-dependent checks are separate from ordinary merge
verification. They are bounded, sanitized, rate-aware, and paired with a
credential-free preflight. Treat their failure as owned evidence, not
best-effort noise, while avoiding a requirement that every local contributor
possess production access.

## Revisit when

Remove redundant tests when a stronger interface-level test replaces an
obsolete implementation path. Add a layer only for a real risk or compatibility
claim; verification breadth is not a goal by itself.
