# CLI Version Checking History

## 2026-09-08

Accepted cached, bounded automatic version advisories based on sjskills in
agent-scripts. Agent and noninteractive invocations are primary consumer paths,
so suppressing checks there hides useful update evidence. Retained stable
published releases as the comparison baseline, explicit uncertainty, and
separate installation authority. Refresh intervals, retry cooldowns, and
latency budgets remain project-specific rather than adopting sjskills's exact
values as universal defaults.
