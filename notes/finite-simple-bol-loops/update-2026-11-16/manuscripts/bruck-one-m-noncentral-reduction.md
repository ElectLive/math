# Passive projective blocks in one-M noncentral radicals

**Independently reviewed reduction and finite control.** Let $`(G,H,K)`$ be the faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. Suppose $`P=O_2(G)`$ has class at most two and exponent at most four, $`G/P\cong S_5`$, and $`Z=\Phi(P)\cong M`$ is elementary abelian and central in $`P`$, but not assumed central in $`G`$. Assume


```math
V=P/Z\cong X\oplus U^b,\qquad b\ge1,\quad X\in\{J,P_6\}, \tag{1}
```


where $`J=\mathbb F_2^6/\langle\mathbf1\rangle`$, $`P_6=\mathbb F_2^6`$, $`M`$ is the even-six heart, $`N`$ is the deleted five-point simple, and $`U=N\otimes\mathbb F_2[C_2]`$, with $`S_5`$ acting on $`C_2`$ through sign. The proposed reduction below separates all but one $`U`$-block from the actual group and outer marked fibers. It does **not** classify folders, normalize all stabilizer graphs, or bound $`b`$. This continues C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`], without a new permanent ID.

The original section-fiber and canonical-inversion inputs are Baumeister–Stein, [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5, as recorded in the Frattini-shadow source [dependency/context not reproduced in this update: `bruck-frattini-shadow.md`] at `9009bb98c97148e7cf250344f714528b1620b0a9` and the all-radical bounds [dependency/context not reproduced in this update: `bruck-all-radical-constraints.md`] at `6b719ad3026522f93cd9e0e027ae4027f6ee12df`. The elementary $`J/N`$ and $`P_6`$ quadratic controls are in bruck-j-n-frattini-exclusion.md [dependency/context not reproduced in this update: `bruck-j-n-frattini-exclusion.md`] at `2a25b81e3efe5bdd8a3923e27c94aef16a559094` and bruck-p6-semisimple-frattini.md [dependency/context not reproduced in this update: `bruck-p6-semisimple-frattini.md`] at `54aec585a4311d67571500965fbf63d42b1a7e99`. The reviewed N-block/dual-number inputs and F-module identifications are in [the N-block manuscript](bruck-s5-module-blocks.md) at `dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499` and [the active-U normal form](bruck-s5-active-u-stabilizer.md) at `7ee728cc65fcaa28ffac8850185d0fdfe9a8bc48`. The exact-source review below covers the present group splitting, stabilizer cases and finite control.

## Quadratic and marked-orbit constraints

The source factorization $`P=(H\cap P)(K\cap P)`$ makes the canonical inversion $`\tau`$ act trivially on $`V`$. It also fixes $`Z`$: the squares generate $`Z`$, and if $`\tau(p)=pz`$ with $`z\in Z`$, then $`\tau(p^2)=(pz)^2=p^2`$. The square gives an $`S_5`$-equivariant quadratic map $`q:V\to M`$, with polar form the commutator. Its values generate $`M`$. Put $`W=H\cap P`$, $`w=\log_2|W|`$, and let $`\rho_V,\rho_Z`$ denote the ranks of $`1+t`$ for a transposition $`t`$.

For a selected marked involution $`\lambda=\widehat\tau k`$ above $`t`$, let $`\alpha`$ be conjugation by $`\lambda`$ on $`P`$. Define


```math
\ell_\lambda:C_V(t)\to Z/(1+t)Z,\qquad
 v\longmapsto\alpha(p)p^{-1}\bmod (1+t)Z,
```


where $`p`$ is any lift of $`v`$. This is well-defined and linear because $`Z`$ is central elementary, and the image of $`C_P(\lambda)`$ in $`V`$ is exactly $`\ker\ell_\lambda`$. Thus


```math
|\lambda^P|=2^{\rho_V+\rho_Z+\mathop{\mathrm{rank}}\nolimits\ell_\lambda}. \tag{2}
```


The original fiber has size $`|P:W|/2`$, while the number of all inversion solutions above $`t`$ is at most $`2^{\dim V-\rho_V+\dim Z-\rho_Z}`$. Therefore


```math
\rho_V+\rho_Z-1\le w\le\dim V+\dim Z-\rho_V-\rho_Z-1. \tag{3}
```


Corefreeness gives $`W\cap Z=0`$, since $`M|F_{20}`$ is irreducible. On restriction to $`F_{20}`$, the nonfixed part of $`V`$ is $`S^{1+2b}`$, and its fixed part has dimension at most one for $`J`$ or two for $`P_6`$. The ranks $`\rho_Z=2`$, $`\rho_U=4`$, $`\rho_J=2`$, and $`\rho_{P_6}=3`$, together with (3) and the four-dimensional $`S`$-multiplicities, force


```math
w=4b+4,\qquad \mathop{\mathrm{rank}}\nolimits\ell_\lambda=0, \tag{4}
```


and the $`F`$-fixed part of the $`W`$-shadow is zero. The original transposition fiber is consequently a single $`P`$-orbit. No conclusion about a quotient folder follows.

## All-b quadratic normal form

The standalone verifier [dependency/context not reproduced in this update: `../code/verify_bruck_one_m_noncentral.py`] uses synchronized five- and six-point permutation generators, with the two $`N`$-coordinates of $`U`$ swapped by an odd generator. It checks the paired group of order 120 and solves fixed-component equivariance equations, obtaining


```math
\dim \mathop{\mathrm{Quad}}\nolimits_{S_5}(X,M)=1,\quad
 \dim \mathop{\mathrm{Quad}}\nolimits_{S_5}(U,M)=0,\quad
 \dim \mathop{\mathrm{Hom}}\nolimits_{S_5}(X\otimes U,M)=2,\quad
 \mathop{\mathrm{Hom}}\nolimits_{S_5}(U\otimes U,M)=0. \tag{5}
```


It also checks $`\dim\mathop{\mathrm{End}}\nolimits_{S_5}(U)=2`$, with basis $`1,\varepsilon`$, $`\varepsilon^2=0`$, and that precomposition by $`\varepsilon`$ has rank one on the cross-map space for both choices of $`X`$. Thus that space is free of rank one over $`R=\mathbb F_2[\varepsilon]/(\varepsilon^2)`$, consistent with the reviewed dual-number input.

These fixed-component calculations imply the all-$`b`$ statement, rather than extrapolating from small $`b`$: every quadratic map on a direct sum is uniquely the sum of its restrictions to the summands and its polar cross maps between distinct summands. Therefore $`q|_{U^b}=0`$, and its $`X`$-to-$`U^b`$ cross coefficients form a row in $`R^b`$. Under $`\mathop{\mathrm{GL}}\nolimits_b(R)=\mathop{\mathrm{Aut}}\nolimits_{S_5}(U^b)`$, the row has precisely three types: zero, a unit row, or a nonzero row contained in $`\varepsilon R^b`$. Elementary operations put them in the respective forms $`0`$, $`(1,0,\ldots,0)`$, or $`(\varepsilon,0,\ldots,0)`$. The quadratic datum consequently has at most one active $`U`$-block. For the zero row choose any one block as active; the argument below applies equally. This is a change of module coordinates and is not asserted to lift as an automorphism of a fixed extension.

## Splitting the passive blocks

Let $`Y=U^{b-1}`$ be the passive sum and $`V_0=X\oplus U`$. The preimage $`E_Y`$ of $`Y`$ in $`P`$ is elementary abelian and centralizes $`P`$: both $`q|_Y`$ and its polar with all $`V`$ vanish. Conjugation on $`E_Y`$ factors through $`S_5`$, giving an exact sequence of modules


```math
0\to M\to E_Y\to Y\to0.
```


The projectivity of $`Y`$ splits it; choose an $`S_5`$-stable complement $`Y_0\cong Y`$. This is normal in $`G`$ and centralizes $`P`$. The central shear of $`\tau`$ on $`Y_0`$ is an $`S_5`$-map $`Y\to M`$: $`\tau(g)g^{-1}\in P`$, which centralizes $`E_Y`$. The distinct-block input gives $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(Y,M)=0`$, so $`\tau`$ fixes $`Y_0`$ pointwise.

Let $`P_0`$ be the preimage of $`V_0`$ in $`P`$. Then $`P=P_0\times Y_0`$. Since group-algebra projectives are injective, $`H^1(S_5,Y_0)=H^2(S_5,Y_0)=0`$. Thus $`G/P_0`$ splits over $`Y_0`$; letting $`E`$ be the inverse image of a chosen quotient complement gives


```math
G=E\ltimes Y_0,\qquad E\cap P=P_0,\qquad \tau(E)=E. \tag{6}
```


For the last assertion, $`\tau`$ induces a derivation $`\delta:S_5\to Y_0`$ on $`G/P_0`$. Every $`b\in F_{20}`$ has an $`H`$-lift fixed by $`\tau`$, and $`\tau`$ fixes $`Y_0`$, so $`\delta|F=0`$. Vanishing of $`H^1(S_5,Y_0)`$ makes $`\delta`$ principal, and $`Y_0^F=0`$ forces it to vanish. No splitting of the active extension $`E/P_0`$ is assumed. If $`b=1`$, $`Y_0=1`$ and (6) is tautological.

For a marked involution over $`t`$, the passive coordinate lies in $`C_{Y_0}(t)=(1+t)Y_0`$, because $`U|\langle t\rangle`$ is free and $`\tau`$ fixes $`Y_0`$. Conjugation by $`Y_0`$ fills this entire passive fiber. Thus selection of an outer marked class is determined by its active $`E`$-coordinate. This does not imply that the radical section $`K\cap P`$ factors, or that the image of $`K`$ defines a quotient loop.

## The remaining stabilizer graphs

Put $`s=b-1`$, let $`4c=\dim(W\cap Y_0)`$, and define


```math
\delta_W=\tfrac14\dim(\mathop{\mathrm{proj}}\nolimits_{P_0}W\cap Z)\in\{0,1\}. \tag{7}
```


All these subspaces are $`F`$-stable. By (4), $`W`$ has no fixed $`F`$-summand and has dimension $`4s+8`$. Corefreeness makes $`(W\cap Y_0)\cap\mathop{\mathrm{soc}}\nolimits(Y_0)=0`$: every $`F`$-submodule of the socle $`N^s`$ is $`S_5`$-invariant. Hence $`c\le s`$. The active shadow of $`W`$ has $`S`$-multiplicity $`s+2-c-\delta_W`$. It cannot contain all three active $`S`$-copies, because $`q`$ vanishes on the $`W`$-shadow. A nonzero $`q|_X`$ is nonzero on the $`X`$-side $`S`$. If a cross map vanished on $`S\times U`$, equivariance would make it vanish on the $`S_5`$-span of $`S`$, which is $`M`$ for $`J`$ or the even-six submodule for $`P_6`$; it would then factor through a trivial quotient of $`X`$, contrary to $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(U,M)=0`$. Since $`q\ne0`$, the full active nonfixed space is not singular.

Thus $`c+\delta_W\ge s`$, leaving only


```math
(\delta_W,c)=(0,s),\quad(1,s-1),\quad(1,s), \tag{8}
```


with $`c\ge0`$. The latter two cases retain an actual possible graph $`z+y`$ with $`0\ne z\in Z`$, $`y\in Y_0`$: $`W\cap Z=0`$ does not imply its projection to $`P_0`$ avoids $`Z`$.

This reduction leaves the active 2-group and group-extension classes, the stabilizer graph in (8), the full radical section and all normal-subgroup simplicity tests to be determined. In particular it is not an all-$`b`$ classification or an assertion that passive blocks can be discarded from isomorphism tests. The exact-source independent reviews are recorded below.

Run the fixed-component control from the repository root with Python 3.11+ and assertions enabled:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_one_m_noncentral.py
```

## Independent review and evidence

At exact source `39e524307bcd8036c7d9e1908a67f6c16252957f`, GPT-6.1 Terra reviewers [model reviewer] and [model reviewer] independently accepted the full proof and code, conditional on the cited envelope, projectivity and module inputs. Both read and reran the pinned standalone certificate with Python 3.12.14. They checked the marked orbit bound, arbitrary-b row normal form, actual passive group split and τ compatibility, and all three stabilizer graph cases. Each also independently checked q_X on the F₂₀-simple S in a temporary calculation: it is nonzero on every nonzero S vector (and its values span M). That extra assertion is not explicitly tested by the pinned certificate. These are independent model reviews, not fresh primary-source audits or formal verification, and do not classify the remaining active extensions or folders.

## Further outer-collision reduction

**Independently reviewed continuation.** Retain all hypotheses and notation above, including $`b\ge1`$, $`Z\cong M`$, and the three graph cases (8). The previous review applies only to exact source `39e524307bcd8036c7d9e1908a67f6c16252957f`; it does not cover the following deductions or the additional verifier assertions. The extended standalone verifier now explicitly checks that the nonzero $`q_X`$ is nonzero on each of the 15 nonzero vectors of the $`F`$-simple $`S\le X`$, as well as the line, plane and complement calculations used below.

Let $`Y=U^b`$ denote the entire N-block summand of $`V`$, and let $`E_Y`$ be its preimage in $`P`$. Irrespective of the cross-row type, $`E_Y`$ is elementary abelian, because $`q|_Y=0`$, and is normal and $`\tau`$-stable. It need not centralize $`P`$ when the cross row is nonzero. Suppose the $`W`$-shadow lies in $`Y`$. Then $`W\le E_Y`$. For a selected marked involution $`\lambda`$ over a transposition $`t`$, conjugation by $`\lambda`$ induces $`t`$ on $`Y`$ and on $`Z`$. Its displacement image on $`E_Y`$ has rank at least $`4b+2`$: its image in $`Y`$ has rank $`4b`$, and its intersection with $`Z`$ contains $`(1+t)Z`$, of dimension two. Since $`\dim W=4b+4`$ and $`\dim E_Y=8b+4`$,


```math
\dim\bigl(W\cap(1+\lambda)E_Y\bigr)\ge2. \tag{9}
```


Any nonzero displacement in (9) conjugates $`\lambda`$ to another selected marked involution with $`K`$-coordinate in the same $`H`$-coset, contrary to transversality. Thus the $`W`$-shadow cannot lie in $`Y`$. In particular the zero cross row is impossible: its nonzero $`q_X`$ is nonzero on every nonzero vector of the $`X`$-side $`S`$, while $`q|_Y=0`$ and the $`W`$-shadow is $`q`$-singular.

For each $`X=J,P_6`$, the extended verifier constructs all seven $`F`$-simple lines and seven $`F`$-stable $`S^2`$-planes in the nonfixed part of the active $`X\oplus U`$. It evaluates each of the 16 or 256 vectors in these spaces. A unit cross row has exactly one $`q`$-singular plane, the pure $`U`$ plane, for either coefficient of $`q_X`$. An $`\varepsilon`$ row with $`q_X=1`$ has the same property and no $`q`$-singular line projecting nontrivially to $`X`$, so it is excluded by (9). For $`\varepsilon`$ with $`q_X=0`$, there are two singular planes: pure $`U`$ and one with nonzero $`X`$-projection. The unit row has exactly one singular $`F`$-line with nonzero $`X`$-projection for each $`q_X`$ coefficient; the $`\varepsilon,q_X=0`$ row has two.

Accordingly, for the unit row only $`(\delta_W,c)=(1,s)`$ remains, and the active $`W`$-shadow is the unique singular $`S`$-line projecting nontrivially to $`X`$. For $`\varepsilon,q_X=0`$, the same graph case remains and $`(1,s-1)`$ can additionally use the exceptional $`X`$-projecting singular $`S^2`$-plane. The zero row, $`\varepsilon,q_X=1`$, and all other uses of (8) are excluded by (9). Here $`s=b-1`$, with $`s-1\ge0`$ when that case is used.

## A finite-active test for original outer collisions

Continue with a remaining case. In $`(\delta_W,c)=(1,s)`$, put $`T=W\cap Y_0`$. It is an $`F`$-complement to $`\mathop{\mathrm{soc}}\nolimits(Y_0)`$. The extended verifier checks that on one $`U`$, the two $`F`$-simple complements to its socle both meet $`C_U(t)`$ trivially. The reviewed $`\mathop{\mathrm{GL}}\nolimits_s(\mathbb F_2[\varepsilon]/(\varepsilon^2))`$ complement normal form at `7ee728cc65fcaa28ffac8850185d0fdfe9a8bc48` then gives


```math
Y_0=T\oplus C_{Y_0}(t). \tag{10}
```


Let $`\overline W=\mathop{\mathrm{proj}}\nolimits_{P_0}W`$, an elementary subgroup of $`P_0`$ of order $`2^8`$ containing $`Z`$. A selected marked involution can be conjugated by $`Y_0`$ to one $`\lambda`$ with zero passive coordinate, because its passive coordinate lies in $`C_{Y_0}(t)=(1+t)Y_0`$. Write


```math
D_\lambda(P)=\{p\lambda p^{-1}\lambda^{-1}:p\in P\};
```


this is a set, not a presumed subgroup. Then


```math
D_\lambda(P)\cap W\ne\{1\}
 \quad\Longleftrightarrow\quad
 D_\lambda(P_0)\cap\overline W\ne\{1\}. \tag{11}
```


For the forward implication, a displacement with trivial active component would be in $`T\cap C_{Y_0}(t)=0`$. Conversely, lift a nontrivial active displacement in $`\overline W`$ to $`w\in W`$; by (10), subtract its $`T`$-component using $`W`$, and realize the remaining $`C_{Y_0}(t)`$-component by passive conjugation. Equation (11) is a test for a collision in the **original** folder. It does not assert that $`\overline W`$ is a quotient-folder stabilizer.

Equation (11) immediately excludes every case with $`\delta_W=1,c=s`$. Indeed $`\overline W`$ contains $`Z`$, while $`D_\lambda(P_0)`$ contains $`(1+t)Z`$, which has dimension two. Thus its intersection with $`\overline W`$ is nontrivial. This eliminates the entire unit row (for either coefficient of $`q_X`$) and the nonexceptional $`\varepsilon,q_X=0`$ case, without enumerating active extensions. Only $`\varepsilon,q_X=0,(\delta_W,c)=(1,s-1)`$ remains.

In the exceptional $`\varepsilon,q_X=0,(\delta_W,c)=(1,s-1)`$ case, $`T`$ is $`F`$-stable, disjoint from $`\mathop{\mathrm{soc}}\nolimits(Y_0)`$, and has multiplicity $`s-1`$. Its projection to $`Y_0/\mathop{\mathrm{soc}}\nolimits(Y_0)`$ is injective. Dual-number base changes send this top image to the first $`s-1`$ coordinates, and $`\varepsilon`$-shears remove the socle graph. Thus $`T`$ becomes the standard complement on $`s-1`$ passive blocks; promote the remaining passive $`U`$ to the active group. The same argument proves (10)–(11), with active shadow $`X\oplus U^2`$ and an elementary active projection $`\overline W`$ of order $`2^{12}`$. The old $`\delta_W=1`$ graph need not give $`Z\le\overline W`$: its $`Z`$-coordinate can be accompanied by a coordinate in the newly active block. The automorphisms are $`S_5`$-equivariant automorphisms of the split passive factor, with all folder data transported; they do not identify arbitrary stabilizer graphs.

Thus the sole remaining original **outer-collision test** reduces to an active shadow $`X\oplus U^2`$, independent of $`b`$. This is not a classification or a quotient-loop construction. The active group and extension classes, $`\tau`$-shears, $`\overline W`$, the full radical section, and the generation, isomorphism and normal-subloop tests remain. The added component and complement computations are in the extended verifier [dependency/context not reproduced in this update: `../code/verify_bruck_one_m_noncentral.py`]; the exact-source independent reviews of this continuation are recorded below.

At exact source `ad3426f804a1c2c32d379a27191a35fdb5886dea`, GPT-6.1 Terra reviewers [model reviewer] and [model reviewer] independently accepted the complete outer-collision continuation and expanded verifier, conditional on the earlier `39e524307bcd8036c7d9e1908a67f6c16252957f` reduction and its pinned module/folder inputs. Both read and reran the exact certificate: [model reviewer] used Python 3.12.14 and [model reviewer] used Python 3.12.13. They checked the displacement bound, complete fixed-component enumeration, complement normalization, original-folder collision equivalence, zero/unit-row exclusions, and exceptional promotion retaining the possible Z graph. Neither review certifies realization of the exceptional extension, a quotient folder, full sections or a classification; no fresh primary-source audit or formal verification was performed.

## Exclusion of the exceptional graph case

**Independently reviewed continuation.** Under the hypotheses of (1), including arbitrary $`b\ge1`$, the remaining exceptional case is also impossible. Consequently the preceding results and this argument exclude every such envelope with $`\Phi(P)\cong M`$. This is a bounded conclusion, not a statement about other Frattini modules. The review at `ad3426f804a1c2c32d379a27191a35fdb5886dea` predates this section and the additional verifier assertions below.

Write $`s=b-1`$, and retain the active $`U`$ from the epsilon row. The exceptional singular plane is exactly

```math
X_S\oplus\mathop{\mathrm{soc}}\nolimits(U), \tag{12}
```

where $`X_S`$ is the nonfixed four-dimensional $`F`$-simple subspace of $`X`$. Indeed the epsilon cross polar vanishes on $`X\times\mathop{\mathrm{soc}}\nolimits(U)`$, while $`q_X=0`$; the unique $`X`$-projecting singular plane identified above is therefore (12). The extended verifier also checks this equality directly for both $`X`$. In particular the shadow of $`W`$ lies in $`X\oplus\mathop{\mathrm{soc}}\nolimits(U)\oplus U^s`$.

Let $`E_R`$ be the preimage in $`P`$ of $`\mathop{\mathrm{soc}}\nolimits(U)\oplus U^s`$, and $`E`$ the preimage of $`X\oplus\mathop{\mathrm{soc}}\nolimits(U)\oplus U^s`$. The epsilon cross map and all its polar terms vanish on the indicated radical, and $`q_X=0`$; hence $`E_R`$ is elementary abelian and central in $`P`$, and $`E`$ is elementary abelian. Both are normal in $`G`$, and $`W\le E`$. Since the two simple modules lie in distinct blocks, the extension of $`N\oplus U^s`$ by $`M`$ splits as an $`S_5`$-module, giving

```math
E_R\cong M\oplus N\oplus U^s. \tag{13}
```

Here projectivity splits the $`U`$-summands; the distinct-block decomposition splits the $`N`$-summand. These are the same block and projectivity inputs pinned above. The involution $`\tau`$ fixes $`E_R`$ pointwise: it fixes $`Z`$ and its quotient by $`Z`$, and the resulting shear is an $`S_5`$-map $`N\oplus U^s\to M`$, necessarily zero by the distinct blocks. The shear is equivariant because $`E_R`$ centralizes $`P`$ and $`\tau`$ induces the identity modulo $`P`$.

Choose any selected marked involution $`\lambda`$ over a transposition $`t`$. Its conjugation action on $`E_R`$ is the action of $`t`$, so

```math
\mathop{\mathrm{rank}}\nolimits(1+\lambda)|_{E_R}=2+1+4s=4s+3.
```

On $`E/E_R\cong X`$, its displacement has rank $`2`$ for $`J`$ and $`3`$ for $`P_6`$. Consequently

```math
\mathop{\mathrm{rank}}\nolimits(1+\lambda)|_E\ge 4s+3+\rho_X,\qquad
 \dim E=\dim X+8s+8,\qquad \dim W=4s+8. \tag{14}
```

The first inequality uses the image in the quotient and the displacement image already inside $`E_R`$. Thus $`\dim W+\mathop{\mathrm{rank}}\nolimits(1+\lambda)|_E\ge\dim E`$ for either $`X`$.

There is one further codimension. The ordinary six-point augmentation descends to $`J`$, because the all-ones vector has even weight, and is $`S_5`$-invariant. Extend it from $`X`$ to $`E`$ through $`E/E_R`$. Both $`W`$ and $`(1+\lambda)E`$ lie in its kernel: the $`X`$-projection of $`W`$ is $`X_S`$, and the augmentation kills $`(1+t)X`$. The verifier checks both containments and the ranks for the explicit paired models. Since the kernel has codimension one, (14) forces

```math
W\cap(1+\lambda)E\ne1.
```

A nonidentity element of this intersection conjugates $`\lambda`$ to a distinct marked element with the same $`H`$-coset, contradicting transversality. This takes place in the original group and uses neither a quotient folder nor a split extension over $`S_5`$. Together with the already reviewed zero- and unit-row exclusions and the epsilon $`q_X=1`$ exclusion, it proves the stated bounded exclusion, with the exact-source reviews recorded below.

## Corollary for no projective blocks

**Independently reviewed.** The same exclusion holds when $`b=0`$, so the bounded conclusion covers $`X=J`$ or $`P_6`$ and every $`b\ge0`$. This case is independent of the active-block splitting above. With $`V=X`$, the original bounds (3), corefreeness $`W\cap Z=0`$, and the $`F`$-module structure of $`X`$ force $`|W|=2^4`$ and no fixed $`F`$-summand in its shadow, exactly as in the derivation of (4). Thus the shadow is the unique nonfixed $`F`$-simple submodule $`X_S`$.

The quadratic map $`q:X\to M`$ is nonzero because its values generate $`Z=M`$. Its space has dimension one by the fixed-component computation (5), and the verifier checks that its nonzero member is nonzero on each nonzero vector of $`X_S`$. But every square of an element of $`W`$ is trivial, so its shadow must be $`q`$-singular. This contradiction excludes $`b=0`$ for both choices of $`X`$. No nonexistent $`U`$-block or passive splitting is used.

At exact source `49b2a2c248d1b492fa0b35d5784999e7f8854000`, GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted the complete exceptional-case exclusion and the separate b=0 corollary. All three read and reran the exact expanded verifier with Python 3.12.14. They checked the exceptional plane, actual S₅-module splitting, τ-fixed central subgroup, displacement ranks, augmentation-kernel dimension contradiction and original-folder collision, under the reviewed `39e524307bcd8036c7d9e1908a67f6c16252957f`/`ad3426f804a1c2c32d379a27191a35fdb5886dea` reductions and their block/projectivity/envelope inputs. The conclusion covers Φ(P)≅M and V=J⊕Uᵇ or P₆⊕Uᵇ for every b≥0 under the stated class/exponent hypotheses. Other Frattini modules and radical classes remain outside it; no fresh primary-source audit or formal verification was performed.
