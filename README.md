# willow-decoder-s1

**Independent Computational Audit and Deposited-Artifact Scope Finding for the Google Willow Surface-Code Decoding Dataset**

[![Reproduction Gate Status](https://img.shields.io/badge/Reproduction-VERIFIED-brightgreen)](#reproduction-results)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![DOI](https://img.shields.io/badge/Zenodo%20Dataset-10.5281%2Fzenodo.13273331-blue)](https://doi.org/10.5281/zenodo.13273331)

---

## 1. Audit Scope & Objective

This repository contains the single-entry reproduction harness and formal preregistration for an independent computational audit of the publicly deposited dataset associated with the Willow quantum error correction experiment:

- **Source Dataset:** Zenodo [`10.5281/zenodo.13273331`](https://doi.org/10.5281/zenodo.13273331)
- **Archive MD5:** `21fa6ad35b395d838ebcdbc92e364a12` (`google_105Q_surface_code_d3_d5_d7.zip`, 5.72 GB)
- **Preregistration Contract:** [`PREREGISTRATION.md`](PREREGISTRATION.md)

---

## 2. Key Findings

### Target B — Deposited-Artifact Scope Finding
- **Finding:** The public Zenodo archive contains **zero** neural-network prediction bitstreams, weights, or model files.
- **Disposition:** `NOT_REPRODUCIBLE_FROM_PUBLIC_DATA` for the Nature 2025 headline claim ($0.143\%$ logical error rate and $\Lambda = 2.14$).
- **Boundary:** This finding reflects strictly the *absence of data from the public deposited artifact*, not an evaluation of the original experimental pipeline.

### Target A1 & A2 — Recomputation of Deposited Libra SOTA
- **Population:** $N_{\text{Libra}} = 364$ distinct experimental configurations across code distances $d \in \{3, 5, 7\}$ and rounds $r \in [10, 250]$, derived dynamically from the preserved manifest.
- **Target A1 ($\varepsilon_7$):** Recomputed $\varepsilon_7 = 1.7113 \times 10^{-3}$ vs published $1.71 \times 10^{-3}$ ($|\Delta| = 1.35 \times 10^{-6} \le 5.00 \times 10^{-6}$, half-unit tolerance rule) $\rightarrow$ **VERIFIED**.
- **Target A2 ($\Lambda$):** Recomputed $\Lambda = 2.0383$ vs published $2.04$ ($|\Delta| = 0.0017 \le 0.0050$, half-unit tolerance rule) $\rightarrow$ **VERIFIED**.

---

## 3. Reproduction Instructions

### Requirements
- Python $\ge 3.10$
- `numpy >= 1.26.0`

```bash
pip install -r requirements-minimal.txt
python3 reproduce.py
```

Execution runs all four registered gates (G0–G3), derives $N_{\text{Libra}} = 364$ from the manifest, verifies 728 bitstream SHA-256 digests, and generates `results/summary.json`.

---

## 4. Repository Structure

```text
willow-decoder-s1/
├── PREREGISTRATION.md       # Pre-analysis decision rules and gate criteria
├── reproduce.py             # Deterministic reproduction harness
├── requirements-minimal.txt # Minimal dependency specification
├── data_manifest.json       # SHA-256 digests for all 728 telemetry files
├── data/                    # Preserved local telemetry bitstreams (.b8)
├── results/
│   └── summary.json         # Structured machine-readable audit report
├── LICENSE                  # MIT License
└── README.md
```
