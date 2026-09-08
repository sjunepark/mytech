# Standalone CLI Distribution History

## 2026-09-08

Replaced the blanket no-delay and no-CI/noninteractive update-notice rule with
the accepted [version-checking preference](../../practices/cli-version-checking.md).
Bounded foreground refresh is acceptable with caching, an explicit opt-out,
and preserved command success and structured output. Distribution guidance
continues to own installation and upgrade recovery; the new document owns
update detection.

## 2026-09-07

Clarified release transition ownership and consumer-visible completion in
response to [issue #2](https://github.com/sjunepark/mytech/issues/2). Successful
certification or temporary CI artifacts do not establish delivery. Publication
requires exact-artifact verification for all claimed targets, durable delivery
through the supported public or private channel, and owned recovery that
preserves release immutability.

## 2026-09-05

Retained immutable artifacts and one release identity while making installers follow actual audiences and self-upgrade conditional on recurring need. Reinstallation is sufficient until the project earns receipt ownership and cross-platform replacement/recovery machinery.
