---
status: accepted
---

# CLI Consumer Skills

**Initial evidence:** KASB, krx-cli, YTM, and darty consumer documentation and
available skill packages

## Decision

Ship a repository-owned skill package that helps an agent complete user tasks
with the installed CLI. Keep `SKILL.md` small enough for routine use: it owns
task selection, essential constraints, conditional resource links, and what
counts as a complete result. Load installation, configuration, detailed usage,
and recovery instructions only when the task requires them.

The skill supplies tool-specific judgment that command help cannot replace:
which operation answers the request, how identifiers and dates relate, when a
fallback changes the answer's meaning, and what evidence to report. Discover
exact syntax through the installed CLI's help or schema rather than copying
its entire command reference.

## Package and entry point

Keep each distributable skill in a named package under the repository's skill
directory. For a new `skill/` directory, a minimal shape is:

```text
skill/<cli-name>/
  SKILL.md
  references/
    installation.md
    usage.md
```

Retain existing published paths such as `skills/<cli-name>/` unless a migration
is intended. Consumer packages are separate from installed maintainer skills
under `.agents/skills/` or other client directories. Keep CLI use separate from
SDK integration and contributor setup when they have different prerequisites
and execution paths.

Use portable frontmatter with a directory-matching `name` and a `description`
that states the capability and when to use it. Preserve existing activation
policy; default new skills to explicit invocation. Broader discovery needs
representative implicit requests and near misses that demonstrate a reliable,
useful boundary. Put optional client controls in adapter metadata, with the
same activation intent in the portable description.

Give each bundled runtime resource a direct relative link from `SKILL.md` and
a concrete condition for reading it. Keep resources inside the package so an
installed copy works without the source checkout. Add authentication,
task-specific workflows, or troubleshooting files when they have a distinct
loading condition. The example tree is a starting point, not a required file
count; a short, cohesive CLI can keep routine usage in the entry point.

## Progressive loading

Organize by decisions that change what the agent needs to read:

| Surface | Owns | Load condition |
| --- | --- | --- |
| Description | Capability, activation intent, relevant exclusions | Skill selection |
| `SKILL.md` | Minimal execution path, universal constraints, routing, completion | Selected skill |
| Installation reference | Installation, PATH, verification, upgrade and installation recovery | CLI missing, unusable, demonstrably incompatible, or setup/upgrade requested |
| Authentication reference, if needed | Credential configuration and access diagnosis | Operation needs unconfigured access, or access setup/diagnosis is requested |
| Usage reference or task workflow | Operation selection, domain semantics, bounded examples, result interpretation | Request matches that task family |
| Troubleshooting reference, if needed | Known failure diagnosis and recovery | Observed failure matches its scope |

Establish executable usability with a cheap, keyless local check supported by
that CLI. Reuse a successful check from the current execution context; recheck
after an executable or environment change, or a relevant failure. First skill
use does not imply a missing installation. Authentication and provider failures
do not by themselves establish a broken executable.

If the executable works, continue directly to the relevant task guidance and
command-level help. Read top-level help when command selection is unclear.
Reserve full schema/catalog output for tasks that need it; avoid reading every
reference or dumping the complete interface before a narrow operation.

Keep the installation route conditional: if the executable is missing or needs
installation repair, read the linked installation resource; otherwise continue
to the matching usage route. Do not inline installer instructions or require
every invocation to read setup. Keep universal constraints visible even when
setup is skipped.

## Installation and access

Write the installation resource against the supported consumer path, following
[CLI Installation Guides](cli-installation-guides.md). Give an installed-skill
user a complete route to a verified executable without assuming a checkout,
developer toolchain, or credentials needed only for data access. Cover supported
prerequisites, platform branches, release locations, verification, PATH, and the
owning upgrade method.

Give installation facts one source owner. The README and skill resource can
share a canonical consumer guide through a stable external link, or the skill
can bundle a release-aligned projection with a drift check. Keep the conditional
decision and guide locator inside the package. A vague instruction to find
“the repository installation docs” or a filesystem link outside the package is
insufficient. If a linked guide is unavailable, report that boundary instead of
inventing an install command. Describe supported, obtainable channels; a
package-shaped artifact does not establish registry publication.

Treat executable installation, credential configuration, and service approval
as distinct states. Route only the missing requirement to its guide. Preserve
existing authorization; ask only when a necessary change exceeds it. An update
notice alone does not authorize an upgrade. Keep secrets out of responses and
logs, and let the tool's supported credential mechanism resolve them. Isolate
account or portal mutations behind their own explicit task route.

## Usage guidance

Teach the shortest reliable route from intent to a verified result. Include
examples where they resolve a non-obvious choice; discover exact options and
formats from the installed executable. State supported compatibility when the
workflow depends on a particular contract. Current checkout behavior does not
establish released behavior. Inspect current help after an unsupported flag
before considering an upgrade.

Preserve the tool's actual
[automation contract](automation-facing-cli-contracts.md): structured output
where available, exit-status meaning, output destinations, partial results,
and recovery metadata. Do not invent shared flags or success envelopes across
different CLIs. Bound broad queries and large outputs with supported filters,
limits, pagination, or artifact output.

Keep result-changing domain rules beside the task that uses them: exact versus
resolved dates, returned identifiers, missing-value semantics, partial coverage,
fallback authority, and source links. Distinguish confirmed absent data from
transport or protocol failure before retrying or changing the query. Define
completion using the requested evidence or artifact and remaining limitations,
not merely a successful process exit.

## Delivery and verification

Document how consumers obtain the skill separately from how they obtain the
executable. Verify the advertised skill installation path includes all runtime
resources. Keep one source owner; generate or check distributed copies rather
than maintaining competing versions by hand. Follow
[canonical-source guidance](../architecture/canonical-sources-and-derived-artifacts.md)
when projecting the skill into another distribution.

Check frontmatter, resource links, package closure, and compatibility with the
documented CLI contract. Exercise a copy outside the repository so missing
files, parent-relative links, and maintainer-environment assumptions are visible.
Keep evaluation fixtures and maintenance evidence outside the routine reading
path.

Evaluate changed instructions in fresh contexts against the prior skill, or
without a skill for a new package. Include these boundaries where applicable:

- Working CLI: complete a narrow task without loading installation material.
- Missing CLI: follow setup through verification, then resume the task.
- Missing access: load access guidance without reinstalling the executable or
  submitting unrequested service applications.
- Contract mismatch or provider failure: inspect relevant help or error evidence
  and select the appropriate recovery, preserving partial results.
- Specialized or large-result task: load only its required references and
  preserve domain semantics and output limits.

Record files read, commands attempted, resulting evidence, and failures. Compare
context loaded and task correctness; fewer words alone do not establish a better
skill. Test activation separately with intended requests and near misses when
the description or invocation policy changes. Static checks do not prove agent
behavior, and fixture trials do not prove installation against a live release.

## Revisit when

Revisit the split when repeated runs load irrelevant material, skip essential
constraints, or need to rediscover missing procedures. Revisit packaging and
compatibility when platforms, release channels, command contracts, or the
intended consumer change. Add a resource only when a distinct recurring decision
earns it.
