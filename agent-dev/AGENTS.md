# Agent workflow

You are a coding agent on a hackathon team. Humans own the **spec**, the **plan approval**, and the **code review**. You own the setup, code, self-review, tests, and docs in between.

You'll be pointed at one feature: `agent-dev/features/NNN-name/`. Work only on that feature.

```
Project context → Spec → Setup (worktree) → Plan approval → Write with laws → Self-review → Test (skill) → Sidecar (skill) → Human code review → PR
```

---

## Core rules (always on)

1. **Stay in scope.** Build what the spec says. Anything else goes in the plan's "Out of scope / follow-ups."
2. **Don't guess silently.** If the spec leaves something open, pick the simplest reasonable option and list it under the plan's "Risks / assumptions" so the human sees it at approval. If something unexpected comes up mid-build, stop and ask.
3. **Never commit secrets.** Keys go in gitignored env files and are read from environment variables.
4. **No new dependencies** unless the approved plan lists them.
5. **Stay in your worktree.** After Setup, every file edit and command happens inside `.worktrees/NNN-name/`. Don't touch the main checkout, other worktrees, or files the approved plan doesn't list.
6. **Never push, open a PR, merge, or touch `main`.** Local commits on the feature branch are fine. A human pushes and opens the PR.
7. **Load only what the current step needs** (load table below).

---

## Load table
All paths below are relative to your worktree after Setup.

| Step | Load |
|---|---|
| 1. Setup | nothing |
| 2. Plan | `agent-dev/project-context.md`, the spec, `agent-dev/templates/plan.md`, `agent-dev/skills/estimate-tokens.md` |
| 3. Write | `agent-dev/laws/comments.md` + `agent-dev/laws/tests.md` (always), plus each law the plan checks: `backend.md`, `frontend.md`, `database.md` |
| 4. Self-review | `agent-dev/skills/self-review.md` |
| 5. Test | `agent-dev/skills/run-checks.md` |
| 6. Sidecar | `agent-dev/skills/write-sidecar.md` (it loads its own template) |

Laws are stack-neutral. The stack-specific *how* lives in `project-context.md` (Commands, Stack conventions). If a section you need doesn't exist yet, use the standard approach for the stack listed under Fundamentals and say so in the plan. The sidecar step records it so the next feature can follow it.

---

## Steps

### 1. Setup
From the repo root, run:
```
python agent-dev/feature.py start NNN-name
```
(`python3` if `python` isn't found.) This creates `.worktrees/NNN-name/` on branch `feat/NNN-name` and moves the spec into it. **Work only inside that folder from now on.** If the worktree already exists, continue there. Install dependencies in the worktree before running anything.

If you can't run commands, ask the human to run it and tell you when it's done.

### 2. Plan approval (Loop 1)
- Read `project-context.md` and the spec.
- Copy `agent-dev/templates/plan.md` to `agent-dev/features/NNN-name/plan.md` and fill it in. Every "Done when" item maps to at least one test case. Anything the spec left open goes under "Risks / assumptions."
- Load `agent-dev/skills/estimate-tokens.md` and fill in the plan's "Token estimate": total tokens and each step's share.
- Show the plan and ask: **"Approve this plan, or what should change?"**
- **STOP and wait.** Revise and ask again until approved. Then set `Status: APPROVED by <name>` and the spec status to `BUILDING`.
- No code before approval.

### 3. Write with laws (Loop 2 starts)
- Confirm `git branch --show-current` is `feat/NNN-name`.
- Load the laws from the load table, then write the code and tests the plan lists. Need an unlisted file? Ask first.

### 4. Self-review
- Load `agent-dev/skills/self-review.md` and follow it. Fix what it finds.

### 5. Test
- Load `agent-dev/skills/run-checks.md` and follow it.
- On failure: fix, self-review the changed code, re-run checks. **Max 3 attempts**, then STOP: show the failing check, the error, and what you tried.

### 6. Sidecar
- Load `agent-dev/skills/write-sidecar.md` and follow it. It writes `agent-dev/features/NNN-name/sidecar.md` and adds what this feature introduced to `project-context.md`.

### 7. Hand off for human code review
Say:
> Ready for review in `.worktrees/NNN-name/`. Read `agent-dev/features/NNN-name/sidecar.md`, answer its "Questions you should be able to answer" before opening the answers, then review `git diff main...HEAD`.

If the reviewer asks for changes, go back to Step 3 and run Steps 4–6 again.

---

## Front + back in one spec
Default: one agent builds both, backend first, against the spec's API contract.
If the plan says `Split: yes`, two humans each run an agent: the first one runs Setup, the second works in the same worktree on the other side only. The API contract is fixed; changes to it go back to the humans.

## Fast path (small changes)
Skip Setup's worktree, the plan, and the sidecar when **all** are true: under ~20 lines, no new endpoint, table, or dependency, and the change is obvious (copy, styling, a bug with a clear cause). Work on a branch named `fix/<short-name>` instead.
Still load the relevant laws, self-review, and run checks. If the change affects anything recorded in `project-context.md` (a command, a convention), update that line. Say "fast path" in your hand-off.
