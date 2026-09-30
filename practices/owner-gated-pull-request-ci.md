---
status: accepted
---

# Owner-Gated Pull Request CI

## Decision

In GitHub repositories the owner maintains, run pull request CI automatically
only for pull requests the owner opened, currently GitHub user `sjunepark`.
Pull requests from anyone else do not run CI automatically; the owner reviews
them first and runs CI deliberately, for example through `workflow_dispatch`
or by pushing the reviewed change to an owner branch.

Enforce this in two layers:

- Gate every job on a trigger `pull_request` (never `pull_request_target`) with
  a job-level `if` that requires the pull request author, `github.actor`, and
  `github.triggering_actor` to be the owner, and the head repository to be the
  base repository. Checking the triggering actor stops a re-run by someone
  else from reusing an owner-authored event. Reusable workflows repeat the
  gate so a new caller cannot bypass it.
- Set the repository's fork pull request workflow approval to require approval
  for all external contributors, so fork runs do not start without the owner.

A skipped job satisfies a required status check, so do not make the gated jobs
themselves the merge gate. Require a status that only a completed owner run
reports, such as a commit status the workflow writes for the validated SHA.

This limits spending on paid runners and keeps untrusted code away from
workflow secrets and caches. It does not replace
[verification from source to consumer](verification-from-source-to-consumer.md)
or the [platform coverage](cost-aware-ci-platform-coverage.md) required before
merging an external contribution.

Initial evidence: `cpaikr/darty` CI workflows.

## Revisit when

Reconsider when trusted collaborators regularly open pull requests and need
unattended feedback, when a merge queue or GitHub setting provides the same
author-based control more simply, or when CI no longer uses paid runners or
secrets that justify withholding automatic runs.
