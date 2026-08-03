---
status: accepted
---

# Repository Documentation States

**Initial evidence:** OpenDART, Creo, Seoro, Unslide

## Decision

Organize documentation by authority and state. Readers should be able to tell
whether a statement describes implemented behavior, accepted target design,
an active plan, exploratory evidence, or historical rationale.

Do not combine these states in one growing project diary.

## Document roles

Use the smallest subset a repository needs:

- **README** routes readers to the correct source and lists supported commands.
- **ARCHITECTURE** maps implemented boundaries, flows, and invariants.
- **Target or product docs** describe committed intent that is not yet current.
- **Decision records** preserve costly choices, rationale, consequences, and
  revisit conditions.
- **Current runbooks** document implemented operation and debugging.
- **Plans or goals** own temporary delivery sequence, validation, blockers, and
  next action.
- **Research** preserves evidence and unresolved alternatives.
- **History** explains why an active preference changed when that rationale
  remains useful.

Names may follow local conventions. The states must remain distinguishable.

## Truthful language

Use present tense only for implemented current behavior. Mark accepted target
design explicitly; accepted does not mean delivered.

Proposed or open decisions are not architecture. Plans may reference them, but
current docs must not silently assume their outcome.

When a decision becomes authoritative, compress the research to the evidence
worth retaining and link to the decision. When implementation lands, update the
current architecture and runbooks instead of leaving the result trapped in a
completed plan.

## Progressive disclosure

Keep parent documents to routing, system-wide invariants, and high-signal
orientation. Put subsystem details near the code or ownership boundary they
describe.

Prefer one canonical explanation, paths to entry points, stable identities and
invariants, and concise contract examples. Link to source code for discoverable
implementation details.

Avoid duplicating DTOs, function lists, directory inventories, test totals,
dependency versions, and transient milestone status.

## Lifecycle

Maintain active documents in place and update their consumers when the truth
changes. Remove superseded active documents and preserve only useful rationale
through the repository's history convention.

Keep a stable path while its subject remains the same. Rename it when the old
path would misrepresent the current decision rather than maintaining a redirect.

Keep plans to current decisions, completed work, validation, blockers, and the
next action; compress execution transcripts and close a plan once its durable
content belongs in architecture, a runbook, or a decision record.

Use decision records for choices that are costly to reverse or easy to undo
accidentally. Record the decision, rejected alternatives, consequences, and
revisit evidence, but not implementation status.

## Mechanical checks

Mechanically validate documentation that consumers depend on, including its
links, schema, generated freshness, published contents, or executable examples
as applicable.

## Revisit when

Add a new documentation category only when existing states cannot express a
concrete body of information. Remove or merge categories that readers cannot
distinguish in practice.
