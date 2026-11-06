# Skill: Run checks

The exact commands come from `project-context.md` → **Commands**. If a command isn't listed yet, find it in the repo (package.json scripts, the stack's standard tools), use it, and note it so the sidecar step records it. Run every check that applies, in order, and record each result.

| # | Check | When | Command from |
|---|---|---|---|
| 1 | Backend tests | backend changed | `Commands → Test (backend)` |
| 2 | Frontend tests | frontend changed and a test command exists | `Commands → Test (frontend)` |
| 3 | Lint | always, only tools already installed | `Commands → Lint` |
| 4 | Build | frontend changed | `Commands → Build` |
| 5 | Smoke test | backend changed | `Commands → Smoke` |

**Smoke test:** start the server on a spare port (so it doesn't collide with a teammate's), call the health endpoint and one new endpoint, then stop the server.

If there's no way to run a check yet (e.g. no linter installed), mark it ⏭ and say why.

## On failure
1. Read the full error. Fix the cause, not the symptom.
2. Re-run self-review on what you changed, then **all** checks, not just the failed one.
3. **Max 3 attempts.** Then stop and report the failing check, the error, and what you tried.

**Never** delete, skip, or loosen a test, add lint-disable comments, or swallow an exception to get a pass.

## Output
A table for the sidecar:
| Check | Result |
|---|---|
| Backend tests | ✅ 8 passed |
| Lint | ⏭ no linter installed |
| Build | ✅ |
| Smoke | ✅ health 200, POST /shifts/1/signups 201 |
