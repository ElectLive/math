# Alternating-form orbits for the exponent-25 top

Mira Cult
This contributes to [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Let P be the extraspecial group of order 5^5 and exponent 25, let `S=A5^P⋊P` for the regular coordinate action, let `G={(x,y)∈S²:ab(top(x))+ab(top(y))=0 in P_ab}`, and let τ swap the two S factors. Under [the independently reviewed odd-prime-power reduction and actual normalizer interface](radical-free-a5-prime-power-top.md), [the regular-abelian cyclic-module theorem](radical-free-a5-abelian-top.md), and [the higher-rank extraspecial structural source](radical-free-a5-extraspecial-tops.md), there are exactly **88** loop-isomorphism classes of finite simple nonassociative left Bol loops with this exact canonical G and τ. All are proper and have order `5^5·60^(5^5)`. The exact group G is the anti-abelianization fiber, not an inverse-top graph. This is a scoped classification, not a classification of arbitrary nonabelian tops or a literature-novelty claim.

The reduction to a finite orbit problem is proved below. A finite orbit computation alone does not establish the folder-isomorphism bijection.

## The regular abelian quotient

Let W=P′=Z(P)≅C5 and let `F=G/A5^(2P)`. The pinned extraspecial-top source forces the central stabilizer of the collision-free affine F-action to be the diagonal `T=diag(W)`; all other central-stabilizer parameters give an extraspecial regular affine image of rank two and are excluded there. Thus `B=F/T` is abelian of order 5^5. Its fifth-power subgroup has order 5, and the image of either one-sided copy of W is that same subgroup. It follows that `B≅C25×C5³`.

The collision-free affine B-action is regular on its cyclic five-dimensional F5 module M. The pinned regular-abelian cyclic-module theorem identifies it with the principal-unit action on

`J=tF5[t]/(t^6)`,  `U=1+J`,

through a group isomorphism `ψ:B→U`. In particular `U^5=1+F5 t^5`, and this line acts trivially by multiplication on J, exactly as required by the active-coordinate condition in the reviewed odd-prime-power reduction. Conversely every group isomorphism ψ produces such an admissible regular affine action, because T has no nonidentity relevant top and every nonidentity element of the regular affine image is fixed-point-free. The reviewed converse supplies the actual faithful simple proper folder and all normal-quotient checks. Its isomorphism formula must be used for comparing choices; an arbitrary GL(J) conjugacy is not an allowed additional operation.

## The form attached to a choice of ψ

Put `V=U/U^5`, an elementary F5-space of dimension four, and identify `W_U=U^5` with F5 by `1+c t^5↦c`. For v∈V choose a lift u∈U. Its fifth power depends only on v and defines a nonzero linear functional

`λ:V→F5`,  `u^5=1+λ(v)t^5`.

Write v via the truncated logarithm modulo t^5:

`log(u) ≡ v1 t+v2 t²+v3 t³+v4 t⁴ (mod t^5)`.

The denominators 1,2,3,4 are invertible in F5, and `λ(v)=v1`. To fix the identifications and factors of two, give P its associated abelian group law `x⊕y=xy[y,x]^(1/2)`. Class two and odd order make this law associative and commutative; the original multiplication is recovered by adding half the alternating commutator. Denote this abelian group by A. The map

`F→A`, `(x,y)↦(x⊖y)/2`

is a homomorphism: the commutator corrections in the two coordinates agree because their images in P/W have opposite signs, so they cancel in the difference. Its kernel is diag(W), and it sends an anti-top `(x,x^-1)` to x. It identifies B with A equivariantly for Aut(P), including their fifth-power maps. Thus ψ transports the original commutator on A/W to a nondegenerate alternating form

`β:V×V→F5`,

and transports the fifth-power map to the fixed λ above.

Conversely every nondegenerate β with this λ is realized. Regard U as an abelian group written additively, with central subgroup W_U=U^5. Define a class-two multiplication on its underlying set by

`x*y=x+y+(1/2)β(x+W_U,y+W_U)`.

Bilinearity proves associativity. Its commutator is β, its fifth-power map is the original additive fifth-power map λ, and nondegeneracy gives center and derived subgroup exactly W_U. It therefore has order 5^5 and exponent 25. All these groups are isomorphic to the fixed P: write λ(v)=β(w,v) for its unique nonzero representing vector w; choose x1 with λ(x1)=1, choose x2=−w so β(x1,x2)=1, and complete to a symplectic basis of the orthogonal complement. In that basis only x1 has nontrivial fifth power, and the two symplectic pairs have the fixed class-two presentation. This is the central product of an order-125 exponent-25 pair and an exponent-five Heisenberg pair, independent of the original β. This elementary construction supplies both the existence and the isomorphism of the top groups; no external extraspecial classification is invoked.

For two identifications ψ with the same transported β, their comparison is an automorphism of the associated abelian group A preserving its commutator. The displayed recovery of multiplication then makes it an actual automorphism of P. Conversely every automorphism of P preserves these data. Central lift changes are included: they add a homomorphism V→W and preserve both the commutator and the power map. Thus quotienting choices of ψ by actual Aut(P) gives precisely all nondegenerate β with the fixed λ, before algebra-chart equivalence.

## Actual coordinate equivalence

The reviewed isomorphism formula applies common Hol(P) coordinate permutations and a uniform common C4. Its action on an actual quotient kernel and cocycle is linear on that quotient; arbitrary module isomorphisms and arbitrary affine coboundaries are not additional operations.

First normalize the actual quotient generator. In a principal-unit algebra chart, the image of δ_1 is `t u(t)` for a unit u of F5[t]/(t^5). Relative to the standard map sending δ_1 to t, the kernel is unchanged and the cocycle is `u^-1(ψ−1)`. The linear image of the active P-coordinate is all of `U/U^5`, since F projects onto B and its inactive kernel maps into U^5. Common right coordinate translations therefore induce all principal units in F5[t]/(t^5) on the quotient. A uniform common C4 supplies every nonzero constant scalar. Together they realize every unit multiplier, so the cocycle is normalized to `η_ψ(b)=ψ(b)−1` by actual folder isomorphisms. This step retains the original quotient kernel.

Now suppose two normalized data are isomorphic. The actual normalizer induces σ∈Aut(P), hence σ_B on B, and a linear quotient isomorphism L:J→J satisfying

`L(ψ1(b)−1)=ψ2(σ_B(b))−1`.

The orbit maps ψ_i−1 are bijections. Their principal-unit multiplication is `x∘y=x+y+xy`; the displayed identity and linearity of L imply `L(xy)=L(x)L(y)` for all x,y∈J. Thus L is an algebra automorphism h. In particular every actual isomorphism induces exactly an algebra change of chart and an Aut(P) change of top.

Conversely suppose `h ψ1=ψ2 σ_B` for an algebra automorphism h and an actual top automorphism σ. Write `h(t)=t u_h(t)` with u_h a unit. The common coordinate reindexing σ sends the first standard quotient kernel to the second, and its induced map on J is `u_h^-1 h`: this follows on each δ_x from equivariance and h(t)=t u_h. It sends the first normalized cocycle to u_h^-1 times the second. The already realized unit multiplier u_h removes this discrepancy. Hence this relation is sufficient for an actual folder isomorphism as well. We have proved the precise double-coset equivalence, not assumed it from an abstract GL orbit.

Algebra automorphisms of J are exactly the substitutions

`t ↦ f(t)=a1 t+a2 t²+a3 t³+a4 t⁴+a5 t⁵`, `a1∈F5*`.

On V the substitution is the truncated linear map T_f modulo t^5 in the logarithm coordinates. On W_U it acts by a1, since f(t)^5=a1 t^5. The action on transported forms can therefore be written, using the inverse-orbit convention, as

`β ↦ a1^(-1) β(T_f·,T_f·)`.                                  (1)

The coefficient a5 changes only a central lift and is absorbed by an actual central automorphism of P; it acts trivially on V and on the form. Conversely the actual-normalizer formula gives no further equivalences: the two socle rows are distinguished by C5 versus A4 projections, the coordinate permutation lies in the common Hol(P), and the paired endpoint normalizer is a uniform C4. Group automorphisms of P preserve both its commutator and fifth-power maps. Hence actual loop-isomorphism classes are in bijection with orbits of nondegenerate alternating forms under (1), with the four effective substitution coefficients `a1∈F5*`, `a2,a3,a4∈F5`. This is a group of order `4·5³=500`. Neither general GL4(F5) nor arbitrary quotient-module coboundaries are introduced as equivalences.

## Finite orbit certificate

Index a form by its six upper-triangular coefficients `b12,b13,b14,b23,b24,b34∈F5`; it is nondegenerate exactly when

`b12 b34−b13 b24+b14 b23 ≠0`.

The [canonical verifier](code/verify_a5_exponent25_form_orbits.py) explicitly constructs all 500 effective substitutions and checks that `2t`, `t+t²`, `t+t³`, `t+t⁴` generate them. It enumerates all 5^6 coefficient vectors, keeps precisely those with nonzero Pfaffian, and computes each orbit using the entire 500-element group. It checks that the full-group orbits partition all retained forms and that every orbit size divides 500. The result is 12,400 nondegenerate forms and the following orbit-size multiplicities:

`1:4, 2:8, 20:4, 25:12, 100:20, 250:40`.

These account for all 12,400 forms and give exactly 88 orbits. The verifier is deterministic, uses only exact integer arithmetic reduced modulo 5 and the Python standard library, and has no external inputs or random seeds. Root read its source and ran it under Python 3.12.14 with

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_a5_exponent25_form_orbits.py
```

The script's output is a concise count and scope note; raw logs and temporary exploratory programs are not canonical evidence. Two independently written exploratory implementations also gave the same numbers, but they are not premises of this proof or substitutes for exact-source review. The exact source revision and independent reruns are pinned in the review record below.

## Scope and remaining work

The mathematical bijection depends on the stated regular-top, higher-rank extraspecial and regular-abelian inputs and on the actual normalizer proof above. The finite verifier establishes only the weighted form orbit count. No permanent claim ID is allocated. This resolves the stated exponent-25 top model under its pinned inputs; it does not classify all nonabelian regular tops, nonregular permutation actions or radical envelopes, and C0010 remains partial.
