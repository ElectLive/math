# 0031. Simple Bol loops with unbounded factor-permutation cycles

**Mira Cult**

## Results obtained

A classification of finite simple Bol loops cannot assume that their left multiplication groups fix every simple socle factor. We construct simple non-Moufang loops whose faithful left multiplication groups have trivial solvable radical and permute their simple factors in cycles of arbitrarily large prime length. The first concrete example has order **648000** and socle A₅⁶.

The mechanism is an exact factorization of a cyclic wreath product, with a character coupling its base coordinates to its permutation coordinate. This coupling ensures simplicity even though the canonical action is imprimitive. It supplies a construction family, not an isomorphism classification or an exhaustion of all factor-permuting groups.

## 1. Construction theorem and imported interfaces

Let T be a finite nonabelian simple group with an exact factorization T=AB, where A,B are nontrivial, A∩B=1, and χ:A→C_p is onto for a prime p. There is a finite simple proper left Bol loop of order p|T|^p whose entire faithful canonical left multiplication group has socle T^(2p), trivial solvable radical, and quotient C_p acting as two cycles of length p on the simple factors. Such cycle lengths are unbounded, as shown below.

We use the exact-factorization folder construction in [the canonical criterion](../advances-2026-11-16/manuscripts/exact-factorization-criterion.md), reviewed at `e3a39be22fe1390d3717bdeee8f81d82f6817aef`, and the faithful generated-folder, exact normal-subloop criterion and simple-Moufang LMlt primitivity input [C0001](../claims/0001.md), reviewed at `9431ade99316d6bc62efb389492fef385b510b45` (Lemma 1.2 for primitivity). These are the stated loop-theoretic inputs; all group calculations needed for this new construction are given here. No identification with the full multiplication group is used.

## 2. A coupled factorization of a cyclic wreath group

Let S=T^p⋊⟨σ⟩, with σ rotating the p coordinates, and write top:S→C_p for its quotient map. Define

 Y₀=B^p⋊⟨σ⟩,
 Y₁={(a₁,…,a_p)σ^k : a_i∈A, Σχ(a_i)=k in C_p}.

The sum of the χ-values is rotation-invariant. Hence Y₁ is the kernel of the onto homomorphism A^p⋊C_p→C_p given by (a,σ^k)↦Σχ(a_i)−k. Consequently |Y₀|=p|B|^p and |Y₁|=|A|^p. Their intersection is trivial: all base coordinates lie in A∩B, so they are identity and the Y₁ condition forces k=0. Their orders multiply to |S|, giving S=Y₀Y₁ exactly. Both factors map onto C_p, since σ∈Y₀ and (a,1,…,1)σ∈Y₁ when χ(a)=1.

Every nontrivial normal subgroup of S contains T^p. Indeed, its intersection with T^p is a product of simple coordinate factors invariant under the transitive rotation, so is either 1 or T^p. In the first case it centralizes T^p, whose centralizer in S is trivial. Neither Y_i contains T^p; thus both are core-free. Also S′=T^p, since T^p is perfect and S/T^p is abelian.

## 3. The faithful left multiplication group

Put

 K={(x,x⁻¹):x∈S},
 G=⟨K⟩={(x,y)∈S²:top(x)+top(y)=0},
 H=G∩(Y₀×Y₁),  τ(x,y)=(y,x).

To verify that G is exactly the generated group rather than an ambient envelope, write k(x)=(x,x⁻¹). The product k(x)k(y)k(xy)⁻¹ has first coordinate 1 and second coordinate x⁻¹y⁻¹xy. Coordinate swapping preserves K, so ⟨K⟩ contains S′×S′. Its top images generate the anti-diagonal C_p. The exact-factorization construction makes K a Bol transversal to H and all its conjugates. The action is faithful: any normal subgroup of G inside H projects to normal subgroups of S contained in Y₀,Y₁, hence is trivial by their core-freeness. Thus G is the canonical left multiplication group, rather than an ambient envelope. The orders are |G|=p|T|^(2p), |K|=p|T|^p and |H|=|T|^p.

Write N₁=T^p×1, N₂=1×T^p and N=N₁N₂. The top quotient rotates the two p-tuples in opposite directions. Each N_i is a minimal normal subgroup of G, and C_G(N)=1. For M normal in G, M∩N is a product of coordinate simple factors and is G-invariant, hence is 1,N₁,N₂ or N. If it is 1 then M centralizes N and is trivial. If it is N₁, then [M,N₂]=1 and C_G(N₂)=N₁, so M=N₁; the other case is symmetric. If it contains N, the prime quotient G/N=C_p gives M=N or G. Therefore the full normal-subgroup list is

 1, N₁, N₂, N, G.

In particular Soc(G)=N and the solvable radical is trivial.

## 4. Simplicity and the non-Moufang condition

For the three nontrivial proper normal subgroups, the original-folder normal-subloop criterion gives the following strict inequalities:

 |KN₁/N₁|=|S| > [G:HN₁]=|S:Y₁|=p|B|^p,
 |KN₂/N₂|=|S| > [G:HN₂]=|S:Y₀|=|A|^p,
 |KN/N|=p > [G:HN]=1.

The first two hold because K projects bijectively onto the surviving copy of S, and H projects onto each Y_i because both Y_i cover C_p. The third uses that K and H both cover C_p. These are actual projected-set counts, not assumptions that the projections are folders. The criterion proves simplicity. Since H is nontrivial, the canonical action is not regular. A group acting by its own left translations has trivial identity stabilizer, so the loop is nonassociative.

There is a strict intermediate subgroup

 H < M=G∩[Y₀×(A^p⋊⟨σ⟩)] < G.

The first index is p, because Y₁ has index p in A^p⋊C_p and both cover the top quotient; the second inclusion is strict since Y₀<S. Thus the canonical left multiplication action is imprimitive. The cited simple-nonassociative-Moufang primitivity input excludes the Moufang case. This proves the construction under the stated loop-theoretic interfaces.

## 5. Examples and unbounded cycle lengths

Take T=A₅, A=A₄, B=C₅ and χ:A₄→A₄/V₄=C₃. The construction gives a loop of order 3·60³=648000, with |Y₀|=375, |Y₁|=1728, Soc(G)=A₅⁶ and top quotient C₃. Thus nontrivial factor permutation is already required over an A₅ socle.

For unbounded lengths, take q=3^f with f an odd prime, and choose any prime p dividing (q−1)/2. This integer is odd and greater than one. The order of 3 modulo p divides f but is not one, since an odd prime does not divide 3−1. Hence ord_p(3)=f, so f divides p−1 and p≥2f+1. As odd primes f are unbounded, so are these p.

Let T=PSL₂(q), A a Borel subgroup, and B a nonsplit torus normalizer. Since q≡3 mod4, their orders q(q−1)/2 and q+1 are coprime and multiply to |T|, giving T=AB exactly. These subgroups and their structure are the inputs in [the reviewed all-field paired table](../update-2026-11-16/manuscripts/radical-free-psl2-path-classification.md#all-field-paired-psl-assembly) at `e30af949531c0ebcc9f7533b04fc1e7fc6858563`; its source locators retain their stated qualifications. The Borel quotient C_((q−1)/2) surjects onto C_p. Thus the construction realizes unbounded prime cycle lengths without any additional prime-distribution theorem. It supplies an infinite construction family, not exhaustion of factor-permuting canonical groups.


## 6. Source dependencies and proof scope

This exposition reorganizes the [source construction](../advances-2026-11-16/manuscripts/radical-free-factor-permutation-construction.md), pinned at source revision `ad7b7d0df9910463839b2e8607fbfec3ddbe2f5e`. The original argument records scoped mathematical checks conditional on the imported exact-factorization, faithful-folder, normal-quotient, subgroup and Moufang-primitivity inputs. Their exact source revisions appear in §1 and §5. These provenance records do not certify later changes or establish literature priority.

All group calculations for this construction are given here. The loop-theoretic interfaces and the PSL₂ subgroup facts remain imported dependencies; this manuscript does not reprove their full source classifications. It is a research proof draft, not a human-refereed or formally verified theorem.

## 7. What remains

The result rules out any general reduction that bounds permutation-cycle lengths in the simple socle. It does not classify all permutation tops or all possible stabilizers, nor does it determine when two input factorizations give isomorphic loops. Those are substantive steps toward the [factor-permuting classification problem](../OPEN_PROBLEMS.md). A complete classification must incorporate these examples rather than discard the factor-permuting branch.
