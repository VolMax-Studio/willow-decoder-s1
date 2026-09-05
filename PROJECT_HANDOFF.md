# Project Handoff

## Identity

Project: willow-decoder-s1
Repository: VolMax-Studio/willow-decoder-s1
Branch: instances/willow-decoder-s1
Current commit: Closure commit (Ratified)
Preregistration commit: 6daa877b181aa6ca09900589218eac2d1e8a5282 (PREREG_SHA_v4)
Final evidence commit: 78dd4a51e6ba68ce09f7a7da93f0b2f1505bc7aa
Final run ID: run-003-recreation (Ratified)
Deadline: 2026-09-12

## Phase

Ratified — Instance Closed

Portfolio status: COMPLETED / RATIFIED

Architecture:
Public Zenodo artifact decoding audit (Zenodo 10.5281/zenodo.13273331) evaluating Target A (matching-family Libra decoder recomputation) and Target B (neural decoder artifact scope boundary across complete 9,959-member archive inventory).

Audit Class:
External public-artifact audit.
Claimant: Google Quantum AI (Willow Nature 2025 paper).

## Ratified Verdicts & Dispositions

Controlled P10 Instance Verdict: **`Verified with Limitations`**

- **Target A1 ($\varepsilon_7$):** **`Verified`**
  - Reference: $1.71 \times 10^{-3}$
  - Reconstructed: $0.0017113465352358304$
  - $|\Delta| = 1.35 \times 10^{-6} \le 5.00 \times 10^{-6}$ (satisfied).
- **Target A2 ($\Lambda$):** **`Verified`**
  - Reference: $2.04$
  - Reconstructed: $2.038282091967165$
  - $|\Delta| = 0.0017 \le 0.0050$ (satisfied).
- **Target B (Archive Scope Boundary):** **`Not Demonstrated from Deposited Artifact Alone`**
  - Finding: 0 archive paths matching preregistered tokens `neural`, `weight`, `weights` across all 9,959 members.
  - Disposition: `NO_EXPLICIT_NEURAL_PIPELINE_OR_WEIGHT_ARTIFACT_IDENTIFIED_IN_ARCHIVE_INVENTORY`.
  - Non-inference boundary: Does not claim Google's headline claim is false or that neural weights do not exist outside the archive.

## Scope Limitation

The positive numerical reproduction applies specifically to the deposited **Libra matching-family** results ($\Lambda = 2.0383$). It must not be conflated with the separate neural-decoder headline claim ($\Lambda = 2.14, 0.143\%$).

## Gate Status & Governance

- Pre-Execution Gate: GATE_PASS (Claude @ d42f999)
- Governing Preregistration SHA: `6daa877b181aa6ca09900589218eac2d1e8a5282`
- Post-Execution Review: SURVIVES-REVIEW (Deterministic parity, full 12-artifact package, byte accounting verified)
- Final Ratification: Ratified by Ivan (Operator) on 2026-09-05.

## Next Action

NONE — Instance Closed.
