---
status: accepted
---

# External HTTP Contracts and Handwritten Clients

**Initial evidence:** OpenDART, DartDB, Seoro

## Decision

Every external HTTP provider integration keeps or creates an OpenAPI contract
as the sole repository authority for the supported wire contract. This applies
even when only one language implements or consumes the contract.

Handwrite and maintain each language implementation independently as a
conformer to OpenAPI. Do not generate client code, wire types, validators,
request builders, or response decoders from the contract. This prohibition
includes general-purpose generators, templates, and repository-owned custom
emitters.

Prefer Rust for a new protocol implementation or SDK when no consumer
ecosystem, target platform, runtime, deployment, or organizational constraint
favors another language. Rust is a default for the implementation, not for the
OpenAPI toolchain or every application that consumes the protocol.

Verify each implementation against OpenAPI and independent provider evidence.
When multiple languages exist, use one shared, fictional, evidence-backed
fixture corpus and align their observable request, outcome, and failure
behavior through common canonical projections and exact differential
comparison. Public APIs and internal code remain idiomatic to their languages.

## Why OpenAPI remains canonical

The provider owns the external protocol. The repository-owned OpenAPI contract
is the reviewed representation of the subset the project supports. Official
provider specifications and bounded observations are evidence for that
representation, not competing repository contracts.

A language implementation can encode many wire rules, but its types and
runtime behavior do not provide a complete, portable, independently
inspectable HTTP contract. In particular, they often cannot express all of
these facts clearly in one place:

- operations, paths, methods, and stable operation identities;
- parameter locations, styles, encoding, and serialization;
- request and response media types;
- schema constraints, nullability, and absent-versus-empty distinctions;
- status and provider-failure response shapes; and
- authentication requirements without credential values.

Keeping OpenAPI canonical makes those facts reviewable without interpreting
language-specific types, serializers, HTTP libraries, control flow, or error
handling. It also preserves a neutral contract when another implementation or
standards-native consumer is added later. Do not wait for a second language to
establish this authority.

The implementation does not need to parse OpenAPI at runtime. It may repeat
wire facts in types and code as necessary to implement them, but a wire change
begins in OpenAPI and is complete only when every conformer and applicable
shared expectation agrees.

## Ownership boundary

OpenAPI owns:

- supported operations, paths, methods, and parameters;
- parameter and body serialization;
- authentication shape;
- wire schemas and structural validation;
- statuses, media types, and provider failure envelopes; and
- the supported OpenAPI dialect and approved specification extensions.

Handwritten language code owns:

- an ergonomic project-owned interface;
- pure request preparation and response decoding;
- language-specific types, serializers, and validators used to conform;
- credential acquisition and secret handling;
- redirects, retries, proxies, timeouts, decompression, and size limits;
- project safety bounds and policy outside OpenAPI's expressiveness;
- translation into application domain models; and
- presentation through command-line, service, or user interfaces.

Give each rule one semantic owner. Do not add a language-owned manifest,
fixture set, or model that becomes a parallel authority for OpenAPI-owned
facts. Handwritten policy covers only concerns the wire contract cannot express
truthfully, such as result-selection policy, retry decisions, or domain
mapping.

## Multi-language target shape

```text
Official specification or reviewed provider evidence
                         |
                         v
             Canonical OpenAPI contract package
             - OpenAPI source
             - provenance and supported scope
             - shared fixtures and expectations
                         |
             +-----------+-----------+
             |                       |
             v                       v
   Handwritten conformer A   Handwritten conformer B
             |                       |
             +-----------+-----------+
                         |
                         v
       Canonical request/outcome/failure projections
                         |
                         v
       independent expectations + differential checks
```

A single-language project keeps the same OpenAPI authority and verifies its
handwritten implementation through proportionate project-native tests against
the contract and independent provider evidence. Do not require the shared
fixture, projection, or differential harness until another language implements
the same contract.

## Canonical contract package

A project-owned package has these conceptual roles:

```text
contracts/<provider>/
  openapi.yaml
  manifest.yaml
  fixtures/                 # when cross-language conformance applies
    cases/
    expected/
  generated/
    openapi.bundle.yaml
```

Names may follow local conventions:

- `openapi.yaml` is the reviewed authority for the supported wire behavior.
- `manifest.yaml` records provenance, supported scope, known unknowns,
  validation profile, and project policy that OpenAPI cannot express cleanly.
  It references rather than redefines OpenAPI-owned operations or schemas.
- `fixtures/` contains fictional, independently justified shared cases and
  their versioned expected projections when multiple languages conform.
- `generated/` contains deterministic non-code views and is never edited
  manually.

Generated bundles, documentation, reports, and other non-code views are
permitted when they are deterministic derivatives of OpenAPI with freshness
checks. They must not generate or own any language implementation.

Use a provider-owned specification directly when it exactly serves the
supported subset, or pin it unchanged as evidence for a repository-authored or
narrowed contract. Do not quietly patch an upstream file and continue calling
it provider-owned.

Declare and pin the source dialect and the profile supported by repository
validators and consumers. Reject unsupported or ambiguous constructs with
structured diagnostics rather than ignoring or weakening them. Pin or vendor
external references so ordinary verification does not require uncontrolled
network access.

Fixture payloads are fictional or sanitized, bounded, reviewable, and safe to
retain. They never contain credentials, authenticated URLs, unrestricted
request data, or raw sensitive provider responses.

## Handwritten protocol boundary

Each implementation is a deep handwritten boundary with a small project-owned
interface. Request preparation is pure:

```text
request -> prepared request or PrepareError
```

A prepared request has passed deterministic validation and serialization.
Preparing it performs no network I/O and does not require credentials.
Provider-specific success and failure decoding stays behind the same boundary.

Keep provider-native wire types private by default. Callers should not need to
understand wire fields, validation dependencies, URL encoding, HTTP-library
errors, or provider failure envelopes. Use a transport seam only when real
variation or focused testing requires one; do not publish an abstraction backed
by one implementation merely to anticipate future variation.

Ordinary language libraries may implement serialization, validation, parsing,
URL handling, and transport. They are private implementation machinery, not
contract generators or authorities. Translate their errors into project-owned
failure categories at the protocol boundary.

## Language selection

Prefer Rust when the choice is otherwise neutral because it can make protocol
and capability states explicit and hard to misuse. In particular, Rust can:

- distinguish unprepared, prepared, authorized, possibly sent, and decoded
  states with types and exhaustive results;
- prevent cloning, displaying, serializing, or reusing credential-bearing
  values where those capabilities are unsafe;
- keep a small transport-independent protocol core while offering an optional
  production HTTP adapter; and
- express typed, sanitized failures while configuring transport behavior
  explicitly.

These advantages favor correctness, reviewability, and maintainability over
delivery speed. They do not make Rust universally appropriate. Prefer another
language when its consumer ecosystem, platform support, runtime integration,
deployment model, or team ownership materially improves the contract's use and
maintenance.

Choose the language separately for each role. A Rust protocol implementation
does not imply Rust for OpenAPI maintenance tools, documentation pipelines,
applications, or other consumers.

## Shared cross-language conformance

When multiple languages implement the same contract, every conformer consumes
the same cases and independent expected results. Each case identifies its
operation, fictional inputs or response bytes, and the evidence or decision
that justifies the expectation. Cover successful requests and responses,
missing and empty values, provider failures, malformed data, and relevant
boundary conditions.

A test-only runner in each language emits the same versioned JSON projection
of:

- the prepared method, path, parameters, relevant headers, media type, and
  body;
- the decoded success or provider-failure outcome;
- stable shared failure classifications; and
- validation issues that are part of the shared contract.

The projection is a comparison protocol, not a new source of wire truth. Keep
it minimal, deterministic, credential-free, and independent of language type
names, dependency errors, map-order accidents, or display strings.

Every project verifies the OpenAPI source, references, supported profile, and
its handwritten implementation's observable conformance. With multiple
languages, CI additionally verifies:

1. every shared fixture and expectation against independent contract evidence;
2. every conformer's projection against the independent expectation;
3. exact differential equality across all implementations;
4. complete fixture identity coverage in every implementation; and
5. deterministic mutations that prove protected differences are detected.

Differential agreement cannot replace independent expectations because two
implementations can share a mistake. Shared conformance aligns observable wire
behavior and stable failure meaning; it does not require identical public API
shapes, internal types, dependencies, or source structure.

Each language separately proves its production transport behavior against a
local server or equivalent real boundary. Cover origin and credential scope,
redirects, retries, proxy behavior, encoding, size limits, timeouts,
decompression, malformed responses, and redaction as applicable. Agreement at
the pure protocol layer cannot certify a language's HTTP library or runtime.

## Errors and adapters

Distinguish preparation, credential, transport, HTTP status,
provider-reported, and response-decoding failures whenever callers must react
differently. Callers never classify failures by parsing display strings or
dependency errors.

Public failure variants and codes receive the compatibility guarantee of the
adopting interface. Internal errors may evolve more quickly. Automation-facing
command-line behavior follows
[Automation-Facing CLI Contracts](../practices/automation-facing-cli-contracts.md).

The command-line or process adapter stays thin: parse invocation syntax, call
the protocol boundary, and map project-owned results and failures to the
external envelope. It does not revalidate provider semantics, reconstruct wire
paths, or decode provider bodies.

## Adoption and evolution

An adopting project should:

1. inventory every current source of wire, validation, decoding, and failure
   behavior;
2. establish the canonical OpenAPI contract and supported subset;
3. choose the implementation language, preferring Rust when constraints are
   otherwise neutral;
4. bring one handwritten client into conformance behind its protocol boundary;
5. when another language is added, establish shared fictional fixtures and
   independent expected projections, then conform every implementation to
   them;
6. test the real transport independently in every language;
7. cut over once; and
8. remove superseded wire authorities, generated client pipelines, and
   duplicated fixture sets.

A contract change is complete only when every supported conformer and consumer
passes its verification portfolio. Pin relevant provider revisions, contract
tools, projection versions when used, and language dependencies. Migration may
use temporary parity checks, but the target state has one OpenAPI authority
and independently handwritten conformers, plus one shared evidence corpus when
multiple languages exist.

Provider selection, bounded observations, and production enablement follow
[External Provider Qualification](../practices/external-provider-qualification.md).
General source ownership follows
[Canonical Sources and Derived Artifacts](canonical-sources-and-derived-artifacts.md).

## Revisit when

Reconsider the supported OpenAPI profile when it cannot represent the provider
contract truthfully, or the handwritten implementation policy when independent
conformers cannot be maintained reliably. Preserve one language-neutral wire
authority, independent evidence, and language-specific transport verification
while evaluating a different mechanism.
