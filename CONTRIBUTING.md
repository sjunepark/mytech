# Contributing

Use this guide when maintaining mytech. The [README](README.md) routes readers
to technical preferences; this document owns their authoring and validation
contract.

## Choose a home

Choose a document's location by what it owns:

| Location | Responsibility |
| --- | --- |
| `architecture/` | Boundaries, authority, and contracts across components |
| `libraries/` | Choices and constraints for individual libraries, grouped by language |
| `practices/` | Engineering, verification, and delivery practices |
| `stacks/` | Combinations of technologies for a defined application or workload |
| `draft/` | Proposed preferences with unresolved scope or tradeoffs |
| `reference/` | Research, dated observations, reviews, and tool usage instructions |
| `history/` | Brief dated rationale for meaningful preference changes |

Keep navigation shallow. Add a category only when concrete content needs it.
Update the README decision index for accepted guidance, the
[draft index](draft/README.md) for proposals, and the
[reference index](reference/README.md) for supporting material. Link shared
rules to their owning document instead of copying them into each topic.

## Guidance document contract

Guidance starts with exactly this restricted frontmatter form:

```yaml
---
status: accepted
---
```

Use `status: draft` for proposals. No other frontmatter fields are supported.
The body starts with a level-one title; required sections are level two.

- `accepted` belongs in `architecture/`, `libraries/`, `practices/`, or `stacks/`
  and requires `Decision` and `Revisit when` sections.
- `draft` belongs under `draft/` and requires `Tentative preference`,
  `Why this is uncertain`, `Promotion questions`, and `If accepted` sections.
- Routing READMEs, references, and history are outside this lifecycle schema.

Each guidance document owns one coherent preference with its rationale,
applicability, and stable constraints. Project procedures, delivery plans, and
historical evidence belong elsewhere. Initial-evidence project names record
provenance; they do not prove those projects currently implement the guidance.

## Maintenance

Update guidance in place. Re-distill overlapping preferences rather than
concatenating them and update their consumers. Create history entries only for
meaningful preference changes: preserve the rationale in a brief dated
`history/` file mirroring the guidance path. Git retains exact diffs.

Promote a draft when its scope and tradeoffs are resolved, not merely because
it appeared in more repositories.

## Skill ownership

`skills/` contains repository-owned, distributable skills for other projects.
`.agents/skills/` and `.claude/skills/` contain installed skill dependencies used
while working here. `sjskills.toml` selects their profile, and
`.sjskills/state.json` records their source provenance. Maintain installed
packages in their source repositories.

## Validation

Use Python 3.10 or newer and `uv` (providing `uvx`). The lint wrapper selects its
pinned rumdl version and may download it on first use. Run:

```sh
./scripts/validate-guidance
./scripts/query-unsettled-guidance
```

Validation checks guidance placement and headings, runs script regression
tests, and lints repository-owned Markdown including relative links. Installed
skill dependencies are excluded; distributable sources under `skills/` remain
in scope. The query emits one JSON document listing drafts and invalid lifecycle
metadata or placement; it does not replace full validation. Neither command
verifies external links or the
truth of technology claims. Checks currently run locally; this repository has
no configured CI gate.
