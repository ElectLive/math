# Central socle shadows in an N-Frattini envelope

**Theorem with scoped independent reviews, continuing [0323:C0010](../../claims/0010.md).** Retain the faithful simple nonassociative Bruck-envelope hypotheses and notation of [the marked-rank theorem](bruck-n-frattini-marked-rank.md), at exact source the recorded source revision: $`A=G/P\cong S_5`$, $`P`$ has class at most two and exponent at most four, $`Z=\Phi(P)\cong N`$,

```math
V=P/Z\cong X\oplus U^b,\qquad X\in\{J,P_6\},
```

$`W=H\cap P`$, and $`q:V\to Z`$ has polar $`\beta`$. In particular $`W`$ is elementary abelian and $`W\cap Z=1`$, the canonical involution $`\tau`$ fixes $`H,V,Z`$ pointwise, and the marked-rank theorem gives

```math
\beta(v,tv)\in(1+t)Z\quad\text{for every }v\in V,                \tag{1}
```

for a transposition $`t\in S_5`$. The $`N`$-block decomposition used below is [the reviewed block theorem](bruck-s5-module-blocks.md), at the recorded source revision. The quadratic-support rank argument is [the reviewed support theorem](bruck-n-frattini-quadratic-support.md), at the recorded source revision. The present deduction has the scoped exact-source reviews below. It gives a necessary condition, not an envelope classification.

## The actual-lift obstruction

Let $`\overline W\le V`$ be the injective shadow of $`W`$. If an $`S_5`$-submodule

```math
T\le \overline W\cap\mathop{\mathrm{soc}}\nolimits(U^b)
```

is contained in the polar radical $`\mathop{\mathrm{rad}}\nolimits(\beta)=\{v:\beta(v,V)=0\}`$, then $`T=0`$.

Indeed, $`q`$ vanishes on $`\mathop{\mathrm{soc}}\nolimits(U^b)`$: by the reviewed fixed-component calculation, the individual square terms are top projections, and every pair term vanishes on socle pairs. Let $`E_T`$ be the full preimage of $`T`$ in $`P`$. It is elementary abelian, because its elements have square zero, and it centralizes $`P`$, because $`T`$ is polar-radical. Thus conjugation by $`G`$ makes $`E_T`$ an actual $`\mathbb F_2S_5`$-module, fitting into

```math
0\longrightarrow Z\longrightarrow E_T\longrightarrow T\longrightarrow0.
                                                                    \tag{2}
```

Write $`T\cong N^c`$. Since $`T\le\overline W`$ and $`W\cap Z=1`$, the subgroup $`W_T=W\cap E_T`$ maps isomorphically onto $`T`$. Therefore $`E_T=Z\oplus W_T`$ as vector spaces. The canonical involution fixes both $`Z`$ and the actual subgroup $`W_T`$ pointwise, hence fixes all of $`E_T`$ pointwise. No $`S_5`$-splitting of (2) is assumed at this stage.

Let $`\lambda`$ be a selected marked involution above $`t`$, with marked map $`\ell_\lambda`$ as in the cited theorem. Each $`U`$ restricts freely to $`\langle t\rangle`$; consequently

```math
C_T(t)\subseteq C_{U^b}(t)=(1+t)U^b\subseteq(1+t)V.
```

Equation (1) and the marked identity $`\ell_\lambda((1+t)v)=\beta(v,tv)\pmod{(1+t)Z}`$ show that $`\ell_\lambda`$ vanishes on $`C_T(t)`$. Thus every vector of $`C_T(t)`$ has a $`\lambda`$-fixed lift in $`E_T`$, and the kernel of this fixed-lift map is $`C_Z(t)`$. Since $`\dim C_N(t)=3`$,

```math
\dim C_{E_T}(\lambda)=3c+3,\qquad
 \mathop{\mathrm{rank}}\nolimits_{E_T}(1+\lambda)=c+1.                         \tag{3}
```

Because $`\tau`$ fixes $`E_T`$ pointwise and $`P`$ centralizes $`E_T`$, the action of $`\lambda`$ on $`E_T`$ is exactly the action of its image $`t\in S_5`$.

The reviewed $`N`$-block theorem says an $`N`$-only $`S_5`$-module is a direct sum of copies of $`N`$ and $`U`$. In the extension (2), whose kernel is one simple $`N`$ and whose quotient is semisimple, this leaves exactly the two types

```math
E_T\cong N^{c+1}\quad\text{or}\quad U\oplus N^{c-1}.
```

The transposition ranks on $`N,U`$ are 1 and 4, respectively. The latter type has rank $`c+3`$, contradicting (3); therefore $`E_T\cong N^{c+1}`$ as an $`S_5`$-module.

The group $`F=H/W\cong F_{20}`$ stabilizes $`W_T`$, and $`\mathop{\mathrm{End}}\nolimits_F(N)=\mathop{\mathrm{End}}\nolimits_{S_5}(N)=\mathbb F_2`$. Hence every $`F`$-submodule of $`N^{c+1}`$ is determined by a binary multiplicity subspace and is automatically $`S_5`$-stable. Thus $`W_T`$ is normal in $`G`$. Core-freeness of $`H`$ forces $`W_T=1`$, so $`T=0`$.

## Consequences for the polar map

The intersection $`\overline W\cap\mathop{\mathrm{soc}}\nolimits(U^b)`$ is an $`F`$-submodule of $`N^b`$. The same endomorphism-ring argument makes it an $`S_5`$-submodule. Its intersection with $`\mathop{\mathrm{rad}}\nolimits(\beta)`$ is therefore an $`S_5`$-submodule, and the theorem yields

```math
\overline W\cap\mathop{\mathrm{soc}}\nolimits(U^b)\cap\mathop{\mathrm{rad}}\nolimits(\beta)=0.
                                                                    \tag{4}
```

Equivalently, the $`S_5`$-equivariant map

```math
v\longmapsto\beta(v,-)\in\mathop{\mathrm{Hom}}\nolimits_{\mathbb F_2}(V,Z)
```

is injective on $`\overline W\cap\mathop{\mathrm{soc}}\nolimits(U^b)`$. This assertion does not require the whole socle to be polar-radical.

Suppose now $`X=J`$ and write the $`U`$-pair coefficient matrix as $`C=C_0+\varepsilon C_1`$ in the reviewed support theorem. If $`C_0=0`$, the whole $`\mathop{\mathrm{soc}}\nolimits(U^b)`$ is polar-radical: the $`U`$-pair maps have zero socle restriction after multiplication by $`\varepsilon`$, and the $`J`$-to-$`U`$ cross-map space is annihilated by precomposition with $`\varepsilon`$. Equation (4) gives $`c=0`$, where $`c`$ is the socle-intersection multiplicity of the support theorem. Its residual polar-rank argument then yields $`\mathop{\mathrm{rank}}\nolimits(C_1)\le2c=0`$, so

```math
C_0=0\quad\Longrightarrow\quad c=0\ \text{and}\ C_1=0
 \qquad (X=J).                                                     \tag{5}
```

This conclusion concerns the quadratic datum and the actual stabilizer shadow under the stated hypotheses. It does not eliminate the remaining $`J`$-to-$`U`$ cross terms or classify the group extension, marked section, or loop.

## Invariant functionals and an excluded J branch

**Further deductions with the scoped reviews below.** These use the preceding actual-lift lemma, the marked-rank and quadratic-component inputs already cited, and the central-extension detection used in [the principal-envelope bound](bruck-s5-principal-envelope-bound.md), independently reviewed at the recorded source revision. In particular, detection of a central $`C_2`$-extension of $`S_5`$ by its restrictions to $`F_{20}`$ and a transposition was used at the recorded source revision and the recorded source revision, under the source qualifications recorded in the principal-envelope manuscript. The following extends its elementary-radical pushout argument to the present possibly nonabelian $`P`$; that extension has the scoped reviews below.

First, restriction to $`\overline W`$ is injective on $`S_5`$-invariant linear functionals $`V\to\mathbb F_2`$. Suppose a nonzero invariant functional $`a`$ vanishes on $`\overline W`$, and let $`L`$ be the kernel of its pullback $`P\to\mathbb F_2`$. Then $`L\lhd G`$, $`Z\le L`$, and $`G/L`$ is a central $`C_2`$-extension of $`S_5`$. The image of $`H`$ complements its central kernel over $`F_{20}`$, because $`H\cap P=W\le L`$.

The involution $`\tau`$ preserves $`L`$ and acts trivially on both the central kernel and the $`S_5`$ quotient. Its induced automorphism of $`G/L`$ is therefore described by a derivation $`S_5\to C_2`$. Actual $`H`$-lifts are fixed by $`\tau`$, so this derivation vanishes on $`F_{20}`$. The only nonzero homomorphism $`S_5\to C_2`$ is sign, whose restriction to $`F_{20}`$ is nonzero; hence $`\tau`$ acts trivially on $`G/L`$. A selected marked involution $`\widehat\tau k`$ above a transposition consequently gives an involutory transposition lift $`kL`$ in $`G/L`$. The cited detection forces $`G/L\cong C_2\times S_5`$.

A projection of this split quotient onto its central $`C_2`$, adjusted by sign if necessary, vanishes on the image of $`H`$ and is nonzero on $`P/L`$. Since $`K`$ generates $`G`$, it induces a nontrivial loop homomorphism to $`C_2`$: section multiplication changes a product representative only by an element of $`H`$. The loop has order at least $`[S_5:F_{20}]=6`$, so this contradicts simplicity. This proves injectivity.

For both $`X=J`$ and $`X=P_6`$, the six-point augmentation is a nonzero $`S_5`$-invariant functional; for $`J=\mathbb F_2^6/\langle\mathbf1\rangle`$ it descends because six is even. The $`F_{20}`$-fixed nontrivial-block part $`U^b`$ is zero, so injectivity forces a nonzero fixed vector in $`\overline W\cap X`$. The marked-rank alternatives then force the fixed dimension to be one and

```math
\dim W=4b+5.                                                      \tag{6}
```


Now suppose $`X=J`$ and $`C_0=0`$. The actual-lift obstruction and the reviewed residual-rank argument give $`c=0`$ and $`C_1=0`$, as in (5). Let $`a:J\to\mathbb F_2`$ be augmentation. The unique allowed $`J`$-to-$`U`$ cross-map is

```math
\beta(x,u)=a(x)\mathop{\mathrm{top}}\nolimits(u):
```

this map is nonzero and $`S_5`$-equivariant, and the reviewed component calculation gives a one-dimensional cross-map space. The fixed line of $`J|_{F_{20}}`$ has augmentation one: the singleton fixed by $`F_{20}`$ represents such a vector in $`J`$. Hence the fixed vector in $`\overline W`$ has augmentation one and has no $`U`$-component.

The nonfixed part of $`\overline W`$ has $`S`$-multiplicity $`b+1`$, while its intersection with $`\mathop{\mathrm{soc}}\nolimits(U^b)`$ is zero. Its projection to $`J_S\oplus\mathop{\mathrm{top}}\nolimits(U^b)`$ is therefore an isomorphism. In particular its projection to $`\mathop{\mathrm{top}}\nolimits(U^b)`$ is onto. Polar isotropy of $`\overline W`$, tested against the fixed vector, forces the entire $`J`$-to-$`U`$ cross row to vanish. The reviewed component calculation gives $`q|_J=0`$, and $`C_0=C_1=0`$, so $`q`$ is now just its binary row of $`U`$-top projections. Since $`q(\overline W)=0`$ and the top projection is onto, that row also vanishes. Thus $`q=0`$, contradicting $`\Phi(P)=P^2[P,P]=Z\cong N\ne0`$: the polar of the zero square map is zero as well.

Consequently the stated envelope hypotheses exclude

```math
X=J,\qquad C_0=0.                                                  \tag{7}
```

In particular they exclude $`X=J`$ with $`b=0`$ or $`b=1`$, since an alternating $`b\times b`$ matrix $`C_0`$ is then zero. This conditional exclusion does not address $`X=P_6`$ or the $`J`$-cases with nonzero residue polar matrix, with the scoped independent reviews recorded below.

## Independent review

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted the full manuscript, conditional on the pinned N-block, marked-rank, quadratic-component/support and central-extension detection inputs and their recorded source qualifications. All checked the actual elementary lift and transposition-rank splitting, the F20-to-S5 stability and core contradiction, the nonabelian-radical pushout including triviality of the induced involution and the actual transposition lift, the mandatory fixed dimension and the all-b J exclusion. No new computation was required or claimed. Their acceptance covers these necessary restrictions and exclusions, not the remaining P6 or nonzero-residue J branches, a fresh primary-source audit or formal verification.

## A rank bound for any stable stabilizer shadow

**Continuation with the scoped independent reviews below.** Retain all hypotheses and the reviewed mandatory dimension $`\dim W=4b+5`$ above. Let $`A_0\le\overline W`$ be any $`S_5`$-submodule. Then

```math
\mathop{\mathrm{rank}}\nolimits(1+t)|_{A_0}\le3.                              \tag{8}
```

This is an actual-lift condition; $`A_0`$ need not be polar-radical.

Indeed, let $`E_{A_0}`$ be the full preimage of $`A_0`$ in $`P`$, and put $`W_{A_0}=W\cap E_{A_0}`$. The latter maps isomorphically onto $`A_0`$, because $`A_0\le\overline W`$ and $`W\cap Z=1`$. As a group $`E_{A_0}=ZW_{A_0}`$ is elementary abelian: $`Z`$ is elementary and central in $`P`$, and $`W_{A_0}`$ is elementary. Both $`Z`$ and the actual subgroup $`W_{A_0}`$ are fixed pointwise by $`\tau`$, so $`\tau`$ fixes $`E_{A_0}`$ pointwise. This does **not** imply that $`P`$ centralizes $`E_{A_0}`$.

Fix a selected marked involution $`\lambda`$ above the transposition $`t`$. The marked-rank table and $`\dim W=4b+5`$ give $`\ell_\lambda=0`$ on all of $`C_V(t)`$. Since $`A_0`$ is $`S_5`$-stable, $`E_{A_0}`$ is $`\lambda`$-stable. Every element of $`C_{A_0}(t)`$ has a $`\lambda`$-fixed lift in $`E_{A_0}`$, and the kernel of the fixed-lift map is $`C_Z(t)`$. Therefore, writing

```math
D=(1+\lambda)E_{A_0},
```

we have

```math
\dim D=\mathop{\mathrm{rank}}\nolimits(1+t)|_{A_0}+1,
 \qquad D\cap Z=(1+t)Z.                                            \tag{9}
```

Here the action of $`\lambda`$ on the quotient $`A_0`$ is $`t`$; its action on the actual preimage $`E_{A_0}`$ can contain a nontrivial $`P`$-induced shear and is not identified with a pure $`t`$-action.

For each $`u\in(1+t)A_0`$, let $`w\in W_{A_0}`$ be its unique actual lift and choose $`d\in D`$ above $`u`$. The discrepancy

```math
\Delta(u)=w-d+(1+t)Z\in Z/(1+t)Z
```

is well-defined and linear by (9). If $`\Delta(u)=0`$, then $`w\in D`$. Every element of $`D`$ is the product of $`\lambda`$ with an $`E_{A_0}`$-conjugate of $`\lambda`$; hence $`W\cap D\ne1`$ would contradict the folder condition $`H\cap\Lambda^2=1`$. Thus $`\Delta`$ is injective. Its target has dimension $`\dim Z-\mathop{\mathrm{rank}}\nolimits(1+t)|_Z=4-1=3`$, proving (8).

As a conditional consequence, suppose $`X=J`$ and the whole $`J`$-summand lies in $`\overline W`$. The socle intersection $`T=\overline W\cap\mathop{\mathrm{soc}}\nolimits(U^b)\cong N^c`$ is $`S_5`$-stable by the $`F_{20}`$ multiplicity argument above. Hence $`A_0=J\oplus T`$ is a stable submodule of $`\overline W`$. The transposition ranks on $`J`$ and $`N`$ are 2 and 1, so (8) gives

```math
c\le1.                                                            \tag{10}
```

The hypothesis $`J\le\overline W`$ is essential to this corollary; neither (8) nor (10) asserts a classification of the remaining shadows or lifts. The new section has the exact-source reviews below.

## Nonsingular residue polar form in the J branch

**Continuation with the scoped independent reviews below.** Retain the hypotheses above, including the stable-shadow rank bound (8). Suppose $`X=J`$, $`b>0`$, and the residue $`C_0`$ of the alternating $`U`$-pair matrix is nonsingular. Then no such envelope exists. In particular $`b`$ is even and at least two. This extends the reviewed $`J,C_0=0`$ exclusion, but leaves nonzero singular $`C_0`$ open.

Let $`S=N|_{F_{20}}`$, let $`D=\mathbb F_2^b`$, and write the nonfixed part of $`\overline W`$ as $`S\otimes B`$, where

```math
B\le \mathbb F_2 J_S\oplus D_{\rm top}\oplus D_{\rm soc},
 \qquad \dim B=b+1.
```

The fixed augmentation-one vector supplied above belongs to $`J`$. The unique $`J`$-to-$`U`$ cross map is augmentation times top, so its restriction to $`J_S\times U|_{F_{20}}`$ vanishes. Thus polar isotropy of $`B`$ is governed on the $`U`$-multiplicities by the reviewed pair restrictions alone.

These restrictions separate two scalar alternating forms. More precisely, the two $`D_U\times D_U`$ restrictions of the $`U`$-pair maps are linearly independent, while every top–socle restriction is in the line of the $`\varepsilon`$-multiple and socle–socle restrictions vanish. Hence any polar-isotropic $`U`$-multiplicity subspace must be isotropic for

```math
d^TC_0d',\qquad
 d^TC_1d'+d^TC_0z'+z^TC_0d',                                    \tag{11}
```

where $`(d,z),(d',z')\in D_{\rm top}\oplus D_{\rm soc}`$. A choice of the independent pair-map basis can add a multiple of the first form to the second; this does not change their common isotropic subspaces. The second form is nondegenerate because its off-diagonal block $`C_0`$ is nonsingular. Its isotropic subspaces have dimension at most $`b`$.

The projection of $`B`$ to the $`2b`$-dimensional $`U`$-multiplicity space has dimension at least $`b`$, since its kernel lies in the one-dimensional $`J_S`$ multiplicity. By the previous paragraph its dimension is exactly $`b`$, and the kernel is all of $`J_S`$. Thus

```math
B=\mathbb F_2 J_S\oplus L,
 \qquad \dim L=b,                                                 \tag{12}
```

with $`L`$ isotropic for both forms (11).

Let $`T_0=\mathop{\mathrm{pr}}\nolimits_{\rm top}L\le D`$ and $`Z_0=L\cap D_{\rm soc}`$. The first form makes $`T_0`$ $`C_0`$-isotropic, and the top–socle part of the second gives $`Z_0\le T_0^{\perp_{C_0}}`$. Since $`\dim L=b`$, both spaces on the latter inclusion have dimension $`b-\dim T_0`$, so equality holds. In particular $`T_0\le T_0^{\perp_{C_0}}=Z_0`$. The dual-number operator $`\varepsilon`$ sends $`(d,z)`$ to $`(0,d)`$; it therefore preserves $`L`$. Consequently $`S\otimes L`$ is an $`S_5`$-submodule of $`U^b`$, rather than merely an $`F_{20}`$-submodule. To see this directly in the chosen complement/socle coordinates, both diagonal actions on one U are the N-action, and the off-diagonal action is a linear map from top to socle. The same maps act on every copy of U. The diagonal terms preserve S tensor L, and the off-diagonal term preserves it whenever epsilon L is contained in L. Thus epsilon-stability of the multiplicity subspace suffices; no S5-stability of the chosen F20 complement is assumed.

The fixed line and $`J_S`$ together span $`J`$, so (12) shows that $`\overline W`$ contains the $`S_5`$-submodule $`J\oplus(S\otimes L)`$. If $`t=\dim T_0`$, the latter $`U`$-part is isomorphic to $`U^t\oplus N^{b-2t}`$. Its transposition rank is $`b+2t`$, so the total rank is $`2+b+2t\ge4`$. This contradicts the actual-lift rank bound (8), which requires rank at most 3. No identification of a marked involution with a pure transposition on an actual lift is used here.

Combining this exclusion with the reviewed $`J,C_0=0`$ case leaves only $`X=J`$ with nonzero singular $`C_0`$ within the displayed $`N`$-Frattini hypotheses. The $`X=P_6`$ branch is not addressed by this argument.

## Stable J inside the shadow

**Continuation with the scoped independent reviews below.** Under the same hypotheses and rank bound (8), no $`X=J`$ envelope has the whole $`J`$-summand inside $`\overline W`$, for any $`C_0`$. The reviewed $`C_0=0`$ exclusion handles that case, so suppose $`\mathop{\mathrm{rank}}\nolimitsC_0=2r>0`$.

Put $`D=\mathbb F_2^b`$, $`K_0=\mathop{\mathrm{rad}}\nolimits(C_0)`$, and $`k=\dim K_0=b-2r`$. Since $`J\le\overline W`$, the nonfixed multiplicity shadow is $`B=\mathbb F_2J_S\oplus L`$, where $`L\le D_{\rm top}\oplus D_{\rm soc}`$ has dimension $`b`$. Write

```math
T_0=\mathop{\mathrm{pr}}\nolimits_{\rm top}L,\qquad
 S_0=L\cap D_{\rm soc},\qquad
 h=\dim(T_0\cap K_0),\qquad
 u=\dim T_0-h.
```

The reviewed pair-map restrictions in the preceding section make the image $`\overline T_0`$ of $`T_0`$ in $`D/K_0`$ symplectically isotropic and give $`\overline S_0\le\overline T_0^{\perp}`$. The socle directions in $`K_0`$ are polar-radical, so the reviewed central-socle obstruction gives $`S_0\cap K_0=0`$: these are pure socle directions in $`\overline W`$, because $`B`$ contains $`J_S`$. Hence

```math
\dim S_0=b-u-h\le2r-u,
```

which forces $`h=k`$ and equality. Thus $`T_0`$ contains $`K_0`$, $`\overline S_0=\overline T_0^{\perp}`$, and $`\dim(S_0\cap T_0)=u`$.

Choose a basis $`d_1,\ldots,d_u`$ of $`S_0\cap T_0`$, and choose $`(d_i,z_i)\in L`$. Both $`(d_i,z_i)`$ and $`(0,d_i)`$ belong to $`L`$, and $`\varepsilon(d_i,z_i)=(0,d_i)`$. They span $`u`$ free dual-number summands. Extending their socle vectors inside $`S_0`$ gives $`2r-2u`$ further trivial dual-number summands. Therefore $`\overline W`$ contains the $`S_5`$-submodule

```math
J\oplus U^u\oplus N^{2r-2u},
```

whose transposition rank is $`2+4u+(2r-2u)=2+2r+2u\ge4`$. This contradicts (8). The conclusion uses an $`S_5`$-stable submodule inside the shadow, not an assertion that the whole $`L`$ is $`\varepsilon`$-stable. It does not cover a shadow that projects onto $`J_S`$ as a nontrivial graph without containing $`J_S`$.

## Independent review of stable shadows

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted the stable-shadow rank bound and both appended J exclusions, conditional on the earlier central-socle/invariant-functional, marked-rank and pair-restriction inputs. All checked the actual elementary preimage with its possible P-induced shear, the discrepancy injection, the two scalar alternating forms, the nonsingular dimension bound and the explanation of epsilon-stability. They also checked the pure-socle condition and equality argument in the singular case when the whole J is in the shadow, and the constructed stable U/N summands. No new computation was required. Their scope excludes nonsingular C0 and whole-J shadows, not every J case or the exceptional mixed graph.

