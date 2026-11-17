# A local-factor obstruction for elementary Bruck radicals

**Mira Cult**

**Theorem with scoped independent reviews below, conditional on the cited inputs.** This continues [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md), without a new permanent ID. Work in the faithful canonical envelope $`(G,H,K)`$ of a finite simple nonassociative right Bruck loop of 2-power exponent, with elementary $`V=O_2(G)`$. Use the quotient, stabilizer, inversion, marked-invariance and singleton-fiber inputs of Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5, as scoped in [the product constraints](bruck-elementary-product-constraints.md) at input revision [the source revision](https://github.com/Mira-Cult/math-wip/commit/b88cd1d25a469cc06277febc9f20725ed68934f4). Let $`\pi:G\to A=\prod_j A_j`$, where $`A_j=\mathop{\mathrm{PGL}}\nolimits_2(q_j)`$ are the allowed factors, and $`\pi(H)=\prod_j B_j`$ with $`B_j`$ the projective point Borel. Write $`W=H\cap V`$. Choose one factor $`A_i`$, put $`q=q_i`$, and let $`t\in A_i`$ be a prescribed nonsplit outer involution, $`T=\langle t\rangle`$, $`R\le C_{A_i}(t)`$ an odd subgroup. Regard $`A_i`$ as its singleton-support subgroup of $`A`$.

Assume the following conditions on the restriction of the actual $`A`$-module $`V`$ to $`A_i`$:

1. $`H^1(A_i,V)=H^2(A_i,V)=0`$.
2. $`V|_{B_i}`$ is semisimple and projective, and $`V^{B_i}=0`$.
3. One fixed odd prime $`p`$ divides the size of every nonzero $`R`$-orbit in $`H^1(T,V)`$.

Then no envelope with these properties exists, subject to the cited source inputs. This is a local-factor conclusion: no complement of $`V`$ in all of $`G`$ is assumed or constructed, and no condition on the other factors is required. The module hypotheses are not asserted for arbitrary mixtures of nonprincipal isotypes. The odd group $`R`$ may act trivially if $`H^1(T,V)=0`$; condition 3 is then vacuous.

## Local complement and inversion

Set $`G_i=\pi^{-1}(A_i)`$ and $`H_i=H\cap\pi^{-1}(B_i)`$, where $`B_i`$ also denotes its singleton-support embedding. The restriction $`\pi:H\to\prod_j B_j`$ is onto, so $`H_i\to B_i`$ is onto and its kernel is exactly $`W`$. The $`B_i`$-module $`W\le V`$ is a submodule. Since $`V|_{B_i}`$ is semisimple projective, both $`W`$ and $`V/W`$ are projective $`B_i`$-modules.

The local extension $`1\to V\to G_i\to A_i\to1`$ splits by $`H^2(A_i,V)=0`$. In the quotient of $`\pi^{-1}(B_i)`$ by $`W`$, the image $`H_i/W`$ is a complement to $`V/W`$. Its class in $`H^1(B_i,V/W)`$ is zero because $`V/W`$ is projective, hence $`V/W`$-conjugacy adjusts a chosen local $`A_i`$-complement to one whose $`B_i`$-part lies in $`H_i`$. Consequently, with this local complement identified with $`A_i`$,

```math
G_i=V\rtimes A_i,\qquad H_i=W\rtimes B_i.\tag{1}
```

The conjugating vector belongs to $`V`$; this makes no assertion about a complement for the whole product.

The canonical inversion automorphism $`\tau`$ fixes the elementary radical $`V`$ pointwise and induces the identity on $`A`$, by the source interfaces. In particular it preserves $`G_i`$. Relative to (1), its difference on $`A_i`$ is a derivation $`\delta_i:A_i\to V`$, and $`\delta_i|_{B_i}=0`$ because $`\tau`$ fixes $`H`$ pointwise. Since $`H^1(A_i,V)=0`$, $`\delta_i(a)=(1+a)v`$ for some $`v\in V`$. Its vanishing on $`B_i`$ means $`v\in V^{B_i}=0`$, so $`\tau|_{G_i}=1`$. No conclusion about $`\tau`$ outside $`G_i`$ follows.

The marked set $`\widehat\tau K`$ is invariant under conjugation by $`G`$. For $`g\in G_i`$, $`\tau(g)=g`$; hence this marked invariance gives $`gKg^{-1}=K`$. Thus $`K`$ is invariant under ordinary conjugation by $`G_i`$, even though $`\tau`$ need not be globally trivial.

## Singleton fiber and collision

Let $`K_t=\{k\in K:\pi(k)=t\}`$, with $`t`$ at the chosen singleton support and identity elsewhere. The source singleton-fiber formula makes $`K_t`$ nonempty of positive 2-power cardinality with expression $`|V:W|\,2/(q-1)`$ for this singleton support. Every $`k\in K_t`$ belongs to $`G_i`$, and $`\tau|_{G_i}=1`$ together with $`\tau(k)=k^{-1}`$ makes it an involution. Write $`k=xt`$, $`x\in V`$. Then $`(1+t)x=0`$, and conjugation by $`V`$ changes $`x`$ by $`(1+t)V`$. The resulting label is

```math
[x]\in H^1(T,V)=\ker(1+t)/(1+t)V.
```


The pure subgroup $`R\le A_i\le G_i`$ centralizes $`t`$, preserves $`K_t`$ by the preceding invariance, and acts equivariantly on labels. Within any $`R`$-orbit of labels, all selected label fibers have equal size. If no label were zero, condition 3 would make $`|K_t|`$ divisible by the odd prime $`p`$, impossible. Thus zero occurs; conjugating that element by a suitable vector of $`V`$ gives the pure element $`t\in K`$.

Ordinary $`G_i`$-conjugacy invariance now puts the entire pure $`A_i`$-conjugacy class of $`t`$ into $`K`$. Its elements are nonsplit outer involutions and fix no point of the projective line. The class has $`q(q-1)/2`$ elements, because its centralizer is the dihedral normalizer of the nonsplit torus, of order $`2(q+1)`$. None belongs to the point stabilizer $`B_i`$. There are only $`q`$ other $`B_i`$-cosets in $`A_i`$, but $`q(q-1)/2>q`$ for $`q\ge5`$. Two distinct elements $`t_1,t_2`$ of that pure class therefore lie in the same $`B_i`$-coset. By (1) their quotient is a nonidentity element of $`B_i\le H_i\le H`$, whereas both lie in $`K`$. This contradicts the folder transversal property.

The proof has the scoped exact-revision reviews below. The representation inputs for a nonprincipal binary isotype are discussed in [the uniform core manuscript](bruck-central-frattini-all-quotients.md), but the present statement assumes conditions 1–3 and does not establish them for a given radical. In particular, neither global splitting nor triviality of global $`\tau`$ is assumed or derived.

## Nonprincipal block descent and Borel restriction

Let k=F2, let G be finite, and let b be a primitive block idempotent of kG. Suppose that over an algebraic closure K, b splits into one Galois orbit of blocks and that each resulting block has defect group C2. Then b has one simple kG-module F, and every finite b-module is a direct sum of copies of F and its projective cover P(F). Moreover P(F) has length two with both composition factors F. There is no extra twisted form.

Proof. The absolute block theorem of Hiss–Lassueur, arXiv:1908.07833v2, §4.6, printed p.12, gives one simple S_i in each absolute block and exactly two indecomposables S_i and P(S_i), with the latter uniserial of length two. Primitive rational block idempotents form precisely Galois orbits of absolute block idempotents. As the field is finite, simple modules descend by ordinary finite-field Galois descent (equivalently Wedderburn's theorem and separability); hence the single orbit of absolute simples corresponds to one simple F. Let E=End_{kG}(F), a finite field, and let e be a primitive idempotent giving the projective cover. The basic corner algebra C=e(kG b)e is local with residue field E. Scalar extension is faithfully flat and commutes with radicals over the perfect field k; its radical has square zero, since every absolute basic block is the two-dimensional algebra K[ε]/(ε²). Thus J(C)^2=0 and dim_E J(C)=1 on either side.

The separable residue field E embeds in C (Wedderburn–Malcev). The E-E bimodule J(C) is invertible of rank one and therefore has the form _1 E_σ for a k-automorphism σ of E. On scalar extension to K, the primitive idempotents corresponding to embeddings E→K have arrows determined by σ. But each absolute block is local, so all arrows are loops; consequently σ=1. A nonzero x in J(C) commutes with E, x²=0, and C≅E[x]/(x²). The left ideal (kG b)e is a projective generator because there is only one simple module, and its endomorphism algebra is opposite to C. The projective-generator form of Morita equivalence therefore reduces the finite b-modules to finite-dimensional E-spaces with a square-zero E-linear operator; choosing a Jordan basis gives exactly the 1- and 2-dimensional blocks. They correspond to F and P(F), respectively. This argument also establishes the length-two statement over k, without assuming absolute indecomposability of F or P(F).

Now let G=A=PGL₂(q), q≥5 odd with q−1 a power of 2, and B=N⋊C with N=(F_q,+) and C=F_q^×. Suppose b is one nonprincipal binary block whose absolute simple modules have the degree-(q−1) cuspidal character restriction recorded in the central-Frattini manuscript. For each such absolute simple S, all nonidentity elements of N have ordinary and Brauer character −1, so dim S^N=(q−1+(q−1)(−1))/q=0. Therefore F^N=0; N-invariants are exact because |N| is odd, and consequently P(F)^N=0 too, using its two F composition factors.

The complement C acts regularly on the q−1 nontrivial linear characters of N over K. Clifford theory (or diagonalizing N and using the transitive C-action) gives a unique simple KB-module with nontrivial N-action, of dimension q−1, induced from any nontrivial N-character; its restriction to C is regular, so it is projective. Its unique binary form E_B is the augmentation submodule of kN with the affine B-action, and has dimension q−1. Indeed after extension to K its N-weights are exactly the q−1 nontrivial characters once, hence it is absolutely simple. Any finite kB-module with zero N-invariants belongs to this single defect-zero block and is semisimple, a direct sum of copies of E_B. Thus every finite b-module restricts to B as E_B^n. In particular if [End_A(F):F2]=f then F|B≅E_B^f and P(F)|B≅E_B^{2f}.

Dependencies and scope: uses the previously established ordinary/ Brauer character matching and defect-C2 assertion for the chosen nonprincipal absolute blocks; the latter uses the covering-block result whose original Alperin source is not independently accessed. Standard finite-dimensional algebra facts used above are separable Wedderburn–Malcev, Morita equivalence and scalar-extension behavior of radicals and primitive blocks. This block lemma makes no claim about the principal block; its application to mixed nonprincipal blocks follows in the next section.

The algebraic source interfaces are [Baranov–Mudrov–Shlaka, arXiv:1609.05812v2](https://arxiv.org/pdf/1609.05812v2), Theorem 1(1), p.1 (Wedderburn–Malcev for a separable quotient); [Eberly, 1989 thesis](https://cspages.ucalgary.ca/~eberly/Research/Papers/phdthesis.pdf), Proposition 2.3.19 and Theorem 2.3.20(ii), printed p.76 (radicals under algebraic extension of a perfect field); and [Boltje–Yılmaz, arXiv:2102.13149v2](https://arxiv.org/pdf/2102.13149v2), §2.4–2.5, printed p.4, and Proposition 4.1(a,b), printed p.6 (finite-field module descent and block-idempotent Galois orbits for arbitrary finite groups). Source auditor contributor 1 directly checked these statements. Eberly's original Curtis–Reiner §69 input and the original Alperin covering-block theorem were not accessed. The projective-generator form of Morita's theorem remains an explicit standard external input; a finite-field textbook page was not directly verified. This source check is separate from independent review of the new application.

## Consequences for elementary-radical block support

Fix a quotient factor A_i and decompose the restricted radical V as an F₂A_i-module. Suppose it has no summand from the principal block. The preceding block lemma expresses V as a direct sum of nonprincipal simples F_j and their projective covers. For each binary simple F_j let d_j>1 be the order of its associated nontrivial character of R=C_{(q_i+1)/2}, as identified in [the uniform module theorem](bruck-central-frattini-all-quotients.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/1d5ea37a268b08d90bb345825c5f36e2366bed4c). This order is unchanged by Frobenius conjugacy and inversion. Retain only the F_j occurring as nonprojective direct summands; projective covers have zero H¹(T,−).

All nonprincipal simple summands have zero H¹ and H² for A_i, by their projective restriction to PSL₂(q_i) with no fixed vectors; projective covers also have zero positive cohomology. The Borel restriction is semisimple projective with no fixed vectors by the preceding lemma. Thus conditions 1–2 hold. If no nonprojective summands occur, H¹(T,V)=0 and condition 3 is vacuous. Otherwise each nonzero cohomology label has R-orbit length equal to the least common multiple of the d_j for its nonzero coordinates. If the d_j share one odd prime divisor, condition 3 holds. The local-factor theorem therefore gives the necessary condition:

> For every factor A_i whose restricted radical has no principal-block summand, nonprojective simple summands must occur and the greatest common divisor of their character orders d_j must be one.

In particular, restriction to one nonprincipal block is impossible, with arbitrary multiplicities and projective summands. If (q_i+1)/2 is a prime power, restriction to A_i must have a principal-block summand. This applies to q_i=5,9,17, where those torus orders are 3,5,9. At q_i=257 the torus order is 129=3·43; a radical with no principal-block component would require nonprojective summands of both character orders 3 and 43 (order 129 alone or combined with only one of them has gcd greater than one). These are necessary module restrictions, not a claim that the remaining mixed blocks yield loops.

For a single quotient and V=F^n with F any nonprincipal binary simple, the result recovers the pure-isotype exclusion for all n≥1. The q=5 N-only special case was previously reviewed in [the S₅ block argument](bruck-s5-module-blocks.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499). The new proof requires neither an assumed split envelope nor exponent two; local splitting and local triviality of inversion are derived. It says nothing about non-elementary radicals. No computation establishes these uniform deductions; the local-factor, descent and block-support arguments have the independent reviews below.

## Independent review

reviewers contributor 2 and contributor 3 independently accepted the local-factor obstruction, finite-field block descent, Borel restriction and stated support consequences at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/16b4ee26345dbc03b2e6ec64599bf766d885cbd4), conditional on the cited Bruck-envelope and uniform representation interfaces and standard algebra inputs. Both checked the local complement, normalization of the actual H_i, local inversion derivation, original singleton fiber and pure-class collision. Both checked the absence of extra finite-field block forms and the common-divisor consequences for q=5,9,17,257. Reviewer contributor 2 directly inspected the cited Wedderburn–Malcev, cyclic-defect, radical and descent sources; the original Alperin text and a specific finite-field Morita textbook locator remain unaccessed as disclosed.

Reviewer contributor 4 separately accepted the finite-field block descent and Borel-restriction section at the same revision, checking the primitive corner, radical base change, untwisted bimodule, Morita step and Borel character orbit. That narrower review excludes the folder argument and later support conclusions. No new computation or formal verification was used. All three reviews retain the elementary-radical scope and do not construct any residual mixed-block envelope.
