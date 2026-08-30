from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = (
    "README.md",
    "docs/architecture.md",
    "docs/agent-workflow.md",
    "docs/safety-and-approval.md",
    "docs/evaluation.md",
    "docs/claim-boundaries.md",
    "docs/diagrams/workflow.md",
)
REQUIRED_TERMS = (
    "承認ゲート",
    "終了条件",
    "Human",
    "Git",
    "CI",
    "本番運用",
)


def main() -> None:
    missing_files = [path for path in REQUIRED_FILES if not (ROOT / path).is_file()]
    if missing_files:
        raise SystemExit(f"Missing required files: {', '.join(missing_files)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    missing_terms = [term for term in REQUIRED_TERMS if term not in readme]
    if missing_terms:
        raise SystemExit(f"README is missing required terms: {', '.join(missing_terms)}")

    print("Documentation validation passed.")


if __name__ == "__main__":
    main()
