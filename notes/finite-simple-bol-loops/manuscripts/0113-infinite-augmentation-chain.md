# 0113. An infinite nested chain of simple left Bol loops of exponent six

**Mira Cult**

The [matrix construction of 0112](0112-elementary-radical-example.md) gives one finite simple loop of exponent six. Here we embed it into a larger simple loop of the same exponent, keeping the multiplication of every old pair. The construction can be repeated indefinitely. The resulting union is infinite and simple, although every finitely generated subloop is finite.

**Theorem.** There is a strictly ascending sequence $`Q_0<Q_1<Q_2<\cdots`$ of finite simple proper left Bol loops of exponent six such that
```math
        |Q_n|=20\cdot3^{119+19n},\qquad
        \operatorname{LMlt}(Q_n)=(C_3)^{236+38n}\rtimes\operatorname{PSL}_2(19).
```
The canonical embeddings are actual operation-preserving inclusions, and the elementary normal subgroup in the displayed left group is its whole solvable radical. No two stages are isomorphic or isotopic, since their orders differ. None has an element of order five although five divides its order. The failure of the right alternative identity already occurs inside $`Q_0`$.

Here and below every vector space is over $`k=\mathbb F_3`$. The quotient group is $`T=\operatorname{PSL}_2(19)`$, with stabilizer $`B=U\rtimes P`$ of infinity, $`U=\langle u\rangle`$ of order nineteen and $`P=\langle r\rangle`$ of order nine. The projective maps are $`u:x\mapsto x+1`$, $`r:x\mapsto4x`$, $`w:x\mapsto-1/x`$, so $`wrw=r^{-1}`$. Write $`M`$ for the augmentation submodule of $`k[\mathbb P^1(19)]`$; its basis is $`m_j=e_j-e_\infty`$ for $`j\in\mathbb F_{19}`$. This $`M`$ has dimension 19, not 20.

## The coupling and its dimension margin

The $`T`$-module $`M`$ is simple over the **prime field**. On restriction to $`U`$ its displayed basis is regular. Since $`3`$ has order 18 modulo 19, the cyclotomic part of $`x^{19}-1`$ is irreducible of degree 18 over $`k`$; the remaining factor is $`x-1`$. A proper nonzero $`T`$-submodule must therefore have dimension 1 or 18. A one-dimensional representation of perfect $`T`$ is trivial, but the sole $`T`$-fixed vectors in the transitive permutation module are the constants and 20 is nonzero in $`k`$. There are no such nonzero vectors in $`M`$. The invariant dot product restricts nondegenerately to the orthogonal complement of the constants, namely $`M`$. Hence its trivial quotient is also zero, ruling out a submodule of codimension one. In particular $`M_T=M^T=0`$. Its negative $`w`$-space is nonzero: $`w`$ does not act identically and is an involution in odd characteristic.

At stage $`n`$, the sign modules of the preceding construction are $`X=X_0\oplus M^n`$, $`Y=Y_0\oplus M^n`$, its actual $`B`$-linear graph map is $`f:X\to Y`$, and its derivation on $`B`$ is the original one embedded in the $`Y_0`$ summand. For a $`T`$-module $`N`$, a $`B`$-map $`M\to N`$ is determined by, and may have as its value on $`m_0`$, **any** $`\beta\in N^P`$: the $`m_j`$ form the nineteen-point $`B`$-permutation basis, with stabilizer $`P`$ at zero, and the map sends $`m_j`$ to $`u^j\beta`$. The values of the $`T`$-linear maps on $`m_0`$ form exactly $`(w-1)N^B`$. Indeed $`M`$ splits off the full permutation module along its constants since 20 is a unit; a map on that full module is determined by $`c\in N^B`$, the image of $`e_\infty`$, and sends $`e_0-e_\infty`$ to $`(w-1)c`$.

Consequently choose any
```math
        \beta\in Y^P\setminus \bigl(f((w-1)X^B)+(w-1)Y^B\bigr),\qquad
        a(m_j)=u^j\beta .
```
Here $`(w-1)`$ acts in the relevant source or target module; both terms indeed lie in $`Y^P`$. Equivalently $`a\notin f\operatorname{Hom}_T(M,X)+\operatorname{Hom}_T(M,Y)`$. The original matrices give $`\dim X_0^B=1`$, $`\dim Y_0^B=2`$, $`\dim Y_0^P=14`$. These three numbers are verified directly in the [chain verifier](../sources/augmentation-chain/code/verify_psl2_19_infinite_chain.py). The $`B`$-permutation basis of $`M`$ has one orbit, and $`P`$ on the nineteen finite labels has three orbits (zero and two orbits of size nine). Thus $`\dim M^B=1`$, $`\dim M^P=3`$. The available space has dimension $`14+3n`$, while the forbidden one has dimension at most $`3+2n`$. The gap is at least $`11+n`$ at every stage, independently of any earlier choice. Ordinary row reduction supplies a deterministic $`\beta`$, for example the first nullspace-basis vector outside the indicated span. No genericity or passage to a larger field is being assumed.

Put
```math
 X'=X\oplus M,\quad Y'=Y\oplus M,\quad f'(x,v)=(f(x)+a(v),v),
 \qquad d'_B=(d_B,0).
```
Use precisely the earlier split sign construction: $`G'=(X'\oplus Y')\rtimes T`$, $`z`$ fixes $`X',T`$ and negates $`Y'`$, $`H'`$ is the true graph over $`X'\rtimes B`$ with these data, and $`K'=z\Lambda'`$ uses all outside involutions. The matrix is triangular as a linear map, not assumed $`T`$-equivariant. We prove that the untrimmed new input is already a faithful simple loop, not merely a source with some unknown simple quotient.

## Actual sharpness survives

Write $`e=(1-w)/2`$ for the negative projection on any module. The negative dimensions of source and target rise by the same amount, so their difference stays two. The map $`e f'|_{eX'}`$ is injective by its two diagonal blocks $`e f|_{eX}`$ and $`I_{eM}`$. Above the identity the translation sheet is $`Y'`$; above each nonidentity involution $`i`$ it has direction $`(X')_i^-\oplus(Y')_i^+`$. The base proof's count, since the 171 involutions are $`B`$-conjugate, is $`|K'|=20|Y'|=[G':H']`$. The vertical stabilizer graph meets each sheet direction trivially by the just-proved injection. Nonvertical projected inverter pairs are exactly the same eight simultaneous $`B`$-orbits represented by $`(w,r^j)`$ from [the base proof](0112-elementary-radical-example.md#why-the-chosen-permutations-form-a-left-bol-loop). Their conjugators lift in $`H'`$. Any alleged inversion of an $`H'`$ element over $`r^j`$, $`j\ne0\pmod9`$, powers to an inversion of an $`H'`$ element over $`r^3`$ by the same outside involution.

We need only the following sufficient test for excluding this last actual collision, not a classification or an iff. For any one stage define
```math
 F=f+w_Y f w_X,\qquad
 S=Y/\bigl(F(X)+(r^3-1)Y\bigr),\qquad D=d_B(r^3).
```
If $`(1-w)D`$ is nonzero in $`S`$, the stated inversion is impossible. To see this work over the genuine dihedral group with $`\mu=zw`$ and $`W=\operatorname{graph}(f)`$ in $`V=X\oplus Y`$. The subspace $`W+\mu W+(r^3-1)V`$ is stable under both $`r,\mu`$ (for instance $`\mu r\mu=r^{-1}`$). Its quotient is $`S`$ via $`(x,y)\mapsto y-fx`$; $`\mu`$ acts there by $`-w`$, and $`r^3`$ is trivial. If an outside involution $`(c,\mu)`$ inverts an $`H`$ element over $`r^3`$, their product must have square one. On this quotient the variable vector $`c\in(1-\mu)V`$ contributes zero to the square, as does the freely chosen graph vector. The remaining contribution is $`(1+\mu)\mu(0,D)`$, exactly $`(1-w)D`$, a contradiction. The base input passes: the originally checked physical vector $`(r^{-3}-w)D`$ has this same class and raises rank from 116 to 117.

For the new stage write $`A=a+w_Y a w_M`$. This intertwines the $`r`$-actions, since $`a`$ does and $`w`$ inverts $`r`$. The corresponding $`F'`$ is
```math
                 F'=\begin{pmatrix}F&A\\0&2I\end{pmatrix}.
```
The shear $`L:Y'\to Y`$, $`L(y,v)=y-A v/2`$, takes $`F'(x,v)`$ to $`F x`$, intertwines $`r`$, and takes $`(1-w_{Y'})D'`$ to $`(1-w_Y)D`$. Thus the latter's nonzero class forces the former's class nonzero. It does not require $`L`$ to intertwine the full $`T`$-action or to be a map of whole loops. The physical sharpness argument with the actual eight projective orbits now applies. Since the outside square is conjugacy-invariant and $`|K'|=[G':H']`$, the section is sharp at every point; sandwich closure proves the left Bol law exactly as in the base.

## Why adding a module does not add a normal subloop

For any submodules $`J\le X`$, $`Z\le Y`$ with $`f(J)\subseteq Z`$, write $`\theta(J,Z)=\dim eZ-\dim eJ`$. The negative injection makes every such defect nonnegative. The base input has no nonzero pair of defect zero. We prove this property survives. In the added coordinates the map is $`I:M\to M`$, and $`M`$ is simple with nonzero negative space. Its only pairs of zero defect are $`(0,0)`$ and $`(M,M)`$.

For an arbitrary possible flat pair $`J'\le X'`$, $`Z'\le Y'`$ at the larger stage take the intersections with $`X,Y`$ and the projections to the two copies of $`M`$. They are admissible pairs for $`f`$ and $`I`$, respectively, by triangularity of $`f'`$. The defect is the sum of their defects, because the negative eigenspace functor is exact for an involution in odd characteristic. Equality forces equality in both. Hence both intersections vanish, and a nonzero such pair must project onto both copies of $`M`$. It must consist of graphs of $`T`$-linear maps $`l:M\to X`$, $`h:M\to Y`$. Containment of the image of the first graph in the second yields $`f l+a=h`$, contradicting the choice of $`a`$. So no nonzero flat pair exists at the new stage. With $`a=0`$ this argument rightly fails: the two added copies would themselves be a flat pair.

We recall why this suffices for all possible elementary cuts, even ones not preserved by $`z`$. For a $`T`$-invariant $`R\le X'\oplus Y'`$ put $`d_R=\dim R-\dim(R\cap W')`$ and $`A_w=(X')^-_w\oplus(Y')^+_w`$. The ratio of the actual section size in the quotient by $`R`$ to the new index is
```math
           (3^{d_R-\dim(R\cap Y')}+19\,3^{d_R-\dim(R\cap A_w)})/20 .
```
Both exponents are nonnegative by disjointness with $`W'`$. Equality gives the graph of the restriction of $`f'`$ modulo $`Z=R\cap Y'`$ on $`J_0=\pi_{X'}R`$, and this induced $`\bar f:J_0\to Y'/Z`$ is $`T`$-linear. Then $`R\cap A_w=(\ker\bar f)^-_w\oplus Z^+_w`$: a negative source vector maps to a negative class in $`Y'/Z`$, which can equal a positive class only if both classes vanish. Thus the second equality supplies the true flat pair $`(\ker\bar f,Z)`$. Both spaces must vanish. If $`R`$ were still nonzero, then $`f'|_{J_0}`$ would itself be $`T`$-linear and $`(J_0,f'(J_0))`$ would be another nonzero flat pair, again impossible. Thus every nonzero elementary cut is strict.

Since $`M_T=0`$, the trivial quotient of $`X'`$ stays zero and the trivial quotient of $`Y'`$ stays the original one-dimensional line; $`H'`$ still maps onto that line through the original graph elements. Every normal subgroup projecting onto $`T`$ contains $`[T,V']`$ by commutators. In $`G'/[T,V']=T\times (Y')_T`$ its image contains $`T`$ by perfectness; the single possible proper projecting cut is strict since both the section and the stabilizer surject onto the remaining line. These cases exhaust normals because $`T`$ is simple. The core of $`H'`$ is vertical and would violate strictness if nonzero. The section generates $`G'`$: its group is normal (generated by the full outside square), projects onto $`T`$, and contains $`Y'`$. The faithful action hence gives the claimed left group and radical. A proper nontrivial loop quotient would induce equality on its translation-group kernel, exactly as proved for the base, contradicting strictness. This establishes simplicity of the whole stage, not just of a quotient.

## Actual embeddings, exponent and limit

Embed all old coordinates by adjoining zeros in both new $`M`$ summands, and use the same $`T`$ and $`z`$. Then $`H'\cap G=H`$ directly from the block map and old cocycle. Every old outside mark is still an outside involution and multiplication by $`z`$ commutes with this inclusion of sets, so each old left translation in $`K`$ lies in $`K'`$. The map $`gH\mapsto gH'`$ is injective. For an old point its old section member already sends $`H'`$ to that image and, by sharpness, is the unique new section member doing so. Thus this is a homomorphism of loops, with operations preserved on all embedded old points. Merely embedding the two groups would not have implied this fact. The degree grows by $`3^{19}`$ each step. The base right-alternative failure persists, giving properness. All elements retain orders in $`\{1,2,3,6\}`$: a section member above an involution squares to a vector in the elementary kernel, and the vertical members have exponent three. The base has actual order-six elements, so the exponent is exactly six.

As an additional consequence, the union under these embeddings is a countably infinite locally finite simple proper left Bol loop of exponent six. A nontrivial normal subloop meets some finite stage nontrivially; intersection with any later stage is a normal subloop there (restrict the quotient homomorphism), so it contains that entire stage. Local finiteness holds because any finite list lies in one finite stage. The finite theorem does not rely on this limit argument.

The [author replay](../sources/augmentation-chain/evidence/author.out) constructs the first three enlargements over the original, verifies their actual bottom and vertical ranks and all-cut fixed-point iterations, and tests the bad $`a=0`$ graph. The induction and improving dimension margin, not those finite replays, give unboundedness.
This theorem does not classify loops of any given order or determine whether two different choices at the same stage give the same loop.

## Reproducibility and acknowledgment

The [two chain verifiers and their recorded outputs](../sources/augmentation-chain/README.md) use the same published base matrices but choose different couplings. Their finite checks at the base and three enlarged stages complement the induction; a finite sample alone would not prove unboundedness. A separate AI mathematical review accepted the precise chain, its embeddings and its locally finite simple union, using the independently checked base theorem. No human refereeing, proof-assistant verification or historical priority is claimed. Mira Cult directed the research; OpenAI models assisted with the construction, exposition and separate mathematical audit. Exact model versions were not established.
