# 0109. A nilpotent transitive action on a whole simple socle power must be a 2-group

**Mira Cult**

When the socle of a left multiplication group is a product of isomorphic simple groups, conjugation can permute the factors. Nilpotence alone permits many odd-order permutations. For a simple proper left Bol loop, the actual left translations place a stronger restriction on this action.

**Theorem.** Let $`G`$ be the faithful left multiplication group of a finite simple non-Moufang left Bol loop, $`H`$ the stabilizer of the identity, and suppose the **whole** socle of $`G`$ is $`S=T^\Omega`$ with $`T`$ nonabelian simple and $`n=|\Omega|\ge2`$. If the permutation group $`C`$ induced by $`G`$ on the factors is nilpotent and transitive, then **$`C`$ is a 2-group and $`n`$ is a power of two**. Write $`U_i`$ for the projection of $`H\cap S`$ on the $`i`$th factor. No $`N_{T_i}(U_i)`$ can factor $`T_i`$ with an automorphic conjugate. There is a selected signed involution permuting none of the factors, and a different one exchanging all factors in pairs. Neither a regular factor action nor surjectivity of $`H\to G/S`$ is required.

## Why two different kinds of marked involution must occur

In the canonical signed extension the marked involutions are the original left translations multiplied by the distinguished inversion $`t`$. They form a conjugacy-invariant set $`\Lambda`$ with $`H\cap\Lambda^2=\{1\}`$. The [whole-socle projection theorem](0105-nilpotent-socle-stabilizer-projections.md) gives $`H\to C`$ and $`1<U_i<T_i`$. Local coordinates can therefore identify the $`U_i`$ through actual stabilizer elements. For the common model $`U<T`$, distinguish its conjugacy class under $`T`$ from the other inner classes of its automorphic images. These classes are the local **colors**.

The signed translations carry the orbit of the tuple $`(U,\ldots,U)`$ uniformly onto its signed image. The source and target may be different sets. Even in that case, the true incidence matrix between a chosen pair of color-pattern fibers is a positive multiple of the all-ones matrix. If the two local colors at every site have more than one orbit of ordered pairs under their joint stabilizer, one can build a separate centered relation on each pair of colors. Its transpose may have **negative** sign. Using the appropriate sign in a product of these relations makes every exchanged coordinate pair contribute zero. The positive constant on the uniform side implies that an actual selected mark in the specified block exchanges no sites. This gives such a mark for **each** eligible target pattern, not one mark covering all patterns.

A flat color pair, meaning the joint color stabilizer is transitive on the Cartesian product, is the only way to evade that conclusion. Flatness gives a full almost-simple factorization. A theorem of Baddeley and Praeger descends this to the inner simple group; intersection with a normal subgroup does not justify the descent by itself. The inner factors are isomorphic normalizers. The homogeneous factorization classification leaves the four pairs

```math
(A_6,A_5),\quad(M_{12},M_{11}),\quad
(\operatorname{Sp}_4(2^f),\operatorname{PSL}_2(2^{2f}))\ (f\ge2),\quad
(\operatorname{P}\Omega_8^+(q),\Omega_7(q)),
```

where the second entry is the socle of the normalizer and is understood projectively. The [rectangular incidence proof](../sources/factor-permutation/rectangular-stabilizer-incidence.md) gives the construction in both orientations and the precise classification inputs.

In each of the four actual embeddings, an automorphism-invariant class in the smaller simple group is carried into one inverse-closed, automorphism-invariant class in $`T`$. This forces the perfect residual of $`H\cap S`$ to be a single diagonal strip: otherwise suitable coordinates on a strip component produce an actual nonidentity product of two selected marks in $`H`$. The product is taken in the ambient socle, **not** in a smaller product assumed normal. A strict count at degree three, and a stronger count above three, then rule out that remaining strip as well. The [local class and count proof](../sources/factor-permutation/homogeneous-normalizer-endpoints.md) identifies all four embeddings, including the characteristic-two orthogonal case and its triality transports.

Every target pattern therefore admits a coordinate-unpermuted mark. It follows that the $`G`$- and signed-extension coordinate images agree. Conjugation by $`t`$ is inner on $`C`$, but it induces inversion on its abelianization, so the abelianization has exponent at most two. Each nontrivial odd Sylow factor of a finite nilpotent group has a nontrivial abelian quotient. Thus $`C`$ is a 2-group. Finally, if every mark fixed some coordinate, its image would lie in a conjugate of one point stabilizer. A normal maximal subgroup containing that proper stabilizer would contain all those conjugates, and hence all translation images. Those translations generate $`C`$, a contradiction. At least one mark exchanges every coordinate.

## What remains

This theorem restricts the **permutation group**, not the simple factors to characteristic two. It neither constructs nor classifies the remaining transitive 2-group actions, and it says nothing general about nonnilpotent actions or an arbitrary smaller normal layer. For the separate complete exclusions of [even-field projective-line socles](0106-nilpotent-transitive-even-field-psl2.md) and [simple types with odd outer automorphism group](0107-odd-outer-nilpotent-socles.md), see the indicated manuscripts. The two proof stages above received separate, revision-pinned independent AI mathematical reviews. The [evidence and executable checks](../normal-layer-evidence.md#nilpotent-transitive-actions-and-homogeneous-factorizations) distinguish their scopes from human review, formal verification and a loop census.
