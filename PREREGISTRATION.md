# Willow Decoder Audit — Pre-registration v3

**Instance:** `willow-decoder-s1`  
**Phase:** Specification Draft v3 (PRE-EXECUTION GATE DRAFT)  
**Target Run:** `run-002-confirmatory`  
**Audit Object:** Zenodo `10.5281/zenodo.13273331` (`google_105Q_surface_code_d3_d5_d7.zip`, MD5: `21fa6ad35b395d838ebcdbc92e364a12`)

---

## 1. Prior Exposure & Lineage Disclosure

This pre-registration v3 incorporates full prior exposure disclosure per P10 governance standards:

1. **Exploratory Run Lineage (`FAILURES #001`):** An exploratory execution (`run-001`) was performed prior to the formal preregistration freeze commit. Per `FAILURES #001`, `run-001` is classified as `Exploratory (not pre-registered)`.
2. **Prior Numerical Observations from run-001:**
   - Population count: $N_{\text{Libra}} = 364$ distinct experimental configurations.
   - Matching-family Libra logical error rate for $d=7$: $\varepsilon_7 \approx 1.71 \times 10^{-3}$.
   - Matching-family threshold scaling exponent: $\Lambda \approx 2.04$.
3. **Prior Archive Inventory Observations (Claude Gate Review):**
   - The complete public Zenodo archive contains **9,959 members** (verified via central directory parsing).
   - The archive contains **five named decoder pipelines** under `decoding_results/`:
     1. `correlated_matching_decoder_with_rl_optimized_prior`
     2. `correlated_matching_decoder_with_si1000_prior`
     3. `harmony_decoder_with_rl_optimized_prior`
     4. `harmony_decoder_with_si1000_prior`
     5. `libra_decoder_with_rl_optimized_prior`
   - No explicitly named neural pipeline directory, model weight file, or neural prediction bitstream was identified in the archive inventory.
4. **Target B Non-Outcome-Blind Status:** Because the archive inventory has already been inspected, Target B is evaluated as a pre-registered reproduction of the archive inventory finding, not a blinded discovery.

---

## 2. Scope & Boundary Invariants

The audit evaluates two distinct targets with separate evidence chains:

1. **Target A (Matching-Family Deposited Numerical Reproduction):** Recomputation of matching-family Libra decoder error rates ($\varepsilon_7$) and scaling exponent ($\Lambda$) from the 728 deposited telemetry bitstreams mapped 1:1 to the public Zenodo archive.
2. **Target B (Complete Archive Scope Finding):** Systematic inventory of all 9,959 members of the public Zenodo archive to establish the presence or absence of identifiable neural decoder artifacts.

### Strict Non-Inference Invariant (§15):
- The absence of neural decoder artifacts in the public Zenodo archive establishes strictly that:
  $$\text{Reconstruction of the neural-decoder headline is }\mathbf{NOT\ DEMONSTRATED\ FROM\ DEPOSITED\ ARTIFACT\ ALONE}$$
- It **does not** establish that Google's neural headline claim ($0.143\%$ error rate, $\Lambda = 2.14$) is false, that neural decoding was not performed experimentally, or that model weights do not exist outside the archive.

---

## 3. Provenance & 728-Entry Source Lineage (W-2 Resolution)

### Archive Identity:
- **Zenodo Record:** `13273331`
- **DOI:** [`10.5281/zenodo.13273331`](https://doi.org/10.5281/zenodo.13273331)
- **Archive Filename:** `google_105Q_surface_code_d3_d5_d7.zip`
- **Archive Size:** `5,716,907,033` bytes (5.45 GB)
- **Remote Archive MD5 Digest:** `21fa6ad35b395d838ebcdbc92e364a12`

### 1:1 Member Mapping (`SOURCE_MAPPING.json`):
Every entry in `data_manifest.json` maps bijectively to exactly one original archive member:
1. `obs_flips_actual.b8`:
   - Local: `{patch}/{basis}/{round}/obs_flips_actual.b8`
   - Archive: `google_105Q_surface_code_d3_d5_d7/{patch}/{basis}/{round}/obs_flips_actual.b8`
2. `libra_predicted.b8`:
   - Local: `{patch}/{basis}/{round}/libra_predicted.b8`
   - Archive: `google_105Q_surface_code_d3_d5_d7/{patch}/{basis}/{round}/decoding_results/libra_decoder_with_rl_optimized_prior/obs_flips_predicted.b8`

### Lineage Invariants:
- Total manifest entries: `728`
- Total mapped entries: `728`
- Unmapped entries: `0`
- Ambiguous mappings: `0`
- CRC32 mismatches between local and archive members: `0`
- SHA-256 mismatches between local and manifest digests: `0`

---

## 4. Population Invariant (P1 / G1)

The Libra population $N_{\text{Libra}}$ is defined operationally and derived dynamically from `SOURCE_MAPPING.json` and `data_manifest.json`:
$$N_{\text{Libra}} = \text{count}(\text{distinct experimental roots}) = 364$$
across 14 patches ($9 \times d=3$, $4 \times d=5$, $1 \times d=7$), 2 bases ($X, Z$), and 13 primary rounds ($r \in [10, 250]$).

If derived count $\ne 364$, execution halts immediately (`POPULATION_MISMATCH`).

---

## 5. Target B — Complete Archive Scope Finding (G2)

### Test Procedure:
Enumerate all 9,959 members in `archive_inventory.json` and execute case-insensitive matching against path tokens:
```text
"neural", "weight", "weights"
```

### Controlled Output Vocabulary:
- If $\text{count}(\text{matching}) == 0$:
  $$\mathbf{NO\_EXPLICIT\_NEURAL\_PIPELINE\_OR\_WEIGHT\_ARTIFACT\_IDENTIFIED\_IN\_ARCHIVE\_INVENTORY}$$
- Report the complete list of 5 distinct decoder pipelines present in the archive.

---

## 6. Target A1 & A2 — Exact Weighted Least-Squares Model (W-1 Resolution)

### Exact Weighting Specification:

#### 1. Per-Round Decay Fit (`fit_decay`):
For each of the 28 series (14 patches $\times$ 2 bases):
- Empirical logical error probability across $N_{\text{shots}} = 50,000$:
  $$P_L(r) = \frac{1}{N_{\text{shots}}} \sum_{i=1}^{N_{\text{shots}}} (\text{actual}_i \oplus \text{predicted}_i)$$
- Bounded probability: $p = \text{clip}(P_L(r), 10^{-7}, 0.499999)$
- Transformed coordinate: $y = \ln(1 - 2p)$
- Binomial variance: $\sigma_p = \sqrt{\frac{p(1-p)}{N_{\text{shots}}}}$
- Propagated standard error: $\sigma_y = \frac{2 \sigma_p}{1 - 2p}$
- **Exact Inverse-Variance Weights:**
  $$w_i = \frac{1}{\sigma_y^2} = \frac{N_{\text{shots}} (1 - 2p)^2}{4 p (1 - p)}$$
- Model: $y(r) = \ln(1 - 2\varepsilon_{\text{init}}) + r \cdot \ln(1 - 2\varepsilon_d)$
- Slope $m = \ln(1 - 2\varepsilon_d) \implies \varepsilon_d = \frac{1 - e^m}{2}$

#### 2. Threshold Scaling Fit (`fit_lambda`):
- Distance coordinate: $x = d / 2$ for $d \in \{3, 5, 7\}$
- Mean error rate: $\bar{\varepsilon}_d = \text{mean}(\varepsilon_{d, \text{patch}, B})$
- Standard error: $\sigma_{\bar{\varepsilon}_d} = \frac{\sqrt{\sum \sigma_{\varepsilon}^2}}{N_{\text{fits}}}$
- Transformed coordinate: $y = \ln(\bar{\varepsilon}_d)$
- **Exact Inverse-Variance Weights:**
  $$w_d = \left(\frac{\bar{\varepsilon}_d}{\sigma_{\bar{\varepsilon}_d}}\right)^2$$
- Model: $y(x) = \ln(C) - x \cdot \ln(\Lambda)$
- Slope $m = -\ln(\Lambda) \implies \Lambda = e^{-m}$

### Acceptance Tolerances:
- **Target A1 ($\varepsilon_7$):** $|\bar{\varepsilon}_7 - 1.71 \times 10^{-3}| \le 0.005 \times 10^{-3}$ (half-unit rule on second displayed decimal).
- **Target A2 ($\Lambda$):** $|\Lambda - 2.04| \le 0.005$ (half-unit rule on second displayed decimal).

---

## 7. Execution Invariants & Evidence Packaging

Official execution runner `reproduce.py` enforces:
1. `git status --porcelain` is empty.
2. `git rev-parse HEAD == PREREG_SHA`.
3. `inputs.sha256` records:
   - `PREREGISTRATION.md`
   - `reproduce.py`
   - `requirements-minimal.txt`
   - `data_manifest.json`
   - `SOURCE_MAPPING.json`
   - `archive_inventory.json`
4. All outputs recorded under `evidence/runs/<RUN_ID>/` with `outputs.sha256`.
