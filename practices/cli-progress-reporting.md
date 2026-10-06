---
status: accepted
---

# CLI Progress Reporting

**Initial evidence:** KASB (`kasb upgrade`)

## Decision

Report progress for short-running CLI operations as plain stage lines rather
than progress bars. An operation that takes a few seconds or transfers a few
megabytes reads best as a short sequence: `Checking for updates...`,
`Downloading kasb 0.6.0 (5.3 MB)...`, `Verifying...`, `Installing...`, then
the outcome. A bar earns its place only for long or large transfers, where rate
and remaining time help the reader.

## Streams and terminals

Structured output owns stdout under the
[automation contract](automation-facing-cli-contracts.md). Human progress goes
to stderr, and only when stderr is an interactive terminal. Pipes, CI, and
agents then see unchanged stdout and an empty stderr without passing a quiet
flag.

When a project documents an empty-stderr contract, record any exception, such
as terminal-only progress, in the document that owns that contract rather than
only in the implementation.

## Truthful, advisory output

Progress writes are advisory. Ignore write failures such as a closed terminal
or broken pipe; they must never fail the operation or change its result.

Report a stage only once it is true. Claim success after the effect has
happened, and report deferred work as deferred: a replacement scheduled for
after process exit is reported as scheduled, not installed.

## Rust

Gate progress on `std::io::IsTerminal` for stderr and write stage lines through
a small reporter with an injectable sink, so tests can assert the emitted
stages and production code can be silent. Write with `writeln!` and discard the
result; `eprintln!` panics when stderr is closed. A handful of stage lines does
not justify `tracing`. When a bar is warranted, use `indicatif`, which hides
itself when its target is not a terminal.

## Revisit when

Revisit when an operation becomes long or large enough that rate and remaining
time matter, when a consumer needs machine-readable progress events, or when the
CLI already uses structured logging that can carry stage messages without a
separate reporter.
