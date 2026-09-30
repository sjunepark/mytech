# External Request Pacing History

## 2026-09-30

Accepted default-on pacing for external provider requests, based on darty's
cross-process OpenDART pacing (500 ms, shared through a file lock). Four
concurrent CLI processes had bypassed per-client pacing with request gaps under
10 ms. That showed pacing must cover the shared provider identity, not one
process. Requested that the interval be configurable through a flag, an
environment variable, and a client option. The specific interval remains
project-specific.
