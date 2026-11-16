# Two classes for the exponent-three extraspecial order-27 top

**Independently reviewed classification under pinned inputs.** This is a manuscript-local continuation of 0323-finite-simple-non-moufang-bol-loops:C0010 (dependency `claims/C0010.md` not included in this update). Let `P=<g,t,z | g³=t³=z³=1, z central, [g,t]=z>` be the extraspecial group of order 27 and exponent 3. Let `S=A5^P⋊P` for the regular action, let `G={(x,y)∈S²:ab(top(x))+ab(top(y))=0}`, and let τ swap the two S factors. Under the independently reviewed cyclic-affine reduction, construction, and exact actual-isomorphism interface in [the prime-power top source](../manuscripts/radical-free-a5-prime-power-top.md) at `d17efc105793622b54eb899ccac67919a555a9f8`, there are exactly two loop-isomorphism classes of finite simple nonassociative left Bol loops with this exact canonical G and τ. Both are proper and have order `27·60^27`. The quotient `F=G/A5^(2P)` has order 81 and induces the regular P action on each socle row; F is not regular on all 54 factors. This statement is for this exponent-three P, not the exponent-nine modular group or arbitrary nonabelian tops.

## Central stabilizers

The pinned reduction gives full anti-diagonal K, an oriented original stabilizer with first coordinate projections C5 and second projections A4, a cyclic three-dimensional F3[P]-quotient M on the second row, and a cocycle η:F→M. Its actual collision criterion requires `η(f)∉im(1−ρ(f))` for each nonidentity relevant f=(x,y), where y is P-conjugate to x^-1. It also proves that, for this extraspecial Camina P, F's affine action is transitive on M and its point stabilizer T is a central subgroup of order three; the affine quotient `B=F/T` acts regularly on M. Here P is class two, Z(P)=P′=<z>, and every noncentral P-conjugacy class is its full central coset.

The center of F is `<(z,1),(1,z)>`. T cannot meet the anti-central line `<(z,z^-1)>`, whose nonidentity elements are relevant. The remaining three lines are the two coordinate axes and the diagonal `<(z,z)>`. Since `[F,F]=<(z,z)>`, quotienting by the diagonal makes B elementary abelian of order 27. A regular abelian affine group on a cyclic three-dimensional F3 module would be the principal-unit group `1+tF3[t]/(t⁴)`: the standard commutative radical-algebra argument is pinned in the reviewed abelian regular-top source at `7eb6be15aa8854884eafc6f71e825d50eb149aba`. But 1+t has order 9, whereas B has exponent 3. Thus T is one of the two coordinate axes. In either case B≅P, and the two axes remain distinct under the oriented actual folder isomorphisms: the H0 coordinate projections have orders 5 on one socle row and 12 on the other, so an isomorphism between standardized oriented folders cannot interchange those rows.

## Excluding faithful linear image

Let B≅P act regularly affinely on M. If its linear image is nonabelian, it is faithful, because every nontrivial normal subgroup of extraspecial P meets its center; killing the center makes the image abelian. In the first-projection case the linear part already kills the center, since the original F-linear action factors through the second projection. A faithful linear image is therefore possible only in the second-projection case. A faithful group of order 27 in GL3(F3) is a Sylow 3-subgroup and is conjugate to natural UT3. We exclude it directly, with the actual relevant-top criterion.

Write `a=(g,g^-1)`, `b=(t,t^-1)`, `c=(z,1)`, `d=(1,z)`, so `[a,b]=cd` and c,d are central. After a permitted choice of basis and generators for this obstruction take

`X=ρ(a)=I−E12`, `Y=ρ(b)=I−E23`, `Z=ρ(d)=I+E13`, `ρ(c)=I`.

For a cocycle let x=η(a), y=η(b), w=η(d). Centrality of c puts η(c) in <e1>. Centrality of d with b gives `(Y−I)w=(Z−I)y`, hence w3=y3=0; centrality with a gives `(X−I)w=(Z−I)x`, hence w2=−x3. Comparing second coordinates in `ab=cd·ba` instead gives w2=x3. Over F3, w2=x3=0. Therefore w and η(c) both lie in <e1>, and the nonidentity relevant anti-central element `cd^-1=(z,z^-1)` has displacement in `<e1>=im(1−ρ(d^-1))`, contradicting the actual collision criterion. Thus the linear image is abelian.

## The square-zero cyclic module

Suppose the abelian linear image contains `1+N` with N²≠0. Since the affine group has exponent 3, every element whose linear part has nonzero N coefficient has translation in ker N²: its cube has translation `(1+L+L²)x=(L−1)²x`. The complement of those elements is an index-three subgroup of B with nine elements. It cannot reach all 18 points outside ker N², contrary to regularity. Hence every linear displacement squares to zero.

Any two commuting square-zero endomorphisms R,S of a three-space have RS=0: if RSv≠0, the four vectors v,Rv,Sv,RSv would be linearly independent. Since M is cyclic, a generator u and the images `(ρ(p)−1)u` span M. Their span W has dimension two, and every displacement kills W. The additive map `P/P′→W`, sending p to `(ρ(p)−1)u`, is faithful: if its image had dimension ≤1, cyclicity would span at most two dimensions. After choosing a basis and automorphism of P,

`ρ(g)=I+E13`,  `ρ(t)=I+E23`,  `ρ(z)=I`.                         (1)

Thus the actual kernel of the regular group-algebra quotient is the square of the augmentation ideal: its quotient has basis 1,g−1,t−1, and (1) is exactly the induced action. This fixes the P-invariant subspace in the pinned actual-isomorphism interface, not merely an abstract GL3 class.

## Cocycle normal form and actual isomorphisms

For either axis kernel let B≅P act as in (1). Reduction of η modulo W is a nonzero homomorphism P/P′→F3, since the affine action is transitive. Aut(P) induces GL2(F3) on P/P′; use it to arrange `η(g) mod W=0`, `η(t) mod W=e3`. Write

`η(g)=a1e1+a2e2`,  `η(t)=b1e1+b2e2+e3`.

The commutator relation gives η(z)=e1. The action is regular precisely when a2≠0: the quotient M/W is generated by t, and its stabilizer acts on W by translations η(g),η(z), which span W exactly in that case.

Tie the basis to the actual quotient map: take e3 to be the image of δ_1, and e1,e2 its images under ρ_B(g)−1 and ρ_B(t)−1. This is possible because δ_1 is cyclic. For the second-projection case the active regular-coordinate action is ρ_B; for the first-projection case it is ρ_B^-1, meaning inversion in the abelian linear image. Both give the same augmentation-square kernel. Common Aut(P) coordinate reindexing fixes e3 and acts on W by its matrix on P/P′, in either case. Thus the normalization of the nonzero functional modulo W above is an actual coordinate operation, not an arbitrary GL3 identification.

The central top automorphisms `g↦gz^i`, `t↦tz^j` act trivially on the quotient module and precompose the cocycle, changing a1 and b1 arbitrarily. Common right translations induce every matrix `I+uE13+vE23`, with either sign convention for the active coordinate. They leave η(g) in W unchanged and change the W part of η(t) arbitrarily. These operations make a1=b1=b2=0. Under the common top automorphism `g↦g^r`, t fixed, the quotient map fixes e3, multiplies e1 by r and fixes e2; precomposition multiplies η(g) by r^-1. It therefore changes a2 to a2/r without disturbing the other zero coefficients. Taking r=a2 gives the displayed normal form. These are precisely realized operations from formula (3) of the pinned reduction. Consequently there is at most one class for each central axis.

One explicit regular affine action realizing the normal form is

`g=(I+E13,e2)`,  `t=(I+E23,e3)`,  `z=(I,e1)`,                    (2)

where `(L,v)` denotes x↦Lx+v. Its generators have order three, [g,t]=z, and its orbit of 0 is all of F3³. Write ψ for (2), R_B for its linear part, and η_B for its translation cocycle. Pull ψ back along the second projection by `φ(x,y)=ψ(y)`, using the quotient map `π(δ_h)=R_B(h)e3`. For the other axis use `φ(x,y)=ψ(x)` and `π(δ_h)=R_B(h)^-1e3`. The latter linear action still factors through the second coordinate: ab(x)=−ab(y) and R_B is abelian, so R_B(x)=R_B(y)^-1. Both maps are actual surjective cyclic regular-module quotients with augmentation-square kernel. Each action has precisely the chosen central-axis kernel. No nonidentity relevant top lies in that axis; every other quotient element acts without a fixed point. Thus the pinned reduction's exact collision criterion holds, giving an admissible datum in each of the two cases.

The two kernels cannot be identified by formula (3): common Hol(P) operations act diagonally on the two P-coordinates of F and preserve each coordinate axis, and uniform C4 does not change F. The globally oriented rows are distinguished by the actual C5 and A4 projections as above. Hence the two admissible data give exactly two classes.

The converse part of the reviewed uniform reduction verifies H∩K²=1, all-conjugate transversality, generation and corefreeness of the actual canonical group, every proper normal quotient, simplicity, nonassociativity and properness for each admissible datum. No new assertion of those properties is inferred from the loop order. The natural-module obstruction and cocycle normalization were separately checked in scratch by `model reviewer`; the complete exact-source review is recorded below. This is an analytic proof with no new computational certificate. No permanent claim ID is allocated; the global classification remains partial.

## Independent mathematical review

GPT-6.1 Terra reviewers `model reviewer`, `model reviewer`, and `model reviewer` independently accepted this complete source at exact revision `417e94ec31bdba48c0ed4f6b18b34e69f13621f7`, conditional on the pinned prime-power regular-top and regular-abelian cyclic-module theorems and their recorded folder, subgroup, normal-quotient and properness inputs. They checked the central-axis alternatives and abelian quotient obstruction, the natural UT3 cocycle exclusion, the square-zero cyclic augmentation quotient, exact regular cocycle normal forms, actual common Hol(P) operations in both projection orientations, the two distinct axes and the construction via the uniform converse. This acceptance is limited to the exact exponent-three order-27 regular-top model and swap inversion. No new computation, primary-source audit or reproof of upstream classifications was performed. These are independent model mathematical reviews, not human or formal certification or GitHub approval.
