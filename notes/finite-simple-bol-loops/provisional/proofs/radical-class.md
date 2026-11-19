# Unbounded radical class at fixed projective quotient and fixed exponent

**Mira Cult · Provisional research.** Author proof, not independently reviewed.

This is not a consequence of the reviewed [class-two construction](../../projective-radicals/proofs/multiplicity.md). The proposed radicals have fixed exponent and arbitrarily large nilpotency class; Hall-regular power arguments do not apply.

**Theorem.** For every integer $`n\ge3`$ there is a finite simple non-Moufang **left** Bol loop of exponent six, of order

```math
20\cdot3^{119+v_n},\qquad v_n=20(2^n-1)-(n+1),
```

whose faithful left multiplication group is $`P_n\rtimes\mathrm{PSL}_2(19)`$. Its entire solvable radical $`P_n`$ is a **metabelian $`3`$-group of nilpotency class exactly $`n`$ and exponent exactly nine**. Its order is $`3^{236+19(2^n-1)+v_n}`$. Thus the groups in the irregular exponent-nine branch truly occur. Neither the projective quotient, the native loop exponent, the radical exponent nor even its derived length bounds the radical's nilpotency class. The proof does not deduce sharpness or simplicity merely from a count of selected signs.

## 1. Fixed, finite prior input

Write $`T=\mathrm{PSL}_2(19)`$, $`B=19{:}9=\langle u,r\rangle`$ the point stabilizer, $`r:x\mapsto4x`$, $`u:x\mapsto x+1`$, $`w:x\mapsto-1/x`$. All vector spaces below are ternary. The base has plus and minus $`T`$-modules $`X_0,Y_0`$ of dimensions 117,119, a $`B`$-map $`f_0:X_0\to Y_0`$, and a derivation $`d:B\to Y_0`$. Among projective involutions every nonidentity one is $`B`$-conjugate to $`w`$; the signed central label is $`z`$. Write $`M`$ for the sum-zero submodule of the functions $`K=\mathbb F_3^{20}`$ on the projective line. The permutation module splits as $`K=M\oplus\mathbb F_3\mathbf1`$, and $`M`$ is simple and nontrivial. Use $`e=(1-w)/2`$.

The [class-two source, §1](../../projective-radicals/proofs/multiplicity.md#1-the-base-matrix-input-and-an-obstruction-insensitive-to-all-the-new-central-slots) supplies a single $`B`$-map $`a:M\to Y_0`$ and a row $`\phi`$ on $`Y_0`$ with the following properties. On the central bottom pair $`X_b=X_0\oplus M`$, $`Y_b=Y_0\oplus M`$, use

```math
f_b(b,c)=(f_0(b)+a(c),c).
```

Then $`e f_b|_{eX_b}`$ is injective. For $`T`$-submodules $`J_b\le X_b,U_b\le Y_b`$ with $`f_b(J_b)\subseteq U_b`$, one has $`\dim eU_b\ge\dim eJ_b`$, with equality only for $`J_b=U_b=0`$. Also $`\phi`$ kills $`(f_b+w f_b w)X_b`$ on extending it by zero on the new $`M`$; $`\phi(r^3-1)=0`$ and $`\phi((1-w)d(r^3))=1`$. These require just the first, single passive shear of that proof; there are no high-dimensional generic shear choices below. The old $`X_0`$ has no trivial coinvariant and $`Y_0`$ has one coinvariant line, hit by $`f_0`$ and $`d`$ together. The old signed folder is faithful, sharp, simple, and fails right alternativity.

## 2. A ring with no invisible bottom ideal

Fix $`n\ge3`$. For every nonempty $`S\subseteq[n]`$ take a formal squarefree monomial $`t_S`$ with coefficient space $`C_S=M`$ for $`|S|=1`$, $`C_S=K`$ for $`1<|S|<n`$, and $`C_{[n]}=K/\mathbb F_3\mathbf1\simeq M`$ via subtraction of the mean. Let $`I=\bigoplus_S C_S t_S`$. Multiplication is pointwise on coefficients and union on disjoint subsets, zero for overlapping subsets; project to $`K/\mathbb F_3\mathbf1`$ at the top. This commutative associative nil algebra is the indicated subquotient of the squarefree-variable polynomial algebra over $`K`$. Every $`b\in I`$ has $`b^3=0`$ by Frobenius, although $`I^n\ne0`$. Its dimension is $`v_n`$. Write $`I_{\ge j}`$ for the degrees at least $`j`$.

Products of two degree-one $`M`$ coefficient spaces on distinct variables span $`K`$: for distinct sites $`i,b,c`$, $`(e_i-e_b)(e_i-e_c)=e_i`$. Further multiplication by a suitable member of $`M`$ preserves $`e_i`$. Thus products with specified disjoint degree-one factors span all the listed coefficient spaces from degree two up, including the top.

The principal unit group $`1+I`$ is abelian of exponent three. Each of its elements has a unique expression $`\prod_{S\ne\varnothing}(1+b_S t_S)`$ with $`b_S\in C_S`$: at each successive degree the known lower-degree contributions leave the new coefficients uniquely determined, and $`(b_S t_S)^2=0`$. The product is independent of the ordering, and multiplication of units adds these **factor coordinates** componentwise. The $`T`$-action on 20 sites permutes them by its given linear action. Let $`A`$ consist of those units whose factor coefficients belong to $`M`$ on **every** subset (at the top this means the whole quotient). Thus $`A\simeq M^{2^n-1}`$ as an additive $`T`$-module; write $`c_*(s)=b_{[n]}`$ for its additive, equivariant top-coordinate map. The unrelated usual coefficient of $`t_{[n]}`$ in $`s-1`$ contains nonlinear terms and must not be used instead.

Let $`A`$ act on the additive group of $`I`$ by multiplication by units. We use two facts. First $`[A,I]=I_{\ge2}`$ and, more generally, successive differences by $`A`$ span every possible higher grade: the units $`1+m t_j`$ act by the difference $`m t_j`$, and the preceding single-site products reach each basis output. Second, if $`y\in I`$ has a nonzero term on a subset $`S`$ of minimal size $`d<n`$, for every $`j\notin S`$ take a degree-one difference $`m_jt_j`$. Their product on $`y`$ kills all terms except the one on $`S`$. Choose the $`m_j`$ supported on two sites, including a site where the original coefficient is nonzero, with value 1 there. The resulting nonzero coefficient has support at most two and is not constant, so survives in the **true top quotient**. In particular every nonzero $`A`$-invariant additive subspace with a lower term meets the top nontrivially. Also the annihilator of $`I`$ inside $`I`$ is precisely the top: the same test rules out any other element. These facts do not require that a subspace split by homogeneous degree.

## 3. The physical group, stabilizer and marks

Put $`X=X_0\oplus A`$, $`Y=Y_0\oplus I`$. Write $`X`$ additively when acting on its factor coordinates, writing $`s`$ for the corresponding unit in $`A`$. Let $`P=Y\rtimes X`$, where $`X`$ acts as the just defined units on $`I`$, trivially on $`Y_0`$, and $`X_0`$ acts trivially on everything. In standard group coordinates $`\iota(y)s(x)`$ write $`\rho(x)`$ for the action, $`s(x)`$ for the pure lift and $`\iota`$ for the normal additive inclusion. The signed group adds the commuting $`T`$-action and $`z`$ acting identically on $`X`$, as minus on $`Y`$. Let $`G=P\rtimes T`$. Define a true $`1`$-cocycle on $`X`$ by

```math
D(x_0,s)=(f_0(x_0)+a(c_*(s)),\ s-1)\in Y.
```

Here $`(s s'-1)=(s-1)+s(s'-1)`$, and the base term is additive. Its graph $`W=\{\iota(D(x))s(x):x\in X\}`$ is consequently an abelian subgroup; $`D`$ is $`B`$-equivariant. Adjoin the old $`B`$-lifts $`\iota(d(g))g`$ to obtain $`H`$ over $`B`$, of order $`|X||B|`$. The old vectors $`d(g)`$ are central in $`P`$. The section is $`K_Q=z\Lambda`$ where $`\Lambda`$ consists of **all** outside involutions (not a set of chosen linear representatives).

Use symmetric coordinates $`[x,y]=s(x/2)\iota(y)s(x/2)`$. Inversion is $`[-x,-y]`$ and $`T,z`$ act by their given signs. Thus $`K_Q`$ over the identity is $`Y`$, and above a nonidentity projective involution $`i`$ is exactly $`\{[x,y]i:x\in X_i^-,\ y\in Y_i^+\}`$. On each new slot the difference of the negative ranks of $`Y`$ and $`X`$ is zero, since $`K/M`$ is trivial. The base negative-rank difference is two. There are 171 genuine nonidentity projective involutions, so

```math
|K_Q|=|Y|(1+171/9)=20|Y|=[G:H].
```

The extra trivial *middle* directions in $`Y`$ are deliberate. Had they been left in $`X`$, no mark would generate their trivial coinvariants; had an extra untwisted direction been put in $`Y`$ in degree one, an unhit quotient could survive. Both failures are avoided here.

## 4. Sharpness with nonabelian conjugated lifts

A forbidden element is a nonidentity $`h\in H`$ inverted by a selected signed involution $`\lambda`$: then $`h\in\Lambda^2`$ and conversely. First take $`h\in W`$. If its unit $`s`$ is nontrivial, let $`d`$ be its least nonzero factor degree. In the ring part of $`P`$ filter units and additive coordinates together by degree. Commutators with $`P`$ raise this filtration, since the action differences are products by positive-degree terms. The leading pair of $`h`$ in degree $`d`$ is $`(b,b)`$: $`D`$ contributes $`s-1`$ and the conversion to symmetric coordinates does not affect the leading term. On the leading pair every actual lift of $`zi`$ acts by $`(i,-i)`$ because conjugation by its $`P`$-part disappears there. Inversion would require both $`ib=-b`$ and $`ib=b`$, impossible. Therefore $`s=1`$. What remains is central in $`P`$ and lies in the pure base graph; the base's actual vertical avoidance (equivalently its negative injection at $`w`$ and $`B`$-conjugacy) gives $`h=1`$. We have not assumed that the pure sign equals its conjugates as an operator on all of $`P`$.

For a nonvertical inverted $`h`$, the old projective geometry puts the signed inverter and a nontrivial power of $`h`$ over $`zw,r^3`$ after conjugating by an actual element of $`H`$. Indeed an involution inverting a nontrivial Borel element cannot invert a unipotent here (its normalizer is the odd Borel); the split eigenpair of a semisimple Borel element includes infinity, and the Borel can carry the other point to zero. Weyl inverters differ by a torus element, all conjugate by a torus square. A suitable power yields $`r^3`$. Project away **all** ring minus coordinates $`I`$, retaining $`X`$. The resulting kernel is abelian, $`X\oplus Y_0`$, and the image of $`W`$ is the graph of $`f(x_0,s)=f_0(x_0)+a(c_*(s))`$. This quotient is not required to form a loop. Compress by the additive subgroup

```math
W'+(zw)W'+(r^3-1)(X\oplus Y_0),\qquad W'=\mathrm{graph}f.
```

It is stable under $`zw,r`$, and its residue is $`Y_0/((f+wfw)X+(r^3-1)Y_0)`$ via $`(x,y)\mapsto y-f(x)`$. On the residue $`r^3=1`$ and $`zw`$ acts by $`-w`$. The stabilizer vector over $`r^3`$ leaves $`d(r^3)`$. An actual involution over $`zw`$ has vector in its negative eigenspace, so the square of its product with this stabilizer element leaves $`(1-w)d(r^3)`$. That cannot vanish, by $`\phi`$ from §1: $`f`$ uses only the bottom additive factor coordinate. Hence $`H\cap\Lambda^2=1`$. Conjugacy invariance and the genuine index count give sharp transversality for all conjugate stabilizers; the signed sandwich identity gives the left Bol operation.

## 5. Simplicity: a nonlinear cut lemma

We check all $`R\lhd G`$, not merely sign-stable normals. If $`1<R\le P`$ acquired a flat cut $`|K_QR/R|=[G:HR]`$, the quotient section would meet each projected coset exactly once, because all are met. Only the projective identity sheet reaches the base Borel coset ($`B`$ is odd), and its section is the actual subgroup $`Y`$. Put $`U=R\cap Y`$ and $`J=\pi_X R`$. Counting this one whole quotient block gives $`[R:R\cap W]=|U|`$, hence $`R=U(R\cap W)`$ and $`R\cap W`$ projects onto all of $`J`$. Modulo $`U`$, the graph $`R/U`$ is central in $`P/U`$: its commutators with $`X`$ or $`Y`$ are in $`R\cap Y`$. Therefore $`j\in J`$ acts trivially on $`Y/U`$, and $`\bar D:J\to Y/U`$ is an actual **additive $`T`$-map**, with values fixed by $`X`$. Additivity follows from the cocycle equation and $`T`$-equivariance from normality of the residual graph. Write $`J_1=\ker\bar D`$. In particular $`D(J_1)\subseteq U`$ as actual sets, even though $`D`$ is nonlinear on $`X`$.

For a reflected sheet over $`i`$, a pair of its images can agree mod $`R`$ only if its two $`X_i^-`$ coordinates differ by $`j\in J_i^-`$. In $`P/U`$ the graph element over $`j`$ is central and equals the pure $`j`$ times $`\bar D(j)`$ in either standard or symmetric coordinates. Thus the required change of the $`Y_i^+`$ coordinate modulo $`U`$ is precisely $`\bar D(j)`$ up to the harmless sign of the chosen difference. Since $`\bar D`$ is a $`T`$-map, that change is $`i`$-negative, and it must also be $`i`$-positive. Hence it vanishes. Conversely every $`j\in(J_1)_i^-`$ and every difference in $`U_i^+`$ works. The common fiber cardinality on this sheet is

```math
|(J_1)_i^-|\,|U_i^+|.                       \tag{2}
```

Here one may explicitly multiply central pure-$`j`$ in midpoint coordinates: its action on $`Y/U`$ is trivial, and $`X`$ fixes $`\bar D(j)`$; consequently no quadratic or higher change of $`y`$ has been discarded. The counts are the same for every conjugate $`i`$. Every nonbase projective coset receives nine reflected sheets, each originally of size $`|Y|/9`$, and the quotient block has size $`|Y|/|U|`$. Flatness therefore gives $`\dim eJ_1=\dim eU`$ by (2).

Filter $`J_1`$ and $`U`$ by their genuine intersections with the degree-at-least-$`d`$ flag, keeping $`X_0`$ and $`Y_0`$ in the final, degree-$`n`$ bottom layer. On every grade below $`n`$, the leading coefficient of $`D(x)`$ is identically the leading factor coefficient of $`x`$; the $`Y_0`$ coupling has no entry there. The induced graded $`J_1`$ thus sits by the original, equivariant inclusion $`M\hookrightarrow C_S`$ in graded $`U`$ on each **whole degree** (correlations between subsets of one degree are allowed). Its negative dimension is at most the corresponding one of $`U`$. At the bottom put $`J_b=J_1\cap X_b`$, $`U_b=U\cap Y_b`$; there $`D=f_b`$ exactly and $`f_b(J_b)\subseteq U_b`$. All the inequalities add since the negative projection for the involution is exact in characteristic three. Equality forces equality at the bottom, whence $`J_b=U_b=0`$ by §1. Section 2 now forces $`U=0`$: any lower term of an element of $`U`$ can be driven by actual $`A`$-action differences to a nonzero *pure* top vector in $`U_b`$, and a vector already supported at the bottom belongs to $`U_b`$. It follows that $`R\le W`$.

For clarity this last possibility really is harmless: any normal subgroup of $`G`$ lying in $`W`$ commutes with $`Y`$, since its intersection with $`Y`$ is trivial. Its unit component therefore acts trivially on $`I`$ and lies at the top by the annihilator assertion in §2. Its graph is a $`T`$-linear restriction of the bottom $`f_b`$. On its $`T`$-subspace $`J`$ the image then has negative dimension exactly $`\dim eJ`$, by the negative injection at the bottom. Applying the bottom zero-defect condition to $`(J,f_b(J))`$ forces $`J=0`$. This proves both the impossibility of a nonzero flat vertical cut and core-freeness there without assuming that $`R`$ is a graded ideal or is normalized by $`z`$.

Any normal $`R`$ with nontrivial projective image surjects onto simple $`T`$. The group $`G/R`$ is then a 3-group, so the pure perfect $`T`$ dies. This kills all of $`X`$ by its zero coinvariants. It also kills $`[A,I]=I_{\ge2}`$ and $`I/I_{\ge2}=M^n`$ modulo the remaining trivial $`T`$-action. Thus $`G/R`$ is at most the one original coinvariant line in $`Y_0`$. If nontrivial, both $`H`$ and $`K_Q`$ map onto it by §1 and by $`Y\subseteq K_Q`$. Hence the projected section strictly exceeds index one. A normal subgroup inside $`H`$ has trivial projective image, so the preceding vertical argument gives actual core-freeness. The genuine marks generate $`G`$: they contain all of $`Y`$, all pure projective involutions generating $`T`$, and after multiplying by those same pure involutions they contain $`s(X_i^-)`$ for every $`i`$. These negative spaces span $`X`$ since their sum contains all differences for the generating involutions and $`X_T=0`$. We have the **faithful generated** left group as claimed. The [exact normal-subloop criterion](../../sources/foundations/C0001.md) now gives simplicity of the original loop.

## 6. Orders and the sharp separation between the loop and its left group

The old signed group at zero ring coordinates preserves its genuine $`H`$ intersection and section, hence embeds the original matrix loop as an actual subloop; its right-alternative failure and order-six element persist. Every vertical mark lies in elementary $`Y`$. For each nonvertical mark $`[x,y]i`$, $`ix=-x`$ and $`iy=y`$. Squaring in the actual group gives $`s(x/2)\iota(2y)s(-x/2)\in Y`$, so the native exponent is exactly six, **not** eighteen. The radical is exactly $`P`$ since the quotient is nonabelian simple.

In $`P`$, both $`X`$ and $`Y`$ are elementary abelian, whence the group is metabelian and every element has order dividing nine. Iterated commutators apply successive positive-degree differences to $`I`$; with $`n-1`$ such differences on degree one they reach the nonzero top, whereas $`n`$ differences always vanish. Therefore the nilpotency class is exactly $`n`$. Write an element as $`\iota(y)s(x)`$. Its cube has $`Y`$-coordinate $`(1+\rho(x)+\rho(x)^2)y=(s-1)^2 y`$. Choose $`s=(1+b_1t_1)(1+b_2t_2)`$ and $`y=b_3t_3`$ with $`b_1b_2b_3`$ supported at one site (take two distinct differences supplying $`e_i`$ and a third with $`i`$-value one). The degree-three term $`2b_1b_2b_3t_{123}`$ is nonzero, including modulo constants if $`n=3`$. Thus the radical has exponent exactly nine. This last witness is a group element, not alleged to be a native order-nine point in the original exponent-six loop.

The smallest construction of this scheme, $`n=3`$, has order $`20\cdot3^{255}`$ and radical order $`3^{505}`$. No minimality in the universe of simple loops, review of all earlier results, or public release is claimed.

[Provisional results and replay](../README.md)
