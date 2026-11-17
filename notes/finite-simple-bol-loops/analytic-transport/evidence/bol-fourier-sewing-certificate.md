# Exact certificate for commutator Fourier sewing

Calculation and verification record.

The canonical statements and proofs are in
[Commutator Fourier sewing](../manuscripts/bol-fourier-sewing.md).
The finite calculations below validate its explicit controls, transfer
convention, coefficient extraction, and rigid local application. The
earlier [class-fusion construction](../manuscripts/bol-translation-class-fusion.md)
and [correlation geometry](../manuscripts/bol-correlation-geometry.md)
own the inherited class-seed and pinned-coordinate interfaces.

## Reproduction and arithmetic

From the repository root, run with assertions enabled:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_fourier_sewing.py --certificate problems/0323-finite-simple-non-moufang-bol-loops/evidence/bol-fourier-sewing-certificate.json
```

The script uses Python's standard library. It was run with Python 3.12.14.
It uses exact arithmetic over $\mathbb F_3$, the two explicitly
presented fields of order 81, integers, rational numbers, and
$\mathbb Z[\zeta_3]$. No floating-point approximation is used. Its
SHA-256 is

```text
4d8a76734ecc22f014d498c4d7f5dd3b511dfce437cf5977257977b68a424b17
```

The [machine-readable output](bol-fourier-sewing-certificate.json)
also contains the digest of the executed script. With the displayed
option the script prints a concise summary; without that option it
prints the full JSON. It returns a nonzero status if any assertion fails.

The standardized convention is


```math

 A(Tx,y)=B(x,y),\qquad
 F_A\eta_y=|W|^{-1/2}\sum_x\psi(A(x,y))\eta_x,
 \qquad F_AF_B^{-1}=P_T,\quad P_T\eta_x=\eta_{Tx}.

```


In alternating matrix coordinates this is $T=A^{-1}B$. Replacing it
by its inverse would preserve cycle counts but would change the stated
operator identity. The canonical proof fixes this convention, and the
noninvolutory quartic matrix checks test the defining relative-form
equation and its covariance. The small explicit Fourier-product check
uses $T=-1=T^{-1}$, so that check alone does not distinguish the two
orientations.

## 1. Exact Fourier identity and shared-variable networks

On $W=\mathbb F_3^2$, use
$A=\left(\begin{smallmatrix}0&1\\2&0\end{smallmatrix}\right)$
and $B=2A$, so $T=-1$. The script checks all 81 entries of
$F_AF_B^{-1}=P_T$, without taking numerical square roots: the
normalization is removed before comparing the exact cyclotomic sums.

It also directly sums the cyclic network at lengths one and two,
using 6,642 terms in total. The normalized values are 1 and 9, agreeing
with $|\ker(T^k-1)|$. A deterministic point relabeling, with seed
323438, preserves the cycle type $1^1 2^4$.

## 2. Equal-fusion quartic controls and invariant transfer packets

For each of


```math

 f_1(t)=t^4+t+2,\qquad f_2(t)=t^4+t^2+2,

```


the script excludes all monic linear and quadratic divisors, constructs
the corresponding field of order 81, and checks inverses of all 80
nonzero elements. The alternating pencil is


```math

 A_{(a,b)}=
 \begin{pmatrix}0&aI+bC_i\\-(aI+bC_i)^t&0\end{pmatrix},
 \qquad C_i=\operatorname{companion}(f_i).

```


Both scalar-rank histograms are $\{0:1,8:8\}$. Hence every
nonzero character has zero radical, and the entire intersection/fusion
profile is identical. The corresponding local central sets have 6,569
points: one regular central orbit of size 9 and 6,560 fixed points.

For the distinguished pair $A=A_{(1,0)},B=A_{(0,1)}$, the script
constructs the actual 6,561-point permutation of $W$, obtaining:

| Control | Order of $T$ | Cycles on $W$ | Cycles after identity extension to $A_C$ |
|---|---:|---|---|
| $f_1$ | 80 | $1^1 80^{82}$ | $1^9 80^{82}$ |
| $f_2$ | 16 | $1^1 16^{410}$ | $1^9 16^{410}$ |

The result is not restricted to these chosen generators. All 48 ordered
independent character pairs are tested in each control:

| Order | Count for $f_1$ | Count for $f_2$ |
|---:|---:|---:|
| 5 | 0 | 4 |
| 10 | 0 | 4 |
| 16 | 0 | 8 |
| 20 | 16 | 0 |
| 40 | 0 | 16 |
| 80 | 32 | 16 |

The second control's pair $(1,1),(1,2)$ has order five. All 48
changes of central basis are checked for each control, for 96 checks
in total. A simultaneous change of basis of $W$ conjugates the
computed relative operator as required. For every one of the 96
relative operators and every power 1 through 80, the script checks
the predicted rank of $T^k-1$, including its evenness: 7,680 exact
power-rank checks.

These are class-two group controls. The certificate does not assert
that either particular quartic pencil has been realized in the selected
simple proper Bol construction.

## 3. Actual odd-mode traces and logarithmic recovery

The power series are expanded directly from the finite cycle
determinants at positive odd oscillator modes, with 24 fermion species.
Thus the coefficient check is independent of the displayed discriminant
quotient evaluation. The local distinguished ratio has its first
nonconstant term at degree 16:


```math

 \frac{\Psi_1}{\Psi_2}=1+9840q^{16}+O(q^{17}).

```


The same check at induced index two gives coefficient 19,680. In
general induction multiplies this first coefficient by $I$; the
group-control choice $G=Q$, $I=6561$, gives 64,560,240.
The canonical modular formula is


```math

 \frac{[\Delta(80\tau)/\Delta(160\tau)]^{82I}}
 {[\Delta(16\tau)/\Delta(32\tau)]^{410I}},

```


with a common weight-zero law on $\Gamma_0(320)$.

The script computes $D\log$ from the expanded trace, performs the
odd-divisor Möbius inversion, and recovers the actual fixed-point
counts. It tests 176 coefficients across the two quartic controls and
the reduced rigid transfer. Every recovered count is an even power
of three, as required by alternating self-adjointness.

## 4. Rigid local geometry, norm probes, and all regular pairs

Use the three exact matrices $B_0,B_1,B_2$ in the pinned rigid
construction. The actual translation commutator is represented by
$B_i^t-B_i$. The validation replaces the extension field
$\mathbb F_{3^{18}}$ by $\mathbb F_3$, only to test the local
class-two arithmetic. It does not claim that the reduced object has
the simplicity or properness of the huge loop.

The resulting local class set has 363 points. The script constructs
its central cosets explicitly, all 27 charge radicals, and all
12 nondegenerate scalar forms. It checks the nondegeneracy of their
restrictions to every radical, giving 324 checks. All 144 ordered
regular pairs give the four relative operators $1,-1,T,-T$, each
with multiplicity 36. On independent pairs their multiplicities are
24, 24, 36, 36. Every transfer preserves each radical and each
commutator image $J_w$.

For
$A=A_{(0,0,1)}$, $B=A_{(1,0,1)}$, the full-charge transfer
is an involution with cycle type $1^{99}2^{132}$. Writing
$z_+=(1,0,1)$, $z_-=(1,0,0)$, its mixed profiles are


```math

 TR_{z_+}:2^{132}3^{33},\qquad
 TR_{z_-}:2^{96}3^{33}6^{12}.

```


All four transfers against all 27 central elements are checked, for
108 tests. The exact normalized cyclotomic factors of the four-sector
determinants agree precisely when the sparse permutation operator
$(T-1)(R_z-1)$ is zero. The existential factorization locus over
nonidentity transfers is exactly


```math

 \langle(0,0,1)\rangle\ \cup\ \langle(1,0,1)\rangle.

```


It contains $z_+$ and excludes $z_-$. The normalized odd-mode
trace ratio for the latter starts with $1+1728q+O(q^2)$.

The script also checks the BCH correction specifying the marked
translation origins on all 81 local vectors, and computes the
positive-cocycle norm word
$f(a^3)+f(a^2)-f(a)=(1+T_{\rm center})^2f(a)$.
It gives exactly $z_+$ and $z_-$ for the two pinned cocycles.

For the huge loop these calculations are used symbolically, with
$M=3^{36}$, $I=3^{146}19^6$, and $|C|=3(M+2)^2$:

| Quantity | Exact value |
|---|---|
| Fixed classes of full transfer | $9M+18$ |
| Its two-cycles | $3(M^2+M-2)/2$ |
| Six-cycles of $TR_{z_+}$ | 0 |
| Six-cycles of $TR_{z_-}$ | $3(M-1)/2$ |
| First normalized induced ratio defect | $216I(M-1)q$ |

No set of the huge loop's size, or of its induced seed's size, is
enumerated. These formulas are proved in the canonical manuscript;
the reduced computation validates their local algebra, not their
inherited selected-loop hypotheses.

There is also an explicit limitation check. The six charges that are
simultaneously nondegenerate after matching both positive-cocycle
phase flags give only the same scalar transfers $\pm1$, in all
36 pairs. Zero-charge Fourier sewing alone does not resolve the
isotope pair. The successful test uses the full-charge transfer and
the live cocycle norm probe together.

## 5. Individual-spectrum and mode-resolved current ablations

Two 12-point permutation actions have the same individual profiles
$S:1^6 2^3$, $R:1^6 3^2$, and both faithfully represent
$C_2\times C_3=C_6$. In the first action the moving supports are
disjoint; in the second six points carry the regular $C_6$-action
and six are fixed. Their product profiles are respectively
$2^3 3^2$ and $1^6 6^1$. The four-sector identity holds in the
first and fails in the second, with first ratio coefficient 144.
Their full joint group characters differ; the control preserves the
individual spectra and abstract group relations only.

The certificate also tests the common-source extension using the
original off-diagonal currents


```math

 \exp(tE_a^{1,3})\exp(uE_b^{3,1}),\qquad
 a_x=x-5,\quad b_x=(x^2+2\bmod7)-3\quad(0\le x<12).

```


It directly enumerates the 311 signed exterior trace states of energy
at most three for one species in modes 1 and 3. Intermediate states
of larger energy are retained. It applies creation and annihilation
operators with their exact exterior signs, rather than using either
the determinant formula or the desired factorization. Eight traces
are evaluated, then raised to the 24th power to implement 24 species.

All 36 coefficients with $q$-degree at most three and each source
degree at most two agree between $Z_{SR}Z_1$ and $Z_SZ_R$ in
the disjoint control. This includes nonzero mixed coefficients such
as $[qtu]=336$ and $[q^2t^2u^2]=52176$. The overlapping control
already fails at its zero-source $q$ coefficient by 144. This is
a check of actual mode-switching correlations, not only a zero-point
partition-function check.

## Scope

This is a manual exact execution, not a repository CI result.
The certificate supports exact finite and formal-series instances of
the stated theorems. It does not replace their proofs, independently
reverify the canonical simplicity/properness or strict-isomorphism
results, establish a proper-Bol realization of the quartic controls,
or establish historical priority. Exterior determinant modularity
and the common-source support factorization are general mechanisms.
The additional input here is the commutator-derived admissible
transfer and the finite geometric support condition tested against
the positive-cocycle norm.
