# A conditional passive-group reduction for N-Frattini envelopes

**Theorem with the scoped independent reviews below.** This is a continuation of [0323:C0010](../../claims/0010.md). Let $`(G,H,K)`$ be the faithful canonical envelope of a finite simple nonassociative Bruck loop of 2-power exponent. Put $`P=O_2(G)`$, and suppose $`P`$ has class at most two and exponent at most four, $`G/P\cong S_5`$, $`Z=\Phi(P)\cong N`$, and

```math
V=P/Z\cong X\oplus U^b,\qquad X\in\{J,P_6\}.
```

Here $`N`$ is the deleted five-point simple, $`U=N\otimes\mathbb F_2[C_2]`$ with sign action on the second factor, and $`J,P_6`$ are the six-point modules in [the marked-rank source](bruck-n-frattini-marked-rank.md). Use the independently reviewed [quadratic-support theorem](bruck-n-frattini-quadratic-support.md): after an $`S_5`$-module coordinate change, the square map and its polar are supported on $`X\oplus U^a`$, with $`a\le\min(b,14)`$. Under that input there is a further decomposition, with $`a'\le\min(b,15)`$, and subgroups $`P_0,Y_0,E`$ such that

```math
P=P_0\times Y_0,\quad Y_0\cong U^{b-a'},\quad
 G=E\ltimes Y_0,\quad E\cap P=P_0,\quad \tau(E)=E,\quad \tau|_{Y_0}=1. \tag{1}
```

Here $`\tau`$ is the canonical involutory automorphism. This is a reduction of the group and its marked automorphism. It does **not** assert that $`H`$, $`K`$, or the original folder is a product, nor that any projection defines a quotient loop. Their stabilizer and section graph data remain part of the problem.

The support theorem depends on the lifted-socle bound at exact source the recorded source revision, independently reviewed separately. The canonical-inversion and envelope inputs are as in the [marked-rank source](bruck-n-frattini-marked-rank.md) at the recorded source revision. The projectivity and cohomology inputs are the reviewed [N-block manuscript](bruck-s5-module-blocks.md) at the recorded source revision; the analogous passive group and involution argument for a different Frattini block is reviewed in [the one-M noncentral reduction](bruck-one-m-noncentral-reduction.md) at the recorded source revision. The same-block shear argument and its use with the support theorem have the exact-source reviews below.

## Central preimage and the involution shear

Choose a support decomposition $`V=V_0\oplus Y`$, where $`V_0=X\oplus U^a`$ and $`Y=U^s`$. For every $`y\in Y`$ and $`v\in V`$, the hypothesis gives $`q(y)=0`$ and $`\beta(y,v)=0`$. Thus the preimage $`E_Y`$ of $`Y`$ in $`P`$ is elementary abelian and central in $`P`$. Conjugation by $`G`$ makes it an $`S_5`$-module, and its exact sequence

```math
0\longrightarrow Z\longrightarrow E_Y\longrightarrow Y\longrightarrow0
```

splits $`S_5`$-equivariantly because $`U`$ is projective. Here this splitting is a module splitting; it does not require $`P`$ itself to be abelian.

The canonical involution fixes $`V`$ and $`Z`$ pointwise, as in the cited marked-rank source. Consequently $`\tau(e)e^{-1}\in Z`$ defines a linear shear $`d:Y\to Z`$, independent of the choice of section. It is $`S_5`$-equivariant: $`\tau(g)g^{-1}\in P`$, and $`P`$ centralizes $`E_Y`$. By the reviewed N-block description,

```math
\mathop{\mathrm{End}}\nolimits_{S_5}(U)\cong R=\mathbb F_2[\varepsilon]/(\varepsilon^2),\qquad
 \mathop{\mathrm{Hom}}\nolimits_{S_5}(U,N)\cong\mathbb F_2,
```

and precomposition by $`R`$ on this Hom space is reduction modulo $`\varepsilon`$. Thus $`d`$ is a binary row of length $`s`$. The reduction map $`\mathop{\mathrm{GL}}\nolimits_s(R)\to\mathop{\mathrm{GL}}\nolimits_s(\mathbb F_2)`$ is surjective, so a change of the passive $`U`$-coordinates makes this row zero or supported on one coordinate. Such a change preserves the vanishing of $`q`$ and $`\beta`$ on the entire passive space. If needed, move that one coordinate into $`V_0`$; the enlarged active space has at most 15 $`U`$-summands. Denote the remaining passive space by $`Y'`$.

Choose an $`S_5`$-equivariant section $`Y'\to E_Y`$, and let its image be $`Y_0`$. The shear vanishes on $`Y'`$, so $`\tau`$ fixes $`Y_0`$ pointwise. The equivariance makes $`Y_0`$ normal in $`G`$, and it centralizes $`P`$. Let $`P_0`$ be the preimage in $`P`$ of the enlarged $`V_0`$. It is normal in $`G`$ and $`\tau`$-stable, since both the $`S_5`$-action and $`\tau`$ preserve that shadow. The shadow decomposition and $`Y_0\cap Z=1`$ imply $`P=P_0Y_0`$ and $`P_0\cap Y_0=1`$; hence $`P=P_0\times Y_0`$.

## Complement compatible with the marked involution

The quotient $`G/P_0`$ is an extension of $`S_5`$ by $`Y_0`$. Each $`U`$ is a projective $`\mathbb F_2S_5`$-module, so $`H^i(S_5,Y_0)=0`$ for $`i>0`$: the finite group algebra is self-injective. In particular $`H^2=0`$ gives a complement to $`Y_0`$ in $`G/P_0`$. Its full preimage $`E`$ in $`G`$ satisfies $`G=E\ltimes Y_0`$ and $`E\cap P=P_0`$.

Relative to that complement, the automorphism induced by $`\tau`$ on $`G/P_0`$ determines a derivation $`\delta:S_5\to Y_0`$, since it acts trivially on both $`S_5`$ and $`Y_0`$. Let $`F\cong F_{20}`$ be the image of $`H`$ in $`S_5`$. Every element of $`F`$ has an actual lift in $`H`$, fixed by $`\tau`$; because $`\tau`$ also fixes $`Y_0`$, this implies $`\delta|_F=0`$. As $`H^1(S_5,Y_0)=0`$, $`\delta`$ is principal, say $`\delta(g)=g y-y`$. Then $`y\in Y_0^F=0`$: each $`U|_F`$ is a sum of copies of the nontrivial irreducible restriction of $`N`$. Thus $`\delta=0`$, the chosen complement is $`\tau`$-stable, and its full preimage $`E`$ is $`\tau`$-stable. This proves (1), conditional on the stated support theorem.

The reduction leaves the embeddings of $`H`$ and the section $`K`$ in this semidirect product unrestricted. In particular, it supplies neither a finite classification for arbitrary $`b`$ nor a bound on $`b`$.

## Bounded stabilizer coordinates

The group and $`\tau`$-splitting above was independently accepted at exact source the recorded source revision; the following stabilizer deduction has the separate scoped reviews recorded below. Retain its notation, writing $`P_0/Z\cong X\oplus U^a`$, $`a\le15`$, $`Y_0\cong U^s`$, and $`W=H\cap P`$. Put $`F=H/W\cong F_{20}`$ and $`S=N|_F`$. The reviewed [lifted-socle bound](bruck-n-frattini-marked-rank.md#lifted-socle-bound) at the recorded source revision bounds the $`S`$-multiplicity of the intersection of the $`W`$-shadow with the full $`U`$-socle by 3. We show that, after a passive module automorphism and conjugation by a $`\tau`$-fixed passive element, there is a decomposition

```math
Y_0=Y_{\rm exc}\oplus Y_{\rm std},\qquad
 H=\bigl(H\cap(E\ltimes Y_{\rm exc})\bigr)\ltimes T_{\rm std}, \tag{2}
```

where $`Y_{\rm exc}\cong U^e`$, $`e\le 5a+2c_0+5\le86`$, $`c_0\le3`$, and $`T_{\rm std}`$ is the direct sum of standard $`F`$-stable complements to $`\mathop{\mathrm{soc}}\nolimits(U)`$ in the remaining blocks. Thus the active and exceptional parts together have at most 101 $`U`$-blocks. The displayed sharper bound depends on $`a,c_0`$; empty standard parts are allowed.

The module $`S`$ is irreducible and projective over $`F`$, with endomorphism ring $`\mathbb F_2`$, and $`U|_F\cong S\oplus S`$. Choose an $`F`$-stable complement to $`\mathop{\mathrm{soc}}\nolimits(U)`$. The dual-number endomorphism $`\varepsilon`$ maps this complement isomorphically to the socle. In multiplicity coordinates, write

```math
Y_0|_F\cong S\otimes(D_{\rm soc}\oplus D_{\rm top}),\qquad D=\mathbb F_2^s.
```

An $`S_5`$-module automorphism $`g+\varepsilon h\in\mathop{\mathrm{GL}}\nolimits_s(\mathbb F_2[\varepsilon]/(\varepsilon^2))`$ acts by $`(x,y)\mapsto(gx+hy,gy)`$. Such an automorphism extends to $`G=E\ltimes Y_0`$ by fixing $`E`$, and commutes with $`\tau`$.

Since $`W`$ is elementary abelian and normal in $`H`$, conjugation on it factors through $`F`$. Its subgroup $`W\cap Y_0=S\otimes L`$ corresponds to a subspace $`L\le D\oplus D`$. Define

```math
A=\{x:(x,0)\in L\},\qquad B=\mathop{\mathrm{pr}}\nolimits_{\rm top}L,\qquad c_0=\dim A\le3.
```

An $`h`$-shear straightens $`L`$ to $`A\oplus B`$: choose a linear lift of its graph $`B\to D/A`$ and extend that lift to all of $`D`$.

The projection $`\mathop{\mathrm{pr}}\nolimits_{P_0}:W\to P_0`$ is a homomorphism with kernel exactly $`W\cap Y_0`$. Its image is elementary abelian. Both actual projections to $`P_0`$ and $`Y_0`$ are $`H`$-equivariant for the action obtained from the $`E`$-component of $`H`$: $`P_0`$ centralizes $`Y_0`$, and $`Y_0`$ centralizes $`P_0`$. Since $`W`$ is abelian, its conjugation action on its image is trivial, so this action factors through $`F`$. The $`S`$-multiplicity of $`W`$ is $`b+1=a+s+1`$. Its projection image modulo $`Z`$ has at most $`1+2a`$ copies of $`S`$, while intersection with $`Z\cong S`$ can add one more. Therefore

```math
\dim L\ge s-a-1,\qquad \mathop{\mathrm{codim}}\nolimits_D B\le a+1+c_0. \tag{3}
```

The possible extra copy in $`Z`$ is essential: the kernel of the **shadow** projection can contain a nonzero central graph and need not equal $`W\cap Y_0`$.

The nonfixed $`F`$-block is semisimple. Choose equivariant lifts in $`W`$ of the $`S`$-part of the actual projection image; there are at most $`r=2a+2`$ copies. Their passive coordinates supply at most $`2r`$ vectors of $`D`$. The possible trivial $`F`$-summand of $`W`$ has zero passive projection, because $`Y_0|_F`$ is $`S`$-isotypic. Choose $`Q\le D`$ containing $`A`$, a complement to $`B`$, and all those coordinate vectors. Then

```math
\dim Q\le c_0+(a+1+c_0)+2(2a+2)=5a+2c_0+5.
```

Since $`B+Q=D`$, choose a complement $`D'\le B`$ to $`Q`$. A common basis adapted to $`D=Q\oplus D'`$ induces $`Y_0=Y_{\rm exc}\oplus Y_{\rm std}`$, with $`e=\dim Q`$, and the actual subgroup decomposition

```math
W=W_{\rm core}\oplus T_{\rm std},\qquad
 W_{\rm core}\le P_0\times Y_{\rm exc},\qquad
 T_{\rm std}=S\otimes(0\oplus D')\le Y_{\rm std}. \tag{4}
```

This is a statement about actual elements of $`W`$, including their possible central coordinates, not merely their shadows.

Finally restrict attention to the preimage of $`F`$ in $`G`$; $`T_{\rm std}`$ need not be $`S_5`$-stable. Projection to $`F\ltimes(Y_{\rm std}/T_{\rm std})`$ sends $`H`$ to a complement: by (4) its intersection with the kernel over $`F`$ is trivial. Its graph is a 1-cocycle, and $`H^1(F,Y_{\rm std}/T_{\rm std})=0`$ because this quotient is a direct sum of copies of the projective simple $`S`$. Conjugation by an element of $`Y_{\rm std}`$ makes the graph zero. This conjugation preserves the group splitting and $`\tau`$, since $`\tau`$ fixes $`Y_{\rm std}`$ pointwise, and yields (2). No factorization of $`K`$, product-folder structure, or quotient-loop assertion follows.

## Independent review of the support reductions

At exact source the recorded source revision, Independent checks an independent check, an independent check and an independent check independently accepted both the quadratic-support and passive-group reductions, conditional on the pinned marked-rank, lifted-socle, Bruck-envelope and N-block/projectivity inputs. All checked the two polar rank bounds on the actual F20 shadow graph, simultaneous row normalization including the changed top-linear row, the central passive preimage, the same-block involution shear, and the H2/H1 argument using actual fixed H lifts. Each read the exact certificate and both imports, extracted all three from the committed tree, and independently ran the new certificate with pinned Python 3.12; the folder and small-order reviewers specified 3.12.14. Both J and P6 checks passed. Their acceptance covers the 14-block quadratic and 15-block group/involution bounds, not a classification or product decomposition of H, K or the folder, a fresh primary-source audit, or formal verification. It does not cover subsequent appended stabilizer deductions.

## Independent review of the stabilizer coordinates

At exact source the recorded source revision, Independent checks an independent check and an independent check independently accepted the bounded-stabilizer section, conditional on the previously reviewed group/involution splitting, lifted-socle bound and F20 module inputs. Both checked the actual projection kernel, the possible extra central S-copy, the bound on the coordinate space Q, the actual W decomposition and the final H1 normalization by a tau-fixed passive conjugation. This supports the bound of 86 exceptional passive blocks. Neither review asserts a splitting of K, a product folder or a quotient loop. No new computation was needed.

