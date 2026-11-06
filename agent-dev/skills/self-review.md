# Skill: Self-review

Review your own change like a strict teammate before running checks. Read the diff (`git diff main...HEAD` plus any uncommitted changes), then go through this list. Fix every problem you find.

## Against the spec
- [ ] Every "Done when" item is implemented.
- [ ] Nothing beyond the spec was built, and nothing the spec's "Changes / Dev" says to leave alone was changed.
- [ ] The API matches the spec's contract exactly: paths, field names, status codes.

## Against the plan
- [ ] Only the files the plan lists were touched, all inside this feature's worktree. Any extra file was approved.
- [ ] No dependencies beyond the plan's list.
- [ ] Every test case in the plan exists.

## Against the laws
- [ ] Re-read each loaded law and check the diff against it, rule by rule.

## General
- [ ] No secrets, keys, or personal data in code or committed files.
- [ ] No leftover debug prints, commented-out code, or dead code.
- [ ] Errors are handled where they can happen (missing records, bad input, failed external calls).
- [ ] Names are clear enough that a teammate could guess what each thing does.

## Output
A short list for the sidecar's "Decisions" section: anything you changed during self-review, and anything you chose to leave (with why).
