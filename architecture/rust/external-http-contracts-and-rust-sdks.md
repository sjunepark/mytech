# External HTTP Contracts and Rust SDKs

**Status:** Accepted  
**Initial evidence:** OpenDART, Seoro

## Decision

Rust clients of external HTTP providers use one contract-driven architecture.
Provider evidence is reconciled into a repository-owned canonical contract
package. Private tooling compiles that package into a normalized model and
deterministic Rust artifacts. A project-owned protocol module exposes request
preparation, execution, response decoding, and structured errors through a
small interface.

The architecture is shared. Public exposure, supported operations, provider
semantics, and migration order remain project-specific.

Current code does not define the target design. It only determines how a
project migrates to it.

## Scope

This decision governs:

- organizing and verifying provider contracts;
- generating Rust protocol code;
- validating requests and responses;
- structuring SDK and command-line errors;
- separating provider protocols from application domains; and
- testing the contract compiler, protocol module, and transport.

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
             Canonical contract package
             - repository-selected OpenAPI dialect
             - provenance and support manifest
             - independently authored fixtures
                         |
                         v
                Contract compiler
             - load, resolve, lint, bundle
             - reject unsupported constructs
             - produce a normalized model
                         |
                         v
              Deterministic derivatives
             - Rust wire and request types
             - serialization and validation
             - operation and rule metadata
                         |
                         v
                 Protocol module
             - prepare a request
             - execute through transport
             - decode provider responses
             - return project-owned errors
                         |
                +--------+---------+
                |                  |
                v                  v
          Command-line adapter   Application or public SDK
```

The canonical contract package is authoritative for what the repository claims
to support. It is not proof of undocumented provider behavior.

## Canonical contract package

Each provider contract uses this conceptual layout:

```text
contracts/<provider>/
  openapi.yaml
  manifest.yaml
  fixtures/
  generated/
    openapi.bundle.yaml
```

Names may follow local repository conventions, but the roles must remain
distinct:

- `openapi.yaml` is the reviewed canonical wire contract in the OpenAPI dialect
  selected and pinned by the repository. Each project declares whether its
  owning path is direct authoring or repository-controlled generation; changes
  go through that path.
- `manifest.yaml` records provenance, known unknowns, repository policy, and
  contract metadata OpenAPI cannot express cleanly. It references but does not
  redefine operations or schemas owned by OpenAPI.
- `fixtures/` contains independently justified success and failure examples.
- `generated/` contains reproducible derivatives and is never edited manually.

Official specifications are preferred evidence. When a provider does not
publish a complete specification, bounded observations may fill documented
gaps. Rust implementation behavior is never evidence for the contract it
implements.

Unknown behavior stays unknown. The contract must not invent response fields,
pagination rules, status semantics, or error shapes to make generation easier.

## Contract compiler

The compiler is a deep module with a small interface:

```text
canonical contract package -> normalized model or structured diagnostics
normalized model           -> deterministic artifacts
```

Its implementation owns OpenAPI loading, reference resolution, linting,
normalization, compatibility checks, and generation. Callers do not depend on
the OpenAPI parser's types.

The normalized model contains only concepts the generators support, including:

- operations and stable operation identifiers;
- parameter locations and serialization rules;
- request and response schemas;
- success and provider-failure responses;
- schema-derived validation rules;
- stable rule metadata and source provenance; and
- supported authentication requirements without credential values.

Unsupported or ambiguous OpenAPI constructs fail compilation with source
locations. They must not be approximated silently.

A shared compiler is earned when multiple consumers prove they need the same
policy-free normalized model and conformance contract. Until then, keep the
compiler project-owned and compare behavior through independently justified
fixtures rather than extracting around assumed variation.

## Generated and handwritten responsibilities

Generate facts that are mechanical consequences of the canonical contract:

- provider-shaped wire types;
- request parameters and serialization;
- schema-derived request validation;
- response dispatch and decoding metadata;
- operation discovery metadata;
- stable validation rule metadata; and
- contract and generated-file freshness checks.

Keep policy and ergonomics handwritten:

- the deliberately supported public or internal interface;
- credential acquisition and secret handling;
- transport limits, retries, and timeouts;
- repository safety bounds;
- semantic rules that are not part of the provider wire contract;
- translation into an application domain model; and
- command-line presentation.

Generated types are private by default. Public re-exports are deliberate and
receive the adopting project's compatibility guarantees.

Do not add a handwritten compatibility layer over poor generated output. Fix
the normalized model or generator so all consumers receive the correction.

## Protocol module

The protocol module hides contract and transport complexity behind a small
interface. Request preparation is pure:

```text
request -> prepared request or PrepareError
```

A prepared request has already passed contract validation, repository policy
validation, and deterministic serialization. Preparing it performs no network
I/O.

Execution accepts transport behavior through an internal seam. Production uses
an HTTP adapter; tests use a local or in-memory adapter. Provider-specific
response decoding remains inside the protocol module.

Callers must not need to understand OpenAPI, the normalized model, the
validation engine, URL encoding, HTTP-library errors, or provider error
decoding to use the module correctly.

## Validation

Validation has two explicit sources:

1. **Contract validation** is generated from OpenAPI and canonical contract
   metadata. It covers required values, formats, ranges, enumerations,
   serialization constraints, and schema relationships.
2. **Client policy validation** is handwritten. It covers repository safety
   bounds, credential availability, deliberately unsupported combinations,
   and other policy that is not a provider wire constraint.

Both sources produce project-owned validation issues:

```rust
struct ValidationIssue {
    code: ValidationCode,
    path: ParameterPath,
    message: String,
}
```

Rule codes and paths are stable machine-readable data. Human-readable messages
are not identifiers. Error details must not expose credentials, secret-bearing
headers, or unsafe request values.

Schema rules must not be repeated as independent handwritten validation
attributes. A handwritten semantic rule must have one owner and a stable rule
identifier.

## Errors

The protocol module owns its error taxonomy. A representative preparation
shape is:

```rust
enum PrepareError {
    InvalidRequest { issues: Vec<ValidationIssue> },
    MissingCredential { /* safe structured context */ },
    UnsupportedOperation { /* stable operation identity */ },
    Serialization { /* safe structured context */ },
}
```

Preparation, transport, HTTP status, provider-reported failure, and response
decoding are distinct failure categories. Callers never classify failures by
parsing display strings.

Public error variants and codes receive the compatibility guarantee of the
adopting interface. Internal errors may evolve more quickly, but command-line
machine output remains explicitly versioned.

The command-line module is a thin adapter. It maps structured protocol errors
to a structured envelope and stable exit status. It does not revalidate
requests, reconstruct parameter paths, or translate library error messages.

Agent- and automation-facing command-line behavior follows
[Automation-Facing CLI Contracts](../../practices/automation-facing-cli-contracts.md).
Contract discovery and request validation should remain keyless and
side-effect-free.

## Transport policy

The production transport adapter must choose its behavior explicitly. Do not
inherit HTTP-library defaults for redirects, retries, ambient proxies,
decompression, DNS, TLS, or response-size handling without reviewing how they
affect credential scope, wire fidelity, idempotency, and compatibility.

For a credentialed fixed-origin protocol, add credentials only after validating
the allowed origin. Never forward them to an unapproved redirect or alternate
origin; disable redirects unless an explicit policy can preserve that
invariant. Retries require operation-level evidence that replay is valid.
Transparent decoding is enabled only when callers do not need the original
entity bytes and headers.

Compatibility tests should include positive controls proving that safeguards
can distinguish the unsafe behavior. Dependency upgrades that can change
transport or parsing behavior renew those focused tests.

## Verification

Verification is layered so one implementation cannot certify itself:

1. **Source verification** lints OpenAPI, resolves references, checks the
   manifest, and rejects unsupported constructs.
2. **Independent contract verification** checks externally justified fixtures
   and request examples without using generated Rust as its oracle.
3. **Compiler verification** tests normalized output, deterministic generation,
   and failure diagnostics.
4. **Freshness verification** fails when committed derivatives differ from
   regenerated output.
5. **Protocol verification** tests observable preparation and decoding behavior
   through the protocol module's interface.
6. **Transport verification** uses a local HTTP adapter to exercise status,
   headers, compression, size limits, timeouts, and malformed responses.
7. **Consumer verification** tests the public SDK or command-line structured
   output without reaching past its interface.
8. **Bounded live probes** detect provider drift and collect new evidence. They
   are credential-aware, rate-limited, sanitized, and not the sole merge gate.

Fixtures generated from the normalized model may increase coverage, but they
cannot replace independently authored fixtures.

Provider selection, contract readiness, bounded observations, and production
enablement follow
[External Provider Qualification](../../practices/external-provider-qualification.md).

When a new interface-level test replaces tests of an obsolete validation or
serialization path, delete the old tests. Migration must replace duplicated
behavior rather than layer another path over it.

## Reference Rust technology profile

Projects adopting this architecture use the same default library for the same
role unless a documented constraint requires an exception:

- `serde` and format-specific adapters implement wire conversion.
- `reqwest` is the default production HTTP adapter.
- `tokio` is the default asynchronous runtime for network execution.
- `thiserror` defines concrete project-owned error enums.
- `secrecy` and `zeroize` protect credential-bearing values.
- a standards-compliant URL encoder owns query serialization.

Runtime-independent preparation must not require an HTTP client or asynchronous
runtime. Public crates may feature-gate the production transport adapter.

### Garde

Garde is optional implementation machinery, not part of the architecture's
interface and not a contract authority.

It may be used privately when its derive, nested validation, context, custom
rules, and aggregate reporting remove meaningful handwritten complexity.
Schema-derived Garde attributes must be generated from the canonical contract.
Any Garde report must be converted immediately into project-owned validation
issues.

Prefer direct generated validation when it produces stable typed rule codes
more clearly. Do not retain Garde merely for consistency, and do not introduce
it if doing so creates a second validation path.

Dependency versions and minimum supported Rust versions remain project release
decisions. Shared libraries should be aligned when their compatibility
requirements permit it.

## Adoption and migration

An adopting project should:

1. inventory every current source of contract and validation truth;
2. establish independently justified fixtures and provenance;
3. make the canonical contract package truthful before generating from it;
4. prove compiler parity against the existing verifier and protocol behavior;
5. introduce the generated path behind the existing protocol interface;
6. cut over once;
7. delete superseded models, validators, fixtures, and tests; and
8. keep project-specific milestones in the project's own plan.

Migration constraints may change sequencing. They do not weaken the target
invariants or create permanent parallel authorities.
