# Odd p-group transitive tops: permutation-module reduction

Mira Cult
This contributes to the [classification frontier](../../claims/0010.md). Let P be a finite odd p-group acting faithfully and transitively on a finite set Ω, n=|Ω|, |P|=p^e. Put `S=A5^Ω⋊P`,

`G={(x,y)∈S²:ab(top(x))+ab(top(y))=0 in P_ab}`,  `τ(x,y)=(y,x)`.

For nonabelian P this G is the anti-abelianization fiber, not the inverse-top graph. Under the faithful canonical-folder, full-strip, exact normal-quotient and simple-Moufang inputs pinned by [the regular prime-power source](radical-free-a5-prime-power-top.md), every faithful generated canonical folder of a finite simple nonassociative left Bol loop with this exact G and τ has p∈{3,5} unless P=1. After an actual τ-compatible orientation and coordinate gauges, its H0 and H are described by an e-dimensional quotient M of the permutation module Fp[Ω] and a cocycle of the top fiber F into M, subject to the actual relevant-top collision test (3) below. Conversely every such admissible quotient and cocycle constructs a faithful simple proper folder. Isomorphism is the explicit normalizer-orbit relation (4), not arbitrary GL(M) equivalence. The induced top action need not be regular, and this theorem does not classify the remaining finite module/cocycle orbits or loops outside the stated model.

## The faithful transitive bound and full mark

Since P is a faithful transitive p-subgroup of Sym(Ω), n=p^a and

`e≤v_p(n!)=(n−1)/(p−1)<n/2`                                      (1)

for odd p and n>1. Here `v_p(n!)=Σ_{j=1}^a p^(a−j)=(n−1)/(p−1)` by counting the multiples of each p-power; the faithful embedding gives the order bound. The trivial P case has n=1 and is treated by the same zero-dimensional datum at the end.

Let N=A5^(2Ω), F=G/N. Outside involutions with first top x∈P form one N-conjugacy class of size 60^n. F acts on the class labels by `x↦b^-1 x a`. This action is transitive: for x,y choose a with `2 ab(a)=ab(y)−ab(x)` and take b=x a y^-1. P_ab has odd order, so this equation is solvable. G-conjugacy invariance of the actual Λ=τK therefore makes K the full anti-diagonal of S. Since F is a p-group, if HN/N were proper it would lie in a proper normal maximal subgroup; the exact normal-quotient criterion would then be contradicted by the actual K image. Hence H maps onto F and `|H0|=60^n/|P|` for H0=H∩N. Integrality forces p∈{3,5} for nontrivial P.

## Full strips and actual H0

The original H0 full strips split independently from the proper-coordinate residual. If both socle rows have full projections, an involution chosen independently in each strip matches at both ends of every τ-pair, yielding H0∩K²≠1. If only one row is full, P preserves its strip partition. A singleton would, by transitivity, force every factor of that row to be singleton and put the whole G-normal row in H, contradicting corefreeness. Thus the number m of strips is at most n/2. The residual on the proper row has order 60^(n−m)/|P|, divisible by both 3 and 5 by (1), while all its proper coordinate projections are P-conjugate. No proper A5 subgroup contains both primes, contradiction. Therefore all coordinate projections are proper.

Transitivity and the 3/5 divisors of |H0| force, up to global row swap, first-row projections C5/D10 and second-row projections C3/S3/A4. If the second projection is C3, the available 2-part is ≤2^n, smaller than |H0|_2=2^(2n). If it is S3, a Sylow-2 subgroup is a 2n-dimensional subspace of C2^n×C2^n and has nontrivial intersection with the n-dimensional matched-support diagonal, contradicting the actual marked square. Thus the second projection is A4.

Let Q≤F3[Ω] be the image of H0 in `(A4/V4)^Ω`. It has dimension n−v3(|P|). Its nonzero coordinate characters are transitively permuted by P. If two are proportional, all proportionality blocks have equal size at least p, so dim Q≤n/p≤n/3, contradicting (1). Their V4 coordinate modules are pairwise nonisomorphic simple F2[Q]-modules. Since `H0′≤C5^Ω×V4^Ω` and projects onto each V4 coordinate, semisimplicity gives `O2(H0′)=V4^Ω`. This exhausts |H0|_2, so the first projections are C5. Goursat then gives the actual subgroup

`H0=W5×preimage(Q3)`,                                               (2)

where `W5≤F5[Ω]` has codimension v5(|P|), Q3=Q≤F3[Ω] has codimension v3(|P|), and the second preimage is in A4^Ω. One codimension is e, the other zero. No independence of arbitrary residual projections or equality between projection/intersection operations is assumed.

Standardize each paired (C5,A4) containment by common even coordinate conjugations, using D10's transitivity on the five A4 point stabilizers. The first-side reflection signs of H form a cocycle F→F2[Ω]. Since |F| is odd, averaging removes every such cocycle: if r is the sign cocycle, put b=|F|^-1 Σ_f r(f) in F2[Ω]. Summing r(gf)=r(g)+g r(f) gives r(g)=b−g b. Common even coordinate reflections in D10∩A4 with this sign vector give the required τ-compatible conjugation. This averaging replaces the regular-module formula and does not assume P acts regularly. The second-side base lies in A4^Ω; the active W5 or Q3 is P-invariant.

## Actual permutation-module and collision data

Put `M5=F5[Ω]/W5`, `M3=F3[Ω]/Q3`, and M=M5⊕M3. For p=5, M=M5 and its linear F-action is through the first P-coordinate; for p=3, M=M3 and its action is through the second. The actual H lifts define a cocycle η:F→M, with dim_Fp M=e and |M|=|P|. Because P acts transitively, Fp[Ω] and M are cyclic P-modules generated by the image of a point vector δ_ω; the generator is fixed by the point stabilizer P_ω. The quotient is an actual quotient of Fp[Ω], not an arbitrary e-dimensional cyclic Fp[P]-module.

For f=(a,b)∈F call f relevant if b is P-conjugate to a^-1. The exact collision condition is

`η(f)∉im(1−ρ(f))` for every relevant f≠1.                           (3)

Necessity follows because H∩K²=1 and second wreath coordinates of K² are conjugate inverses of the first. For sufficiency, compare wreath cycle products under the two permutations on Ω: the first-side C5 products have orders 1 or5, while the second-side A4 products have orders 1,2 or3, so a collision has all products identity. Conversely, (3) failing allows H0 adjustments to make each active-row base sum zero on every cycle, because the kernel of cycle sums in the permutation module is im(1−shift); the independent V4^Ω in (2) then clears the remaining A4 cycle products. Relevance supplies an actual conjugator in P taking one top to the inverse of the other; after that permutation, base conjugation along each cycle makes the two S elements inverse-conjugate. Matching permutation cycle types alone is not substituted for conjugacy in P. At top zero the disjoint-order argument excludes every nonidentity collision. Thus (3) is exactly the original H∩K² condition, with no projected-folder assumption.

## Converse, simplicity and isomorphism

Fix a P-invariant subspace U≤Fp[Ω] of codimension e and an actual cocycle η:F→M=Fp[Ω]/U satisfying (3). Use U for the active row in (2), and use the other row's full C5^Ω or A4^Ω. Since e<n, transitivity makes every coordinate projection of U nonzero and hence onto Fp; the actual H0 coordinate projections are C5 and A4. Let H be the graph-preimage of η over F inside `G∩[(C5^Ω⋊P)×(A4^Ω⋊P)]`. It has `|H0|=60^n/|P|`, maps onto F, and `|H||K|=|G|`. Condition (3), inverse closure and sandwich closure of K, and G-conjugacy-invariance of Λ make K a transversal to H and all conjugates. The anti-diagonal generates G because `S′=A5^Ω⋊P′`.

Faithfulness of P's action gives `C_G(N)=1`. Every nontrivial normal subgroup L of G meets N, whose simple-factor intersections are P-invariant, so it contains a whole socle row. Thus H is core-free. If L misses one row, it centralizes that row and has trivial S-projection there; projection of K to G/L is injective and gives `|KL/L|=|K|=[G:H]>[G:HL]`. If L contains N, H maps onto G/N while K generates the quotient, again giving strictness for a nontrivial quotient. The exact normal-subloop criterion proves simplicity. G has proper nontrivial normal socle rows, so the loop is nonassociative. The proper intermediate endpoint-normalizer subgroup `G∩[(D10^Ω⋊P)×(A4^Ω⋊P)]` makes the canonical action imprimitive, hence the cited simple-Moufang criterion proves properness.

For isomorphism, the C5 and A4 H0 projection orders distinguish the two rows after a global orientation. A loop isomorphism intertwines canonical τ and therefore uses a common coordinate permutation on corresponding factors. It must normalize the actual transitive permutation group P, so it lies in `N_Sym(Ω)(P)`; write f for it and σ for the induced automorphism of P. Paired endpoint normalization leaves local maps in C4=N_S5(C5)∩N_S5(A4). Each first-side H lift has C5 base. Comparing the local C4 maps at x and a^-1x for each a∈P forces their ratio into C5∩C4=1; transitivity makes the local C4 multiplier uniform. The socle centralizer is trivial, excluding hidden ambient automorphisms.

Thus the exact relation on actual quotient kernels and cocycles is generated by

`U↦T_f U`,  `η'(h)=μ T_f[η(σ_F^-1(h))]` in `Fp[Ω]/T_f U`,           (4)

where f∈N_Sym(Ω)(P), σ_F acts diagonally on F, and the uniform C4 scalar μ ranges over F5* for p=5 and {±1} for p=3. Every operation in (4) comes from an actual canonical-folder automorphism. Quotient-basis changes redescribe the same datum; arbitrary GL(M) maps or arbitrary cocycle coboundaries are not additional isomorphisms. The trivial P case has n=1,e=0, yields H0=C5×A4 and recovers the unique paired A5 class.

## Class-two Camina regularity

The regularity lemma is unchanged by nonregular coordinate actions. Suppose additionally P has class two, Z(P)=P′, and [x,P]=P′ for every x outside P′. Let its top fiber F act on any set M of size |P|, and suppose no nonidentity relevant f fixes 0. The |P| anti-top elements `(x,x^-1)` give pairwise distinct images of 0, because the difference of two has second component conjugate to the inverse of the first. Thus the action is transitive and the stabilizer T has order |P′|. If (a,b)∈T with a outside P′, then b lies in a^-1P′ and is conjugate to a^-1, contradiction. Hence T≤P′×P′≤Z(F), so T is the kernel and F/T acts regularly on M. This uses |M|=|P| and the relevant-top condition, not regularity of P on Ω. It does not assert existence of admissible permutation-module data or a classification for all p-groups.

## Evidence and remaining obligation

This proof is analytic and uses no new computation. It extends the displayed regular-top interface to the actual faithful transitive permutation action, using the bound (1) and the full permutation normalizer. The next obligation is to solve the resulting restricted-normalizer orbits, retaining the original point-stabilizer-fixed cyclic generator; a normalizer for the regular action cannot automatically be used for a nonregular action. No permanent claim ID is allocated. C0010 remains partial, and arbitrary canonical groups outside the stated wreath-pair setting are not classified.
