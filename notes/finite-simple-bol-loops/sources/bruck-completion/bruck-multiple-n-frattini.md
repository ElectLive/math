# Two N Frattini factors over P₆ and projective shadows

**Theorem with scoped independent reviews, continuing of [0323:C0010](../../claims/0010.md).** In the faithful simple nonassociative Bruck-envelope setting of [the N-Frattini marked-rank source](bruck-n-frattini-marked-rank.md), suppose $`G/P\cong S_5`$, $`P`$ has class at most two and exponent at most four, and

```math
Z=\Phi(P)\cong N^2,\qquad V=P/Z\cong P_6\oplus U.
```

Conditional on the cited envelope, module and marked-fiber inputs and the finite calculation below, the conclusion is that no such envelope exists. The proof and certificate have the scoped exact-source reviews below. No quotient is assumed to be a folder; neither larger $`b`$ nor arbitrary multiple-$`N`$ layers are classified here.

The one-$`N`$ marked identity and fiber arguments are reviewed at the recorded source revision; their dimension proofs apply here with the new dimensions explicitly substituted below. The $`N`$-block classification is reviewed at the recorded source revision, and the fixed-component equation solver and paired module inputs are recorded in [the quadratic-support theorem](bruck-n-frattini-quadratic-support.md) at the recorded source revision. The invariant-functional pushout argument is reviewed in [the central-socle manuscript](bruck-n-central-socle-obstruction.md) at the recorded source revision; applying its proof with an arbitrary central $`N^a`$ as below is included in the present scoped reviews.

The original factorization P=(H intersect P)(K intersect P) makes tau the identity on V. It fixes Z as well: for a lift p, tau(p)=pz with z in the elementary central Frattini subgroup, so tau(p squared)=p squared, and squares generate Z. These observations apply to multiple N factors and do not use a split extension.

## A central actual-lift lemma for multiple N factors

The following lemma works for any $`a\ge1`$, not just two. Let $`Z\cong N^a`$, and let $`T\cong N^c`$ be an $`S_5`$-submodule of the shadow of $`W=H\cap P`$ that lies in the polar radical of the square map. Suppose a selected marked involution $`\lambda`$ over a transposition $`t`$ has

```math
\ell_\lambda|_{C_T(t)}=0.                                       \tag{1}
```

Then $`T=0`$.

Indeed, $`W\cap Z=0`$: every $`F_{20}`$-submodule of $`N^a`$ is a binary multiplicity subspace and is $`S_5`$-stable, since both endomorphism rings on $`N`$ are $`\mathbb F_2`$. Any nonzero such intersection would be a normal subgroup of $`G`$ contained in $`H`$, contrary to core-freeness. Because $`T`$ lies in the elementary $`W`$-shadow, $`q|_T=0`$. Its full preimage $`E_T\le P`$ is therefore elementary and central in $`P`$, and is an actual $`S_5`$-module with

```math
0\longrightarrow N^a\longrightarrow E_T\longrightarrow N^c\longrightarrow0.
```

The actual group $`W\cap E_T`$ maps isomorphically onto $`T`$. Together with $`Z`$ it spans $`E_T`$, so $`\tau`$, which fixes $`H`$ and $`Z`$, fixes $`E_T`$ pointwise. Equation (1) makes every vector of $`C_T(t)`$ lift to a $`\lambda`$-fixed vector. Hence the transposition rank on $`E_T`$ is $`a+c`$. On the other hand the reviewed $`N`$-block theorem writes

```math
E_T\cong U^s\oplus N^{a+c-2s},
```

whose transposition rank is $`a+c+2s`$. Thus $`s=0`$. Every $`F_{20}`$-submodule of $`N^{a+c}`$ is $`S_5`$-stable, so $`W\cap E_T`$ is normal in $`G`$. Core-freeness forces it to be trivial, proving the lemma.

## Necessary shadow dimensions and one zero marked component

Return to $`a=2`$, $`V=P_6\oplus U`$. As in the lemma, $`W\cap Z=0`$. For a transposition, $`\rho_V=\mathop{\mathrm{rank}}\nolimits(1+t)|_V=3+4=7`$, $`\rho_Z=2`$, and $`\dim V=14`$, $`\dim Z=8`$. The original selected-fiber capacity argument gives

```math
\rho_V+\rho_Z-1\le\dim W\le
 \dim V+\dim Z-\rho_V-\rho_Z-1,
```

so $`8\le\dim W\le12`$. The $`F_{20}`$-module $`V`$ has nonfixed multiplicity three and a two-dimensional fixed part. The invariant-functional pushout proof of the central-socle manuscript applies to $`V=P/\Phi(P)`$ with $`Z=N^2`$ as well: the kernel of any invariant functional is normal and contains $`Z`$, while the central $`C_2`$-by-$`S_5`$ quotient is split by the same $`F_{20}`$/transposition detection. Thus augmentation is nonzero on the $`W`$-shadow, forcing at least one fixed dimension. The capacity bounds leave exactly

```math
\dim W=9\text{ or }10,
```

with nonfixed $`F_{20}`$-multiplicity two.

For a selected $`\lambda`$, the original orbit-size bound gives $`\mathop{\mathrm{rank}}\nolimits\ell_\lambda\le3`$ in the first case and $`\le2`$ in the second. The marked identity defines a $`C_{S_5}(t)`$-equivariant map

```math
d:(1+t)V\longrightarrow C_Z(t)/(1+t)Z,
 \qquad d((1+t)v)=\beta(v,tv)+(1+t)Z.
```

Its target is two copies of the natural two-dimensional simple $`\mathbb F_2S_3`$-module, so its rank is even and at most $`\mathop{\mathrm{rank}}\nolimits\ell_\lambda`$. Hence its image is contained in one such copy. An $`S_5`$-automorphism of $`Z=N^2`$ therefore supplies a nonzero central projection $`Z\to N`$ on which the projected $`d`$ vanishes. This is a componentwise polar restriction; it does not construct a quotient folder.

## Finite elementary-shadow check

The [standalone certificate](../code/verify_bruck_two_n_one_u.py) solves the complete equivariant quadratic-map equations for $`P_6\oplus U\to N`$: the full space has dimension five, and its projected $`d=0`$ subspace has dimension three. It forms all ordered independent pairs $`(q_0,q_1)`$, with nonzero $`q_0`$ in the latter subspace. Independence is necessary because the square values generate $`Z=\Phi(P)`$; the span of those values is $`S_5`$-stable, and a linear dependency between coordinate maps would place it in a proper $`N`$-submodule.

The certificate derives the $`F_{20}`$-intertwiners and checks all seven binary two-planes in the nonfixed multiplicity space. It tests both augmentation-one fixed lines separately and their two-dimensional span. For each candidate it checks the two N-valued square maps on a basis and on every pair sum, which also checks their full polar forms on the shadow. In each of the three fixed-space tests, the only six ordered coefficient-pair presentations surviving all elementary-shadow equations have the same plane

```math
P_{6,S}\oplus\mathop{\mathrm{soc}}\nolimits(U)
```

and the same two-dimensional coordinate-map span

```math
\left\langle\mathop{\mathrm{top}}\nolimits(U),\ 
 \mathop{\mathrm{aug}}\nolimits(P_6)\mathop{\mathrm{top}}\nolimits(U)\right\rangle.        \tag{2}
```

The two $`N`$-coordinate maps may be changed by an invertible central basis change; (2) records their span, not a preferred order. The certificate independently checks augmentation times top on all $`64\cdot256`$ input pairs.

Its only imports are [the quadratic-support solver](../code/verify_bruck_n_quadratic_support.py), which itself imports [the P₆ Frattini model](../code/verify_bruck_p6_frattini.py) and [the one-M F20/action model](../code/verify_bruck_one_m_noncentral.py), and a direct import of that one-M model. It checks the finite shadow equations, not the existence or nonexistence of an actual extension by itself. From the repository root, with assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_two_n_one_u.py
```

The source author and root read and ran the certificate using bundled Python 3.12.14; it printed `P6 N² one-U elementary-shadow enumeration passed`. This is not independent review of the code or theorem.

## The actual-lift contradiction

Both generators in (2) satisfy the full marked polar condition $`d=0`$, and both have polar annihilating the entire $`U`$-socle. The surviving shadow contains $`T=\mathop{\mathrm{soc}}\nolimits(U)\cong N`$. Since

```math
C_T(t)\subseteq C_U(t)=(1+t)U\subseteq(1+t)V,
```

the marked identity and full $`d=0`$ imply $`\ell_\lambda|_{C_T(t)}=0`$. The multiple-$`N`$ central actual-lift lemma therefore gives $`T=0`$, a contradiction. This uses the actual subgroup $`W\cap E_T`$ and core-freeness in $`G`$, not a projected loop or a quotient-transversal assumption.

## Independent review

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted the multiple-N actual-lift lemma and the stated two-N/P6-plus-U exclusion, conditional on the pinned envelope, central-extension detection, N-block, marked identity and component inputs. All checked the generalized capacity and pushout, the initially single zero projected marked component, the complete elementary-shadow enumeration, and the original-group lift/core contradiction. All inspected the new certificate and its three previously reviewed imports, extracted the four files at the exact commit, and independently ran the certificate with the bundled Python 3.12 runtime; the folder and small-order reviewers specified 3.12.14. The expected elementary-shadow enumeration message passed. The finite calculation verifies representation/shadow identities; the mathematical reviews cover the conditional exclusion. No larger-b or arbitrary multiple-N classification, fresh primary-source audit or formal verification is claimed.

## A uniform two-N support reduction

**Continuation with scoped independent reviews below.** Retain the same envelope hypotheses but allow arbitrary $`b\ge0`$:

```math
Z\cong N^2,\qquad V\cong P_6\oplus U^b.
```

The pair restrictions and dual-number coordinates are from [the quadratic-support theorem](bruck-n-frattini-quadratic-support.md), and the actual passive-group cohomology interface is [the passive reduction](bruck-n-frattini-passive-reduction.md), both independently reviewed at the recorded source revision. Conditional on those and the cited marked-fiber and $`N`$-block inputs, there is an $`S_5`$-module coordinate change for which $`q`$ and $`\beta`$ are supported on $`P_6\oplus U^a`$, with

```math
a\le\min\{b,127\}.                                               \tag{3}
```

A further conditional group/involution reduction uses at most 129 active $`U`$-blocks. These are bounds on support and on the group with its marked involution, not on $`b`$; they do not split $`H`$ or $`K`$, prove transversality, or create a quotient folder. The uniform argument and constants have the scoped exact-source reviews below.

### Capacity and socle bounds

Let $`W=H\cap P`$, and let $`F=H/W\cong F_{20}`$. The same argument as above gives $`W\cap Z=0`$, and the invariant-functional pushout gives at least one fixed $`F`$-dimension in its shadow. Write $`w=4s+e`$, where $`e\in\{1,2\}`$. A transposition has $`\rho_V=3+4b`$ on $`V`$ and $`\rho_Z=2`$ on $`Z`$. The original selected-fiber inequalities give

```math
\rho_V+\rho_Z-1\le w\le\dim V+\dim Z-\rho_V-\rho_Z-1.
```

Substitution forces $`s=b+1`$. Thus the nonfixed $`F`$-shadow $`B`$ has multiplicity $`b+1`$.

Let $`T\cong N^c`$ be the actual shadow intersection with $`\mathop{\mathrm{soc}}\nolimits(U^b)`$. It is $`S_5`$-stable by the same binary multiplicity argument as in the central actual-lift lemma. Its preimage $`E_T`$ is elementary because $`T`$ is contained in the shadow of the elementary group $`W`$, even though $`q`$ need not vanish on the whole socle. Fix a selected $`\lambda`$ over $`t`$, put $`I=(1+t)Z`$, and let $`h=\mathop{\mathrm{rank}}\nolimits(\ell_\lambda|_{C_T(t)})`$. The displacement image $`D=(1+\lambda)E_T`$ projects onto $`(1+t)T`$, and $`\dim(D\cap Z)=2+h`$. Comparing the unique $`W`$-lifts over $`(1+t)T`$ with $`D`$ gives an injection

```math
(1+t)T\hookrightarrow Z/(D\cap Z),
```

as in the reviewed lifted-socle argument: a nonzero kernel would give an element of $`H\cap\Lambda^2`$. Consequently

```math
c\le6-h\le6.                                                      \tag{4}
```

This uses neither $`d=0`$ nor $`\ell_\lambda=0`$. If $`B_0=B\cap\{(P_6)_S=0\}`$, then $`\dim B_0\ge b`$. Its top image $`T_0\le\mathbb F_2^b`$ has codimension at most $`c`$, because the kernel is contained in the $`c`$-dimensional shadow-socle intersection.

### Isolating the nonlinear square row

The marked capacity bound, exactly as in the $`b=1`$ argument above, supplies a nonzero central projection $`Z\to N`$ for which the projected $`d`$-map vanishes. Choose $`N^2`$ coordinates so this is the first component. The reviewed fixed-component equations say that a $`d=0`$ square map on one $`U`$ is a multiple of top, while the full $`Q(U,N)`$ has dimension two. Restriction to $`\mathop{\mathrm{soc}}\nolimits(U)`$ is nonzero and its kernel is the top-linear line. Explicitly, realize $`N=\{a\in\mathbb F_2^5:\sum_i a_i=0\}`$ and $`U=N\oplus N`$, with odd permutations swapping the two factors. The map

```math
Q_{\rm extra}(a,b)=a*b+\bigl(\sum_i a_i b_i\bigr)\mathbf1,
```

where $`a*b`$ is coordinatewise multiplication. The displayed value has even coordinate sum; the map is quadratic, symmetric in $`a,b`$, and $`S_5`$-equivariant. On the socle it satisfies $`Q_{\rm extra}(a,a)=a`$, since $`\sum_i a_i=0`$. Top vanishes on the socle, so the reviewed dimension-two calculation proves that the kernel of restriction to the socle is exactly the top line.

All $`U`$-pair maps vanish on socle pairs. Hence $`q|_{\mathop{\mathrm{soc}}\nolimits(U^b)}`$ is encoded by a $`2\times b`$ binary row matrix whose first row is zero. A binary multiplicity change confines its possible nonzero second row to one reserved $`U`$-coordinate. On each other individual $`U`$-summand, both central square components are top-linear. Further coordinate changes confined to those remaining summands preserve this property.

Let $`D=\mathbb F_2^{b-1}`$ be the remaining multiplicity space, and put $`d=c+1`$. If no nonlinear row exists, one may still reserve a coordinate when $`b>0`$; the trivial small cases need no reservation. For each central component $`j=1,2`$, write the $`U`$-pair coefficient matrix on $`D`$ as

```math
C^{(j)}=C_0^{(j)}+\varepsilon C_1^{(j)},
```

alternating over $`\mathbb F_2[\varepsilon]/(\varepsilon^2)`$. Since $`T_0\cap D`$ has codimension at most $`d`$ in $`D`$, the reviewed independence of the two $`D_U\times D_U`$ restrictions, together with the fact that every top–socle graph correction lies in the $`\varepsilon`$-line, implies

```math
\mathop{\mathrm{rank}}\nolimitsC_0^{(j)}\le2d\quad(j=1,2).                \tag{5}
```

The reserved-coordinate socle components of a graph may contribute in the $`\varepsilon`$-line; they do not affect this residue-rank estimate.

### A common polar radical

Let $`K\le D`$ be the common radical of $`C_0^{(1)},C_0^{(2)}`$ on $`D`$, further intersected with the kernels of their pairings against the reserved coordinate. Then

```math
k=\mathop{\mathrm{codim}}\nolimits_D K\le4d+2.
```

Choose a complement $`H_0`$ of $`K`$ of dimension $`k`$. The extra reserved-coordinate conditions ensure that all $`C_0`$ graph corrections vanish for top vectors in $`K`$, including corrections involving the reserved socle. Applying the same isotropy argument to $`T_0\cap K`$, which has codimension at most $`d`$ in $`K`$, gives

```math
\mathop{\mathrm{rank}}\nolimits(C_1^{(j)}|_K)\le2d\quad(j=1,2).           \tag{6}
```

Now choose $`K'\le K`$ in the radicals of both restricted $`C_1`$ forms, in the kernels of their pairings with $`H_0`$, in the kernels of their pairings with the reserved coordinate, and in the kernels of both $`R`$-coordinates of each of the two $`P_6`$-to-$`U`$ cross rows. These conditions cost at most

```math
4d+2k+2+4=4d+2k+6
```

dimensions inside $`K`$. Therefore $`U\otimes K'`$ is polar-radical against all of $`V`$.

At this point $`q|_{U\otimes K'}`$ is an $`S_5`$-equivariant **linear** map, because its polar vanishes there. Each component of such a map $`U^{\dim K'}\to N`$ is a fresh binary row of top maps. Restrict to the common kernel of these two freshly computed rows, losing at most two additional coordinates. This order is necessary: an earlier binary coordinate change can alter the original top-square rows through quadratic diagonal corrections, so their original kernels are not used here. The resulting submodule $`Y`$ has $`q(Y)=0`$ and $`\beta(Y,V)=0`$, and its codimension among the $`U`$-coordinates is at most

```math
1+k+(4d+2k+8)\le16d+15=16c+31\le127.                       \tag{7}
```

A binary basis extending a basis of this submodule realizes (3). This proves the quadratic-support bound.

### Group and involution

The preimage of $`Y`$ in $`P`$ is elementary abelian and central in $`P`$. As an $`S_5`$-module it extends $`Y`$ by $`Z=N^2`$; projectivity of $`U`$ gives an equivariant complement $`Y_0`$. On this polar-radical preimage, $`p\mapsto\tau(p)p^{-1}`$ is an $`S_5`$-equivariant shear $`Y\to Z`$: the possible failure of equivariance elsewhere is a polar term, which vanishes on $`Y`$. Since $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(U,N^2)\cong\mathbb F_2^2`$, a passive multiplicity change confines the two shear rows to at most two further $`U`$-coordinates. Move those into the active part and retain the notation $`Y_0`$ for the remainder. Then $`\tau`$ fixes $`Y_0`$ pointwise and

```math
P=P_0\times Y_0,
```

where $`P_0/Z`$ has at most 129 $`U`$-summands.

The reviewed passive-group argument now applies with this $`Y_0`$: projectivity gives $`H^2(S_5,Y_0)=H^1(S_5,Y_0)=0`$, so $`G/P_0`$ has a complement to $`Y_0`$. The shear of $`\tau`$ on that complement is a principal derivation. Actual $`\tau`$-fixed $`H`$-lifts above $`F`$ make it vanish on $`F`$, and $`Y_0^F=0`$ makes it vanish globally. Its full preimage $`E`$ is $`\tau`$-stable and gives

```math
G=E\ltimes Y_0,\qquad E\cap P=P_0,\qquad\tau(E)=E,\quad\tau|_{Y_0}=1.
```

This proves the group/involution reduction conditional on the stated cohomology and actual-lift interfaces. It says nothing further about a decomposition of $`H`$, $`K`$, or the loop.

## Radical fiber and a relative-cohomology correction

Retain the original faithful simple Bruck-envelope hypotheses above with $`Z=\Phi(P)\cong N^2`$, $`V=P/Z\cong P_6\oplus U^b`$, and arbitrary $`b\ge0`$. Put $`W=H\cap P`$ and $`B=WZ/Z`$. Write $`q:V\to Z`$ for the square map and $`\beta`$ for its polar. The canonical involution $`\tau`$ fixes $`V`$ and $`Z`$ pointwise and fixes $`H`$ pointwise. The $`N`$-block, projectivity and Hom inputs used below are in [bruck-s5-module-blocks.md](bruck-s5-module-blocks.md) at exact reviewed source the recorded source revision; in particular $`U`$ is projective. The model $`P_6=\mathbb F_2[S_5/F]`$, with $`F\cong F_{20}`$, is the six-point permutation model used in [the one-U source](bruck-n-p6-one-u-exclusion.md) at the recorded source revision. The argument in this section has the scoped reviews below; it does not assume a quotient folder.

For $`p\in P`$ with shadow $`v=pZ`$, put $`\tau(p)=p\delta(v)`$. Because $`Z`$ is central elementary and fixed by $`\tau`$, this defines a linear map $`\delta:V\to Z`$, and $`\delta(B)=0`$. **It need not be $`S_5`$-equivariant.** For $`g\in S_5`$, choose a lift $`\widetilde g\in G`$ and set

```math
a(g)=\tau(\widetilde g)\widetilde g^{-1}Z\in V.
```

This is independent of the lift: replacing $`\widetilde g`$ by $`\widetilde g p`$ changes the displacement by a central element, because $`\tau(p)p^{-1}\in Z`$. It is a 1-cocycle $`S_5\to V`$, and $`a|_F=0`$, using actual $`H`$-lifts of $`F`$. Applying $`\tau`$ to $`\widetilde g p\widetilde g^{-1}`$ yields the exact defect formula

```math
\delta(gv)=g\delta(v)+\beta(a(g),gv).                     \tag{1}
```


The cohomology class of $`a`$ is zero. For $`U`$, projectivity and self-injectivity of the finite group algebra give $`H^1(S_5,U)=0`$. For $`P_6=\mathop{\mathrm{Ind}}\nolimits_F^{S_5}\mathbb F_2`$, Shapiro's isomorphism $`H^1(S_5,P_6)\cong H^1(F,\mathbb F_2)`$ is explicitly restriction to $`F`$ followed by evaluation at the $`F`$-fixed point. As $`a|_F=0`$, its image under this isomorphism is zero. Explicitly for the P6 component, define $`v_0(xF)=a(x)(xF)`$. This is independent of the coset representative because $`a(h)(F)=0`$ for $`h\in F`$; evaluating the cocycle identity at $`xF`$ gives $`a(g)(xF)=v_0(xF)+v_0(g^{-1}xF)`$, the required coboundary. Therefore there is $`v_0\in V`$ such that

```math
a(g)=v_0+gv_0\quad(g\in S_5).
```

The equality $`a|_F=0`$ gives $`v_0\in V^F=P_6^F`$. The $`F`$-fixed plane is spanned by the $`F`$-fixed singleton $`f`$ and the constant vector $`\mathbf1`$. The invariant-functional input above puts an augmentation-one $`F`$-fixed vector in $`B`$; using the reviewed coordinate normalization, take it to be $`f`$. Adding the $`S_5`$-fixed vector $`\mathbf1`$ does not change the displayed coboundary, so we may choose $`v_0\in\{0,f\}\subseteq B`$, regardless of whether the $`F`$-fixed part of $`B`$ has dimension one or two.

Define the auxiliary map

```math
\delta_0(v)=\delta(v)+\beta(v_0,v).
```

Equation (1) shows that $`\delta_0`$ is $`S_5`$-equivariant; this construction does not replace or modify the canonical $`\tau`$. Since $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(P_6,N)=0`$ and every $`S_5`$-map $`U\to N`$ is a scalar multiple of the top projection, $`\delta_0`$ kills $`\mathop{\mathrm{soc}}\nolimits(U^b)`$. Accordingly

```math
\delta(v)=\beta(v_0,v)\quad\text{for }v\in\mathop{\mathrm{soc}}\nolimits(U^b),\qquad v_0\in B. \tag{2}
```


The original radical factorization $`P=W(K\cap P)`$ gives a separate exact criterion for the existence of inverted lifts in every $`W`$-coset. An element over $`v`$ is inverted by $`\tau`$ exactly when $`q(v)+\delta(v)=0`$; this is independent of the central lift. Since $`q(B)=\delta(B)=0`$, the factorization implies

```math
\forall v\in V\quad\exists w\in B:\qquad q(v)+\delta(v)=\beta(v,w). \tag{3}
```

Conversely, if (3) holds, then each actual $`W`$-coset contains an inverted element: choose an inverted element over $`v+w`$, and adjust it by the required element of $`Z`$, which remains inverted. This converse concerns existence only; it does not construct a unique all-conjugate transversal or establish a folder.

By (2), (3) says $`q(v)\in\beta(v,B)`$ for every $`v\in\mathop{\mathrm{soc}}\nolimits(U^b)`$, and in particular

```math
q(v)=0\quad\text{for }v\in\mathop{\mathrm{soc}}\nolimits(U^b)\cap B^{\perp_\beta}. \tag{4}
```

Also $`q`$ vanishes on $`B`$, since $`W`$ is elementary. Neither (3) nor (4) proves that $`q`$ vanishes on the full $`U`$-socle, and no such conclusion is asserted. The relative-$`H^1`$ and fiber deductions have the scoped exact-source reviews below.

## Independent review of uniform support and relative cohomology

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted both appended deductions, conditional on the pinned envelope/fiber, N-block/projectivity, component/pair-map and invariant-functional inputs. All checked the c-at-most-six actual discrepancy without vanishing marked map, the explicit nonlinear component, both central polar forms with reserved-coordinate corrections, the freshly computed square rows, and the 127/129 bounds. They also checked equivariance only on the polar-central passive preimage, the actual group/involution splitting, the displacement cocycle and explicit relative-cohomology formula, the auxiliary corrected shear, and the existence-only radical-fiber criterion. No new computation or primary-source audit was required. Their scope does not include a stabilizer or section product, full socle-square vanishing, a quotient folder or a classification of the surviving envelopes.

## A bounded actual stabilizer with two N factors

**Continuation with the scoped independent reviews below.** Under the $`Z=N^2`$, $`V=P_6\oplus U^b`$ hypotheses and the group/involution splitting just reviewed at the recorded source revision, the actual stabilizer can also be confined to bounded active coordinates. More precisely, after an $`S_5`$-module automorphism of the passive factor and conjugation by a $`\tau`$-fixed passive element, there is a normal form

```math
G=E'\ltimes Y,\qquad H=H_0\ltimes T,\qquad
 \tau(E')=E',\quad\tau|_Y=1,                                      \tag{15}
```

where $`Y\cong U^s`$, $`H_0=H\cap E'`$, and $`T`$ is a direct sum of standard $`F_{20}`$-stable complements to $`\mathop{\mathrm{soc}}\nolimits(U)`$. The active shadow has at most 794 $`U`$-blocks, so

```math
|E'|\le120\cdot2^{6366}.                                        \tag{16}
```

The new deduction is an adaptation of the actual-stabilizer argument independently reviewed for the one-$`N`$ case at the recorded source revision; it is not covered by that earlier review. It does not split $`K`$, identify a quotient loop, or classify stabilizer or section orbits.

Start with the reviewed splitting

```math
G=E\ltimes Y_0,\quad P=P_0\times Y_0,\quad E\cap P=P_0,
 \quad\tau(E)=E,\quad\tau|_{Y_0}=1,
```

where $`P_0/Z\cong P_6\oplus U^a`$, $`a\le129`$, and $`Y_0\cong U^s`$, with $`b=a+s`$. Write $`W=H\cap P`$, $`F=H/W\cong F_{20}`$, and $`S=N|_F`$. The nonfixed $`F`$-multiplicity in $`W`$ is $`b+1=a+s+1`$, because $`W\cap Z=0`$. Let $`c_0`$ be the multiplicity in $`(W\cap Y_0)\cap\mathop{\mathrm{soc}}\nolimits(Y_0)`$; by the reviewed two-$`N`$ bound it is at most 6.

Choose an $`F`$-stable complement to $`\mathop{\mathrm{soc}}\nolimits(U)`$, and write

```math
Y_0|_F\cong S\otimes(D_{\rm soc}\oplus D_{\rm top}),
 \qquad D=\mathbb F_2^s.
```

An $`S_5`$-automorphism $`g+\varepsilon h`$ acts on multiplicities by $`(x,y)\mapsto(gx+hy,gy)`$. It extends to an automorphism of $`G=E\ltimes Y_0`$ fixing $`E`$ and commuting with $`\tau`$.

The projection $`\mathop{\mathrm{pr}}\nolimits_{P_0}:W\to P_0`$ is a group homomorphism with kernel $`W\cap Y_0`$. Both actual projection image and kernel carry the $`F`$-action: $`Y_0`$ centralizes $`P_0`$, and $`W`$ is abelian. The image is elementary abelian. Its shadow in $`P_0/Z`$ has at most $`1+2a`$ nonfixed copies of $`S`$, while its intersection with $`Z\cong N^2`$ can add two more. Thus its nonfixed multiplicity is at most $`2a+3`$. This is a statement about the actual projection, including possible central graph coordinates; the kernel of the shadow projection need not equal $`W\cap Y_0`$.

Write $`W\cap Y_0=S\otimes L`$, with $`L\le D\oplus D`$, and define

```math
A=\{x:(x,0)\in L\},\qquad B=\mathop{\mathrm{pr}}\nolimits_{\rm top}L.
```

Then $`\dim A=c_0`$, and the preceding multiplicity bound gives

```math
\dim L\ge s-a-2,\qquad \mathop{\mathrm{codim}}\nolimits_D B\le a+c_0+2.
                                                                    \tag{17}
```

An $`\varepsilon`$-shear straightens $`L`$ to $`A\oplus B`$: lift its graph $`B\to D/A`$ linearly and extend that lift to $`D`$.

Choose $`F`$-equivariant lifts in $`W`$ of the $`S`$-part of its actual projection image in $`P_0`$. The simple $`S`$ is projective as an $`F`$-module, so such lifts exist; there are at most $`2a+3`$ copies. Their passive coordinates use at most $`2(2a+3)`$ vectors of $`D`$. The $`F`$-fixed part of $`W`$ has zero passive projection, since $`Y_0^F=0`$. Choose $`Q\le D`$ containing $`A`$, a complement to $`B`$, and these coordinate vectors. Then

```math
\dim Q\le c_0+(a+c_0+2)+2(2a+3)
 =5a+2c_0+8\le665.                                               \tag{18}
```

Because $`B+Q=D`$, choose $`D'\le B`$ complementary to $`Q`$. The resulting decomposition $`Y_0=Y_{\rm exc}\oplus Y`$ gives the actual subgroup equality

```math
W=W_{\rm core}\oplus T,\qquad
 W_{\rm core}\le P_0\times Y_{\rm exc},\qquad
 T=S\otimes(0\oplus D')\le Y.                                    \tag{19}
```

In particular all central graph coordinates in the actual $`P_0`$-projection remain in $`W_{\rm core}`$.

Set $`E'=E\ltimes Y_{\rm exc}`$. Projecting $`H`$ to $`F\ltimes(Y/T)`$ gives a complement, since (19) makes its intersection with the kernel trivial. Its graph is a 1-cocycle; $`H^1(F,Y/T)=0`$ because $`Y/T`$ is a direct sum of copies of the projective $`F`$-simple $`S`$. Conjugation by a suitable element of $`Y`$ kills this cocycle. That element is fixed by $`\tau`$, and $`Y`$ centralizes $`P`$, so the group and involution splitting are preserved and (15) follows. The total active number is at most $`a+\dim Q\le794`$. Since $`P_0'=O_2(E')`$ has order at most $`2^{6+8\cdot794+8}=2^{6366}`$ and $`E'/P_0'\cong S_5`$, (16) follows. The original section and all conjugate-transversal conditions remain to be imposed in $`G`$.

## Independent review of the actual two-N stabilizer

Independent checks an independent check, an independent check and an independent check independently accepted the bounded actual-stabilizer deduction at exact source the recorded source revision, conditional on the reviewed two-N support/group-involution splitting and cited module, projectivity and envelope inputs. All checked the actual projection including its possible two central S copies, equivariant lifts with both passive coordinates, shear and direct-sum construction, and the τ-fixed H¹ conjugation. The arithmetic bounds 665 additional and 794 total active blocks, and 120·2^6366 for the active group, were checked. No new computation, section product, label classification or quotient-loop claim is included.

## A quadratic socle bound without vanishing marked map

**Continuation with the scoped independent reviews below.** Retain the original faithful simple Bruck-envelope hypotheses, with $`P`$ of class at most two and exponent at most four, $`G/P\cong S_5`$, $`Z=\Phi(P)\cong N^a`$, and $`V=P/Z\cong P_6\oplus U^b`$. Let $`c`$ be the multiplicity of the $`W`$-shadow intersection with $`\mathop{\mathrm{soc}}\nolimits(U^b)`$, and let $`\lambda`$ be a selected marked involution above a transposition $`t`$. If $`r=\mathop{\mathrm{rank}}\nolimits\ell_\lambda`$, the proposed necessary bound is

```math
c\le\left\lfloor\frac{3a-r}{2}\right\rfloor.                    \tag{20}
```

No vanishing of $`d`$ or $`\ell_\lambda`$ is assumed. The marked map and original fiber interfaces are as in [the marked-rank theorem](bruck-n-frattini-marked-rank.md), at the recorded source revision; the actual elementary-lift and discrepancy interfaces are in its lifted-socle section at the recorded source revision. The two-$`N`$ group and stabilizer bounds above have independent reviews recorded at the recorded source revision. This multiple-$`N`$ quadratic deduction has the exact-source reviews recorded below.

Let $`W=H\cap P`$, and write $`T\cong N^c`$ for the shadow intersection with $`\mathop{\mathrm{soc}}\nolimits(U^b)`$. As above, $`W\cap Z=1`$, and $`T`$ is $`S_5`$-stable by the binary $`F_{20}`$-multiplicity argument. Its full preimage $`E_T\le P`$ is elementary: $`W`$ supplies unique elementary lifts and $`Z`$ is central elementary. This does not assume that the square map vanishes on the whole $`U`$-socle. Put $`\alpha=\mathop{\mathrm{Int}}\nolimits(\lambda)|_P`$ and

```math
D(p)=p^{-1}\alpha(p),\qquad I=(1+t)Z.
```


The subgroup $`F_t=\pi^{-1}(C_V(t))\le P`$ has the following important property: $`D(F_t)`$ is a subgroup of $`Z`$, and every one of its elements is the displacement of a single element of $`F_t`$. Indeed each $`D(q)`$ is central when $`\overline q\in C_V(t)`$, and the class-two identity

```math
D(pq)=D(p)D(q)[D(p),q]                                         \tag{21}
```

makes $`D|_{F_t}`$ a homomorphism. Put $`J_t=D(F_t)`$. It contains $`I=D(Z)`$, and $`J_t/I=\mathop{\mathrm{im}}\nolimits\ell_\lambda`$; hence

```math
\dim J_t=a+r,\qquad \dim Z/J_t=3a-r.                            \tag{22}
```

Because $`P_6`$ and $`U`$ both restrict freely to $`\langle t\rangle`$, $`C_V(t)=(1+t)V`$. Therefore, for every $`m\in C_T(t)`$,

```math
\beta(m,C_V(t))\subseteq I: \quad
 \beta(m,(1+t)v)=(1+t)\beta(m,v).                                \tag{23}
```


Put $`C=C_T(t)`$ and $`R=(1+t)T`$. Their dimensions are $`3c`$ and $`c`$, and $`C\subseteq(1+t)V`$. For each $`m\in C`$, let $`w_m\in W\cap E_T`$ be its unique lift and choose $`p_m\in P`$ with $`(1+t)\overline{p_m}=m`$. Define

```math
\Delta(m)=w_mD(p_m)+J_t\in Z/J_t.                               \tag{24}
```

This is well-defined: changing $`p_m`$ by an element of $`F_t`$ changes its displacement by an element of $`J_t`$, and the commutator correction in (21) is in $`I`$ by (23). The $`W`$-lift map is linear because $`W`$ is elementary and $`W\cap Z=1`$. Since $`E_T`$ is elementary, the polar of $`\Delta`$ is

```math
B_\Delta(m,n)=\beta(m,\overline{p_n})+J_t.                      \tag{25}
```

It is bilinear and independent of the chosen preimage by (23). Its diagonal lies in $`J_t`$: the marked identity identifies $`\beta(v,tv)+I`$ with $`\ell_\lambda((1+t)v)`$, even when this value is nonzero. Its sum with its transpose is zero because it equals $`(1+t)\beta(\overline{p_m},\overline{p_n})+\beta(m,n)`$ modulo $`J_t`$, and $`\beta(T,T)=0`$. Thus $`\Delta`$ is quadratic.

If $`\Delta(m)=0`$, choose $`q\in F_t`$ with $`D(q)=w_mD(p_m)`$, which is possible because this element lies in the **actual displacement subgroup** $`J_t`$. By (21), $`D(p_mq)`$ equals $`w_m`$ up to a commutator in $`I`$; since $`I=D(Z)`$, a further central adjustment makes the displacement exactly $`w_m`$. For nonzero $`m`$, this gives a nonidentity element of $`H\cap\Lambda^2`$, contrary to the original folder transversality. Hence $`\Delta`$ has no nonzero zero.

The polar of $`\Delta`$ vanishes on $`R\times C`$. Indeed, if $`m=(1+t)u`$ with $`u\in T`$, then by equivariance and $`\beta(T,T)=0`$,

```math
\beta(m,\overline{p_n})
 =\beta(u,(1+t)\overline{p_n})=\beta(u,n)=0\pmod I.
```

Consequently $`\Delta|_R`$ is linear and injective. Its image is a $`c`$-dimensional subspace of $`Z/J_t`$. Modding out by that image induces a quadratic map on the $`2c`$-dimensional space $`C/R`$, with target dimension $`3a-r-c`$, and with no nonzero zero. If $`2(3a-r-c)<2c`$, this is impossible: for $`k`$ binary quadratic coordinate functions in more than $`2k`$ variables, the product of their zero indicators has degree below the number of variables, so its sum over the vector space is even; the origin is a zero, so another exists. This proves (20) without a quotient-folder argument.

## Tighter two-N active bounds

For $`a=2`$, (20) gives $`c\le3`$, independently of the value of $`r`$. In the already reviewed uniform-support proof above, retaining its notation and recomputing its conservative estimate with this new value gives

```math
a_{\rm quad}\le16c+31\le79,\qquad
 a_{G,\tau}\le81.                                                 \tag{26}
```

The reviewed actual-stabilizer estimate then gives at most

```math
a_{G,\tau,H}\le6\cdot81+2\cdot3+8=500
```

active $`U`$-blocks and

```math
|E|\le120\cdot2^{6+8\cdot500+8}=120\cdot2^{4014}.             \tag{27}
```

The earlier reviewed 127/129/794 bounds and their review records remain valid independently of this proposed improvement. With the scoped review of (20) below, the separate structural section transport at source the recorded source revision applies with the smaller active bound (27), without changing its original-section, core, generation or simplicity formulas. The new bound and its corollaries have the scoped reviews below.

## Independent review of the quadratic bound

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted the generalized quadratic socle bound and tighter two-N corollary, conditional on the pinned marked-fiber, actual-lift, module, folder and support/stabilizer inputs. All checked that J_t consists of actual single displacements, the class-two correction and choice independence, the quadratic polar including its nonzero-marked-map diagonal, the actual collision adjustment, the injective restriction to R, and the binary common-zero parity argument. They checked the 79/81/500 and 120·2^4014 bounds. The general statement is limited to P6 plus U-blocks and central N^a; it assumes neither whole-socle square vanishing nor a quotient loop. No new computation or fresh primary-source audit was claimed.

