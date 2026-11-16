# Concrete b=3 crossed-system generator

This deterministic constructor recovers the mathematical witness in `../bruck_b3_witness.json`; the independent verifier is `../verify_bruck_b3_noncentral.py`. These are source inputs and equations for one explicit finite group, not runtime logs or a census. The constructor uses the existing canonical P6, quadratic-support and one-M sources one directory above. It retains scratch derivations using selected definition prefixes; those textual interfaces are explicit in the source.

Run with Python3.12, assertions enabled, from this directory:

```sh
python3 bruck_b3_freeze.py --output /tmp/bruck-b3-regenerated.json
python3 ../verify_bruck_b3_noncentral.py
```

Compare the two JSON objects after parsing (formatting differs). `bruck_crossed_system_fast.py` constructs solutions of the generating equations; the separate verifier checks all crossed-action and factor-associativity identities and the actual orbit/collision calculation. Neither source classifies arbitrary quadratic maps, involutions or stabilizers. The proof and review status are in `../../manuscripts/bruck-b3-concrete-obstruction.md`. Keep generated data and logs outside Git.

