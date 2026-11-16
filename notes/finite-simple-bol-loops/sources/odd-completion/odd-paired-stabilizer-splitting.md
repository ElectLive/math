# Stabilizer splitting on paired odd-envelope layers

Mira Cult
This bounded argument concerns the residual frontier in [C0010](../../claims/0010.md) and the local splitting hypothesis in [paired-layer-factorization.md](paired-layer-factorization.md). It does not claim that every odd-order loop has an odd left multiplication group, that the displayed hypotheses always hold, or that exact-factorization presentations are exhaustive.

Let $`(G,H,K)`$ be the canonical faithful generating left Bol folder of a finite simple nonassociative loop, with **$`|G|`$ odd**, and let $`\tau\in\mathop{\mathrm{Aut}}\nolimits(G)`$ invert every member of $`K`$. Let $`V`$ and $`W=\tau(V)`$ be distinct minimal normal elementary abelian subgroups of $`G`$; put $`A=V\times W`$ and $`d=\dim_{\mathbb F_p}V=\dim_{\mathbb F_p}W`$. The odd-envelope results in [odd-folder-radicals.md](odd-folder-radicals.md) give $`K=\{g\in G:\tau(g)=g^{-1}\}`$ and the strict defect $`|H\cap A|<|C_A(\tau)|=p^d`$. Put $`D=H\cap A`$.

## Irreducibility and orbit-avoidance criteria

**Irreducibility criterion.** If $`V`$ or $`W`$ is irreducible as an $`\mathbb F_pH`$-module, then

$$D=(H\cap V)\times(H\cap W).$$

Indeed, $`D`$ is an $`H`$-invariant subspace of $`A`$, and each coordinate projection is an $`H`$-submodule. Strict defect gives $`\dim D<d`$, so an irreducible factor has zero projection of $`D`$; hence $`D`$ lies in the opposite factor. More generally it suffices that $`\dim D`$ be less than the least dimension of a nonzero $`H`$-submodule of either factor. If the defect is exactly one, then $`\dim D=d-1`$; irreducibility of one factor makes $`D`$ a hyperplane in the other, while irreducibility of both forces $`D=0`$ and $`d=1`$.

Since $`V`$ and $`W`$ are minimal normal elementary abelian subgroups, they are irreducible $`G`$-modules. Thus either $`G=HC_G(V)`$ or $`G=HC_G(W)`$ supplies the irreducibility hypothesis. Conversely, a nonzero graph component in $`D`$ forces both coordinate projections to be nonzero proper $`H`$-submodules, and Goursat's lemma gives a common nonzero $`H`$-subquotient. In particular, graph coupling forces both $`HC_G(V)<G`$ and $`HC_G(W)<G`$. None of these statements assumes semisimplicity on restriction to $`H`$.

**Orbit-avoidance criterion.** Set

$$B=K\cap A=\{(v,-\tau(v)):v\in V\}.$$

The displayed equality follows from the cited odd-envelope fact that $`K`$ is the full set of elements inverted by $`\tau`$: on $`A=V\times W`$, inversion is coordinatewise negation and $`\tau`$ swaps the factors. For every $`g\in G`$,

$$D\cap B^g=1.$$

Indeed, $`K`$ is a transversal to every conjugate of $`H`$ and contains $`1`$, so $`K\cap H^{g^{-1}}=1`$; $`B\subseteq K`$ gives the assertion. If the $`G`$-conjugates of $`B`$ cover every mixed element of $`V^\#\times W^\#`$, then $`D`$ contains no mixed element. An additive subgroup with no mixed element lies in one coordinate, since adding nonzero elements from both coordinates would produce a mixed element. Thus $`D`$ splits. More generally, any graph-coupled $`D`$ must avoid the explicit union of these conjugate anti-diagonals. The covering condition is an additional hypothesis, not a claimed property of all odd envelopes.

## Control from $`Q_{3,13}`$

The [C0003](../../claims/0003.md) construction has $`X=\mathbb F_{27}^+\rtimes(C_{13}\rtimes C_3)`$, $`\widehat G=\{(u,v)\in X^2:uv\in X'\}`$, $`H=\widehat G\cap(Y_0\times Y_1)`$, $`V=\mathbb F_{27}\times1`$ and $`W=1\times\mathbb F_{27}`$. Because $`X'Y_0=X`$, the second projection of $`H`$ is $`Y_1=C_{13}\rtimes C_3`$, whose $`C_{13}`$ action on $`W`$ is irreducible. The criterion therefore gives $`D\le V`$. In fact $`D=(\ker\mathop{\mathrm{Tr}}\nolimits)\times0`$ has dimension $`2=d-1`$. This example uses the stated C0003 folder data; it does not show that the irreducibility hypothesis is universal or that the layer itself is an intrinsic witness.

## Nonsimple graph-coupled control

The following control shows why the simple-loop/strict-defect hypothesis cannot simply be dropped. Let $`F=\mathbb F_{27}`$, choose $`\zeta\in F^\times`$ of order $`13`$, and set

$$G=(F^+\oplus F^+)\rtimes\langle a\rangle,\quad a(u,v)=(\zeta u,\zeta^{-1}v),\quad \tau(u,v,a^i)=(v,u,a^{-i}),\quad H=\{(t,t):t\in F\}.$$

The full $`\tau`$-inverted set is

$$K=\{(u,-\zeta^{-i}u,a^i):u\in F,\ i\in\mathbb Z/13\}.$$

It contains $`1`$, is inverse-closed and is closed under $`xyx`$. Its size is $`13\cdot27=[G:H]`$. Conjugates of $`H`$ are graphs of slopes $`\zeta^{2j}`$, up to orientation. If two elements of $`K`$ occupy the same coset of one such conjugate, they have the same $`a`$-coordinate; comparing their differences forces a power of $`\zeta`$ to equal $`-1`$ unless the elements coincide. Since $`\langle\zeta\rangle`$ has odd order, they coincide. Counting gives transversality to every conjugate of $`H`$, and the folder criterion produces a left Bol loop. The core of $`H`$ is trivial because two distinct conjugate graphs intersect trivially. The set $`K`$ contains $`a`$ and the antidiagonal $`\{(u,-u):u\in F\}`$; that antidiagonal and an $`a`$-conjugate span $`F\oplus F`$, so $`G=\langle K\rangle`$.

The coordinate factors are distinct minimal normal subgroups, since $`\mathop{\mathrm{ord}}\nolimits_{13}(3)=3`$, and $`\tau`$ swaps them. Here $`D=H`$ is the full diagonal graph and $`D=C_A(\tau)`$, so the defect is zero. The image of $`K`$ in $`G/A\cong C_{13}`$ is a transversal to $`HA/A=1`$. Hence the quotient folder induces a loop homomorphism onto the order-$`13`$ group with kernel $`K\cap A`$, a nontrivial proper normal subloop. This control is therefore **not simple** and does not decide whether strict defect or simplicity forces splitting.

The irreducibility and orbit-avoidance hypotheses above are sufficient conditions only. In particular, splitting on $`A`$ alone does not provide the index and quotient-splitting conditions required by the linked paired-layer witness criterion.

These remain sufficient criteria, not universal splitting or odd-LMlt assertions.

## Publication and verification scope

This public source preserves the mathematical argument at the revision recorded in the source crosswalk. Its conclusions retain every stated hypothesis and dependency. Source-specific automated mathematical checks are not human referee acceptance, formal verification or a literature-priority audit. Computational checks, where cited, have only their stated finite scope.

The review checked the projection/irreducibility and Goursat arguments without semisimplicity, the conjugate anti-diagonal avoidance criterion, and the Q₃,₁₃ control. It also checked the nonsimple control's automorphism and inverted-set formula, coset slopes, faithfulness, generation, minimal normal factors and proper quotient onto C₁₃, with equality rather than strict defect. No computation was needed. These remain sufficient criteria, not universal splitting or odd-LMlt assertions.
