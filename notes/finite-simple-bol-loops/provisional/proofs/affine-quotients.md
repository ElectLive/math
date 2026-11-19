# All quotients of the affine Burnside example, and an intrinsic linear-operator classification

**Mira Cult · Provisional research.** Author proof, not independently reviewed.

The proof proposes a complete normal-quotient lattice for the infinite affine example and an intrinsic linear-operator classification in finite dimension. Neither is part of the review of the underlying Burnside construction.

## The infinite example is just infinite

Use the [explicit two-generator loop](../../bol-burnside/two-generators.md) $`Q=F\times R`$, $`F=\mathbb F_p`$, $`p`$ odd, $`R=F[t,(1-t^{p-1})^{-1}]`$, and let $`V=0\times R`$. For $`N\trianglelefteq Q`$ write $`U=N\cap V`$, identifying this with an additive subgroup of $`R`$.

**Normal lattice.** The vertical normals are precisely $`0\times I`$ for ideals $`I`$ of $`R`$. The others are precisely $`Q`$ and the preimages of the $`p`$ nonvertical lines of the plane $`Q/(0\times tR)=F^2`$.

Indeed the return moves in (3) of the explicit proof fix $`0`$ on $`V`$ and are words in left and right multiplications by constants. Such maps preserve every congruence, so $`U`$ is stable under all $`f_i/f_j`$, $`f_i=1+it`$. These generate $`R`$ as an $`F`$-algebra, so $`U`$ is an ideal. Every such vertical ideal is realized by reduction of the actual table modulo the ideal. If $`(i,z)\in N`$ with $`i\ne0`$, the products $`(i,z)(0,v)`$ and $`(0,v)(i,z)`$ have the same quotient image. Their second coordinates differ by $`2itv`$. Applying the base shifts and the additive law on $`V`$ shows $`2itv\in U`$ for every $`v`$, so $`tR\subseteq U`$. Modulo this ideal the law is vector addition in $`F^2`$, proving the stated lattice. Existence of the preimages and the lack of other normal subloops follow from the ordinary loop homomorphism correspondence.

Every nonzero ideal of this localization contains a nonzero polynomial, and its quotient is finite. Thus every proper quotient of the infinite loop is finite: $`Q`$ is **just infinite** as well as residually finite. An irreducible specialization of degree at least two has exactly the three normals $`1,V,Q`$, because $`t`$ is invertible. Such a proper Bol loop is not simple; its nontrivial proper normal is the additive group of the extension field.

## Which finite loops are classified?

Fix an odd prime $`p`$. Consider **all finite Bol loops of exponent $`p`$ whose associated Bruck loop is abelian and whose abelianization has order $`p`$**. The abelianization here means the actual largest abelian-group quotient, not the matched multiplication group's abelianization. Aside from $`C_p`$, this class is parametrized by a nonzero finite-dimensional $`F`$-space $`V`$ and an operator $`T\in\mathrm{End}_F(V)`$ with **no eigenvalue in $`F`$**, modulo the equivalences below. The native table in suitable coordinates is

```math
(i,u)(j,v)=(i+j,\,v+f_{i+2j}f_i^{-1}u),\qquad f_i=I+iT.
 \tag{1}
```

Here is the exact input. The separately [reviewed alternating-algebra theorem](../../odd-degree/manuscripts/abelian-bruck-fibers-as-alternating-algebras.md) identifies every finite odd Bol loop with abelian associate $`(A,+)`$ with an intrinsic alternating biadditive $`b`$, with $`J=\langle b(A,A)\rangle`$ abelian as a native group, $`b(J,J)=0`$ and $`I-b(x,-)`$ invertible. Its native law is $`x+y+(I-b(x+y,-))^{-1}b(x,y)`$ and $`J`$ is its native abelian-derived subloop. In the present finite class $`A`$ is an elementary abelian $`p`$-group, because original and associated powers agree, and $`A/J`$ has dimension one. Write $`A=Fe\oplus V`$, $`V=J`$, and $`T(v)=-b(e,v)`$. Then $`J=TV`$ forces $`T`$ invertible, and invertibility of every $`I+iT`$ excludes the remaining rational eigenvalues. Conversely these conditions on $`T`$ give exactly this alternating algebra by $`b((i,u),(j,v))=jTu-iTv`$, hence precisely this class. In the native table from the input, replace the fiber coordinate $`u`$ at base $`i`$ by $`f_i u`$ to obtain (1). This last computation uses that all $`f_i`$ commute. Every nonidentity element has order $`p`$ by the same single-shear power computation as for the scalar example.

In the noncyclic case the fiber $`V`$ is intrinsic even without the bracket construction: it is the entire right nucleus. With $`x=(i,u),y=(j,v),z=(k,w)`$, subtract the second coordinate of $`x(yz)`$ from that of $`(xy)z`$. Direct expansion in (1) gives

```math
2k T^2 f_{i+j}^{-1}(j f_i^{-1}u-i f_j^{-1}v).
 \tag{2}
```

Since $`T`$ is invertible, (2) vanishes for all $`x,y`$ exactly when $`k=0`$. Similarly the left and middle nuclei and the commutant are trivial. The actual matched multiplication group is the group of **all** shears $`(j,v)\mapsto(j+i,v+u+jw)`$, order $`p^{1+2\dim V}`$, class two, exponent $`p`$: remove the base shifts from marks over $`i=0,1`$ to obtain two additive graph spaces of slopes $`2T`$ and $`2T f_1^{-1}`$. The difference $`2T^2 f_1^{-1}`$ is invertible, so these generate the whole space of affine shears. This group does not classify the individual loops.

## Native isomorphism, isotopy, and generator rank

**Isomorphism.** Two parameters $`T,T'`$ give isomorphic loops iff $`T`$ is linearly similar to $`cT'`$ for some $`c\in F^\times`$. An isomorphism sends the intrinsic $`V`$ onto $`V'`$, acts there by some linear $`P`$, and induces $`i\mapsto ci`$ on the quotient. Since $`(i,u)=(i,0)(0,u)`$, it is of the form $`(i,u)\mapsto(ci,s_i+Pu)`$. Comparing $`(0,u)(j,0)`$ yields $`PT=cT'P`$. Conversely, given this intertwining, $`s_i=0`$ gives an isomorphism of the entire tables (1).

**Isotopy.** Put $`D=T^{-1}`$. The complete isotopy equivalence is

```math
D' \sim cD+dI\qquad(c\in F^\times,\ d\in F),
 \tag{3}
```

where $`\sim`$ is similarity over $`F`$. In particular all isotopes stay within the stated class. To see exhaustiveness rather than just a set of examples, let $`K=\{L_x\}`$ be the set acting on the original point set. After identifying the output coordinate of any isotopy with the old point set, the new left mark set is $`K\epsilon^{-1}`$ for a bijection $`\epsilon`$ (the change in the second input). Because the new marks contain the identity, $`\epsilon\in K`$. Choose $`m\in K`$ with $`m^2=\epsilon`$, using the native odd exponent and power alternativity. The bijection $`m^{-1}`$ conjugates $`K\epsilon^{-1}`$ to $`m^{-1}Km^{-1}=K`$; the last equality follows from twisted closure in both directions. The original isotope is therefore isomorphic to the law of the **same physical sharply transitive mark set $`K`$ at a different basepoint**. Conversely, the law of $`K`$ at any basepoint $`a`$ is an isotope, by the first-input change $`x\mapsto x a`$.

At basepoint $`(h,s)`$ use relative coordinates $`(i,u)\leftrightarrow(h+i,s+u)`$. The mark sending the basepoint to that point has native parameter $`(i, f_i f_{i+2h}^{-1}u)`$. Its action at the relative point $`(j,v)`$ gives coefficient $`f_{i+2h+2j}f_{i+2h}^{-1}`$. This is (1) for $`T_h=T(I+2hT)^{-1}`$, independently of $`s`$. Thus changing origin adds $`2hI`$ to $`D`$, and the preceding isomorphism criterion allows precisely nonzero scalar dilation in addition to similarity, proving (3).

**Minimal number of generators.** For the noncyclic cases it is $`1+\mu_F(V,T)`$, where $`\mu_F(V,T)`$ is the minimum number of generators of $`V`$ as an $`F[t]`$-module with $`t=T`$. This is the largest number of Jordan primary blocks at any one irreducible polynomial (over $`F`$, using rational canonical form). In a generating tuple choose one member with nonzero first coordinate. Raising it to a nonzero power makes that coordinate 1 without changing its generated cyclic group; write it $`(1,s)`$. All points of this cyclic section are $`(i,s_i)`$ with $`s_i=i f_i f_1^{-1}s`$. Translation of coordinates $`(i,u)\mapsto(i,u+s_i)`$ is an automorphism by (1) because $`s_{i+j}=s_j+ f_{i+2j}f_i^{-1}s_i`$. Normalize the chosen generator to $`(1,0)`$; true base shifts then make all the other generators vertical. In their generated subloop, the vertical span is precisely the $`F[T]`$-submodule they span: the return moves allow $`f_h`$ and $`f_i^{-1}`$ and therefore $`T`$; conversely the inverses $`f_i^{-1}`$ are polynomials in $`T`$ by finite dimensionality, so no table operation or division leaves that submodule. This proves both inequalities and the module formula. In particular the two-generator subfamily consists of precisely the cyclic rational canonical operators. Field specializations correspond only to the irreducible cyclic case.

## Enumeration recipe and overlap

In dimension $`n`$ list functions $`g\mapsto\lambda_g`$ from monic irreducible polynomials over $`F`$ of degree at least two to partitions such that $`\sum_g(\deg g)|\lambda_g|=n`$. These are the similarity classes of $`D`$. Nonzero dilations of its roots, or affine transformations of its roots, preserve block sizes and degrees. Orbits of these data under $`F^\times`$ give ordinary types; under $`\mathrm{AGL}_1(F)`$ give isotopy types. Equivalently the two counting series, including the empty dimension, are

```math
\frac{1}{|H|}\sum_{h\in H}\prod_{O}\prod_{k\ge1}(1-X^{k(\deg O)|O|})^{-1},
```

where $`O`$ runs over $`h`$-orbits on the allowed irreducible polynomials, $`\deg O`$ is their common polynomial degree and $`H`$ is the appropriate group. Each coefficient uses only finitely many factors. This counts ordinary loops, not choices of labeled native generators.

For dimension two all parameters are irreducible. The $`p(p-1)`$ non-base-field elements form one regular affine orbit before Frobenius (an affine map fixing a non-base point is identity). The scalar orbits are the $`p`$ nonrational lines in $`\mathbb P(\mathbb F_{p^2})`$ on this non-base-field set, meaning all $`F`$-lines except $`F`$ itself; the one Frobenius-fixed remaining line is the trace-zero line. This gives one isotope class with $`(p+1)/2`$ ordinary types, **recovering**, not reasserting as new, the previously reviewed [prime-cube fiber calculation](../../odd-degree/manuscripts/abelian-bruck-fibers-as-alternating-algebras.md). The new census is in all dimensions, including repeated and multiple primary blocks. This finite classification does not imply anything about existence of a simple nonassociative loop of prime exponent; the loops here have a large abelian normal subgroup. The intrinsic class has not been enlarged to loops with nonabelian associates or larger abelianization.

[Provisional results and replay](../README.md)
