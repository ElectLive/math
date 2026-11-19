# Exactly the finite groups of odd order occur as right nuclei of finite simple proper odd Bol loops

**Mira Cult**

This is a classification of one intrinsic invariant, not of the loops up to isomorphism. The target group can be given by any multiplication table; the structural conditions on an auxiliary group in the proof are not conditions on the target.

**Theorem.** For every finite group $`R`$ of odd order, including $`1`$, there is a finite simple non-Moufang **left Bol** G-loop $`Q`$ of odd order with

```math
\mathrm{Nuc}_r(Q)\cong R,\qquad
 \mathrm{Nuc}_\ell(Q)=\mathrm{Nuc}_m(Q)=\mathrm{Comm}(Q)=1,\qquad
 Z(\mathrm{LMlt}(Q))=1.
```

Thus no nonidentity nuclear right translation belongs to the left multiplication group. These conclusions continue to hold for every loop isotope of the constructed $`Q`$, since it is a G-loop. Conversely the right nucleus of **any** finite loop acts freely by its right translations: $`xc=x`$ implies $`c=1`$ by cancellation and the nucleus is a group. Consequently its order divides the loop order. In particular the possible group isomorphism types of right nuclei among simple proper odd left Bol loops are **exactly all finite groups of odd order**.

More explicitly let $`n=|R|`$, $`F_0`$ have order $`f_0=7\cdot11^3`$, and choose any prime $`\ell\equiv1\bmod11`$ not dividing $`3 n f_0`$. Put $`v=\ell^{49 n}`$. Our loop has order

```math
v\,f_0^{\,2n}|R'|\bigl(3n f_0^{\,2n}\bigr)^v.
```

This is an existence bound, emphatically not a minimum. All prescribed groups with the same $`n,|R'|`$ are realized at this very same degree, by choosing the same $`\ell`$; nonisomorphic right nuclei distinguish the resulting loops up to isotopy. For instance all abelian groups of a fixed odd order occur this way. The established abelian-specific families often give much smaller degrees.

## 1. Balanced coefficients without a chief-series restriction

We prove a transfer lemma for a nonabelian finite solvable group $`P`$ of odd order, $`A=P'`$, $`E=P/A`$, satisfying **only** $`A\cap Z(P)=1`$ concerning its commutator structure. Suppose it has a faithful irreducible action on a nonzero elementary abelian group $`V`$ over its actual odd prime field $`\mathbb F_\ell`$, with $`\ell\nmid|P|`$. Suppose $`P=S T`$ exactly, $`S`$ core-free, and $`T`$ normally generating $`P`$ (equivalently here, surjecting to $`E`$). For $`v=|V|`$ the resulting simple odd proper G-loop has order $`v|A||P|^v`$ and right nucleus

```math
N_P(S)/S\ \times\ \big(C_A(T)\rtimes (N_P(T)/T)\big).
 \tag{1}
```

The second action is conjugation by representatives, well-defined as $`T`$ centralizes the first constituent. In particular $`A`$ may contain central *sections* of $`P`$, and may be nonabelian with overlapping primes. This point is essential when the target $`R`$ in the theorem is nonabelian nilpotent. We prove the needed transfer here; the earlier stronger-hypothesis version is not assumed.

Let

```math
W=\{w\in P^V:\ \prod_{x\in V}\overline{w(x)}=1\text{ in }E\},\quad
 G=V\rtimes P,\quad Y=W\rtimes G .
```

Translations act by moving the sites, and $`h\in P`$ acts on $`w`$ by $`w(x)\mapsto h w(h^{-1}x)h^{-1}`$. With $`\varphi(w)=w(0)`$ we have the genuine epimorphism $`\pi(w,h)=\varphi(w)h`$ on $`W\rtimes P`$. Put $`K=\pi^{-1}(S)`$ and $`J=V\rtimes T`$ in their stated subgroups. The two-site balancing word shows each coordinate evaluation of $`W`$ onto $`P`$ is surjective, $`K`$ projects onto the whole pure $`P`$ in $`G`$, $`|K|=|W||S|`$, $`|J|=v|T|`$, and $`K\cap J=1`$. Thus $`Y=KJ`$ is exact.

Set $`A_*=A^V`$ and $`M=W/A_*=\ker(E^V\to E)`$. We have the following three genuinely different calculations:
* $`W'=A_*`$. To obtain a commutator $`[a,b]`$ at one specified site, put $`a,b`$ there in two words, balancing $`a^{-1}`$ at a second site and $`b^{-1}`$ at a *different third* site. The word commutator is supported only at the original site, with value $`[a,b]`$. There are at least three sites; the reverse inclusion follows by abelianizing coordinatewise. No coprimality of $`A,E`$ is used.
* $`[M,V]=M`$, since the $`V`$-average projects onto balanced constants and these are zero ($`v`$ is a unit on $`E`$). Hence $`W\le Y'`$. Also $`[V,P]=V`$ by faithfulness and prime-field irreducibility, giving $`Y'=W\rtimes(V\rtimes A)`$ and $`Y/Y'=E`$.
* $`C_W(Y')=1`$: to centralize the translations a word must be constant, to centralize $`W`$ its value must lie in $`Z(P)`$ by evaluation surjectivity, and balance puts that value in $`A`$. We do **not** claim $`[U,Y']=U`$ for every $`Y`$-normal word subgroup when only $`A\cap Z(P)=1`$ is known.

$`K,J`$ are core-free. A $`Y`$-normal subgroup inside $`K\cap W`$ has $`\varphi`$-image normal in $`P`$ and contained in $`S`$, hence trivial; by translations every point evaluation then vanishes. A normal subgroup inside $`K`$ disjoint from $`W`$ must centralize $`W`$. This is impossible for an element with nonidentity affine component: it moves a site while $`W`$ contains nonidentity single-site $`A`$ values, whose support is not restored by inner conjugation of the values. The same test excludes a normal subgroup inside the pure $`J`$. It also shows $`Z(Y)\subseteq W`$, and the third calculation makes $`Z(Y)=1`$.

[Nagy, Proposition 3.2 and Lemma 3.4](https://arxiv.org/pdf/math/0703919) now give the faithful left Bol G-loop formed by the marks $`d_y=(y,y^{-1})`$ on left cosets of $`K\times J`$ in $`Y^2`$. The actual left multiplication group $`D`$, native stabilizer $`H`$, and sign $`\tau`$ are

```math
D=\{(y_1,y_2)\in Y^2:\bar y_1\bar y_2=1\text{ in }E\},\qquad
 H=D\cap(K\times J),\qquad \tau(y_1,y_2)=(y_2,y_1).
```

Indeed products $`d_xd_yd_{xy}^{-1}`$ and their swaps supply both copies of $`Y'`$, and the marks project to the inverse graph on $`E`$. The true marks are the whole $`\tau`$-inverted set in $`D`$; $`Z(D)=1`$ by subdirectness into $`Y^2`$. The degree is $`|Y|=v|A||P|^v`$.

### All normal cuts

We apply the [odd complete-inverted signed-cut criterion](../../extraspecial-cores/signed-cut-test.md), to this faithful generating folder: it suffices to show $`|C_C(\tau)|>|C\cap H|`$ for every proper nonidentity swap-stable normal $`C`$ of $`D`$. This criterion handles the kernels of simple quotients; it does not simply assume all loop quotients have swap-stable kernels.

**Inside $`W^2`$, correlated cuts are allowed.** Let $`U=\mathrm{pr}_1 C=\mathrm{pr}_2 C`$ and $`B=\{x:(x,1)\in C\}`$. Both are $`Y`$-normal and $`B^2\le C`$. If $`B=1`$, then commutating $`C`$ with $`Y'\times1\le D`$ implies $`[U,Y']=1`$. The centralizer calculation gives $`U=1`$, impossible. Thus $`B\ne1`$, and its evaluation cannot lie entirely in $`S`$ because that image is normal in $`P`$, $`S`$ is core-free, and translated evaluations detect $`B`$. The actual fixed subgroup contains the diagonal of $`B`$, while $`J\cap W=1`$ gives

```math
|C\cap H|=|B\cap\varphi^{-1}(S)|<|B|\le |C_C(\tau)|.
```

This argument neither asserts $`C=U^2`$ nor discards normal cuts with an unsplit correlated quotient.

**Outside $`W^2`$.** A nontrivial signed normal image in $`D/W^2=\widehat G\le G^2`$ intersects $`V^2`$ nontrivially, since $`C_{\widehat G}(V^2)=V^2`$ by faithfulness. Both coordinate projections of this intersection are all of $`V`$ by prime-field irreducibility. Moreover $`[V,A]=V`$ since $`A\ne1`$ acts faithfully and is $`P`$-normal. Commutating with $`A\times1\le\widehat G`$ isolates $`V\times1`$, and swapping gives all $`V^2`$. In the original $`C`$, lift each pure translation separately. Commutate with each pure copy of $`W`$ inside $`D`$; the lifted word parts act trivially on $`M`$. Thus $`C\cap W^2`$ maps onto $`M^2`$ because $`[M,V]=M`$. It is normal in $`W^2`$, and $`M^2`$ is the full abelianization of $`W^2`$. The solvable quotient $`W^2/(C\cap W^2)`$ is perfect and hence trivial. Thus $`C\supseteq(W\rtimes V)^2`$. This implication would be false for a general *nonnormal* subgroup mapping onto the abelianization.

**Remaining correlated nonabelian tops.** $`C`$ is the full preimage of a proper swap-stable normal $`I`$ in $`\widehat P=\{(h_1,h_2):\bar h_1\bar h_2=1\}`$. Its fixed subgroup has $`|W|v|C_I(\tau)|`$ elements by literal diagonal lifts. Those stabilizer lifts above $`(h_1,h_2)\in I`$ exist precisely for $`h_2\in T`$. There are $`v`$ choices there and $`|W||S|/|P|=|W|/|T|`$ choices for the first word with $`\varphi(w)h_1\in S`$. Write $`U=\mathrm{pr}_1 I=\mathrm{pr}_2 I\triangleleft P`$ and $`B=\{x:(x,1)\in I\}\triangleleft P`$, $`B\le A`$. Then $`I/B^2`$ is the graph of an automorphism $`\alpha`$ of $`U/B`$ with $`\alpha^2=1`$. The denominator count $`|I\cap(P\times T)|`$ equals $`|B||U\cap T|`$, and $`|C_I(\tau)|=|B||\mathrm{Fix}(\alpha)|`$; all diagonal lifts are counted, whether or not the graph splits. The true cut ratio is $`[T:U\cap T]|\mathrm{Fix}(\alpha)|`$. Equality forces $`U=P`$ by normal generation of $`T`$. It also makes $`\alpha`$ fixed-point-free: $`x\mapsto x^{-1}\alpha(x)`$ then injects, hence surjects, and its images are inverted by $`\alpha`$. Thus inversion is an automorphism of $`P/B`$, so this quotient is abelian. We get $`B=A`$ and the signed graph on $`E`$ must be the entire $`\widehat P`$, contradiction. This proves simplicity in full. The stabilizer has nonidentity pure translations in its second slot; faithfulness rules out associativity, and [odd Moufang solvability](https://arxiv.org/pdf/math/0208231v2) rules out Moufangness.

### Computing the entire native right nucleus

Both $`K,J`$ surject onto $`E`$, so $`H`$ projects onto both factors and $`N_D(H)=D\cap(N_Y(K)\times N_Y(J))`$. Each pair of factor-normalizer cosets can be matched by adjusting with $`K`$ or $`J`$ since they both surject $`E`$; the quotient of this normalizer by $`H`$ is the direct product of the individual quotients. For $`K`$ its normalizer projects into $`N_G(P)=P`$ since $`V^P=0`$; within $`W\rtimes P`$ it is exactly $`\pi^{-1}(N_P(S))`$. For $`J`$ its affine projection lies in $`V\rtimes N_P(T)`$, which already normalizes $`J`$ in its pure copy. The remaining normalizing words must be fixed by all of $`J`$, hence constant with value in $`C_P(T)`$ and balanced, i.e. in $`C_A(T)`$. This proves the two factors in (1), including the conjugation action. The full centralizer of a transitive coset group in the symmetric group is the opposite of the normalizer quotient. Evaluating at the loop identity shows that a permutation commuting with every left translation is precisely a right translation by a right-nuclear element. Thus (1) computes the whole group, up to the harmless opposite conventions; group inversion identifies opposite groups.

For an exact Nagy factorization with $`Z(Y)=1`$ we also have trivial left and middle nuclei: $`d_xd_y`$ can equal any genuine mark only when $`xy=yx`$ in $`Y`$, because its first coordinate fixes the putative mark. Either nuclear identity would require this for all $`y`$; use faithfulness of the action. For the commutant we use the elementary observation in the [separate centerless ridge construction](abelian-centerless.md): if the mark $`x`$ commutes as a loop element with every $`y`$, then $`(d_yd_x)^{-1}d_xd_y\in H`$ implies $`[x,y]\in K`$ for all $`y`$. The identity $`[x,yz]=[x,z][x,y]^z`$ puts every conjugate of every $`[x,y]`$ in $`K`$. Core-freeness makes $`x\in Z(Y)=1`$. Finally any nuclear translation lying in $`D`$ centralizes it and hence is identity.

## 2. Two graph factors with exactly the prescribed normalizer residue

Let $`F_0=k^+\rtimes\langle z\rangle`$, $`k=\mathbb F_{11^3}`$, where $`z`$ acts by a primitive seventh root $`\zeta`$, and take primitive $`c\in k^\times`$. Then $`F_0'=k^+`$ and $`Z(F_0)=1`$. Define automorphisms

```math
a(x,z^j)=(x^{11},z^{4j}),\qquad
 \theta(x,z^j)=(c x^{11},z^{4j}),\qquad a_2=\theta a\theta^{-1}.
```

Here $`11\equiv4\bmod7`$; $`a,a_2`$ have order three and $`a_2(x)=c^{1-11}x^{11}`$ on $`k^+`$. Also $`\theta`$ fixes only the identity: the $`z`$-exponent must vanish and $`\theta^3`$ on $`k^+`$ is multiplication by $`c^{133}`$ of order ten. For $`i=1,2`$ the restriction of $`a_2^i a^{-i}`$ to $`k^+`$ is the scalar $`c^{1-11^i}`$ of order $`133`$, not any seventh-root scalar induced by an inner automorphism. This is an actual outer obstruction, not a count of graph sizes.

Let $`\Omega`$ be the underlying set of the target $`R`$, with $`R`$ acting regularly by left translation; $`B=F_0^\Omega`$. Apply the three automorphisms coordinatewise and denote the coordinatewise $`\theta`$ by $`\Theta`$. Define the auxiliary

```math
P=(B\times B)\rtimes(\langle s\rangle\times R),\quad |s|=3,
```

where $`s`$ acts by $`(a,a_2)`$ and $`R`$ permutes the sites **in the same manner on both copies**. These actions commute. Set

```math
S=\{(b,b):b\in B\},\quad T_0=\{(b,\Theta b):b\in B\},\quad
 T=T_0\rtimes(\langle s\rangle\times R).
```

Every pure top normalizes $`T_0`$ by the definition of $`a_2`$ and the constant-coordinate $`\Theta`$. The fixed-free $`\Theta`$ gives $`S\cap T=1`$; orders give $`ST=P`$. Since $`Z(B)=1`$, conjugating by $`(b,1)`$ forces the core of $`S`$ to be trivial. Each graph normalizes only itself in $`B^2`$, by centerlessness.

An element $`(x,y)s^i r`$ normalizing $`S`$ forces the automorphisms of the two wings to be equal after their respective inner conjugations. The common site permutation cancels in their relative automorphism. When $`i=1,2`$ the relative automorphism on each site is the preceding scalar obstruction, so not inner in $`B`$. For $`i=0`$ the two inner conjugations coincide precisely when $`x=y`$. Hence

```math
N_P(S)=S\rtimes R,\qquad N_P(S)/S=R
```

with the original multiplication of $`R`$ (the action on sites is faithfully left regular). Since $`T\cap B^2=T_0`$, normalization of $`T`$ forces preservation of $`T_0`$, whose normalizer in $`B^2`$ is itself, and all pure tops already belong to $`T`$. Thus $`N_P(T)=T`$.

In fact $`C_P(T_0)=1`$. To centralize the first projection of the graph pointwise, a putative $`(x,y)s^ir`$ would have to induce the identity on the first $`B`$. An inner automorphism cannot undo any moved direct factor, so regularity gives $`r=1`$. A nontrivial $`s^i`$ acts nontrivially on the abelianization of each $`F_0`$, unlike an inner map, so $`i=0`$. Then both $`x,y`$ must be central in $`B`$, hence trivial. Consequently $`Z(P)=1`$ and $`C_{P'}(T)=1`$; these are conclusions about the auxiliary $`P`$ even when $`Z(R)`$ is large.

We have $`P'=B^2\rtimes R'`$. The derived subgroup includes all the additive $`k^+`$ factors internally; on the remaining $`C_7`$ factors $`(s-1)`$ is multiplication by $`4-1=3`$, so each factor is filled. The pure top contributes exactly $`R'`$ and the quotient is abelian. The abstract quotient can even be seen on the **literal native nuclear marks**. Regard $`r\in R`$ as a pure top in $`P\le Y`$. Then $`d_r=(r,r^{-1})`$ normalizes $`H`$ since $`r\in N_P(S)`$ and $`r^{-1}\in T`$. Distinct $`r`$ give distinct $`H`$-cosets, since a pure $`R`$-element belongs to $`K`$ only at the identity. For $`r,t\in R`$ the discrepancy $`d_{rt}^{-1}d_r d_t=(1,rt r^{-1}t^{-1})`$ belongs to $`H`$: its second entry is in $`R'\le T`$ and its first is identity. Therefore the element represented by $`d_r`$ multiplied in the **native loop** by the one represented by $`d_t`$ is represented by $`d_{rt}`$. These are all nuclear elements by (1); the nonabelian multiplication has not been replaced by its commuting shadow.

The group $`P`$ is solvable by the odd-order theorem (or by extension from solvability of the given odd $`R`$); $`T`$ surjects onto $`P_{\mathrm{ab}}`$, thus normally generates $`P`$. If $`R`$ is the nonabelian group of order $`27`$ and exponent three, for example, $`R'`$ is a nontrivial central chief factor in the quotient by $`B^2`$: the older noncentral-chief restriction would not suffice. The weaker lemma above applies.

## 3. Faithful irreducible prime-field action, with only $`49n`$ weights

Choose $`\ell`$ as in the theorem. Such primes exist: take a prime divisor of $`\Phi_{11}(M)`$ with $`M`$ a sufficiently large multiple of $`3\cdot11\cdot n f_0`$ and all already excluded primes. The divisor is coprime to this $`M`$ and not eleven, so the multiplicative order of $`M`$ there is exactly eleven. In particular $`\ell`$ is odd. Fix an actual order-eleven scalar $`\xi\in\mathbb F_\ell^\times`$.

Write $`P=N\rtimes L`$ with $`N=(k^+\times k^+)^\Omega`$ and $`L=(C_7\times C_7)^\Omega\rtimes(C_3\times R)`$. This $`L`$ acts faithfully on $`N`$: any moved coordinate immediately detects $`r\ne1`$, and the two nonidentity Frobenius powers on the first additive field are not scalar maps, so independent seventh-root scalars cannot cancel them. At the identity site $`e\in R`$ define the character of $`N`$

```math
\lambda((x_j,y_j)_{j\in\Omega})
  =\xi^{\mathrm{Tr}_{k/\mathbb F_{11}}(x_e)
      +\mathrm{Tr}_{k/\mathbb F_{11}}(c^{-1}y_e)} .
```

This is nontrivial on each of the two local summands and fixed by $`s`$ since $`a_2=c a c^{-1}`$ on the second. Independent seventh-root scalars give precisely $`49`$ weights at the selected site, and the regular action puts them on each of the $`n`$ distinct sites, with disjoint supports. Thus its orbit has exactly $`49n`$, not $`49^n`$. The exponents span the whole $`6n`$-dimensional dual over $`\mathbb F_{11}`$: differences under one local scalar-seven subgroup give a nonzero form supported only on that one summand, and its orbit spans the irreducible local dual because $`\mathrm{ord}_7(11)=3`$. Repeat for the other wing and all sites.

On $`V=\mathbb F_\ell^{49n}`$ let $`N`$ act diagonally by the actual orbit characters, and $`L`$ permute their coordinates by the dual action. The semidirect relations follow from this weight action. Distinct weight projections exist over the **prime field** by ordinary character averaging on the elementary eleven-group; transitivity makes $`V`$ irreducible. The dual span proves faithfulness on $`N`$. Any kernel element must then centralize $`N`$, so its $`L`$-part is trivial by faithful action, and its remaining $`N`$-part is trivial by the same dual span. All hypotheses of (1) are now verified, the three calculated normalizer groups give precisely $`R`$, and the parameter sizes give the displayed degree.

**Controls and scope.** The [standalone checker](../code/verify_universal_odd_nucleus_graph_wreath.py) uses actual matrices for the two outer arrows, true site permutations and prime-field character actions at $`R=1,C_9,C_3^2,C_7\rtimes C_3`$ and the Heisenberg group of order $`27`$, along with a deliberately failing anti-diagonal central cut; [output](../checks/universal-odd-nucleus-graph-wreath.out). The [one-site field and top-cut checker](../code/verify_trivial_nucleus_normalizer_transfer.py) tests the complete local field group and all signed normal subgroups of smaller genuine models. No large loop table is claimed. The [1053 literature comparison](../nagy-comparison.md) separates FKP's arXiv v2 Corollary 6.24 from full right-nucleus nontriviality; our theorem includes the trivial group by positive construction, not by misusing that assertion. Nagy's factorization and G-loop theorem are explicit inputs. Nothing here purports to classify the loops themselves, their minimum degrees, or their occurrence in earlier undiscovered literature. The [independent checker](../code/check_native_nucleus_and_signed_tops.py) and [output](../checks/all-odd-groups-independent.out) test the group action independently; this is not human peer review or formal verification.

[Review and replication](../verification.md) · [Right nuclei](../README.md)
