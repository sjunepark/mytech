---
status: accepted
---

# External Provider Qualification

**Initial evidence:** OpenDART, Creo, Seoro

## Decision

Qualify an external provider in distinct stages:

1. provider and rights suitability;
2. documented wire-contract readiness;
3. bounded observational evidence;
4. client or adapter conformance; and
5. production enablement.

Passing one stage does not imply the next. A complete client does not authorize
production traffic, and successful requests do not establish content reuse
rights, capacity, historical coverage, or stable undocumented behavior.

## Evidence labels

Classify every consequential provider claim as one of:

- **documented** — stated by an authoritative provider source;
- **observed** — produced by a dated, bounded probe;
- **inferred** — a reviewable conclusion from other evidence;
- **project decision** — policy selected by the adopting project; or
- **unknown** — not established.

Do not convert prose, examples, current implementation behavior, or one
successful response into a stronger contract without evidence.

Keep contradictions and provenance visible. Preserve unknown fields and future
values when the provider permits them. Do not invent pagination closure, status
semantics, response fields, or successful-empty behavior to simplify a client.

## Contract readiness

The repository-owned contract should state what the project supports, not
everything the provider might do. It must distinguish provider-native facts
from client policy.

Use independently authored fixtures and examples. Generated fixtures can add
coverage but cannot certify the contract or implementation that produced them.

Contract verification remains credential-free and offline. Production
credentials are never required to validate evidence, prepare requests, or test
the ordinary merge path. OpenAPI validation, bundling, shared conformance,
differential comparison, mutation tests, and local generated-artifact freshness
checks also remain credential-free. Checking whether a live provider changed
belongs to bounded observation, separate from the ordinary merge gate.

## Bounded probes

Before resolving a credential or making a request, fix:

- the allowed origin and operation set;
- request inputs and maximum attempt count;
- pacing, time, and byte budgets;
- assertions and stop conditions;
- permitted output fields; and
- sanitization and retention policy.

Run a preflight that proves those bounds without a credential. Probes should
avoid automatic retries, discard raw bodies when they are not approved
evidence, and emit only a versioned bounded report.

Credentials remain opaque. Resolve them only inside a fixed launcher or
similarly constrained boundary, expose only the value the child needs, and
never print, inspect, or persist them or a credential-bearing URL. If a provider
requires query-string authorization, construct that URL only inside a
fixed-origin, redirect-safe transport, keep it ephemeral, and redact it from
errors and telemetry.

## Privilege separation

Separate observation from mutation when automation needs both:

```text
credentialed or network-capable producer
        |
        v
bounded sanitized report
        |
        v
no-secret validator/notifier with narrow write authority
```

The producer should not receive issue, deployment, or repository mutation
authority merely because it holds a provider credential. The notifier should
not receive that credential. Validate the report against trusted code before
using it to mutate external state.

## Production gate

Production enablement requires explicit decisions about:

- terms, attribution, retention, and content reuse;
- credentials and account ownership;
- quotas, pacing, concurrency, and cost;
- retry and ambiguity handling;
- monitoring, drift detection, and incident ownership; and
- acceptable provider outage or withdrawal behavior.

Provider registration, terms acceptance, paid use, and production activation
remain human-owned actions unless the user explicitly delegates them.

## Related guidance

Use
[External HTTP Contracts and Handwritten Clients](../architecture/external-http/external-http-contracts-and-handwritten-clients.md)
to select a proportionate wire authority, contain SDK or client behavior,
and define independent conformance evidence.
Use [External Request Pacing](external-request-pacing.md) for default pacing,
its cross-process scope, and interval configuration.

## Revisit when

Relax a bound only after production-shaped evidence establishes the need and
the provider contract permits it. An observed behavior may become supported,
but the evidence and compatibility consequence must remain explicit.
