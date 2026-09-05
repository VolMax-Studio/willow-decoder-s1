# Failures & Non-Compliances Log

## #001 — Protocol Non-Compliance: Execution Preceding Preregistration Git Freeze
- **Date:** 2026-09-05
- **Severity:** Process / Epistemic Gate Violation
- **Description:** `reproduce.py` was executed locally and generated `results/summary.json` before `PREREGISTRATION.md` and the harness were formally frozen in git commit `6a61e80`.
- **Impact:** The executed run cannot be classified as a formal confirmatory preregistered run.
- **Classification:** `run-001` is classified as `Exploratory (not pre-registered)`.
- **Remediation:** Any future confirmatory evaluation must follow the frozen-commit execution protocol (`Draft -> Gate -> Freeze Commit -> SHA -> Execute -> Evidence -> Recreation -> Gate -> Ratification`).

## #002 — B-W1: Missing Literal Output Stream Artifacts in run-002-confirmatory
- **Date:** 2026-09-05
- **Severity:** Evidentiary Sufficiency Failure / Process Defect
- **Description:** `run-002-confirmatory` was executed directly via python without command-line output redirection (`> stdout.log 2> stderr.log`). Consequently, `stdout.log`, `stderr.log`, `command.sh`, and `env.txt` were missing from `evidence/runs/run-002-confirmatory/`.
- **Impact:** Although scientific computations and input hashes were verified, the run cannot be independently ratified due to lack of literal command-bound execution streams.
- **Classification:** `run-002-confirmatory` scientific outputs are preserved, but the run is classified as `Non-Ratifiable (Evidentiary Incomplete)`.
- **Remediation:** Enforce frozen execution wrapper capturing literal `stdout.log`, `stderr.log`, `exit_code.txt`, `command.sh`, `env.txt`, and full 11-artifact package in `run-003-recreation`.

## #003 — B-W2: Runtime Duration Requires Measured Input Byte Accounting
- **Date:** 2026-09-05
- **Severity:** Telemetry / Accountability Gap
- **Description:** `run-002-confirmatory` reported a total runtime of ~100 ms without explicitly recording the exact number of bytes opened and read during execution.
- **Impact:** Reviewers cannot verify whether all 728 bitstreams were fully read or cached.
- **Classification:** Open until recreation records exact byte accounting.
- **Remediation:** Instrument `reproduce.py` to record `bytes_read.json` tracking `files_read_count` (exact 728), `bytes_read_total` (exact 36,400,000 bytes = 34.71 MB across 50,000 shots per file), and per-file byte counts and SHA-256 digests.

## #004 — B-W3: Unrecorded Recreation Execution Attempt
- **Date:** 2026-09-05
- **Severity:** Process / Accounting Gap
- **Description:** An initial attempt to invoke `run-003-recreation` failed prior to artifact directory creation due to uncommitted working tree state, leaving no evidence record or execution trace.
- **Impact:** No determinism proof was generated for `run-002`.
- **Classification:** Recorded as an unrecorded/failed recreation attempt; halt mechanism is not inferred retroactively.
- **Remediation:** Execute a single clean `run-003-recreation` under a dedicated execution wrapper after formal v4 freeze.
