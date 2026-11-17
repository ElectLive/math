# Structural parameters for elementary S₅ Bruck envelopes

**Mira Cult**

**Effective parameterization with two scoped independent reviews below, conditional on the cited inputs.** This continues [C0010](../../claims/0010.md) for the following restricted endpoint: classify up to loop isomorphism faithful Baer envelopes of finite simple exponent-2 right Bruck loops whose radical $`V=O_2(G)`$ is elementary abelian and whose quotient is $`S_5`$. Under those inputs, the data and tests below give soundness, exhaustiveness and a two-way isomorphism criterion for that endpoint. They are effective finite constructions at fixed parameters, not a numerical census; no parameter is asserted to admit a solution. They do not classify other radical types, other quotients, or all finite Bol loops. No permanent claim ID is allocated.

Write $`F\cong F_{20}`$ for a fixed point stabilizer in $`S_5\cong PGL_2(5)`$, and $`T`$ for an $`F`$-invariant complement to the socle in $`U=N\otimes\mathbb F_2C_2`$. We use Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1(b), Lemmas 4.1 and 4.5, for $`\pi(H)=F`$, the section image and fiber counts. The N-block and $`H^2(S_5,U)=0`$ are in [bruck-s5-module-blocks.md](bruck-s5-module-blocks.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499); the linear support and N-multiplicity bounds are in [bruck-s5-uniform-principal-support.md](bruck-s5-uniform-principal-support.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/32b5918c4b3fa3b2686185006b80d41b1ece76aa). The active stabilizer normal form is [bruck-s5-active-u-stabilizer.md](bruck-s5-active-u-stabilizer.md), source [the source revision](https://github.com/Mira-Cult/math-wip/commit/7ee728cc65fcaa28ffac8850185d0fdfe9a8bc48); its review record and the new deductions below must be checked at their exact revisions. The simplicity criterion used below is [C0001, Theorem 2.2](../foundations/C0001.md), transported to right folders.

## Active group and stabilizer parameters

Choose $`m\ge1`$, the number of principal $`M`$-composition factors, an integer $`s\ge0`$, and a finite $`S_5`$-module


```math
V=V_a\oplus U^s,
```


where $`V_a=X\oplus N^a\oplus U^{b_0}`$, $`X`$ has exactly $`m`$ composition factors $`M`$ and all remaining factors trivial, $`\dim X\le328m`$, $`0\le a\le110m+1`$, and $`0\le b_0\le111m+1`$. The reviewed N-block obstruction requires $`m\ge1`$ for any envelope in the target. Thus $`V_a`$ contains the principal block, all $`N`$-summands and the active $`U`$-summands, and one may restrict the search to


```math
\dim V_a\le328m+4(110m+1)+8(111m+1)=1656m+12.
```


The active bound applies at fixed $`m`$; $`m`$ and $`s`$ are not bounded. A standard finite module-presentation or matrix construction, followed by intertwiner checks, supplies $`V_a`$; no precomputed list of isomorphism types is assumed.

Choose $`W_a\le V_a`$ invariant under $`F`$, set $`W=W_a\oplus T^s`$, and impose that $`W`$ contain no nonzero $`S_5`$-submodule. This is exactly core-freeness for a stabilizer mapping onto $`F`$, since the core of $`F`$ in $`S_5`$ is trivial. Also impose


```math
W+[V,A_5]=V.                                                   \tag{1}
```


Condition (1) is necessary by the reviewed invariant-functional obstruction. Indeed $`W+[V,S_5]=V`$; in $`B=V/[V,A_5]`$, the action factors through sign. If $`\epsilon=t-1`$, then $`\epsilon^2=0`$. The $`F`$-stable image $`\bar W`$ satisfies $`\bar W+\epsilon B=B`$; applying $`\epsilon`$ gives $`\epsilon B\subseteq\bar W`$, hence $`\bar W=B`$.

Choose an extension class $`e_a\in H^2(S_5,V_a)`$, construct the corresponding finite extension $`E`$, and choose a subgroup $`H_a\le E`$ mapping onto $`F`$ with $`H_a\cap V_a=W_a`$. Equivalently, after quotienting the preimage of $`F`$ by $`W_a`$, the image of $`e_a|_F`$ in $`H^2(F,V_a/W_a)`$ must vanish, and $`H_a/W_a`$ is a complement. Complements up to $`V_a`$-conjugacy form a torsor for $`H^1(F,V_a/W_a)`$; retaining these choices avoids assuming uniqueness.

Set $`G=E\ltimes U^s`$, with action through $`S_5`$, and $`H=H_a\ltimes T^s`$. Every envelope in the stated scope admits this form: the active normal form first splits the radical module; $`H^2(S_5,U^s)=0`$ splits that component of the group extension. For a given $`H`$, projection to $`E`$ gives $`H_a\cap V_a=W_a`$. The graph cocycle of $`H`$ modulo $`T^s`$ factors through $`F`$, and $`H^1(F,U^s/T^s)=0`$ because this quotient is projective. Conjugation by $`U^s`$ makes the graph zero. This is a group and stabilizer reduction, not a quotient-loop or product assertion.

## Outer classes and radical section

Choose an $`E`$-conjugacy-invariant set $`\Omega_a`$ of involutions above the transposition class, and require


```math
\Omega_a\Omega_a^{-1}\cap H_a=\{1\},\qquad
 |\Omega_a\cap\pi^{-1}(t)|=2^{\dim V_a-\dim W_a-1}              \tag{2}
```


for a transposition $`t`$. The first condition is pairwise collision-freeness, not an assertion that $`\Omega_a`$ alone is a transversal. It also applies to every conjugate of $`H_a`$, since $`\Omega_a`$ is conjugacy-invariant. The second number must be an integer; conjugacy makes it independent of the chosen $`t`$.

Let $`\Omega`$ be the involutions in $`G`$ projecting to $`\Omega_a`$. For $`t`$ a transposition, $`U^s|_{\langle t\rangle}`$ is free, so $`C_{U^s}(t)=(1+t)U^s`$. Every involution above an active one is therefore $`U^s`$-conjugate to its zero lift, and projection gives a bijection of the relevant outer conjugacy classes. Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.3(i), gives $`T\cap C_U(t)=0`$; $`F`$ is transitive on transpositions. Either $`F`$-complement has this property, since the two complements are interchanged by the $`S_5`$-module automorphism $`1+\epsilon`$. Thus (2)'s active collision test is equivalent to $`\Omega\Omega^{-1}\cap H=\{1\}`$: an active collision lifts using zero coordinates; conversely, if projected elements coincide, their difference lies in $`T^s\cap C_{U^s}(t)=0`$. The full $`t`$-fiber has $`2^{4s}`$ times the active size.

Choose a union $`D`$ of $`S_5`$-orbits on all of $`V`$, containing $`0`$, that is a transversal to $`W`$. Explicitly, for each orbit $`O\subseteq V`$ choose a binary variable $`x_O`$, require $`x_{\{0\}}=1`$, and impose for every coset $`v+W`$


```math
\sum_O |O\cap(v+W)|x_O=1.                                     \tag{3}
```


Set $`K=D\cup\Omega`$. The section $`D`$ may couple active and inactive coordinates; no product or projection condition on $`D`$ is assumed. Radical–radical collisions are excluded by (3); outer–outer collisions by (2); mixed products project to transpositions, absent from every conjugate of $`F`$. The sizes are


```math
|D|=2^{\dim V-\dim W},\quad
 |\Omega\cap\pi^{-1}(t)|=2^{\dim V-\dim W-1},\quad
 |K|=6\cdot2^{\dim V-\dim W}=[G:H].
```


Thus $`K`$ is a transversal to $`H`$ and all its conjugates, is conjugacy-invariant and consists of the identity and involutions. It defines an exponent-2 Bruck folder. **Separately require** $`\langle K\rangle=G`$, checked in the finite extension: the collision and cardinality conditions alone do not establish generation. Together with core-freeness, this makes the folder the faithful Baer envelope of its loop.

Generation also has a linear-span test. Choose one selected involution lift $`k_i`$ of each of the four adjacent-transposition Coxeter generators $`s_i`$ of $`S_5`$, and fix a word $`w_t(s_i)`$ for each transposition $`t`$. Let $`A_K\le V`$ be the $`S_5`$-submodule generated by $`D`$, by the vectors $`k\,w_t(k_i)^{-1}`$ for all $`k\in K_t`$, and by the residues in $`V`$ of the Coxeter relators $`k_i^2`$, $`(k_ik_j)^2`$ for $`|i-j|>1`$, and $`(k_ik_{i+1})^3`$. All these vectors lie in $`\langle K\rangle`$, as do their conjugates by the selected lifts. Conversely, modulo $`A_K`$, the selected lifts satisfy the presentation of $`S_5`$ and generate the image of $`K`$, so their generated group maps isomorphically onto $`S_5`$. Hence $`A_K=\langle K\rangle\cap V`$, and generation is equivalent to $`A_K=V`$. This test uses the actual selected fibers and does not require them to be saturated over $`V`$.

## Simplicity test

For each nonzero $`S_5`$-submodule $`S\le V`$, including $`S=V`$, define $`K_t=\Omega\cap\pi^{-1}(t)`$. Require the following quantities to be unequal:


```math
|(D+S)/S|+10\,|(K_t+S)/S|
 \ne 6\cdot2^{\dim V-\dim(W+S)}.                              \tag{4}
```


The left side is $`|KS/S|`$: the radical and ten outer images are disjoint in the $`S_5`$-quotient, and $`F`$ acts transitively on transpositions. The right side is $`[G:HS]`$. By the cited normal-subloop criterion, equality is precisely the transversal condition needed for $`S`$ to give a loop quotient. Core-freeness makes $`S\not\subseteq W`$, so its kernel is nontrivial; $`\pi(HS)=F`$ makes the quotient proper.

No other normal subgroup need be tested. If $`R\lhd G`$ has nontrivial image in $`S_5`$, that image contains $`A_5`$. Then $`[V,R]\supseteq[V,A_5]`$, and (1) gives $`V\subseteq HR`$. Since $`\pi(HR)=FA_5=S_5`$, one has $`HR=G`$. The exact normal-subloop criterion therefore reduces simplicity to the finite linear-submodule and cardinality tests (4). This uses (1), and is not an inference from the quotient image alone.

## Isomorphism and completeness

For two admissible data, write their full extension cocycles as $`f,f'`$ after choosing normalized sections. A loop isomorphism induces an isomorphism of Baer envelopes. Every automorphism of $`S_5`$ is inner, and an automorphism carrying $`F`$ to itself is conjugation by an element of $`N_{S_5}(F)=F`$. Composing with an inner automorphism from the target stabilizer reduces the quotient map to the identity without changing its $`H`$ or conjugacy-invariant $`K`$.

The resulting envelope isomorphism is exactly a pair consisting of an $`S_5`$-module isomorphism $`\alpha:V\to V'`$ and a normalized 1-cochain $`u:S_5\to V'`$ satisfying


```math
\alpha f+f'=\delta u,                                         \tag{5}
```


with the induced group isomorphism carrying $`H`$ to $`H'`$ and $`K`$ to $`K'`$. Conversely every such pair induces a loop isomorphism. The module map is allowed to mix the chosen active and inactive $`U`$-coordinates; neither the active normal form nor a particular cocycle representative is declared canonical. The cochain and exact $`H,K`$ conditions retain all complement and section choices.

For fixed $`m,s`$, the active modules, group extensions and stabilizer choices are finite; (2) is a finite class calculation, (3) a finite orbit exact-cover problem on the full $`V`$, (4) a finite submodule/cardinality test, and (5) finite linear cohomology and group-action tests. Thus the displayed criteria give the effective construction and equivalence relation under the stated inputs and scoped reviews. Their cost still depends on $`s`$ through the full radical orbit and submodule problems; no scalability bound for those computations, finite list across all $`m,s`$, or exhaustive solution of the larger Bol-loop problem is asserted.

## Independent reviews

reviewer contributor 1 accepted this parameterization at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/b7e884bf04800a357b549026bdb58529f547ef85), conditional on the cited source and prior reviewed inputs. The review checked active dimensions, extension splitting and stabilizer normalization, outer-class and collision equivalence, the full-variable identity-containing radical cover, independent generation and its Coxeter-span test, the Nakayama argument eliminating normal subgroups outside V, all radical-submodule quotient tests including S=V, and both directions of the full-module/cochain isomorphism criterion.

A second reviewer, contributor 2, independently accepted the same exact source under the stated inputs. This critical review found no soundness, exhaustiveness or isomorphism gap and judged the fixed-group module/cohomology/orbit data to give structural effective enumeration rather than arbitrary loop-table enumeration. It explicitly did not accept an efficiency or global-scalability claim: m and s are unbounded, and D and the submodule searches still use the full V. Neither reviewer reran or reproved all upstream work, supplied formal verification, proved nonemptiness for all parameters, or classified other radicals, quotients or all Bol loops.

## Proposed extension to all elementary S₅ Bruck envelopes

**Scoped independent reviews below; the exponent-2 theorem and reviews above are unchanged.** This section proposes to extend the preceding effective parameterization to faithful Baer envelopes of all finite simple right Bruck loops with elementary abelian $`V=O_2(G)`$ and $`G/V\cong S_5`$. The exponent may be 2 or 4. It remains restricted to that radical and quotient and makes no assertion that every parameter admits a solution, that $`m`$ or $`s`$ is bounded, or that the radical section decomposes across active and inactive coordinates.

The input [bruck-s5-elementary-inversion.md](bruck-s5-elementary-inversion.md) at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/343e1daba1ff08c869fd4a2b8a9bb318c873bf17) was independently accepted by contributor 3 and contributor 4 under its stated prior inputs. In particular, it supplies the canonical inversion automorphism $`\tau`$, the relative derivation $`\delta:S_5\to V`$ with $`\delta|_F=0`$, the exponent-at-most-4 conclusion, the invariant-functional obstruction, and the carryover of the support and active-stabilizer bounds. That review does not accept the new parameterization below.

### Data changed from the exponent-2 construction

Use the same choices of $`m,s,V=V_a\oplus U^s,W=W_a\oplus T^s,E,H_a`$, the active dimension bound $`\dim V_a\le1656m+12`$, the group $`G=E\ltimes U^s`$, and $`H=H_a\ltimes T^s`$ as above, with $`m\ge1`$. Retain core-freeness of $`W`$, condition (1), and the complement/cohomology choices for $`H_a`$. The active decomposition is only a normal form: it is not canonical and imposes no product condition on the loop or on its radical section.

Let $`E_6=\ker(\mathbb F_2[S_5/F]\to\mathbf1)=J^*`$. Choose an $`S_5`$-module map $`f:E_6\to V_a`$ with image in the principal block, and set


```math
\delta(g)=f(gF+F).
```


The inversion input proves that all relevant relative derivations arise this way and have no $`N`$- or $`U`$-block component. On $`G`$, define $`\tau(g)=\delta(\pi(g))g`$; it fixes $`V`$ and $`H`$ pointwise, and $`\tau^2=1`$. Work in the formal semidirect products $`E^+=E\rtimes\langle\hat\tau\rangle`$ and $`G^+=G\rtimes\langle\hat\tau\rangle`$, with an external element $`\hat\tau`$ of order 2 acting by $`\tau`$, including when $`\tau=1`$.

Replace the ordinary outer class choice by an $`E^+`$-conjugacy-invariant union $`\Lambda_a`$ of involutions in $`\hat\tau E`$ above transpositions. Put $`\Omega_a=\hat\tau\Lambda_a\subseteq E`$, and impose the same active collision and fiber-size tests as (2), now on $`\Omega_a`$. In particular $`\Omega_a`$ need not be ordinarily conjugacy-invariant. Lift $`\Lambda_a`$ to the full union $`\Lambda_{\rm outer}`$ of involutions in $`\hat\tau G`$ projecting to it, and set $`K_{\rm outer}=\hat\tau\Lambda_{\rm outer}`$.

Replace the linear radical orbit cover (3) by an affine orbit cover. The action is


```math
x\cdot d=xd+\delta(x)\qquad(x\in S_5,\ d\in V).
```


Choose a union $`D`$ of its orbits, containing $`0`$, and require that $`D`$ be a transversal to $`W`$. Equivalently use (3) with **affine** orbits and set the variable for the entire orbit of 0 to 1. In particular $`\delta(S_5)\subseteq D`$. This exact cover is on the full $`V`$; $`D`$ can couple active and inactive coordinates.

Define $`\Lambda=\hat\tau D\cup\Lambda_{\rm outer}`$ and $`K=\hat\tau\Lambda=D\cup K_{\rm outer}`$. Retain the separate generation and simplicity tests from above. In the Coxeter-span generation test the selected lifts $`k_i`$ can have order 4: their squares $`k_i^2`$ remain required relator residues, as do all the other Coxeter residues. In the simplicity test, $`K_t`$ means the actual selected fiber, and **every** nonzero $`S_5`$-submodule $`S\le V`$, including $`S=V`$, is tested by (4); no quotient loop by a particular block is assumed.

### Sufficiency and necessity of the changed section conditions

Because $`\tau`$ fixes $`V`$, the conjugation action of $`G`$ on $`\hat\tau V`$ is precisely the displayed affine action. Thus $`\hat\tau D`$ is $`G^+`$-invariant. The bulk $`U^s`$-part of $`\delta`$ is zero, and the module $`U^s`$ restricts freely to any transposition subgroup. Consequently, for each active involution in $`\Lambda_a`$, the bulk involution lifts form $`C_{U^s}(t)=(1+t)U^s`$, one $`U^s`$-conjugacy orbit. Hence $`\Lambda_{\rm outer}`$, and therefore $`\Lambda`$, is $`G^+`$-invariant. It contains $`\hat\tau`$ because $`0\in D`$, and all its elements are involutions.

For $`k\in K`$, $`(\hat\tau k)^2=1`$ gives $`\tau(k)=k^{-1}`$. Invariance of $`\Lambda`$ under $`\hat\tau`$ gives $`K^{-1}=K`$, and its invariance under $`K`$ gives $`k_1k_2k_1\in K`$. Since $`\tau`$ fixes $`H`$, invariance under $`H`$ gives $`H`$-conjugacy invariance of $`K`$. Thus the section has the Bol and Bruck compatibility; the induced inverse is an automorphism because $`\tau`$ acts as inversion and fixes $`H`$.

The active outer collision equivalence is the same projection argument as above: an active collision has zero-bulk lifts, while, if the projections coincide, two bulk involution lifts differ by an element of $`T^s\cap C_{U^s}(t)=0`$. The two $`F`$-complements of the socle in $`U`$ have this property by Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.3(i), and the $`1+\epsilon`$ module automorphism. Radical–radical collisions are excluded by the affine exact cover; mixed products project to transpositions, which lie in no conjugate of $`F`$.

Although $`K`$ need not be $`G`$-conjugacy-invariant, $`KK^{-1}=\hat\tau(\Lambda\Lambda^{-1})\hat\tau`$ is $`G`$-conjugacy-invariant. Thus collision-freeness against $`H`$ holds against every conjugate of $`H`$. The radical cover has size $`2^{\dim V-\dim W}`$; the ten outer fibers each have half that size; hence $`|K|=6\cdot2^{\dim V-\dim W}=[G:H]`$. Therefore $`K`$ is a transversal to every $`H`$-conjugate. With the independent generation and core-freeness tests it is the faithful Baer section of the constructed Bruck loop; the cited normal-subloop criterion and all tests (4) give simplicity exactly as above.

Conversely, in every envelope in this section's scope the inversion input gives $`\delta`$, its vanishing bulk part, and the active stabilizer normal form. The $`U^s`$ group extension and bulk stabilizer graph split by the same $`H^2(S_5,U^s)=0`$ and $`H^1(F,U^s/T^s)=0`$ arguments as above. The marked set $`\hat\tau K`$ is conjugacy-invariant and consists of involutions; its radical part is an affine-orbit union and its outer part is a union of full bulk lifts. The source fiber count, transversality, generation and simplicity supply all the stated tests. Thus the proposed data are exhaustive under the cited inputs.

### Isomorphism and limitations

Use the full-module/cochain criterion (5), allowing module isomorphisms to mix active and inactive coordinates, and add


```math
\alpha\delta=\delta'.
```


This compatibility is necessary because every loop isomorphism transports its canonical inversion; it is sufficient alongside the extension-cocycle equation and exact $`H,K`$ preservation. As above, target-$`H`$ conjugation normalizes the quotient automorphism, and the cochain retains all complement choices. The condition $`\delta=0`$ recovers the exponent-2 case; if $`\delta\ne0`$, generation ensures some section element has order 4.

At fixed $`m,s`$, the active module, extension, stabilizer and marked-class choices are finite, followed by finite affine-orbit exact-cover, generation, submodule/cardinality and cochain-equivalence tests on the full $`V`$. Their cost can grow with $`s`$. This is a proposed structural parameterization of the stated elementary-$`S_5`$ class, not a numerical census or a classification of all Bruck or Bol loops. The new section has the scoped independent reviews below.

### Independent reviews of the general-exponent extension

reviewers contributor 1 and contributor 2 independently accepted this appended extension at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/e2e4609612cf6de99be9d2456c339b18d4a04173), conditional on the separately reviewed inversion result at [the source revision](https://github.com/Mira-Cult/math-wip/commit/343e1daba1ff08c869fd4a2b8a9bb318c873bf17) and the cited exponent-two, module, support and folder inputs. Both checked marked involution classes and affine radical orbits, bulk saturation and collision equivalence, twisted closure and all-conjugate transversality, generation with order-four lifts, the all-submodule simplicity test, and the derivation-compatible full-module/cochain isomorphism criterion. The result is effective structural enumeration at fixed parameters only; the reviews do not bound m or s, prove efficiency or nonemptiness for all parameters, or classify other radicals or quotients. No new computation or formal verification was supplied.
