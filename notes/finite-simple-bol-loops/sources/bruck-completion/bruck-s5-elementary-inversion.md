# Inversion and linear support for elementary S₅ Bruck envelopes

**Mira Cult**

**Scoped independent reviews recorded below, conditional on the cited inputs.** Let $`X`$ be a finite simple right Bruck loop with faithful Baer envelope $`(G,H,K)`$, elementary abelian radical $`V=O_2(G)`$, and $`G/V\cong S_5`$. Then the proposed deductions below show that $`X`$ has exponent at most 4, its canonical inversion automorphism fixes $`V`$ pointwise, and its departure from exponent 2 is encoded by a relative derivation. They extend the cited support and stabilizer bounds to this exponent-at-most-4 setting. They do **not** assert that $`X`$ is exponent 2, isotopic to an exponent-2 loop, or classified by the existing exponent-2 parameterization. This continues [C0010](../../claims/0010.md) without allocating a new claim ID.

## Source input and inversion

Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2, 3.4, 4.1 and 4.2, give the following in this setting. The loop has 2-power exponent; $`\pi(H)=F\cong F_{20}`$, where $`\pi:G\to S_5`$; $`\pi(K)`$ lies in the identity and transposition class; each $`k\in K`$ satisfies $`k^2\in V`$; and


```math
V=(V\cap H)(V\cap K).                                       \tag{1}
```


The canonical inversion automorphism $`\tau\in\mathop{\mathrm{Aut}}\nolimits(G)`$ fixes $`H`$ pointwise and sends every $`k\in K`$ to $`k^{-1}`$. It satisfies $`\tau^2=1`$ because $`K`$ generates $`G`$. Since $`V`$ is elementary abelian, it fixes $`V\cap K`$, and it fixes $`V\cap H`$; equation (1) gives $`\tau|_V=1`$. Every element of $`\pi(K)`$ is an involution or the identity, so $`\tau`$ also fixes the generating image $`\pi(K)`$ pointwise. Thus $`\tau`$ acts trivially on $`G/V`$. Moreover $`k^2\in V`$ gives $`k^4=1`$, so the loop exponent divides 4.

For a uniform convention, let $`G^+=G\rtimes\langle\hat\tau\rangle`$ with a **formal external** element $`\hat\tau`$ of order 2 acting as $`\tau`$, even when $`\tau=1`$. Then $`V^+=V\times\langle\hat\tau\rangle`$ is elementary abelian and normal, and $`G^+/V^+\cong S_5`$. Since $`O_2(S_5)=1`$, $`O_2(G^+)=V^+`$. This formal convention is distinguished from an internal permutation-group realization, which may identify the acting automorphism with an element already present in $`G`$.

## Relative derivations and affine radical sections

Use additive notation for $`V`$ and let $`S_5`$ act by conjugation. Define


```math
\delta(gV)=\tau(g)g^{-1}\in V.
```


This is well-defined because $`\tau`$ fixes $`V`$, and is a left derivation: $`\delta(xy)=\delta(x)+x\delta(y)`$. It vanishes on $`F`$, since $`H`$ maps onto $`F`$ and $`\tau`$ fixes $`H`$. For $`k\in K`$, $`\tau(k)=k^{-1}`$ and $`k^4=1`$ give


```math
k^2=\delta(\pi(k)).                                           \tag{2}
```


Thus all section elements above the same transposition have the same square. The loop has exponent 2 exactly when $`\delta=0`$: if its section consists of involutions then $`\tau`$ fixes the generating set $`K`$; the converse follows from (2). Conversely any derivation $`\delta:S_5\to V`$ vanishing on $`F`$ defines an involutory automorphism $`g\mapsto\delta(\pi(g))g`$ fixing $`V`$ and $`H`$. This remains valid for nonsplit extensions, but does not by itself supply a compatible section.

Let $`P_6=\mathbb F_2[S_5/F]`$ and let $`E=\ker(P_6\to\mathbf1)`$, the even six-point module $`J^*`$. There is a natural isomorphism


```math
\{\delta\in Z^1(S_5,V):\delta|_F=0\}
 \cong\mathop{\mathrm{Hom}}\nolimits_{S_5}(E,V).                            \tag{3}
```


Given $`\delta`$, the linear map $`gF\mapsto\delta(g)`$ on $`P_6`$ is well-defined, and its restriction to $`E`$ is equivariant because the extra derivation term cancels on even sums. Conversely $`f:E\to V`$ gives $`\delta_f(g)=f(gF+F)`$. The maps are inverse. The submodule lattice $`0<\mathbf1<E`$ and $`E/\mathbf1\cong M`$ are recorded in [bruck-s5-principal-one-m.md](bruck-s5-principal-one-m.md#inputs-and-the-six-point-module), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9). In particular $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(E,\mathbf1)=0`$, and each nonzero map in (3) has image isomorphic to $`M`$ or $`E`$.

Let $`D=K\cap V`$ and $`\Lambda=\hat\tau K\subseteq G^+`$. The same source, Lemma 3.2(2), makes $`\Lambda`$ $`G`$-invariant; its elements are involutions. Because $`\tau`$ fixes $`V`$, conjugation on $`\hat\tau V`$ is the affine action


```math
d\longmapsto x d+\delta(x),\qquad x\in S_5.
```


Hence $`D`$ is a union of affine orbits, not necessarily linear $`S_5`$-orbits. Since $`0\in D`$, the affine orbit $`\delta(S_5)`$ is contained in $`D`$. If $`\delta\ne0`$, its zero set is a subgroup containing the maximal subgroup $`F`$, hence is $`F`$; this forced orbit has size 6.

## Invariant functionals beyond exponent 2

Let $`W=H\cap V`$. We propose that the restriction map


```math
\mathop{\mathrm{Hom}}\nolimits_{S_5}(V,\mathbf1)\longrightarrow
 \mathop{\mathrm{Hom}}\nolimits_{F}(W,\mathbf1)                             \tag{4}
```


is injective also when the loop has exponent 4. Suppose a nonzero invariant functional $`\lambda`$ vanishes on $`W`$, and put $`L=\ker\lambda`$. Since $`\lambda\circ f:E\to\mathbf1`$ is zero by (3) and $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(E,\mathbf1)=0`$, one has $`\lambda\delta=0`$. Equivalently, invariance makes $`\lambda\delta:S_5\to\mathbb F_2`$ a homomorphism; it vanishes on F, which contains odd permutations, so it is zero. The quotient $`G/L`$ is a central $`C_2`$-extension of $`S_5`$, and $`H/W`$ complements its kernel above $`F`$. By (2), a section element above a transposition becomes an involution in $`G/L`$. These two restrictions jointly detect $`H^2(S_5,\mathbf1)`$, so $`G/L`$ splits. The detection, including the spin class with an order-eight lift of a generator of $`C_4\le F`$, is recorded in [bruck-s5-principal-envelope-bound.md](bruck-s5-principal-envelope-bound.md#proposed-invariant-functional-obstruction), independently reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6a563df3804682acb6bd4191fff2ac749cb0bd16) and citing Nagy Lemma 3.1.

A projection $`G/L\to C_2`$, adjusted by the sign character if needed, vanishes on the image of $`H`$ and remains nonzero on $`V/L`$. Because $`K`$ generates $`G`$, it induces a nontrivial loop homomorphism to $`C_2`$. The loop order is at least 6 because $`[S_5:F]=6`$, so this gives a proper nontrivial normal subloop, contradicting simplicity. This proves the proposed injectivity of (4), subject to review; it does not assume $`K`$ is a union of conjugacy classes in $`G`$.

## Capacity and uniform support

Write $`d=\dim V`$, $`w=\dim W`$, and $`r=\mathop{\mathrm{rank}}\nolimits(1+t|V)`$ for a transposition $`t`$. The cited Lemma 4.5 gives $`|K\cap\pi^{-1}(t)|=2^{d-w-1}`$. The set $`K`$ is invariant under conjugation by $`V`$: $`\hat\tau K`$ is $`G`$-invariant and $`\hat\tau`$ centralizes $`V`$. Each $`V`$-conjugacy orbit in this fiber has size $`2^r`$, giving $`r\le d-w-1`$. By (2), elements in the fiber solve one square equation; its solution set is an affine translate of $`C_V(t)`$ and has size at most $`2^{d-r}`$, giving $`r\le w+1`$. Thus both capacity inequalities used in the exponent-2 support arguments remain valid.

The module-theoretic part of [bruck-s5-uniform-principal-support.md](bruck-s5-uniform-principal-support.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/32b5918c4b3fa3b2686185006b80d41b1ece76aa), is independent of exponent. With (4) and the capacity inequalities just established, its envelope deductions carry over: if the principal block has $`m`$ $`M`$-factors and the N-block is $`N^a\oplus U^b`$, then


```math
\dim V_{\rm principal}\le328m,\qquad a\le110m+1.
```


The kernel-graph and shear proof of [bruck-s5-active-u-stabilizer.md](bruck-s5-active-u-stabilizer.md), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/7ee728cc65fcaa28ffac8850185d0fdfe9a8bc48), uses only those module facts, core-freeness and the capacity bounds. It therefore carries over as a stabilizer normal form: at most $`111m+1`$ U-blocks need be active, with arbitrarily many standard complements. It does not assert a product decomposition of the loop or its section.

Finally $`m\ge1`$. If $`m=0`$, every image of $`E=J^*`$ in $`V`$ must vanish because every nonzero image has an $`M`$-factor. Equation (3) gives $`\delta=0`$, so the loop has exponent 2; the reviewed N-block exclusion in [bruck-s5-module-blocks.md](bruck-s5-module-blocks.md), source [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499), rules out that envelope. Block separation also gives $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(E,N^a\oplus U^b)=0`$, so $`\delta`$ takes values in the principal block and the U-block is untwisted by inversion.

The inversion, derivation, functional-obstruction and general-exponent carryover arguments have the scoped independent reviews below. They do not bound $`m`$ or the inactive U multiplicity, solve the affine radical-section problem, or establish a parameterization of exponent-4 loops. Prior reviews apply only to their pinned inputs.

## Independent reviews

reviewers contributor 1 and contributor 2 independently accepted this reduction at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/343e1daba1ff08c869fd4a2b8a9bb318c873bf17), conditional on the explicitly cited source results and pinned module, central-extension detection, support, active-normal-form and N-block inputs. Both directly checked Baumeister–Stein arXiv:0908.2597v1 Lemmas 3.2, 3.4, 4.1, 4.2 and 4.5. Their reviews cover inversion on V and the quotient, the nonsplit relative derivation and its augmentation-module correspondence, the affine action and forced orbit, the invariant-functional pushout, both capacity bounds, and their use in the stated support bounds and m≥1 conclusion. Neither review independently audits all earlier module calculations, accepts the subsequent parameterization extension, proves exponent 2, or establishes the full classification. No formal verification was performed.
