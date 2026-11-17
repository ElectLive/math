# Candidate prime-factor HC exclusions with inner automorphisms

**Mira Cult**

This manuscript-local candidate addresses [C0010](../../claims/0010.md), using the HC folder and shared-transposition interfaces in [C0014](../../claims/0014.md) and [C0015](../../claims/0015.md). It has the scoped independent review recorded below and introduces no claim ID. It concerns primitive `HC` with a prime number of simple factors in each regular minimal normal subgroup, under the separate hypotheses stated below; it does not exclude general `HC` or other O'Nan–Scott types.

## Conditional statement and interface

Let $`Q`$ be a finite nonassociative left Bol loop whose left multiplication group $`G=\mathop{\mathrm{LMlt}}\nolimits(Q)`$ acts faithfully and primitively on $`Q`$ of `HC` type. Suppose the socle is $`B=B_1\times B_2`$ with $`B_i\cong T^2`$ regular, where $`T`$ is a nonabelian finite simple group. Let $`H=G_{1_Q}`$ and identify the factors so that $`H\cap B=\Delta(T^2)`$. Assume the folder/inversion results used in C0014 and C0015: $`K=\{L_x:x\in Q\}`$ contains $`1`$, generates $`G`$, and is inverted elementwise by an involutory $`\tau\in\mathop{\mathrm{Aut}}\nolimits(G)`$. Put $`\widetilde G=G\rtimes\langle t\rangle`$, with $`t`$ acting as $`\tau`$, and $`\Lambda=tK`$. Assume each element of $`\Lambda`$ is an involution, $`\Lambda`$ is $`G`$-conjugacy invariant, and $`\Lambda^2\cap H=\{1\}`$.

**Candidate theorem.** If every involution in $`\mathop{\mathrm{Aut}}\nolimits(T)`$ is inner and every $`T`$-conjugacy class of involutions is $`\mathop{\mathrm{Aut}}\nolimits(T)`$-invariant, no such folder exists. In particular, this excludes $`\mathop{\mathrm{Out}}\nolimits(T)=1`$ under the stated folder and shared-pair interfaces. The proof uses an involution in $`T`$; its existence follows from Feit–Thompson's odd-order theorem for finite nonabelian simple groups. The shared-pair argument needs an invariant involution class, which the present hypotheses supply directly. No general CFSG-dependent invariant-class assertion is needed for this conditional special case.

## Factor actions and point-stabilizer identification

The two socle subgroups are regular and transitive, so $`G=BH`$. Any $`h\in H`$ normalizes $`H\cap B=\Delta(T^2)`$ and therefore induces the same automorphism of $`T^2`$ on $`B_1`$ and $`B_2`$. Inner conjugations by $`B`$ preserve every simple factor setwise. Thus the factor actions of any $`g\in G`$ agree on the two socles. Since each $`B_i`$ is minimal normal in $`G`$, this common action on its two factors is transitive; its image is $`\Delta(C_2)`$.

Moreover $`C_G(B)=1`$. Indeed, a nontrivial normal centralizer is transitive by primitivity, and is semiregular because it centralizes transitive $`B`$; hence it is regular. Its centralizer in the full symmetric group is regular and contains the transitive group $`B`$, forcing $`B`$ regular, contrary to $`H\cap B\ne1`$. Therefore an element of $`G`$ inducing on $`B`$ the same automorphism as an element of $`H`$ belongs to $`H`$. More concretely, if an element of $`G`$ induces the same automorphism of $`T^2`$ on the two socles, write it as $`bh`$ with $`b\in B`$ and $`h\in H`$. The two components of $`b`$ induce the same inner automorphism; since $`T^2`$ is centerless, $`b\in\Delta(T^2)\le H`$, so the element lies in $`H`$.

## An off-diagonal fixed-factor obstruction

Suppose $`\tau`$ preserves both $`B_i`$ (Case A) and $`\mu\in\Lambda`$ has top (identity, swap). Assume its fixed-side restrictions to $`B_1`$ are $`(\iota_u,\iota_v)`$ with $`u^2=v^2=1`$ and at least one of $`u,v`$ nonidentity; let $`C_u,C_v`$ denote their $`T`$-conjugacy classes, including $`C_1=\{1\}`$. Under the theorem's hypotheses these classes are $`\mathop{\mathrm{Aut}}\nolimits(T)`$-invariant. We show such $`\mu`$ is impossible. The reverse orientation is symmetric.

Choose **any** $`h\in H`$ with matched swap top, available because $`G=BH`$ and the common factor action is transitive. No involutory lift is assumed. The two $`B_2`$ restrictions of $`\mu`$ and $`\mu^h`$ have forms $`(\gamma,\gamma^{-1})s`$ and $`(\eta,\eta^{-1})s`$, where $`s`$ swaps the two factors, because both elements are involutions. The fixed $`B_1`$ components of $`\mu^h`$ are inner by elements in $`C_v,C_u`$, in that order: conjugation by $`h`$ transports the factors by automorphisms, and the classes are invariant.

The product $`\mu\mu^h\in G`$ has trivial factor top. Its first $`B_1`$ restriction is inner, whereas the corresponding $`B_2`$ restriction is $`\gamma\eta^{-1}`$. Matched outer actions of $`G=BH`$ imply $`[\gamma]=[\eta]`$ in $`\mathop{\mathrm{Out}}\nolimits(T)`$.

Independent conjugation by $`B`$ changes each fixed inner restriction throughout its $`T`$-conjugacy class and changes the parameter of a swapped restriction throughout its inner coset. Select $`u_1\in C_u`$ and $`v_2\in C_v`$ with $`z=u_1v_2\ne1`$. Such a choice exists: a nonidentity class in centerless $`T`$ has more than one element. Put $`v_1=\gamma^{-1}(v_2)\in C_v`$ and $`u_2=\gamma^{-1}(u_1)\in C_u`$. After independent $`B`$-conjugation of $`\mu`$ and $`\mu^h`$, choose their fixed restrictions as $`(\iota_{u_1},\iota_{v_1})`$ and $`(\iota_{v_2},\iota_{u_2})`$. Their product restricts to

$$
 (\iota_z,\iota_{\gamma^{-1}(z^{-1})})
$$

on $`B_1`$. Choose the swapped parameters of these conjugates to be $`\gamma`$ and $`\eta'=\iota_{z^{-1}}\gamma`$, respectively. The latter is available since $`[\eta']=[\eta]`$. Their product restricts on $`B_2`$ as

$$
 (\gamma\eta'^{-1},\gamma^{-1}\eta')
 =(\iota_z,\iota_{\gamma^{-1}(z^{-1})}).
$$

It therefore induces the same automorphism on the two socles and lies in $`H`$ by the preceding identification. It is nonidentity because $`z\ne1`$ and $`T`$ is centerless. Both factors belong to $`\Lambda`$ by $`G`$-conjugacy invariance, contradicting $`\Lambda^2\cap H=\{1\}`$.

## Mixed orientations with trivial fixed sides

Suppose instead $`\Lambda`$ contains $`\mu`$ of top (identity, swap) centralizing $`B_1`$ pointwise and $`\nu`$ of top (swap, identity) centralizing $`B_2`$ pointwise. Let their swapped-side parameters be $`\gamma`$ and $`\alpha`$. Their product lies in $`G`$, so its matched factor automorphisms have the same outer class; hence $`[\gamma]=[\alpha]`$ in $`\mathop{\mathrm{Out}}\nolimits(T)`$. Independent $`B`$-conjugation makes their swapped parameters equal. Their product then induces the same swap automorphism on both socles, and lies in $`H`$ by the point-stabilizer identification. Its top is nontrivial, so it is nonidentity, contradicting $`\Lambda^2\cap H=\{1\}`$.

## Top-coset conclusion

The automorphism $`\tau`$ either preserves $`B_1,B_2`$ or swaps them. The latter is excluded by the HC Case-B argument of C0014 under its stated folder hypotheses. In Case A, let $`\pi(t)\in C_2\times C_2`$ denote the two factor permutations of the external involution. Since $`\pi(G)=\Delta(C_2)`$, the top of $`\Lambda=tK`$ lies in $`\pi(t)+\Delta(C_2)`$. Because $`1\in K`$ and $`\langle K\rangle=G`$, both elements of that coset occur: $`t\in\Lambda`$, and some $`k\in K`$ has nontrivial common top.

If $`\pi(t)`$ is diagonal, one element of $`\Lambda`$ swaps the two factors on both socles. The shared-pair argument in C0014/C0015 excludes it using any $`\mathop{\mathrm{Aut}}\nolimits(T)`$-invariant involution class; such a class exists here by Feit–Thompson and the theorem's class-invariance hypothesis. If $`\pi(t)`$ is off-diagonal, both orientations occur. Every fixed-factor automorphism of each $`\lambda\in\Lambda`$ is an involution or identity; by hypothesis it is inner. The first obstruction forces both fixed restrictions to be identity for every element in either orientation. The mixed-orientation obstruction then gives the contradiction. Thus the candidate theorem follows, conditional on its stated folder and shared-pair inputs. $`\square`$

## Scope and review

The special case $`\mathop{\mathrm{Out}}\nolimits(T)=1`$ meets both additional hypotheses: all automorphisms are inner and inner automorphisms preserve each conjugacy class. The argument uses Feit–Thompson and the cited folder/shared-pair inputs; it does not assert a general HC exclusion, an independently verified upstream inversion theorem, or an unrestricted classification. In particular, outer involutions and involution classes moved by automorphisms are outside the theorem's hypotheses. The two obstructions, their use of arbitrary $`h`$, and the aggregate argument have the scoped review below.


## Candidate odd-prime extension for trivial outer automorphism group

Assume the same faithful primitive HC folder and inversion interface, replacing $`T^2`$ by $`T^r`$ in each regular socle $`B_i`$, where $`r\ge3`$ is an odd prime. In particular $`G=BH`$, $`H\cap B=\Delta(T^r)`$, $`\Lambda=tK`$ is $`G`$-conjugacy invariant and consists of involutions, and $`\Lambda^2\cap H=\{1\}`$. Suppose $`\mathop{\mathrm{Out}}\nolimits(T)=1`$. **Candidate conclusion:** no such folder exists. The argument also uses the conditional HC Case-B and shared-pair results of C0014/C0015; it has the scoped independent review below.

As above $`C_G(B)=1`$, the two factor actions of $`G`$ coincide under the diagonal identification, and their common image $`P\le S_r`$ is transitive by minimal normality of the two socles. C0014 excludes $`\tau`$ swapping $`B_1,B_2`$, so suppose it preserves them, with factor actions $`a,b\in S_r`$ for the external involution $`t`$. Since $`t`$ normalizes $`G`$ and the factor image of $`G`$ is $`\Delta(P)`$, both $`a,b`$ normalize $`P`$ and $`\delta=a^{-1}b`$ centralizes $`P`$. Both $`a,b`$ are involutions or identity.

If $`\delta=1`$, then $`a=b`$. If $`a\ne1`$, $`t\in\Lambda`$ has a shared transposed pair; if $`a=1`$, generation of $`G`$ by $`K`$ gives $`k\in K`$ with nonidentity top $`p\in P`$, and $`tk\in\Lambda`$ has matched nonidentity involutory top $`p`$, hence a shared transposed pair. The shared-pair argument of C0014/C0015 applies to any $`\mathop{\mathrm{Aut}}\nolimits(T)`$-invariant involution class. Such a class exists here: Feit–Thompson gives an involution in $`T`$, and $`\mathop{\mathrm{Out}}\nolimits(T)=1`$ makes its class invariant.

Now suppose $`\delta\ne1`$. The centralizer in $`S_r`$ of a transitive permutation group is semiregular: a centralizing permutation fixing one point fixes all points. Thus the cyclic group $`\langle\delta\rangle`$ acts semiregularly on $`r`$ points, so its nontrivial orbits all have size $`r`$ and $`\delta`$ is an $`r`$-cycle. As $`P`$ centralizes $`\delta`$, $`P\le C_{S_r}(\delta)=\langle\delta\rangle`$, and transitivity gives $`P=\langle\delta\rangle\cong C_r`$. The normalizer of $`P`$ is the affine group on $`\mathbb F_r`$. Since $`a,b`$ normalize $`P`$, are distinct, have $`a^{-1}b\in P\setminus\{1\}`$, and are involutions or identity, they are distinct affine reflections: each has multiplier $`-1`$ and one fixed point. In particular they each conjugate every element of $`P`$ to its inverse.

Let $`c`$ generate $`P`$. Choose $`h_0\in H`$ with common factor action $`c`$, possible since $`G=BH`$. Every factor automorphism of $`h_0`$ is inner because $`\mathop{\mathrm{Out}}\nolimits(T)=1`$. Multiplication by a suitable element of $`H\cap B=\Delta(T^r)`$ makes its action on both socles the pure matched factor permutation $`c`$. Call the resulting element $`h\in H`$. Its $`r`$th power centralizes $`B`$, so $`h^r=1`$ by $`C_G(B)=1`$. Thus the pure lift is constructed; it is not assumed that an arbitrary lift has order $`r`$.

Take $`\lambda=t\in\Lambda`$ and $`\mu=\lambda^h\in\Lambda`$. On a socle, if $`\lambda`$ has reflection top $`\sigma`$, then $`\mu`$ has top $`c^{-1}\sigma c`$ and their product top is

$$\sigma(c^{-1}\sigma c)=c^2,$$

independent of $`\sigma`$, since $`\sigma c^{-1}\sigma=c`$. As $`r`$ is odd, $`c^2`$ is a nontrivial $`r`$-cycle, and this is the common product top on both socles. The same formula covers distinct reflections $`a`$ and $`b`$.

On each socle $`\lambda`$ is an involutory monomial automorphism with reflection top: it has one fixed factor and $`(r-1)/2`$ transposed pairs. Since $`\mathop{\mathrm{Out}}\nolimits(T)=1`$, all factor maps are inner. Independent conjugation by $`B`$ normalizes the maps on every transposed pair to identity; on the fixed factor the remaining map is an inner involution $`\iota_u`$ for some $`u^2=1`$, including $`u=1`$. The two socles may have different $`u`$. The pure matched permutation $`h`$ transports each socle's fixed restriction of $`\lambda`$ to that of $`\mu`$, preserving its $`T`$-conjugacy class. Independently $`B`$-conjugate $`\mu`$ to normalize all its transposed pairs and make its fixed restriction exactly the same $`\iota_u`$ as the normalized $`\lambda`$ on that socle. These operations preserve membership in $`\Lambda`$ and do not alter factor tops.

Their product on each socle has the single $`r`$-cycle top $`c^2`$ and has exactly two potentially nonidentity coordinate maps, both equal to $`\iota_u`$; the reflection fixed points are distinct because $`c^{-1}\sigma c\ne\sigma`$. Its cycle product is therefore $`\iota_u^2=1`$. A monomial automorphism with a single cycle and trivial cycle product is conjugate by an inner automorphism of $`T^r`$ to that pure cycle: starting at one coordinate, choose successive inner conjugating maps to cancel each coordinate map; the last equality follows from the trivial cycle product. Conjugating the entire product by a suitable element of $`B_1\times B_2`$ independently normalizes both socles, while simultaneously conjugating both factors and keeping them in $`\Lambda`$.

The resulting product $`x`$ induces the pure matched $`c^2`$ on both socles. The element $`h^2\in H`$ induces the same automorphism of $`B`$; since $`C_G(B)=1`$, $`x=h^2\in H`$. Its factor top is a nontrivial $`r`$-cycle, contradicting $`\Lambda^2\cap H=\{1\}`$. This proves the proposed odd-prime extension under the stated inputs. $`\square`$

Together with the two-factor theorem above, the candidate therefore excludes primitive HC with a prime number of factors in each socle when $`\mathop{\mathrm{Out}}\nolimits(T)=1`$. This assembly and its monomial-cycle normalization have the scoped review below; it says nothing about composite factor counts or arbitrary outer automorphism groups. The existing two-factor theorem retains its weaker, separately stated hypotheses.

## Independent review

contributor 1 accepted both the two-factor result and the odd-prime Out(T)=1 extension at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/e8f8c9609eaa8e9fd6fbc29acf92e9b4c835462c), conditional on the stated C0014/C0015 folder, Case-B and shared-pair inputs and Feit–Thompson (source details in [REFERENCES.md](../foundations/references.md)). The review checked matched factor/outer actions and H-membership, arbitrary matched-swap h and independent B-conjugations, mixed orientations, the centralizer-of-P prime-degree argument, affine reflections, construction of the pure h, and trivial cycle monodromy giving a nonidentity stabilizer collision. This does not certify the upstream HC results or exclude composite factor counts and arbitrary outer automorphism groups.
