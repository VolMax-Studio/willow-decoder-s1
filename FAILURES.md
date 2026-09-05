# Failures & Non-Compliances Log

## #001 — Protocol Non-Compliance: Execution Preceding Preregistration Git Freeze
- **Date:** 2026-09-05
- **Severity:** Process / Epistemic Gate Violation
- **Description:** `reproduce.py` was executed locally and generated `results/summary.json` before `PREREGISTRATION.md` and the harness were formally frozen in git commit `6a61e80`.
- **Impact:** The executed run cannot be classified as a formal confirmatory preregistered run.
- **Classification:** `run-001` is classified as `Exploratory (not pre-registered)`.
- **Remediation:** Any future confirmatory evaluation must follow the frozen-commit execution protocol (`Draft -> Gate -> Freeze Commit -> SHA -> Execute -> Evidence -> Recreation -> Gate -> Ratification`).
