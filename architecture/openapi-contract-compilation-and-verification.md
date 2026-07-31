---
status: accepted
---

# OpenAPI 3.2 Contract Compilation and Verification

**Initial evidence:** OpenDART, Seoro

## Decision

When an external HTTP contract needs a language-neutral repository authority,
use [OpenAPI 3.2](https://spec.openapis.org/oas/v3.2.0.html) and compile it
through a repository-owned boundary into a normalized, language-neutral model.
Produce deterministic target artifacts from that model and verify the path from
source contract to each consumer.

The compiler boundary and verification pipeline are part of choosing OpenAPI,
not optional follow-up refinements. They prevent each language generator from
interpreting the source independently and give standards-native tools one
verified bundle. Existing parsers, resolvers, validators, and emitters may
implement the boundary; this decision does not require writing those
mechanisms from scratch.

OpenAPI 3.2 is the default dialect for project-authored contracts. Pin the exact
3.2 patch version and the repository-supported feature profile. When a useful
provider-owned specification uses another dialect, retain it unchanged as
pinned evidence and import it deterministically into the reviewed 3.2
authority. The import must preserve every supported semantic or reject the
unmappable construct; downstream compilation accepts only the canonical 3.2
package.

This guidance applies only after a project establishes a concrete need for a
language-neutral contract. Rust projects use
[External HTTP Contracts and Rust SDKs](rust/external-http-contracts-and-rust-sdks.md)
to make that choice. This document does not make OpenAPI the default for
Rust-only integrations.

## Scope

This decision governs:

- the canonical OpenAPI contract package;
- the supported OpenAPI 3.2 profile;
- reference resolution, linting, normalization, and diagnostics;
- language-neutral operation and schema modeling;
- deterministic language-specific generation; and
- verification from the OpenAPI source through generated consumers.

It does not define:

- when an integration should choose OpenAPI instead of direct Rust;
- provider selection, credential access, or live-probe approval;
- application domain models or product policy;
- a public SDK's compatibility policy; or
- a specific parser, generator framework, or implementation language.

## Target shape

```text
Official specification or reviewed provider evidence
                         |
                         v
             Canonical OpenAPI contract package
             - OpenAPI source
             - provenance and support manifest
             - independently justified fixtures
                         |
                         v
                  Contract compiler
             - load, resolve, lint, bundle
             - enforce the supported profile
             - produce normalized diagnostics and model
                         |
                         v
              +----------+----------+
              |                     |
              v                     v
   Language-neutral model   Verified OpenAPI bundle
              |                     |
              v                     v
     Language generators    Standards-native tools
     - wire types           - documentation
     - serialization        - mocks and gateways
     - validation           - compatibility analysis
              |
              v
       Protocol modules and SDKs
```

Only the canonical contract package is edited as the repository authority for
supported wire behavior. The normalized model, bundles, generated source, and
reports are reproducible derivatives.

## Canonical contract package

A project-owned package uses this conceptual layout:

```text
contracts/<provider>/
  openapi.yaml
  manifest.yaml
  fixtures/
  generated/
    openapi.bundle.yaml
```

Names may follow local conventions, but the roles remain distinct:

- `openapi.yaml` is the reviewed OpenAPI authority for operations, parameters,
  schemas, responses, authentication shape, and wire serialization.
- `manifest.yaml` records provenance, supported scope, known unknowns, compiler
  profile, and policy OpenAPI cannot express cleanly. It references rather than
  redefines operations and schemas owned by OpenAPI.
- `fixtures/` contains independently justified request, success, and failure
  examples. Generated examples may add coverage but are not independent
  evidence.
- `generated/` contains deterministic derivatives and is never edited
  manually.

The owning path is explicit. A directly authored contract changes through
review. A provider-imported contract changes through a reviewed deterministic
import from unchanged pinned evidence. The resulting 3.2 contract is the
repository authority for its supported subset; the provider source remains
external evidence. Do not quietly patch a provider-owned file and continue
calling it upstream.

External references are pinned or vendored for offline compilation. Reference
resolution must not perform uncontrolled network access during ordinary builds
or merge verification. Preserve base-URI semantics, including OpenAPI 3.2
`$self`, and reject ambiguous or unsafe resolution.

Official specifications are preferred evidence. Bounded observations may fill
documented gaps only through the owning review path. Unknown behavior stays
unknown; do not invent response fields, pagination rules, status semantics, or
error shapes to make compilation easier.

## OpenAPI 3.2 profile

Project-authored authorities declare OpenAPI 3.2 and pin the exact patch
version accepted by the repository. The compiler supports a deliberate subset,
not an implicit claim to every construct allowed by the specification.

The profile must define at least:

- supported document and reference shapes;
- required stable operation identities;
- parameter locations, styles, and serialization combinations;
- accepted media types and schema vocabularies;
- request, success-response, and failure-response modeling;
- authentication schemes represented without credential values;
- supported JSON Schema keywords and format semantics; and
- approved specification extensions and their schemas.

Undefined behavior is rejected. Implementation-defined behavior is rejected
unless the repository selects one interpretation, records it in the profile,
and verifies that interpretation across every affected generator and consumer.

Unsupported constructs produce structured diagnostics with source locations.
They are never ignored, approximated, or translated to an unconstrained type
without an explicit contract decision.

## Contract compiler

The compiler is a deep module with a small interface:

```text
canonical contract package -> normalized model or structured diagnostics
normalized model           -> deterministic artifacts
```

It owns these phases behind that interface:

1. load the entry document and manifest;
2. resolve references under the repository's offline and origin policy;
3. validate OpenAPI and the repository-supported profile;
4. bundle or canonicalize documents when a derivative requires it;
5. normalize supported semantics into the language-neutral model; and
6. invoke target generators with pinned configuration.

Callers do not depend on parser-library types or reimplement reference,
serialization, or validation semantics. The compiler may compose existing
standards-compliant tools, but the repository owns their configuration,
compatibility checks, diagnostics, and deterministic orchestration.

A project-owned compiler is the default ownership boundary and serves all
local generator targets. Extract a shared compiler only after multiple projects
demonstrate the same policy-free normalized model and conformance contract.
Sharing is an organizational decision; compilation is an architectural
requirement.

## Normalized model

The normalized model contains only semantics supported consistently by the
compiler and its generators, including:

- operations and stable operation identities;
- parameter locations and serialization rules;
- request bodies, media types, and schemas;
- success and provider-failure responses;
- authentication requirements without credential material;
- schema-derived validation constraints;
- stable rule metadata and source provenance; and
- explicit distinctions between absent, nullable, empty, and unknown values.

Normalization removes representational variation, not meaning. It must not add
defaults, weaken constraints, collapse distinct response cases, or silently
choose among ambiguous interpretations.

The model is private compiler API unless independent consumers prove that a
versioned public representation is necessary. Generators depend on this model,
not directly on the OpenAPI parser or syntax tree.

## Generated and handwritten responsibilities

Every supported language target consumes deterministic artifacts from the
normalized model. Generate facts that are mechanical consequences of the
contract:

- provider-shaped wire types;
- operation and parameter identities;
- request serialization and content negotiation;
- schema-owned validation;
- response dispatch and decoding metadata;
- provider failure-envelope metadata; and
- stable validation-rule metadata.

Keep consumer policy and ergonomics handwritten:

- the deliberately supported public or internal interface;
- credential acquisition and secret handling;
- transport limits, retries, redirects, and timeouts;
- repository safety bounds;
- semantics deliberately outside the wire contract;
- translation into application domain models; and
- command-line or user-interface presentation.

Generated artifacts are private by default. Public re-exports are deliberate
and receive the adopting consumer's compatibility guarantee. Generated source
is never manually corrected; fix the contract, profile, normalized model, or
generator so every affected target receives the correction.

A handwritten protocol wrapper may add transport and ergonomic behavior, but
it must consume generated contract artifacts and must not redefine their wire
facts. A target that cannot generate a required fact fails adoption until the
profile or generator supports it.

Standards-native consumers use the compiler-verified source or bundle rather
than a language artifact. Test their observable behavior when documentation,
mocking, gateway, or compatibility semantics affect the reason OpenAPI was
selected.

## Verification

Verification is layered so no single implementation certifies itself:

1. **Source verification** validates OpenAPI 3.2, the manifest, reference
   resolution, the supported profile, and approved extensions.
2. **Independent contract verification** checks externally justified requests,
   responses, and provider failures without using generated artifacts as its
   oracle.
3. **Compiler verification** tests normalization, structured failure
   diagnostics, deterministic ordering, and rejected constructs.
4. **Generator verification** tests each target against normalized-model
   fixtures and target-language behavior.
5. **Freshness verification** regenerates all committed derivatives and fails
   on any diff.
6. **Cross-target conformance** applies the same independent fixture semantics
   to every language target so serialization, validation, and response
   classification do not drift.
7. **Consumer verification** tests each protocol module or SDK only through its
   supported interface.
8. **Bounded live probes** detect provider drift under explicit credential,
   rate, data-retention, and sanitization policy; they are never the sole merge
   gate.

Compiler and generator fixtures may increase internal coverage but cannot
replace independently justified provider examples. Positive controls must show
that verification fails when a protected invariant is intentionally violated.

Diagnostics, fixtures, generated comments, and reports must not contain
credentials, authenticated URLs, unrestricted request data, or raw sensitive
provider responses.

## Determinism and evolution

Pin the OpenAPI dialect, compiler dependencies, profile, generator versions,
and target configuration. Given the same canonical package and toolchain, the
compiler produces byte-stable committed artifacts or a canonical comparison
that detects every semantic difference.

A contract change is complete only when all supported targets compile and
their conformance suites pass. Compatibility reporting may inform review, but
the owning SDK or API policy decides whether a change is breaking.

Expand the supported profile from concrete provider or consumer needs. Add the
new source case, normalized representation, diagnostics, every affected target
mapping, and independent conformance evidence together. Do not accept syntax
that only one generator understands.

OpenAPI patch upgrades and compiler dependency upgrades renew source,
determinism, and cross-target tests. Minor or major dialect changes require an
explicit architecture review because the specification permits feature and
behavior changes across minor versions.

## Adoption

An adopting project should:

1. inventory current contract, validation, serialization, and decoding truth;
2. establish the canonical package, provenance, supported profile, and
   independent fixtures;
3. compile the package into the minimal truthful normalized model;
4. generate one target and prove parity through its supported consumer
   interface;
5. add remaining language or standard-artifact generators against the same
   model and conformance evidence;
6. enable freshness verification for committed derivatives;
7. cut over once; and
8. delete superseded models, validators, generators, fixtures, and tests.

Migration may use temporary parity checks, but it must not leave OpenAPI and
handwritten wire behavior as permanent co-equal authorities.

Provider qualification and safe evidence collection follow
[External Provider Qualification](../practices/external-provider-qualification.md).
General derivative ownership follows
[Canonical Sources and Derived Artifacts](canonical-sources-and-derived-artifacts.md).

## Revisit when

Reconsider this pipeline when OpenAPI 3.2 cannot represent a required protocol
truthfully, when another language-neutral format better serves every named
consumer, or when compilation obscures rather than removes divergent contract
interpretation. Preserve one authority, independent evidence, deterministic
derivatives, and source-to-consumer verification even if the format or compiler
changes.
