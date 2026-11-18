# 0110. No nilpotent transitive factor action on an entire alternating socle

**Mira Cult**

The [general nilpotent-action theorem](0109-nilpotent-socle-actions-are-two-groups.md) leaves transitive 2-groups acting on the simple factors of a whole socle. For alternating factors, none of those actions can occur.

**Theorem.** Suppose the faithful left multiplication group $`G`$ of a finite simple non-Moufang left Bol loop has **entire socle** $`S=A_d^n`$, with $`d\ge5`$ and $`n\ge2`$. The group induced by $`G`$ on the $`n`$ factors cannot be both nilpotent and transitive. This includes nonregular transitive 2-groups, with no assumption that the actual loop stabilizer maps onto $`G/S`$.

The key is to find one involution in the actual stabilizer, not to assemble one from unrelated coordinate images. If the stabilizer meets the socle in odd order, the other part of the proof bounds how many distinct original left translations its small coordinate projections can accommodate.

## A central involution in the actual stabilizer layer

Put $`T=A_d,\ A=H\cap S,\ U_i=\pi_i(A)`$. By the [whole-socle projection theorem](0105-nilpotent-socle-stabilizer-projections.md), $`H\to C`$ and the $`U_i`$ are equivalent nontrivial proper subgroups under actual stabilizer transports, so we can identify them with $`U`$. The [nilpotent factor-action theorem](0109-nilpotent-socle-actions-are-two-groups.md) gives $`C`$ a 2-group, $`n`$ a power of two, equality of the signed and unsigned coordinate images, and a selected mark $`\lambda`$ exchanging every coordinate in pairs.

**Parity lemma.** For any nonabelian simple type $`T`$ for which every involution class is invariant under $`\operatorname{Aut}(T)`$, under these hypotheses $`A`$ has odd order. Indeed take a Sylow 2-subgroup $`P`$ of $`H`$. It maps onto the entire 2-group $`C`$, since the index of its image divides the odd $`[H:P]`$. If $`|A|`$ is even, $`P\cap A`$ is a nontrivial normal 2-subgroup of $`P`$ (it is Sylow in $`A`$). Conjugation by $`P`$ on it has nontrivial fixed subgroup by the class equation; choose an involution $`z\in Z(P)\cap A`$. Its projection is nonidentity at some site, hence at every site by transitivity, and all local entries represent a **single inner class** because they are related by actual $`P`$-arrows and that class is automorphism-invariant. On each exchanged edge of $`\lambda`$ the two entries are inverse-conjugate after its actual arrow. Within the allowed inner coset choose a forward arrow $`r`$ identifying the source entry $`z_i`$ with its target $`z_j=r(z_i^{-1})`$. The two forward arrows $`r`$ and $`r\operatorname{Inn}(z_i)`$, with their corresponding inverses on the return edge, both occur among the inner conjugates of this mark. Their product on the two sites is $`(z_i,z_j)`$. Perform this independently on the disjoint edges: since the conjugation action of $`G`$ on its whole socle is faithful, the product is the actual element $`z`$. This contradicts $`A\subseteq H,\ H\cap\Lambda^2=1`$. In particular no independent-coordinate lifting of a collection of involutions in the $`U_i`$ was assumed; $`z`$ is one actual element of $`A`$.

For $`d\ge7,\ \operatorname{Aut}(A_d)=S_d`$. Every nonidentity involution has an odd permutation in its symmetric centralizer, namely any one of its constituent transpositions. Thus its symmetric conjugacy class does not split on restriction to $`A_d`$. The same holds for $`d=5`$; at $`d=6`$ the full outer group is exceptional, but $`A_6`$ has just one nonidentity involution class, its double transpositions. This verifies the parity lemma in every alternating case. Hence $`U`$ too has odd order.

Here are two packing estimates. Let $`L=|T|,\ V=|\operatorname{Aut}(T)|`$ and $`I=|\{\gamma\in\operatorname{Aut}(T):\gamma^2=1\}|`$, identity included. For a physical coordinate involution $`\sigma`$ with $`s`$ fixed sites, at most $`I^s V^{(n-s)/2}`$ actual marks have that label; different marks on the signed coset have different actions on $`S`$ since $`C_G(S)=1`$. The true transversal gives $`|K||A|=[G:SH]L^n\ge L^n`$. If $`I^2\ge V`$, then $`|K|\le2^{n-1}I^n<(2I)^n`$, using the order of a Sylow 2-subgroup on $`n=2^a`$ sites. Since $`|A|\le|U|^n`$,
```math
L<2I|U|.\qquad (1)
```
For $`d\ge7`$ the inequality $`I^2\ge d!`$ is immediate without character estimates: every permutation is a product of two involutions (reverse each of its cycles by an involution).

Sometimes $`U\le M\le T`$ where the $`T`$-class of **this overgroup** $`M`$ is invariant under $`\operatorname{Aut}(T)`$. This does not require $`H`$ to normalize any chosen $`M`$. After using frames with $`A\subseteq M^n`$, conjugate the all-paired mark inside $`S`$ so that on each edge its arrow identifies the two copies of $`M`$. Such an inner adjustment exists by class invariance and may be made independently on each edge. The left translate of its $`S`$-class by the adjusted mark contains all pairs $`(u,r u^{-1}r^{-1})`$ on each edge with $`u\in M`$ and its actual adjusted arrow $`r`$. These $`|M|^{n/2}`$ tuples in $`M^n`$ lie in distinct left cosets of $`A`$, or the product of two original signed involutions would be in $`A\setminus\{1\}`$. Thus $`|A|\le|M|^{n/2}`$; (1) then strengthens to $`L<2I\sqrt{|M|}`$. The packing compares genuine paired cosets even if $`A`$ is correlated and $`M`$ is just a convenient container.

## The size of an odd permutation group

For self-containment we give the elementary size estimate needed after the odd-order solvability theorem:
```math
D\le S_b,\quad |D|\text{ odd}\quad\Longrightarrow\quad
                              |D|\le3^{(b-1)/2}.\qquad (2)
```
Induct on $`b`$, including $`b=1`$. For an intransitive action multiply the bounds for the orbit projections; with $`k`$ orbits this actually gives $`3^{(b-k)/2}`$. For a transitive imprimitive action on $`c`$ blocks of size $`a`$, the block kernel embeds in a product of $`c`$ odd groups on $`a`$ letters, and the quotient is an odd group on $`c`$ letters. The product bound has exponent $`(c(a-1)+c-1)/2=(b-1)/2`$.

In the primitive case $`D`$ is solvable by [Feit–Thompson, *Solvability of groups of odd order*](https://msp.org/pjm/1963/13-3/pjm-v13-n3-p01-s.pdf). A minimal normal subgroup is elementary abelian of order $`p^k`$ and is transitive, its orbits being blocks; being abelian and transitive in a faithful action, it is regular. Its point stabilizer in $`D`$ acts faithfully by linear maps, so $`b=p^k`$ and $`|D|\le b\,|\operatorname{GL}_k(p)|_{\rm odd}`$, where the subscript denotes the odd part. For $`k\ge3`$, the crude $`p^{k(k+1)}\le3^{(p^k-1)/2}`$ suffices: at $`p=3`$ this is $`k(k+1)\le(3^k-1)/2`$, by induction from $`k=3`$, and $`(x-1)/\log x`$ increases with $`x>1`$. For $`k=2,\ p\ge5`$ use the same increasing ratio and the check $`5^6\le3^{12}`$; for $`k=2,\ p=3`$, the affine odd bound is $`9\cdot3=27\le81`$. For $`k=1,\ p\ge11`$ use $`p^2\le3^{(p-1)/2}`$, starting at eleven. At $`p=3,5,7`$ the respective affine odd bounds are $`3,5,21`$, all satisfying (2). This proves (2).

## Alternating degrees at least seven

For $`d\ge7`$, $`L=d!/2`$ and $`I=I_d`$ satisfies $`I_0=I_1=1,\ I_d=I_{d-1}+(d-1)I_{d-2}`$, by whether the last letter is fixed. For $`d\ge11`$,
```math
d!>4 I_d\,3^{(d-1)/2}.
```
Indeed $`X_d=I_d3^{(d-1)/2}/d!`$ satisfies $`X_d=(\sqrt3 X_{d-1}+3X_{d-2})/d`$. Directly $`X_{11},X_{12}<1/4`$, with $`I_{11}=35696,\ I_{12}=140152`$, and the recurrence preserves the strict inequality. Now (2) contradicts (1).

At $`d=10`$ the odd $`U`$ is intransitive since its orbit lengths are odd. It has at least two orbits, hence $`|U|\le3^4=81`$ by the stronger intransitive bound. But $`L=1814400,\ I=9496`$ contradict (1). At $`d=9`$, if $`U`$ is intransitive it has at least three odd-length orbits, giving $`|U|\le27`$. If primitive its affine bound is also 27. If transitive imprimitive on nine letters it embeds in the group on three blocks of size three, of order $`(3!)^3\,3!`$; thus it is a 3-group and is contained in a Sylow 3-subgroup $`M`$ of $`A_9`$, of order 81. All such subgroups are $`A_9`$-conjugate, so the packing bound applies. The weaker of the two resulting local multipliers is $`\max(27,\sqrt{81})=27`$; $`L=181440,\ I=2620`$ again contradict the required bound.

At $`d=7,8`$ we give stable containers rather than assuming two $`S_d`$-conjugate odd subgroups are $`A_d`$-conjugate. The odd orbit sizes different from one can only be $`3,5,7`$. On each such orbit the action is primitive of prime degree. The preceding affine argument puts it in a specific $`C_3,\ C_5,`$ or $`C_7:C_3`$ of order $`3,5,21`$, respectively: these are the odd Hall subgroups of the one-dimensional affine normalizers. The product of these containers on the disjoint actual orbits is an odd $`M`$ of order at most 21 (the largest other possibilities are $`5\cdot3`$ and $`3^2`$). Its $`A_d`$-class is $`S_d`$-invariant. In fact an odd permutation normalizes a local factor, and can be extended by identity elsewhere: on a triple take a transposition; on a five- or seven-orbit take multiplication by a primitive scalar in the affine field, a cycle of length four or six on the nonzero points, normalizing the specified odd subgroup. The nontrivial $`U`$ has some such orbit. Packing gives $`L<2I\sqrt{21}`$, contradicted by $`(L,I)=(2520,232),(20160,764)`$, respectively.

## A sharp signed count in a symmetric Sylow 2-group closes degree six

At $`T=A_6`$, odd $`U`$ has either a five-point orbit and one fixed point or only orbits of lengths one and three. In the first case it is a five-group by the affine bound; in the other it is a 3-group. It lies in a Sylow five- or three-subgroup of $`A_6`$, of order five or nine respectively. These containers have automorphism-invariant inner classes by the Sylow theorem even for the **full exceptional** automorphism group. Thus $`|A|\le3^n`$ by paired packing. To contradict $`|K|\ge120^n`$ it does not suffice to use $`2I=224`$.

For arbitrary $`T`$, take a Sylow 2-group $`W_n`$ of $`\operatorname{Sym}(n)`$ containing a conjugate of the actual $`C`$. Define
```math
F_n=\sum_{\substack{\sigma\in W_n\\ \sigma^2=1}}
           I^{|\operatorname{Fix}(\sigma)|}\,
           V^{(n-|\operatorname{Fix}(\sigma)|)/2}.
```
This is an **upper bound**, not an assertion that every possible label occurs. In the natural binary block presentation, $`W_{2m}=(W_m\times W_m)\rtimes C_2`$. A square-one element preserving both halves gives two independent square-one permutations. One interchanging the halves has form $`(w,w^{-1})`$ times the swap and exchanges $`m`$ pairs. Since $`|W_m|=2^{m-1}`$,
```math
|K|\le F_n,\qquad F_1=I,\qquad
                         F_{2m}=F_m^2+2^{m-1}V^m.\qquad (3)
```
If $`r=V/I^2<1/2`$, then, using $`F_m\ge I^m`$,
```math
\log(F_n^{1/n}/I)
 \le \sum_{m=1,2,4,\ldots<n}\frac{1}{2m}\log(1+2^{m-1}r^m)
 \le \sum_{m=1}^{\infty}\frac{(2r)^m}{4m}
 =-\tfrac14\log(1-2r).
```
The first sum runs only over powers of two, the second over all positive integers. For $`A_6`$, $`V=1440,\ I=112`$ as shown for the actual $`\operatorname{P\Gamma L}_2(9)`$ in the [simple-type count](0105-nilpotent-socle-stabilizer-projections.md) and the independent finite replay linked below; taking $`I`$ merely from $`S_6`$ would be wrong. Thus $`2r<1`$ and $`I(1-2r)^{-1/4}<120`$, equivalently
```math
112^6<120^4\,(112^2-2\cdot1440).
```
This contradicts the required $`|K|\ge120^n`$ for all $`n`$, without a finite cutoff in the number of factors.

Finally $`A_5=\operatorname{PSL}_2(4)`$ is already excluded in this setting by the separately reviewed [four-element-field endpoint](0106-nilpotent-transitive-even-field-psl2.md) and its tuple-incidence argument. It is not a consequence of the small alternating inequality just used. This proves the stated family exclusion.

## Scope and reproducibility

This rules out a whole alternating power with the stated action. It does not rule out single alternating factors, alternating sections, mixed socles, nontransitive actions, or nonnilpotent transitive actions. The question of which simple types admit a nilpotent transitive factor action remains open in general.

The [author's finite checks](../sources/code/verify_alternating_nilpotent_odd_stabilizers.py) and the [independent exceptional-action checks](../sources/code/check_alternating_sylow_wreath_independent.py) test different parts of the argument. In particular, the second constructs every semilinear permutation in the exceptional ten-point model of $`\operatorname{Aut}(A_6)`$ and all 13,984 square-one permutations in its two-site wreath product. The [evidence record](../normal-layer-evidence.md#alternating-whole-socle-powers) gives the exact scientific revision and separate dependency scopes. Under Mira Cult's research direction, OpenAI models contributed the proof, finite computations, independent review and public exposition. Model versions for these contributions are not documented here. This is not human peer review or formal verification.
