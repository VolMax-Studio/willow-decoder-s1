# willow-decoder-s1

**Independent Computational Audit and Deposited-Artifact Scope Finding for the Google Willow Surface-Code Decoding Dataset**

[![Instance Verdict: Verified with Limitations](https://img.shields.io/badge/P10%20Verdict-Verified%20with%20Limitations-brightgreen)](#ratified-audit-results)
[![Process State: Ratified](https://img.shields.io/badge/Process%20State-Ratified-blue)](#governance--ratification)
[![Dataset: Zenodo 10.5281/zenodo.13273331](https://img.shields.io/badge/Zenodo-10.5281%2Fzenodo.13273331-blue)](https://doi.org/10.5281/zenodo.13273331)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 1. Executive Summary & Ratified Results

This repository contains the frozen reproduction harness, cryptographic lineage manifests, and literal execution evidence for the independent computational audit of Google Quantum AI's public surface-code error correction dataset (Zenodo [`10.5281/zenodo.13273331`](https://doi.org/10.5281/zenodo.13273331), MD5: `21fa6ad35b395d838ebcdbc92e364a12`).

### Ratified Target Dispositions (`run-003-recreation`)

| Target | Claim Under Test | Nature (2025) Reference | Reconstructed Value (`run-003`) | Preregistered Acceptance Prag ($R_1$) | Absolute Difference ($|\Delta|$) | Controlled P10 Verdict |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Target A1** | Libra Matching-Family $\varepsilon_7$ | $1.71 \times 10^{-3}$ | **$1.7113465 \times 10^{-3}$** | $|\Delta| \le 0.005 \times 10^{-3}$ | **$1.35 \times 10^{-6}$** | **`Verified`** |
| **Target A2** | Libra Matching-Family $\Lambda$ | $2.04$ | **$2.038282$** | $|\Delta| \le 0.0050$ | **$0.0017$** | **`Verified`** |
| **Target B** | Neural Headline Scope Boundary | $0.143\%$ / $\Lambda = 2.14$ | **0 matching token paths** across 9,959 members | Token pre-registered inventory | `0` matching paths | **`Not Demonstrated from Deposited Artifact Alone`** |

**Instance Aggregate Verdict:** **`Verified with Limitations`** (Ratified by Operator on 2026-09-05).

---

## 2. Deposited-Artifact Scope Boundary & §15 Non-Inference Rule

> [!IMPORTANT]
> **Scope Limitation & Non-Inference Invariant (§15):**
> 1. **Matching-Family Positive Reproduction:** The positive numerical reproduction applies strictly and specifically to the deposited **Libra matching-family** decoder results ($\Lambda = 2.0383$, $\varepsilon_7 = 1.7113 \times 10^{-3}$).
> 2. **No Conflation:** The reproduced matching-family exponent $\Lambda = 2.0383$ must not be conflated with the separate neural-network decoder headline claim ($\Lambda = 2.14$, $0.143\%$).
> 3. **Absence from Deposited Artifact Alone:** All 9,959 members in the Zenodo deposit were systematically evaluated. Zero paths match the preregistered tokens `neural`, `weight`, `weights` (5 matching-family/harmony pipelines identified). This establishes strictly that:
>    $$\text{Reconstruction of the neural headline is }\mathbf{NOT\ DEMONSTRATED\ FROM\ DEPOSITED\ ARTIFACT\ ALONE}$$
>    This finding **does not** imply that Google's headline claim is false, that neural decoding was not experimentally performed, or that neural decoder weights do not exist outside the public archive.

---

## 3. Provenance & Measured Byte Accounting

The audit establishes complete mathematical and cryptographic transparency over the processed bitstreams:

- **1:1 Member Bijection (`SOURCE_MAPPING.json`):** All 728 local bitstreams in `data/` match original archive CRC32 checksums and manifest SHA-256 digests with 0 unmapped and 0 ambiguous entries.
- **Population Invariant ($N_{\text{Libra}} = 364$):** Dynamically derived from the 728 paired bitstreams ($364 \times \text{obs\_flips\_actual.b8}$ and $364 \times \text{libra\_predicted.b8}$) across 14 patches, 2 bases ($X, Z$), and 13 primary rounds ($r \in [10, 250]$).
- **Per-File Shot Invariant:** Every evaluated `.b8` file contains exactly **$50,000$ bytes** ($1$ byte per shot for $N_{\text{shots}} = 50,000$).
- **Measured Byte Accounting (`bytes_read.json`):**
  - Unique input dataset: **728 files** $\times$ 50,000 B = **$36,400,000$ bytes (34.71 MB)**.
  - Integrity pass: 728 read operations ($36,400,000$ B).
  - G3 Computation pass: 728 read operations ($36,400,000$ B).
  - Total application reads: **1,456 operations ($72,800,000$ bytes / 69.43 MB)**.

---

## 4. Exact Frozen Weighting Model (WLS)

1. **Per-Round Decay Fit (`fit_decay`):**
   $$P_L(r) = \frac{1}{N_{\text{shots}}} \sum_{i=1}^{N_{\text{shots}}} (\text{actual}_i \oplus \text{predicted}_i)$$
   $$w_i = \frac{N_{\text{shots}} (1 - 2p)^2}{4 p (1 - p)}, \quad p = \text{clip}(P_L(r), 10^{-7}, 0.499999)$$
2. **Threshold Scaling Fit (`fit_lambda`):**
   $$w_d = \left(\frac{\bar{\varepsilon}_d}{\sigma_{\bar{\varepsilon}_d}}\right)^2, \quad x = \frac{d}{2}, \quad y = \ln(\bar{\varepsilon}_d)$$

---

## 5. Replication & Verification Instructions

### Requirements
- Python $\ge 3.10$
- `numpy >= 1.26.0`

### Execution
```bash
# Install dependencies
pip install -r requirements-minimal.txt

# Run official execution wrapper under frozen PREREG_SHA
./runner.sh run-003-recreation 6daa877b181aa6ca09900589218eac2d1e8a5282
```

---

## 6. Governance & Evidence Structure

```text
willow-decoder-s1/
├── PREREGISTRATION.md       # Pre-analysis specification v4
├── reproduce.py             # Single-entry reproduction harness
├── runner.sh                # Execution wrapper with log capture
├── SOURCE_MAPPING.json      # 728-entry 1:1 bijection to Zenodo archive
├── archive_inventory.json   # 9,959-member complete archive directory
├── data_manifest.json       # Pinned SHA-256 digests for local bitstreams
├── LICENSE_L0.md            # Provenance and MD5 vs SHA-256 distinctions
├── FAILURES.md              # Historical failures log (#001 to #004)
├── STATUS.md                # Lifecycle status (Ratified)
├── PROJECT_HANDOFF.md       # Final project handoff
└── evidence/runs/run-003-recreation/
    ├── command.sh           # Literal executed command
    ├── stdout.log           # Captured literal stdout
    ├── stderr.log           # Captured literal stderr
    ├── exit_code.txt        # Execution exit code (0)
    ├── env.txt              # Execution environment details
    ├── git_commit.txt       # Measured git HEAD SHA
    ├── inputs.sha256        # Hashes of 7 immutable input files
    ├── outputs.sha256       # Hashes of all produced run artifacts
    ├── bytes_read.json      # Two-pass byte accounting telemetry
    ├── recreation_comparison.json # Parity comparison against run-002
    └── summary.json         # Structured machine-readable results
```

---

## 7. Citation & Attribution

```text
Google Quantum AI (2024), Data for "Quantum error correction below the surface code threshold", Zenodo, DOI 10.5281/zenodo.13273331, CC BY 4.0
```

Primary Paper:
> Google Quantum AI and Collaborators. *Quantum error correction below the surface code threshold.* Nature 638, 920–926 (2025). DOI: [10.1038/s41586-024-08449-y](https://doi.org/10.1038/s41586-024-08449-y).
