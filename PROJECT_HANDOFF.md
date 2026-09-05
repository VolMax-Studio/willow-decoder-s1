# Project Handoff

## Identity

Project: willow-decoder-s1
Repository: VolMax-Studio/willow-decoder-s1
Branch: instances/willow-decoder-s1
Current commit: Pending post-execution update
Preregistration commit: 6daa877b181aa6ca09900589218eac2d1e8a5282 (PREREG_SHA_v4)
Latest run ID: run-003-recreation (COMPLETED RECREATION CERTIFIED)
Next run ID: None (Awaiting Final Ratification)
Deadline: 2026-09-12

## Phase

Post-Execution Review & Ratification — Execution State: POST_EXECUTION_REVIEW

Portfolio status: ACTIVE / DEADLINE PRIORITY

Architecture:
Public Zenodo artifact decoding audit (Zenodo 10.5281/zenodo.13273331) evaluating Target A (matching-family Libra decoder recomputation) and Target B (neural decoder artifact scope boundary across complete 9,959-member archive inventory).

Audit Class:
External public-artifact audit.
Claimant: Google Quantum AI (Willow Nature 2025 paper).

## Exact claim under test

Claim under test (Target A): From the public deposited bitstreams in Zenodo 10.5281/zenodo.13273331, the matching-family Libra decoder error rate ($\varepsilon_7 = (1.71 \pm 0.03) \times 10^{-3}$) and scaling exponent ($\Lambda = 2.04 \pm 0.02$) can be deterministically reconstructed from raw telemetry bitstreams without manual post-hoc adjustments.

Claim under test (Target B): Whether the public Zenodo archive contains files corresponding to neural-network decoder weights, architecture specifications, or neural predicted bitstreams required for the Nature 2025 headline claim ($0.143\%$ error rate, $\Lambda = 2.14$).

## Evidence boundary

Public artifacts:
- Zenodo deposit `10.5281/zenodo.13273331` (MD5: `21fa6ad35b395d838ebcdbc92e364a12`).
- Preserved local telemetry bitstreams (`728` files matching SHA-256 digests in `data_manifest.json` and CRC32 in `SOURCE_MAPPING.json`).
- Complete archive central directory inventory (`archive_inventory.json`, 9,959 members).

## Current results

- run-001: Classified as `Exploratory (not pre-registered)` per FAILURES #001 due to execution preceding git freeze commit.
- run-002-confirmatory: Scientific computation verified ($\varepsilon_7 = 1.7113 \times 10^{-3}$, $\Lambda = 2.0383$, Target B disposition confirmed), classified as non-ratifiable per FAILURES #002 (B-W1).
- run-003-recreation: Successfully executed under frozen PREREG_SHA_v4 `6daa877b181aa6ca09900589218eac2d1e8a5282` via `runner.sh`.
  - Target A1 ($\varepsilon_7$): Recomputed $\varepsilon_7 = 1.7113 \times 10^{-3}$ vs reference $1.71 \times 10^{-3}$ ($|\Delta| = 1.35 \times 10^{-6} \le 5.00 \times 10^{-6}$) $\rightarrow$ **`VERIFIED`**.
  - Target A2 ($\Lambda$): Recomputed $\Lambda = 2.0383$ vs reference $2.04$ ($|\Delta| = 0.0017 \le 0.0050$) $\rightarrow$ **`VERIFIED`**.
  - Target B (Archive Scope): 0 archive paths matching preregistered tokens `neural`, `weight`, `weights` across 9,959 members $\rightarrow$ **`NOT DEMONSTRATED FROM DEPOSITED ARTIFACT ALONE`**.
  - Recreation Parity: 10/10 scientific fields match `run-002-confirmatory` (`recreation_comparison.json`, `all_scientific_payloads_match: true`).
  - Byte Accounting: 36.4 MB unique input bytes across 728 files (50k shots verified per file), 72.8 MB application read total.
  - Complete 12-artifact package captured and covered under `outputs.sha256`.

## Gate status

Gate model/person: Claude
Pre-Execution Gate outcome: GATE_PASS (Draft v4 @ d42f999)
Accepted by: Ivan (Operator)
Post-Execution Gate outcome: PENDING POST-EXECUTION REVIEW & RATIFICATION

## Next single action

Submit post-execution Gate review packet to Claude and Operator for final ratification.
