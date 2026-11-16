# One-M principal module isotypes

This manuscript continues [C0010](../../claims/0010.md), allocates no new claim ID, and concerns finite F₂S₅ modules with exactly one M factor and otherwise trivial composition factors. Conditional on the [567-extension cover](bruck-s5-principal-enumeration.md) and [corrected splitting test](bruck-s5-principal-indecomposables.md), accepted by an independent check at source the recorded source revision, the 28 surviving extension representatives give 17 isomorphism types of indecomposable modules X₀. The enumerated representatives are not loop or envelope classes. This calculation and proof have the scoped independent review recorded below.

For two representations X,Y with generator matrices (C_X,D_X),(C_Y,D_Y), a linear map F is a module map if and only if F C_X=C_Y F and F D_X=D_Y F. Solve these linear equations over F₂ to obtain a basis for Hom(X,Y). X and Y are isomorphic exactly when some linear combination of the basis matrices has full rank. The [certificate](../code/classify_bruck_s5_principal_isotypes.py) exhausts every linear combination; it tests a candidate against one representative for each previously discovered type of the same dimension. If it finds full rank it records the matrix, while otherwise it has exhausted the Hom space. Thus each identification has a checkable isomorphism and each distinct pair of output representatives has an exhaustive negative test. In this run at most 5 basis vectors occur in a comparison; 56 comparisons suffice. The underlying enumeration and the correct unit test for R remain separate inputs, and the script retains the identity, swap, zero and identity-plus-swap unit controls of the corrected input.

The first representative for each class, labelled (quotient,a,b,index,cocycle,d,h₀), is:

```
0  M  0 0 0       0 4 0
1  M  0 1 1     194 6 0
2  M  0 1 2     136 6 1
3  M  1 0 1       8 5 0
4  J  0 0 0       0 5 1
5  J  0 1 1     577 7 2
6  J  0 1 2    1024 7 1
7  J  1 0 1       3 6 1
8  J  1 0 2      32 6 1
9  J  1 0 3      35 6 1
10 J  1 1 7   51235 8 2
11 J  1 1 9 1048579 8 1
12 J  2 0 6    1120 7 1
13 V6 0 0 0       0 6 1
14 V6 0 1 1  134273 8 2
15 V6 0 1 2  135168 8 1
16 V6 1 0 1    2112 7 1
```

The program emits all class members and witness matrices. The invariant vector (dimension, h₀, fixed-point dimension, endomorphism dimension, dimensions Hom(M,X), Hom(J,X), Hom(V₆,X), Hom(X,M), Hom(X,J), Hom(X,V₆)) distinguishes all except classes 7 and 8. For those, Hom(class 6,class 7) has dimension 1, while Hom(class 6,class 8) has dimension 2. Thus these invariant dimensions give an independent, compact certificate of pairwise nonisomorphism, alongside the exhaustive Hom-space test.

For principal blocks X₀⊕1ᵘ⊕Rᵛ, Krull–Schmidt makes the triple (X₀ isotype,u,v) unique: the summand carrying M is distinguished by its composition factors. Under the previously stated necessary inequality h₀+u+v≤d−4, the numbers of such triples by (d,h₀) are

```
(d,h₀)       types   permitted triples
(4,0)           1      1
(5,0)           1      3
(5,1)           1      1
(6,0)           1      6
(6,1)           5     15
(7,1)           3     18
(7,2)           1      3
(8,1)           2     20
(8,2)           2     12
                       --
                       79
```

The total includes M alone and gives necessary module candidates, not constructed stabilizers, extensions, sections or loops. Excluding the separately ruled-out M-alone module leaves 78 candidates if the cited exclusion applies. The principal-block dimension bound 14 remains unchanged.

Reproduction, from the repository root with Python 3.12.14 and the exact corrected source revision: run `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/classify_bruck_s5_principal_isotypes.py`. The program imports the sibling enumerator and its exact reviewed source must be retained or rechecked when it changes. It asserts all unit controls, all positive intertwining witnesses, the counts, and the distinguishing invariant signatures. The scoped independent review of the script and deduction is recorded below.

## Independent review

an independent check accepted this classification at exact source the recorded source revision, conditional on the reviewed cover, splitting test, envelope inequality and M-alone exclusion. The sibling enumerator was checked byte-unchanged from its reviewed f6 source. The review verified exhaustive Gray-code enumeration of the Hom spaces, full-rank intertwining witnesses, negative comparisons between all distinct same-dimensional class representatives, the separate distinguishing Hom invariants, and the Krull–Schmidt tail argument. An independent Python 3.12.14 run reproduced 28 inputs, 17 isotypes, 56 comparisons with maximal Hom dimension 5, and 79 necessary principal-block isotypes (78 after the prior exclusion). This neither bounds the N-block nor classifies or constructs envelopes or loops.

