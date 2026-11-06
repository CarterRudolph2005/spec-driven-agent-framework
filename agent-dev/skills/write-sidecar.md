# Skill: Write the sidecar

The sidecar lets a teammate understand this feature without reading every line. Keep it to about one screen.
This step also keeps `project-context.md` current, so the next feature's agent starts with an accurate picture.

## Steps
1. Read `agent-dev/features/NNN-name/spec.md` and `plan.md`.
2. Read the actual change: `git diff main...HEAD --stat`, then the full diff. Describe what the code **does**, not what the plan intended. If they differ, say so under "Decisions."
3. Copy `agent-dev/templates/sidecar.md` to `agent-dev/features/NNN-name/sidecar.md` and fill in every section.
4. Write **3–5 "Questions you should be able to answer,"** based on this feature's real decisions:
   - Where a business rule lives and what happens when it's broken
   - How data flows from the user's action to the database and back
   - Why this approach was chosen over the obvious alternative
   - What would break if a teammate changed something nearby
   Put each answer in a `<details>` block so the reviewer tries first.
5. Add the self-review notes under "Decisions" and the check table under "Checks."
6. **Update `project-context.md`** (agent-maintained sections only; never edit the human Fundamentals):
   | If this feature... | Add / update |
   |---|---|
   | added or changed a table or field | **Data model** row |
   | added or changed an endpoint | **API** row (with this feature's ID) |
   | added an env var, naming rule, or format | **Conventions** |
   | used a command not listed yet (test, lint, build, run, smoke, reset) | **Commands** row |
   | set up a pattern others should copy (test fixtures, a model pattern, a helper) | **Stack conventions** (short, with a snippet if it saves time) |
   | added a folder or changed where code lives | **Folder layout** |
   | added a layer or external service | **Architecture** |
   | made a choice the next feature should know about | **Decisions log**: `date — decision — why (NNN)` |
   Rules: only record what exists in the code. Update or remove entries this feature made untrue. Keep entries to a line or two. Create a section the first time it's needed. List what you changed under the sidecar's "Context updates."
7. Set the spec status to `READY FOR REVIEW`.

## Style
- Plain English. Files and functions in backticks.
- No marketing words ("robust," "seamless"). Say what it does.
- Known gaps are honest. A listed gap is fine; a hidden one isn't.
