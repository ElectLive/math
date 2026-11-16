# Rank-one exponent-five top and odd extraspecial assembly

Mira Cult
This contributes to the [classification frontier](../../claims/0010.md). Let P be extraspecial of order 5³ and exponent 5, let `S=A5^P⋊P` with its regular coordinate action, let `G={(x,y)∈S²:ab(top(x))+ab(top(y))=0}`, and let τ swap the two S factors. Under the independently reviewed full-mark, cyclic-affine, actual-isomorphism and converse interfaces in [the prime-power top source](radical-free-a5-prime-power-top.md), exactly 24 loop-isomorphism classes of finite simple nonassociative left Bol loops have this canonical G and τ. All are proper, of order `5³·60^(5³)`. The quotient by the socle has order 5⁴ and acts through the regular P action on each row; it is not regular on all 250 socle factors.

The assembly at the end combines this case with pinned work on the other odd extraspecial tops. It is scoped to these exact regular-top anti-abelianization fiber models and makes no classification claim for general nonabelian tops, arbitrary factor permutation, or arbitrary radicals. The precise folder and normal-quotient inputs are those pinned by the prime-power source; the cyclic regular-abelian algebra theorem is reviewed.

## Central kernels and the nonabelian affine quotients

Let W=P′=Z(P)≅F5 and let `F=G/A5^(2P)`. The pinned reduction forces the actual mark to be full and the collision-free affine F-action on its cyclic three-dimensional F5 module M to have a central point stabilizer

`T_α={(αw,(1−α)w):w∈W}`,  `α∈F5`.

Every α gives a line avoiding the anti-central relevant line; these are all possible central kernels. The affine quotient B_α=F/T_α acts regularly on M, and

`B_α′=(1−2α)W`.

For α≠1/2, B_α is the extraspecial order-125 exponent-five group; for α=1/2, it is elementary abelian of order 125. The five α are invariant under the actual isomorphism interface: common automorphisms of P scale the two coordinates of W simultaneously and preserve α; uniform local C4 acts on M rather than interchanging these coordinates. The first and second socle rows have C5 and A4 H0 projections, respectively, so an isomorphism between standardized oriented data cannot swap them. We count their affine orbits separately. For α≠1/2 every automorphism of B_α is induced by a common automorphism of P: on the two-dimensional central quotient both are arbitrary GL2(F5) maps with the corresponding determinant action on the commutator line, and central lift changes are arbitrary homomorphisms of that quotient to W. The anti-central image is a nonzero central line in B_α, so common central automorphisms of P realize all such lift changes. This justifies the generator changes used below; no independent automorphism of one socle row is allowed.

## Nonabelian quotient: faithful linear action is impossible

For α≠1/2 let B=B_α. Its affine linear part factors through the first P-coordinate, as p=5. If α≠0, the kernel T_α has nontrivial first central projection, forcing the linear center to be trivial. The only remaining possibility for nonabelian linear image is α=0. In that case a nonabelian linear image of B is faithful: every nontrivial normal subgroup of extraspecial B meets its center, and killing the center makes the image abelian. A faithful subgroup of order 125 in GL3(F5) is a Sylow 5-subgroup and is conjugate to natural UT3. The centrality calculation used in the reviewed exponent-three order-27 case excludes this image for every odd prime, as follows.

In F choose `a=(g^-1,g)`, `b=(t^-1,t)`, `c=(1,z)`, `d=(z,1)` with `[a,b]=cd`, c,d central. For a faithful natural image choose a basis and generators with

`X=ρ(a)=I−E12`, `Y=ρ(b)=I−E23`, `Z=ρ(d)=I+E13`, `ρ(c)=I`.

Write x=η(a), y=η(b), w=η(d). Centrality of c puts η(c) in <e1>. Centrality of d with b gives `(Y−I)w=(Z−I)y`, hence w3=y3=0; centrality with a gives `(X−I)w=(Z−I)x`, hence w2=−x3. The second coordinate of `ab=cd·ba` gives w2=x3. Since 2≠0 in F5, w2=x3=0. Therefore η(cd^-1) lies in `<e1>=im(1−ρ(d^-1))`. But `cd^-1=(z^-1,z)` is nonidentity and relevant, contradicting the actual marked-square collision criterion. Thus the linear image is abelian.

## Nonabelian quotient: five cyclic affine types

A cyclic three-dimensional module for the abelian linear image has either every linear displacement square-zero, or an element with one Jordan block of length three. All linear elements are unipotent because B is a 5-group.

In the square-zero case, any two commuting square-zero endomorphisms R,S satisfy RS=0: if RSv≠0 then v,Rv,Sv,RSv are linearly independent. A cyclic generator and its images show that the displacement span has dimension two. After a top automorphism and basis normalization, the linear generators are `I+E13` and `I+E23`. Regularity and the commutator relation put the affine action into the unique actual-normalizer orbit represented by

`g=(I+E13,e2)`,  `t=(I+E23,e3)`,  `z=(I,e1)`.

The central automorphisms remove the e1 parts of the two translations, and the common right-translation module units remove the remaining W-part of η(t). A top scaling normalizes the nonzero second coefficient of η(g). These are actual operations in formula (3) of the reviewed reduction, not arbitrary affine coboundaries. For this square-zero module the original quotient generator can be used as e3; its two displacement images give e1,e2, so the kernel is the augmentation-ideal square. Common right translations realize all units with constant coefficient one, and uniform C4 supplies the nonzero scalar. The normalizations therefore retain the actual kernel, as in the reviewed [order-27 proof](radical-free-a5-extraspecial-27.md), with the same argument over F5. This gives one class.

In the Jordan case choose g with N=ρ(g)−1 satisfying N³=0≠N², and replace the other generator by a g-multiple to remove its first N coefficient. Let A=η(g) and B=η(t). The commutator displacement is η(z)=NB−vN²A, and centrality makes it N-fixed. Hence N²B=0. If A were also in NM, the translations of both generators would lie in NM; their linear parts preserve NM, so the entire affine orbit of 0 would lie in that proper plane, contradicting regularity. Thus A is cyclic. We have

`ρ(g)=1+N`,  `ρ(t)=1+vN²`,  `η(t)=b2·NA+b1·N²A`.          (1)

Indeed any N coefficient in ρ(t) can be removed by replacing t by a suitable g-multiple. The coefficient of A in η(t) is zero: ρ(z)=1 and η(z) is central, so it must be fixed by ρ(g). The commutator relation gives `η(z)=(b2−v)N²A`. Regularity is equivalent to `b2≠0` and `b2−v≠0`. In a vector with fixed A coefficient, t changes the NA coefficient by b2 and z changes the N²A coefficient by b2−v; g ranges over all five A coefficients. If either scalar vanishes, these fibers cannot all be reached, or the nonidentity central element acts trivially. Conversely, when both are nonzero, this triangular orbit calculation gives all 5³ points. The specified affine generators have order five, because their augmented 4×4 matrices are unipotent in characteristic five, and their commutator is the central translation displayed above. Thus the conditions construct genuine regular exponent-five Heisenberg actions.

The abstract cyclic basis must be tied to the actual quotient map. Its original generator is u(N)A for a unit of F5[N]/N³; the standard map with generator A has the same kernel, and the actual cocycle in that map is u^-1 times (1). If v≠0, the linear P-image already supplies all principal units of this algebra, realized by common right coordinate translations. The uniform C4 supplies every nonzero scalar. If v=0, the extra units needed are realized as below. Hence the cyclic normalization is an actual ambient equivalence. A central automorphism t↦tz^j changes b1 by a nonzero multiple of j and removes it. When v=0, the unit `1+kN²` is still realized: the actual top automorphism `g↦gz^j` changes η(g) by jη(z), and η(z)=b2N²A≠0; no unavailable right-translation unit is assumed. Scaling then gives one orbit with b2≠0. When v≠0, normalize v=1. Under an allowed triangular top automorphism `g↦g^i t^j`, `t↦z^ℓ t^d`, the parameters v and b2 both acquire the same factor d/i² after the canonical cyclic-basis normalization. Their ratio `r=b2/v` is therefore invariant. The two nonzero conditions give `r∈F5\{0,1}={2,3,4}`, and each value occurs. This yields three Jordan orbits when v≠0, one when v=0, and one square-zero orbit: **five classes for each of the four nonabelian kernel parameters**. The allowed unit and top changes here are induced by the common Hol(P) coordinate operations and uniform C4 in the reviewed actual-isomorphism formula; they are not an arbitrary GL(M) quotient.

All five types do yield admissible folders for each nonabelian α. Their linear action kills the center of B_α. Pulling the regular affine action back along F→B_α therefore makes the inactive one-sided P′ linear action trivial, so it factors through the required first P-coordinate. A cyclic vector gives the actual coordinate quotient. No nonidentity relevant top lies in T_α, and every other image in the regular B_α action is fixed-point-free. The uniform converse supplies every folder, faithfulness, normal-quotient simplicity and properness condition.

## Abelian quotient: four form orbits

For α=1/2, B is elementary abelian of order 5³. The reviewed cyclic regular-abelian algebra theorem identifies its action with principal units on `J=tF5[t]/(t⁴)`. The image of the inactive one-sided P′ is the distinguished central line W. It must act trivially linearly, so W is exactly the annihilator line `1+F5 t³`. A choice of identification transports the extraspecial commutator to a nonzero alternating form on the two-dimensional quotient `B/W` with values in W. There are exactly four such forms, indexed by their nonzero scalar β∈F5*.

An algebra substitution `t↦a1t+a2t²+a3t³` acts on B/W in logarithmic coordinates by a triangular matrix of determinant a1³, and on W by the same scalar a1³. Thus the weighted action on β is trivial. Common right translations and the uniform C4 realize the unit changes of a cyclic regular-module generator; central top automorphisms absorb lift choices. To verify completeness, apply the actual-equivalence proof of [the exponent-25 orbit theorem](radical-free-a5-exponent25-orbits.md#actual-coordinate-equivalence) with J of dimension three and the distinguished line W=ann(J), rather than W=U^5. The cyclic-generator units are again all realized. A linear comparison of normalized cocycles η_ψ=ψ−1 preserves principal-unit multiplication and hence is an algebra automorphism; conversely the coordinate reindexing has its generator-unit discrepancy removed by actual units. The associated-abelian identification F/diag(W)→A by (x−y)/2 and the class-two reconstruction from β apply unchanged, with fifth-power map zero. Consequently formula (3) of the prime-power reduction gives precisely these weighted form orbits and no further ambient equivalences. Each nonzero β occurs: define the class-two Heisenberg presentation with commutator z^β, take the regular principal-unit action of B, and pull it back through F/T_(1/2). The inactive one-sided W acts trivially linearly because it maps to the annihilator line. The pinned converse verifies the actual collision condition and all folder properties. Hence this kernel contributes **four classes**.

The count is `4·5+4=24`.

## The exponent-25 order-125 exclusion

If P instead has order 5³ and exponent 25, every permitted central quotient B_α retains an element of order 25: an anti-central pair `(x,x^-1)` with x of order 25 has fifth power on the anti-central W-line, which meets no permitted T_α. Yet a 5-element of AGL3(F5) embeds as a unipotent 4×4 matrix, and every such matrix has order at most 5. Thus B_α cannot act regularly and faithfully affinely on M. No folder in the specified model exists for this P.

## Assembly over odd extraspecial regular tops

For the exact model `S=A5^P⋊P`, G the anti-abelianization fiber and τ the swap, the resulting scoped table is:

| Top P | Class count | Source |
| --- | ---: | --- |
| Order 3³, exponent 3 | 2 | [Exponent-three order-27 source](radical-free-a5-extraspecial-27.md) |
| Order 3³, exponent 9 | 6 | [Modular order-27 source](radical-free-a5-nonabelian-27.md) |
| Order 5³, exponent 5 | 24 | The argument above |
| Order 5^5, exponent 25 | 88 | [Exponent-25 orbit source](radical-free-a5-exponent25-orbits.md) and its finite certificate |
| Every other odd extraspecial top | 0 | [Prime restriction](radical-free-a5-prime-power-top.md), [higher-rank exclusion](radical-free-a5-extraspecial-tops.md), and the order-125 exponent-25 exclusion above |

Completeness of the small top types can also be seen directly: an odd extraspecial group has symplectic elementary abelian central quotient, and its p-th-power map is either zero or a nonzero linear functional into its center. A symplectic basis puts the rank-one cases into the exponent-p and exponent-p² presentations used here, as in the elementary reconstruction in the exponent-25 source. The prime restriction leaves only p=3,5; the reviewed higher-rank theorem leaves only the displayed rank-two exponent-25 exception. Thus no additional odd extraspecial type is omitted.

The four surviving exact models have different orders except the two 3³ types. Those two are distinguished by the intrinsic socle-row factor-permutation group P (equivalently by exponent 3 versus 9), so their classes do not overlap. Under the pinned inputs, the table sums to 120 classes across these specified exact models. It is not a count of all finite simple Bol loops and does not settle general nonabelian tops.

The new rank-one proof and assembly are analytic; no new computation is claimed. The 88-class input retains its separately reviewed finite certificate. The unrestricted classification remains open.
