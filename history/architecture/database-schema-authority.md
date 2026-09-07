# Database Schema Authority History

## 2026-09-05

Made compatible evolution across supported old and new runtimes explicit. Ordered migration alone does not protect rolling deployments or rollback; expansion, backfill, consumer migration, and later removal preserve the intended database authority without destructive coexistence.
