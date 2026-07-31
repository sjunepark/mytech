---
status: accepted
---

# External HTTP Contracts and Rust SDKs

**Initial evidence:** OpenDART, Seoro

## Decision

Rust clients of external HTTP providers expose provider behavior through a
project-owned protocol module. Choose the repository authority for that
behavior from current needs:

- Use the Rust protocol module directly when all current semantic consumers are
  Rust and no independently useful OpenAPI artifact exists.
- Use OpenAPI when an authoritative provider specification, a current non-Rust
  or public consumer, or concrete standards-based tooling gives the contract an
  independent purpose outside the Rust implementation.

Direct Rust is the default for Rust-only integrations. Possible future
languages, a verifier created only to justify the specification, or generation
for its own sake do not earn an OpenAPI authority.

OpenAPI, code generation, a custom contract compiler, and a shared compiler are
separate decisions. Using OpenAPI does not require all three. Each additional
layer must remove demonstrated duplication or serve a named consumer.

Give each provider integration one repository authority. Do not maintain
handwritten Rust and project-authored OpenAPI as co-equal definitions of the
same supported wire behavior. Provider documentation and bounded observations
remain external evidence in either path; they are not a second repository
contract.

The authority choice does not change the caller-facing shape. A small protocol
module still owns request preparation, execution, provider response decoding,
and project-owned errors. Public exposure, supported operations, provider
semantics, and migration order remain project-specific.

## Scope

This decision governs:

- choosing the repository authority for an external provider integration;
- organizing and verifying provider evidence and fixtures;
- deciding whether OpenAPI, generation, or a compiler is justified;
- validating requests and decoding responses;
- structuring SDK and command-line errors;
- separating provider protocols from application domains; and
- testing the protocol module and transport.

It does not define:

- an application domain model shared by unrelated providers;
- product-specific retry, caching, ingestion, or persistence policy;
- which provider operations a project supports; or
- whether a Rust protocol module is public or internal.

## Choose the repository authority

The provider owns the external protocol. The repository owns its selected,
tested representation of the subset it supports. These are different kinds of
authority: provider sources and observations inform compatibility, while one
repository path owns implementation changes.

Use the following current-state test:

| Condition | Repository authority |
| --- | --- |
| All semantic consumers are Rust and no independent standard artifact is needed | Rust protocol module |
| The provider publishes a trustworthy, usable OpenAPI specification | Pinned OpenAPI contract |
| A public or non-Rust consumer needs the HTTP contract | Project-owned OpenAPI contract |
| Current documentation, mocking, gateway, or compatibility tooling specifically requires OpenAPI | OpenAPI contract, while that need remains real |
| Another language might be added later | Rust protocol module until that consumer exists |

Command-line and ingestion executables written in Rust are consumers of the
same Rust module, not independent contract consumers. Likewise, an OpenAPI
compiler or verifier created solely to consume a new OpenAPI file does not make
the file independently useful.

Record the reason for choosing OpenAPI. Revisit it when the named consumer or
tool disappears rather than retaining a permanent representation by inertia.

## Direct Rust target shape

Use this shape for a Rust-only integration without an independently justified
OpenAPI contract:

```text
Official documentation + bounded observations
                         |
                         v
                 Rust protocol module
                 - provider-native types
                 - serialization
                 - validation
                 - pure request preparation
                 - transport execution
                 - response and error decoding
                         |
                +--------+---------+
                |                  |
                v                  v
          Command-line adapter   Application or internal SDK
```

The Rust module is the repository authority for supported wire behavior. Rust
types express structure and requiredness, serialization code expresses wire
representation, and validation code expresses accepted values and
relationships. Doc comments explain semantics, provenance, unknowns, and
non-obvious decisions; they do not replace enforceable types or validation.

Keep provider-native request and response types private by default. Expose a
small project-owned interface rather than making callers understand wire
fields, validation dependencies, URL encoding, HTTP-library errors, or provider
failure envelopes.

Independently justified fixtures and request examples test the Rust authority.
They are evidence and test oracles, not a parallel contract definition. Do not
derive every test vector from the same Rust metadata it verifies.

## OpenAPI target shape

Use this shape only when OpenAPI has a named independent purpose:

```text
Official specification or reviewed provider evidence
                         |
                         v
               Canonical OpenAPI contract
               - provenance and support manifest
               - independently justified fixtures
                         |
                         v
             Optional generation or compilation
               - deterministic Rust derivatives
               - freshness verification
                         |
                         v
                 Rust protocol module
                         |
                +--------+---------+
                |                  |
                v                  v
          Command-line adapter   Application or public SDK
```

The OpenAPI contract is authoritative for the repository-supported wire facts.
Handwritten Rust owns only behavior that is deliberately outside that
contract. Generated Rust is private by default and never becomes a second
editable authority.

When the Rust implementation is handwritten, a contract-to-protocol
conformance check reconciles its observable operation coverage, serialization,
validation, and decoding with OpenAPI. This replaces generated-file freshness;
it does not make the Rust implementation a second authority.

A typical project-owned package may contain:

```text
contracts/<provider>/
  openapi.yaml
  manifest.yaml
  fixtures/
  generated/
    openapi.bundle.yaml
```

Names may follow local conventions, but roles remain distinct:

- `openapi.yaml` is the reviewed contract or pinned provider specification.
- `manifest.yaml` records provenance, supported scope, known unknowns, and
  policy OpenAPI cannot express cleanly without redefining its schemas.
- `fixtures/` contains externally justified success and failure examples.
- `generated/` contains reproducible derivatives and is never edited manually.

Unknown behavior stays unknown. Do not invent response fields, pagination
rules, status semantics, or error shapes to make OpenAPI or generation easier.

## Generation and compilers

Generation is justified when it removes mechanical transcription from an
OpenAPI authority. Generate facts such as:

- provider-shaped wire types;
- request parameters and serialization;
- schema-derived validation;
- response dispatch and decoding metadata;
- operation and rule metadata; and
- generated-file freshness checks.

Keep project policy and ergonomics handwritten:

- the deliberately supported public or internal interface;
- credential acquisition and secret handling;
- transport limits, retries, and timeouts;
- repository safety bounds;
- semantic rules outside the provider wire contract;
- translation into an application domain model; and
- command-line presentation.

Use a direct existing generator or a small project-owned generation step when
it satisfies the concrete contract. Build a custom compiler only after real
specifications repeatedly require the same loading, resolution, normalization,
unsupported-feature diagnostics, and deterministic output policy.

A shared compiler is earned when multiple consumers need the same policy-free
normalized model and conformance behavior. One specification and one output do
not by themselves establish that seam.

When a compiler is justified, keep its interface small:

```text
canonical OpenAPI contract -> normalized model or structured diagnostics
normalized model           -> deterministic artifacts
```

Unsupported or ambiguous constructs fail with source locations. Never
approximate them silently. Correct poor generated output in the contract,
normalized model, or generator rather than adding a permanent handwritten
compatibility layer.

## Protocol module

Both authority paths converge on the same deep module. Request preparation is
pure:

```text
request -> prepared request or PrepareError
```

A prepared request has passed deterministic validation and serialization.
Preparing it performs no network I/O and does not require credentials.

Execution uses a private or internal transport seam when real variation or
focused testing requires one. Production uses an HTTP adapter. Provider-specific
response and failure decoding stays inside the protocol module.

Do not publish a transport trait backed by only one implementation merely to
anticipate future variation. Local HTTP fixtures often test the real transport
behavior more directly.

## Validation

Give each validation rule one owner.

For direct Rust, encode structural invariants in types where practical and own
remaining field, aggregate, or cross-field rules in the protocol module. Garde
or explicit validation may implement those rules privately.

For OpenAPI, generate schema-owned validation when generation is part of the
chosen path. Handwritten validation owns only project policy or semantics that
the OpenAPI authority does not claim. Do not repeat schema rules as independent
handwritten attributes.

Translate validation failures into project-owned errors. Machine-facing
interfaces use stable classifications or rule codes and parameter paths when
callers need that detail. Human-readable messages are diagnostics, not
identifiers. Error details must not expose credentials, authenticated
coordinates, or unsafe request values.

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
decompression, DNS, TLS, and response-size behavior explicitly. Review how each
choice affects credential scope, wire fidelity, idempotency, and compatibility
rather than inheriting library defaults accidentally.

For a credentialed fixed-origin protocol, add credentials only after validating
the allowed origin. Never forward them to an unapproved redirect or alternate
origin. Retries require operation-level evidence that replay is valid.

Compatibility tests include positive controls proving that safeguards can
distinguish unsafe behavior. Dependency upgrades that can change transport or
parsing behavior renew those focused tests.

## Verification

Both paths use independent evidence so the implementation is not its only
oracle:

1. Verify provider provenance, selected operations, known unknowns, and safety
   policy.
2. Test independently justified request examples and response fixtures.
3. Test observable preparation and decoding through the protocol module's
   interface.
4. Exercise the production transport against a local server for status,
   headers, encoding, size limits, timeouts, and malformed responses.
5. Test the public SDK or command-line contract without reaching past its
   interface.
6. Use bounded, credential-aware live probes to detect drift without making
   them the sole merge gate.

The OpenAPI path additionally verifies source linting, reference resolution,
unsupported constructs, and either handwritten implementation conformance or
generated output freshness. Do not add those layers to direct Rust merely to
make the verification portfolios look symmetrical.

Fixtures generated from Rust or a normalized model may increase coverage, but
they do not replace independently justified examples.

Provider selection, bounded observations, and production enablement follow
[External Provider Qualification](../../practices/external-provider-qualification.md).

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

Garde is optional private machinery. In direct Rust it may own field,
aggregate, or cross-field rules when its derive and reporting remove meaningful
handwritten complexity. In an OpenAPI-generated path, schema-derived Garde
attributes must be generated rather than independently repeated. Convert Garde
reports into project-owned errors at the protocol interface.

## Adoption and migration

An adopting project should:

1. inventory every current source of wire, validation, and error behavior;
2. choose Rust or OpenAPI from current consumers and tooling, then name the one
   repository authority;
3. establish independently justified fixtures and provenance;
4. introduce the selected path behind the protocol module's interface;
5. use temporary parity checks only when replacing an existing path;
6. cut over once and delete superseded models, validators, generators,
   fixtures, and tests; and
7. keep project-specific milestones in the project's own plan.

When collapsing project-authored OpenAPI into direct Rust, move useful fixtures
and behavior tests before deleting the OpenAPI source, generated artifacts,
compiler, and OpenAPI-only tooling. When a real independent consumer later
earns OpenAPI, migrate deliberately from the existing provider evidence and
supported behavior rather than maintaining both authorities indefinitely.

Migration constraints may change sequencing. They do not justify permanent
parallel authorities.

## Revisit when

Reconsider the authority when a current non-Rust or public consumer appears,
an authoritative provider specification becomes usable, standards-based
tooling becomes materially valuable, or OpenAPI generation obscures rather
than removes work. Keep the protocol module and independent evidence whichever
representation owns the contract.
