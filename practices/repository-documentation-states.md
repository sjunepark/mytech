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

Prefer:

- one canonical explanation with links from other docs;
- paths to entry points instead of file-by-file inventories;
- stable identities and invariants instead of volatile counts;
- concise examples that illustrate a contract; and
- links to source code for implementation details discoverable there.

Avoid duplicating DTOs, function lists, directory inventories, test totals,
dependency versions, and transient milestone status.

## Plans and progress

Maintain active plans in place. Keep current decisions, completed work,
validation, blockers, and the next action. Compress prior execution notes rather
than appending session transcripts.

Close or archive a plan when its remaining information belongs in current
architecture, a runbook, or a decision record.

## Decision records

Create a decision record when a choice is costly to reverse or easy for a
future maintainer to undo accidentally. A useful record answers:

- what was decided;
- why the alternatives were rejected;
- what consequences and boundaries follow; and
- what evidence would justify revisiting it.

Do not use decision records as implementation status trackers.

## Mechanical checks

Where documentation is a contract, validate it. Useful checks include:

- link and Markdown validation;
- frontmatter or schema validation;
- generated-document freshness;
- public package-content checks; and
- tests that compare documented command or protocol examples with behavior.

## Revisit when

Add a new documentation category only when existing states cannot express a
concrete body of information. Remove or merge categories that readers cannot
distinguish in practice.
