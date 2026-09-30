---
status: accepted
---

# External Request Pacing

**Initial evidence:** darty (OpenDART)

## Decision

Pace requests to external providers by default. A client, SDK, or CLI should
wait a conservative minimum interval between request starts even when the
provider documents no limit. An unpaced burst can suspend a key or block an
address, and that cost usually exceeds the latency pacing adds.

Pacing is a project decision, not a provider fact. Choose the default from the
provider's documented limits when they exist, and otherwise from its expected
use and risk. For example, darty waits 500 ms between OpenDART requests. No
single interval is a universal default. Record the chosen value and its evidence
label as described in
[External Provider Qualification](external-provider-qualification.md).

## Scope of the interval

Apply the interval to everything that shares the provider identity, not only to
one client instance. This commonly means all local processes that use the same
provider and credential. Agents and scripts often launch CLI processes
concurrently, so per-process pacing alone does not prevent bursts.

Coordinate local processes through shared state, such as an OS file lock in a
per-user state directory. Hold the wait in a form that survives slow connection
setup, cancellation, process death, and wall-clock changes. Do not let an expired
reservation release a burst. When concurrent callers request different
intervals, honor the largest. If pacing state cannot be read or locked, fail
closed with an explicit error rather than sending unpaced requests.

Coordination across hosts that share a credential needs a server-side or
provider-side mechanism. Local pacing does not provide it.

## Configuration

Make the interval configurable at every consumer boundary the tool supports:

- a CLI flag, such as `--request-interval-ms <ms>`, for one invocation;
- an environment variable for inherited agent, CI, and wrapper contexts; and
- a client or SDK option for library consumers.

Use this precedence: explicit flag or option, then environment variable, then
project configuration, then the built-in default. Validate the value against a
documented range. Reject invalid, negative, or out-of-range values with an
explicit error instead of silently using the default. Allow `0` to disable
pacing for controlled tests and fixture origins. Document its risk.

Where the shared pacing state lives should also be configurable, for example
with an absolute state-directory override, so tests and sandboxes can isolate or
share it deliberately. Report the effective interval and its source in
diagnostic or status output.

## Rate-limit responses

Pacing reduces risk but does not guarantee quota compliance. Classify responses
that indicate rate limiting separately from connection failures. A reset or
timeout does not prove throttling. Honor provider back-off signals such as
`Retry-After`. Keep automatic retries bounded and paced through the same
interval, and never retry a rate-limit error immediately.

## Revisit when

Revisit the default when the provider publishes limits, returns quota headers,
or production evidence shows the interval is too strict or too loose. Replace
the fixed interval with a token bucket or concurrency budget when documented
limits and throughput needs justify the added complexity. Add coordination
beyond one host when multiple machines share one credential.
