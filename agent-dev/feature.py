#!/usr/bin/env python3
"""Feature helper. Works on Mac, Linux, and Windows (git 2.31+, Python 3.8+, no packages).

  python agent-dev/feature.py new 003 shift-signup
      (human) Creates agent-dev/features/003-shift-signup/spec.md from the template.

  python agent-dev/feature.py start 003-shift-signup
      (agent) Creates the worktree .worktrees/003-shift-signup on branch feat/003-shift-signup,
      moves the feature folder into it, and prints where to work.

  python agent-dev/feature.py done 003-shift-signup
      (human, after the PR merges) Removes the worktree.

Worktrees live inside the repo (.worktrees/, ignored locally via .git/info/exclude),
so any agent tool opened at the repo root can reach them.
"""
import shutil
import subprocess
import sys
from pathlib import Path


def git(*args, cwd=None):
    """Run a git command and return its output, or exit with git's error."""
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result.stdout.strip()


def repo_root():
    """Main checkout root, even when run from inside a worktree."""
    return Path(git("rev-parse", "--path-format=absolute", "--git-common-dir")).parent


def ignore_worktrees(root):
    """Ignore .worktrees/ locally without changing any tracked file."""
    exclude = root / ".git" / "info" / "exclude"
    exclude.parent.mkdir(parents=True, exist_ok=True)
    text = exclude.read_text(encoding="utf-8") if exclude.exists() else ""
    if ".worktrees/" not in text.split():
        exclude.write_text(text.rstrip("\n") + "\n.worktrees/\n", encoding="utf-8")


def cmd_new(feature_id, name):
    root = repo_root()
    slug = f"{feature_id}-{name}"
    feature_dir = root / "agent-dev" / "features" / slug
    if feature_dir.exists():
        sys.exit(f"{feature_dir} already exists. Pick a new ID.")
    feature_dir.mkdir(parents=True)
    template = (root / "agent-dev" / "templates" / "spec.md").read_text(encoding="utf-8")
    (feature_dir / "spec.md").write_text(template.replace("NNN", feature_id), encoding="utf-8")
    rel = feature_dir.relative_to(root).as_posix()
    print(f"Spec created: {rel}/spec.md")
    print("Fill it in, then tell your agent:")
    print(f"  Follow agent-dev/AGENTS.md for {rel}")


def cmd_start(slug):
    root = repo_root()
    src = root / "agent-dev" / "features" / slug
    worktree = root / ".worktrees" / slug
    if worktree.exists():
        sys.exit(f".worktrees/{slug} already exists. If it's yours, keep working there.")
    if not (src / "spec.md").exists():
        sys.exit(f"No spec at agent-dev/features/{slug}/spec.md. Run: python agent-dev/feature.py new <id> <name>")

    ignore_worktrees(root)
    git("worktree", "add", str(worktree), "-b", f"feat/{slug}", cwd=root)

    # Move the spec folder into the worktree so it's committed on the feature branch, not left on main.
    dest = worktree / "agent-dev" / "features" / slug
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        shutil.rmtree(dest)          # a copy already committed on main; the working version wins
    shutil.copytree(src, dest)
    shutil.rmtree(src)

    print(f"Worktree: .worktrees/{slug}   (branch feat/{slug})")
    print(f"Spec:     .worktrees/{slug}/agent-dev/features/{slug}/spec.md")
    print(f"From now on, every file edit and command happens inside .worktrees/{slug}/")
    print("Install dependencies there before running the app or tests (npm install, venv, etc.).")


def cmd_done(slug):
    root = repo_root()
    worktree = root / ".worktrees" / slug
    git("worktree", "remove", str(worktree), cwd=root)
    print(f"Removed .worktrees/{slug}. Delete the branch when you're ready: git branch -d feat/{slug}")


def main():
    usage = ("Usage:\n  python agent-dev/feature.py new <id> <name>\n"
             "  python agent-dev/feature.py start <id-name>\n  python agent-dev/feature.py done <id-name>")
    args = sys.argv[1:]
    if args[:1] == ["new"] and len(args) == 3:
        cmd_new(args[1], args[2])
    elif args[:1] == ["start"] and len(args) == 2:
        cmd_start(args[1])
    elif args[:1] == ["done"] and len(args) == 2:
        cmd_done(args[1])
    else:
        sys.exit(usage)


if __name__ == "__main__":
    main()
