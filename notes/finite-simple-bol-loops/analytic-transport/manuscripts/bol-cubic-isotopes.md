# A central cubic Bol family and a principal-isotope ablation

**Mira Cult**

Owner of this exploratory calculation: model participant 2.
These are manuscript-local results, not allocated permanent claims. The family
is small and centrally nilpotent; none of its members is simple. Its role is to
test what marked translation traces retain and what an unmarked group or an
associator-only trace forgets. The formulas and proofs below are independent of
the large simple-loop constructions in PR #431. Novelty of this particular
coordinate family has not been established. In particular, the two isomorphism
types at `p=3` are already known: they are the opposites of `B_6` and `B_2`,
respectively, in Grishkov--Kinyon--Vojtěchovský, *Bol loops of order 27*,
[Theorem 5.3 and Table 1](https://cs.du.edu/~petr/data/papers/bol_loops_of_order_27.pdf).
That identification follows from the classification and the Bruck property,
center order 3, and 14 elements of order 3 calculated below. The source also
records their isotopy. The examples themselves are therefore rediscovered
controls; the purpose here is the explicit symbolic trace comparison.

## Definition and structural theorem

Let `p` be an odd prime and let `k` be in `F_p`. On `F_p^3`, write elements
as `(c,a,b)` and define


```math

 (c,a,b)\cdot_k(d,u,v)
 =\bigl(c+d+b u(a+u)+k(av-bu),\ a+u,\ b+v\bigr).
 \tag{S1}

```


All coordinates are taken modulo `p`. The identity is `(0,0,0)` and the
two-sided inverse is `-(c,a,b)`. Every `Q_k` is a proper left Bol loop. Its
center and full nucleus are `F_p x {(0,0)}`. `Q_0` is a Bruck loop; `Q_k`
is not a Bruck loop when `k != 0`. The displayed family has exactly two
isomorphism classes, represented by `k=0,1`, and these two are isotopic.

**Proof.** Put `x=(a,b)`, `y=(u,v)`, `z=(s,t)` and


```math

 \theta_k(x,y)=bu(a+u)+k(av-bu),\qquad
 \Delta(x,y)=av-bu.

```


The normalized central-extension formula immediately gives bijective left and
right translations. Also `theta_k(x,-x)=theta_k(-x,x)=0`, proving the inverse
formula. Its central associator, with convention
`(XY)Z = X(YZ) + A(x,y,z)` in the central coordinate, is


```math

 A(x,y,z)
 =\theta_k(x,y)+\theta_k(x+y,z)
       -\theta_k(y,z)-\theta_k(x,y+z)
 =\Delta(x,y)s.                                      \tag{S2}

```


In particular it is independent of `k`. For a central extension of an abelian
group, the left Bol identity is equivalent to


```math

 A(y,x,z)+A(x,x+y,z)=0.                              \tag{S3}

```


Indeed, rewriting `X(Y(XZ))` as `(X(YX))Z` successively contributes these two
central associators. Formula (S2) satisfies (S3), because `Delta` is alternating.
More generally, for a triadditive central associator over an abelian quotient,
(S3) holds if and only if the associator is alternating in its first two
variables. Setting `y=0` first gives `A(x,x,z)=0`; applying this to `x+y`
gives `A(x,y,z)=-A(y,x,z)`. These identities also immediately imply (S3).
For `x=(1,0)` and `y=(0,1)`, `A(x,y,x)=1`; therefore flexibility fails and
the loop cannot be Moufang. The left and middle nuclei consist exactly of
elements with zero quotient coordinate, because `Delta` is nondegenerate.
The right nucleus consists of the elements with `a=0`. Their intersection is
the asserted full nucleus; its elements commute with everything, proving the
center statement. The central subgroup of order `p` is nontrivial and proper,
so these loops are not simple.

The cubic summand of `theta_k` changes sign under `(x,y)->(-x,-y)` and its
bilinear summand does not. Consequently


```math

 X^{-1}\cdot_kY^{-1}
 = (X\cdot_kY)^{-1}+(2k\Delta(x,y),0,0).             \tag{S4}

```


The automorphic inverse property holds exactly when `k=0`, proving the Bruck
distinction. If `r,s` are nonzero field elements, then


```math

 (c,a,b)\longmapsto(r^2s\,c,ra,sb)
 \tag{S5}

```


is an isomorphism `Q_k -> Q_{rk}`: the cubic term scales by `r^2s`, and the
bilinear coefficient condition is precisely `k'=rk`. Thus all nonzero
parameters are isomorphic, whereas (S4) separates them from zero.

For an explicit principal isotope, in `Q_0` put `t_k=(0,-k,0)` and


```math

 U\circ_k V=(U/_0t_k)\cdot_0 V.
 \tag{S6}

```


Its identity is `t_k`. The map


```math

 \Phi_k(c,a,b)=(c-kab,a-k,b)                         \tag{S7}

```


is an isomorphism `Q_k -> (Q_0,circ_k)`. For verification, division by
`(0,h,0)` in `Q_0` is


```math

 (c,a,b)/_0(0,h,0)=(c-bha,a-h,b).

```


Substitution in (S6) shows that both sides of the homomorphism identity for
(S7) have first coordinate


```math

 c+d+bu(a+u)-kab-2kbu-kuv

```


and quotient coordinate `(a+u-k,b+v)`. This proves the isotope assertion.
In particular, the non-Bruck member of this small family *is* isotopic to a
Bruck loop. It is not a model of the stronger non-Bruck-isotopy obstruction of
the large rigid-center construction.

## Exactly the same associated permutation group

The left translation of `X=(c,a,b)` acts on `(d,u,v)` as


```math

 L_X^{(k)}(d,u,v)
 =\bigl(d+bu^2+b(a-k)u+ka v+c,\ u+a,\ v+b\bigr).
 \tag{S8}

```


Its left multiplication group consists exactly of the `p^4` maps


```math

 T_k(a,b,B,C)(d,u,v)
 =\bigl(d+bu^2+Bu+ka v+C,\ u+a,\ v+b\bigr).
 \tag{S9}

```


Composition, with the right factor acting first, is


```math

 (a,b,B,C)(a',b',B',C')
 =\bigl(a+a',b+b',B+B'+2ba',
 C+C'+b(a')^2+Ba'+ka b'\bigr).
 \tag{S10}

```


This proves closure. The maps in (S9) are distinct even for `p=3`: the quotient
coordinates recover `a,b`, and then the central values at `u=0,1` recover
`C,B`. To prove generation, let


```math

 D_k(X,Y)=\bigl(L_{X\cdot_kY}^{(k)}\bigr)^{-1}
                  L_X^{(k)}L_Y^{(k)}.

```


Formula (S2) gives


```math

 D_k(X,Y)(d,u,v)=(d-\Delta(x,y)u,u,v).               \tag{S11}

```


Taking `x=(1,0)`, `y=(0,1)` supplies the unit central shear, whose powers
supply every shear. Composing a shear with (S8) gives arbitrary `B`, while
`a,b,c` are already arbitrary in (S8). Thus (S9) is the whole group.

The coordinate shear


```math

 F_k(d,u,v)=(d+kuv,u,v)

```


fixes the identity and satisfies


```math

 F_kT_0(a,b,B,C)F_k^{-1}
   =T_k(a,b,B+kb,C+kab).                            \tag{S12}

```


Hence all `LMlt(Q_k)` are conjugate as permutation groups. Their stabilizers
of the identity correspond as well; each stabilizer consists of the `p` maps
`T_k(0,0,B,0)`. The pair `(LMlt(Q), stabilizer)` therefore does not distinguish
the two nonisomorphic loops. The distinguished transversal of left translations
does: the conjugacy (S12) does not take the transversal of `Q_0` to that of
`Q_k` when `k != 0`.

## Associator traces and the inverse-property probe

For any permutation `g` of a finite set of cardinality `N`, let `c_j(g)` be
its number of `j`-cycles. The normalized oscillator trace is


```math

 \mathcal Z_g(\tau)
 =q^{-N/24}\prod_{m\ge1}\det(1-q^m g)^{-1}
 =\prod_{j\ge1}\eta(j\tau)^{-c_j(g)}.
 \tag{S13}

```


The modular theory for (S13) is proved in [the translation construction](bol-translation-fock.md); the following
are exact loop-specific cycle calculations, requiring no numerical fitting.
Put `N=p^3`.

If `Delta(x,y)=0`, then `D_k(X,Y)=1`. Otherwise (S11) has `p^2` fixed
points and `p(p-1)` cycles of length `p`. Consequently


```math

 \mathcal Z_{D_k(X,Y)}=
 \begin{cases}
 \eta(\tau)^{-p^3},&\Delta(x,y)=0,\\
 \eta(\tau)^{-p^2}\eta(p\tau)^{-p(p-1)},&\Delta(x,y)\ne0.
 \end{cases}                                      \tag{S14}

```


These *marked* associator-defect permutations are identical for every `k`,
not merely equidistributed. Among the `p^6` ordered pairs `(X,Y)`, the
nonidentity case occurs


```math

 p^2(p^2-1)(p^2-p)                                 \tag{S15}

```


times, by counting ordered bases of `F_p^2` and the two central coordinates.

To retain the inverse-property information that (S14) loses, define the marked
translation word


```math

 E_k(X,Y)=
 \bigl(L_{(X\cdot_kY)^{-1}}^{(k)}\bigr)^{-1}
      L_{X^{-1}\cdot_kY^{-1}}^{(k)}.
 \tag{S16}

```


Since the two indexed elements differ only by a central coordinate, (S4)
gives


```math

 E_k(X,Y)(d,u,v)=(d+2k\Delta(x,y),u,v).
 \tag{S17}

```


For `k=0` every such word is the identity. For `k != 0` and `Delta != 0`,
the cycle type is `p^{p^2}`, so


```math

 \mathcal Z_{E_k(X,Y)}=\eta(p\tau)^{-p^2}.           \tag{S18}

```


The weight and q-expansion are therefore structurally different from the
identity case, although the order, associated permutation group and all the
defect traces (S14) agree. The probe is defined from multiplication and inversion
alone, so the entire marked family and its unmarked multiset are invariant under
loop isomorphism and under arbitrary relabeling. Its use is intentional:
associator defects detect association, whereas (S16) also detects a specific
identity involving inverses. No reconstruction from the unmarked multiset is
claimed.

Even the individual left-translation cycle types are independent of `k` for
each fixed coordinate `X`. Direct iteration gives


```math

 X^n=\bigl(nc+ba^2(n^3-n)/3,\ na,\ nb\bigr),        \tag{S19}

```


where `(n^3-n)/3` is first evaluated as an integer and then reduced modulo
`p`. This convention is essential when `p=3`. The same direct iteration gives
`(L_X^{(k)})^n=L_{X^n}^{(k)}`. Every nonidentity translation is fixed-point
free. Thus all its cycles have length `ord(X)`, and that order is independent
of `k`. For `p>=5`, every nonidentity translation has type `p^{p^2}`. For
`p=3`, the distribution on all 27 elements is one identity, 14 translations
of type `3^9`, and 12 of type `9^3`.

At `p=3`, (S15) gives 432 nonidentity associator defects and 297 identity
defects. The nonidentity associator trace is
`eta(tau)^(-9) eta(3 tau)^(-6)`. The inverse-property probe in `Q_1` is
`eta(3 tau)^(-9)` on those 432 pairs; in `Q_0` it is always
`eta(tau)^(-27)`.

For completeness, the central coordinate of `(L_X^{(k)})^n(d,u,v)` is


```math

 d+nc+b\{nu^2+n^2au+a^2(n^3-n)/3\}+nk(av-bu).

```


This follows by summing the quadratic increments at `u+ja,v+jb`, for
`0<=j<n`; substituting (S19) in (S8) gives exactly the same expression.

## What a scalar categorical associator would forget

There is no automatic coherence assertion for an arbitrary loop associator.
In this particular central-extension setting there is an explicit one. Regard
`theta_k` as a group 2-cochain on the *abelian quotient* `V=F_p^2`. For the
usual group-cohomology differential, (S2) says `A=-delta theta_k`. Therefore


```math

 \omega(x,y,z)=\exp(2\pi iA(x,y,z)/p)

```


is a normalized group 3-cocycle, with the pentagon identity


```math

 \omega(y,z,w)\omega(x,y+z,w)\omega(x,y,z)
 =\omega(x+y,z,w)\omega(x,y,z+w).

```


This follows by substituting the four terms of (S2); every `theta_k` term
cancels. But more is true: putting `F(x,y)=exp(-2pi i theta_k(x,y)/p)` gives
`omega=delta F`. Consequently the category of `V`-graded complex vector spaces
with associator `omega` is monoidally equivalent to the ordinary graded category.
The identity functor from the twisted to the ordinary category with tensorator
`F(x,y)` implements the equivalence: its coherence equation reads
`omega(x,y,z) F(x+y,z) F(x,y)=F(x,y+z) F(y,z)`, which is exactly
`omega=delta F`. Thus retaining only that monoidal equivalence class cannot
detect the nonassociativity of this family. Marked cochain or translation data
are needed. This is an obstruction for this specific scalar-cochain architecture,
not for categorical Bol theories in general.

## Exact validation

`verify_bol_cubic_isotopes.py` uses integer arithmetic modulo `p`, checks the loop and
left Bol axioms, exhibits a failure of flexibility, verifies every AIP pair,
verifies (S11), (S16)--(S17), all principal-isotope products, conjugate generated
groups, and deterministic random relabeling. It also checks finite oscillator
coefficients by the exact Euler product. The finite checks validate the
implementation; the symbolic argument above proves the family statements.
