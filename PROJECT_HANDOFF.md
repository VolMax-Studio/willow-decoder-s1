# Project Handoff

## Identity

Project: willow-decoder-s1
Repository: VolMax-Studio/willow-decoder-s1
Branch: instances/willow-decoder-s1
Current commit: Pending post-execution update
Preregistration commit: d16cfac78cb2d6777fb026c60a2488956c88e704 (PREREG_SHA_v3)
Latest run ID: run-002-confirmatory (COMPLETED CONFIRMATORY)
Next run ID: None (Awaiting Post-Execution Review & Ratification)
Deadline: 2026-09-12

## Phase

Post-Execution Review — Execution State: POST_EXECUTION_REVIEW

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
- run-002-confirmatory: Successfully executed under frozen PREREG_SHA_v3 `d16cfac78cb2d6777fb026c60a2488956c88e704`.
  - Target A1 ($\varepsilon_7$): Recomputed $\varepsilon_7 = 1.7113 \times 10^{-3}$ vs reference $1.71 \times 10^{-3}$ ($|\Delta| = 1.35 \times 10^{-6} \le 5.00 \times 10^{-6}$) $\rightarrow$ **`VERIFIED`**.
  - Target A2 ($\Lambda$): Recomputed $\Lambda = 2.0383$ vs reference $2.04$ ($|\Delta| = 0.0017 \le 0.0050$) $\rightarrow$ **`VERIFIED`**.
  - Target B (Archive Scope): 0 neural/weight artifacts found across 9,959 members $\rightarrow$ **`NOT DEMONSTRATED FROM DEPOSITED ARTIFACT ALONE`**.

## Gate status

Gate model/person: Claude
Pre-Execution Gate outcome: GATE_PASS (Draft v3 @ 71e5b8c)
Accepted by: Ivan (Operator)
Post-Execution Gate outcome: PENDING POST-EXECUTION REVIEW

## Next single action

Submit post-execution Gate review packet to Claude for final review and ratification.
