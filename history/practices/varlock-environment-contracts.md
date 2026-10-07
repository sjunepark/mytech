# Varlock Environment Contracts History

## 2026-10-07

Accepted Varlock as the default environment contract for every repository that
reads environment variables, across languages, in preference to direct
environment reads. Robustness and clarity were judged worth the extra schema,
CLI, and generated code. Current Varlock documentation shows typed generated
loaders for Python, Rust, Go, and other languages, so language was not a reason
to exclude a repository. Those loaders fail without `varlock run`, which led to
the exclusion for the runtime of distributed binaries. A Windows-native install
for non-JavaScript repositories and 1Password plugin use under `op-agent` were
unverified when this was accepted.
