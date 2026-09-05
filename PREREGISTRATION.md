# willow-decoder-s1
## Preregistration

Status: preregistered before recomputation

---

## 1. Audit object

This audit evaluates publicly deposited artifacts associated with the
Willow surface-code decoding dataset.

The audit does not evaluate the scientific competence, intentions, or
internal implementation of the original authors.

The audit is limited to claims that can be tested from the deposited
artifacts and their pinned provenance.

---

## 2. Provenance

Source archive:

Zenodo:
10.5281/zenodo.13273331

Archive MD5:

21fa6ad35b395d838ebcdbc92e364a12

The audit input is the deposited archive and the locally preserved
manifest derived from its complete listing.

No subsequent modification of the source archive is admissible.

---

## 3. Frozen archive manifest

The complete archive listing is preserved as:

data_manifest_full.txt

The structured manifest is preserved as:

data_manifest.json

The manifest, rather than shell-output transformations, is the
authoritative source for deriving population counts.

Directory counts must not be inferred from counts of files or ZIP entries.

---

## 4. Population derivation

The Libra population is defined operationally as:

N_Libra =
number of experimental roots containing:

decoding_results/libra_decoder_with_rl_optimized_prior/

The population is therefore a property derived from the preserved
archive manifest.

The value MUST NOT be entered manually into the reproduction harness.

The expected population observed during preparation is:

N_Libra = 364

This value is a preregistration target for the deterministic population
derivation and is not accepted merely because it is written here.

If the harness derives a different value, the audit HALTS and the
difference is reported.

---

## 5. Target B — deposited-artifact scope finding

The audit tests whether the deposited archive contains artifacts
identifiable as neural-network predictions or model weights.

The search is performed over the preserved archive manifest.

Operational indicators include filenames containing terms such as:

- neural
- weight

The result is reported as:

count of matching deposited artifacts

The interpretation is deliberately restricted to:

"absence from deposited artifact"

It MUST NOT be interpreted as proof that no neural component existed
elsewhere in the original experimental pipeline.

Expected result from the preparation inspection:

0 matching deposited artifacts.

---

## 6. Target A1 — Libra logical error

The harness recomputes the logical error from the deposited Libra
bitstreams.

The computation is performed directly from:

- obs_flips_actual.b8
- obs_flips_predicted.b8

No value from the original reported fit is used as an input to the
recomputation.

The fit produces ε_d across the available code distances.

The preregistered target is:

ε_7 = (1.71 ± 0.03) × 10^-3

Acceptance threshold:

R1 = 0.005 × 10^-3

If the independently recomputed value falls outside the registered
acceptance criterion, the result is reported as FAIL.

No manual alteration of the fit, filtering, or parameter selection is
permitted after inspection of the result.

---

## 7. Target A2 — Lambda

The same preregistered fit used for Target A1 produces Λ.

The preregistered target is:

Λ = 2.04 ± 0.02

Acceptance threshold:

R1 = 0.005

The result is recomputed without importing the reported value into the
calculation.

If the result fails the registered criterion, the audit HALTS.

---

## 8. Gate structure

### G0 — Provenance and integrity

Required:

- source archive identified
- archive hash recorded
- complete listing preserved
- manifest internally consistent

Failure:

HALT.

### G1 — Population

Required:

- population derived from manifest
- N_Libra independently computed by harness

Expected:

N_Libra = 364

Failure:

HALT.

### G2 — Bitstream integrity

Required:

- all expected Libra artifacts present
- file hashes consistent with manifest
- bitstream dimensions/lengths internally valid

Failure:

HALT.

### G3 — Reproduction

Required:

- ε_7 recomputed from deposited bitstreams
- Λ recomputed from the preregistered procedure
- no manual fitting intervention

Failure:

HALT and report the observed discrepancy.

---

## 9. Blindness and independence

The audit is not a replication of proprietary SCADA/BMS/internal data.

It evaluates only publicly deposited artifacts.

The reproduction procedure is fixed before examining the numerical
outcome of the recomputation.

Any model-assisted interpretation must be treated as an analytical
reading of the registered artifacts, not as an independent experimental
measurement.

---

## 10. Reporting rule

The audit MUST distinguish:

1. verified/reproduced numerical results;
2. scope findings concerning deposited artifacts;
3. failures of the registered gates;
4. claims that cannot be resolved from the deposited evidence.

No unresolved claim may be upgraded to VERIFIED by inference.

If a gate fails, subsequent targets are not silently repaired or
recomputed under modified criteria.

---

## 11. Expected output

The harness produces:

results/summary.json

The summary records:

- source archive identity
- manifest identity
- derived N_Libra
- integrity checks
- Target B count
- recomputed ε_7
- recomputed Λ
- gate statuses
- final audit disposition

The JSON output is generated by the harness and is not manually edited.
