# Reproducible finite checks

All eight programs are byte-identical copies of the scientific sources
identified in [VERIFICATION.md](../VERIFICATION.md). Their historical
manuscript filenames in docstrings are retained to preserve that identity;
the public mapping is below. The Python programs use only the standard
library. Python 3.11 or newer is sufficient; the C scan needs a C compiler
and the system math library.

## Run the checks

From the public note directory
`notes/combinatorics/fourier-entropy-influence`, run:

```sh
python -B code/check_spectral_forest_arithmetic.py
python -B code/check_positive_spectral_forest_fei.py
python -B code/check_cycle_facet_arithmetic.py
python -B code/check_dyadic_feedback_forest.py
python -B code/check_integer_forest_logsobolev.py
python -B code/check_forest_selector_interpolation.py
python -B code/check_beyond_forest_bridge.py
```

The compiled scan can be run independently:

```sh
cc -O3 code/scan_ternary_integer_forests.c -lm -o /tmp/fei-ternary-scan
/tmp/fei-ternary-scan 3
```

The optional exhaustive four-variable scan is:

```sh
/tmp/fei-ternary-scan 4
```

Its parameter range is one through four. The four-variable run examines
$`3^{16}=43{,}046{,}721`$ ternary truth tables. The default when no argument
is supplied is four, so pass `3` explicitly for the smaller replay.

## What each program checks

| Program | Public proof and exact range | Numerical parts and limits |
| --- | --- | --- |
| [check_spectral_forest_arithmetic.py](check_spectral_forest_arithmetic.py) | [Forest arithmetic](../forest-arithmetic.md): explicit four-bit path core and two 12-input prefix/bent completions, all 4,096 truth values and integer Walsh coefficients; exact rational entropy and influence. | Does not search all forest spectra or prove the general completion theorem. |
| [check_positive_spectral_forest_fei.py](check_positive_spectral_forest_fei.py) | [Positive forests](../positive-forests.md): all 65,814 Boolean truth tables through four variables; 37,926 tree energies; four- and six-bit core parameters; actual hard-zero Boolean stars for $`k=3,4,5`$. | The tree-energy sample has fields in $`\{-1,0,1\}`$ and couplings in $`\{-1,1\}`$, all labelled trees through four vertices and paths on five and six. It does not replace the simultaneous induction. |
| [check_cycle_facet_arithmetic.py](check_cycle_facet_arithmetic.py) | [Cycles and cacti](../cycles-and-cacti.md): all 252 odd-edge cycle normal forms of lengths three through eight, 43,680 point checks; 1,574,912 Boolean modular tests at primes three and five, including 11,680 eligible exact lifts; the $`K_5`$-facet counterexample; 200 constructed cacti with seed 20261116; all 2,047 nonempty cutsets of the eleven-vertex path square. | The 200 cacti are generated controls, not an exhaustion of all cacti. The cut-polytope theorem remains a classical external input. |
| [check_dyadic_feedback_forest.py](check_dyadic_feedback_forest.py) | [Spectral conditioning](../spectral-conditioning.md): two exact 12-input cycle realizations; all 65,814 Boolean functions through four variables, 60,500 eligible cutsets and 223,944 integer sections; 6,654 ternary functions and 342 eligible forest sections at scales 1, 2, and 8; exact odd-factor counterexamples. | Its finite forest classifier includes coordinate-subcube support but does not exhaust general deterministic-edge quotients. Excluding those cases only reduces the test scope. |
| [check_integer_forest_logsobolev.py](check_integer_forest_logsobolev.py) | [Integer forests](../integer-forests.md): exact scalar certificates and all ternary functions on one, two, and three variables, with 4, 48, and 704 positive forest spectra respectively. | Entropy ratios and comparisons on 1,400 integer-factor tensors through seven bits and 500 integer product functions through six bits use floating point. They are diagnostics, not interval certificates or universal proofs. |
| [check_forest_selector_interpolation.py](check_forest_selector_interpolation.py) | [Interpolation](../interpolation.md): all fourteen Bernstein coefficients in rational arithmetic; certified logarithm enclosures for 16,660 eligible ordered branch pairs through three data bits; bent selectors for $`m=1,2,3`$; first-hit lists for $`m=1,2`$ and $`1\le k\le6`$; explicit balanced gate and exact composition recurrences. | Decimal entropy displays come from certified enclosures. The 257-input obstruction is evaluated by the proved recurrence, not by enumerating its truth table. |
| [check_beyond_forest_bridge.py](check_beyond_forest_bridge.py) | [Mixtures and obstructions](../mixtures-and-obstructions.md): all 65,814 Boolean functions through four variables, including 65,752 noncharacter minimum-layer checks; all sixteen majority-supported Boolean functions; exact tree projection; the four-bit core's eight-bit independent fair-completion lower bound. | Does not prove a universal mixture or denominator budget. The six-bit core is checked by the positive-forest program above. |
| [scan_ternary_integer_forests.c](scan_ternary_integer_forests.c) | [Integer forests](../integer-forests.md): exact Walsh transforms, positivity, multiplicative pairwise/forest recognition, counts, and largest odd Walsh part for all ternary functions on the requested dimension, at most four. | Printed entropy ratios and reported ratio maximizers are floating-point diagnostics. At four variables the author-run exact counts were 43,776 positive forests and largest odd part nine; independent replay was through three variables. |

## Interpreting a successful run

The universal inequalities are proved in the manuscripts. These programs
guard exact examples, formulas, integer divisibility, support handling,
certificate transcription, and finite classifications. They do not prove
FEI for an untested class and do not establish historical priority.

Some older checks retain weaker forest completion bounds of six or ten
fair bits. Those inequalities remain valid. The Boolean minimum-layer
refinement gives the stronger bounds eight and twelve; the bridge checker
verifies the former, and the latter follows from the six-bit parameters
and the displayed general proof.


## Positive bounded-treewidth continuation

From this directory, run:

```sh
python -B check_bounded_treewidth_integer_spectra.py
python -B check_connected_triangle_spectral_family.py
python -B check_forest_slack_continuation.py
```

These three files are byte-identical to scientific revision
`566b6a1a6ac3ff0b8ef1684d467b5ec904bcbe57`; all three were rerun here.
They use the standard library. The first verifies the nine integer scalar
certificates, the two strict constant comparisons, 65,814 Boolean functions,
6,654 ternary functions, and 300 exact gcd bag factorizations with seed
20261116. The eligible raw-entropy comparisons use integer exponentiation,
not floating logarithms.

The connected-family program checks the complete twelve-bit base function
and the exact core laws for one through four blocks, including their cubic
interactions, tree decomposition, feedback cut, entropy and influence.
Its optional `--full-two-block` argument requires NumPy and verifies every
signed Walsh coefficient of the actual 24-variable two-block function.
That optional run was performed by both the author and a nonauthor reviewer,
but was not repeated during public adaptation.

The zero-edge program checks 89,480 admissible physical sections, exact
energy stars, the integer star at N=16 and M=2, the seven-bit path, and the
six-bit Boolean two-star counterexample. The latter has 25 positive Fourier
atoms and exact half-integer sections on the second forbidden-edge cut.
These finite checks supplement the complete analytic proofs in
[bounded treewidth](../bounded-treewidth.md),
[connected triangles](../connected-triangles.md) and
[zero edges](../zero-edges.md); they are not extrapolated to prove a theorem.
