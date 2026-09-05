# Project Handoff

## Identity

Project: willow-decoder-s1
Repository: VolMax-Studio/willow-decoder-s1
Branch: instances/willow-decoder-s1
Current commit: Pending draft v4 commit
Preregistration commit: Pending Gate pass and Operator freeze (PREREG_SHA_v4)
Latest run ID: run-002-confirmatory (Non-Ratifiable per FAILURES #002 / B-W1)
Next run ID: run-003-recreation (NOT YET AUTHORIZED)
Deadline: 2026-09-12

## Phase

Specification Draft v4 (PRE-EXECUTION GATE DRAFT) — Execution State: NOT AUTHORIZED

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
- run-002-confirmatory: Scientific computation verified ($\varepsilon_7 = 1.7113 \times 10^{-3}$, $\Lambda = 2.0383$, Target B disposition confirmed), but classified as non-ratifiable due to missing literal stdout/stderr stream logs per FAILURES #002 (B-W1).
- run-003-recreation: Awaiting pre-execution Gate review of Draft v4 to recreate scientific outputs with full 11-artifact command-bound evidence package.

## Gate status

Gate model/person: Claude
Gate outcome: PENDING PRE-EXECUTION GATE REVIEW (Draft v4)
Blocking findings:
None.

## Next single action

Submit Draft v4 commit to Claude for pre-execution Gate review.
