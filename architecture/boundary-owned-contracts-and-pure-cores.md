---
status: accepted
---

# Boundary-Owned Contracts and Pure Cores

**Initial evidence:** OpenDART, Creo, Seoro, Unslide

## Decision

Keep deterministic domain and transformation logic in a pure core. Put I/O,
framework integration, parsing, authorization, persistence, and process behavior
behind explicit boundary modules.

Each boundary owns the contract it promises to the rest of the project. Decode
unknown input once, translate dependency behavior into project-owned types, and
let callers depend on those types rather than on framework or library internals.

## Boundary responsibilities

Validate data whenever it crosses a trust, process, persistence, or compatibility
boundary. Typical boundaries include:

- HTTP requests and provider responses;
- command-line arguments, environment, stdin, stdout, and exit status;
- persisted documents and configuration;
- desktop IPC and preload bridges;
- generated artifacts and extension manifests; and
- database rows returned through a runtime mapping.

Boundary validation establishes structural validity. Domain logic still owns
semantic rules, and the database still owns persisted integrity. Give each rule
one authoritative owner rather than repeating it in every layer.

Reject unsupported versions, unknown fields, unsafe paths, ambiguous identities,
and invalid state transitions when accepting them would create a second
interpretation. Preserve genuinely unknown external values when rejecting them
would invent a contract the source does not provide.

## Project-owned contracts

Public and cross-module interfaces use project-owned:

- request, response, and domain values;
- validation issues with stable codes or classifications;
- error categories;
- operation and artifact identities; and
- result envelopes when a process boundary is involved.

Translate dependency types where semantic ownership or compatibility promises
change. An HTTP client, ORM, Electron object, or UI framework must not become
the accidental vocabulary of unrelated callers. Modules intentionally sharing
an internal runtime may use its types directly; Effect-returning application
services do not need wrappers between every module. A stable standard type
does not need a project-owned copy merely to rename it.

Human-readable messages are diagnostics, not control-flow identifiers. Callers
must not parse display strings or dependency errors to decide retry, recovery,
exit status, or user-visible state.

## Pure core

Prefer pure functions for:

- normalization and canonicalization;
- request preparation before authorization or transport;
- document transformations and derived projections;
- scheduling and policy decisions from already validated facts; and
- mapping between boundary values and domain values.

The pure core should not acquire credentials, read ambient configuration, open
connections, start runtimes, or write files. Those actions belong to explicit
services composed at an application boundary.

Keep distinct forms of state separate. Authored state, execution state,
presentation state, and machine-local state usually have different lifecycles
and portability guarantees. Do not place them in one document merely because
one screen uses them together.

## Adapters and services

An adapter should be thin enough that its primary work is translation:

```text
external or framework value
            |
            v
validate and translate
            |
            v
project-owned application operation
            |
            v
translate result or typed failure
```

Create a service or pluggable seam when it hides a substantial capability,
owns a real resource lifetime, or has proven variation. Do not wrap every
dependency in an interface or publish an adapter system backed by only one
implementation.

## Enforcement

Where a boundary matters repeatedly, enforce it with import restrictions,
types, schemas, generated-code checks, or focused tests. Documentation should
explain why the boundary exists; tooling should prevent routine violations.

## Revisit when

Deepen or split a boundary when independent consumers need different
compatibility promises, when a second implementation proves actual variation,
or when a process boundary becomes necessary for deployment or security.
Do not introduce a network or plugin boundary only to anticipate those needs.
