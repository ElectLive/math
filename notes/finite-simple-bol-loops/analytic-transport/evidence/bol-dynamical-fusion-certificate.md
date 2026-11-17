# Exact certificate for the separate-symbol fusion obstruction

Calculation and verification record.

## Reproduction

From the repository root, with assertions enabled:

    python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_dynamical_fusion.py --certificate /tmp/bol-dynamical-fusion-recheck.json

Without the option, the program prints the entire deterministic JSON.
The committed expected result is
[bol-dynamical-fusion-certificate.json](bol-dynamical-fusion-certificate.json).
The author ran the final script under Python 3.12.14; it exited zero and
reported PASS. It uses only standard-library integer, rational and finite
field operations. Script SHA-256:

    911024063a6b874a717a343c4b8cccce309d8cd0f72117a7c84145f17725f156

## Exhaustive nine-point support test

The grid is F_3 times F_3. The program exhausts all 9!=362,880 permutations.
For each permutation, it pushes a basis of the separate function space
f(x)+g(y) and tests all mixed rectangle differences exactly. Independently,
it tests equivariance from simultaneous input translation to translation
of the output's first coordinate.

| Predicate | Exact count |
| --- | ---: |
| Preserves the separate symbol space | 72 |
| Product or swapped-product grid permutation | 72 |
| Intertwines the first-axis translations | 162 |
| Satisfies both conditions | 0 |

The first two sets are compared as sets of permutations, not just counts.
The canonical (1,1) fusion permutation belongs to the equivariant set and
does not normalize the separate symbol space. Exact rational elimination
gives dimension four for each separate traceless space, eight for their
joint span and nine after adjoining the identity.

This exhausts permutation supports, not all complex matrices. The symbolic
normalizer proof in SY1 is what reduces an arbitrary invertible matrix to
this kind of support; SY2--SY3 prove the universal obstruction. The finite
enumeration alone does not prove those reductions.

## Actual charged representations

All six charge pairs in F_3 with nonzero sum are retained, including pairs
with one zero input charge. For all nine delta-basis pairs and all twenty-seven
Heisenberg elements, the weighted-center coordinate map and its inverse are
checked, and the input and output phases agree. This gives 1,458 exact
intertwiner equations. Phases are represented by their exponents modulo three;
no floating-point roots of unity are used.

## Joint parameter spaces

Finite Fourier supports are checked for p=3,5,7,11. The two original axes,
the difference direction and every regular scalar charged center direction
are pairwise disjoint away from zero and cover all nonzero frequency vectors.
The resulting dimensions are:

| p | One regular splitting, unital span | All regular splittings, unital span | Full traceless dimension |
| ---: | ---: | ---: | ---: |
| 3 | 9 | 9 | 8 |
| 5 | 17 | 25 | 24 |
| 7 | 25 | 49 | 48 |
| 11 | 41 | 121 | 120 |

The symbolic projective-line proof gives the general odd-prime statement.
These checks establish neither a flat connection on that enlarged space
nor a coherent analytic tensor law.

## Product-reached fixed algebras

For two three-dimensional irreducible sectors, the separately fixed
algebras are scalar. The certificate directly enumerates the joint invariant
Weyl labels in F_3^4, then their center under the restricted alternating form.

| Charges | Joint dimension | Center dimension | Matrix block size |
| --- | ---: | ---: | ---: |
| (1,1) | 9 | 1 | 3 |
| (1,2) | 9 | 9 | 1 |

Thus regular-total and zero-total channels have equal invariant dimensions
but different algebra structures. The general conclusion is an application
of CH3 as stated in SY5, not a newly inferred classification from the table.

## Limits

These are local Heisenberg controls, not enumerated simple proper Bol loops.
No huge matrix, loop table or field extension is generated. Full separate
principal-symbol images are essential hypotheses; arbitrary shared-q systems
or unspecified trace-sector restrictions are not tested. Neither analytic
convergence nor flatness nor a pentagon is certified by this program.
The inherited classification, marked-folder and isotope interfaces are not
independently re-proved. No repository CI or formal certification is claimed.
