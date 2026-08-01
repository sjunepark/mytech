---
status: accepted
---

# OpenAPI Contract Authority and Conformance

**Initial evidence:** OpenDART, Seoro

## Decision

For every external HTTP provider integration, keep or create an OpenAPI
contract as the sole repository authority for the supported HTTP and wire
contract. Handwrite each language-specific client as a conforming
implementation. Do not generate client source and do not let a handwritten
implementation become a second wire authority.

The provider still owns the external protocol. The repository-owned OpenAPI
contract is the reviewed representation of the subset the project supports.
Official provider specifications and bounded observations are evidence for
that representation, not competing repository contracts.

Both the contract and every implementation are verified against one shared,
fictional, evidence-backed fixture corpus. When multiple languages implement
the contract, test-only runners emit the same versioned canonical projection
of prepared requests, decoded outcomes, and failure classifications. CI checks
each result against independent expectations and compares implementations
differentially. Deterministic mutations provide positive controls that prove
the checks detect drift.

OpenAPI owns wire facts. Handwritten code may own transport safety, project
policy, ergonomics, and domain translation that OpenAPI cannot express
truthfully, but it must not duplicate paths, parameter serialization, wire
schemas, statuses, media types, or other facts already owned by the contract.

## Scope

This decision governs:

- the canonical OpenAPI contract package for an external provider;
- the selected OpenAPI dialect and supported profile;
- handwritten language-specific conforming clients;
- shared fixture and canonical-projection contracts;
- cross-language differential verification; and
- language-specific transport-safety verification.

It does not define:

- provider selection, credential access, or live-probe approval;
- application domain models or product policy;
- a public SDK's compatibility policy; or
- a specific OpenAPI parser, validator, or implementation language.

## Target shape

```text
Official specification or reviewed provider evidence
                         |
                         v
             Canonical OpenAPI contract package
             - OpenAPI source
             - provenance and support manifest
             - independent shared fixtures
                         |
             +-----------+-----------+
             |                       |
             v                       v
   Handwritten Rust conformer  Handwritten TypeScript conformer
             |                       |
             +-----------+-----------+
                         |
                         v
       Versioned canonical request/outcome/failure projections
                         |
                         v
       exact expectations + differential comparison + mutations
```

Only the canonical OpenAPI contract is edited as the repository authority for
supported wire behavior. Bundles, reports, documentation, and other generated
views are reproducible derivatives. Language-specific clients are handwritten
conformers: their code is not derived mechanically, but their observable wire
behavior is constrained mechanically.

## Canonical contract package

A project-owned package uses this conceptual layout:

```text
contracts/<provider>/
  openapi.yaml
  manifest.yaml
  fixtures/
    cases/
    expected/
  generated/
    openapi.bundle.yaml
```

Names may follow local conventions, but the roles remain distinct:

- `openapi.yaml` is the reviewed authority for supported operations,
  parameters, schemas, responses, authentication shape, media types, and wire
  serialization.
- `manifest.yaml` records provenance, supported scope, known unknowns,
  validation profile, and project policy that OpenAPI cannot express cleanly.
  It references rather than redefines OpenAPI-owned operations or schemas.
- `fixtures/` contains fictional, independently justified request, success,
  and failure cases plus their versioned expected projections.
- `generated/` contains deterministic views of the contract and is never
  edited manually.

A provider-owned specification may be pinned unchanged as evidence or used
directly when it exactly serves the supported subset. If the repository authors
or narrows the contract, record that ownership and provenance explicitly. Do
not quietly patch a provider-owned file and continue calling it upstream.

Official specifications are preferred evidence. Bounded observations may fill
documented gaps only through the owning review path. Unknown behavior stays
unknown; do not invent response fields, pagination rules, status semantics, or
error shapes to make a client easier to implement.

Fixture payloads must be fictional or sanitized, bounded, reviewable, and safe
to retain. They never contain credentials, authenticated URLs, unrestricted
request data, or raw sensitive provider responses.

## OpenAPI dialect and profile

Declare and pin the exact source dialect. Use the newest dialect supported
truthfully by the repository validators and every standards-native consumer;
otherwise pin the dialect that serves the current provider evidence and tools.
Do not add lossy dialect conversion only to standardize repository internals.

The repository profile must define at least:

- supported document and reference shapes;
- required stable operation identities;
- parameter locations, styles, and serialization combinations;
- accepted media types and schema vocabularies;
- request, success-response, and failure-response modeling;
- authentication schemes represented without credential values;
- supported JSON Schema keywords and format semantics; and
- approved specification extensions and their schemas.

Unsupported or ambiguous constructs fail validation with structured
diagnostics. They are never ignored, approximated, or translated silently to
unconstrained language types.

External references are pinned or vendored for offline verification. Reference
resolution must not perform uncontrolled network access during ordinary builds
or merge verification.

## Handwritten conformers

Each supported language implements the same contract behind a small
project-owned protocol boundary. Handwritten code owns:

- an ergonomic public or internal interface;
- pure request preparation and provider response decoding;
- credential acquisition and secret handling;
- transport limits, retries, redirects, and timeouts;
- repository safety bounds;
- explicit project policy outside the wire contract;
- translation into application domain models; and
- command-line or user-interface presentation.

The implementation reads the OpenAPI contract as authority during review and
verification; it need not parse the contract at runtime. Language types,
serializers, validators, and decoders may encode wire facts locally as
implementation machinery, but changes to those facts begin with the OpenAPI
source and must pass shared conformance. Do not maintain independent
language-specific fixtures or expectations for behavior that every conformer
shares.

Give every rule one semantic owner. OpenAPI owns schema and protocol rules.
Handwritten policy owns only semantics outside that expressiveness, such as a
project's acceptable-result criteria, safety budget, retry decision, or domain
mapping. Record those rules explicitly and test them without restating the wire
contract in a second manifest or model.

## Shared evidence and canonical projections

Every conformer consumes the same cases and independent expected results. A
case identifies its operation, fictional inputs or response bytes, and the
evidence or decision that justifies the expectation. Cover successful requests
and responses, missing or empty values, provider failures, malformed data, and
boundary conditions relevant to the supported subset.

A test-only runner in each language emits a versioned JSON projection of:

- the prepared request structure, including method, path, ordered or
  canonically represented parameters, relevant headers, media type, and body;
- the decoded success or provider-failure outcome;
- the stable failure classification; and
- validation issues that are part of the shared contract.

The projection is a comparison protocol, not a new source of wire truth. Keep
it minimal, deterministic, credential-free, and independent of dependency
display strings or target-language type names. Version it when its own shape or
meaning changes.

## Verification

Verification is layered so no implementation certifies itself:

1. **Source verification** validates the selected OpenAPI dialect, manifest,
   local references, supported profile, and approved extensions.
2. **Independent contract verification** checks every shared fixture and its
   expected result against the reviewed OpenAPI contract and evidence.
3. **Per-language conformance** runs every fixture through each handwritten
   conformer and compares its canonical projection with the independent
   expectation.
4. **Differential conformance** compares canonical projections across all
   implementations exactly. It is additional evidence, not a replacement for
   independent expectations; two clients can share the same mistake.
5. **Mutation controls** deterministically alter protected request, response,
   or classification behavior and prove that expectation and differential
   checks fail.
6. **Transport safety** is proved independently in each language against a
   local server or equivalent real boundary, covering origin and credential
   scope, redirects, retries, proxy behavior, encoding, size limits, timeouts,
   decompression, malformed responses, and redaction as applicable.
7. **Consumer verification** tests each SDK or protocol module through its
   supported interface.
8. **Bounded live probes** detect provider drift under explicit credential,
   rate, retention, and sanitization policy; they are never the sole merge
   gate.

CI fails if a fixture lacks coverage in any supported implementation, an
implementation disagrees with an independent expectation, implementations
disagree with each other, a mutation survives, the OpenAPI source is invalid,
or a committed derivative is stale.

## Evolution and adoption

Pin the OpenAPI dialect, provider-source revision, validation tools, supported
profile, canonical-projection version, and relevant language dependencies. A
contract change is complete only when every supported conformer and consumer
passes the shared verification portfolio.

An adopting project should:

1. inventory every source of wire, validation, decoding, and policy behavior;
2. establish the canonical OpenAPI package and supported subset;
3. establish fictional, independently justified shared fixtures and expected
   projections;
4. bring one handwritten client into conformance behind its protocol boundary;
5. add each remaining language to the same cases and differential comparison;
6. add independent transport-safety tests for every language;
7. cut over once; and
8. remove superseded wire authorities, duplicated fixtures, and generated
   client pipelines.

Migration may use temporary parity checks, but the target state has one OpenAPI
authority, one shared evidence corpus, and handwritten conformers whose
observable behavior is mechanically constrained.

Provider qualification and safe evidence collection follow
[External Provider Qualification](../practices/external-provider-qualification.md).
General source ownership follows
[Canonical Sources and Derived Artifacts](canonical-sources-and-derived-artifacts.md).

## Revisit when

Reconsider the dialect, profile, projection shape, or implementation strategy
when it cannot represent or verify a provider's supported behavior truthfully.
Preserve one language-neutral wire authority, independent evidence, shared
cross-language conformance, and language-specific transport-safety proof even
if the supporting tools change.
