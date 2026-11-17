# Executable controls

Run with Python 3.11 or later, assertions enabled. The latest reviewed checkpoint used Python 3.12.14. All dependencies are in the Python standard library or in this directory. These exact finite checks supplement the written proofs; they do not prove universal analytic convergence, coherence, inherited huge-loop construction, or classification completeness.

From this directory, the latest six controls are:

```sh
python verify_bol_dynamical_twist.py
python verify_bol_dynamical_fusion.py
python verify_bol_theta_fusion.py
python verify_bol_collective_transport.py
python verify_bol_shifted_analytic.py
python verify_bol_heat_repair.py
```

Each writes JSON to standard output. Compare with the corresponding `../evidence/bol-*-certificate.json`; no source code or stored JSON is rewritten by these commands. Certificate hashes bind the executable bytes. The exact [review record](../evidence/bol-dynamical-payoff-review.md#exact-reproduction-and-computational-scope) explains their finite ranges and exclusions.

Earlier controls include `verify_bol_fourier_sewing.py`, `verify_bol_charged_sewing.py`, `verify_bol_gaussian_sewing.py`, `verify_bol_genus_one.py`, `verify_bol_graded_fusion.py`, `verify_bol_cubic_isotopes.py`, `verify_bol_coordinate_packet.py` and `check_bol_modular_packet.py`. Their review records state the executions actually performed. A new public mirror does not imply that every earlier control was rerun.

Paths in preserved historical shell examples may use the original research layout. For this public package use the identical executable basenames in this directory. The research repository's `check.py` is not a public-package test and its historical 115-test results must not be mistaken for a fresh public-checkout run.
