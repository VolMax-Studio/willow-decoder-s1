# Willow Decoder Audit — Pre-registration v2

**Instance:** `willow-decoder-s1`  
**Phase:** Specification Draft v2 (PRE-EXECUTION GATE DRAFT)  
**Target Run:** `run-002-confirmatory`  
**Purpose:** Independent computational reproduction and deposited-artifact scope audit of the publicly deposited Willow surface-code decoding dataset.

---

## 1. Prior Exposure & Lineage Disclosure

An exploratory run (`run-001`) was previously executed locally prior to git freeze of the preregistration specification. Per `FAILURES #001`, `run-001` is permanently classified as `Exploratory (not pre-registered)`.

### Prior Observations from run-001:
- Dynamically derived Libra population count: $N_{\text{Libra}} = 364$.
- Recomputed matching-family Libra logical error rate for distance $d=7$: $\varepsilon_7 \approx 1.71 \times 10^{-3}$.
- Recomputed matching-family threshold scaling exponent: $\Lambda \approx 2.04$.
- Target B case-insensitive search for neural/weight artifacts in public Zenodo manifest returned count $= 0$.

`run-002-confirmatory` is the formal, pre-registered confirmatory run executed strictly after independent Gate review and Operator freeze.

---

## 2. Scope & Boundaries

This audit evaluates only claims and properties that can be directly tested from the publicly deposited artifacts in the referenced Zenodo archive:

1. **Target A (Deposited-Data Numerical Reproduction):** Direct recomputation of matching-family Libra decoder error rates ($\varepsilon_7$) and scaling exponent ($\Lambda$) from deposited bitstreams.
2. **Target B (Deposited-Artifact Scope Finding):** Verification of the presence or absence of neural-network decoder weights, architecture definitions, and neural prediction bitstreams in the public archive.

### Strict Non-Inference Rule:
- The absence of neural decoder artifacts in the public Zenodo archive establishes strictly an **archive-content boundary**.
- It **does not** establish that Google's neural headline claim ($0.143\%$ error rate, $\Lambda = 2.14$) is false or that neural decoding was not performed experimentally.
- No inference from absence in the public deposit to non-existence outside the archive is permitted.

---

## 3. Provenance & Dataset Identity

- **Source Archive:** Zenodo [`10.5281/zenodo.13273331`](https://doi.org/10.5281/zenodo.13273331)
- **Archive Pinned MD5:** `21fa6ad35b395d838ebcdbc92e364a12` (`google_105Q_surface_code_d3_d5_d7.zip`, 5.72 GB)
- **Authoritative Telemetry Manifest:** `data_manifest.json` containing SHA-256 digests for all 728 telemetry bitstreams (`obs_flips_actual.b8` and `obs_flips_predicted.b8` / `libra_predicted.b8`).

Every bitstream file used in the audit must match its pinned SHA-256 digest in `data_manifest.json`. Any hash mismatch triggers an immediate halt (`EXECUTION_STATE_INVALID`).

---

## 4. Operational Population Definition (P1 / G1)

Let an experimental root be a relative directory containing a deposited Libra decoding pipeline:
`decoding_results/libra_decoder_with_rl_optimized_prior/` (or `libra_predicted.b8`).

The population $N_{\text{Libra}}$ is defined operationally and derived dynamically from `data_manifest.json`:
$$N_{\text{Libra}} = \text{count}(\text{distinct experimental roots})$$

- **Expected Population:** $N_{\text{Libra}} = 364$.
- The runner must derive $N_{\text{Libra}}$ from the manifest itself.
- If the derived count differs from 364, execution halts immediately (`POPULATION_MISMATCH`).

---

## 5. Target B — Deposited-Artifact Scope Finding (G2)

### Test Procedure:
Perform a case-insensitive search across all path and key entries in the authoritative manifest for neural-network and model-weight indicators:
```text
"neural", "weight"
```

### Decision Rule:
- If $\text{count}(\text{matching artifacts}) == 0$:
  $$\text{Disposion: }\mathbf{TARGET\ B:\ ABSENCE\ FROM\ DEPOSITED\ ARTIFACT}$$
- Any matching path is recorded verbatim.
- The outcome is classified strictly as a scope finding of the public deposit.

---

## 6. Target A1 — Libra Logical Error Rate $\varepsilon_7$

### Target Reference:
- Published reference value: $\varepsilon_7 = 1.71 \times 10^{-3}$ (Nature 2025 reported value for matching-family Libra).
- Tolerance: $R_1 = 0.005 \times 10^{-3}$ (half-unit rule on second displayed decimal place in units of $10^{-3}$).

### Recomputation Method:
For each distance $d \in \{3, 5, 7\}$, patch, basis $B \in \{X, Z\}$, and round $r \in [10, 250]$:
1. Compute per-shot logical error probability $P_L(r)$ via bitwise XOR mean between actual and predicted bitstreams:
   $$P_L(r) = \frac{1}{N_{\text{shots}}} \sum_{i=1}^{N_{\text{shots}}} (\text{actual}_i \oplus \text{predicted}_i)$$
2. Fit exponential decay model via deterministic weighted least-squares:
   $$\ln(1 - 2 P_L(r)) = \ln(1 - 2 \varepsilon_{\text{init}}) + r \cdot \ln(1 - 2 \varepsilon_d)$$
3. Compute distance-7 mean error rate $\varepsilon_7 = \text{mean}(\varepsilon_{7, \text{patch}, B})$.
4. Target A1 passes if and only if:
   $$|\varepsilon_7 - 1.71 \times 10^{-3}| \le 0.005 \times 10^{-3}$$

---

## 7. Target A2 — Threshold Scaling Exponent $\Lambda$

### Target Reference:
- Published reference value: $\Lambda = 2.04$.
- Tolerance: $R_1 = 0.005$ (half-unit rule on second displayed decimal place).

### Recomputation Method:
Fit scaling relation across code distances $d \in \{3, 5, 7\}$ via deterministic weighted least-squares:
$$\ln(\varepsilon_d) = \ln(C) - \frac{d}{2} \cdot \ln(\Lambda)$$

Target A2 passes if and only if:
$$|\Lambda - 2.04| \le 0.005$$

---

## 8. Execution Governance & Artifact Requirements

Official execution runner `reproduce.py` must enforce:
1. **Clean Git Tree & Commit Verification:** `git status --porcelain` is empty and `git rev-parse HEAD == PREREG_SHA`.
2. **Immutable Input Recording:** `PREREGISTRATION.md`, `reproduce.py`, `requirements-minimal.txt`, and `data_manifest.json` hashed into `inputs.sha256`.
3. **Structured Evidence Output:** All outputs and logs written under `evidence/runs/<RUN_ID>/`:
   - `git_commit.txt`
   - `inputs.sha256`
   - `outputs.sha256`
   - `run_metadata.json`
   - `summary.json`
   - `stdout.log`
   - `stderr.log`
   - `exit_code.txt`
   - `command.sh`
   - `env.txt`
