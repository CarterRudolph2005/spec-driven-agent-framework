# Skill: Estimate tokens

Loaded at the plan step. Add a rough token budget to the plan so the human can see the cost before approving. It's an estimate, not a promise; aim for the right order of magnitude.

## Rules of thumb
| Thing | Tokens |
|---|---|
| 1 token | ~4 characters, ~¾ of a word |
| 1 line of code | ~10 |
| 1 line of markdown | ~15 |
| A file you'll read | its size in characters ÷ 4 (`wc -c <file>` if you can run it) |
| One command's output (tests, build, lint) | ~500–2,000 |
| Back-and-forth overhead (tool calls, re-reading, your own reasoning) | add ~50% to each step |

## Per step
Estimate **reading + writing + command output** for each step, then add the overhead.

| Step | What to count |
|---|---|
| Plan | `project-context.md` + spec + plan template read, plan written, one revision round |
| Write | laws read + existing files you'll open + new/changed code and tests written (use the plan's file list) |
| Self-review | skill read + the full diff read once + fixes |
| Test | skill read + one full run of every check + **one** fix-and-rerun round |
| Sidecar | skill + template + spec + plan + diff read, sidecar written, `project-context.md` read and updated |

## Output (goes in the plan's "Token estimate" section)
| Step | Est. tokens | % of total |
|---|---|---|
| Plan | 6k | 10% |
| Write | 25k | 42% |
| Self-review | 8k | 13% |
| Test | 12k | 20% |
| Sidecar | 9k | 15% |
| **Total** | **60k** | **100%** |

Round to the nearest 1k. Percentages add up to 100. Below the table, one line: **the biggest cost and how to shrink it** (e.g. "Write is 42% because of the 3 frontend files; splitting the spec would halve it").
