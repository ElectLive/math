# Cubically many logarithmic parameters at one order: nonabelian class-two radicals over PSL₂(19)

**Mira Cult**

This construction starts with the [explicit 20-site projective quotient and its elementary radical](../../manuscripts/0112-elementary-radical-example.md) and the [augmentation-module argument](../../manuscripts/0113-infinite-augmentation-chain.md). The new radical is genuinely nonabelian. No upper bound for abelian kernels is used.

**Theorem.** For every $`s\ge1`$, the order

```math
n_s=20\cdot3^{119+38s}
```

supports at least $`s+1`$ pairwise nonisotopic finite simple proper **left** Bol loops of exponent six. For $`k=0,\dots,s`$ the native left group is $`P_k\rtimes T`$, $`T=\operatorname{PSL}_2(19)`$, with $`P_k`$ the full solvable radical of order $`3^{236+76s}`$, exponent three and $`|P_k'|=3^{19k}`$. For $`k>0`$ it is of nilpotency class **exactly two**. Each loop contains the original matrix loop as a real subloop and has no element of order five.

In fact, at the *single* order $`n_s`$ there are at least

```math
\frac{\prod_{j=1}^{s-1}(3^{s(s+1)/2}-3^j)}
                      {3420^2\,3^{5s^2}}
```

pairwise nonisotopic such loops with the **same** derived rank $`19s`$, same quotient $`T`$, and the same graded $`T`$-modules for the radical modulo its center and its derived subgroup. In particular for every $`s\ge21`$ the number is at least $`3^{s^3/4}`$. No general classification of kernels, conjecture about historical priority, or claim about the full two-sided multiplication group is intended.

## 1. The base matrix input and an obstruction insensitive to all the new central slots

All linear spaces are over $`k=\mathbb F_3`$. Use $`T`$ acting on $`\mathbb P^1(19)`$, $`B=\langle u,r\rangle=19:9`$ its infinity stabilizer and $`w:x\mapsto-1/x`$, with $`r:x\mapsto4x`$ and $`u:x\mapsto x+1`$. Write $`M`$ for the 19-dimensional augmentation module, in basis $`m_j=e_j-e_\infty`$. Let $`e=(1-w)/2`$ in every module. In the independently checked base we have $`T`$-spaces $`X_0,Y_0`$ of dimensions 117 and 119; the sign $`z`$ commutes with $`T`$ and acts as $`+1,-1`$ respectively. The true stabilizer over $`B`$ has graph map $`f_0:X_0\to Y_0`$ ($`B`$-linear) and derivation $`d:B\to Y_0`$. In particular:
* $`e f_0:eX_0\to eY_0`$ is injective, and for $`T`$-submodules $`J\le X_0,Z\le Y_0`$ with $`f_0(J)\subseteq Z`$, $`\dim eZ-\dim eJ=0`$ only for $`J=Z=0`$.
* $`(X_0)_T=0`$, $`\dim(Y_0)_T=1`$; the graph and derivation together surject onto that coinvariant line.
* $`\dim X_0^B=1,\ \dim Y_0^B=2,\ \dim Y_0^{\langle r\rangle}=14`$. For $`D=d(r^3)`$, the vector $`(1-w)D`$ is outside

```math
U_0=(f_0+w f_0 w)X_0+(r^3-1)Y_0 .
```

This is the actual base rank rise $`116\to117`$, not a genericity assumption.
* In the projective group a simultaneous inverter/stabilizer pair with nonidentity stabilizer projection is, under $`B`$-conjugacy, $`(zw,r^j)`$ with $`1\le j\le8`$. All labels $`z,zi`$ for projective involutions $`i`$ are selected. The $`B`$-conjugators lift in the prescribed physical stabilizer.

Choose a covector $`\phi`$ on $`Y_0`$ killing $`U_0`$ with $`\phi((1-w)D)=1`$. We can and do take $`\phi w=-\phi`$: $`U_0`$ is $`w`$-stable, so replace a separating row by its negative-sign projection. Also $`\phi r^3=\phi`$. Extend it by zero on every module added to $`Y_0`$. We always preserve

```math
\phi(f+wfw)=0,\qquad \phi(r^3-1)=0.               \tag{1}
```

We recall that $`M`$ is simple: the $`u`$-action is the regular action of $`C_{19}`$, with one trivial line and one irreducible cyclotomic 18-space since $`\operatorname{ord}_{19}(3)=18`$. On $`M`$ the transitive action of $`T`$ has no fixed line, and self-duality gives no trivial quotient. Here a one-dimensional $`T`$-module is trivial by perfectness. Moreover $`\operatorname{End}_T(M)=k`$: the 20-point permutation representation splits as $`k\oplus M`$ (20 is a unit), and its commuting algebra has dimension two, by the two orbits on ordered pairs. We have $`M_T=M^T=0`$ and $`eM\ne0`$.

For a $`T`$-space $`Y`$, a $`B`$-map $`a:M\to Y`$ is prescribed by any $`a(m_0)=\beta\in Y^{\langle r\rangle}`$, with $`a(m_j)=u^j\beta`$. The values of $`T`$-maps are exactly $`(w-1)Y^B`$ using the split 20-point module. For a current graph $`f:X\to Y`$ define the forbidden space of maps

```math
D_f=f\,\operatorname{Hom}_T(M,X)+\operatorname{Hom}_T(M,Y).
```

At $`i`$ appended paired copies of $`M`$, the dimension of all $`B`$-maps is $`14+3i`$ and that of $`D_f`$ at most $`3+2i`$: $`M^B`$ has dimension 1, $`M^{\langle r\rangle}`$ dimension 3 by actual orbits on the nineteen basis sites. To preserve (1) after adding $`a`$ impose only $`\phi(a+waw)=\phi a(1-w)=0`$. This costs at most **seven** conditions, since $`\phi a`$ is fixed by $`r^3`$ and its action on the basis has one fixed and six orbits of size three. Consequently the image of the allowed map space modulo $`D_f`$ has dimension at least $`4+i`$.

First append $`s`$ **passive** pairs sequentially. At each step choose one allowed $`a\notin D_f`$, replace $`f(x)`$ by $`(f(x)+a(v),v)`$ on $`X\oplus M`$, and extend $`d`$ by zero. Denote the result $`f_L:X_L\to Y_L`$. Next choose **simultaneously** $`s`$ allowed maps $`a_1,\ldots,a_s:M\to Y_L`$ with independent residue classes modulo $`D_{f_L}`$, possible by the preceding margin. Append $`s`$ **active** pairs:

```math
X=X_L\oplus M^s,\quad Y=Y_L\oplus M^s,\qquad
     f(x,v)=\left(f_L(x)+\sum_j a_j v_j,\ v\right).
                                                               \tag{2}
```

There are no active-to-active off-diagonal entries. At every stage $`e f|_{eX}`$ is injective by triangularity with identity diagonal on added slots, and (1) holds with the same extended $`\phi`$.

The zero-defect submodule property of the base survives each batch. Intersect a candidate pair $`J,Z`$ with the lower modules and project onto the high modules. Each is an admissible pair for, respectively, the lower graph and the identity on $`M^l`$ ($`l=1`$ or $`s`$). The nonnegative defects add because the negative sign projection for $`w`$ is exact. At zero defect the lower intersections vanish, and the top images coincide in some $`U\le M^l`$: the quotient of the two nested images is semisimple of type $`M`$ and $`e`$ vanishes there, hence zero. A nonzero $`U`$ contains a simple copy $`m\mapsto(c_1m,\ldots,c_lm)`$ with $`c_j\in k`$ not all zero. On this copy, $`J`$ and $`Z`$ are graphs of $`T`$-linear maps to the lower $`X_L,Y_L`$ (with the appropriate lower space at a passive step). Their containment after (2) would imply $`\sum c_j a_j\in D_{f_L}`$, a contradiction. Thus no nonzero zero-defect pair exists.

## 2. A genuine class-two group on the same coordinates

In the natural 20-site representation, put

```math
\beta(x,y)=(x_i y_i)_{i\in\mathbb P^1(19)}
                -\frac{\sum_i x_i y_i}{20}\mathbf{1}\ \in M .
```

This symmetric bilinear map is $`T`$-equivariant and nonzero (use $`e_0-e_\infty`$ twice), hence spans $`M`$ by simplicity. Its common radical is zero by the same simplicity. Choose symmetric matrices $`C_1,\ldots,C_s`$ of size $`s`$ over $`k`$, and use the $`s`$ copies of $`M`$ in the *passive minus* space as central output coordinates. On $`V=X\oplus Y`$, with active coordinates $`(x_i,y_i)`$, put in output slot $`h`$

```math
[v,v']_h=\sum_{i,j}(C_h)_{ij}\bigl(\beta(x_i,y'_j)-\beta(x'_i,y_j)\bigr).
                                                               \tag{3}
```

Every other bracket component is zero. Define $`P(C)`$ by the actual product $`v*v'=v+v'+[v,v']/2`$. Bilinearity and central output give associativity directly, inverse $`-v`$, exponent three, and commutator (3). Both $`T`$ and $`z`$ are group automorphisms, since the bracket flips sign on the mixed input and lands in a minus slot. Let $`G=P(C)\rtimes T`$, adjoin $`z`$, use $`\Lambda=`$ all outside involutions, $`K=z\Lambda`$, and take the physical subgroup

```math
H=\{((x,f(x)+d(g)),g): x\in X,\ g\in B\}.
```

It really is a subgroup with the old cardinality: the active coordinates of two graph entries, even after the $`B`$ action, are *diagonal*; symmetry of every $`C_h`$ and of $`\beta`$ makes (3) vanish there. Their BCH product on that graph equals the old additive product. The derivation has no active coordinates.

The number of actual marked lifts is unchanged: $`(v,zi)`$ is an involution iff $`(zi)v=-v`$ in vector coordinates, since group inverse is $`-v`$. This is true also for $`i=1`$. After multiplication by $`z`$, the physical sheets are $`Y`$ and $`A_i=X_i^-\oplus Y_i^+`$ as before. Thus $`|K|=20|Y|=[G:H]`$. Avoidance cannot be inferred from these numbers alone.

For an alleged vertical collision a $`w_0\in W=\operatorname{graph}(f)`$ is inverted by an actual outside involution. After dropping passive and base coordinates the kernel is abelian, and on an active diagonal pair it requires $`(i x,-i x)=(-x,-x)`$; hence $`x=0`$ in every active slot. Such a $`w_0`$ commutes with the **whole** $`P(C)`$ by (3). Its inversion condition is now the genuine linear condition for the pure sign $`zi`$. At $`i=1`$ the base-sheet graph meets $`Y`$ only at zero; for any nonidentity $`i`$ use its $`B`$-conjugacy to $`w`$ and the injection $`ef|_{eX}`$. Thus there is no nonidentity vertical collision. This step is needed: in a nonabelian kernel a conjugated lift need not act as its pure linear sign everywhere.

For a nonvertical collision, conjugate the projected pair by a true lift in $`H`$ to $`(zw,r^j)`$. A power of that same inverted $`H`$ element lies over $`r^3`$ with the same inverter. Now quotient the entire passive-minus subspace $`C_0=M^s\le Y_L`$ (central in $`P(C)`$ and $`T,z`$-stable); the kernel is abelian, and the alleged collision remains nonidentity over $`r^3`$. This quotient need **not** define a Bol loop. It is used solely to separate that physical nonvertical collision. On its vector kernel, further quotient by the graph, its $`zw`$-image, and $`(r^3-1)V`$. Concretely $`(x,y)\mapsto y-f(x)`$ first kills the graph and the remaining quotient is

```math
S=Y/\big(C_0+(f+w f w)X+(r^3-1)Y\big).
```

It is a local $`r,zw`$-module; here $`r^3`$ acts trivially and $`zw`$ by $`-w`$. The vector of an $`H`$ element over $`r^3`$ has affine residue $`D=d(r^3)`$ in $`S`$. The variable vector part of a lift of $`zw`$ is in its minus space and contributes nothing to the square of the product on $`S`$. Consequently inverting would require $`(1-w)D=0`$ there. But the originally chosen functional $`\phi`$ kills every term in the denominator, including all of $`C_0`$, and is 1 on $`(1-w)D`$. This is a physical obstruction with variable inverter and stabilizer, not the assumption that a flat additive graph remains sharp after arbitrary multiplication changes. Thus $`H\cap\Lambda^2=1`$, which by conjugacy and the index gives sharpness. Sandwich closure of $`K`$ gives the left Bol identity on $`G/H`$.

## 3. Native simplicity, not merely a simple quotient

Let $`R\lhd G`$ lie within $`P(C)`$. It is a $`T`$-subspace of the original additive space: closure under group products and central commutators implies closure under $`v+v'=v*v'*(-[v,v']/2)`$. Moreover $`R`$ is a bracket ideal by normality, so the true $`R`$-cosets on $`P(C)`$ are precisely its additive cosets. No $`z`$-stability of $`R`$ is assumed. Projection of the genuine $`K`$ sheets modulo $`R`$ has exactly the old sizes, because the sheets as *sets* were just verified; $`H\cap R=W\cap R`$ also has exactly the old size. In particular the ratio $`|KR/R|/[G:HR]`$ is

```math
\frac{3^{d_R-\dim(R\cap Y)}+19\,3^{d_R-\dim(R\cap A_w)}}{20},
 \qquad d_R=\dim R-\dim(R\cap W).
```

The two exponents are nonnegative by linear vertical avoidance. Recall the all-cut argument in detail: if both vanish, $`R=(R\cap W)\oplus(R\cap Y)`$ as vector spaces. Writing $`J_0=\pi_X R`$ and $`Z=R\cap Y`$, $`R`$ is the tilted graph of $`f|_{J_0}`$ modulo $`Z`$, a $`T`$-map $`\bar f:J_0\to Y/Z`$. The $`x`$-image of $`R\cap A_w`$ is $`(\ker\bar f)^-_w`$: its negative $`x`$-value has negative image under $`\bar f`$, which can be represented by a positive vector only when its image is zero. The vertical kernel here is $`Z^+_w`$. Therefore equality of the second exponent gives $`\dim e(\ker\bar f)=\dim eZ`$. The pair $`(\ker\bar f,Z)`$ is admissible, so both vanish by §1. If $`R`$ were still nonzero, its graph would be an actual $`T`$-linear restriction of $`f`$ on $`J_0`$, making $`(J_0,f(J_0))`$ another nonzero zero-defect pair by the negative injection. This is impossible. Thus all proper nonzero vertical normal cuts are strict.

If $`R\lhd G`$ projects onto $`T`$, then $`G/R`$ is a 3-group. The **pure** copy of perfect $`T`$ in this split $`G`$ must die in that quotient, so is contained in $`R`$. Every commutator target is a sum of copies of $`M`$ in passive-minus slots, centralized by the kernel and spanned by its differences under $`T`$; all of $`C_0`$ therefore dies as well. The remaining abelian kernel modulo coinvariants has only the single old $`Y_0`$ line. For a proper such $`R`$, $`H`$ and $`K`$ both surject onto this surviving line; consequently $`|KR/R|=3>1=[G:HR]`$. This exhausts normals by simplicity of $`T`$. These strict inequalities also exclude any nontrivial core of $`H`$. And $`\langle K\rangle=\langle\Lambda^2\rangle`$ is normal, contains pure involutions generating $`T`$ and all of $`Y`$, so the same quotient calculation proves generation. Hence $`G`$ is the faithful native left multiplication group. A nontrivial proper loop quotient would induce a nontrivial proper translation-group kernel with equality of the projected section count and group index, contradicting the strictness just proved.

Embedding the base signed group with zeros in the added slots respects its group law, the actual stabilizer intersection and the selected marks, hence the induced coset injection preserves **every** base product. Its right-alternative failure persists. Every translation above a projective involution has square in the exponent-three kernel, and every vertical translation has order at most three. Sharpness and power closure identify translation and native element orders; the old order-six element persists. The radical is precisely $`P(C)`$ since the quotient is nonabelian simple.

## 4. Distinct actual loops and the cubic-logarithmic growth

As a first choice activate $`k`$ separate diagonal coefficients, sending active pair $`i`$ by (3) to passive output $`i`$ for $`i\le k`$ only. The commutator spans exactly those $`k`$ copies of $`M`$ by surjectivity of the span of $`\beta`$, giving $`|P(C)'|=3^{19k}`$. Hence the $`s+1`$ left multiplication groups are inequivalent. Isotopy of loops implies isomorphic left multiplication groups: if $`(A,B,C)`$ is an isotopism and $`A(a)`$ is the target identity, then $`B=C L_a`$ and the new translations are the conjugates of $`L_x L_a^{-1}`$, which together still generate the original left group (take $`x=1`$). Thus these loops are pairwise nonisotopic.

For the stronger count fix $`C_1=I_s`$ and choose $`C_2,\ldots,C_s`$ so that the matrices are linearly independent. This gives exactly the numerator in the statement as ordered coefficient arrays. In every case $`P(C)'`$ is the whole passive output $`M^s`$: evaluating pure high tensors gives $`\beta(v,w)`$ times the coefficient vectors at each entry $`(i,j)`$, and these vectors span $`k^s`$ by independence. The center of $`P(C)`$ consists exactly of vectors with zero active coordinates. In fact the first coefficient matrix is $`I_s`$, so a nonzero active coordinate pairs nontrivially with a vector in the opposite wing at that same index, using the zero common radical of $`\beta`$. These two spaces give intrinsic $`T`$-modules $`P/Z(P)\cong M^{2s}`$ and $`P'\cong M^s`$; inner kernel elements act trivially on both. Distinct coefficient arrays give different actual alternating commutator maps on these two *fixed* additive spaces (test pure slots with a nonzero product $`\beta`$).

An isomorphism of the native groups takes the characteristic radical to the radical and hence identifies these two tensors compatibly with one automorphism of $`T`$. For a fixed automorphism the transporting linear maps, if any, form torsors for $`\operatorname{GL}_{2s}(3)`$ and $`\operatorname{GL}_{s}(3)`$ by $`\operatorname{End}_T(M)=k`$. Their choices determine at most one transported commutator tensor, regardless of any choices of representatives, complements, or central automorphisms. Since $`T`$ is generated by two elements, $`|\operatorname{Aut}T|\le3420^2`$. Thus at most $`3420^2\,3^{5s^2}`$ distinct arrays belong to any one possible isomorphism class of native left group. This proves the claimed lower bound without treating inequivalent coordinate graphs as inequivalent loops. For the simplified estimate, $`3420^2<3^{15}`$ and every numerator factor is at least $`3^{s(s+1)/2-1}`$. Its base-three logarithm after division is at least $`s^3/2-5s^2-3s/2-14\ge s^3/4`$ for $`s\ge21`$. One does not need to compute a full automorphism group or classify symmetric pencils to get this lower bound.

[Review and reproduction](../verification.md) · [Overview](../README.md)
