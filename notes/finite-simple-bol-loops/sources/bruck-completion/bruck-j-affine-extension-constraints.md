# Affine transposition fibers for J with multiple N factors

**Mira Cult**

**Scoped constraints**, continuing [0323:C0010](../../claims/0010.md). Let $`(G,H,K)`$ be a faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. Put $`P=O_2(G)`$, suppose $`P`$ has class at most two and exponent at most four, and assume

```math
G/P\cong S_5,\qquad Z=\Phi(P)\cong N^a,\qquad
 V=P/Z\cong J\oplus U^b,\qquad a\ge1.
```

Here $`J=P_6/\langle\mathbf1\rangle`$, with $`P_6`$ the six-point permutation module; $`N`$ is the deleted five-point simple and $`U=N\otimes\mathbb F_2[C_2]`$, with sign action on the second factor. In particular $`J`$ is not its dual. The conclusions concern actual selected marked fibers. They neither construct a quotient loop nor assume every involution lift is selected.

The J cohomology and restriction inputs are [the dimension-five source](bruck-s5-dimension-five.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/266152034b2f190313d253c4d55df0d4f85f68c2) and its independent $`H^3`$ certificate at [the source revision](https://github.com/Mira-Cult/math-wip/commit/418b4d50d1d6deb2e72182e867f1b1f70450fa92), with the Nagy normalizer restriction in [bruck-s5-radical.md](bruck-s5-radical.md). The N-block cohomology is reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499). The original marked-fiber and quadratic identity inputs are reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/123933cc594b601dd317d62b333a949d20431d35), and their J/multiple-N setting and socle bounds at [the source revision](https://github.com/Mira-Cult/math-wip/commit/3c3cafff03f9e9d79640b68f03883c22e57210d6). Independent exact-source reviews of the extension and selected-fiber deductions are recorded below.

## Extension coordinates and relative inversion

The group quotient $`\overline G=G/Z`$ is an extension of $`S_5`$ by $`V`$; no assertion is made that it is a loop envelope. Projectivity gives $`H^i(S_5,U)=0`$ for $`i>0`$, so

```math
H^2(S_5,V)\cong H^2(S_5,J)\cong\mathbb F_2^2.
```

Let $`F\cong F_{20}`$ and $`T=\langle t\rangle`$ for a transposition. The reviewed restriction calculations give an isomorphism

```math
H^2(S_5,V)\longrightarrow H^2(F,J)\oplus H^2(T,J)
 \cong\mathbb F_2^2.                                           \tag{1}
```

Indeed $`J|_F=\mathbf1\oplus S`$, where $`S`$ is projective, so the first target is one-dimensional and detected on a Sylow $`C_4`$. The cited long exact sequence for $`0\to\mathbf1\to P_6\to J\to0`$, together with the reviewed $`H^3`$ input, makes the transposition restriction onto. Nagy's nonsplit class has zero transposition restriction and nonzero $`F`$-restriction, the latter detected by the order-eight element in its five-normalizer. Thus the two coordinates are independent and all four ordinary extension classes occur at the group-cohomology level. This does not assert that all four lift through $`Z`$ to simple Bruck envelopes.

The canonical inversion $`\tau`$ fixes $`V`$ and induces the identity on $`S_5`$, so on $`\overline G`$ it is described by a derivation $`\delta:S_5\to V`$. Actual $`H`$-lifts are $`\tau`$-fixed, hence $`\delta|_F=0`$. For a selected $`k\in K`$ above $`t`$, the actual inversion equation gives

```math
k^2=\delta(t)\quad\text{in }\overline G.                      \tag{2}
```

For any lift of $`t`$, its square represents the restriction of the extension class to $`H^2(T,V)=V^t/(1+t)V`$. Thus the transposition bit of (1) is

```math
e_T=[\delta(t)]\in H^1(T,V)\cong\mathbb F_2.                    \tag{3}
```

This allows order-four section lifts. It does not import an exponent-two split/nonsplit dichotomy.

The relative derivations $`\delta|_F=0`$ form a two-dimensional $`\mathbb F_2`$-space. Indeed $`H^1(S_5,V)\cong H^1(S_5,J)\cong\mathbb F_2`$, and its restriction to $`F`$ vanishes: under the reviewed connecting injection it is represented by $`\mathop{\mathrm{sign}}\nolimits^2`$, which restricts trivially to $`C_4`$. The relative coboundaries come from $`V^F=J^F`$, which is one-dimensional, while $`V^{S_5}=0`$. Hence there are four such derivations, two in each global cohomology class; (3) fixes the class but not a unique cochain. These are ordinary group-extension data, with original stabilizer and section constraints still to be imposed.

## Two affine shadow torsors

Fix a quotient transposition $`t`$ and an actual selected marked involution $`\lambda=\widehat\tau k`$ above it. For the formal external extension $`G\rtimes\langle\widehat\tau\rangle`$, this remains meaningful when $`\tau=1`$. The restriction of $`J`$ to $`T`$ has $`\mathop{\mathrm{rank}}\nolimits(1+t)=2`$ and $`H^1(T,J)\cong\mathbb F_2`$; each $`U`$ is $`T`$-free. Thus $`H^1(T,V)\cong\mathbb F_2`$. Relative to $`\lambda`$, involutory lifts over $`t`$ have at most two shadow cohomology classes. A lifted order-three subgroup of $`C_{S_5}(t)/\langle t\rangle\cong S_3`$ fixes each class: its action has order dividing three on a set of at most two points.

Let $`\ell_\lambda:C_V(t)\to H^1(T,Z)`$ be the actual marked displacement map. Its restriction to $`(1+t)V`$ is the intrinsic centralizer-equivariant map $`d`$. Within one relative shadow class, $`\ell`$ is independent of the involution lift. To see this, reduce two lifts to the same shadow by $`P`$-conjugation; they then differ by a central element, which does not change their conjugation on $`P`$. Conjugating by a shadow $`x`$ changes the displacement on $`v\in C_V(t)`$ only by

```math
\beta((1+t)x,v)=(1+t)\beta(x,v),
```

which is zero modulo $`(1+t)Z`$. Thus the map is $`C_3`$-equivariant in each class. The quotient $`C_V(t)/(1+t)V`$ is a trivial one-dimensional $`C_3`$-module, whereas $`H^1(T,Z)/\mathop{\mathrm{im}}\nolimitsd`$ has no $`C_3`$-fixed points: restriction to the odd-order group $`C_3`$ is semisimple, and the natural two-dimensional modules have no fixed vector. Consequently

```math
\mathop{\mathrm{im}}\nolimits\ell_\lambda=\mathop{\mathrm{im}}\nolimitsd,\qquad
 r:=\mathop{\mathrm{rank}}\nolimits\ell_\lambda=\mathop{\mathrm{rank}}\nolimitsd\text{ is even}. \tag{4}
```

The two classes have the same $`d`$. Indeed, changing $`\lambda`$ to $`p\lambda`$, with $`p`$ of $`t`$-fixed shadow $`m`$, adds $`\beta(m,v)`$ to $`\ell(v)`$; when $`v=(1+t)x`$ this correction lies in $`(1+t)Z`$.

Both shadow classes actually contain involutory lifts. For $`m\in C_V(t)`$, let $`p`$ be a lift and define

```math
\sigma(m)=(p\lambda)^2\bmod(1+t)Z=q(m)+\ell_\lambda(m)
 \in H^1(T,Z).                                                 \tag{5}
```

Changing $`m`$ by $`(1+t)v`$ leaves (5) unchanged: both $`q((1+t)v)`$ and $`\ell_\lambda((1+t)v)`$ represent $`d((1+t)v)`$, while $`\beta(m,(1+t)v)\in(1+t)Z`$. Hence $`\sigma`$ descends to $`H^1(T,V)\cong\mathbb F_2`$. It is $`C_3`$-equivariant, and the target has no nonzero fixed vector, so $`\sigma=0`$. Adjusting the central lift of $`p`$ then produces an involution in the other class.

Within each class, every $`P`$-orbit has a representative $`z\lambda`$ with $`z\in C_Z(t)`$, and the residual equivalence is modulo $`(1+t)Z`$ and $`\mathop{\mathrm{im}}\nolimits\ell`$. Its orbit set is therefore an affine torsor for

```math
M=H^1(T,Z)/\mathop{\mathrm{im}}\nolimitsd.
```

A lift of $`C_3`$ acts affinely on this torsor with fixed-point-free linear part. It has exactly one fixed $`P`$-orbit. This holds also when $`M=0`$; no choice of a pure $`S_5`$-complement is involved.

## Selected origins and the odd-multiplicity obstruction

The selected original fiber over $`t`$ has size $`|P:W|/2`$, where $`W=H\cap P`$. By (4), all its $`P`$-orbits have size $`2^{\rho_V+a+r}`$, with $`\rho_V=2+4b`$. The number of selected $`P`$-orbits is therefore

```math
n=2^{4b+3a+2-w-r},\qquad w=\dim W.                         \tag{6}
```

The invariant-functional obstruction makes the $`F`$-fixed part of $`WZ/Z`$ the one-dimensional $`J^F`$, so $`w\equiv1\pmod4`$. All nonfixed $`C_3`$-orbits on the $`P`$-orbit set have length three; exactly two fixed orbits exist, one in each shadow class. Since $`r`$ is even, (6) gives:

- If $`a`$ is odd, exactly one of the two fixed $`P`$-orbits is selected.
- If $`a`$ is even, both fixed $`P`$-orbits are selected.

Conjugation by the actual $`k\in K`$ above $`t`$ acts as the $`t`$-factor of the quotient centralizer. It preserves the set of the two $`C_3`$-origins and

```math
(k\lambda k^{-1})\lambda^{-1}=k^2.
```

Thus it swaps their shadow classes exactly when $`[k^2]=e_T\ne0`$. For odd $`a`$, a selected set containing exactly one origin cannot be invariant under that swap. Therefore

```math
\boxed{\ a\text{ odd}\quad\Longrightarrow\quad e_T=0.\ }       \tag{7}
```

This excludes the nonzero transposition-restriction extension types for every odd $`a`$ under the stated envelope hypotheses. For even $`a`$, both origins are selected and this argument leaves the bit open. It also does not settle whether the two forced origins collide with the actual stabilizer, or classify the remaining extension, section, and simplicity data.

## Independent review

Three independent mathematical reviewers — `review_s5_h3`, `review_hs_full` and `review_presentations` — accepted the extension coordinates, both actual affine shadow torsors and the odd-multiplicity transposition-bit obstruction at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/4c93742a59ccdd786f23598f0374f674c6f75fff), conditional on the cited cohomology, module and marked-fiber inputs. Each checked the common intrinsic map, vanishing square obstruction, selected-origin count and actual centralizer exchange. No new computation or primary-source audit was performed. These are necessary constraints, not a realization theorem or a full J-branch exclusion.
