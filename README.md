# Spec-Driven Agent Framework

A tool-agnostic workflow for building features with a coding agent while the team still understands every line. Humans own the spec, plan approval, and code review. The agent writes, self-reviews, tests, and documents in between.

**Full guide with diagrams: [agent-dev/README.md](agent-dev/README.md)**

## Install into a project
Copy into the project repo root (the curl one-liner is in [agent-dev/README.md](agent-dev/README.md#integrating-into-dev-repo)):
```
agent-dev/     ← the whole framework, tucked away
AGENTS.md      ← 3-line pointer (Codex, Cursor, Copilot auto-read this)
CLAUDE.md      ← 2-line pointer (Claude Code auto-reads this)
```
The two pointer files are the only things at the root. They're optional: without them, just name the file in your prompt ("Follow agent-dev/AGENTS.md for ...").

Then fill in the four **Fundamentals** in `agent-dev/project-context.md` as a team (~5 min) and start your first feature:
```bash
python agent-dev/feature.py new 001 my-feature
```
Then tell your agent: `Follow agent-dev/AGENTS.md for agent-dev/features/001-my-feature`
