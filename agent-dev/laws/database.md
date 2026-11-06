# Law: Database

Load if the plan touches the schema, models, seed data, or DB setup. ORM/driver specifics come from `project-context.md` → **Stack conventions → Database**.

1. **The schema is defined in one place** (models or a schema file). No tables created ad hoc in feature code.
2. **Storage shape ≠ API shape.** Keep separate definitions for what's stored and what the API accepts/returns, so internal fields don't leak and validation can't be skipped.
3. **Rules the data must always obey go in the database:** NOT NULL, UNIQUE, foreign keys, CHECKs. Make sure foreign keys are actually enforced (some engines, like SQLite, need it turned on).
4. **Constraint violations become clean errors:** catch them, roll back, return 409 (or 404 for a missing parent).
5. **Queries are always parameterized** (or go through the ORM). Never build SQL by string formatting.
6. **Schema changes are announced.** If the change breaks existing local databases, the plan and sidecar say exactly what to do (run the migration, or delete the dev DB and restart).
7. **Seed data stays useful and idempotent:** new tables get demo rows, and re-running the seed doesn't duplicate them.
8. **Dates/times use ISO 8601,** UTC unless the spec says otherwise.
