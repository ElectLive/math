# Polynomial active support for multiple N Frattini factors

**Theorem with scoped independent reviews, continuing [0323:C0010](../../claims/0010.md).** Let $`(G,H,K)`$ be the faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. Assume $`G/P\cong S_5`$, $`P=O_2(G)`$ has class at most two and exponent at most four, and

```math
Z=\Phi(P)\cong N^a,\qquad V=P/Z\cong P_6\oplus U^b,
 \qquad a\ge1.
```

Put $`C(a)=\lfloor3a/2\rfloor`$ and define

```math
\begin{aligned}
 B(a)&=4a+2a(a+2)(C(a)+a)+a^2(a+2),\\
 H(a)&=6B(a)+9a+2C(a)+2.
\end{aligned}                                                     \tag{1}
```

The conclusion is an $`S_5`$-coordinate system in which $`q`$ and $`\beta`$ are supported on $`P_6\oplus U^{\min(b,B(a))}`$, followed by an actual normal form

```math
G=E\ltimes Y,\qquad H=H_0\ltimes T,\qquad
 \tau(E)=E,\quad \tau|_Y=1,                                      \tag{2}
```

where $`Y\cong U^s`$, $`T`$ is a direct sum of the standard $`F_{20}`$-stable complements to the $`U`$-socles, $`H_0=H\cap E`$, and the active group uses at most $`\min(b,H(a))`$ $`U`$-blocks. In particular

```math
|E|\le120\cdot2^{6+4a+8H(a)},\qquad
 H(a)\le36a(a+1)^2+2.                                           \tag{3}
```

These are polynomial bounds on the number of active module blocks, not on $`b`$ or the passive multiplicity $`s`$. They do not split the original section $`K`$, classify label orbits, or assert a quotient loop. The generalization in this manuscript has the exact-source reviews recorded below.

The marked-fiber and paired module inputs are those of [the marked-rank source](bruck-n-frattini-marked-rank.md), reviewed at the recorded source revision. The arbitrary-$`a`$ quadratic socle bound $`c\le\lfloor3a/2\rfloor`$ is independently accepted at the recorded source revision. The $`U`$-component and pair restrictions are reviewed in [the quadratic-support source](bruck-n-frattini-quadratic-support.md) at the recorded source revision; the two-$`N`$ support and group/involution construction is reviewed at the recorded source revision. The structural original-section transport in [the section manuscript](bruck-n-frattini-sections.md) is recorded at the recorded source revision. The proofs below state the changes needed for arbitrary $`a`$; the cited two-$`N`$ reviews do not themselves certify them.

## Marked capacity and the top shadow

Let $`W=H\cap P`$, and let $`F=H/W\cong F_{20}`$. Core-freeness gives $`W\cap Z=1`$: every $`F`$-submodule of $`N^a`$ is $`S_5`$-stable, since $`S=N|_F`$ is simple and both endomorphism rings are $`\mathbb F_2`$. Write

```math
w=\dim W=4m_W+e,\qquad 0\le e\le2,
```

where $`m_W`$ is the nonfixed $`F`$-multiplicity. A transposition has ranks $`4b+3`$ on $`V`$ and $`a`$ on $`Z`$. The original marked-fiber capacity inequalities give

```math
4b+a+2\le w\le4b+3a+2.                                          \tag{4}
```

The lower inequality and $`e\le2`$ imply $`m_W\ge b+\lceil a/4\rceil`$. Thus the intersection of the nonfixed $`W`$-shadow with the zero $`(P_6)_S`$-coordinate has multiplicity at least $`b`$. If $`c`$ is the socle-intersection multiplicity, its image $`T_0`$ in the $`U`$-top multiplicity space $`\mathbb F_2^b`$ has codimension at most $`c`$; the accepted quadratic collision gives

```math
c\le C(a).                                                       \tag{5}
```


## Simultaneous quadratic support

For one $`U`$, the reviewed space $`Q(U,N)`$ has dimension two. Restriction to $`\mathop{\mathrm{soc}}\nolimits(U)`$ has kernel the top-linear line: the explicit second map in [the two-$`N`$ source](bruck-multiple-n-frattini.md#a-uniform-two-n-support-reduction) restricts to the identity on the socle. All $`U`$-pair maps vanish on socle pairs. Hence $`q|_{\mathop{\mathrm{soc}}\nolimits(U^b)}`$ is an $`a\times b`$ binary matrix. A binary multiplicity change confines its row support to $`h\le a`$ reserved coordinates. On every remaining individual $`U`$-summand, all $`a`$ square components are top-linear. No projection of the full marked map is assumed to vanish.

Let $`D=\mathbb F_2^{b-h}`$ be the remaining multiplicity space and put $`d=c+h`$. On $`D`$, write the $`j`$-th $`N`$-component of the alternating $`U`$-pair matrix as

```math
C^{(j)}=C_0^{(j)}+\varepsilon C_1^{(j)},\qquad j=1,\ldots,a.
```

The top subspace $`T_0\cap D`$ has codimension at most $`d`$ in $`D`$. The reviewed independence of the two top–top pair restrictions, with all top–socle graph corrections in the $`\varepsilon`$-line, makes $`T_0\cap D`$ isotropic for each $`C_0^{(j)}`$. Hence

```math
\mathop{\mathrm{rank}}\nolimitsC_0^{(j)}\le2d.                               \tag{6}
```

Let $`K_0`$ be the common radical of these forms on $`D`$, further intersected with the kernels of their pairings against all $`h`$ reserved coordinates. Then

```math
k=\mathop{\mathrm{codim}}\nolimits_D K_0\le2ad+ah.                          \tag{7}
```

Choose a complement of dimension $`k`$. The extra reserved-coordinate conditions ensure that all residue graph corrections vanish on $`K_0`$, including corrections involving reserved socle coordinates. Applying isotropy to $`T_0\cap K_0`$ therefore gives

```math
\mathop{\mathrm{rank}}\nolimits(C_1^{(j)}|_{K_0})\le2d\quad(j=1,\ldots,a). \tag{8}
```


Inside $`K_0`$, impose the following linear conditions: lie in the radical of each restricted $`C_1^{(j)}`$; pair trivially under each $`C_1^{(j)}`$ with the $`k`$-dimensional complement and the $`h`$ reserved coordinates; and lie in the kernel of both binary $`R=\mathbb F_2[\varepsilon]/(\varepsilon^2)`$ coordinates of each $`P_6`$-to-$`U`$ cross row. These lose at most $`2ad+ak+ah+2a`$ dimensions. The resulting $`S_5`$-submodule of the $`U`$-part is polar-radical against all of $`V`$.

Only now restrict the square map to that polar radical. It is additive and $`S_5`$-equivariant; $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(U,N^a)`$ consists of $`a`$ binary top rows. Compute those rows **after** the preceding changes and pass to their common kernel, losing at most $`a`$ further coordinates. This gives an $`S_5`$-submodule $`Y\cong U^s`$ with $`q(Y)=0`$ and $`\beta(Y,V)=0`$. The number of retained coordinates is at most

```math
h+k+2ad+ak+ah+3a
 \le h+(a+1)(2ad+ah)+2ad+ah+3a\le B(a),                       \tag{9}
```

using $`h\le a`$, $`d=c+h\le C(a)+a`$. In particular (9) uses freshly computed linear square rows: the original rows can change by quadratic diagonal corrections under multiplicity changes. This proves the quadratic-support bound.

## Actual group, involution and stabilizer

The preimage of $`Y`$ in $`P`$ is elementary and central in $`P`$. Projectivity of $`U`$ gives an $`S_5`$-equivariant complement to $`Z=N^a`$. On this polar-central preimage the canonical $`\tau`$-shear $`Y\to Z`$ is $`S_5`$-equivariant, although the global shear on $`V`$ need not be. Its $`a`$ binary top rows can be confined to at most $`a`$ further $`U`$-coordinates. Moving those to the active part and using the projective $`H^2/H^1`$ and actual $`\tau`$-fixed $`H`$-lift argument of the reviewed passive reduction gives

```math
G=E_0\ltimes Y_0,\quad P=P_0\times Y_0,\quad
 \tau(E_0)=E_0,\quad\tau|_{Y_0}=1,
```

with $`Y_0\cong U^{s_0}`$ and $`P_0/Z\cong P_6\oplus U^A`$, where $`A\le\min(b,B(a)+a)`$. This is an actual group/involution splitting, not a product statement for $`H`$ or $`K`$.

For the stabilizer, write $`b=A+s_0`$, $`m_W=b+\delta`$ for the nonfixed multiplicity of $`W`$, and let $`c_0\le c`$ be the socle-intersection multiplicity of $`W\cap Y_0`$. Equation (4) gives $`\delta\ge\lceil a/4\rceil\ge1`$. The actual projection $`W\to P_0`$ has nonfixed multiplicity at most $`(1+2A)+a`$: the last $`a`$ copies are possible central graphs in $`Z`$ and are not discarded. Hence the top multiplicity of $`W\cap Y_0`$ has codimension at most

```math
A+a+c_0+1-\delta.
```

The $`\varepsilon`$-shear and actual projection-lift argument reviewed for the two-$`N`$ stabilizer now gives an exceptional passive subspace of dimension at most

```math
c_0+(A+a+c_0+1-\delta)+2(2A+a+1)
 \le5A+3a+2c_0+2.                                               \tag{10}
```

It contains the pure socle part, a top complement and the passive coordinates of actual $`F`$-equivariant lifts of the active projection, including its central graphs. The remaining standard top complements lie literally in $`W`$. As in the reviewed proof, projectivity of the $`F`$-simple $`S`$ gives $`H^1(F,Y/T)=0`$, so a $`\tau`$-fixed passive conjugation removes the passive $`H/W`$ cocycle and yields (2).

Combining (10) with $`A\le B(a)+a`$ and $`c_0\le C(a)`$ gives the active $`H(a)`$ bound. Since the active 2-group has shadow dimension at most $`6+8H(a)`$ and center layer dimension $`4a`$, (3) follows. The final elementary upper bound follows by $`C(a)\le3a/2`$.

## Original-section applicability

Under (2), the structural hypotheses used in [the original-section and simplicity test](bruck-n-frattini-sections.md#structural-applicability-to-the-two-n-normal-form) are unchanged: the passive module is $`U^s`$, $`T`$ is its standard $`F`$-complement, the original marked-image theorem applies, and $`E`$ is finite with $`E/O_2(E)\cong S_5`$. Its section/collision conditions, core and generation tests, and normal-subgroup $`(S,L,f)`$ formulas therefore transport with $`L`$ ranging over normal subgroups of this arbitrary-$`a`$ active group and the active bound replaced by (3). This is the same structural use as the two-$`N`$ transport, not a claim that the original section splits or that the remaining label and isomorphism problems have been solved.

## Independent mathematical review

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted the full manuscript, conditional on the pinned marked-fiber, socle-bound, fixed-component, projectivity and original-section inputs. All checked the arbitrary-a capacity and top shadow, nonlinear socle reservation without vanishing marked map, simultaneous residue/epsilon rank bounds with reserved and complementary pairings, freshly recomputed square rows, and B(a). They checked the actual group/involution splitting, all a central graph copies in the actual stabilizer projection, H(a) and its cubic upper bound, active-group order and structural section transport. No new computation or primary-source audit was claimed. The result bounds active module blocks only; it does not bound b or the passive multiplicity, split K, or solve the remaining section and isomorphism constraints.

<a id="proposed-extension-to-the-j-principal-shadow"></a>
## Extension to the J principal shadow

**Appendix with the scoped independent reviews below.** The main theorem and its the recorded source revision review remain stated for $`P_6`$. Suppose instead that all the same envelope hypotheses hold with

```math
V=P/Z\cong J\oplus U^b,\qquad Z=\Phi(P)\cong N^a.
```

The conclusion is the same quadratic-support bound $`B(a)`$ and the same actual $`G,\tau,H`$ active-block bound $`H(a)`$ in (1), with

```math
|E|\le120\cdot2^{5+4a+8H(a)}.                                  \tag{11}
```

The base dimension is five rather than six. The $`J`$ deduction has the exact-source reviews below; it neither changes the reviewed $`P_6`$ theorem nor asserts a quotient folder or a product for $`K`$.

### The quadratic socle bound for J

Let $`T\cong N^c`$ be the actual $`W`$-shadow intersection with $`\mathop{\mathrm{soc}}\nolimits(U^b)`$, and fix a selected marked involution $`\lambda`$ above $`t`$. The proof of the arbitrary-$`a`$ $`P_6`$ quadratic bound at the recorded source revision uses the freeness $`C_V(t)=(1+t)V`$ to establish

```math
\beta(C_T(t),C_V(t))\subseteq I=(1+t)Z.                        \tag{12}
```

Although $`J|_{\langle t\rangle}`$ need not be free, (12) remains valid. The $`U`$-fixed part is $`(1+t)U^b`$, and for $`tm=m`$, equivariance gives $`\beta(m,(1+t)u)=(1+t)\beta(m,u)`$. The **full unrestricted** $`S_5`$-space $`\mathop{\mathrm{Hom}}\nolimits(J\otimes U,N)`$ is one-dimensional, generated by augmentation on $`J`$ times top on $`U`$; hence every $`J`$-to-$`U`$ cross map annihilates the $`U`$-socle, including against all of $`C_J(t)`$. This is the full-space component calculation, prior to imposing $`d=0`$, in [the quadratic-support source](bruck-n-frattini-quadratic-support.md#fixed-components), reviewed at the recorded source revision, and its linked [fixed-component verifier](../code/verify_bruck_n_quadratic_support.py).

Also $`C_T(t)\subseteq(1+t)U^b`$ because $`U|_{\langle t\rangle}`$ is free. These are the two points needed to transport the actual-displacement proof: with $`I=(1+t)Z`$, the subgroup of actual displacements of elements above $`C_V(t)`$ has dimension $`a+\mathop{\mathrm{rank}}\nolimits\ell_\lambda`$; the quadratic discrepancy on $`C_T(t)`$, scalarized by its injective image on $`(1+t)T`$, has no nonzero zero. The same parity argument therefore gives

```math
c\le\left\lfloor\frac{3a-\mathop{\mathrm{rank}}\nolimits\ell_\lambda}{2}
 \right\rfloor\le\left\lfloor\frac{3a}{2}\right\rfloor.       \tag{13}
```

No vanishing of $`d`$, of $`\ell_\lambda`$, or of $`q`$ on the whole $`U`$-socle is assumed. The preimage of $`T`$ is elementary because $`T`$ lies in the shadow of the actual elementary subgroup $`W`$, exactly as in the cited proof.

### Capacity, support and actual stabilizer

The original marked-fiber capacity argument depends only on dimensions and transposition ranks. With $`\rho_J=2`$, $`\rho_U=4`$, and $`\rho_Z=a`$, it gives

```math
4b+a+1\le w\le4b+3a+2.                                        \tag{14}
```

Writing $`w=4s+e`$, with $`0\le e\le1`$ the $`F_{20}`$-fixed dimension on $`J`$, the lower bound gives $`s\ge b+\lceil a/4\rceil`$. Thus the intersection of the nonfixed $`W`$-shadow with the zero $`J_S`$-coordinate has multiplicity at least $`b`$, and its top image has codimension at most $`c`$. This lower-top conclusion does not require a mandatory fixed-vector assumption.

The unrestricted $`U`$-square and $`U`$-pair component spaces and their $`F_{20}`$ restrictions are identical to those used in the main theorem. The only changed mixed term is smaller: the full $`J`$-to-$`U`$ space is one binary row per central component, so the main proof's allowance of $`2a`$ binary mixed-row constraints remains conservative. With (13) in place, the same isolation of the nonlinear socle rows, simultaneous residue and $`\varepsilon`$-form rank bounds, reserved-coordinate pairings, and freshly recomputed linear square rows give support on at most $`B(a)`$ $`U`$-blocks. No full $`d=0`$ projection is used in that argument.

The passive preimage is polar-central and elementary; projectivity of $`U`$, the $`\tau`$-shear calculation on that preimage and the $`H^2/H^1`$ argument give the same actual group/involution splitting with at most $`B(a)+a`$ active blocks. For the stabilizer step, the nonfixed multiplicity of $`W`$ is $`b+\delta`$ with $`\delta\ge\lceil a/4\rceil\ge1`$. Its **actual** projection to the active 2-group has at most $`1+2A+a`$ nonfixed simple factors: the final $`a`$ account for possible central graphs in $`Z=N^a`$. Thus the same $`F_{20}`$-equivariant lift, graph-straightening and $`H^1(F_{20},S)=0`$ normalization gives (2) with at most $`H(a)`$ active blocks. The passive conjugation is $`\tau`$-fixed; the original section and all its transversality conditions remain in $`G`$.

Finally, the structural original-section, core/generation and normal-triple formulas cited above use the passive $`U/F_{20}`$ complement and the actual normal form, not the dimension of the active principal summand. They therefore apply conditionally with $`P_0/Z\cong J\oplus U^A`$ and bound (11), with the separate scoped review of the $`J`$ transport below. They do not solve the passive label, simplicity or isomorphism-orbit tests.

## Independent review of the J extension

Independent checks an independent check, an independent check and an independent check independently accepted the separate J appendix at exact source the recorded source revision, conditional on the full unrestricted J–U component identification, marked-fiber and actual-lift inputs and the reviewed P6 support/section arguments. They checked that socle annihilation replaces transposition freeness precisely where required in the discrepancy proof, the J capacity and top-shadow bound, conservative mixed-row count, actual group/stabilizer transport including central graphs, and base dimension five in the group-order bound. This review preserves the separate P6 provenance and does not classify the remaining sections or assert a product for K. No new computation or primary-source audit was claimed.

