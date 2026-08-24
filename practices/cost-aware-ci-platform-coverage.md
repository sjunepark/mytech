---
status: accepted
---

# Cost-Aware CI Platform Coverage

## Decision

For GitHub Actions in organization-owned repositories, use
[Blacksmith](https://docs.blacksmith.sh/blacksmith-runners/overview) as the
default runner provider when it is available to the repository. Otherwise, use
a suitable GitHub-hosted runner.

Use the smallest runner size that completes the job reliably, normally 2 vCPU.
Choose operating system and CPU architecture for correctness; the cost default
concerns runner size. Increase the size only for a demonstrated resource need
or when measurements show that a larger runner lowers total job cost.

Separate routine development feedback from platform-compatibility gates:

- For pull requests targeting the normal development branch, usually `dev`,
  run ordinary verification on Linux only. Supporting Windows or macOS for
  distribution does not by itself justify testing them on each development PR.
- For pull requests targeting `main`, require verification on every operating
  system the project claims to support, including Windows and macOS when
  applicable. Include the equivalent merge-queue check when a merge queue is
  enabled.
- Do not repeat the same full platform matrix on the post-merge `main` push
  when the pull request gate already verified it, unless a project-specific
  risk requires post-merge evidence.

Release workflows must still build and verify every claimed distribution
target. Follow [Verification from Source to Consumer](verification-from-source-to-consumer.md)
and [Standalone CLI Distribution](standalone-cli-distribution.md) so reduced
development coverage does not weaken the compatibility promised to users.

## Revisit when

Reconsider the runner size when measurements show a different size has lower
total cost or the smallest runner is unreliable. Reconsider the branch-based
platform split when platform-specific defects are routinely discovered too
late, a protected-branch or release process cannot provide the full gate, or
runner pricing changes enough that the savings no longer justify delayed
coverage.
