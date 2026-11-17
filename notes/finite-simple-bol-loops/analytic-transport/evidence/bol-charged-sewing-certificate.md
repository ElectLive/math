# Exact certificate for charged fusion and geometric degree

Calculation and verification record.

The principal source is
[CH1--CH6](../manuscripts/bol-charged-heisenberg-obstruction.md). The final
control also validates the small instance in root-authored
[LC3](../manuscripts/bol-local-current-obstruction.md). The analytic
exchange architecture has its own
[companion manuscript](../manuscripts/bol-charged-exchange.md); no numerical
claim below certifies its continuum analytic statements.

## Reproduction

From the repository root:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_charged_sewing.py --certificate problems/0323-finite-simple-non-moufang-bol-loops/evidence/bol-charged-sewing-certificate.json
```

This was run with Python 3.12.14 and assertions enabled. It uses only the
standard library, with exact arithmetic over $\mathbb F_3$, integer
polynomial coefficients modulo three, $\mathbb Z[\zeta_3]$, and
rational degree values. The final script SHA-256 is

```text
a5c3f12f0d348b83c7fd27b56d4b2807bfc3b2f8e401536afa1427cde1010630
```

The command writes the [complete JSON](bol-charged-sewing-certificate.json)
and prints a concise summary. Without `--certificate`, the script prints
the complete report. It returns nonzero on a failed assertion. This is a
manual execution; no repository CI result or formal verification is claimed.

## Charged action and fusion

The representation convention is exactly CH2:


```math

 \rho_\ell(x,y,z)\phi(u)
  =\psi(\ell(z+b(u,y)+b(x,y)/2))\phi(u+x).

```


On delta functions, its permutation is $t\mapsto t-x$, with phase
$\ell(z+b(t,y)-b(x,y)/2)$. This sign matters for the subsequent
projective holonomy and degree conventions.

The script checks all 6,561 combinations of central charge, two group
elements, and delta basis vector in the one-dimensional $\mathbb F_3$
model. It compares operator composition with the actual BCH group product.

For charged fusion it uses a two-dimensional matrix pencil with every
nonzero scalar form invertible:


```math

 B_{(a,b)}=aI+b\begin{pmatrix}0&2\\1&0\end{pmatrix}.

```


There are 72 ordered charge pairs with regular sum. For each it tests
every pair of delta functions against all first-axis, second-axis, and
central generators, yielding 34,992 exact intertwining checks. The
weighted-center map is tested together with its inverse. The script
retains the transpose in $L_\ell x(y)=x^tB_\ell y$; it does not
silently identify a nonsymmetric form with its transpose.

All 336 triples with regular inputs, two intermediate sums, and total
sum are then tested. On the four basis vectors of the multiplicity
coordinate space, the explicit F-move and its inverse agree with the
coordinates computed from the original three variables: 1,344 checks.
The universal pentagon is the coordinate-change proof in CH2, not an
inference from these finite tests.

## Dual zero channels

The certificate enumerates the common invariant Weyl basis and the center
of its restricted twisted algebra. It also evaluates each finite Weyl
trace exactly. The cases are:

| Irreducible dimension | Holonomy span | Common zero algebra |
|---:|---|---|
| 3 | Nondegenerate plane | $\mathbb C$ |
| 9 | Nondegenerate plane | $\operatorname{Mat}_3(\mathbb C)$ |
| 9 | Isotropic plane | $\mathbb C^9$ |
| 9 | Nonzero line | $\mathbb C^3\otimes\operatorname{Mat}_3(\mathbb C)$ |
| 9 | Zero span | $\operatorname{Mat}_9(\mathbb C)$ |

The isotropic-plane case is an explicit check that a nonscalar zero
algebra need not be nonabelian in the smallest two-degree model. No
scalar-zero-mode simplification is imposed on a product sector.

## Geometric degree and carry coherence

For 27 charges and a specified nonzero central commutator, the script
checks all 729 carry values and all 19,683 instances of


```math

 n(\ell,\mu)+n(\ell+\mu,\nu)
 =n(\mu,\nu)+n(\ell,\mu+\nu).

```


The 18 charges detecting that commutator have a nonzero cyclic carry
sum, as required for the nonsplit degree extension. Twenty-four direct
Weyl-basis calculations check the sign of
$UV=e^{-2\pi ik/3}VU$, including positive and negative degree labels.

In the control with central commutator $-1$, normalized labels are
$0,1,2$. The three-dimensional nontrivial-charge bundles have degrees
one and two; the nine-dimensional versions have degrees three and six.
The normalized charge-dual labels $1,2$ add to three and therefore
carry a degree-one line. The true categorical dual uses $1,-1$ and
adds to zero. These are geometric labels, with no conformal-weight claim.

The certificate verifies finite automorphy signs and carry arithmetic.
The holomorphic bundle, curvature, divisor, and line-valued map statements
are proved in CH4; no finite test is treated as an analytic existence proof.

## Compact rigid data and the cocycle boundary

The three $B_i$ matrices are copied exactly from equations (1)--(2) at
the pinned [rigid source 2a25b81](https://github.com/Mira-Cult/math-wip/blob/2a25b81e3efe5bdd8a3923e27c94aef16a559094/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/odd-rigid-center-nongloop.md#data).
Polynomial dictionaries verify coefficientwise, without interpolation,


```math

 \det(xB_0+yB_1+zB_2)=(y^2-yz-z^2+xz)^2

```


and all sixteen entries of the adjugate factorization in CH22. Exact
Gaussian elimination gives full-bimap rank histogram $\{0:1,2:8,4:18\}$.
This is the rank of $b_\ell$, not its alternating part. The nondegenerate
field-trace argument in the manuscript multiplies these ranks by eighteen,
giving $\{0:1,36:8,72:18\}$ in the huge construction.

For the three shifts $f_k(a)=f(a)-k\epsilon^2$, the script verifies
the torus-bimap covariance, positive-cocycle condition, and 729 exact
graph-transport gauge identities. It also checks 2,187 charge-junction
phase identities. The fixed raw $\epsilon^2$-character sees the
three phases $1,0,2$ modulo three; those fixed boundary phases are
distinct even though the graph-only closed networks are gauge-equivalent.
This documents the information loss, rather than claiming that the
neutral repair already separates the isotopes.

No field of order $3^{18}$, huge loop table, or induced seed is constructed.
The selected-loop, properness, and strict-isomorphism interfaces remain
the inherited inputs listed in the canonical manuscripts.

## The cubic proper-Bol local-current control

For each $k=0,1$ at $p=3$, the script builds the 27-point cubic
loop table and generates the equivalence relation forced by all 19,683
associativity triples. It then closes under both left and right contexts
until stable, making 4,374 context checks in each case. The resulting
nine classes are exactly


```math

                  \{(c,a,b):c\in\mathbb F_3\}
                    \quad ((a,b)\in\mathbb F_3^2).

```


The induced quotient operation is checked against addition on
$\mathbb F_3^2$. For $x=(0,1,0),y=(0,0,1),z=x$, both parameters
give the exact witness


```math

               (xy)z=(2,2,1),\qquad x(yz)=(1,2,1).

```


This validates LC3's small instances. Its universal quotient theorem and
LC1's Jacobi argument are the separate proofs in that manuscript. These
calculations do not establish a fusion-compatible nonabelian analytic
connection or an interacting Bol vertex structure.
