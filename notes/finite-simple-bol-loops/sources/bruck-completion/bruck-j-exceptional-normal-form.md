# A bounded exceptional-graph normal form for the J branch

**Theorem with scoped independent reviews, continuing of [0323:C0010](../../claims/0010.md).** Retain the faithful simple nonassociative Bruck-envelope and $`N`$-Frattini hypotheses of [the central-socle manuscript](bruck-n-central-socle-obstruction.md): $`G/P\cong S_5`$, $`P`$ has class at most two and exponent at most four, $`Z=\Phi(P)\cong N`$, and $`V=P/Z\cong J\oplus U^b`$. The central-socle, invariant-functional and $`J,C_0=0`$ restrictions are reviewed at the recorded source revision; the stable-shadow transposition-rank bound and whole-$`J`$ exclusion are reviewed at the recorded source revision. The pair-map restrictions and passive-group cohomology interfaces are pinned in [the quadratic-support theorem](bruck-n-frattini-quadratic-support.md) and [the passive reduction](bruck-n-frattini-passive-reduction.md), including their review at the recorded source revision.

The conclusion is that every surviving $`J`$-branch envelope has $`b\ge3`$ and, after the specified coordinate changes and a $`\tau`$-fixed conjugation, its actual group, involution and stabilizer have at most three active $`U`$-blocks. The remaining $`U`$-blocks occur as a standard passive bulk. This does not give a product decomposition of $`K`$, a quotient loop, or a classification of the surviving folders. The deduction has the scoped exact-source reviews below.

## The exceptional graph

Write $`W=H\cap P`$, $`\overline W\le V`$, and $`F=H/W\cong F_{20}`$. The reviewed pushout gives $`\dim W=4b+5`$; the fixed part of its shadow is the augmentation-one fixed line of $`J`$. Let $`S=N|_F`$, put $`D=\mathbb F_2^b`$, and let the nonfixed shadow be $`S\otimes B`$, with

```math
B\le\mathbb F_2J_S\oplus D_{\rm top}\oplus D_{\rm soc},
 \qquad\dim B=b+1.
```

The reviewed whole-$`J`$ exclusion implies $`B\cap\mathbb F_2J_S=0`$. Thus $`B`$ is the graph of a linear functional $`\varphi:L\to\mathbb F_2`$ over its $`(b+1)`$-dimensional projection $`L\le D_{\rm top}\oplus D_{\rm soc}`$.

Let $`C_0`$ be the residue of the alternating $`U`$-pair matrix, with rank $`2r`$, radical $`K_0`$ of dimension $`k=b-2r`$, and quotient $`\bar D=D/K_0`$. The reviewed $`C_0=0`$ exclusion gives $`r>0`$. Write

```math
T_0=\mathop{\mathrm{pr}}\nolimits_{\rm top}L,\quad
 S_0=L\cap D_{\rm soc},\quad
 h=\dim(T_0\cap K_0),\quad
 u=\dim T_0-h.
```

The independent reviewed pair restrictions imply $`\bar T_0`$ is symplectically isotropic and $`\bar S_0\le\bar T_0^\perp`$. The central-socle obstruction applies to **pure** socle vectors of $`B`$: its restriction makes $`\varphi`$ injective on $`S_0\cap K_0`$. Thus $`\delta=\dim(S_0\cap K_0)\le1`$. Since

```math
\dim S_0=b+1-u-h,\qquad
 \dim\bar S_0=\dim S_0-\delta\le2r-u,
```

we have $`h+\delta\ge k+1`$. Therefore $`h=k`$, $`\delta=1`$, $`T_0`$ contains $`K_0`$, and $`\bar S_0=\bar T_0^\perp`$.

It follows that $`\dim(S_0\cap T_0)=u+1`$, and $`\varphi`$ has a $`u`$-dimensional kernel on the pure socle vectors there. For a basis $`d_i`$ of that kernel, choose $`(d_i,z_i)\in L`$ and add the unique nonzero element of $`S_0\cap K_0`$, if necessary, to make $`\varphi(d_i,z_i)=0`$. The resulting pure $`U`$-vectors and their $`\varepsilon`$-images give $`U^u`$ in the shadow. Extending their socles within $`\ker(\varphi|_{S_0})`$ gives $`N^{2r-2u}`$. These form an actual $`S_5`$-submodule of the shadow with transposition rank $`2r+2u`$. The reviewed rank bound is 3; since $`r>0`$, it forces

```math
r=1,\qquad u=0,\qquad T_0=K_0,\qquad \dim S_0=3.              \tag{1}
```

Thus $`C_0`$ has rank two, $`b\ge3`$, and precisely one radical-socle direction is mixed with $`J_S`$. This argument does not assume that a projected socle vector in the graph is pure.

## Quadratic and shadow coordinates

The fixed vector in $`\overline W`$ has augmentation one and no $`U`$-component. Its polar with $`\overline W`$, whose top is $`K_0`$, gives $`r_J|_{K_0}=0`$ for the binary $`J`$-to-$`U`$ cross row. Polar isotropy on the top-$`K_0`$ shadow gives $`C_1|_{K_0\times K_0}=0`$: $`C_0`$ vanishes there and the $`J_S`$-to-$`U`$ cross term vanishes.

Choose $`D=A_0\oplus K_0`$, $`\dim A_0=2`$, with $`C_0=J_2\oplus0`$, and write

```math
C_1=\begin{pmatrix}A&B_0\\B_0^T&0\end{pmatrix}.
```

For a dual-number change $`I+\varepsilon X`$, the new coefficient is $`C_1+X^TC_0+C_0X`$. Choose the active-to-radical block of $`X`$ to remove $`B_0`$, and its active square block to remove $`A`$; the latter is possible because $`X\mapsto X^TJ_2+J_2X`$ maps onto the one-dimensional space of alternating $`2\times2`$ matrices. Thus $`C=J_2\oplus0`$. The $`J`$-cross row is unchanged because its coefficient module is $`R/(\varepsilon)`$. The quadratic diagonal correction to the $`U`$-square row $`\ell`$ vanishes on $`K_0`$, since no $`C_0`$ entry is incident to a radical coordinate. Testing $`q(\overline W)=0`$ on nonfixed shadow vectors with arbitrary top in $`K_0`$ then gives $`\ell|_{K_0}=0`$. Hence $`q`$ and $`\beta`$ are supported on $`J\oplus U^2`$.

A $`C_0`$-preserving binary change of block form $`\left(\begin{smallmatrix}I&0\\M&I\end{smallmatrix}\right)`$ removes the $`K_0`$-socle components from the two pure active-socle generators. Choose a basis of $`K_0`$ making the exceptional mixed line $`\mathop{\mathrm{soc}}\nolimits(U_3)`$. For each top-$`K_0`$ generator, adding that exceptional socle graph removes its $`J_S`$ coefficient; subtracting the pure active-socle generators removes its active-socle components, and an $`\varepsilon`$-shear with image in $`K_0`$ then removes its remaining socle graph. Such shears preserve $`C=J_2\oplus0`$ and do not introduce a square or cross row on $`K_0`$. The resulting **shadow**, not yet an actual subgroup decomposition, is

```math
\overline W=\langle f\rangle\oplus
 \mathop{\mathrm{graph}}\nolimits(J_S\leftrightarrow\mathop{\mathrm{soc}}\nolimits(U_3))
 \oplus\mathop{\mathrm{soc}}\nolimits(U_1)\oplus\mathop{\mathrm{soc}}\nolimits(U_2)
 \oplus\bigoplus_{i=3}^b D_i,                                    \tag{2}
```

where $`f`$ is the augmentation-one $`F`$-fixed vector in $`J`$, and each $`D_i`$ is the chosen $`F`$-stable top complement to the socle in $`U_i`$.

## Actual passive subgroup and stabilizer

Put $`Y=\bigoplus_{i=4}^b U_i`$, allowing $`Y=0`$, and let $`P_0`$ be the full preimage in $`P`$ of $`J\oplus U_1\oplus U_2\oplus U_3`$. The preimage $`E_Y`$ of $`Y`$ is elementary abelian and central in $`P`$, because both $`q`$ and $`\beta`$ vanish on $`Y`$. It is an actual $`S_5`$-module extending $`Y`$ by $`Z`$; projectivity of $`U`$ gives an $`S_5`$-equivariant complement.

The map $`p\mapsto\tau(p)p^{-1}`$ induces a linear shear $`Y\to Z`$, independent of the lift because $`\tau`$ fixes $`Z`$. It is $`S_5`$-equivariant here because $`E_Y`$ centralizes $`P`$ and $`\tau`$ is the identity on $`G/P`$. The actual subgroup $`W`$ supplies lifts of the full top $`F`$-complements $`D_i`$, and $`\tau`$ fixes those lifts and $`Z`$. Every $`S_5`$-map $`U\to N`$ is a scalar multiple of top and restricts nontrivially to $`D_i`$; hence this shear vanishes on $`Y`$. Thus $`\tau`$ fixes all of $`E_Y`$ pointwise.

For each $`i\ge4`$, the actual $`W`$-lift of $`D_i`$ is a graph over $`D_i`$ with values in $`Z`$. It is $`F`$-equivariant because $`W`$ is normalized by $`H`$, and $`\mathop{\mathrm{End}}\nolimits_F(S)=\mathbb F_2`$. Adjust the chosen $`S_5`$-equivariant $`U_i`$-complement by that scalar multiple of $`\mathop{\mathrm{top}}\nolimits:U_i\to Z`$. This makes $`D_i`$ lie in $`W`$ literally, preserves normality and $`\tau`$-fixedness of the passive complement, and does not alter $`P_0`$. Denote the adjusted direct sum by $`Y_0`$, and put $`T_{\rm std}=\bigoplus_{i=4}^b D_i`$. Then

```math
P=P_0\times Y_0,\qquad W=(W\cap P_0)\oplus T_{\rm std}.       \tag{3}
```

The central graph on the active part remains unrestricted.

As in the reviewed passive-group reduction, $`H^2(S_5,Y_0)=0`$ gives a complement to $`Y_0`$ in $`G/P_0`$, with full preimage $`E`$. Projectivity of $`U`$ supplies the cohomology vanishing. The actual $`\tau`$-fixed $`H`$-lifts over $`F`$, together with $`Y_0^F=0`$ and $`H^1(S_5,Y_0)=0`$, make this complement $`\tau`$-stable. Therefore

```math
G=E\ltimes Y_0,\qquad E\cap P=P_0,\qquad \tau(E)=E,\quad\tau|_{Y_0}=1.
                                                                    \tag{4}
```

In the preimage of $`F`$, the image of $`H`$ in $`F\ltimes(Y_0/T_{\rm std})`$ is a complement, by (3). The quotient is a direct sum of copies of the projective $`F`$-simple $`S`$, so $`H^1(F,Y_0/T_{\rm std})=0`$. Conjugating by an element of $`Y_0`$, which is fixed by $`\tau`$, kills this complement cocycle and gives

```math
H=(H\cap E)\ltimes T_{\rm std}.                                   \tag{5}
```

Every change above is an explicit module-coordinate change, complement adjustment, or conjugation in the original group. In particular, (5) is an actual stabilizer statement, not only a statement about its shadow.

The remaining section $`K`$, its original conjugate-transversal condition, the active central graphs and extension classes, and loop isomorphism data have not been reduced to a product. No quotient of the folder is asserted to be a loop. The bounded active reduction has the scoped independent reviews below.

## Independent review

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted the full normal-form proof, conditional on the pinned actual-lift, marked-rank, pair-map, projectivity and envelope inputs. All checked the pure-socle qualification, graph dimension equalities and construction of the stable U/N summands; the dual-number and binary coordinate changes; and the actual passive subgroup, involution shear, central graph adjustments and group/stabilizer complement arguments. No new computation was required. Their scope is at most three active U-blocks for G, tau and H, not a decomposition of K, existence of the remaining folders or a complete classification.

