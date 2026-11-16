# Nonsplit extension lifts and a fixed-vector bound

**Scoped continuation of [0323:C0010](../../claims/0010.md).** The algebraic realization below concerns groups and specified module actions; it does not construct a Bruck envelope. The marked bound additionally assumes the original faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. The split-extension and odd-multiplicity exclusions are independently accepted at the recorded source revision, conditional on their stated inputs. They leave the even-multiplicity nonsplit branch open.

Write $`Q=S_5`$, $`F=F_{20}`$, and use the modules $`P_6,U,N`$ of [the module-block source](bruck-s5-module-blocks.md), reviewed at the recorded source revision. In particular $`P_6=\mathop{\mathrm{Ind}}\nolimits_F^Q 1`$ is self-dual, $`U`$ is self-dual projective, and $`N|_F`$ is projective. The marked-displacement proof used below is [the quadratic socle bound without vanishing marked map](bruck-multiple-n-frattini.md#a-quadratic-socle-bound-without-vanishing-marked-map), independently accepted at the recorded source revision. The fixed-space parity input is [the affine-fiber parity theorem](bruck-n-affine-fiber-parity.md), at the recorded source revision. Independent reviews of the new deductions are recorded below.

## Realization of ordinary quotient classes

Let $`P`$ be a finite group of class at most two and exponent at most four, and let $`Z`$ be a central elementary subgroup containing $`\Phi(P)`$. Put $`V=P/Z`$, and suppose specified compatible $`Q`$-actions give $`V\cong P_6\oplus U^b`$, $`Z\cong N^a`$, and preserve the squaring map $`q:V\to Z`$. Then every class $`e\in H^2(Q,V)`$ is represented by $`G/Z`$ for an extension


```math
1\longrightarrow P\longrightarrow G\longrightarrow Q\longrightarrow1
```


inducing the specified actions on $`V,Z`$. This includes the nonzero class identified in [the quotient-extension theorem](bruck-n-split-extension-exclusion.md#quotient-extensions-and-odd-multiplicity). The construction makes no assertion about an involution $`\tau`$, a stabilizer $`H`$, a transversal $`K`$, or simplicity. In particular it does not show that any such extension is a loop envelope. It does not require $`Z(P)=Z`$.

### Cohomology and lifting the action

Put $`M=\mathop{\mathrm{Hom}}\nolimits_{\mathbb F_2}(V,Z)`$. It is projective: $`P_6^*\otimes N\cong\mathop{\mathrm{Ind}}\nolimits_F^Q(N|_F)`$ by the tensor identity, while $`U^*\otimes N`$ is projective because tensoring a projective module with any finite-dimensional group module preserves projectivity. Therefore $`H^i(Q,M)=0`$ for $`i>0`$.

Also $`H^i(Q,N)=0`$ for every $`i\ge0`$. Indeed $`\mathbb F_2^5=1\oplus N`$; Shapiro identifies the cohomology of the permutation module with $`H^i(S_4,1)`$. Restriction from $`S_5`$ to a point stabilizer $`S_4`$ on trivial-coefficient cohomology is an isomorphism: the two double cosets and Mackey's formula give $`\mathop{\mathrm{res}}\nolimits\mathop{\mathrm{cor}}\nolimits(x)=x+\mathop{\mathrm{cor}}\nolimits_{S_3}^{S_4}\mathop{\mathrm{res}}\nolimits_{S_3}^{S_4}(x)=x+4x=x`$, and $`\mathop{\mathrm{cor}}\nolimits\mathop{\mathrm{res}}\nolimits=5\mathop{\mathrm{id}}\nolimits=\mathop{\mathrm{id}}\nolimits`$. Thus $`H^3(Q,Z)=0`$.

Every pair of automorphisms of $`V,Z`$ preserving $`q`$ lifts to an automorphism of $`P`$. For completeness, choose ordered basis lifts $`x_i`$ of $`V`$; their squares are $`q(e_i)`$ and their commutators are $`\beta(e_i,e_j)=q(e_i+e_j)+q(e_i)+q(e_j)`$. Send each $`x_i`$ to any lift of the transformed basis vector and send $`Z`$ by the prescribed automorphism. The resulting images satisfy exactly the same central, square and commutator relations, which give the normal forms $`z\prod_i x_i^{\epsilon_i}`$; hence this defines the desired automorphism. The kernel acting trivially on $`V,Z`$ consists exactly of $`d_f:p\mapsto p f(pZ)`$, $`f\in M`$. Pulling back this automorphism extension along $`Q`$ and using $`H^2(Q,M)=0`$ yields a genuine action $`\alpha:Q\to\mathop{\mathrm{Aut}}\nolimits(P)`$ inducing the specified actions.

### Crossed-system construction

Choose a normalized cocycle $`e(g,h)\in V`$ representing the desired class. The polar map gives the equivariant linear map $`\beta_*:V\to M`$, $`v\mapsto(w\mapsto[\tilde v,\tilde w])`$. Since $`H^2(Q,M)=0`$, choose normalized $`f:Q\to M`$ with $`\delta f=\beta_*e`$, and put $`\alpha'_g=d_{f(g)}\alpha_g`$. Choose normalized lifts $`c(g,h)\in P`$ of $`e(g,h)`$. Then, with $`\mathop{\mathrm{Int}}\nolimits(c)(p)=cpc^{-1}`$,


```math
\alpha'_g\alpha'_h=\mathop{\mathrm{Int}}\nolimits(c(g,h))\alpha'_{gh}. \tag{1}
```


Define the associator $`z(g,h,k)`$ by


```math
\alpha'_g(c(h,k))c(g,hk)=z(g,h,k)c(g,h)c(gh,k). \tag{2}
```


The two sides have the same image in $`V`$ by the cocycle identity for $`e`$, so $`z(g,h,k)\in Z`$, not merely in $`Z(P)`$. Equation (1) and associating four factors show that $`z`$ is a normalized 3-cocycle for the prescribed action on $`Z`$. Replacing $`c(g,h)`$ by $`u(g,h)c(g,h)`$, with $`u`$ a normalized $`Z`$-valued 2-cochain, changes $`z`$ by $`\delta u`$. Since $`H^3(Q,Z)=0`$, choose $`u`$ so that $`z=1`$. Equations (1)–(2) then make


```math
(p,g)(p',h)=(p\alpha'_g(p')c(g,h),gh)
```


associative and define the required extension. The image of $`c`$ in $`V`$ remains $`e`$. Thus the quadratic datum alone cannot obstruct the ordinary nonsplit quotient class.

## A fixed-vector refinement of the socle bound

Now impose the original envelope assumptions and $`Z=\Phi(P)\cong N^a`$, $`V\cong P_6\oplus U^b`$, with $`a`$ even. Let $`W=H\cap P`$, let $`T_{\rm soc}\cong N^c`$ be the pure $`W`$-shadow intersection with $`\mathop{\mathrm{soc}}\nolimits(U^b)`$, and fix a selected marked involution $`\lambda`$ above a transposition $`t`$. Put $`r=\mathop{\mathrm{rank}}\nolimits\ell_\lambda`$. The parity theorem gives fixed-shadow dimension two, so the shadow contains the all-ones vector $`\mathbf1\in P_6`$. Put $`T=\langle\mathbf1\rangle\oplus T_{\rm soc}`$. Its full preimage in $`P`$ is elementary: $`W`$ supplies unique elementary lifts and $`Z`$ is central elementary. It need not be central in $`P`$.

The proof at the pinned [quadratic socle bound](bruck-multiple-n-frattini.md#a-quadratic-socle-bound-without-vanishing-marked-map) applies to this $`T`$: $`V`$ is free on restriction to $`\langle t\rangle`$, so $`C_T(t)\subseteq(1+t)V`$ and $`\beta(C_T(t),C_V(t))\subseteq(1+t)Z`$. With its notation $`D(p)=p^{-1}\lambda(p)`$, $`F_t=\pi^{-1}C_V(t)`$ and $`J_t=D(F_t)`$, the same actual-displacement construction gives a quadratic discrepancy $`\Delta:C_T(t)\to Z/J_t`$, with no nonzero zero, whose restriction to $`R=(1+t)T`$ is linear and injective and whose polar kills $`R`$. The dimension changes are


```math
\dim C_T(t)=1+3c,\quad \dim R=c,\quad
\dim C_T(t)/R=1+2c,\quad \dim Z/J_t=3a-r.
```


After quotienting by $`\Delta(R)`$, the resulting quadratic map on $`1+2c`$ variables has $`3a-r-c`$ binary coordinates and no nonzero zero. The same binary common-zero parity argument as in the cited proof therefore gives


```math
c\le \left\lfloor\frac{3a-r-1}{2}\right\rfloor. \tag{3}
```


For $`a=2`$, this is $`c\le2`$ when $`r=0`$, and $`c\le1`$ when $`r=2`$. The proof uses the actual displacement subgroup and original transversal; it assumes neither a quotient folder nor that $`\ell_\lambda=0`$. The even-multiplicity nonsplit branch remains open.

## Independent review

Three independent Independent checks mathematical reviewers — an independent check, an independent check and an independent check — accepted both deductions at exact source the recorded source revision. Each checked the action lift, projective cohomology, exact-Z associator and correction, and the changed dimensions in the actual marked-displacement argument. Acceptance is conditional on the cited module, displacement and parity inputs. No new computation or primary-source audit was performed. The ordinary group realization supplies no compatible involution, stabilizer or selected section; the even-multiplicity nonsplit envelope problem remains open.

## Proposed automatic stabilizer lift

**Deduction with scoped independent reviews below.** Under the group and action hypotheses of the realization theorem above, let $`\bar W\le V`$ be an $`F=F_{20}`$-submodule on which $`q`$ vanishes and which contains the entire $`F`$-fixed two-plane of $`P_6`$. Then there exists $`H\le G`$ such that $`H\cap Z=1`$, $`H\cap P`$ projects onto $`\bar W`$, and $`HP/P=F`$. This allows any central elementary $`Z\supseteq\Phi(P)`$ satisfying the stated module hypotheses. It does not assert core-freeness, $`\tau`$-stability, an original transversal, or simplicity.

Indeed $`V|_F\cong1^2\oplus S^{1+2b}`$, where $`S=N|_F`$ is projective simple, as in the pinned module-block input. Since $`\bar W`$ contains the fixed plane, $`V/\bar W`$ is projective over $`F`$, and $`H^2(F,V/\bar W)=0`$. Let $`E`$ be the preimage of $`F`$ in $`G/Z`$. The subgroup $`\bar W`$ is normal in $`E`$, and the extension $`E/\bar W`$ of $`F`$ by $`V/\bar W`$ therefore splits. The preimage in $`E`$ of one complement gives $`\bar H\le G/Z`$ with $`\bar H\cap V=\bar W`$ and image $`F`$. No splitting of $`\bar H`$ over $`\bar W`$ is asserted, and $`\bar W`$ need not be normal in all of $`G/Z`$.

For $`1\to\bar W\to\bar H\to F\to1`$, $`\bar W`$ acts trivially on $`Z`$. The two terms $`H^2(F,Z)`$ and $`H^1(F,\mathop{\mathrm{Hom}}\nolimits(\bar W,Z))`$ vanish: $`Z|_F=S^a`$ is projective and tensoring with $`\bar W^*`$ preserves projectivity. The Lyndon–Hochschild–Serre filtration consequently makes restriction


```math
H^2(\bar H,Z)\longrightarrow H^2(\bar W,Z)^F
```


injective, even when $`\bar H`$ is nonsplit. The actual extension over $`\bar W`$ is elementary abelian, since $`q|_{\bar W}=0`$ and its polar vanishes there. Its restriction class is therefore zero. Thus the preimage of $`\bar H`$ in $`G`$ splits over $`Z`$, giving $`H`$.

For a fixed $`\bar H`$, the complements to $`Z`$, up to conjugation by $`Z`$, form a torsor for


```math
H^1(\bar H,Z)\cong\mathop{\mathrm{Hom}}\nolimits_F(\bar W,Z),
```


by the five-term exact sequence and $`H^1(F,Z)=H^2(F,Z)=0`$. The torsor acquires this parametrization only after choosing a base complement; no canonical origin is asserted.

### Independent review of the stabilizer lift

Independent checks an independent check, an independent check and an independent check independently accepted the automatic stabilizer-lift section at exact source the recorded source revision, conditional on the group/action and F20 projectivity inputs. Each checked the quotient complement, the degree-two LHS filtration for possibly nonsplit Hbar, and the degree-one complement torsor. No new computation or primary-source audit was performed. The section does not assert core-freeness, inversion compatibility or a loop section.

## Proposed exact core criterion

**Criterion with scoped independent reviews below.** The stabilizer-lift source is independently reviewed at the recorded source revision; the N-block equivalence and intertwiner inputs are those of [the module-block source](bruck-s5-module-blocks.md) at the recorded source revision. The criterion has its separate independent reviews below. Assume the actual subgroup $`H`$ of the stabilizer-lift construction, with $`H\cap Z=1`$, $`HP/P=F_{20}`$, and full $`F_{20}`$-fixed $`P_6`$-plane contained in its elementary shadow $`\bar W`$. Put $`R=\bar W\cap\mathop{\mathrm{rad}}\nolimits\beta`$. Although $`R`$ is only $`F_{20}`$-stable, let $`A`$ be its largest $`S_5`$-submodule and let $`T_0\cong N^{c_0}`$ be the **entire $`N`$-isotypic socle** of $`A`$, namely the sum of all its simple $`N`$-submodules. This need not be the whole nonprincipal block of $`A`$: that block may contain copies of $`U`$.

The preimage $`E=\pi^{-1}(T_0)`$ is elementary and centralizes $`P`$, since $`q|_{\bar W}=0`$ and $`T_0\le\mathop{\mathrm{rad}}\nolimits\beta`$. Conjugation therefore makes $`E`$ an $`S_5`$-module. The reviewed N-block equivalence gives an exact sequence of $`\mathbb F_2C_2`$-multiplicity modules

```math
0\longrightarrow B\longrightarrow D\longrightarrow C\longrightarrow0,
\qquad Z\cong N\otimes B,\quad T_0\cong N\otimes C,
```

with trivial $`B,C`$. The operator $`1+t`$ on $`D`$ induces the well-defined extension map $`\epsilon:C\to B`$.

The $`W`$-lift of $`T_0`$ is an $`F_{20}`$-stable complement to $`Z`$ in $`E`$. On $`N\otimes\ker\epsilon`$, the extension splits as an $`S_5`$-module; its actual $`F_{20}`$-stable graph is also $`S_5`$-stable, since $`\mathop{\mathrm{End}}\nolimits_{F_{20}}(N)=\mathop{\mathrm{End}}\nolimits_{S_5}(N)=\mathbb F_2`$. Conversely any $`S_5`$-stable submodule of the actual $`W`$-lift has multiplicity space inside $`\ker\epsilon`$. Thus its largest such submodule is the actual lift of $`N\otimes\ker\epsilon`$.

Every normal subgroup contained in $`H`$ lies in $`P`$, because $`F_{20}`$ is core-free in $`S_5`$. It intersects $`Z`$ trivially and therefore centralizes $`P`$; its shadow is an $`S_5`$-submodule of $`R`$. Every nonzero $`S_5`$-submodule of the six-point permutation module $`P_6`$ contains its constant vector $`\mathbf1`$: for a nonzero even-weight vector, average over the $`C_5`$ fixing a point in its support; for odd weight below six, average over a $`C_5`$ fixing a point outside its support and then take a difference with a conjugate. Block separation shows that a nonzero principal-block core shadow consequently contains $`\mathbf1`$.

If $`\beta(\mathbf1,-)\ne0`$, no principal-block core is possible. Any nonzero nonprincipal-block core contains a simple $`N`$-submodule in its socle, which lies in $`T_0`$, so it exists exactly when $`\ker\epsilon\ne0`$. This remains true if the radical shadow contains a full $`U`$: its socle is a simple $`N`$-submodule and is detected by $`T_0`$. Conversely, if $`\beta(\mathbf1,-)=0`$, the preimage of $`\langle\mathbf1\rangle`$ is elementary and centralizes $`P`$; it splits as an $`S_5`$-module because $`H^1(S_5,Z)=0`$. Its unique $`F_{20}`$-fixed lift (uniqueness follows from $`Z^{F_{20}}=0`$) is also $`S_5`$-fixed, belongs to $`H`$, and is normal in $`G`$. Consequently

```math
\mathop{\mathrm{core}}\nolimits_G(H)=1
\quad\Longleftrightarrow\quad
\beta(\mathbf1,-)\ne0\ \text{ and }\ \epsilon\text{ is injective}.
```


If additionally the canonical involution $`\tau`$ fixes $`H`$ and $`Z`$ pointwise, it fixes $`E`$ pointwise. A marked involution above a transposition $`t`$ acts on $`E`$ as $`t`$. The restriction of the marked map to $`C_{T_0}(t)`$ is the connecting map into $`H^1(t,Z)`$; each nonsplit $`U`$ summand gives the natural quotient $`C_N(t)\to H^1(t,N)`$, of rank two, while each split summand gives zero. Its rank is $`2\mathop{\mathrm{rank}}\nolimits\epsilon`$; hence core-freeness forces $`\mathop{\mathrm{rank}}\nolimits\ell_\lambda\ge2c_0`$. This is an actual-lift statement, not a construction of $`\tau`$, a transversal, or a simple loop.

### Independent review of the core criterion

Independent checks an independent check, an independent check and an independent check independently accepted the exact core criterion and conditional marked-rank consequence at exact source the recorded source revision, under the pinned actual-stabilizer, N-block, cohomology and intertwiner inputs. Each checked the principal constant-line obstruction, the full N-isotypic socle, and the actual F20 graph over the kernel of the extension operator; none assumed a split of the whole C2 extension. No new computation or primary-source audit was performed. Inversion and original selected-section compatibility remain open.

