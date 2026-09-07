# Persist Before External Effects History

## 2026-09-05

Made the crash window between provider success and local finalization explicit. Recovery must discover the original admitted record, and retry safety depends on provider idempotency or reconciliation rather than a local promise of exactly-once delivery.
