# Marked sections with standard N-block bulk

**Theorem with the scoped independent reviews below.** This continues [0323:C0010](../../claims/0010.md) under the hypotheses and group splitting of [the passive reduction](bruck-n-frattini-passive-reduction.md) at the recorded source revision, and its bounded-stabilizer section independently reviewed at the recorded source revision. In particular use the actual normal form

```math
G=E\ltimes Y,\quad H=H_0\ltimes T,\quad \tau(E)=E,\quad \tau|_Y=1,
```

where $`Y\cong U^s`$, $`H_0=H\cap E`$, the image of $`H_0`$ in $`S_5`$ is $`F\cong F_{20}`$, and $`T`$ is a direct sum of $`F`$-stable complements to $`\mathop{\mathrm{soc}}\nolimits(U)`$. After absorbing the exceptional blocks into E, write P0=O2(E). Then E/P0 is S5, the Frattini subgroup of P0 is N, and P0/N is X plus at most 101 copies of U, with X=J or P6. Thus |E| is at most 120 times 2^818, independently of s. The inherited automorphism fixes H0 pointwise. These are bounded active data; the section deductions below have the scoped independent reviews recorded at the end. This paper describes the remaining original section, without assuming a quotient loop or a product decomposition of the folder.

Form $`G^+=G\rtimes\langle\widehat\tau\rangle`$, where $`\widehat\tau`$ implements $`\tau`$. Let $`\Omega`$ be the involutions in $`E\widehat\tau`$ whose image in $`S_5`$ is either the identity or a transposition; write $`\Omega_{\rm rad}`$ and $`\Omega_{\rm out}`$ for these two parts. For $`a\in\Omega`$, denote its image in $`S_5`$ by $`t_a`$. **Use the product convention $`a y`$** for $`y\in Y`$, and write $`e y e^{-1}=e\cdot y`$.

For a transposition $`t`$, $`C_U(t)=(1+t)U`$ has dimension four, and either $`F`$-stable complement to the socle satisfies

```math
U=T_1\oplus C_U(t). \tag{1}
```

The [standalone certificate](../code/verify_bruck_n_bulk_complements.py) checks (1) for all ten transpositions and both complements, as well as $`\sum_t C_U(t)=U`$. There are exactly two complements because $`\mathop{\mathrm{End}}\nolimits_F(N|_F)=\mathbb F_2`$. Consequently $`Y=T\oplus C_Y(t)`$, with $`|C_Y(t)|=2^{4s}`$.

## Exact residual section test

Choose an $`E`$-conjugacy-invariant subset $`O\subseteq\Omega_{\rm out}`$, and subsets $`L_r\subseteq Y`$, possibly empty, for $`r\in\Omega_{\rm rad}`$, satisfying

```math
L_{e r e^{-1}}=e\cdot L_r\quad(e\in E). \tag{2}
```

Define

```math
\Lambda=\bigcup_{a\in O}\{a y:y\in C_Y(t_a)\}
 \;\cup\;\bigcup_{r\in\Omega_{\rm rad}}\{r y:y\in L_r\}. \tag{3}
```

Require $`\widehat\tau\in\Lambda`$ and all of the following:

1. For distinct $`a,b\in O`$, $`ab\notin H_0`$.
2. For $`a\in O`$ and $`r\in\Omega_{\rm rad}`$ with $`L_r\ne\varnothing`$, $`ar\notin H_0`$.
3. For $`r,r'\in\Omega_{\rm rad}`$ with $`rr'\in H_0`$, no $`y\in L_r`$, $`y'\in L_{r'}`$ satisfy $`y+y'\in T`$, except when $`r=r'`$ and $`y=y'`$.
4. $`\displaystyle |O|\,2^{4s}+\sum_{r\in\Omega_{\rm rad}}|L_r|=[E:H_0]\,2^{4s}.`$

These are necessary and sufficient for (3) to define the required marked folder section under the displayed ambient hypotheses. Indeed $`a y`$ is an involution exactly when $`y\in C_Y(t_a)`$. For outer $`a`$, conjugation by $`Y`$ fills that fixed space because it equals $`(1+t_a)Y`$. For radical $`r`$, $`Y`$ centralizes $`r`$. Thus (2) and the invariance of $`O`$ make $`\Lambda`$ $`G`$-invariant; conversely every such invariant set of marked involutions has the form (3).

For distinct active outer marks, an active product in $`H_0`$ is already a collision with passive labels zero. If the active marks coincide, two different labels cannot collide because $`C_Y(t)\cap T=0`$. For an outer and a radical mark, every radical label can be matched by an outer label modulo $`T`$, by (1). Finally two radical marks act trivially on $`Y`$, so their passive product lies in $`T`$ exactly in the case excluded by condition 3. Hence conditions 1–3 are exactly $`H\cap\Lambda^2=\{1\}`$. $`G`$-invariance gives the same condition for all conjugates of $`H`$, and condition 4 gives $`|\Lambda|=[G:H]`$. Thus $`K=\widehat\tau\Lambda`$ is a transversal to every conjugate of $`H`$, and $`1\in K`$. The involution and invariance properties give inverse closure and twisted closure; since $`\tau(H)=H`$, the resulting Bol folder is Bruck. These statements test the original section in $`G`$, rather than a section in a quotient.

## Core, generation, and isomorphism

Let $`C=\mathop{\mathrm{core}}\nolimits_E(H_0)`$. Its image in $`S_5`$ is a normal subgroup contained in $`\mathop{\mathrm{core}}\nolimits_{S_5}(F)=1`$; hence $`C\le P_0`$. It centralizes $`Y`$, so it is normal in $`G`$ and contained in $`\mathop{\mathrm{core}}\nolimits_G(H)`$. Conversely the projection of $`\mathop{\mathrm{core}}\nolimits_G(H)`$ to $`E`$ lies in $`C`$, while its intersection with $`Y`$ is an $`S_5`$-submodule contained in $`T`$. That intersection is zero: every nonzero submodule of $`Y`$ meets its socle, and $`T\cap\mathop{\mathrm{soc}}\nolimits(Y)=0`$. Subtracting the $`C`$-component therefore gives

```math
\mathop{\mathrm{core}}\nolimits_G(H)=\mathop{\mathrm{core}}\nolimits_E(H_0). \tag{4}
```


If $`O\ne\varnothing`$, differences of section elements in an outer fiber generate $`C_Y(t)`$, and $`E`$-invariance provides such fibers over every transposition. Their fixed spaces span $`Y`$, by the certificate. Therefore $`\langle K\rangle=G`$ exactly when the active projection of $`K`$ generates $`E`$. Every $`k\in K`$ has 2-power order because its image in $`S_5`$ has order at most two and the kernel $`P`$ is a 2-group.

For generated canonical envelopes, an identity-preserving loop isomorphism is exactly a group isomorphism $`\varphi:G\to G'`$ carrying $`H`$ to $`H'`$ and $`K`$ to $`K'`$. It necessarily intertwines the canonical automorphisms, $`\varphi\tau=\tau'\varphi`$, because their values on the generating sets are inversion. This is an exact full-group pointed criterion, not a classification of the label data under automorphisms. Arbitrary shifts of the marked involution or conjugation of the stabilizer are not included as loop-isomorphism operations.

Conditions (1)–(4) do not by themselves classify simple loops or remove the radical label sets. The exact simplicity test below leaves the existence and isomorphism orbits of label solutions unresolved. The theorem and certificate have the exact-source reviews recorded below.

Run the finite control with assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_n_bulk_complements.py
```

## Proposed simplicity test by linear normal-subgroup data

**Scoped independently reviewed continuation.** Assume the original-section, core and generation conditions above, so that $`G,H,K`$ is the faithful canonical envelope of the resulting Bruck loop. The following is an exact test for simplicity, expressed using the bounded active group $`E`$, submodules of $`Y`$, linear maps, and the still arbitrary original label sets. It does not classify label solutions or identify their isomorphism orbits.

Every normal subgroup $`R\lhd G=E\ltimes Y`$ is specified uniquely by a triple $`(S,L,f)`$:

- $`S=R\cap Y`$ is an $`S_5`$-submodule of $`Y`$;
- $`L=\mathop{\mathrm{proj}}\nolimits_E R\lhd E`$, with $`[Y,L]\le S`$, so $`L`$ acts trivially on $`Y/S`$;
- $`f:L\to Y/S`$ is an $`E`$-equivariant group homomorphism, with $`E`$ acting on $`L`$ by conjugation and on $`Y/S`$ through $`S_5`$.

Indeed $`R/S`$ is the graph of $`f`$ in $`E\ltimes(Y/S)`$. Triviality of the $`L`$-action makes the graph a subgroup exactly when $`f`$ is a homomorphism; conjugation by $`E`$ is exactly equivariance, and conjugation by $`Y`$ is exactly $`[Y,L]\le S`$. Conversely the inverse image of every such graph is normal in $`G`$. As $`Y/S`$ is elementary abelian, $`f`$ factors through the finite binary vector space $`L/(L^2[L,L])`$, and equivariance is a linear system. Thus $`L`$ ranges over normal subgroups of the bounded active group $`E`$; the unbounded data are the invariant subspace $`S`$, the equivariant linear map $`f`$, and the original label sets.

To state the test, express the original section as $`K=\bigcup_k kQ_k`$, with active $`k=\widehat\tau a\in E`$. For an outer mark $`a`$, $`Q_k=C_Y(t_a)`$; for a radical mark $`r`$, $`Q_k=L_r`$. Group the active $`k`$'s by their cosets $`C=kL`$ in $`E/L`$; in each occupied coset choose $`e_C`$ and write $`k=e_C\ell_k`$, $`\ell_k\in L`$. The original image has cardinality

```math
|KR/R|=\sum_C\left|\bigcup_{k\in C}
 \left(f(\ell_k)+(Q_k+S)/S\right)\right|. \tag{5}
```

The union is in $`Y/S`$: $`L`$ acts trivially there, and $`\ell_k`$ equals the passive shift $`f(\ell_k)`$ modulo $`R`$. Also

```math
[G:HR]=[E:H_0L]\,2^{\dim Y-\dim(S+T+\widetilde f(H_0\cap L))}. \tag{6}
```

Here $`\widetilde f(H_0\cap L)`$ means **any choices of lifts in $`Y`$** of the subgroup $`f(H_0\cap L)\le Y/S`$; adjoining $`S`$ makes the indicated subspace and its dimension independent of those choices. Formula (6) follows since $`HR`$ projects to $`H_0L`$ in $`E`$, and its intersection with $`Y`$ is $`S+T+\widetilde f(H_0\cap L)`$.

The loop is simple if and only if, for every such triple other than $`(0,1,0)`$ with $`HR\ne G`$, the value in (5) is strictly greater than (6). This is the normal-subloop interface associated with [C0001, Theorem 2.2](../../claims/0001.md), with the following direct justification for arbitrary normal $`R`$, without requiring $`R=\mathop{\mathrm{core}}\nolimits_G(HR)`$. The image of $`K`$ in $`G/R`$ covers every coset of $`HR/R`$; equality of its size with $`[G:HR]`$ makes it a transversal, and normality of $`R`$ gives the same conclusion for every conjugate. The folder operations descend, so this equality gives a quotient folder. If $`R\ne1`$ and $`HR\ne G`$, its loop kernel is a proper nontrivial normal subloop: a trivial kernel would put $`R`$ in the core of $`H`$, which is trivial. Conversely every proper nontrivial normal subloop gives such a normal subgroup as the kernel of the canonical left-multiplication action on the quotient and satisfies the equality. No $`\tau`$-stability of $`R`$ is assumed; (5) uses the $`K`$-coordinates directly.

There is a useful necessary constraint when $`s>0`$. Put $`\mathcal R=\{r\in\Omega_{\rm rad}:L_r\ne\varnothing\}`$. Taking $`S=Y`$, $`L=1`$, and $`f=0`$ gives

```math
|O|+|\mathcal R|>[E:H_0]. \tag{7}
```

To see why this is a strict inequality in the stated direction, partition active marks by their $`H_0`$-cosets. An outer mark fills all $`2^{4s}`$ passive $`T`$-cosets in its active coset. In a radical-only active coset, the images of the label sets in $`Y/T`$ are disjoint, including within each label set. Original transversality and the section cardinality force every active coset to be filled. Thus the left side of (7) is at least $`[E:H_0]`$; equality would give the prohibited quotient for $`R=Y`$. In particular, at least one active coset contains two distinct radical marks.

There is also an exact mass identity. Radical marks project to the identity of $`S_5`$, hence lie over the base $`F`$-coset; outer marks project to transpositions, none of which belongs to $`F_{20}`$. Every active coset over each of the other five $`F`$-cosets must therefore be filled by an outer mark. Consequently

```math
|O|=\tfrac56[E:H_0],\qquad
 \sum_{r\in\mathcal R}|L_r|=\tfrac16[E:H_0]\,2^{4s}. \tag{8}
```

These conditions constrain the original labels but do not prove that any label system satisfying them exists or bound $`s`$.

## Independent review

Independent checks an independent check, an independent check and an independent check independently accepted the full manuscript at exact source the recorded source revision, conditional on the cited group/stabilizer reductions, N-block and F20 facts, marked-image and canonical-folder inputs. All checked the marked product convention and complete collision conditions, core equality, generation and 2-power statements, full-group pointed isomorphism scope, all normal-subgroup triples, formulas (5)-(6), the arbitrary-normal-subgroup quotient argument, strict simplicity test and 5/6 mass identity. All read the exact standalone verifier and independently ran the committed source with the pinned Python 3.12 runtime; the folder and small-order reviewers specified 3.12.14. The two complements, all ten fixed-space intersections and spanning check passed. This verifies the finite controls separately from the uniform mathematical deduction. The reviews do not classify label solutions, bounded active groups or their isomorphism orbits, and do not constitute a fresh primary-source audit or formal certification.

## Structural applicability to the two-N normal form

**Theorem with the scoped independent reviews below.** Suppose instead that $`Z=\Phi(P)\cong N^2`$, $`P/Z\cong P_6\oplus U^b`$, and that the actual-stabilizer reduction in [the two-N manuscript](bruck-multiple-n-frattini.md#a-bounded-actual-stabilizer-with-two-n-factors) holds. Then the original-section, core/generation and simplicity formulas in this manuscript carry over under that two-N normal form, with the new active-size bound

```math
|E|\le120\cdot2^{6366}.                                         \tag{9}
```

This is a separate structural applicability statement, conditional on the new two-N stabilizer deduction and the same marked-image and canonical-folder interfaces used above. It does not overwrite the earlier one-N active bound or its review record. The present transport to $`N^2`$ has the exact-source reviews recorded below.

To specify the scope, rename the active factor $`E'`$ in the two-N reduction as $`E`$, its standard passive factor as $`Y`$, and its active stabilizer as $`H_0`$. The new hypotheses give exactly

```math
G=E\ltimes Y,\quad H=H_0\ltimes T,\quad
 \tau(E)=E,\quad\tau|_Y=1,
```

with $`Y\cong U^s`$, $`T`$ the direct sum of the same $`F_{20}`$-stable complements to $`\mathop{\mathrm{soc}}\nolimits(U)`$, and $`H_0`$ mapping onto $`F\cong F_{20}`$. Here $`P_0=O_2(E)=E\cap P`$, $`E/P_0\cong S_5`$, and $`\Phi(P_0)=N^2`$: $`P=P_0\times Y`$ and $`Y`$ is elementary. The central factor $`N^2`$ affects the finite active group and its normal subgroups; it does not alter the passive $`U`$-action or complement identity.

The proof above applies line by line with the following meanings and without replacing the original section by a projected one:

1. The fixed-space identity (1), including $`Y=T\oplus C_Y(t)`$ and $`\sum_tC_Y(t)=Y`$, depends only on the passive $`U|_F`$ module and the transpositions. The same pinned complement certificate applies.
2. Define $`\Omega,\Omega_{\rm rad},\Omega_{\rm out},O,L_r`$ in the actual active group $`E`$ exactly as above. The descriptions (2)–(3), the three collision conditions, and the section cardinality condition in item 4 use only the displayed semidirect products, the marked product convention, and the original marked-image theorem. They therefore test the original $`K`$ in the new $`G`$ with no assumption that $`\Phi(P_0)`$ is one copy of $`N`$.
3. The core equality (4) and generation criterion use only $`O_2(S_5)=1`$, $`P_0`$ centralizing $`Y`$, $`T\cap\mathop{\mathrm{soc}}\nolimits(Y)=0`$, and the spanning part of (1). These hypotheses remain valid. The pointed full-group isomorphism criterion likewise remains unchanged; it does not classify active or passive label orbits.
4. The normal-subgroup triples $`(S,L,f)`$, the original-section cardinality formula (5), the index formula (6), and the strict simplicity test use only $`G=E\ltimes Y`$ and the actual $`H,K`$. Their proofs do not depend on the structure of $`\Phi(P_0)`$. Thus the same formulas apply, with $`L`$ ranging over normal subgroups of the present two-N active group. The necessary inequality (7) and mass identity (8) also carry over when their stated hypotheses hold.

Thus the earlier proof supplies the indicated formulas after replacing its narrower active data by the new bounded two-N data. This does not assert a solution of their finite or unbounded label tests, a product decomposition of $`K`$, an isomorphism-orbit classification, or any new quotient-loop reduction. The active group bound (9) follows from $`|P_0/Z|\le2^{6+8\cdot794}`$, $`|Z|=2^8`$, and $`|S_5|=120`$.

## Independent review of the two-N transport

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted the structural transport, conditional on the two-N stabilizer deduction reviewed at that source and the pinned original-section/module/canonical-folder inputs. All checked the passive complement identity, original-section collision and size conditions, core and conditional generation tests, pointed isomorphism scope, normal-subgroup triples, image/index formulas, strict simplicity and mass identities with their original hypotheses. No new computation or primary-source audit was claimed. This review does not classify labels or their isomorphism orbits.

