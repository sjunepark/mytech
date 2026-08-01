---
status: accepted
---

# External HTTP Contracts and Rust SDKs

**Initial evidence:** OpenDART, Seoro

## Decision

Rust clients of external HTTP providers use a canonical OpenAPI contract for
the supported HTTP and wire behavior and expose that behavior through a
handwritten project-owned protocol module. OpenAPI remains the sole repository
wire authority even when Rust is the only current implementation.

Do not generate the Rust client. Handwrite provider-native types,
serialization, validation, request preparation, response decoding, and
project-owned errors as conforming implementation details. Verify their
observable behavior mechanically against the OpenAPI contract, independent
shared fixtures, and a versioned canonical projection.

When another language implements the provider, both implementations consume
the same fixture corpus and emit the same request, outcome, and failure
projection. CI checks each implementation against independent expectations and
compares them differentially. Each language still proves its own transport
safety because agreement at the pure protocol layer cannot certify library or
runtime behavior.

OpenAPI owns paths, operations, parameter serialization, authentication shape,
wire schemas, statuses, media types, and schema validation. Handwritten Rust
owns transport safety, ergonomics, project policy outside OpenAPI's
expressiveness, and domain translation. It must not establish a parallel
manifest or model that duplicates OpenAPI-owned facts.

## Scope

This decision governs:

- the Rust implementation of a canonical external-provider OpenAPI contract;
- request validation, preparation, and response decoding;
- shared cross-language fixtures and differential conformance;
- structuring SDK and command-line errors;
- separating provider protocols from application domains; and
- testing the protocol module and Rust transport.

It does not define:

- an application domain model shared by unrelated providers;
- product-specific retry, caching, ingestion, or persistence policy;
- which provider operations a project supports; or
- whether a Rust protocol module is public or internal.

## Target shape

```text
Official documentation + bounded observations
                         |
                         v
              Canonical OpenAPI contract
                         |
              +----------+----------+
              |                     |
              v                     v
   Shared fictional fixtures   Independent expectations
              |                     |
              +----------+----------+
                         v
           Handwritten Rust protocol module
           - provider-native private types
           - serialization and validation
           - pure request preparation
           - response and error decoding
                         |
                +--------+---------+
                |                  |
                v                  v
          Rust transport     test-only projection runner
```

Follow
[OpenAPI Contract Authority and Conformance](../openapi-contract-compilation-and-verification.md)
for contract ownership, the canonical package, shared fixtures, projection
versioning, cross-language checks, mutations, and evolution.

## Protocol module

The protocol module is a deep handwritten boundary. Request preparation is
pure:

```text
request -> prepared request or PrepareError
```

A prepared request has passed deterministic validation and serialization.
Preparing it performs no network I/O and does not require credentials.

Keep provider-native request and response types private by default. Expose a
small project-owned interface rather than making callers understand wire
fields, validation dependencies, URL encoding, HTTP-library errors, or provider
failure envelopes.

Execution uses a private or internal transport seam when real variation or
focused testing requires one. Production uses an HTTP adapter.
Provider-specific response and failure decoding stays inside the protocol
module.

Do not publish a transport trait backed by only one implementation merely to
anticipate future variation. Local HTTP fixtures often test the real transport
behavior more directly.

## Authority and handwritten implementation

Rust types and functions implement wire facts, but they do not own them. A
wire-affecting change begins in the canonical OpenAPI contract, updates the
shared fixture expectation when behavior changes, and then updates every
handwritten conformer. Rust-only tests may add implementation coverage but must
not become the sole oracle for shared wire behavior.

Give each validation rule one semantic owner:

- OpenAPI owns structural constraints, requiredness, formats, enumerations,
  parameter serialization, and other supported protocol rules.
- Handwritten project policy owns only constraints OpenAPI cannot express
  truthfully, such as cross-provider acceptance policy, safety budgets, or
  semantic result selection.

Rust may encode OpenAPI-owned rules with types, Serde attributes, Garde, or
explicit validation. Those are conforming implementation mechanics, not an
independent authority. Do not repeat the same rule in a Rust-owned manifest or
fixture set. Translate all failures into project-owned errors at the protocol
interface.

## Shared conformance

The Rust test-only runner consumes every case in the provider's shared fixture
corpus and emits the repository's versioned canonical JSON projection. At
minimum, project the prepared method, path, parameters, relevant headers, media
type, and body; decoded success or provider failure; stable failure
classification; and shared validation issues.

Keep the runner credential-free and deterministic. It must not expose Rust type
names, dependency errors, map-order accidents, or display strings as shared
semantics.

CI verifies:

1. the canonical OpenAPI source and supported profile;
2. every Rust projection against its independent expected result;
3. exact differential equality with every other language conformer;
4. complete fixture identity coverage for all supported implementations; and
5. deterministic mutations that prove protected differences are detected.

Differential agreement cannot replace independent expectations because two
implementations can share a mistake. Rust-specific unit and property tests may
increase coverage but do not replace the shared corpus.

## Errors and command-line adapters

The protocol module distinguishes preparation, credential, transport, HTTP
status, provider-reported failure, and response-decoding errors as far as its
callers need to make different decisions. Callers never classify failures by
parsing display strings or dependency errors.

Public error variants and codes receive the compatibility guarantee of the
adopting interface. Internal errors may evolve more quickly, but
automation-facing command-line output remains explicitly versioned.

The command-line module is a thin process adapter. It parses invocation syntax,
calls the protocol module, and maps project-owned results and errors to a
structured envelope and stable exit status. It does not revalidate provider
semantics, reconstruct parameter paths, or decode provider bodies.

Agent- and automation-facing behavior follows
[Automation-Facing CLI Contracts](../../practices/automation-facing-cli-contracts.md).
Contract discovery and request preparation remain keyless and side-effect-free.

## Transport policy

The production HTTP adapter chooses redirects, retries, ambient proxies,
decompression, DNS, TLS, and response-size behavior explicitly. Review how
each choice affects credential scope, wire fidelity, idempotency, and
compatibility rather than inheriting library defaults accidentally.

For a credentialed fixed-origin protocol, add credentials only after validating
the allowed origin. Never forward them to an unapproved redirect or alternate
origin; disable redirects unless an explicit policy can preserve that
invariant. Retries require operation-level evidence that replay is valid.

Test the actual Rust transport independently against a local server for status,
headers, encoding, redirects, retries, size limits, timeouts, decompression,
malformed responses, and redaction as applicable. Include positive controls
that prove safeguards distinguish unsafe behavior. A TypeScript or other
language transport passing its tests provides no evidence for Rust transport
behavior.

Dependency upgrades that can change transport or parsing behavior renew these
focused tests.

## Reference Rust technology profile

Projects use the same default library for the same role unless a documented
constraint requires an exception:

- `serde` and format-specific adapters implement wire conversion.
- `reqwest` is the default production HTTP adapter.
- `tokio` is the default asynchronous runtime for network execution.
- `thiserror` defines concrete project-owned error enums.
- `secrecy` and `zeroize` protect credential-bearing values.
- a standards-compliant URL encoder owns query serialization.

Runtime-independent preparation does not require an HTTP client or asynchronous
runtime. Public crates may feature-gate the production transport adapter.

Garde is optional private machinery. It may implement field, aggregate, or
cross-field rules when its derive and reporting remove meaningful handwritten
complexity. Whether implemented through Garde or explicit code, OpenAPI-owned
rules remain subordinate to the shared conformance suite. Convert Garde reports
into project-owned errors at the protocol interface.

## Adoption and migration

An adopting Rust project should:

1. inventory every current source of wire, validation, and error behavior;
2. establish the canonical OpenAPI contract and shared evidence corpus;
3. define the versioned canonical projection and independent expectations;
4. bring the handwritten Rust protocol module into conformance;
5. test the real Rust transport independently;
6. add differential comparison when another language exists;
7. cut over once; and
8. delete superseded Rust wire authorities, duplicated fixture sets, and
   generated client pipelines.

Migration constraints may change sequencing. They do not justify permanent
parallel authorities.

Provider selection, bounded observations, and production enablement follow
[External Provider Qualification](../../practices/external-provider-qualification.md).

## Revisit when

Reconsider the implementation machinery when handwritten conformance cannot be
maintained truthfully or economically. Preserve the canonical OpenAPI wire
authority, independent shared evidence, protocol boundary, and Rust-specific
transport-safety proof even if the client implementation technique changes.
