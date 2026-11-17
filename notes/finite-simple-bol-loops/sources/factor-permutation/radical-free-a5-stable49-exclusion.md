# A nonnilpotent stable-orbit exclusion

**Mira Cult**

**Independently reviewed exclusion at the exact source below.** This continues [0323:C0010](../../claims/0010.md). The original faithful-folder and strict normal-quotient inputs are [C0001](../../claims/0001.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45); actual canonical inversion and marked classes are [C0007](../../claims/0007.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The stable-orbit local theorem and singleton-supported collision input are [the odd-top source](radical-free-a5-odd-top-surjectivity.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/3b9e8ae5ff1a9c1562d9a8aba4e8eefd80bcdc46); the full-strip separation and original selected-class-square parity interfaces are pinned there. Let Q=(F7²)⋊C3 with the C3 generator acting diagonally by 2,4, and let θ swap the axes and invert C3. Let Q act on Ω=Ωs⊔Ω1⊔Ω2, where Ωs=Q/⟨c⟩≅F7² is faithful and τ-stable, τ(a,b)=(b,a). Writing A,B for the first and second F7 axes, let Ω1=Q/(B⋊⟨c⟩) and Ω2=Q/(A⋊⟨c⟩); τ exchanges them. Thus |Ω|=63, and pure τ has f=7 fixed factors and c=28 swapped pairs. Assume its local fixed-factor automorphisms are identity, not merely inner. Let G=A5^63⋊Q and suppose (G,H,K,τ) is a faithful generated canonical folder of a finite simple nonassociative Bol loop. No H→Q, residual-product, or quotient-folder assumption is made.

The actual stable-orbit local theorem forces every H0=H∩N projection on Ωs to be A5. If one were proper, every selected involution would have double-transposition marks at every fixed factor of this stable orbit. But τ itself is selected and has seven identity marks there. This is a direct contradiction. Original full A5 strips split from the proper residual by the pinned Goursat input.

Let w be the total fixed-mark weight over a selected top label. The centralizer C_Q(θ)=diag(F7) rotates the seven fixed factors regularly. Selected patterns of inner fixed marks are unions of its binary necklaces; each double contributes 15 and pure τ supplies the empty pattern. All nonconstant necklaces have cardinality seven, while the optional all-double pattern has weight 15^7. Therefore

 w≡1 or 2 (mod 7).                                                (1)

The full actual top projection of Λ has |I|=21 labels, and each N-class over a label has 60^28 times its fixed weight. Thus |K|=21·60^28w, |H|=7·60^35/w, and (1), together with 7∤|N|, forces the 7-part of |U|=|HN/N| to be exactly 7. The original strict normal cut L=N⋊F7² forces U→Q/F7²≅C3 onto: otherwise |KL/L|=[G:HL]=3. Consequently |U|=21 and |H0|=60^35/(3w). Its intersection with F7² is an eigenline. The two possibilities are exchanged by θ; actual τ-fixed diagonal-top conjugations move the complements within either choice. Normalize U to the first eigenline semidirect C3.

Then U has stable-orbit sizes 7,21,21 on Ωs; on the paired seven-point orbits its sizes are 7 and 1,3,3. The following argument allows arbitrary strips crossing the stable and paired factor sets, and does not assume the existence of a literal singleton.

## Excluding the absence of a stable singleton

Assume no literal singleton strip lies in Ωs. Since pure τ is selected, the empty fixed-mark pattern occurs, and every other local pattern has weight divisible by 15. Thus w≡1 (mod 15), so v3(w)=v5(w)=0. Let b be the number of full-projection coordinates among the paired 14 factors, and m the number of full A5 strips. There are 49+b full coordinates and p=14−b proper coordinates. The actual residual R has

 v5(|R|)=35−m,       v3(|R|)=34−m.

No proper A5 subgroup has both 3 and 5 in its order, and either valuation per proper coordinate is at most one. Coordinate-kernel filtrations therefore give 69−2m≤14−b, without any residual independence. Equivalently the full-strip excess

 e=(49+b)−2m=Σ_strips(|S|−2)

satisfies e≤−6.

All singleton strips lie among the paired 14 coordinates. The union of actual selected matchings between the two paired seven-point Q-orbits is the complete bipartite graph: inverted top labels supply all seven relative shifts. Two singleton strips at matched endpoints would give an actual class-square collision by choosing a nonidentity involution in each. Hence singletons can lie in at most one paired row. U is transitive on the first row, so a singleton there would make the entire Q-orbit individual factors lie in H0, contradicting corefreeness. On the other row its orbit sizes are 1,3,3; at most six coordinates can be singleton, again excluding the whole Q-orbit. If a is the number of singleton strips then e≥−a≥−6. Thus a=6, e=−6, and every other full strip has size exactly two. The six singletons are precisely the two U-orbits of size three in the second row.

The remaining full strips give a U-invariant pairing. An odd transitive U-orbit cannot be paired internally, and a U-equivariant pairing between two transitive orbits requires equal size. The two 21-point stable U-orbits therefore pair with one another. The seven-point stable U-orbit must pair with the first paired row of size seven; the lone fixed coordinate of the second row cannot serve. Hence b=13 and m=34. There is exactly one proper coordinate, the U-fixed point of the second row. Its residual projection has 5-valuation 1 and 3-valuation 0, so it is C5 or D10 and has 2-valuation at most 1.

On the other hand the exact residual order has 2-valuation 70−v2(w)−2m=2−v2(w). Since w contains the empty pattern, w=1 or w≥16. If w=1 this valuation is 2, impossible for C5/D10; if w≥16 then v2(w)≥4 because w divides 7·60^35 and is coprime to 3,5,7 by (1) and w≡1 mod 15, so the valuation is negative. Both are impossible. Therefore an actual stable singleton strip exists, and the original singleton-supported class-square argument forces w=1. This deduction reduces the problem to the surviving singleton branch.

## Remaining singleton support

In additive affine coordinates the actual inverted top labels are q=(t,−4^j t)c^j, and their factor reflections act by

 σ(a,b)=(t+2^j b, 4^j(a−t)),      t∈F7, j∈{0,1,2}.

A singleton strip makes its entire U-orbit singleton. For either 21-point U-orbit, choose b≠0; (0,b) and (−b,2b) lie in the same U-orbit and are swapped by σ with j=0,t=−2b. Their two independent singleton A5 factors give a forbidden actual class-square collision. Thus singleton strips cannot occur in either 21-point U-orbit.

The size-seven U-orbit b=0 is different. If σ(a,0)=(a′,0), then 4^j(a−t)=0 gives t=a and hence a′=a. Therefore no selected matching swaps two distinct factors in that orbit. The simple singleton-support argument does not exclude it; this is the remaining branch after the preceding valuation reduction. In particular, a formula with q=(t,−t)c^j for j≠0 would be wrong and would falsely imply an internal edge.

## Excluding the remaining singleton branch

The seven singleton strips lie on the stable U-orbit b=0, and w=1. Let m_s be the number of original full strips meeting Ωs. First take the original normal cut L=N_paired, the product of all 14 paired socle factors. The whole top Q remains. The image of H0 on the stable factors is the independent product of the m_s nontrivial projections of its original full strips, of order 60^m_s; all stable coordinate projections are full, so no proper residual lives there. Since |U|=21, the full image of H has order 21·60^m_s. The marked image has 21·60^21 elements: all selected fixed local marks on Ωs are identity, and τ has 21 swapped pairs there. The strict original normal-quotient criterion gives

 21·60^21 > 7·60^(49−m_s),

so m_s≥28. No quotient loop is assumed.

The seven b=0 factors are singleton strips. Any strip meeting the other 42 stable factors in exactly one coordinate would have a U-orbit of size 21, because the two remaining stable U-orbits have size 21. Such a strip is not a literal singleton, so its 21 disjoint translates would require at least 21 paired factors, but only 14 exist. Every remaining stable-touching strip therefore contains at least two stable factors. Hence m_s≤7+42/2=28, and equality holds.

Consequently there are exactly 21 other stable-touching strips, each containing precisely two stable coordinates. The U-invariant pairing cannot pair either transitive 21-point orbit internally: an odd set has no invariant perfect matching. It must pair the two 21-orbits with one another, and these strips form one U-orbit of size 21. If one such strip had an additional paired coordinate, its disjoint U-translates would consume at least 21 paired factors. Thus all 28 stable-touching strips are wholly contained in Ωs.

The independent full-strip decomposition now gives H0=T_s×H_pair, with |T_s|=60^28 and |H_pair|=|H0|/60^28=60^7/3. Take the second original normal cut L=N_stable. In G/L the image of H has order |U||H_pair|=21·60^7/3=7·60^7, and the quotient group has order 147·60^14. Hence its index is 21·60^7. The original marked set projects onto 21 top labels and has 60^7 choices on the seven paired factor pairs, so |KL/L|=21·60^7. This equality contradicts the strict normal-quotient criterion. ∎

Together with the previous section, this excludes the displayed 49+7+7 model with pure identity local τ marks. It does not cover the outer-local-mark variants or arbitrary nonnilpotent top actions. The exact-source reviews below apply to this pure-inversion theorem.


## Independent exact-source review

reviewers contributor 1, contributor 2 and contributor 3 independently accepted the complete source at [the source revision](https://github.com/Mira-Cult/math-wip/commit/8aee3447a14e2c1dbed913cb63bf2acc43badce4). They checked the direct selected-τ local argument, necklace weight congruences, forced top image, full-strip capacity with crossing strips allowed, complete-bipartite singleton restriction, every U-invariant pairing case, the corrected affine reflection formula, and both original normal cuts including the equality case and prohibition of cross attachments. None assumed that a projected folder is a loop or that H surjects onto Q.

The reviews retain the pinned original-folder, local-character, strip and class-square interfaces; none independently reproved all upstream inputs, ran a computation or made a new primary-source audit. These are model mathematical reviews, not formal GitHub approvals or human/formal certification. The scope remains exactly the displayed action and pure local inversion; other marks require their own argument.

## Extension to all local inversion maps

**Independently reviewed extension at the exact source below.** Keep exactly the same group G, the same Q-action on the 49+7+7 factors and the same factor permutation of τ, but allow arbitrary local automorphisms for an involutory τ inducing the displayed θ on Q. Then the same nonexistence conclusion holds. The earlier review record applies only to the pure-inversion theorem above, not to this extension.

The local Out(A5) class of τ is constant on a transitive Q-orbit: τ normalizes G and its conjugation of a pure top element can differ from another pure top element only by inner factor maps. Suppose first this parity is outer on Ωs. Each of the seven fixed local involutions is an S5 transposition, in its unique A5-conjugacy class of size 10. At each swapped pair there is one N-conjugacy class, regardless of its local parity. All 21 outside top-involution labels occur because Λ is G-invariant and contains τ; each has exactly one such N-class. Thus

 |K|=21·60^28·10^7.

The original selected-class-square parity argument gives v2(|K|)≥2·28+2·7=70: at each fixed outer transposition the local class square contains every A5 involution. But the displayed cardinality has 2-valuation 63, contradiction. This uses neither H→Q nor a decomposition of H0.

Now suppose the stable-orbit parity is inner. For each outside top label, write w for the sum of the weights 15^d of the selected fixed-mark patterns, where d is the number of double transpositions among the seven fixed factors. These patterns are unions of binary necklaces under the regular C7-action of C_Q(θ). In particular

 |K|=21·60^28 w,       |H|=7·60^35/w.                            (6)

The identity/empty pattern is **not** assumed selected: an inner double transposition is not conjugate to the identity.

If an actual selected involution λ0 has the empty pattern, use the independently reviewed general repointing theorem in [odd layers in even envelopes](../odd-completion/odd-layers-in-even-envelopes.md#minimum-rank-repointing-on-one-odd-layer) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/17e56bdfb16097218249f42f10e91adcb9f5a4b8). It replaces τ by conjugation with λ0 and K by λ0Λ, preserving G, H, Λ, every original normal-cut cardinality, simplicity and nonassociativity. It does not assert loop isomorphism or preservation of properness. The new outside top involution is Q-conjugate to θ. On each exchanged pair of Q-orbits, a constant outer coordinate gauge on one orbit removes any swapped-pair outer parity while preserving pure Q; the stable orbit has inner parity. Socle conjugation then clears the remaining local maps on all swapped pairs. The seven fixed local maps are identity, so the resulting involution is pure and is excluded by the reviewed theorem above. That theorem requires a simple nonassociative folder, so no preservation of properness is needed.

It remains to suppose the empty pattern is not selected. Since 7∤|N|, (6) gives v7(|U|)=1−v7(w)≤1 for the actual top image U=HN/N. The original normal cut N has |KN/N|=21, so strictness requires 21>[Q:U]=147/|U|, equivalently |U|>7. The subgroup orders of Q are 1,3,7,21,49,147: its normal 7-subgroup has rank two and the quotient has order three. The 7-adic bound excludes orders 49 and 147, while the strict N-cut excludes orders 1,3 and 7. Hence |U|=21 and v7(w)=0.

A nonconstant binary necklace of length seven has size seven. The empty necklace is absent; the only other one-point necklace is the all-double pattern, of weight 15^7. Thus w≢0 mod 7 forces the all-double pattern to be selected, and

 w=15^7+7∑_{d=1}^6 a_d 15^d,                                    (7)

where 0≤a_d≤(1,3,5,5,3,1)_d. For the selected all-double class, the original parity expansion yields v2(|K|)≥2·28+2·7=70. Since v2(21·60^28)=56, this requires 2^14∣w. The standalone exact certificate [verify_stable49_mark_weights.py](../code/verify_stable49_mark_weights.py) constructs the seven-bit rotation orbits, verifies the necklace counts and checks every one of the 2,304 possible coefficient vectors in (7). It asserts that none yields 2^14∣w. This contradiction excludes the inner no-empty branch.

This extension is limited to the displayed 49+7+7 factor action and its prescribed inversion permutation. It does not exclude stable orbits for arbitrary nonnilpotent tops. The certificate is a finite arithmetic check, not independent mathematical review of the surrounding argument.

## Prime-uniform pure-inversion extension

**Independently reviewed extension at the exact source below.** Let p≥7 be prime with p≡1 mod3, let r∈Fp* have order 3, and put Q=(Fp²)⋊⟨c⟩ with c acting by (r,r⁻¹). Let θ interchange the axes and invert c. The faithful Q-set Ω has a τ-stable component Ωs=Q/⟨c⟩≅Fp² and two exchanged p-point components Ω1=Q/(B⋊⟨c⟩), Ω2=Q/(A⋊⟨c⟩), where A,B are the two axes. Let G=A5^Ω⋊Q and τ be the pure factor permutation induced by θ, with identity fixed local maps. Then no faithful generated canonical folder of a finite simple nonassociative Bol loop has this G and τ. This is the pure-inversion statement; no general local-mark extension is claimed.

Use the original-folder and strict-cut inputs C0001 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), actual inversion/mark input C0007 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813), and the stable local and class-square inputs in `radical-free-a5-odd-top-surjectivity.md` at [the source revision](https://github.com/Mira-Cult/math-wip/commit/3b9e8ae5ff1a9c1562d9a8aba4e8eefd80bcdc46). No stabilizer-top surjectivity, projected folder, or residual independence is assumed.

There are f=p fixed factors, c=p(p+1)/2 swapped pairs, and |I|=3p outside top labels. The stable local theorem makes all p² stable H0 projections full: one proper projection would force every selected fixed mark in this orbit to be double, contradicting the p identity marks of the selected pure τ. Let w be the total selected fixed-mark weight for each top label. Pure τ supplies the empty pattern, and the centralizer C_Q(θ)=diag(Fp) rotates the p fixed factors regularly. Nonconstant binary necklaces have size p, and the optional all-double pattern contributes 15^p. By Fermat, w≡1 or 16 (mod p); in particular p∤w. Also w≡1 (mod 15). The exact marked and transversal counts give

 |K|=3p·60^c w,   |H|=p·60^s/w,   s=(p²+3p)/2.                 (1)

Since p∤|A5^Ω|, the actual top image U=HN/N has p-part exactly p. The strict cut N⋊Fp² forces U onto C3, hence |U|=3p. Its intersection with Fp² is one of the two eigenlines. The two choices are related by τ-compatible automorphisms: θ exchanges them, while conjugations by θ-fixed diagonal translations move the complements. Fix the first eigenline. Then U-orbits on Ωs have sizes p and 3p, the latter occurring (p−1)/3 times; on the paired rows they have sizes p and 1+3+⋯+3. As p≡1 mod6, (p−1)/3 is even. From (1), |H0|=60^s/(3w).

Assume first that there is no stable literal singleton; no tensor existence assertion about cross-strips is needed. Let b be the number of full paired coordinates and m the number of original full strips. The proper residual is supported on 2p−b coordinates, and its 5- and 3-valuations are s−m and s−1−m, because w≡1 mod15. A proper A5 subgroup has at most one of these prime divisors, with valuation at most one. Thus

 2s−1−2m ≤ 2p−b,   e:=p²+b−2m≤1−p.                             (2)

Here e is the sum of |S|−2 over original full strips. The union of selected matchings between the paired rows is complete bipartite: the labels (t,−t) cover every relative shift. Singleton strips can therefore occur in at most one paired row. U is transitive on the first row, where a singleton would force an entire Q-normal socle orbit into H, contradicting core-freeness. On the other row the number is at most p−1. Therefore e≥−(p−1), and (2) forces equality: there are exactly p−1 paired singletons and all remaining full strips have size two.

Those singletons form all nonfixed U-orbits in the second paired row. The remaining U-invariant pairing cannot pair an odd transitive orbit internally, and it pairs only orbits of equal size. Hence the p-point stable orbit pairs with the first paired p-row, while the stable 3p-orbits pair among themselves in pairs. The only proper coordinate is the U-fixed point on the second paired row. Consequently m=s−1, and its residual projection has 5-valuation 1 and 3-valuation 0. It is C5 or D10, with 2-valuation at most 1. But the exact residual order has 2-valuation 2−v2(w). As w divides p·60^s and is coprime to 3,5,p, it is a power of 2. Either w=1, yielding the impossible 2-valuation 2, or w≥16 because the empty pattern is selected and every other class has weight at least 15, yielding a negative valuation. This contradiction proves that a stable singleton strip exists; the reviewed singleton-supported collision then forces every selected stable fixed mark to be identity, so w=1.

The inverted top labels are q=(t,−r^(−j)t)c^j. In the stable affine coordinates, σ=qτ acts by

 σ(a,b)=(t+r^j b, r^(−j)(a−t)).                                  (3)

Every singleton's whole U-orbit consists of singleton strips. For b≠0, the two distinct points (0,b) and ((1−r)b,rb) lie in the same 3p-orbit and are interchanged by (3) with j=0,t=−rb. Their two singleton A5 factors yield an actual marked-square collision. Thus the stable singleton lies on the p-point orbit b=0, all p factors there are singleton strips, and w=1.

Let m_s be the number of original full strips meeting Ωs. For the original normal cut killing the paired socle factors, the actual marked image has 3p·60^((p²−p)/2) elements, while the quotient index is p·60^(p²−m_s). Strictness implies m_s≥p(p+1)/2, since 3<60. The p singleton strips contribute p. Any remaining strip meeting Ωs exactly once has a U-orbit of size 3p and, being nonsingleton, would consume at least 3p of the 2p paired factors. Hence every other stable-touching strip contains at least two stable coordinates, and m_s≤p+(p²−p)/2=p(p+1)/2.

Equality forces all the remaining stable-touching strips to have exactly two stable coordinates. The 3p-orbits cannot be internally paired because they have odd size; each strip orbit therefore pairs two distinct 3p-orbits and has size 3p. None can contain a paired coordinate, since its disjoint translates would require 3p>2p such coordinates. All stable-touching strips are isolated. The independent decomposition gives the remaining paired subgroup of H0 order 60^(s−m_s)/3=60^p/3.

For the second original normal cut, kill the stable socle factors. The H-image has order (3p)(60^p/3)=p·60^p; the quotient has order 3p²·60^(2p), so its index is 3p·60^p. The original marked image has exactly 3p·60^p elements. Equality contradicts strictness. ∎

The proof is analytic and makes no claim about other local inversion lifts or arbitrary nonnilpotent tops. In particular, the separate p=7 all-local-mark certificate does not automatically generalize to this family.


## Independent review of both extensions

reviewers contributor 1, contributor 3 and contributor 4 independently accepted both added sections and the exact certificate at [the source revision](https://github.com/Mira-Cult/math-wip/commit/c57f9453c30375451eee5cde0e857f3afd12b273), keeping their scopes separate. For the all-local p=7 theorem they checked constant outer parity, actual N-class weights, the outer valuation contradiction, legitimate empty-pattern repointing, the original N-cut and complete necklace coefficient obstruction. For the prime-uniform pure theorem they checked all p-dependent orbit counts, strip capacities, singleton matchings and both original cut cardinalities. None extrapolated the p=7 certificate to arbitrary primes.

All three read and extracted the committed verifier and independently ran it using the bundled Python3.12.14: necklace counts `[1,1,3,5,5,3,1,1]`, 2,304 vectors, no weight divisible by 2^14, and only the optional smooth value 15^7. They retained the upstream folder, local/strip, parity and repointing inputs without independently reproving all of them or making a fresh primary-source audit. These are model mathematical/code reviews, not formal GitHub approvals or human/formal certification.

The almost-simple reviewer explicitly resolved a normalization subtlety: after socle conjugation makes the repointed involution pure on N, the original pure complement Q still lies in the unchanged group G. Since the factor action is faithful and N is centerless, `C_G(N)=1`; an automorphism of G is determined by its action on N. The now-pure involution must therefore carry that original Q to itself. This does not require a simultaneous vanishing theorem for an unrelated nonabelian Q-cocycle. Repointing is used only to preserve simplicity and nonassociativity, not isomorphism or properness.


## Pure-inversion stable 121 + 11 + 11 exclusion

**Independently reviewed continuation of [0323:C0010](../../claims/0010.md), at the corrected source below.** Let $`Q=\mathbb F_{11}^2\rtimes\langle c\rangle`$, with $`c`$ acting by $`(3,4)`$, and let $`\theta`$ swap the two axes and invert $`c`$. Let $`G=A_5^\Omega\rtimes Q`$, where $`\Omega`$ consists of the stable $`121`$-point affine orbit and two exchanged $`11`$-point orbits, and let $`\tau`$ be the pure factor-permutation lift. There is no faithful generated canonical folder of a finite simple nonassociative Bol loop with this $`G,\tau`$. No assertion is made for other lifts, factor actions, or general parameters.

The proof uses the original-folder strict normal-cut theorem C0001 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), the actual selected-class and mark interface C0007 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813), and the stable local, full-strip and marked-square inputs of `radical-free-a5-odd-top-surjectivity.md` at [the source revision](https://github.com/Mira-Cult/math-wip/commit/3b9e8ae5ff1a9c1562d9a8aba4e8eefd80bcdc46). In particular these are applied to the actual folder, without assuming its top image is all of Q or projecting to a new folder.

There are 11 fixed coordinates and 66 exchanged pairs in each selected outside class; the inverted top set has size 55. The cited stable local/parity argument forces every stable-coordinate projection of $`H_0=H\cap A_5^\Omega`$ to be full. Let $`w`$ be the total weight of the selected fixed-mark patterns per inverted top label. Pure $`\tau`$ provides the all-identity pattern. The diagonal fixed subgroup of $`Q`$ rotates the 11 fixed coordinates, so nonconstant binary patterns occur in orbits of size 11 and the all-double pattern has weight $`15^{11}`$. Hence $`w\equiv1`$ or $`16\pmod{11}`$, and $`w\equiv1\pmod{15}`$. Actual class and transversal counts yield

```math
|K|=55\,60^{66}w,\qquad |H|=11\,60^{77}/w.
```

In particular $`11\nmid w`$. As $`w`$ divides $`11\,60^{77}`$ and is coprime to 3, 5, and 11, it is a power of 2. The 11-part of the actual top image $`U=HN/N`$ is exactly 11. The original normal cut by $`N\rtimes\mathbb F_{11}^2`$ forces its image onto $`C_5`$: otherwise the selected image has size equal to the quotient index 5, contrary to strictness. Thus $`|U|=55`$. Its intersection with the translation subgroup is an eigenline; the two choices are exchanged by a $`\tau`$-compatible automorphism. Translate the complement to take $`U`$ as the first axis semidirect $`\langle c\rangle`$. Then the stable U-orbits have sizes 11,55,55; the first paired row is transitive of size 11, and the second has orbits 1,5,5. Also $`|H_0|=60^{77}/(5w)`$.

Use the original full strips and their proper residual subgroup. Two literal singleton full strips cannot occupy the two coordinates of a selected exchanged pair: choose conjugate nonidentity involutions on just those two independent factors to obtain an actual class-square collision. The available selected matchings between the paired rows form a complete bipartite relation. Therefore literal singleton full strips can occur in at most one paired row. The transitive first row cannot consist of singletons, since it would put its entire Q-normal socle factor product into H. Thus there are at most ten paired singletons.

Suppose first that there is no stable singleton. Write $`b`$ for the number of paired full coordinates and $`m`$ for the number of full strips. The residual subgroup, supported on $`22-b`$ proper coordinates, has valuations $`v_3=77-m`$ and $`v_5=76-m`$. Every proper subgroup of $`A_5`$ has at most one of 3 and 5 in its order, each to exponent at most one. Hence

```math
153-2m\le22-b,\qquad e:=121+b-2m\le-10.
```

But $`e=\sum_S(|S|-2)\ge-10`$, because only the at most ten paired singletons contribute negatively. Equality holds: all ten nonfixed coordinates of the second row are singleton strips and every other full strip has size two. The two stable 55-orbits must be paired with one another; the stable 11-orbit pairs with the first paired row. This uses U-invariance, oddness of each transitive orbit, and equality of the sizes of the two orbits joined by an equivariant matching. The remaining second-row fixed coordinate is the only proper coordinate, with residual order $`60/(5w)=12/w`$. Since $`w`$ is a power of 2, the empty pattern is selected, and each additional pattern contributes at least 15, either $`w=1`$ or $`w\ge16`$. The latter is impossible from the residual order; therefore $`w=1`$, and the residual is an order-12 subgroup, hence conjugate to $`A_4`$.

The remaining pairing of the two stable 55-orbits is, in the indicated coordinates, necessarily

```math
(x,b)\longleftrightarrow(x+s/b,db)\quad(b\in\langle3\rangle),
 \qquad s\in\mathbb F_{11},\ d\in-\langle3\rangle.
```

This follows by U-equivariance: the 11-translations force the x-coordinate to differ by a function of b, and the action of c makes that function $`s/b`$; the other orbit is labelled by a fixed multiplier $`d`$. The cross pairing is the natural equivariant one after the chosen complement and coordinates. Internal automorphism twists of the strips are arbitrary.

For any selected top reflection write $`z=3^j`$, $`t\in\mathbb F_{11}`$. On the stable orbit its factor permutation is $`\sigma(a,b)=(t+zb,z^{-1}(a-t))`$. Form a support graph with one vertex per 76 full strips and one for the proper $`A_4`$, an edge for each of the 66 exchanged coordinate pairs, and an anchor for each of the 11 fixed coordinates. There are at least 11 components. If $`s\ne0`$, exactly one of $`s=z(d-1)b^2`$ and $`s=z(1-d)b^2`$ holds for some $`b\in\langle3\rangle`$: squaring permutes this odd-order group, and $`-1`$ exchanges its two cosets. The first equality puts two fixed coordinates on one strip; the second makes an exchanged pair a loop on one strip, forcing at least 12 components. If $`s=0`$, the distinct fixed points $`(t+zb,b)`$, $`(t+zdb,db)`$ lie in strips joined by the exchanged pair $`(t+zb,db)\leftrightarrow(t+zdb,b)`$. In all cases an unanchored component exists.

Give every strip in that component a nonidentity involution, and the proper $`A_4`$ vertex an involution if it is included; put identity on the other vertices. Arbitrary strip twists preserve element order, and all nonidentity involutions of $`A_5`$ lie in one conjugacy class. The actual selected class square therefore contains this nonidentity element: paired coordinates need only have conjugate involutions, not equal ones, and fixed coordinates are identity. It lies in $`H_0`$, contradicting the transversal. This obstruction is independent of all top lifts.

Now suppose a stable literal singleton exists. The reviewed singleton class-square argument forces all selected fixed marks to be identity, so $`w=1`$. A singleton's whole U-orbit consists of singleton strips. For any nonzero $`b`$, the points $`(0,b)`$ and $`((1-3)b,3b)`$ belong to the same 55-orbit and are exchanged by a selected reflection (take $`j=0,t=-3b`$); both singleton factors would yield a collision. Thus the 11-point stable orbit consists of singleton strips, and the other stable orbits contain none.

Let $`m_s`$ count full strips meeting the stable orbit. For the original normal cut killing the paired socle factors, the actual selected image has size $`55\,60^{55}`$, while the quotient index is $`11\,60^{121-m_s}`$. Strictness, together with $`5<60`$, gives $`m_s\ge66`$. Each strip meeting a nonzero-b stable orbit exactly once would have 55 distinct U-translates and consume at least 55 paired coordinates, exceeding 22. Hence all such strips contain at least two stable coordinates, and $`m_s\le11+110/2=66`$. Equality makes every remaining stable-touching strip a pair of stable coordinates. No 55-orbit admits an invariant internal perfect matching; thus those strips pair the two 55-orbits and their 55 translates exhaust them. A paired coordinate cannot occur on any such strip because its distinct translates would consume 55 paired coordinates. Accordingly all stable-touching strips are isolated, and the remaining paired residual subgroup has order $`60^{77-66}/5=60^{11}/5`$, without any independence assumption on that residual.

For the original normal cut killing the stable socle factors, the H-image has order $`55\,60^{11}/5=11\,60^{11}`$, and the quotient index is $`55\,60^{11}`$. The actual selected image has exactly $`55\,60^{11}`$ elements, contradicting strictness. This completes both branches.

As a separate finite control, [the committed support-graph verifier](../code/verify_stable121_support_graph.py) checks the 55 equivariant pairings against all 55 selected reflections and finds an unanchored support component in every case. This computation is not a substitute for the proof or for an independent review.

The project read and ran the finite control under Python3.12.14: all 3,025 graphs had an unanchored component and all 55 arrangements failed all 55 selected reflections. This corroborates the analytic obstruction, not the preceding exhaustion or folder inputs. A precommit scratch audit by contributor 5 found no gap in the full argument under those inputs; it is not an exact-source review.


### Review and repair of the stable121 argument

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/e01de6619af5ace529ef8469a36d4808512f7061), reviewers contributor 1 and contributor 3 requested a correction to the unqualified claim that no full strip can contain both endpoints of a selected pair: additional coordinates, especially fixed anchors, can prevent that purported collision. The proof needs only the valid two-literal-singletons restriction, which now replaces that sentence. They found no further defect in the two-branch argument. contributor 4 accepted the earlier source; that acceptance does not erase the other reviewers' objection. All three extracted and ran the exact committed verifier under Python3.12.14 and obtained 3,025 unanchored graphs. All three subsequently accepted the corrected section at [the source revision](https://github.com/Mira-Cult/math-wip/commit/06ec0cf2cb57e6cc5a6827128d334fc6a2b1c3c2), conditional on the pinned inputs; contributor 4 explicitly acknowledged missing the earlier overclaim.

## Arbitrary odd complement: residual reduction and an index-two exclusion

**Independently reviewed continuation at the exact source below.** Let p≥7 be prime, let m>1 be an odd divisor of p−1, and choose r∈Fp* of order m. Put Q=Fp²⋊⟨c⟩ with c acting by (r,r⁻¹), θ exchanging the axes and inverting c. Let Ω be the stable p²-point affine Q-orbit and the two exchanged p-point orbits, G=A5^Ω⋊Q, and τ the pure factor permutation induced by θ. Retain the faithful generated canonical folder hypotheses of C0001 and the actual inversion/mark interface C0007, pinned above at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45) and [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813), with the stable-local, full-strip and marked-square inputs at [the source revision](https://github.com/Mira-Cult/math-wip/commit/3b9e8ae5ff1a9c1562d9a8aba4e8eefd80bcdc46).

Any such folder of a finite simple nonassociative Bol loop would have the following necessary form. Its stabilizer image is U=Fp⋊C_h for h=5 or 15 dividing m, after τ-compatible coordinates. Every selected fixed mark is identity. The stable p-orbit of U is paired by full strips with the first p-row; the nonzero-b stable U-orbits, each of size hp, are paired with one another by full strips of length two. The other paired row has p−1 full singleton strips and one proper coordinate: A4 if h=5, or V4 if h=15. Strip twists and actual top lifts remain unrestricted by this statement. In particular, if 5 does not divide m, no such folder exists. If additionally [Fp*:⟨r⟩]=2, no such folder exists for any h. This is not a classification of larger-index actions or nonpure inversion lifts.

### Actual top image and weights

Write N=A5^Ω and H0=H∩N. Pure inversion supplies the empty fixed-mark pattern; the stable-local theorem forces every stable-coordinate projection of H0 to be full. Set C=p(p+1)/2 and S=(p²+3p)/2. The actual selected class and transversal counts give

    |K|=mp·60^C w,          |H|=p·60^S/w.

The p fixed coordinates are cycled by C_Q(θ). Nonconstant patterns have orbit length p, and the optional all-double pattern weighs 15^p. Thus w≡1 or 16 mod p and w≡1 mod15. Since w divides p·60^S, it is a power of two. Also either w=1 or w≥16.

The p-part of the actual image U is exactly p. Let h be the order of its image in C_m. The original normal cut by N⋊Fp² gives m>m/h, so h>1; it does not imply h=m. Since U divides |H|, h is {3,5}-smooth. The translation part of U is an eigenline for its nontrivial odd complement, since r^(m/h) and its inverse are distinct. Exchange axes if needed. A diagonal translation centralizing θ adjusts the complement's second coordinate, while the first coordinate is absorbed by the translation line; hence U=P⋊C_h with P the first axis. Put ρ=r^(m/h). Its stable orbits have sizes p and hp; the paired rows have sizes p, and 1 together with h-orbits. Moreover |H0|=60^S/(h w).

### No stable singleton, uniformly in m

Suppose a stable literal singleton strip exists. Its U-orbit consists of singletons, and the reviewed singleton mark criterion gives w=1. For nonzero b, the selected reflection σ(a,b)=(t+b,a−t), t=−ρb, swaps (0,b) and ((1−ρ)b,ρb) within the same nonzero-b U-orbit. Two singleton factors there would give an actual collision. Therefore precisely the stable b=0 orbit can contain singletons, and all its p points are singletons.

Let M_s count full strips meeting the stable set. A remaining strip containing exactly one stable coordinate has hp distinct U-translates and would consume at least hp>2p paired coordinates, impossible. Thus every other such strip has at least two stable coordinates, M_s≤C, and

    Δ:=C−M_s = (1/2) Σ (|strip∩Ωstable|−2),

where the sum omits the p singleton strips. The first-axis translation P acts freely on stable coordinates. If a strip contributes positive excess, it has either p distinct translates, contributing at least p/2 to Δ, or it is P-stable and contains at least p stable points, contributing at least (p−2)/2. Consequently Δ=0 or Δ≥(p−2)/2.

The first original cut, killing the paired socle factors, has selected-image size mp·60^((p²−p)/2). Its quotient index is (m/h)p·60^(p²−M_s); strictness gives h>60^Δ. Since h≤p−1<60^((p−2)/2), Δ=0. Every remaining stable-touching strip has exactly two stable coordinates. Its odd-order U-stabilizer fixes both endpoints individually and is trivial, so it has hp translates; it cannot contain a paired coordinate. Thus all stable-touching strips are isolated from the paired factors. The paired subgroup then has order 60^p/h. In the second original cut, killing the stable factors, the H-image has order ph·60^p/h=p·60^p and the quotient index is mp·60^p, equal to the actual selected-image size. This contradicts strictness. The argument excludes stable singleton strips for every odd m in the stated model.

### All stable strips have length two

Now there are no stable singletons. Let b be the number of full paired coordinates and M the total number of full strips. Put v=v3(h)+v5(h). Each proper A5 subgroup has at most one of the primes 3 and 5, with exponent at most one. The residual capacity gives

    e:=p²+b−2M ≤ v−p.

Only paired singletons contribute negatively to e. The union of selected pairings is complete bipartite across the paired rows, so two such singletons cannot occur in opposite rows. All p points of the transitive first row cannot be singletons, as that would place an entire Q-normal socle product in H. Thus at most p−1 paired singletons occur. The sum of positive excesses |strip|−2 is consequently at most v−1. Also v≤log_3 h≤log_3(p−1).

A strip of length at least three that touches the stable set has either p distinct P-translates, contributing at least p to that positive excess, or is P-stable and contains at least p stable coordinates, contributing at least p−2. Both exceed v−1. Hence every stable-touching strip has exactly two total coordinates. Its odd-order U-stabilizer fixes its endpoints, so the endpoint U-orbits have the same size. The stable p-orbit must therefore pair with the first p-row, and the nonzero-b hp-orbits pair with one another. An odd transitive orbit has no invariant internal perfect matching.

Let a be the number of paired singletons. The inequality e=−a plus nonnegative excess gives a≥p−v, without any assumption about paired-only nonsingleton strips. All a singletons lie on the second row. Since h>v, the at most v nonsingleton coordinates cannot contain a nonfixed U-orbit of size h. Thus its p−1 nonfixed coordinates are all singleton strips. Corefreeness makes its remaining fixed coordinate proper; the first row is already used by the cross strips. In particular no paired-only nonsingleton strip remains.

There are S−1 full strips. The single proper residual coordinate has order 60/(h w). Since h is odd, integrality of the residual order gives w dividing 4; together with w=1 or w≥16, this forces w=1. Now h divides 60 and is odd and greater than one, so h∈{3,5,15}. There is no proper order-20 subgroup of A5, eliminating h=3. The remaining residual is A4 for h=5 and V4 for h=15. It is a genuinely single-coordinate residual, with no assumed independence of an unexamined multi-coordinate subgroup.

### Exclusion when the complement has index two

Suppose [Fp*:⟨r⟩]=2. Put A=⟨ρ⟩. Choose a matched pair of nonzero-b U-orbits, with b-coordinate sets B=b0A and dB, d∉A. U-equivariance forces their strip pairing to have the form

    (x,b) ↔ (x+s/b,db),        b∈B,

for some s∈Fp. Every z∈⟨r⟩ and t∈Fp occurs in an actual selected top reflection σ(a,b)=(t+zb,z⁻¹(a−t)); z is not restricted to A.

Form the full support graph with one vertex per full strip and the proper residual, every selected exchanged pair as an edge, and every selected fixed coordinate as an anchor. It has S vertices, C edges and p anchors, hence at least p components. If s=0, the two distinct fixed points (t+zb,b) and (t+zdb,db) lie in strips joined by the edge (t+zb,db)↔(t+zdb,b), so at most p−1 components are anchored. If s≠0, squaring permutes the odd group A and ±⟨r⟩=Fp*. Hence some z∈⟨r⟩ and b∈B satisfy s=z(d−1)b² or s=z(1−d)b². The first puts two fixed coordinates on one strip. The second puts an exchanged pair on one strip, a loop edge, forcing at least p+1 components. In every case some component has no anchor.

Give each strip in that component a nonidentity involution, and give the actual A4 or V4 residual an involution if its vertex belongs to the component. Set all other vertices to identity. Arbitrary strip twists preserve involution order, and all nonidentity involutions of A5 are conjugate. The resulting nonidentity H0-element lies in the square of the actual selected class: paired coordinates have conjugate involutions and fixed coordinates are identity. This contradicts the original transversal and proves the index-two exclusion.

The proof is analytic. contributor 5 audited the scratch arguments, identifying and helping repair the composite-complement surjectivity, capacity-sign and paired-only-strip issues before this source was added. This is not an exact-source review. The general larger-index h=5 or15 support graph, actual top lifts and nonpure inversion remain unresolved. For example, at p=31,m=5 the local two-anchor/self-loop test can fail for a chosen pair of orbits; that does not supply a global graph survivor or a loop.


### Independent review of the arbitrary-complement theorem

contributor 1, contributor 3 and contributor 4 independently accepted the complete arbitrary-complement section at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/06ec0cf2cb57e6cc5a6827128d334fc6a2b1c3c2). They checked the actual h|m top image without surjectivity, both translation-orbit excess arguments, the paired-only-strip repair, the h=5/A4 and h=15/V4 residual conclusion, and the index-two graph obstruction using the full set of selected labels. The same reviews separately accepted the repaired stable121 section. No new computation or primary-source audit was claimed; the original-folder, stable-local, full-strip and class-square inputs remain pinned dependencies. These are independent model reviews, not formal GitHub approvals or human/formal certification.

## Two finite larger-index exclusions

**Computation-assisted corollary with the scoped independent reviews below.** In the same pure-inversion model, there is no faithful generated canonical folder of a finite simple nonassociative Bol loop for m=5 and p=31 or41. The preceding reviewed reduction forces h=5 and exactly the cross strips, paired singleton coordinates and one A4 residual described there. It remains only to exclude every equivariant matching of the nonzero stable U-orbits.

The standalone [C++17 verifier](../code/verify_stable_prime_support.cpp) derives the order-five multiplicative subgroup and its six or eight nonzero cosets. It recursively pairs the least unpaired coset with every other available coset. For each pair, choosing the image of one representative gives all five multipliers d, and s ranges over all of Fp in (x,b)↔(x+s/b,db). Thus it covers every U-equivariant matching; no Q-invariance of that matching is assumed.

The verifier uses the coordinate graph before collapsing strip edges. The actual pure reflection supplies (x,b)↔(b,x) and pairs the two outer rows; the forced cross strips supply (x,0)↔first-row x. A diagonal stable coordinate is an anchor and a second-row coordinate is a terminal leaf (including the A4 residual). Every vertex in the completed graph has degree at most two. A collision-free completion would be exactly p paths with one anchor and one leaf each. A cycle gives an unanchored component. A path joining two leaves is already an unanchored component; a path joining two anchors makes the p anchors cover at most p−1 of the at least p components. These paths have their terminal degrees exhausted, so adding remaining matching edges cannot repair them. The rollback union-find rejects precisely these three irreversible defects and restores all changed component data on backtracking.

The project read the source, compiled it with Apple clang17.0.0 (clang-1700.6.3.2), C++17 and optimization O3, and ran both fixed inputs. It found zero surviving complete matchings. The diagnostic node counts by depth were (1,100,85,0) for p31 and (1,390,30205,8570,0) for p41. An independent precommit scratch audit by contributor 5 checked enumeration and pruning and reproduced the earlier two-instance programs; it is not an exact-source review of this consolidated verifier. The analytic class-square interface, including arbitrary strip twists and the actual A4 residual, turns every unanchored component into a nonidentity H0 collision. This yields the stated finite corollary conditional on the verifier and pinned reduction, not an all-prime theorem.


### Independent review of the finite controls

contributor 1, contributor 3 and contributor 4 independently accepted the finite corollary and exact consolidated verifier at source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8aa8130e5f07aa490f3d32a0fa8692c9e5bdd266). Each extracted the committed C++ source, compiled it with `c++ -std=c++17 -O3 -Wall -Wextra -pedantic`, and ran it successfully on both built-in inputs. All reproduced the node counts above and zero completions. They checked complete coset-pair/multiplier/shift enumeration, initialization, rollback and the irreversible cycle/two-anchor/two-leaf pruning, together with the conditional support-to-collision argument. They retained the pinned geometric and original-class inputs and did not infer a result for other primes, audit fresh external sources, or provide formal GitHub approvals.
