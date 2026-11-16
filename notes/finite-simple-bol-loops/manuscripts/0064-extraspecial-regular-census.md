# 0064. The regular extraspecial-top census

Mira Cult

## Results obtained

This note classifies a specified family of canonical envelopes, not all finite simple Bol loops. Let $`P`$ be an odd extraspecial group, let $`S=A_5^P\rtimes P`$, with the regular action on the coordinates, and set

```math
G=\{(x,y)\in S^2:\overline{\mathop{\mathrm{top}}\nolimits(x)}+
\overline{\mathop{\mathrm{top}}\nolimits(y)}=0\text{ in }P/P'\}.
```

The canonical inversion $`\tau`$ swaps the two copies of $`S`$. For nonabelian $`P`$, the condition on $`G`$ is an anti-abelianization condition; it does not require the two top elements to be inverses.

**Theorem.** Under the faithful-folder, cyclic-affine reduction, actual-coordinate isomorphism and normal-subloop interfaces cited below, the following table gives all simple proper left Bol-loop isomorphism classes with this exact canonical group and inversion. Every class in a row has order $`|P|60^{|P|}`$.

| Extraspecial top | Number of classes |
|---|---:|
| Order 27, exponent 3 | 2 |
| Order 27, exponent 9 | 6 |
| Order 125, exponent 5 | 24 |
| Order 3125, exponent 25 | 88 |
| Every other odd extraspecial top | 0 |

The total is **120 classes across these exact models**. The count 88 uses a finite exact orbit certificate; the new count 24 and the assembly are conventional algebraic arguments. The two order-27 rows were established in the [exponent-three proof](../sources/factor-permutation/radical-free-a5-extraspecial-27.md) and [modular proof](../sources/factor-permutation/radical-free-a5-nonabelian-27.md).

## Structural inputs and proof plan

The [prime-power reduction](../sources/factor-permutation/radical-free-a5-prime-power-top.md) provides full marks, cyclic affine data, the active-coordinate condition, the converse and the actual ambient isomorphism relation. The [regular abelian-top theorem](../sources/factor-permutation/radical-free-a5-abelian-top.md#the-regular-cyclic-module-algebra) identifies regular abelian affine actions on cyclic modules with principal-unit algebras. The [higher-rank obstruction](0037-cyclic-affine-extraspecial-tops.md) leaves only the order-3125 exponent-25 group when the extraspecial rank is at least two. These are dependencies, not conclusions of the finite orbit count.

We first resolve that surviving higher-rank case. We then classify the order-125 exponent-five case and exclude its exponent-25 counterpart. Throughout, an abstract linear equivalence is insufficient: the changes of coordinates must come from the actual canonical-folder normalizer.

## 1. The surviving rank-two group: 88 classes

### The regular abelian quotient

Let W=P′=Z(P)≅C5 and let `F=G/A5^(2P)`. The stated extraspecial-top source forces the central stabilizer of the collision-free affine F-action to be the diagonal `T=diag(W)`; all other central-stabilizer parameters give an extraspecial regular affine image of rank two and are excluded there. Thus `B=F/T` is abelian of order 5^5. Its fifth-power subgroup has order 5, and the image of either one-sided copy of W is that same subgroup. It follows that `B≅C25×C5³`.

The collision-free affine B-action is regular on its cyclic five-dimensional F5 module M. The stated regular-abelian cyclic-module theorem identifies it with the principal-unit action on

`J=tF5[t]/(t^6)`,  `U=1+J`,

through a group isomorphism `ψ:B→U`. In particular `U^5=1+F5 t^5`, and this line acts trivially by multiplication on J, exactly as required by the active-coordinate condition in the cited odd-prime-power reduction. Conversely every group isomorphism ψ produces such an admissible regular affine action, because T has no nonidentity relevant top and every nonidentity element of the regular affine image is fixed-point-free. The cited converse supplies the actual faithful simple proper folder and all normal-quotient checks. Its isomorphism formula must be used for comparing choices; an arbitrary GL(J) conjugacy is not an allowed additional operation.

### The form attached to a choice of ψ

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

### Actual coordinate equivalence

The cited isomorphism formula applies common Hol(P) coordinate permutations and a uniform common C4. Its action on an actual quotient kernel and cocycle is linear on that quotient; arbitrary module isomorphisms and arbitrary affine coboundaries are not additional operations.

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

### Finite orbit certificate

Index a form by its six upper-triangular coefficients `b12,b13,b14,b23,b24,b34∈F5`; it is nondegenerate exactly when

`b12 b34−b13 b24+b14 b23 ≠0`.

The [canonical verifier](../sources/factor-permutation/code/verify_a5_exponent25_form_orbits.py) explicitly constructs all 500 effective substitutions and checks that `2t`, `t+t²`, `t+t³`, `t+t⁴` generate them. It enumerates all 5^6 coefficient vectors, keeps precisely those with nonzero Pfaffian, and computes each orbit using the entire 500-element group. It checks that the full-group orbits partition all retained forms and that every orbit size divides 500. The result is 12,400 nondegenerate forms and the following orbit-size multiplicities:

`1:4, 2:8, 20:4, 25:12, 100:20, 250:40`.

These account for all 12,400 forms and give exactly 88 orbits. The verifier is deterministic, uses only exact integer arithmetic reduced modulo 5 and the Python standard library, and has no external inputs or random seeds. From the public Bol writeup directory, run the certificate with Python 3.12 or later:

```sh
python sources/code/verify_a5_exponent25_form_orbits.py
```

The computation counts form orbits only. The preceding actual-coordinate equivalence is what identifies those orbits with loop isomorphism classes.

## 2. Rank-one order-125 tops

### Central kernels and the nonabelian affine quotients

Let W=P′=Z(P)≅F5 and let `F=G/A5^(2P)`. The stated reduction forces the actual mark to be full and the collision-free affine F-action on its cyclic three-dimensional F5 module M to have a central point stabilizer

`T_α={(αw,(1−α)w):w∈W}`,  `α∈F5`.

Every α gives a line avoiding the anti-central relevant line; these are all possible central kernels. The affine quotient B_α=F/T_α acts regularly on M, and

`B_α′=(1−2α)W`.

For α≠1/2, B_α is the extraspecial order-125 exponent-five group; for α=1/2, it is elementary abelian of order 125. The five α are invariant under the actual isomorphism interface: common automorphisms of P scale the two coordinates of W simultaneously and preserve α; uniform local C4 acts on M rather than interchanging these coordinates. The first and second socle rows have C5 and A4 H0 projections, respectively, so an isomorphism between standardized oriented data cannot swap them. We count their affine orbits separately. For α≠1/2 every automorphism of B_α is induced by a common automorphism of P: on the two-dimensional central quotient both are arbitrary GL2(F5) maps with the corresponding determinant action on the commutator line, and central lift changes are arbitrary homomorphisms of that quotient to W. The anti-central image is a nonzero central line in B_α, so common central automorphisms of P realize all such lift changes. This justifies the generator changes used below; no independent automorphism of one socle row is allowed.

### Nonabelian quotient: faithful linear action is impossible

For α≠1/2 let B=B_α. Its affine linear part factors through the first P-coordinate, as p=5. If α≠0, the kernel T_α has nontrivial first central projection, forcing the linear center to be trivial. The only remaining possibility for nonabelian linear image is α=0. In that case a nonabelian linear image of B is faithful: every nontrivial normal subgroup of extraspecial B meets its center, and killing the center makes the image abelian. A faithful subgroup of order 125 in GL3(F5) is a Sylow 5-subgroup and is conjugate to natural UT3. The centrality calculation used in the cited exponent-three order-27 case excludes this image for every odd prime, as follows.

In F choose `a=(g^-1,g)`, `b=(t^-1,t)`, `c=(1,z)`, `d=(z,1)` with `[a,b]=cd`, c,d central. For a faithful natural image choose a basis and generators with

`X=ρ(a)=I−E12`, `Y=ρ(b)=I−E23`, `Z=ρ(d)=I+E13`, `ρ(c)=I`.

Write x=η(a), y=η(b), w=η(d). Centrality of c puts η(c) in <e1>. Centrality of d with b gives `(Y−I)w=(Z−I)y`, hence w3=y3=0; centrality with a gives `(X−I)w=(Z−I)x`, hence w2=−x3. The second coordinate of `ab=cd·ba` gives w2=x3. Since 2≠0 in F5, w2=x3=0. Therefore η(cd^-1) lies in `<e1>=im(1−ρ(d^-1))`. But `cd^-1=(z^-1,z)` is nonidentity and relevant, contradicting the actual marked-square collision criterion. Thus the linear image is abelian.

### Nonabelian quotient: five cyclic affine types

A cyclic three-dimensional module for the abelian linear image has either every linear displacement square-zero, or an element with one Jordan block of length three. All linear elements are unipotent because B is a 5-group.

In the square-zero case, any two commuting square-zero endomorphisms R,S satisfy RS=0: if RSv≠0 then v,Rv,Sv,RSv are linearly independent. A cyclic generator and its images show that the displacement span has dimension two. After a top automorphism and basis normalization, the linear generators are `I+E13` and `I+E23`. Regularity and the commutator relation put the affine action into the unique actual-normalizer orbit represented by

`g=(I+E13,e2)`,  `t=(I+E23,e3)`,  `z=(I,e1)`.

The central automorphisms remove the e1 parts of the two translations, and the common right-translation module units remove the remaining W-part of η(t). A top scaling normalizes the nonzero second coefficient of η(g). These are actual operations in formula (3) of the cited reduction, not arbitrary affine coboundaries. For this square-zero module the original quotient generator can be used as e3; its two displacement images give e1,e2, so the kernel is the augmentation-ideal square. Common right translations realize all units with constant coefficient one, and uniform C4 supplies the nonzero scalar. The normalizations therefore retain the actual kernel, as in the cited [order-27 proof](../sources/factor-permutation/radical-free-a5-extraspecial-27.md), with the same argument over F5. This gives one class.

In the Jordan case choose g with N=ρ(g)−1 satisfying N³=0≠N², and replace the other generator by a g-multiple to remove its first N coefficient. Let A=η(g) and B=η(t). The commutator displacement is η(z)=NB−vN²A, and centrality makes it N-fixed. Hence N²B=0. If A were also in NM, the translations of both generators would lie in NM; their linear parts preserve NM, so the entire affine orbit of 0 would lie in that proper plane, contradicting regularity. Thus A is cyclic. We have

`ρ(g)=1+N`,  `ρ(t)=1+vN²`,  `η(t)=b2·NA+b1·N²A`.          (1)

Indeed any N coefficient in ρ(t) can be removed by replacing t by a suitable g-multiple. The coefficient of A in η(t) is zero: ρ(z)=1 and η(z) is central, so it must be fixed by ρ(g). The commutator relation gives `η(z)=(b2−v)N²A`. Regularity is equivalent to `b2≠0` and `b2−v≠0`. In a vector with fixed A coefficient, t changes the NA coefficient by b2 and z changes the N²A coefficient by b2−v; g ranges over all five A coefficients. If either scalar vanishes, these fibers cannot all be reached, or the nonidentity central element acts trivially. Conversely, when both are nonzero, this triangular orbit calculation gives all 5³ points. The specified affine generators have order five, because their augmented 4×4 matrices are unipotent in characteristic five, and their commutator is the central translation displayed above. Thus the conditions construct genuine regular exponent-five Heisenberg actions.

The abstract cyclic basis must be tied to the actual quotient map. Its original generator is u(N)A for a unit of F5[N]/N³; the standard map with generator A has the same kernel, and the actual cocycle in that map is u^-1 times (1). If v≠0, the linear P-image already supplies all principal units of this algebra, realized by common right coordinate translations. The uniform C4 supplies every nonzero scalar. If v=0, the extra units needed are realized as below. Hence the cyclic normalization is an actual ambient equivalence. A central automorphism t↦tz^j changes b1 by a nonzero multiple of j and removes it. When v=0, the unit `1+kN²` is still realized: the actual top automorphism `g↦gz^j` changes η(g) by jη(z), and η(z)=b2N²A≠0; no unavailable right-translation unit is assumed. Scaling then gives one orbit with b2≠0. When v≠0, normalize v=1. Under an allowed triangular top automorphism `g↦g^i t^j`, `t↦z^ℓ t^d`, the parameters v and b2 both acquire the same factor d/i² after the canonical cyclic-basis normalization. Their ratio `r=b2/v` is therefore invariant. The two nonzero conditions give `r∈F5\{0,1}={2,3,4}`, and each value occurs. This yields three Jordan orbits when v≠0, one when v=0, and one square-zero orbit: **five classes for each of the four nonabelian kernel parameters**. The allowed unit and top changes here are induced by the common Hol(P) coordinate operations and uniform C4 in the cited actual-isomorphism formula; they are not an arbitrary GL(M) quotient.

All five types do yield admissible folders for each nonabelian α. Their linear action kills the center of B_α. Pulling the regular affine action back along F→B_α therefore makes the inactive one-sided P′ linear action trivial, so it factors through the required first P-coordinate. A cyclic vector gives the actual coordinate quotient. No nonidentity relevant top lies in T_α, and every other image in the regular B_α action is fixed-point-free. The uniform converse supplies every folder, faithfulness, normal-quotient simplicity and properness condition.

### Abelian quotient: four form orbits

For α=1/2, B is elementary abelian of order 5³. The cited cyclic regular-abelian algebra theorem identifies its action with principal units on `J=tF5[t]/(t⁴)`. The image of the inactive one-sided P′ is the distinguished central line W. It must act trivially linearly, so W is exactly the annihilator line `1+F5 t³`. A choice of identification transports the extraspecial commutator to a nonzero alternating form on the two-dimensional quotient `B/W` with values in W. There are exactly four such forms, indexed by their nonzero scalar β∈F5*.

An algebra substitution `t↦a1t+a2t²+a3t³` acts on B/W in logarithmic coordinates by a triangular matrix of determinant a1³, and on W by the same scalar a1³. Thus the weighted action on β is trivial. Common right translations and the uniform C4 realize the unit changes of a cyclic regular-module generator; central top automorphisms absorb lift choices. To verify completeness, apply the actual-equivalence proof of [the exponent-25 orbit theorem](../sources/factor-permutation/radical-free-a5-exponent25-orbits.md#actual-coordinate-equivalence) with J of dimension three and the distinguished line W=ann(J), rather than W=U^5. The cyclic-generator units are again all realized. A linear comparison of normalized cocycles η_ψ=ψ−1 preserves principal-unit multiplication and hence is an algebra automorphism; conversely the coordinate reindexing has its generator-unit discrepancy removed by actual units. The associated-abelian identification F/diag(W)→A by (x−y)/2 and the class-two reconstruction from β apply unchanged, with fifth-power map zero. Consequently formula (3) of the prime-power reduction gives precisely these weighted form orbits and no further ambient equivalences. Each nonzero β occurs: define the class-two Heisenberg presentation with commutator z^β, take the regular principal-unit action of B, and pull it back through F/T_(1/2). The inactive one-sided W acts trivially linearly because it maps to the annihilator line. The stated converse verifies the actual collision condition and all folder properties. Hence this kernel contributes **four classes**.

The count is `4·5+4=24`. The count is conditional on the structural reduction and actual-normalizer interfaces specified in this note.

### The exponent-25 order-125 exclusion

If P instead has order 5³ and exponent 25, every permitted central quotient B_α retains an element of order 25: an anti-central pair `(x,x^-1)` with x of order 25 has fifth power on the anti-central W-line, which meets no permitted T_α. Yet a 5-element of AGL3(F5) embeds as a unipotent 4×4 matrix, and every such matrix has order at most 5. Thus B_α cannot act regularly and faithfully affinely on M. No folder in the specified model exists for this P.

## 3. Why the table is exhaustive

The prime-power reduction forces the prime to be 3 or 5. For an odd extraspecial group the central quotient is symplectic, while its power map is either zero or a nonzero linear functional to its order-prime center. In rank one, a symplectic basis gives precisely the exponent-prime and exponent-prime-squared presentations used above and in the two order-27 proofs. In higher rank the cyclic-affine obstruction leaves only the rank-two exponent-25 case just counted. The order-125 exponent-25 argument excludes the last omitted rank-one possibility.

The four surviving models have different loop orders except for the two order-27 tops. Those two are distinguished by the intrinsic permutation group on a socle row: its exponent is 3 in one case and 9 in the other. Their isomorphism classes therefore do not overlap. Summing the rows gives 120.

## Scope, evidence and further questions

The theorem fixes the entire anti-abelianization envelope and the swap inversion. It does not classify every group with an extraspecial quotient, arbitrary factor-permutation actions, or arbitrary radicals. The [faithful-transitive extension](0065-transitive-camina-tops.md) addresses nonregular actions and gives eight additional classes in its stated models.

The source arguments received separate automated mathematical checks conditional on their upstream inputs. The 88-class source also records separate reruns of its exact finite certificate. Those checks are not human referee acceptance, a formal proof, or a literature-priority claim. The present exposition consolidates the [exponent-25 argument](../sources/factor-permutation/radical-free-a5-exponent25-orbits.md) and the [rank-one and assembly argument](../sources/factor-permutation/radical-free-a5-extraspecial-125.md); their mathematical reductions, rather than their review labels, are the premises used here.

A substantive next question is which non-Camina class-two tops admit the same cyclic affine collision data, and whether their actual normalizer orbits can be described uniformly. The Camina extension in the next note does not settle that problem.
