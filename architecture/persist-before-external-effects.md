---
status: accepted
---

# Persist Before External Effects

**Initial evidence:** implemented paid-operation recovery in Creo; accepted
messaging and worker targets in Seoro

## Decision

When an operation combines durable business state with a costly, retryable, or
user-visible external effect, persist enough intent and recovery state before
depending on delivery.

The database owns durable progress. A scheduler, request process, provider
response, realtime channel, or worker memory may trigger work, but it is not the
authority for whether work is due, completed, charged, or recoverable.

## Operation identity

Give each retriable operation a stable idempotency key and, when payload
equivalence matters, a request fingerprint. A repeated key with the same
fingerprint may return or resume the existing outcome. The same key with
different input must fail rather than silently reusing unrelated work.

Record only the metadata required for control, accounting, and diagnosis.
Prompts, response bodies, credentials, and other sensitive payloads should not
become operational state unless the product explicitly requires their retention.

## Commit before fan-out

For messages, notifications, indexing, or other follow-on delivery, commit the
domain change and an outbox record in the same transaction. A dispatcher
processes committed records outside the user request and may retry safely.

Consumers reconcile from durable history and tolerate duplicate or missed
delivery events. Delivery infrastructure is replaceable and cannot become a
second source of domain truth.

## Costly provider operations

When an external call may incur cost or produce an irreversible result:

1. validate authorization, policy, quota, and idempotency;
2. persist an admitted operation with its safe identity and accounting basis;
3. perform the bounded external call;
4. finalize the durable result and append accounting entries; and
5. enqueue durable recovery if external success is known but finalization
   cannot complete.

Exact retries must not repeat the upstream call or debit. Ambiguous failures
need an explicit reconciliation policy; broad automatic retry is not a safe
default.

Prefer append-only accounting records with correction entries over mutable
balances. Cached balances are derived read models until measured query needs
justify them.

## Durable workers

For database-backed asynchronous work, persist claims, attempts, retry
eligibility, checkpoints, and terminal dispositions. A timer should only wake
the worker to ask the database what is due.

Classify failures according to the decision the worker must make, such as
retry, skip, reconcile, or abort. Do not treat every I/O error as retryable.

## Boundaries

Keep domain ownership separate from delivery adapters:

- application modules decide what state change is valid;
- the database transaction records durable intent and recovery;
- workers own retry and settlement;
- realtime, notification, search, or provider adapters perform delivery; and
- clients reconcile against durable state.

## Revisit when

An in-process action without cost, recovery, or cross-system delivery may not
need durable operation state. Introduce this pattern when failure between
commit and delivery would otherwise lose work, duplicate cost, or leave an
outcome impossible to classify.
