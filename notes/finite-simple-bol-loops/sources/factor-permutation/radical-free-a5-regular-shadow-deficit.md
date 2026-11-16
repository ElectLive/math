# A global shadow-deficit obstruction for regular factor orbits

Mira Cult

**Independently reviewed analytic obstruction under pinned inputs.** This continues [classification frontier](../../claims/0010.md). Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=N=A5^Ω and G=N⋊Q. Assume the [actual marked-square and strip-splitting interfaces](radical-free-a5-full-strip-matching.md), and the [stable-proper local theorem](radical-free-a5-stable-orbit-local.md). The actual joint-shadow and supported-kernel interface is [the residual-kernel source](radical-free-a5-residual-kernels-cuts.md). Assume Q is finite odd nilpotent of order n>1 and acts by pure factor permutations, regularly on every Q-orbit of socle coordinates. There may be any number of stable or paired orbits and any pattern of original full strips. No proper-coordinate projection type is assumed in advance.

Put H0=T×R, where T is the product of the original full strips and R is the correlated proper-coordinate residual. Let A be all proper coordinates whose projection of H0 is A4, set a=|A|, and let W≤F3^A be the image of R in ∏_{i∈A}(A4/V4). Write d=dim W and h=a−d. Let ℓ be the least prime divisor of n. If

    h < n−n/ℓ,                                                (1)

then all the projective coordinate characters {±χ_i} of W for i∈A are globally distinct. Consequently both of the following are necessary:

  (i) there is no τ-stable proper-projection Q-orbit; and
  (ii) v₂(|R|)≥2a.

Thus either a τ-stable proper orbit, or v₂(|R|)<2a, excludes the original folder under (1). The criterion places no restriction on the other proper projection types and does not assume that R is a product.

For a completely numerical sufficient condition, let b be the number of proper coordinates outside A whose projection has order divisible by 3. Then

    h ≤ a+b−v₃(|R|).                                          (2)

Hence a+b−v₃(|R|)<n−n/ℓ implies (1). To prove (2), map R to the product of W and its actual projections outside A at the b indicated coordinates. Every proper subgroup of A5 has 3-part at most 3. The kernel has trivial 3-part: on A it is contained in V4^A, and at all coordinates outside A it has 3-free image. Therefore v₃(|R|)≤d+b.

Proof of global distinctness. H normalizes H0, hence R, and H0 induces the identity on W, so Q acts on W and its projective characters. The map from coordinates in any regular Q-orbit in A to their projective characters is Q-equivariant. If two characters on one such orbit coincide, equality classes are cosets of a nontrivial subgroup and have a common size at least ℓ. At most n/ℓ distinct characters then occur in that orbit, so the total number of distinct projective characters throughout A is at most a−n+n/ℓ. If instead each orbit has pairwise distinct characters but two characters from different orbits coincide, equivariance implies that all n characters of those two regular orbits coincide as sets. Thus the total number of distinct characters is at most a−n. In either case d is no larger than the number of distinct classes, contradicting (1).

For (ii), U=O₂(R′) is elementary abelian, supported on A, and projects onto V4 at every coordinate in A. Indeed the derived subgroup of every proper A5 subgroup is abelian, and only A4 has an even-order derived subgroup. The W-module U is semisimple, and its coordinate modules are pairwise nonisomorphic irreducible F2-modules of dimension 2, one for each of the now-distinct projective characters. Its surjections to these a modules force dim U≥2a and v₂(|R|)≥2a.

For (i), let I be a τ-stable proper Q-orbit. Its Q-action is regular, so the actual factor stabilizer H_i equals H0. The pinned local theorem gives H0 projection A4 at all i∈I and makes every selected fixed mark there a double transposition. Thus I⊂A and all of its n characters are private to I. By semisimplicity, the sum of their isotypic components in U is an actual subgroup U_I supported only on I, of dimension at least 2n. For any actual selected N-class C, its involutory factor permutation σ preserves I and has f>0 fixed coordinates there, all active. Every term in the actual-class-square parity expansion on U_I imposes at most (n−f)/2 zero-coordinate conditions, each of codimension at most 2, hence total codimension at most n−f. Every term is even, while the identity has matched support. A nonidentity matched-support element of U_I therefore lies in H0∩C², contradiction.

For an illustration with n=3 and a=6, if v₃(|R|)=5 and b=0, (2) gives h≤1<2, so all six characters are distinct. If v₂(|R|)=10, (ii) immediately contradicts the necessary value at least 12. These are only numerical data; no folder is constructed.

Scope: this is a conditional necessary criterion for arbitrary collections of regular Q-orbits, not an unconditional exclusion of every stable-full orbit. A stable-full-only configuration can evade it whenever the deficit bound fails and its 2-budget is sufficient. It does not follow from an assumed quotient folder or require that a particular four-orbit pattern appear.

## Evidence and remaining obligation

This is an analytic proof with no computation; independent review of the complete exact source is recorded below. The next obligation is to force the displayed deficit condition from actual cut and full-strip constraints, or to control configurations with repeated projective character classes when that condition fails. No permanent claim ID is allocated; C0010 and the unrestricted classification remain partial.


## Recorded source review scope

Automated source reviewers an automated checker, an automated checker, and an automated checker independently accepted the complete source at exact revision the recorded source revision, conditional on its pinned original-folder, marked-square, local-stable and supported-kernel inputs. They checked the actual Q-action on the joint shadow, both within-row and cross-row character coincidences, the dimension versus distinct-class count, the numerical 3-part budget for arbitrary other proper types, and the semisimple actual Sylow-2 and stable-proper supported-kernel consequences. No new computation or upstream-source audit was performed. These are independent model mathematical reviews, not human or formal certification or GitHub approval. The explicit deficit condition is not proved universally.
