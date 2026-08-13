---
status: accepted
---

# Clap for Rust Command-Line Interfaces

**Initial evidence:** clap derive in dsd2md; clap builder API in OpenDART

## Decision

Use clap as the default parser for Rust command-line interfaces. Prefer its
derive API for a typed command model, enum subcommands, validation, and generated
help. Use the builder API when the command schema is genuinely dynamic rather
than duplicating a static schema imperatively.

Keep execution, process output, and application behavior outside the parser
types. Add `clap_complete` or `clap_mangen` when completion scripts or man pages
are part of the product. For commands used by agents or automation, follow
[Automation-Facing CLI Contracts](../../practices/automation-facing-cli-contracts.md).

Use lexopt only when binary size, compile cost, unusual ordering, or an
intentionally small dependency surface justifies manually owning help,
subcommands, validation, and completion. That is an explicit minimal-parser
tradeoff, not a second general default.

## Revisit when

Reconsider clap when its build or binary cost is material to the distributed
artifact, or when a command grammar is substantially clearer in a smaller
imperative parser. Evaluate bpaf when parser composition is a concrete need;
do not adopt it solely to reduce dependency size.
