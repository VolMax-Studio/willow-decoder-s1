# Willow Decoder Audit — Pre-registration v4

**Instance:** `willow-decoder-s1`  
**Phase:** Specification Draft v4 (PRE-EXECUTION GATE DRAFT)  
**Target Run:** `run-003-recreation`  
**Audit Object:** Zenodo `10.5281/zenodo.13273331` (`google_105Q_surface_code_d3_d5_d7.zip`, MD5: `21fa6ad35b395d838ebcdbc92e364a12`)

---

## 1. Prior Exposure & Lineage Disclosure

This pre-registration v4 incorporates full prior exposure disclosure per P10 governance standards:

1. **Exploratory Run Lineage (`FAILURES #001`):** An exploratory execution (`run-001`) was performed prior to the formal preregistration freeze commit. Per `FAILURES #001`, `run-001` is classified as `Exploratory (not pre-registered)`.
2. **Confirmatory Run-002 Lineage & Evidentiary Remediation (`FAILURES #002`, `#003`, `#004`):**
   - `run-002-confirmatory` was executed under frozen PREREG_SHA_v3 `d16cfac78cb2d6777fb026c60a2488956c88e704`.
   - Scientific outputs were verified:
     - Population count: $N_{\text{Libra}} = 364$ distinct experimental configurations.
     - Matching-family Libra logical error rate for $d=7$: $\varepsilon_7 = 0.0017113465352358304$ (vs Nature published $1.71 \times 10^{-3}$, $|\Delta| = 1.35 \times 10^{-6} \le 5.00 \times 10^{-6}$).
     - Matching-family threshold scaling exponent: $\Lambda = 2.038282091967165$ (vs Nature published $2.04$, $|\Delta| = 0.0017 \le 0.0050$).
     - Complete archive scope evaluation: 0 matching neural/weight artifacts across 9,959 members.
   - Per `FAILURES #002` (B-W1), `run-002-confirmatory` omitted command-bound stream logs (`stdout.log`, `stderr.log`, `command.sh`, `env.txt`), rendering it non-ratifiable.
   - `run-003-recreation` is formally specified to recreate the verified scientific outputs while supplying the complete command-bound evidence package.
3. **Target B Non-Outcome-Blind Status:** Because the archive inventory has already been inspected, Target B is evaluated as a pre-registered reproduction of the archive inventory finding, not a blinded discovery.

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

## 7. Byte Accounting & Shot Population Invariant (B-W2 Resolution)

To ensure full accountability and eliminate runtime ambiguity:
1. **Per-File Shot Invariant:** Every evaluated `.b8` file must contain exactly 50,000 bytes ($1$ byte per shot for $N_{\text{shots}} = 50,000$). Any deviation halts execution (`EXECUTION_STATE_INVALID`).
2. **Global Input Byte Invariant:** Exactly 728 files must be read, accounting for exactly:
   $$\text{Total Bytes Read} = 728 \times 50,000 = 36,400,000\text{ bytes (34.71 MB)}$$
3. **Accounting Artifact:** Every run produces `bytes_read.json` recording total bytes, total files, and per-file byte counts and SHA-256 digests.

---

## 8. Evidentiary Packaging & Command-Bound Logging (B-W1, B-W3 Resolution)

Official execution must be launched via the frozen execution wrapper `runner.sh`, which enforces clean working tree state, verifies `git rev-parse HEAD == PREREG_SHA_v4`, captures literal standard output and error streams outside the tree during execution, and packages the complete 11-artifact evidence suite:

1. `command.sh`
2. `stdout.log`
3. `stderr.log`
4. `exit_code.txt`
5. `env.txt`
6. `git_commit.txt`
7. `inputs.sha256`
8. `outputs.sha256`
9. `run_metadata.json`
10. `summary.json`
11. `bytes_read.json`

For recreation runs (`run-003-recreation`), `recreation_comparison.json` is generated to certify exact scientific parity with `run-002-confirmatory`.

---

## 9. Immutable Input Inventory (7 Pinned Files)

`inputs.sha256` records the cryptographic digests of:
1. `PREREGISTRATION.md`
2. `reproduce.py`
3. `runner.sh`
4. `requirements-minimal.txt`
5. `data_manifest.json`
6. `SOURCE_MAPPING.json`
7. `archive_inventory.json`
