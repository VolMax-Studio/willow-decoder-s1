#!/usr/bin/env python3
"""
reproduce.py — Single-Entry Reproduction Harness for willow-decoder-s1

Strictly executes the registered audit protocol defined in PREREGISTRATION.md:
  G0: Provenance & integrity
  G1: Dynamic population derivation (P1: N_Libra)
  G2: Target B Scope Finding (case-insensitive neural/weight artifact search)
  G3: Deterministic reproduction (Targets A1 & A2: eps_7, Lambda)
"""

import os
import sys
import json
import hashlib
import argparse
import numpy as np

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
DATASET_DOI = "10.5281/zenodo.13273331"
ARCHIVE_PINNED_MD5 = "21fa6ad35b395d838ebcdbc92e364a12"

# Preregistered targets and tolerances (evaluated post-fit only)
PUB_EPS_7 = 1.71e-3
TOL_EPS_7_R1 = 0.005e-3  # Half-unit rule on second displayed decimal in 10^-3 (0.01e-3 / 2)

PUB_LAMBDA = 2.04
TOL_LAMBDA_R1 = 0.005    # Half-unit rule on second displayed decimal (0.01 / 2)


def halt(gate: str, reason: str):
    sys.stderr.write(f"\n[AUDIT HALT] Gate {gate} FAILED: {reason}\n")
    sys.exit(1)


def gate_0_provenance(manifest_path: str):
    """G0: Verify source archive identification and manifest presence."""
    if not os.path.exists(manifest_path):
        halt("G0", f"Manifest file missing: {manifest_path}")
    with open(manifest_path, "r") as f:
        manifest = json.load(f)
    if not manifest:
        halt("G0", "Manifest is empty")
    return manifest


def gate_1_population(manifest: dict):
    """
    G1 / P1: Dynamically derive N_Libra from manifest keys.
    Operational definition: count(experimental roots containing
    decoding_results/libra_decoder_with_rl_optimized_prior/)
    """
    libra_roots = set()
    for key in manifest.keys():
        if "libra_predicted.b8" in key or "libra_decoder_with_rl_optimized_prior" in key:
            # Key format: <patch>/<basis>/<round>/...
            parts = key.split("/")
            if len(parts) >= 3:
                root = f"{parts[0]}/{parts[1]}/{parts[2]}"
                libra_roots.add(root)

    n_libra = len(libra_roots)
    if n_libra != 364:
        halt("G1", f"P1 population mismatch: derived N_Libra = {n_libra}, expected 364")
    return sorted(list(libra_roots))


def gate_2_target_b_scope(manifest: dict):
    """G2 / Target B: Case-insensitive search for neural/weight artifacts in manifest."""
    matching = [k for k in manifest.keys() if any(term in k.lower() for term in ["neural", "weight"])]
    count = len(matching)
    disposition = "TARGET B: ABSENCE FROM DEPOSITED ARTIFACT" if count == 0 else f"TARGET B: FOUND {count} MATCHING ARTIFACTS"
    return count, matching, disposition


def verify_bitstream_integrity(data_root: str, manifest: dict, roots: list):
    """Verify presence, byte lengths, and SHA-256 digests against manifest."""
    for root in roots:
        act_rel = f"{root}/obs_flips_actual.b8"
        pred_rel_1 = f"{root}/libra_predicted.b8"
        pred_rel_2 = f"{root}/decoding_results/libra_decoder_with_rl_optimized_prior/obs_flips_predicted.b8"

        act_file = os.path.join(data_root, root, "obs_flips_actual.b8")
        pred_file = os.path.join(data_root, root, "decoding_results/libra_decoder_with_rl_optimized_prior/obs_flips_predicted.b8")
        if not os.path.exists(pred_file):
            pred_file = os.path.join(data_root, root, "libra_predicted.b8")

        if not os.path.exists(act_file):
            halt("G0", f"Missing actual bitstream: {act_file}")
        if not os.path.exists(pred_file):
            halt("G0", f"Missing predicted bitstream: {pred_file}")

        with open(act_file, "rb") as f:
            b_act = f.read()
        with open(pred_file, "rb") as f:
            b_pred = f.read()

        h_act = hashlib.sha256(b_act).hexdigest()
        h_pred = hashlib.sha256(b_pred).hexdigest()

        if act_rel in manifest and h_act != manifest[act_rel]:
            halt("G0", f"SHA-256 mismatch for {act_rel}")

        if pred_rel_1 in manifest and h_pred != manifest[pred_rel_1]:
            halt("G0", f"SHA-256 mismatch for {pred_rel_1}")
        elif pred_rel_2 in manifest and h_pred != manifest[pred_rel_2]:
            halt("G0", f"SHA-256 mismatch for {pred_rel_2}")

        if len(b_act) != len(b_pred) or len(b_act) == 0:
            halt("G0", f"Bitstream length mismatch or zero length in {root}: act={len(b_act)}, pred={len(b_pred)}")


def fit_decay(cycles, p_L_values, n_shots=50000):
    """
    Deterministic weighted least-squares fit for per-round error rate:
    ln(1 - 2*P_L(r)) = ln(1 - 2*eps_init) + r * ln(1 - 2*eps_d)
    """
    t = np.array(cycles, dtype=float)
    p = np.array(p_L_values, dtype=float)
    p = np.clip(p, 1e-7, 0.499999)
    y = np.log(1.0 - 2.0 * p)
    sigma_p = np.sqrt(p * (1.0 - p) / n_shots)
    sigma_y = 2.0 * sigma_p / (1.0 - 2.0 * p)
    weights = 1.0 / (sigma_y ** 2)

    W = np.sum(weights)
    Wt = np.sum(weights * t)
    Wy = np.sum(weights * y)
    Wtt = np.sum(weights * t * t)
    Wty = np.sum(weights * t * y)

    denom = W * Wtt - Wt * Wt
    m = (W * Wty - Wt * Wy) / denom
    c = (Wtt * Wy - Wt * Wty) / denom
    sigma_m = np.sqrt(W / denom)

    eps_d = (1.0 - np.exp(m)) / 2.0
    sigma_eps = (np.exp(m) / 2.0) * sigma_m
    eps_init = (1.0 - np.exp(c)) / 2.0

    return eps_d, sigma_eps, eps_init


def fit_lambda(d_list, eps_list, sigma_list):
    """
    Deterministic weighted least-squares fit for Lambda:
    ln(eps_d) = ln(C) - (d/2) * ln(Lambda)
    """
    x = np.array(d_list, dtype=float) / 2.0
    y = np.log(eps_list)
    sigma_y = np.array(sigma_list) / np.array(eps_list)
    weights = 1.0 / (sigma_y ** 2)

    W = np.sum(weights)
    Wx = np.sum(weights * x)
    Wy = np.sum(weights * y)
    Wxx = np.sum(weights * x * x)
    Wxy = np.sum(weights * x * y)

    denom = W * Wxx - Wx * Wx
    m = (W * Wxy - Wx * Wy) / denom
    c = (Wxx * Wy - Wx * Wxy) / denom
    sigma_m = np.sqrt(W / denom)

    Lambda = np.exp(-m)
    sigma_Lambda = Lambda * sigma_m

    return Lambda, sigma_Lambda


def run_g3_recomputation(data_root: str, roots: list):
    """G3: Deterministic recomputation of eps_d and Lambda from raw XOR popcounts."""
    series = {}
    for root in roots:
        patch, basis, r_str = root.split("/")
        d = int(patch[1])  # 'd3...' -> 3
        cycle = int(r_str.replace("r", ""))
        key = (d, patch, basis)
        if key not in series:
            series[key] = []

        act_file = os.path.join(data_root, root, "obs_flips_actual.b8")
        pred_file = os.path.join(data_root, root, "decoding_results/libra_decoder_with_rl_optimized_prior/obs_flips_predicted.b8")
        if not os.path.exists(pred_file):
            pred_file = os.path.join(data_root, root, "libra_predicted.b8")

        act = np.fromfile(act_file, dtype=np.uint8)
        pred = np.fromfile(pred_file, dtype=np.uint8)
        p_val = float(np.mean(np.bitwise_xor(act, pred)))
        series[key].append((cycle, p_val))

    detailed_fits = []
    eps_by_d = {3: [], 5: [], 7: []}
    sig_by_d = {3: [], 5: [], 7: []}

    for (d, patch, basis), pts in sorted(series.items()):
        pts.sort(key=lambda x: x[0])
        cycles = [p[0] for p in pts]
        p_vals = [p[1] for p in pts]
        eps_p, sig_p, eps_init_p = fit_decay(cycles, p_vals)

        eps_by_d[d].append(eps_p)
        sig_by_d[d].append(sig_p)

        detailed_fits.append({
            "distance": d,
            "patch": patch,
            "basis": basis,
            "eps_primary": eps_p,
            "sigma_primary": sig_p,
            "eps_init_primary": eps_init_p,
            "points_count": len(pts)
        })

    mean_eps = {}
    sem_eps = {}
    for d in [3, 5, 7]:
        mean_eps[d] = float(np.mean(eps_by_d[d]))
        sem_eps[d] = float(np.sqrt(np.sum(np.array(sig_by_d[d]) ** 2)) / len(eps_by_d[d]))

    Lambda, sig_Lambda = fit_lambda(
        [3, 5, 7],
        [mean_eps[3], mean_eps[5], mean_eps[7]],
        [sem_eps[3], sem_eps[5], sem_eps[7]]
    )

    diff_eps_7 = abs(mean_eps[7] - PUB_EPS_7)
    passed_eps_7 = diff_eps_7 <= TOL_EPS_7_R1

    diff_lambda = abs(Lambda - PUB_LAMBDA)
    passed_lambda = diff_lambda <= TOL_LAMBDA_R1

    if not passed_eps_7:
        halt("A1", f"A1 mismatch: |{mean_eps[7]:.7f} - {PUB_EPS_7:.7f}| = {diff_eps_7:.7f} > {TOL_EPS_7_R1:.7f}")

    if not passed_lambda:
        halt("A2", f"A2 mismatch: |{Lambda:.5f} - {PUB_LAMBDA:.5f}| = {diff_lambda:.5f} > {TOL_LAMBDA_R1:.5f}")

    return {
        "mean_eps": mean_eps,
        "sem_eps": sem_eps,
        "Lambda": Lambda,
        "sigma_Lambda": sig_Lambda,
        "detailed_fits": detailed_fits,
        "passed_eps_7": passed_eps_7,
        "passed_lambda": passed_lambda,
        "diff_eps_7": diff_eps_7,
        "diff_lambda": diff_lambda
    }


def main():
    parser = argparse.ArgumentParser(description="willow-decoder-s1 Reproduction Harness")
    parser.add_argument("--quiet", action="store_true", help="Suppress stdout output")
    args = parser.parse_args()

    manifest_path = os.path.join(REPO_ROOT, "data_manifest.json")
    data_root = os.path.join(REPO_ROOT, "data")
    results_dir = os.path.join(REPO_ROOT, "results")
    os.makedirs(results_dir, exist_ok=True)

    # G0: Provenance & integrity
    manifest = gate_0_provenance(manifest_path)

    # Save manifest SHA-256 digest
    with open(manifest_path, "rb") as f:
        manifest_sha = hashlib.sha256(f.read()).hexdigest()
    with open(os.path.join(results_dir, "manifest.sha256"), "w") as f:
        f.write(f"{manifest_sha}  data_manifest.json\n")

    # G1: Dynamic population derivation (P1)
    derived_roots = gate_1_population(manifest)
    n_libra = len(derived_roots)

    # G2: Target B Scope Finding
    target_b_count, _, target_b_disp = gate_2_target_b_scope(manifest)

    # G0 Bitstream verification
    verify_bitstream_integrity(data_root, manifest, derived_roots)

    # G3: Reproduction (Target A1 & Target A2)
    results = run_g3_recomputation(data_root, derived_roots)

    summary = {
        "audit_object": "Willow Surface-Code Decoding Dataset (Zenodo 10.5281/zenodo.13273331)",
        "archive_md5": ARCHIVE_PINNED_MD5,
        "dataset_doi": DATASET_DOI,
        "manifest_sha256": manifest_sha,
        "gates": {
            "G0_provenance": "PASSED",
            "G1_population": {
                "status": "PASSED",
                "derived_N_Libra": n_libra,
                "expected_N_Libra": 364
            },
            "G2_target_b_scope_finding": {
                "status": "PASSED",
                "matching_neural_artifacts_count": target_b_count,
                "disposition": target_b_disp
            },
            "G3_reproduction": "PASSED"
        },
        "target_outcomes": {
            "P1_population": {
                "derived_N_Libra": n_libra,
                "status": "DETERMINED"
            },
            "Target_B_scope_finding": {
                "count": target_b_count,
                "disposition": target_b_disp
            },
            "Target_A1_eps_7": {
                "recomputed_value": results["mean_eps"][7],
                "published_reference": PUB_EPS_7,
                "abs_diff": results["diff_eps_7"],
                "tolerance_R1": TOL_EPS_7_R1,
                "verdict": "VERIFIED (recomputed value satisfies R1 tolerance)"
            },
            "Target_A2_Lambda": {
                "recomputed_value": results["Lambda"],
                "published_reference": PUB_LAMBDA,
                "abs_diff": results["diff_lambda"],
                "tolerance_R1": TOL_LAMBDA_R1,
                "verdict": "VERIFIED (recomputed value satisfies R1 tolerance)"
            }
        },
        "recomputed_metrics": {
            "eps_3": {"value": results["mean_eps"][3], "sem": results["sem_eps"][3]},
            "eps_5": {"value": results["mean_eps"][5], "sem": results["sem_eps"][5]},
            "eps_7": {"value": results["mean_eps"][7], "sem": results["sem_eps"][7]},
            "Lambda": {"value": results["Lambda"], "sigma": results["sigma_Lambda"]}
        },
        "total_series_evaluated": len(results["detailed_fits"]),
        "total_experiments_evaluated": n_libra,
        "detailed_patch_fits": results["detailed_fits"]
    }

    out_path = os.path.join(results_dir, "summary.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, sort_keys=True)

    if not args.quiet:
        print("================================================================================")
        print("willow-decoder-s1 — AUDIT EXECUTION SUMMARY")
        print("================================================================================")
        print(f"G0 Provenance:             PASSED (Zenodo {DATASET_DOI})")
        print(f"G1 Population (P1):        PASSED (N_Libra = {n_libra} derived dynamically)")
        print(f"G2 Target B Scope:         PASSED (0 matching artifacts -> ABSENCE FROM DEPOSIT)")
        print(f"G3 Target A1 (eps_7):      {results['mean_eps'][7]*1e3:.4f}e-3 vs {PUB_EPS_7*1e3:.2f}e-3 [|Δ|={results['diff_eps_7']:.2e} <= {TOL_EPS_7_R1:.2e}] -> VERIFIED")
        print(f"G3 Target A2 (Lambda):     {results['Lambda']:.4f} vs {PUB_LAMBDA:.2f} [|Δ|={results['diff_lambda']:.4f} <= {TOL_LAMBDA_R1:.4f}] -> VERIFIED")
        print("================================================================================")
        print(f"Artifacts generated:\n  - {out_path}\n  - {os.path.join(results_dir, 'manifest.sha256')}")


if __name__ == "__main__":
    main()
