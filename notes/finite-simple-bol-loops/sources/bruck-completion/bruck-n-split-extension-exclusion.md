# A split-extension obstruction for the P₆ multiple-N branch

**Scoped theorem continuing [0323:C0010](../../claims/0010.md).** Let $`(G,H,K,\tau)`$ be a faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. Suppose $`G/P\cong S_5`$, $`P=O_2(G)`$ has class at most two and exponent at most four, and

```math
Z=\Phi(P)\cong N^a,\qquad V=P/Z\cong P_6\oplus U^b,
 \qquad a\ge1.
```

If, additionally, the **actual group extension splits**, $`G=P\rtimes S_5`$, then no such envelope exists. The conclusion leaves nonsplit extensions over $`P`$, other Frattini modules and other principal shadows open. Independent exact-source reviews are recorded below.

The original envelope and marked-image inputs are those cited in [the multiple-N source](bruck-multiple-n-frattini.md). Its relative-$`H^1`$ displacement argument is reviewed at the recorded source revision. The affine marked-fiber parity and unique $`C_3`$-fixed orbit are reviewed for arbitrary $`a`$ in [the parity theorem](bruck-n-affine-fiber-parity.md) at the recorded source revision. The $`N`$-block, projectivity and cohomology inputs are pinned in [the N-block source](bruck-s5-module-blocks.md) at the recorded source revision. All their recorded scope and source qualifications remain in force.

## A pure double transposition in H

Let $`W=H\cap P`$ and $`F=H/W\cong F_{20}`$. Choose a Sylow-5 subgroup of $`H`$; its image in $`F`$ is the normal 5-subgroup. By coprime complement conjugacy, conjugate the entire folder by an element of $`P`$ so that this subgroup is a pure $`C_5`$ inside the chosen $`S_5`$-complement. The Frattini argument inside $`H`$ gives

```math
N_H(C_5)W=H,
```

so $`N_H(C_5)`$ maps onto $`F`$. Since the extension is split,

```math
N_G(C_5)=C_P(C_5)\rtimes F.
```

Coprime fixed-point lifting maps $`C_P(C_5)`$ onto $`C_V(C_5)`$, and the kernel is $`C_Z(C_5)=1`$. Each $`N|_{C_5}`$ has no fixed vector, while $`C_V(C_5)=P_6^F`$ has dimension two. Thus $`C_P(C_5)`$ is elementary of order four. Pure $`F`$ centralizes it: it acts trivially on the two fixed coordinates in the six-point permutation module, and the projection to $`V`$ is injective.

Choose $`p f\in N_H(C_5)`$ above a pure 4-cycle $`f\in F`$, with $`p\in C_P(C_5)`$. Then $`(pf)^2=f^2`$, so $`H`$ contains the pure double transposition $`f^2\ne1`$.

The canonical $`\tau`$ fixes the pure $`C_5`$ pointwise, because it is contained in $`H`$. It fixes $`C_P(C_5)`$ pointwise as well: $`\tau`$ fixes $`V`$, and $`C_P(C_5)\to V`$ is injective. For each pure $`g\in F`$, choose $`p_g g\in N_H(C_5)`$. Since both $`p_g g`$ and $`p_g`$ are fixed by $`\tau`$, $`\tau`$ fixes pure $`F`$ pointwise. We do **not** assume it fixes the entire chosen $`S_5`$-complement.

## An auxiliary outside involution

For pure $`g\in S_5`$, let $`a_g\in V`$ be the shadow of $`\tau(g)g^{-1}`$. It is a 1-cocycle vanishing on $`F`$. The reviewed relative-$`H^1`$ argument gives

```math
a_g=(1+g)v_0\quad(g\in S_5),\qquad v_0\in V^F=P_6^F.       \tag{1}
```

For completeness, $`H^1(S_5,U)=0`$ by projectivity, while $`P_6=\mathop{\mathrm{Ind}}\nolimits_{F}^{S_5}\mathbb F_2`$ and Shapiro identifies its $`H^1`$ with $`H^1(F,\mathbb F_2)`$ by restriction and evaluation at the fixed coset. Thus a cocycle vanishing on $`F`$ is principal.

The quotient $`V^F/V^{S_5}`$ is one-dimensional. The invariant-functional obstruction, as used in the cited parity theorem for arbitrary $`a`$, gives an augmentation-one vector in the $`F`$-fixed part of the $`W`$-shadow. Hence choose an actual $`w\in W`$ whose shadow represents the class of $`v_0`$ modulo $`V^{S_5}`$; if that class is zero, take $`w=1`$. The map $`W\to V`$ is injective, so $`w`$ is fixed by the pure $`C_5`$. Thus $`w\in C_P(C_5)`$; it is an involution, fixed by $`\tau`$, and centralizes pure $`F`$.

In the formal extension $`G\rtimes\langle\widehat\tau\rangle`$, put

```math
r=w\widehat\tau,\qquad \tau'=\mathop{\mathrm{Int}}\nolimits(w)\tau.
```

Then $`r^2=1`$. By (1), $`\tau'(g)g^{-1}\in Z`$ for every pure $`g\in S_5`$, while $`\tau'`$ fixes pure $`F`$. The residual map $`g\mapsto\tau'(g)g^{-1}`$ is a $`Z`$-valued 1-cocycle, and it vanishes on $`F`$. Since $`H^1(S_5,N)=0`$ and $`Z^F=0`$, the cocycle is zero. Thus $`r`$ centralizes the pure $`S_5`$-complement.

One way to see the cohomology vanishing is $`\mathbb F_2^5=\mathbf1\oplus N`$ and Shapiro's isomorphism $`H^1(S_5,\mathbb F_2^5)\cong H^1(S_4,\mathbb F_2)`$: the trivial summand maps isomorphically by restriction of sign, leaving $`H^1(S_5,N)=0`$. The element $`r`$ is only an auxiliary outside involution. It is **not** assumed to be selected, and it does not replace the canonical $`\tau`$ or alter the original marked set.

## The forced marked orbit

Let $`t`$ be any pure transposition. Because $`r`$ centralizes $`S_5`$, $`rt`$ is an outside involution above $`t`$, and a pure order-three element of $`C_{S_5}(t)`$ fixes its actual $`P`$-conjugacy orbit. The cited parity theorem shows that this order-three action on the full marked-orbit label torsor has a unique fixed orbit and all other orbits have length three. The number of $`P`$-orbits selected in the original marked fiber is a positive power of two congruent to one modulo three. Therefore the unique fixed orbit is selected. The original marked set $`\Lambda=\widehat\tau K`$ is $`G`$-conjugacy-invariant, so $`rt\in\Lambda`$.

Write the pure double transposition $`f^2\in H`$ as $`t_1t_2`$ for two pure transpositions. The preceding argument gives $`rt_1,rt_2\in\Lambda`$, and

```math
(rt_1)(rt_2)=t_1t_2=f^2\in H\setminus\{1\}.
```

This contradicts original folder transversality, equivalently $`H\cap\Lambda^2=1`$. The argument uses neither a selected reference $`r`$ nor a quotient loop. It excludes the stated split-extension case only, conditional on the pinned inputs.

## Quotient extensions and odd multiplicity

**Separate scoped theorem.** Under the same envelope and module hypotheses, but **without assuming that the extension over $`P`$ splits**, the branch with odd $`a`$ is impossible, conditional on the preceding split-extension obstruction and the cited inputs. This is stronger in that it includes nonsplit extensions over $`P`$; it does not extend the preceding split theorem to all even $`a`$. No quotient is asserted to be a loop.

The ordinary group extension

```math
1\longrightarrow V\longrightarrow G/Z\longrightarrow S_5\longrightarrow1
```

has a class in $`H^2(S_5,V)`$. The $`N`$-block source at the recorded source revision gives projectivity of $`U`$, so $`H^2(S_5,U)=0`$. Since $`P_6=\mathop{\mathrm{Ind}}\nolimits_{F_{20}}^{S_5}\mathbb F_2`$, Shapiro's lemma and the normal odd subgroup $`C_5\lhd F_{20}`$ give

```math
H^2(S_5,V)\cong H^2(F_{20},\mathbb F_2)
 \cong H^2(C_4,\mathbb F_2)\cong\mathbb F_2.                    \tag{2}
```

If the class is zero, a complement $`S_5\le G/Z`$ lifts through $`Z`$: its full preimage is an extension of $`S_5`$ by $`N^a`$, and the reviewed $`N`$-block result gives $`H^2(S_5,N)=0`$. Its complement is an actual $`S_5`$-complement to $`P`$ in $`G`$, so the preceding split-extension obstruction applies.

Suppose the class in (2) is nonzero. Let $`F=F_{20}`$, and choose a 4-cycle $`f`$ in a $`C_4`$-complement to its normal $`C_5`$. On the six points underlying $`P_6=\mathbb F_2[S_5/F]`$, $`F`$ has a fixed point and a five-point orbit; $`f`$ fixes one point of the latter orbit and permutes its other four points cyclically. Write $`e_0,e_1`$ for the two $`f`$-fixed basis vectors, and $`e_4`$ for the sum of the four-cycle orbit.

Restrict the extension class to $`\langle f\rangle`$. Mackey–Shapiro gives a nonzero component on each of the two fixed-point summands. The first is the defining Shapiro component of the class in $`H^2(F,\mathbb F_2)`$. For the second, the intersection of $`F`$ with the other point stabilizer is a $`C_4`$-complement; restriction $`H^2(F,\mathbb F_2)\to H^2(C_4,\mathbb F_2)`$ is an isomorphism because the normal $`C_5`$ has odd order. The four-cycle permutation summand is projective for $`C_4`$ and contributes no $`H^2`$. Hence the $`P_6`$-component of the fourth power of any lift of $`f`$ to $`G/Z`$ is

```math
e_0+e_1\pmod{\mathop{\mathrm{Norm}}\nolimits_{\langle f\rangle}(P_6)},\qquad
 \mathop{\mathrm{Norm}}\nolimits_{\langle f\rangle}=1+f+f^2+f^3.             \tag{3}
```

The norm image on $`P_6`$ is $`\langle e_4\rangle`$. Thus (3) is a norm-class statement, not an assertion that the fourth power is literally $`e_0+e_1`$ or the all-ones vector. Any $`U`$-components are immaterial to the next averaging step.

Choose an actual $`h\in H`$ above $`f`$; then $`h^4\in W=H\cap P`$. Average its shadow over the normal $`C_5`$ of $`F`$. This stays in the $`F`$-stable $`W`$-shadow. Every $`U`$-component averages to zero because $`U|_{C_5}`$ has no fixed vector. The vector $`e_4`$ also averages to zero: each point of the five-point orbit occurs four times in its five translates. The average of $`e_0+e_1`$ is the all-ones vector $`\mathbf1`$ of $`P_6`$. Consequently

```math
\mathbf1\in\overline W.                                         \tag{4}
```


The cited parity theorem supplies an independent $`F`$-fixed $`W`$-shadow vector of augmentation one. Since $`\mathbf1`$ has augmentation zero, the $`F`$-fixed dimension of $`\overline W`$ is two. That theorem also gives $`e\equiv a\pmod2`$, so the nonzero extension class is impossible when $`a`$ is odd. Together with the preceding split case, this proves the odd-multiplicity exclusion, conditional on the separately stated split obstruction and all pinned inputs.

The argument retains the actual $`H`$-lift and the norm ambiguity, and makes no assumption that $`H`$ or $`G`$ splits before it has been proved. It does not decide the nonzero quotient-extension class when $`a`$ is even. Both theorems have the scoped independent reviews below.

## Independent review

Three independent Independent checks mathematical reviewers — an independent check, an independent check and an independent check — accepted both proofs at exact source the recorded source revision. Each checked the actual split-complement argument, the auxiliary outside involution and forced selected orbit, and the nonzero quotient-extension class with its C4 norm ambiguity and C5 average. Acceptance is conditional on the cited envelope, multiple-N, affine-fiber and cohomology inputs. These are model reviews, with no new computational, formal or primary-source certification. Nonsplit even multiplicities remain open.

