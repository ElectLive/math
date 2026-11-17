# Separated charged transport: stable cocycle recovery and an effective Bol control

**Mira Cult**



The analytic object is new: a collective Fuchsian transport with two separated
singularities and specified boundary marks. It is not an identification of the
old Fock traces with Felder solutions. Its useful conclusions are a quantitative
inverse theorem for the retained cocycle, from finitely many nonsingular
transport measurements, and a dimension-independent separated-transport gap in
the established cubic Bol controls. The construction uses ordinary linear ODEs
and the actual finite marked operators; no new general Fuchsian theory or
literature-priority assertion is intended.

## SA1. Domain, connection, and a normally convergent response

Let `X` be a finite-dimensional complex Hilbert space, and let `A,B` be
operators of norm at most one. Put `a=1/4`, `b=3/4` and `L=log 3`. The
insertion coordinate `t` lies in


```math

 D=\mathbb C\setminus\bigl(( -\infty,0]\cup[1,\infty)\bigr).
 \tag{SA1.1}

```


The poles `0,1,infinity` and the two boundary points `a,b` are distinct.
The two complex numbers `u,v` are external control amplitudes. The connection
is in the `t` direction; no assertion of flatness in the amplitude directions
is made. Its normalized transport is the solution


```math

 \frac{dU}{dt}
  =\left(\frac{uA}{t}+\frac{vB}{1-t}\right)U,
 \qquad U(a;u,v)=I.                                  \tag{SA1.2}

```


For the tensor-compatible version the residues are augmented, `A-I,B-I`,
so that the tensor unit has zero connection. Write its transport as `V`.
The relation with (SA1.2) is the explicit scalar normalization


```math

 U(t;u,v)=
 \exp\left(u\log(t/a)+v\log\frac{1-a}{1-t}\right)V(t;u,v),
 \quad U(b;u,v)=e^{L(u+v)}V(b;u,v).                  \tag{SA1.3}

```


The logarithms are the branches real on `(0,1)`. Formula (SA1.3) is a
normalization of the measured observable, not an assertion that an unaugmented
connection has a flat tensor unit.

**Proposition SA1 (existence and operator bound).** Equation (SA1.2) has a
unique holomorphic solution on `D`. Its endpoint value is entire in `(u,v)`.
Along the real interval `[a,b]` its Dyson series converges in operator norm,
normally on compact sets of amplitudes, and


```math

                \|U(b;u,v)\|\le e^{L(|u|+|v|)}.      \tag{SA1.4}

```


The series and all its amplitude derivatives are independent of partitions
used for integration. Continuation along homotopic paths in `D` gives the
same transport. No endpoint regularization, subtraction of a divergent trace,
or infinite-dimensional trace is used.

**Proof.** Set `K(t)=uA/t+vB/(1-t)`. Iteration of the integral equation gives


```math

 U(b)=I+\sum_{n\ge1}
 \int_{a<t_1<\cdots<t_n<b}
             K(t_n)\cdots K(t_1)\,dt_1\cdots dt_n.   \tag{SA1.5}

```


The norm of its `n`th term is bounded by
`[L(|u|+|v|)]^n/n!`. The Weierstrass bound proves absolute normal convergence,
entire amplitude dependence and termwise differentiation. Picard iteration
or subtraction of two solutions proves uniqueness. The same argument applies
on every compact piecewise smooth path avoiding the poles; ordinary
holomorphic ODE continuation and uniqueness on overlapping disks imply
homotopy invariance on the simply connected slit domain. Each finite iterated
integral is an ordinary integral of a continuous function on a compact simplex.
The uniform summable bound makes the limiting result independent of a
convergent sequence of integration partitions. Summation gives (SA1.4). QED.

For a boundary projection `P` of rank `d>0`, the response


```math

             R_P(u,v)=d^{-1}\operatorname{Tr}(P U(b;u,v))       \tag{SA1.6}

```


obeys the same bound since `|Tr(PT)|<=d||T||`. A family of such responses
is transported by any unitary marked-data isomorphism carrying `A,B,P`
together. It is not invariant under changing one boundary mark while fixing
the others.

## SA2. The two time orders give an invertible analytic measurement

Define the positive constants


```math

 c_1=\int_{a<s<t<b}\frac{ds\,dt}{t(1-s)},\qquad
 c_2=\int_{a<s<t<b}\frac{ds\,dt}{(1-t)s}.             \tag{SA2.1}

```


They have


```math

 c_1+c_2=L^2,\qquad
                  c_2-c_1\ge\frac13.               \tag{SA2.2}

```


The first equality partitions the square into its two triangles. For the
second,


```math

 \frac1{(1-t)s}-\frac1{t(1-s)}
   =\frac{t-s}{s(1-s)t(1-t)}\ge16(t-s),

```


because `s(1-s),t(1-t)<=1/4`. The integral of `t-s` on the triangle is
`(b-a)^3/6=1/48`. Both coefficients are completely specified ordinary
integrals, so numerical quadrature is not part of the theorem. If desired,
`c1=log(3/4) log 3+Li_2(3/4)-Li_2(1/4)`; the integral definition suffices.

Now use the retained split-torus data of
[CH1 and CH5](bol-charged-heisenberg-obstruction.md) and
[DD7](bol-dynamical-fusion-construction.md#dd7-marked-torus-transport-and-the-positive-cocycle-boundary).
Let `Z` be a finite `F_p`-space, `T` an invertible linear map of `Z`, and
`psi(x)=exp(2 pi i x/p)`. Write `Lambda=Z*` and
`sigma(kappa)=kappa composed with T^{-1}`. The physical charge register is


```math

                   X=\bigoplus_{\kappa\in\Lambda}X_\kappa.

```


Every `X_kappa` is nonzero; the canonical `H_kappa=Fun(W)` satisfies this
condition even at zero or a degenerate charge. Let `A_0` be the actual unitary
pure split-torus transport `X_kappa -> X_sigma(kappa)`. For a fixed marked
value `f=f(a)` of the positive cocycle, define


```math

 G_f|_{X_\kappa}=\psi(\sigma(\kappa)(f)) A_0|_{X_\kappa},
 \qquad H=A_0^{-1}.                                 \tag{SA2.3}

```


These are the actual graph and pure-torus operators. The theorem uses only
the one retained value `f(a)`, its pure split reference, and their displayed
actions; it does not alter any source cocycle law. In the pinned rigid input,
`f` is a crossed group 1-cocycle on the actual torus: the element `a` has
order nine, while its action `T(a)` on `Z` has order three, and
`f(a^3)=epsilon^2`, `f(a^9)=0`. Those distinctions are retained. In the ambient
semidirect group each displayed graph element is a genuine marked element.

Let `P_kappa` be the projection onto `X_kappa`, and use `A=G_f`, `B=H` in
(SA1.2). With `d_kappa=dim X_kappa`, put
`R_kappa=d_kappa^{-1}Tr(P_kappa U(b))`. On each charge block,


```math

 G_f H=\psi(\kappa(f))I,
 \qquad H G_f=\psi(\sigma(\kappa)(f))I.              \tag{SA2.4}

```


The internal coordinate maps cancel in both products. In particular no
irreducibility or invertibility of the physical charge form is required.

**Theorem SA2 (stable marked cocycle recovery).** The mixed endpoint
derivatives of these noncoincident responses satisfy


```math

 M_\kappa:=\partial_u\partial_v R_\kappa(0,0)
    =c_1 s_\kappa+c_2 s_{\sigma(\kappa)},
 \qquad s_\kappa=\psi(\kappa(f)).                    \tag{SA2.5}

```


Thus the full labeled family `M` recovers `f` uniquely. On the space of
charge-indexed complex vectors with the sup norm, the inverse linear map
from `M` to `s` has norm at most three.

**Proof.** The mixed degree-two term in (SA1.5) is
`c1 G_f H+c2 H G_f`. Its normalized block trace is (SA2.5), by (SA2.4).
If `S` permutes a charge vector by `(Ss)_kappa=s_sigma(kappa)`, then
`M=(c1 I+c2 S)s`. Since `||S||=||S^{-1}||=1` and `c1<c2`, its inverse is
the convergent Neumann series


```math

 (c_1I+c_2S)^{-1}
   =\frac1{c_2}\sum_{n\ge0}(-c_1/c_2)^n S^{-n-1}.

```


Its norm is at most `1/(c2-c1)<=3`. Finally the characters of the elementary
abelian group `Z` separate points, so `s` determines `f`. This is an exact
finite Fourier reconstruction after the analytic measurement has been
inverted. QED.

The dynamical parameter in DD is an auxiliary charge and is distinct from
the physical boundary label `kappa` here. In the collective construction,
its actual shifted fusion maps transport the entire operator-valued response,
and hence these boundary matrix elements, after the boundary projections
are transported. The theorem does not identify those two kinds of charge.

## SA3. Recovery from a fixed finite set of nonsingular measurements

An infinitesimal derivative is unnecessary. For any real `r>0`, define


```math

 M_\kappa(r)=
 \frac{R_\kappa(r,r)-R_\kappa(r,0)-R_\kappa(0,r)+1}{r^2}.
                                                               \tag{SA3.1}

```


The fourth value `R_kappa(0,0)=1` is known exactly.

**Theorem SA3 (effective finite-amplitude inverse theorem).** For all charges,


```math

       |M_\kappa(r)-M_\kappa|
              \le r L^3 e^{2rL}.                    \tag{SA3.2}

```


Suppose each of the three measured normalized responses in (SA3.1) has
absolute error at most `delta`. Apply `(c1 I+c2 S)^{-1}` to the resulting
vector. Its error from the phase vector `s` is at most


```math

       3\left(rL^3e^{2rL}+\frac{3\delta}{r^2}\right).             \tag{SA3.3}

```


If this number is strictly less than `sin(pi/p)`, nearest-`p`th-root rounding
recovers every phase and therefore `f` exactly. The constants are independent
of `dim W`, the module ranks, `|Z|`, and the dimension of any neutral matrix
block. For `p=3`, the fixed amplitude `r=1/100` and error
`delta<=1/2,000,000` satisfy the condition.

**Proof.** Inclusion-exclusion in (SA3.1) cancels every purely `u` or purely
`v` term in the absolutely convergent series. The norms of the remaining
mixed terms of degree at least three sum to at most


```math

 \frac{(e^{rL}-1)^2-(rL)^2}{r^2}.

```


For `x>=0`, use `e^x-1-x<=x^2 e^x/2` and
`e^x-1+x<=2x e^x`; their product gives
`(e^x-1)^2-x^2<=x^3e^{2x}`. This proves (SA3.2). Each normalized block trace
has absolute value at most the corresponding operator norm, so the bound
does not incur a dimension factor. Three measurement errors contribute
`3delta/r^2`, and SA2 multiplies that by at most three. Distinct `p`th roots
are separated by at least `2 sin(pi/p)`, proving the rounding claim.

For the numerical example, `L<11/10` and
`e^{2rL}<500/489` imply `rL^3e^{2rL}<0.014`. The error term
`3delta/r^2` is at most `0.015`. The right side of (SA3.3) is therefore
less than `0.087<sqrt(3)/2`. The decimal inequalities here are conservative
rational bounds; no numerical ODE solve establishes the theorem. QED.

This is a quantitative analytic reconstruction statement about a new
observable. Its information content is the existing marked phase tensor,
which can of course also be read directly if supplied as finite data. What
is proved here is that three fixed, separated, bounded transport responses
per charge recover it with a dimension-independent error guarantee, even
when the separate graph and split spectra contain no such information.
It does not claim that finite data become an infinite invariant or that a
complete finite marked operator algebra cannot determine the response.

### SA3a. Stability under a noncentral collective residue

The graph and split-torus subgroup alone need not expose the nontrivial
conjugation of a finite dynamical fusion symbol. A retained first-axis
operator provides a controlled additional test. Let `C` have norm at most
two; in the charged construction take `C=rho(X_s)-I` for a fixed noncentral
first-axis element. Add the independently specified term `wC/(2-t)` to
(SA1.2), with `w` an external control. The extra pole `2` is also separated
from the interval. Put `K=log(7/5)` and denote this transport and its boundary
responses by `U_w,R_{kappa,w}`. If the whole complex domain is needed,
use the universal cover of `C\{0,1,2}`, or a simply connected neighborhood
of `[a,b]` avoiding those poles; the previous slit domain is sufficient
for this particular extra pole as well.

**Corollary SA3a (robust recovery with a nonzero third residue).** For
`|u|,|v|<=r`,


```math

 \|U_w(b;u,v)-U_0(b;u,v)\|
   \le \varepsilon_w:=2|w|K\exp(2rL+2|w|K).          \tag{SA3.5}

```


Use four actual responses with the same nonzero `w` and set


```math

 M_{\kappa,w}(r)=\frac{R_{\kappa,w}(r,r)-R_{\kappa,w}(r,0)
       -R_{\kappa,w}(0,r)+R_{\kappa,w}(0,0)}{r^2}.

```


After the same inverse in SA2, the phase error is at most


```math

 3\left(rL^3e^{2rL}+\frac{4\varepsilon_w}{r^2}
                                      +\frac{4\delta}{r^2}\right),        \tag{SA3.6}

```


if the four normalized measurements have errors at most `delta`.
For `p=3`, `r=1/100`, `w=r^4` and `delta<=1/2,000,000`, this is less than
`0.103`, hence still permits exact root rounding and recovery of `f`.

**Proof.** The variation-of-constants identity inserts the perturbation
between the forward propagator for the perturbed equation and the
unperturbed propagator. Their operator bounds over complementary portions
of the interval multiply to at most `exp(2rL+2|w|K)`. The integral of
the perturbation norm is at most `2|w|K`, proving (SA3.5). Alternatively
expand the Dyson series by the first occurrence of a `C` insertion;
absolute convergence justifies the same estimate. Each of the four responses
changes by at most `epsilon_w`, and each has measurement error `delta`.
Apply SA3 and then the inverse bound three. Finally `K<17/50` and
`exp(2rL+2|w|K)<1.024` give `epsilon_w<7/10^9` in the displayed example.
The error bound is less than `3(0.014+0.00028+0.02)<0.103`. QED.

The exact small DD control has `J^{-1}Delta(X_s)J != Delta(X_s)` on all
81 basis states at the parameters specified in the certificate. Thus the
nonzero third residue makes the collective symbol genuinely depend on the
charged tensorator, while the proved observable estimate remains valid.
The extra term does not create the marked information recovered in SA2;
this corollary proves stability of that analytic recovery under genuine
noncentral coupling. It does not describe a new Felder kernel.

### Coboundary comparison and removal of the split marking

If `f'=f+(I-T)z`, let `D_z|X_kappa=psi(kappa(z))I`. Then


```math

                 G_{f'}=D_z G_f D_z^{-1}.            \tag{SA3.4}

```


Consequently the individual graph spectra and every separate graph-only
Fock trace agree; the pure-torus operator `H` and the physical modules,
bilinear map, and their fusion dimensions have not changed. Yet if `f'!=f`,
SA2--SA3 distinguish the two with `H` and the boundary labels fixed.
If the split marking is removed and one is allowed to conjugate it as well,
`H -> D_z H D_z^{-1}`, then ODE uniqueness gives
`U -> D_z U D_z^{-1}`. Since `D_z` commutes with every `P_kappa`, all the
responses agree exactly. This is the required marking ablation.

For the inherited rigid example, the existing source fixes


```math

 Z=\mathbb F_3[\epsilon]/(\epsilon^3),\quad T=1+\epsilon,
 \quad f=1-\epsilon+\epsilon^2,\quad f'=1-\epsilon.

```


Here the retained center origin `z=epsilon+epsilon^2` gives (SA3.4).
Both graph spectra are conjugate, but the
retained split response recovers their different `f` values. At the charge
`kappa=(1,1,1)` on `(1,epsilon,epsilon^2)`, formula (SA2.5) gives respectively
`c1 psi(1)+c2 psi(2)` and `c1+c2 psi(1)`, which are distinct because
`c2>c1`. The exact script checks all 27 charges and the conjugation. This
uses the inherited strict generator-fixing and marking interface of
[the pinned rigid calculation](bol-cocycle-packets.md#the-rigid-principal-isotope-calculation)
and its
[canonical source, Data and Obstruction to the shift isomorphism sections](https://github.com/Mira-Cult/math-wip/blob/2a25b81e3efe5bdd8a3923e27c94aef16a559094/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/odd-rigid-center-nongloop.md),
not a new proof of the huge loop's construction, simplicity, or unrestricted
isomorphism classification. It is intentionally a marked separator.

## SA4. A genuinely coupled response with a uniform proper-Bol gap

For arbitrary contractions `A,B`, let `U_r=U(b;r,r)` and define


```math

       E_r=U_r-\exp\bigl(rL(A+B)\bigr).              \tag{SA4.1}

```


The comparison term is the transport predicted by replacing the ordered
connection by its integrated constant coefficient. The error vanishes
identically if the two residues commute.

**Theorem SA4 (quantitative ordered-transport defect).** In every dimension,


```math

 \left\|E_r-\frac{r^2(c_1-c_2)}2[A,B]\right\|
       \le \frac83 r^3L^3e^{2rL}.                   \tag{SA4.2}

```


The same bound holds in the normalized Hilbert--Schmidt norm
`||T||_{2,n}=(Tr(T* T)/n)^{1/2}`. In particular `E_r=0` for all sufficiently
small `r` if and only if `[A,B]=0`.

**Proof.** The pure degree-two coefficients of the Dyson expansion are
`L^2 A^2/2,L^2 B^2/2`; its mixed coefficients are `c1 AB,c2 BA`. Subtract
the degree-two exponential expansion and use `c1+c2=L^2`. The remaining
Dyson tail and the exponential tail each have norm at most
`sum_{n>=3}(2rL)^n/n!`. Their sum is at most
`(8/3)r^3L^3e^{2rL}`. Normalized Hilbert--Schmidt norm is at most operator
norm, so the same remainder estimate holds there. Commuting residues give
the exact exponential by direct differentiation. Conversely an identically
zero defect has zero quadratic coefficient, and `c1!=c2`. QED.

Apply this to the established cubic controls


```math

 (c,a,b)\cdot_k(d,u,v)
   =(c+d+bu(a+u)+k(av-bu),a+u,b+v)
 \quad\text{on }\mathbb F_p^3.                    \tag{SA4.3}

```


The earlier
[cubic manuscript, S1--S12 and S19](bol-cubic-isotopes.md), proves that all
`Q_k` are proper left Bol loops, `Q_0` is Bruck, `Q_k` with `k!=0` is not,
their multiplication groups are conjugate, and their individual
left-translation spectra and all associator-defect permutations agree.
Those finite facts are reused with their original scope; the analytic
estimate below is separate.

Let `n=p^3`, use the regular coordinate permutation space, and put


```math

 J(d,u,v)=(-d,-u,-v),\qquad
 h_k=L^{(k)}_{(0,1,0)}:(d,u,v)\mapsto(d+kv,u+1,v),
 \quad A=J,\quad B_k=\frac12(h_k+h_k^{-1}).           \tag{SA4.4}

```


Here permutation symbols also denote their unitary matrices. Both residues
are self-adjoint contractions. Every `h_k` consists of `p^2` cycles of length
`p`; `J` has one fixed point and `(p^3-1)/2` transpositions. Therefore the
individual spectra of both residues are independent of `k`. At `k=0`,
`J h_0 J=h_0^{-1}`, so `[J,B_0]=0`. The same occurs for the associative
additive group `F_p^3` with its usual inversion and the selected translation.

**Theorem SA5 (effective proper-Bol comparison).** For `k!=0`,


```math

           \|[J,B_k]\|_{2,n}^2=1-\frac1p.            \tag{SA4.5}

```


At the fixed separated insertion scale `r=1/100`,


```math

 \|U_{Q_k}(b;r,r)-e^{rL(J+B_k)}\|_{2,n}>9\cdot10^{-6},
                                                               \tag{SA4.6}

```


uniformly for every odd prime `p` and every nonzero `k`. For `Q_0` and the
associative additive control, this defect is zero exactly. With augmented
residues the corresponding defect is multiplied by `e^{-2rL}` and remains
greater than `8\cdot10^{-6}`.

**Proof.** Direct substitution gives
`J h_k J h_k:(d,u,v)->(d+2kv,u,v)`. For `k!=0` it has `p^2` fixed points.
The same is true for `J h_k^{-1}J h_k^{-1}`. The two cross products
`J h_k J h_k^{-1}` and `J h_k^{-1}J h_k` translate `u` by `-2` and `2`,
respectively, and have no fixed points. Also `Tr(B_k^2)=n/2`, since
`h_k^2` and `h_k^{-2}` are fixed-point-free for odd `p`. Hence


```math

 \operatorname{Tr}(J B_k J B_k)=p^2/2,
 \quad
 \|[J,B_k]\|_{\rm HS}^2
       =2\operatorname{Tr}(B_k^2)-2\operatorname{Tr}(J B_k J B_k)
       =p^3-p^2.

```


This proves (SA4.5). Apply the reverse triangle inequality to (SA4.2), use
`c2-c1>=1/3` and `sqrt(1-1/p)>=sqrt(2/3)>4/5`, and obtain


```math

 \|E_r\|_{2,n}
  \ge r^2\left(\frac2{15}-\frac83 rL^3e^{2rL}\right).

```


At `r=1/100`, the bounds `L<11/10` and `e^{2rL}<500/489` make the bracket
strictly greater than `9/100`. This proves (SA4.6). Finally
`e^{-2rL}>1-2rL>489/500`; multiplying the lower bound gives the stated
augmented bound. The commuting controls were already identified. QED.

The outcome detects the relation between inversion and the chosen translation.
It is not a test for nonassociativity alone: the proper nonassociative `Q_0`
and the associative control both have zero defect. For the two proper loops,
the underlying multiplication groups and stabilizers are conjugate, so their
abstract representation fusion data agree under that identification; all
the individual translation oscillator traces and the previously calculated
associator-defect traces agree as well. The older marked inverse-property
word already separates them. The present advance is a uniform quantitative
separation by a genuinely ordered, noncoincident analytic response, with an
explicit comparison term and error bound. It does not assert equality of
their entire earlier marked partition packets.

The cubic inversion example is a separate control of the universal collective
ODE. No implementation of the full CH/DD affine-completion and charged-bundle
construction for its inversion-extended multiplication group is claimed.

## Scope, applications, and remaining boundaries

SA2--SA3 enable recovery of a retained positive-cocycle value from a finite
collection of bounded separated transport measurements. The conditioning and
noise tolerance do not deteriorate with the immense physical Schrödinger
dimension or neutral zero-algebra dimension. Varying the marked torus element
recovers all its retained cocycle values. The reconstruction is natural for
the precise marked-data isomorphisms carrying the split transport, charges,
and boundary projections; removal of the split marking restores the exact
graph-only erasure.

SA4--SA5 provide a testable analytic consequence of noncommuting actual marks.
They compare identical individual spectra and known coincident finite
baselines, exhibit both an associative and a proper nonassociative zero
control, and prove a dimension-independent nonzero gap for the second proper
Bol control. This avoids mistaking nonassociativity by itself for the mechanism.

The collective fusion construction is needed to transport these responses
through the original charged multiplicities and carries. The scalar analytic
bound itself applies to any contractions. It neither proves an elliptic
Felder identification nor puts a heat equation on the old Fock traces. The
responses are determined by the complete finite marked operators; the new
constraint is analytic recoverability and a uniform separated-transport
estimate, rather than an assertion of information beyond complete finite data.
There is no Monster action, genus-zero result, new arithmetic moonshine
consequence or unrestricted classification theorem.

The standard-library
[exact certificate](../code/verify_bol_shifted_analytic.py) checks graph/split
products, the entire 27-charge rigid comparison, exact coboundary ablation,
small collective tensor/dual identities, and cubic controls using exact
rational and finite-field arithmetic. It does not numerically prove the ODE
estimates: their proofs are SA1--SA5 above.
