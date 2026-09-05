# Project Handoff

## Identity

Project: willow-decoder-s1
Repository: VolMax-Studio/willow-decoder-s1
Branch: instances/willow-decoder-s1
Current commit: 4eef577f9ba5b849adaba8aac53471e56d313443
Preregistration commit: 4eef577f9ba5b849adaba8aac53471e56d313443
Latest run ID: run-001 (Exploratory / Protocol Non-Compliance per FAILURES #001)
Next run ID: run-002-confirmatory (AUTHORIZED)
Deadline: 2026-09-12

## Phase

Frozen Specification v3 (FROZEN PRE-REGISTRATION) — Execution State: READY_FOR_EXECUTION

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
- run-002-confirmatory: Authorized for execution under PREREG_SHA_v3.

## Gate status

Gate model/person: Claude
Gate subject: 71e5b8ca319a11edab30ab7d5d9885362c00cee4
Gate outcome: GATE_PASS (v3 specification accepted)
Accepted by: Ivan (Operator)
Blocking findings:
None.

## Next single action

Execute run-002-confirmatory via reproduce.py with pinned PREREG_SHA_v3.
