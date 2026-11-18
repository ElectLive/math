# Even-dimensional tensor operators: split, quadratic and mixed profiles

**Mira Cult**

We finish the [ordinary tensor theorem](../../manuscripts/0108-ordinary-tensor-idealizers.md) in even natural dimension $`d\ge4`$ and odd characteristic. The determinants of the factors distinguish physical operator cosets, while one operator can have two normalized presentations. Keeping both facts straight is essential at ranks four and six.

## Actual outside classes: split, quadratic, or both

Write $`S=\mathrm{SL}_d(q), T=\mathrm{PSL}_d(q), V=\mathrm{Mat}_d(q)^+,\ d=2e,\ D=d(d-1)/2`$. The kernel is faithful irreducible. With $`W=H\cap V,\ J=HV/V`$, the original marks avoid $`H`$ in their nonidentity square. The marked quotient acts faithfully as $`Y`$ and one outside normalizer coset of ordinary operators $`P\otimes Q`$ in this case. Two pairs present the same linear operator exactly by inverse scalar changes. The coset modulo $`Y`$ is determined by

```math
\kappa=\det P\,\det Q\quad\text{and}\quad
 \det P\bmod(\mathbf F_q^\times)^d .
```

Indeed equality of the latter lets one rescale inversely to match the first determinants before removing special-linear factors on both sides. Each outside involution has $`P^2=cI,\ Q^2=c^{-1}I`$, so $`\kappa=\pm1`$. The [profile preparation](ordinary-profiles.md#why-a-common-complement-exists) excludes the implemented coset $`Y`$. The central scalar $`-1`$ in $`Y`$ acts fixed-point-freely on the odd radical; the [odd-kernel splitting lemma](../../manuscripts/0101-odd-kernel-block-action.md) gives a stable split complement. Thus pure zero-vector marks in that identification over every selected quotient label are genuine, as are their full negative eigenspace translates. The projected canonical translations still generate $`Y`$. These facts refer to actual original marks, not a freely chosen set of quotient involutions.

*Split quadratic polynomial.* If $`c`$ is square, inverse rescaling normalizes the squares to identity. Write the operator as $`-A\otimes B`$ for involutions $`A,B`$ with negative dimensions $`r,s\in\{0,\ldots,d\}`$. There is exactly the simultaneous sign ambiguity, interchanging $`(r,s)`$ with $`(d-r,d-s)`$. Since $`d`$ is even, $`\kappa=(-1)^{r+s}`$ and the first determinant tag is $`(-1)^r`$. For each normalized profile the two eigenbasis changes can be adjusted to determinant one in their centralizers, so the profile orbit has the usual size $`q^{r(d-r)+s(d-s)}{d\brack r}_q{d\brack s}_q`$ before identifying signs. Count a selected union by summing **all** its normalized presentations and dividing by two; this also handles the self-complementary middle profile without double-counting. The negative tensor sheet is the sum of its two same-sign blocks, as in the [odd-dimensional spectral argument](ordinary-profiles.md#the-spectral-interval).

*Nonsplit quadratic polynomial.* Fix any nonsquare $`c`$. Each nonsplit operator has exactly two reciprocal scalar normalizations squaring to $`cI,c^{-1}I`$. Both matrices have the quadratic irreducible module repeated $`e`$ times. All normalized pairs form a **single** $`S^2`$-class: their $`\mathrm{GL}_d`$ centralizers are $`\mathrm{GL}_e(q^2)`$, whose determinants over $`\mathbf F_q`$ are all field norms of determinants over $`\mathbf F_{q^2}`$, hence surjective. The corresponding full class of physical tensor operators has size

```math
C_n=\tfrac12\big(|\mathrm{GL}_d(q)|/|\mathrm{GL}_e(q^2)|\big)^2
     =\tfrac12 q^{d^2}\prod_{\substack{1\le j\le d\\j\ {\rm odd}}}(1-q^{-j})^2. \tag{1}
```

In particular it has defining-prime part $`q^{d^2/2}`$, by the unipotent exponents in the quotient of the two general linear orders (the half is prime to $`p`$). Its negative sheet has dimension $`d^2/2`$: it consists precisely of the intertwiners $`PX=-X(Q^\mathsf t)^{-1}`$, between two equivalent direct sums of irreducible quadratic modules. After one isomorphism this is a copy of $`\mathrm{Mat}_e(q^2)`$. It realizes every even matrix rank, and every determinant in full rank by the norm. The $`S^2`$-conjugates therefore cover every even rank; the original $`W`$ has only **odd** ranks at its nonzero entries. The [graph-of-matrices incidence bound](tensor-capacity.md) applies over an arbitrary odd field as well: modulo a prime of $`q+1`$, projective point counts of an intersection have the parity of its vector dimension, and the Gram matrix of these graphs is all-ones minus identity in even $`d`$. Omitting unused vertical points gives

```math
|W|\le q^d(q^d-1)/(q-1)+1< p q^{2d-1},\qquad
                         |W|\le q^{2d-1},                              \tag{2}
```

where the last step uses that $`|W|`$ is a power of $`p`$.

This nonsplit class has $`\kappa=+1`$ and tag $`(-c)^e`$; the terminology refers to the *quadratic polynomial*, not to a nonsplit group. Put $`a_2=v_2(q-1), b_2=v_2(d)`$. If $`q\equiv3\bmod4`$, $`-c`$ is square, so its $`e`$-th power is a $`d`$-th power and the coset is implemented. Otherwise $`-c`$ is nonsquare. Its $`e`$-th power then has nontrivial determinant tag precisely when $`b_2\le a_2`$: use the exponent in the cyclic scalar group modulo $`\gcd(d,q-1)`$, whose odd part already divides $`e`$. A split operator in a nonimplemented $`\kappa=+1`$ coset must have both $`r,s`$ odd and tag $`-1`$ not a $`d`$-th power, which requires $`a_2\le b_2`$. Thus coexistence is possible only when $`a_2=b_2\ge2`$; in particular $`4\mid d,\ q\ge5`$.

## A split balanced profile is never selected

For any selected split profile the [individual orbit bound](ordinary-profiles.md#the-spectral-interval) and the rank argument carry over:

```math
|W|\ge q^{(r-s)^2},\qquad
        W\text{ avoids every nonzero rank }\le d-|r-s|.                 \tag{3}
```

The proof only uses the genuine odd-kernel orbit of a mark under the mark-normalized $`p`$-group in $`J`$, and two eigenflags. Passing through the scalar cover uses a central prime-to-$`p`$ kernel and the unique complement to that central kernel over a $`p`$-subgroup. In the normalized pair a unipotent conjugator cannot carry $`A`$ to $`-A`$: conjugation would interchange $`A,-A`$ despite odd order. Hence the same upper unitriangular orbit sizes hold even after simultaneous signs are identified.

If $`r=s`$, (3) gives $`W=0`$. For $`0<r=s<d`$ the equality of the genuine normalized-$`p`$-subgroup orbit and the full two-unitriangular orbit forces a pure transvection in $`J`$. Every affine lift over it is in the marked square of this profile: diagonalize an involution reversing the transvection in a basis adapted simultaneously to its image/kernel flag and the image of the lift vector, then choose the matching other involution on the kernel/quotient of that vector. The [full argument](ordinary-profiles.md#why-a-balanced-profile-is-impossible) uses only matching sign dimensions and $`1\le r<d`$; special-linear conjugacy is provided by the determinant-flexible split centralizers. It works with additional selected classes and gives the actual stabilizer collision. The balanced endpoints $`r=s=0`$ or $`d`$ represent the implemented scalar $`-1\in Y`$, impossible. Both pairs with $`|r-s|=d`$ give the implemented identity. Thus if there is a split class, let $`1\le m=\min |r-s|\le d-1,\ \rho=d-m`$; $`W`$ has minimum rank at least $`\rho+1`$.

## Only split classes

The matched-sign involution bound (3) is termwise; the ordinary mass equation here is the sum over normalized presentations divided by two. Because the parity of the difference is fixed, half the total number of ordered pairs of difference at least $`m`$ is bounded by $`\sum_{i=0}^{\lfloor\rho/2\rfloor}(\rho+1-2i)\le(\rho+2)^2/4`$. Thus all the estimates (1)--(6) of the [idealizer theorem](ordinary-idealizers.md) hold with the harmless counting constant $`(\rho+2)^2`$ in place of $`(\rho+1)(\rho+3)`$. In particular, with $`a`$ the larger support dimension, $`x=d-a`$, comparison of the forced and allowed pure kernel orders gives a contradiction as soon as

```math
q^B>(6/5)(\rho+2)^2,\quad
 2B=m^2+4mx-3x^2+\rho^2-\rho-2-a\lfloor a/(\rho+1)\rfloor.
```

For $`\rho\ge5`$, already $`B\ge\rho`$ also at $`m=1`$, by substituting $`m=1`$ in the lower bound (6) there; $`3^\rho>(6/5)(\rho+2)^2`$. For $`\rho=4,\ m\ge4`$ it gives $`B\ge66/10`$; at $`m=2,d=6`$ directly $`2B\ge8`$ for $`a=5,6`$. For $`\rho=3,\ m\ge5`$ it gives $`B\ge52/8`$; at $`m=3,d=6`$ directly $`2B\ge7`$ for $`a=4,5,6`$. All suffice.

For the exceptions at the ends of this estimate, use the defining-prime part of the same mass identity. With $`M=\max|r-s|`$, the integer

```math
{\cal S}=\sum_{(r,s)\ {\rm normalized}}q^{M^2-(r-s)^2}{d\brack r}_q{d\brack s}_q
```

satisfies $`v_p({\cal S})/v_p(q)\ge\binom{\rho}{2}`$ by the [pure unipotent support bound and mass equation](ordinary-profiles.md#a-defining-prime-valuation); the extra factor $`1/2`$ has zero defining-prime valuation. Equivalently the same bound holds for the physical sum divided by two. At $`d=4,\rho=3,m=1`$, a largest-difference class count modulo $`q`$ has at most four physical terms (all differences odd, no self-complementary class), and the Gaussian factors are 1 modulo $`q`$. Thus $`q\ge5`$ is impossible. For $`q=3`$ the tag of $`-1`$ is nontrivial modulo fourth powers, so the parity of $`r`$ itself is fixed; at difference one there are at most two complementary-profile orbits, and at difference three at most two. The number of largest-difference physical classes is then prime to three, again impossible.

If $`\rho=2`$, then $`m=d-2`$ even, $`\kappa=+1`$, and both $`r,s`$ must be odd to be nonimplemented. The only profiles of difference at least $`d-2`$ are $`(1,d-1),(d-1,1)`$, one physical class. Its normalized physical mass has valuation zero after removing its leading power, contradicting the lower bound $`\binom22=1`$. Finally if $`\rho=1`$, the physical operators are pure rank-one reflections in one factor or the other. Both kinds are needed for quotient generation, each one class of size $`q^{d-1}(q^d-1)/(q-1)`$; the sheet dimension is $`d`$. Exactly as in the [extremal argument](ordinary-profiles.md#the-extremal-obstruction), both pure kernels have a $`p`$-subgroup larger than the maximal unitriangular group on $`d-1`$ coordinates and so contain rank-one transvections. The two pointwise fixed-space restrictions give $`|W|\le q^{(d-1)(d-2)}`$ against (3), $`|W|\ge q^{(d-1)^2}`$. No all-split candidate remains.

## Only the nonsplit quadratic class

Here $`|J|=(q^{d^2/2}/|W|)|Y|/C_n`$, so $`|J|_p=q^{2D}/|W|`$. Choose a primitive prime $`\ell`$ for $`q^d-1`$, by Bang--Zsigmondy (odd $`q`$, even $`d\ge4`$ has neither classical exception). Then $`\ell>d,\ \ell\nmid q-1`$. Formula (1) shows that $`C_n`$ is $`\ell`$-prime: the $`q^d-1`$ factor in the general linear numerator and denominator cancels. Hence $`|J|_\ell=|T|_\ell^2`$, and **both** actual endpoint projections contain $`\ell`$. An $`\ell`$-element in either projective projection lifts to a pure-order-$`\ell`$ matrix in its full inverse image in $`S`$; it acts irreducibly on the natural $`d`$-space since the order of $`q`$ modulo $`\ell`$ is $`d`$. In particular both endpoint matrix groups act irreducibly. There is no assumption that $`J`$ is a direct product of its projections. If $`W=0`$, then $`|J|_p=q^{2D}`$, so up to conjugacy its image in $`T^2`$ contains the full product of the two standard unitriangular groups. Each endpoint lift to $`S`$ contains the full standard $`U`$ and is irreducible, so equals $`S`$. Here is the Bruhat argument explicitly. Every member of a subgroup $`E\ge U`$ can be written as $`u_1 n u_2`$, with $`n\in E`$ determinant-one monomial. Draw $`j\to i`$ if $`E`$ contains the whole root group $`I+tE_{ij}`$, $`t\in\mathbf F_q`$. The standard upper arrows occur; all monomials in $`E`$ preserve this directed graph. If it is strongly connected, elementary commutators along simple paths give all root groups, generating $`S`$. Otherwise its strongly connected components are consecutive blocks in a total order, by the upper arrows. Each monomial preserves this order and fixes each block; the subspace spanned by the initial block is invariant under every such monomial and $`U`$, hence under $`E`$, contradicting irreducibility. With both projective projections full and a full pure $`p`$-subgroup, the image in $`T^2`$ is full by simplicity (a diagonal graph has $`p`$-order only $`q^D`$). This would force $`[Y:J]\le |Z(Y)|=\gcd(d,q-1)`$. But $`[Y:J]=C_n/q^{d^2/2}=\frac12\prod_{1\le j\le d,\ j\ {\rm odd}}(q^j-1)^2`$ is larger for $`d\ge4,q\ge5`$. Thus $`W\ne0`$.

A rank-one element of $`W`$ is impossible: any two rank-one tensors with different image and row lines sum to rank two, forbidden by (2)'s parity argument. Thus, if there are any, *all* rank-one members have one common image line or one common row line (choose two distinct lines on one side to force the common line on the other). This would give one endpoint an invariant line. In particular the minimum rank in $`W`$ is at least three, and both total supports of $`W`$ are the full natural spaces by endpoint irreducibility.

Consider its full left and right idealizer algebras over $`\mathbf F_p`$, in the two natural matrix algebras (using right multiplication or the transpose-dual identification). Each is normalized by the corresponding endpoint: conjugating a pure endomorphism by a pair preserving $`W`$ cancels the opposite action. Its nilpotent Jacobson radical has a nonzero common annihilator on the natural space; this is an $`\mathbf F_q`$-subspace invariant under the endpoint, so equals the whole space. Hence both effective idealizers are **semisimple**, without asserting $`W`$ is $`\mathbf F_q`$-linear. The endpoint permutes their primitive central idempotents transitively since otherwise a nonempty proper sum of their image spaces would be invariant. Consequently all simple matrix blocks on each side have the same matrix size on that side.

At least one side's matrix size is one. Otherwise take primitive matrix idempotents $`e_1,f_1`$ on the two sides such that $`w=e_1 W f_1`$ has a nonzero member (insert the two complete sums of primitive idempotents into any nonzero member, and use one nonzero summand). Take another primitive diagonal idempotent $`e_2,f_2`$ in each corresponding simple block. Left and right off-diagonal units transport that member into $`e_2 W f_2`$ without changing its rank, since the reverse units undo the transport on the corner. The two maps have images in disjoint spaces and are supported on disjoint direct summands of their domains, so their sum has *twice* the same nonzero rank, a contradiction. This is a two-sided rank argument; disjoint image spaces alone would not prove rank additivity.

Thus one idealizer is a product of finite fields, whose units are prime to $`p`$, so the corresponding pure kernel of $`J`$ has order prime to $`p`$. Projection on the opposite projective factor forces $`|J|_p\le q^D`$; hence $`|W|\ge q^D`$, contradicting (2) if $`d\ge6`$.

For $`d=4`$ each nonzero effective idealizer element has rank at least three by the full supports and the minimum rank of $`W`$. Two nonzero orthogonal primitive idempotents are already impossible; both semisimple idealizers are fields. Both pure kernels have $`p'`$-order. Hence each projective projection has $`p`$-part $`|J|_p=q^{12}/|W|\ge q^5`$. If one idealizer field $`F`$ is not contained in the scalar $`\mathbf F_q`$, then $`\mathbf F_q F`$ is a product of finite fields (it is a quotient of the tensor of two finite separable fields over $`\mathbf F_p`$). Its primitive component spaces are permuted by the endpoint. The irreducible $`\ell>4`$ element must fix each component, so there is just one component, a field of order $`q^b`$, $`b=2`$ or $`4`$. Its normalizer in $`\mathrm{GL}_4(q)`$ has $`p`$-part at most $`q^2`$: the kernel of its action on the field is $`\mathrm{GL}_{4/b}(q^b)`$, and the field automorphism quotient divides $`b`$, prime to $`p`$. This contradicts $`q^5`$. Both pure idealizers therefore consist solely of scalars. A nontrivial pure scalar cannot lie in $`J`$: its cyclic subgroup is central in $`Y`$, has prime-to-$`p`$ order and zero common fixed space on $`V`$, forbidden by the [odd-kernel block-core test](../../manuscripts/0101-odd-kernel-block-action.md). Thus the pure kernels are trivial and $`|J|\le|T|`$. Yet (1),(2) and $`|S|\ge(5/6)q^{15}`$ give

```math
\frac{|J|}{|T|}=\frac{|S|}{[Y:J]}
   \ \ge\ \frac{(5/6)q^{15}}{(1/2)|W|q^8}>1 .
```

This settles the nonsplit-only branch.

## Both types actually selected

Here $`4\mid d,\ q\ge5`$, both split dimensions are odd and $`m\ge2`$ is even. From (2),(3), $`m^2\le2d-1`$, and the larger support dimension $`a`$ obeys $`\rho+1\le a\le d`$. The full index now includes both contributions, so use

```math
[Y:J]\le |W|\,q^{d^2/2}\big((\rho+2)^2+1\big).
```

Indeed the split sum has the additional factor $`q^{-3m^2/2}`$ in the ordinary mass upper bound, while the nonsplit term is at most $`(1/2)|W|q^{d^2/2}`$ by (1). Thus the larger-support pure kernel has lower bound

```math
\frac{5q^{d^2/2-1}}{6((\rho+2)^2+1)|W|},\qquad
                  |W|\le\min(q^{2d-1},q^{a(a-\rho)}).                 \tag{4}
```

Its actual upper bound is still (2) of the [idealizer theorem](ordinary-idealizers.md). For $`d\ge8`$ as above, $`d-\sqrt{2d-1}+1>d/2`$, hence the integer $`\lfloor a/(\rho+1)\rfloor=1`$. The upper exponent is at most $`dm`$: in that formula use $`a\ge\rho+1,\ a\le d,\ x=d-a\le m-1`$, which bounds it by $`D-\rho(\rho+1)/2+d+(m-1)m/2=dm`$. If $`d\ge16`$, $`m\le\sqrt{2d-1}<d/2-2`$, so (4) exceeds this upper bound by a factor at least $`5q^d/[6((\rho+2)^2+1)]>1`$. For $`d=8`$ the only $`m`$ is two; for $`d=12`$ it is two or four. Substitution of the integer support range into (4) and the unsimplified upper bound gives minimal **twice** exponent gaps respectively 14, 70 and 32. Each is more than enough at $`q\ge5`$.

Finally $`d=4`$ forces $`m=2`$; the only possible split profile orbit is $`(1,3),(3,1)`$. There is precisely one split class and one nonsplit class. Setting $`n=(q^4-1)/(q-1)`$, (1) and the split formula give

```math
[Y:J]=|W|\big(n^2/q^4+(q-1)^2(q^3-1)^2/2\big).
```

As $`n\equiv1\bmod p`$, $`|J|_p=q^{16}/|W|\ge q^9`$. At least $`q^3`$ therefore occurs in either pure kernel. The split profile imposes minimum rank three and $`|W|\ge q^4`$ by (3). If both supports had dimension at most three, deleting two rows gives $`|W|\le q^3`$. Thus the larger support has dimension four; on that side the pure $`p`$-part is at most $`q^{6-2(8-2-1)/2}=q`$ by the defining-prime rank bound. This contradicts $`q^3`$ and completes the last mixed case.

The [source checker](../code/verify_even_odd_tensor_completion.py) tests determinant coverage in small quadratic intertwiner spaces, class orders, support inequalities and two-sided corners. The [independent checker](../code/check_a052_quadratic_corners.py) includes 2,592 actual reciprocal-sign operators over the nine-element field. The proof is the uniform rank, group-order and stabilizer argument above, not extrapolation from those controls.

[The ordinary theorem and its scope](../../manuscripts/0108-ordinary-tensor-idealizers.md).
