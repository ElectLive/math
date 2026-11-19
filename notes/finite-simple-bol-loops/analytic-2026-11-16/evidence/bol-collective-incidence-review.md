# Verification of the trace–exponential counting theorem

The [manuscript](../manuscripts/bol-collective-incidence.md) gives uniform mathematical proofs for the exact degree and collision formulas, the sharp variance bounds, the 37-point seven-symbol theorem, and the comparison with the aligned family. A separate OpenAI model checked the mathematics, including the normalizations, equality cases, regularization and finite numerical certificates. Its final editorial check accepted the same scientific text with only byline and display-math changes. This is not human peer review, formal verification or a claim of historical priority.

The two programs are standalone Python (3.11+ standard library). From this directory:

```sh
python3 -B ../code/verify_bol_incidence.py
python3 -B ../code/verify_bol_incidence_independent.py
```

The first checks rational bounds and compressed combinatorial counts ([output](bol-incidence-author.out)). The independently written second checks actual finite-field and radical computations at the stated small scopes ([output](bol-incidence-independent.out)). Neither enumerates the general ambient set or replaces the uniform proofs. The coordinator separately replayed both programs. The inherited full-space norm and the established leftover-hash conversion are explicitly distinguished from the new family-specific arithmetic results.

Mira Cult directed the research. OpenAI models assisted with finding the mathematical arguments, writing the research account, and independently reviewing it. Exact version assignments were not verified.
