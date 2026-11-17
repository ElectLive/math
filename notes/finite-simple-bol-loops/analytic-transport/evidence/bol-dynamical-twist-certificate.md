# Exact finite dynamical-twist certificate

Calculation and verification record.

The mathematical source is
[DD1--DD8](../manuscripts/bol-dynamical-fusion-construction.md).
The certificate tests a finite dynamical tensorator with a shifted
pentagon, true-dual maps and the degree/carry and unitarity inputs to
the auxiliary bundle action. It does not numerically test the Chern
connection theorem, test the unresolved continuous Cartan connection,
or claim a new Bol-specific analytic identity.

## Reproduction

From the repository root, with assertions enabled:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_dynamical_twist.py --certificate /tmp/bol-dynamical-twist.json
```

Without `--certificate`, the command prints its entire deterministic
JSON. With that flag, it writes the JSON and prints a concise summary.
The committed [complete output](bol-dynamical-twist-certificate.json)
was produced under Python 3.12.14, exit zero. All arithmetic is exact
over F_3 and the integers, or uses integer exponents of a primitive
cube root of unity.
The script uses only the standard library. Its SHA-256 is

```text
d00fa6c0257bb05456ea6f8489c7491139c7644530dff49fd20ace2e26d65581
```

No remote CI, formal verification, analytic convergence or independent
review is inferred from this author run.

## The small model and its coordinate convention

Use p=3, W=F_3^2, Z=F_3, B_lambda=lambda I, and the scalar bilinear
matrix C=((0,2),(1,0)). Each C+lambda I is invertible. If a bilinear
form is x^t M y, its map W -> W* has coordinate matrix M^t. The
executable retains this transpose in every projector and controlled
translation; it does not silently identify a nonsymmetric matrix with
its transpose.

This is a finite Heisenberg-coordinate control. It is not asserted to
be a new simple proper Bol loop. Its role is to validate the universal
finite representation and tensor formulas before using their symbolic
form on the huge pinned input.

## Projective representations and expectation intertwiners

For all three auxiliary parameters and all 243^2 ordered group pairs,
the code compares projective composition with the actual BCH product
and the additional common multiplier. It uses t=0 and the two basis
vectors of W, giving 531,441 checks. The phase discrepancy is affine in
t by the displayed formula, so this set tests that whole t-dependence.

The exact expectation map in DD3 is then checked against each first-axis,
second-axis and central generator. All three physical central charges,
including zero, all nine physical delta vectors and all nine auxiliary
delta vectors are included: 3,645 generator equations.

## Shifted fusion, zero channels and true duals

The script evaluates the two sides of the shifted equation on every
delta-basis triple for all three auxiliary parameters and all physical
charge triples: 59,049 checks.

The opposite physical sectors H_1 and H_2 have the full 81-character
neutral decomposition. Each of those characters, including nontrivial
second-axis characters, is explicitly inserted in each of the three
positions alongside H_1,H_2. Every remaining delta pair and every
auxiliary parameter is tested, giving another 59,049 exact equations.
Thus the zero-charge test is not restricted to the special reducible
H_0 model, whose second-axis characters would all be trivial.

For every fourfold physical charge tuple and auxiliary parameter, all
five binary fusion trees agree on the eight coordinate basis vectors:
1,944 comparisons of all five tree maps. In these controls the maps are
linear over F_3, so the basis comparison verifies the complete finite
coordinate map. The universal categorical pentagon is separately proved
by composition of the actual expectation intertwiners in DD4.

The transported evaluation and coevaluation use

    ev^J(lambda)=ev J_(X*,X)(lambda),
    coev^J(lambda)=J_(X,X*)(lambda)^-1 coev.

Both triangle identities are tested on every delta vector for all
physical charges and auxiliary parameters: 162 checks. The first
triangle evaluates the coevaluation at lambda-mu; the second evaluates
the evaluation at lambda+mu. Dropping these shifts would not be the
stated dynamical duality.

Actual parameter dependence is exhibited by taking X=Y=H_1, x=0,
y=(1,0). The first output coordinates for auxiliary lambda=0,1,2 are
(2,1), (0,2), (1,1), respectively.

## Twisted Fourier algebras and reconstruction

For each auxiliary parameter the code constructs all 81^2 Fourier
product phase coefficients, totaling 19,683 pairs. It checks all
81^3 associativity triples in each fiber, totaling 1,594,323 equations.
Only the zero Fourier label commutes with every label, so the center
dimension is one, whereas the identity-twist pointwise algebra has
center dimension 81.

It recovers the two-by-two matrix of F_lambda^-1 from the coordinate
Fourier products, inverts it, and verifies that subtracting F_0 gives
lambda I. Thus all three parameter forms are recovered even though
every abstract algebra has dimension 81 and is Mat_9(C).

The non-gauge-triviality theorem uses the universal fact, proved in DD5,
that a dynamical gauge yields isomorphic fiber algebras. The finite
center counts support the example; they do not replace that argument.

## Auxiliary bundle action, integer carries and true duals

The full expectation map of DD5a includes its multiplicity input:
V_lambda tensor X[mu] -> V_(lambda-mu) tensor X. For the three
physical Schroedinger sectors and all auxiliary parameters the
script checks all 729 basis images form the required permutations.
For every one of the 81 neutral characters it checks the corresponding
phase-permutation map at every auxiliary parameter, giving 2,187
additional basis images. These include the nontrivial neutral
characters absent from H_0 alone.

For every residue of the physical commutator c and auxiliary
multiplier d_C, every auxiliary parameter and physical charge pair,
and three integer degree lifts per physical charge, it checks the
integer carries and their shifted telescoping identity: 2,187
checks. The same integer equality is the slope equality used for
both the dz and d_tau terms of the Chern one-form. It also checks
243 true-dual channels with exactly opposite integer degrees,
whose total auxiliary carry is zero.

The universal unitary assertion uses Schur's lemma and the orthogonal
expectation projectors. The full analytic identity is proved by
differentiating the explicitly given CH metric in both z and tau;
neither theorem is inferred from these finite controls. The input
X[mu] in the bundle action is explicitly a constant multiplicity
space, whereas its output X is the physical bundle.

## Compact rigid completion

The source field scalar has order 19. The executable checks its full
Frobenius exponent orbit under multiplication by 3 modulo 19, giving
degree 18, and verifies 18>4. It checks the displayed symmetric S is
invertible and obeys R^t S=S R for the two unipotent Jordan blocks.

The regularity of alpha S+M_lambda for every rigid central character
is the symbolic minimal-polynomial argument in DD6: its determinant is
a nonzero polynomial of degree four over F_3, so it cannot vanish at
an element of degree eighteen. No element table for F_(3^18), huge
representation matrix, multiplication table, or induced loop set is
constructed.

## Limits

The new parameter is discrete. The auxiliary projective representations
are distinct from the original physical linear sectors. The twist
retains all physical charges and transports geometric degrees/carry
lines. The auxiliary bundle action is constant in the covering frames;
DD5a proves that it is horizontal for independently specified CH Chern
connections. Theta scalarization adds standard carry-line zeros or
poles. This run does not establish noncoincident compatibility with
the continuous CE dynamical variables, a modular isotope separator,
a classification restriction, or arithmetic moonshine.
The positive cocycle remains separately marked; graph-only erasure is
not repaired by these finite identities.
