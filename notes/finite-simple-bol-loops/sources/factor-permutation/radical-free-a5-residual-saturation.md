# Character saturation on a transitive A4 residual orbit

Mira Cult

**Independently reviewed theorem under pinned inputs.** This continues [classification frontier](../../claims/0010.md). Let G=A5^Ω⋊Q with Q finite odd nilpotent acting by pure factor permutations, and let H map onto Q. Put H0=H∩A5^Ω and use the original Goursat decomposition H0=T×R into full twisted A5 strips and the correlated residual R on proper coordinates. Let I be a single Q-orbit of proper coordinates such that every actual H0-projection on I is A4. Put d_I=dim_F3 C, where C is the image of R in (A4/V4)^I. The action of Q on I is transitive. The decomposition and its preservation by actual H are [the orbit-tensor source](radical-free-a5-orbit-tensors.md); the A5 subgroup facts are pinned in [the A5 path source](radical-free-a5-path-classification.md). The module argument below is supplied here, with no independence assumption on R.

Assume |I|>1 and let ℓ be the least prime divisor of |I|. (For |I|=1 the projected V4 conclusion is immediate.) If d_I>|I|/ℓ, then the image of O₂(R′) in V4^I is the full product V4^I. In particular v₂(|R|)≥2|I|. The conclusion concerns a projection: it does NOT imply that the coordinate subgroup V4^I is contained in R. Couplings to A4 coordinates outside I may be diagonal and must be retained.

For the proof, write χ_i:C→F3 for the nonzero coordinate characters. The equivalence relation χ_i=±χ_j has Q-invariant blocks, because actual H normalizes R and permutes the factors. Transitivity makes all blocks equally sized. If any block has size b>1, b is an odd divisor of |I| and b≥ℓ. There are |I|/b projective character classes, so the characters span C* in dimension at most |I|/b≤|I|/ℓ. Therefore the stated inequality forces the projective characters pairwise distinct.

The derived subgroup R′ projects onto [A4,A4]=V4 at each coordinate of I. In each proper A5 coordinate, the derived subgroup is an abelian group of order 1, 3, 4 or 5; hence R′ embeds in a product of abelian p-groups, is abelian, and its Sylow-2 subgroup O₂(R′) projects onto V4 in every I-coordinate. The I-projection of this subgroup is a C-stable F2-submodule of V4^I. Its coordinate modules are the two-dimensional irreducibles indexed by the projective characters χ_i; distinct projective characters give pairwise nonisomorphic constituents. Maschke's theorem separates them, and coordinatewise surjectivity forces the full product as image. Nothing in this argument separates possible isomorphic constituents in coordinates outside I, which is why containment is not concluded.

There is a general budget bound for d_I. Let m be the number of full strips and let b be the number of all OTHER proper coordinates of R whose actual local projection has order divisible by 3. Project R to ALL other proper coordinates. The image has 3-part at most 3^b, including the coordinates not counted by b whose orders are prime to 3. The kernel embeds in A4^I, and its 3-part is at most 3^{d_I} because the quotient by V4^I maps into C. Hence

    d_I ≥ v₃(|H0|)−m−b.                                       (1)

When H comes from a canonical folder as in [the full-strip matching source](radical-free-a5-full-strip-matching.md), independently reviewed, write n=|Ω|, let f be the number of fixed factors of a selected outside involution, k the number of outside top labels, and D their common actual fixed-mark weight. Then v₃(|H0|)=(n+f)/2−v₃(kD), and (1) is the exact lower bound in these parameters. If it exceeds |I|/ℓ, the full projected V4 statement follows. Under that rank hypothesis the global 2-budget is

    v₂(|R|)=n+f−v₂(D)−2m ≥ 2|I|.                               (2)

Inequality (2) is a necessary consequence, not a collision: outside coordinates of O₂(R′) may be tied to I by isomorphic characters, and its full projection alone does not yield an involution supported only on I. For a p-group top, ℓ=p. For a general odd nilpotent top the least prime divisor formulation is the safe bound. No independence of proper residual projections is assumed, and no claim is made for I with H0_i=V4 rather than A4.

## Evidence and remaining obligation

This is an analytic proof with no computation. Independent review of the complete exact source is recorded below. The [four regular-orbit exclusion](radical-free-a5-four-regular-orbits.md) in this source revision is one application. The next obligation is to force the shadow-rank threshold, or obtain a replacement lower bound, for general mixed orbit and strip patterns. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, and an automated checker independently accepted both complete companion sources at exact revision the recorded source revision, conditional on their pinned canonical-folder, actual marked-class, A5 subgroup/strip and local-moment inputs. They checked transitive projective-character blocks, the abelian derived residual and Maschke argument, the all-other-coordinate shadow-rank budget, and the fact that saturation asserts a full projection rather than supported coordinate containment. For the specified four-regular-orbit application they checked the actual local A4 stabilizers and double marks, the correlated E and strict 2-part deficit, the forced 5-bearing proper orbit, and the abelian/nonabelian shadow-rank estimates, including d>n/3≥n/ℓ. These are analytic model mathematical reviews, with no new computation or upstream source audit and no human or formal certification or GitHub approval. The exclusion remains limited to the displayed orbit and strip pattern.
