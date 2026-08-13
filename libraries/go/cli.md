---
status: accepted
---

# Kong for Go Command-Line Interfaces

**Initial evidence:** custom parsing in Baton; standard-library `flag` in
gitlog-html and OpenDART

## Decision

Use Kong as the default parser for Go command-line interfaces. Define commands,
arguments, flags, defaults, environment bindings, and validation as typed nested
structs so the command model stays compact and inspectable.

Keep execution, process output, and application behavior outside the parser
types. For commands used by agents or automation, follow
[Automation-Facing CLI Contracts](../../practices/automation-facing-cli-contracts.md).

Use urfave/cli v3 when first-party multi-shell completion is a baseline
requirement and an explicit command tree is preferable to Kong's static struct
model. It is the general-purpose fallback, not a parallel default; use the v3
API and do not copy the abundant older-version examples.

Use Cobra when generated man or Markdown documentation, dynamically assembled
commands, broad contributor familiarity, or an integration built around the
Cobra ecosystem outweighs its additional wiring. Do not add Viper
automatically; configuration is a separate concern and should earn its own
dependency and precedence model.

Use the standard-library `flag` package for a small single-command utility when
manual help and validation remain simpler than adopting a command framework.

## Revisit when

Prefer urfave/cli v3 as the general default if shell completion becomes a
baseline requirement across most Go CLIs. Prefer Cobra instead if generated
reference documentation or its ecosystem becomes the recurring requirement.
Reconsider Kong if its struct tags obscure the command model or applications
increasingly require commands assembled at runtime.
