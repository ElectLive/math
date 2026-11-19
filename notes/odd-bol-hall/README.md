# Odd-order Bol loops without Sylow subloops

**Mira Cult**

A group of order 63 has a subgroup of order nine. A left Bol loop of order 63 need not: the multiplication below projects onto the group of order nine, but no two lifts of an independent pair of quotient vectors commute. At every other odd prime there are analogous examples. The obstruction is not the absence of prime-order elements; it is the impossibility of assembling them into a subloop of the full prime-power order.

A **loop** is a multiplication with a two-sided identity and unique left and right division. It is **left Bol** when $`x*(y*(x*z))=(x*(y*x))*z`$. If $`n`$ is its finite order and $`\pi`$ is a set of primes, a **Hall** $`\pi`$-**subloop** has order $`n_\pi`$, the largest divisor of $`n`$ supported on $`\pi`$. A **Sylow** $`p`$-**subloop** means a subloop of the full order $`n_{\{p\}}`$, not just one maximal by inclusion. A **loop isotope** is a relabeling of the rows, columns and symbols of a Latin square by three possibly different bijections that produces another loop.

[Foguel, Kinyon and Phillips](https://arxiv.org/pdf/math/0208231v2) ask about existence of Hall and Sylow subloops of the original multiplication in Problem 6.10 of their second arXiv version. They use the same left Bol convention. Their Hall theorem for a *twisted subset* or for the associated Bruck multiplication does not say that the subset is closed under the original multiplication. The distinction matters here: a comparison isotope has many subloops of the very order missing in the original example.

## Results

**Theorem.** Let $`p`$ and $`\ell`$ be distinct odd primes. For every $`q=\ell^f`$ with $`p\mid q-1`$, there is an explicit left Bol loop of odd order

$$
p^2 q^{(p-1)/2}
$$

with normal elementary abelian $`\ell`$-kernel and quotient $`C_p^2`$, but **no subloop of order $`p^2`$**. Its order has full $`p`$-part exactly $`p^2`$. In fact every nontrivial $`p`$-subloop is cyclic of order $`p`$. A comparison isotope has exactly $`q^{(p+1)/2}`$ subloops of order $`p^2`$, all isomorphic to $`C_p^2`$.

For **each** odd prime $`p`$ there are odd-order left Bol loops without a Sylow $`p`$-subloop: take $`q=\ell^{p-1}`$ for any other odd prime $`\ell`$. More precisely, for a *fixed set* $`\pi`$ of primes, universal Hall existence across all finite odd-order Bol loops fails whenever $`\pi`$ contains an odd prime $`p`$ and omits an odd prime $`\ell`$. If it contains no odd prime or contains every odd prime, the trivial subloop or the whole loop, respectively, always works. These quantifiers do not say that a given example has no Hall subloop at all; its additive kernel is already a Hall $`\{\ell\}`$-subloop. The examples are solvable and not simple.


## A two-product obstruction at order 63

Write $`V=\mathbb F_3^2`$, $`F=\mathbb F_7`$, $`s(0)=1`$ and $`s(x)=3`$ for $`x\ne0`$. For $`x=(x_1,x_2)`$, $`y=(y_1,y_2)`$ put $`w=x_2y_1-x_1y_2\in\mathbb F_3`$. Exponentiation $`2^w`$ takes place in $`F`$, where 2 has order 3. For $`e=0,1`$ define a native multiplication on the 63 pairs by

$$
 (x,h)*_e(y,t)=\left(x+y,\frac{2^w s(x-y)h+2^{-w}s(y)t+(2^{-w}-1)e}{s(x+y)}\right).
$$

**Finite example.** For $`e=1`$ this is a left Bol loop, with normal subloop $`C_7`$ and quotient $`C_3^2`$, and it has **no subloop of order 9**. For comparison, $`e=0`$ has 49 subloops of order 9. Both loops have 56 elements of order 3 and six of order 7. In particular the counterexample does not violate Cauchy's theorem.

**No section.** The first coordinate is a homomorphism to the additive group $`V`$. Its kernel $`\{0\}\times F`$ has its ordinary addition. A putative subloop $`P`$ of order 9 has trivial intersection with this kernel: the intersection is a subgroup of $`C_7`$ and its order divides 9 because left translation by a preimage within $`P`$ bijects the zero fiber to each nonempty fiber. Thus $`P`$ projects isomorphically to $`V`$. In particular its products commute. Choose linearly independent first coordinates $`x,y`$. The four vectors $`x,y,x-y,x+y`$ are nonzero. On comparing the products in both orders, the coefficients of $`h,t`$ agree; the difference of the two output second coordinates is $`(2^{-w}-2^w)e/3`$. For independent vectors $`w=1`$ or $`-1`$, so this is nonzero for $`e=1`$, regardless of the two chosen lifts. Contradiction. This is stronger than checking that no element has order 9. For $`e=0`$ graphs $`(x,f(x))`$ with $`f(0)=0`$ give all candidates. Substituting in the displayed multiplication gives 81 homogeneous linear equations in eight unknowns over $`F`$, of rank 6, hence $`7^2=49`$ solutions. Both the elimination and a separate enumeration appear in the [reproducibility bundle](REPRODUCE.md). 

**Loop and Bol verification.** The identity is $`(0,0)`$; all fiber coefficients of $`h,t`$ are nonzero. Together with the Latin square of $`V`$, this proves unique solution in either argument. The following finite exact verifier, including the definition of addition modulo 3 and all integer ranges, is a direct verification of the left Bol identity that requires no group theorem, dependency or external table. Save as Python 3.8+ and run without optimization. It verifies the universal identity, not a sample.

```python
from itertools import product
U = list(product(range(3), range(3), range(7)))
def s(x,y): return 1 if x%3 == y%3 == 0 else 3
def mul(X,Y,e):
    a,b,h = X; c,d,t = Y
    w = (b*c-a*d)%3
    m,n = pow(2,w,7),pow(2,(-w)%3,7)
    H = (m*s(a-c,b-d)*h + n*s(c,d)*t + (n-1)*e) * pow(s(a+c,b+d),-1,7)
    return (a+c)%3,(b+d)%3,H%7
for e in (0,1):
    T = [[U.index(mul(x,y,e)) for y in U] for x in U]
    assert all(T[x][T[y][T[x][z]]] == T[T[x][T[y][x]]][z]
               for x,y,z in product(range(63),repeat=3))
```

## A construction over any finite field containing a primitive pth root

On the additive group $`A=\mathbb F_q^p`$ use basis $`e_i`$ indexed by $`i\in\mathbb F_p`$, and choose $`\zeta\in\mathbb F_q^\times`$ of order $`p`$. Define $`Xe_i=e_{i+1}`$, $`Ye_i=\zeta^i e_i`$, $`Z=\zeta I`$ and $`Je_i=e_{-i}`$. The group $`B=\langle X,Y\rangle`$ has normal forms $`Z^cX^aY^b`$, with $`a,b,c\in\mathbb F_p`$: $`YX=ZXY`$, and inspecting the shift, diagonal ratios and scalar distinguishes them. The center is $`\langle Z\rangle`$, and $`B/\langle Z\rangle\cong C_p^2`$. Conjugation by $`J`$ inverts $`X,Y`$ and fixes $`Z`$, so its fixed subgroup in $`B`$ is $`\langle Z\rangle`$. Its inverted elements are exactly

$$
 S_x=Z^{ab/2}X^aY^b\qquad (x=(a,b)\in\mathbb F_p^2).
$$

This follows by comparing $`Z^cX^{-a}Y^{-b}`$ with $`Z^{ab-c}X^{-a}Y^{-b}`$. In particular they represent each coset of the center once and generate $`B`$, since $`X,Y`$ occur. Write $`A^+,A^-`$ for the fixed and negated spaces of $`J`$, of dimensions $`(p+1)/2,(p-1)/2`$. The field characteristic is odd, so they are complementary.

In $`G=A\rtimes B`$ use $`(a,b)(a',b')=(a+ba',bb')`$. Let $`\alpha(a,b)=(Ja,JbJ)`$, $`H_0=C_G(\alpha)=A^+\rtimes\langle Z\rangle`$, $`K=\{g\in G:\alpha(g)=g^{-1}\}`$. For $`v\in A^-`$ put $`H_v=vH_0(-v)`$, regarding vectors as group elements. We distinguish $`v=0`$ from *any* $`v\ne0`$.

**Odd polar lemma.** The set $`K`$ acts sharply transitively on $`G/H_0`$, and hence on the equivariantly isomorphic $`G/H_v`$ by $`gH_v\mapsto gvH_0`$. Indeed any $`g`$ has a unique polar factorization $`g=kh`$, $`k\in K,h\in H_0`$: $`k`$ is the unique square root of $`g\alpha(g)^{-1}`$, and then $`h=k^{-1}g`$ is fixed. In a finite group of odd order, the square root of any element is its fixed power $`(|G|+1)/2`$; this justifies uniqueness even without commutativity. The set $`K`$ is closed under inverse and $`rsr`$. If two marks $`r,s`$ carry $`kH_0`$ to the same point, $`krkH_0=kskH_0`$, so $`r=s`$ by the unique polar decomposition. Cardinality gives transitivity between any two points. Choosing $`H_v`$ as identity/basepoint and $`K`$ as rows therefore defines a loop $`Q_v`$: its points are labeled uniquely by $`rH_v`$ for $`r\in K`$, and $`(rH_v)*(sH_v)=rsH_v`$. Its genuine left translations are the actions of the rows. The sandwich $`rsr\in K`$ takes the identity to $`r*(s*r)`$, giving the left Bol identity. The equivariant bijection of coset spaces relabels columns and entries by the same map and rows by the marks' old-basepoint labels, yielding a loop isotope. No faithfulness assumption is needed here.

The loop order is $`[G:H_v]=p^2 q^{(p-1)/2}`$. The group homomorphism $`G\to B/\langle Z\rangle`$ kills $`H_v`$; it gives a loop epimorphism $`Q_v\to C_p^2`$ by the actual product rule. Marks over the identity coset must project to the unique inverted element over it, namely $`1`$, and hence are exactly the pure vectors in $`A^-`$. Since products of such vectors stay in $`A^-`$, the kernel is the additive group $`A^-`$. This proves the normality, extension and solvability assertions.

## Why an order-p² subloop would force a stable group complement

Suppose $`P\le Q_v`$ is a subloop of order $`p^2`$. Its intersection with the elementary abelian kernel is trivial: it is an $`\ell`$-subgroup, and within $`P`$ all nonempty fibers have its size by the bijection of left translation. Thus the projection $`P\to B/\langle Z\rangle`$ is an isomorphism. Let $`D\le G`$ be generated by the *actual* marks $`k`$ of the points of $`P`$. Each such mark sends $`P`$ onto itself, by finiteness and closure of $`P`$, hence all of $`D`$ preserves $`P`$; and $`D`$'s orbit of $`H_v`$ is $`P`$. The projection of $`D`$ onto $`B`$ includes every $`S_x`$, since $`P`$ has a point over every $`x`$. Consequently it is onto $`B`$, not just onto its abelianization. Since all its generators are $`\alpha`$-inverted, $`D`$ is $`\alpha`$-stable.

Now $`D\cap A`$ is $`B`$-invariant as an **additive subgroup**, because $`D`$ surjects onto $`B`$ and conjugation of $`A`$ ignores the vector coordinate. It acts trivially on the quotient $`C_p^2`$, hence fixes each point of $`P`$ (the projection on $`P`$ is bijective). In particular $`D\cap A\subseteq H_v\cap A=A^+`$. There is no nonzero $`B`$-invariant additive subgroup in $`A^+`$. In fact for any $`a`$ in one, $`a,Xa,Ya`$ are fixed by $`J`$, implying $`Xa=X^{-1}a`$ and $`Ya=Y^{-1}a`$. Since $`X,Y`$ have odd order, they fix $`a`$; hence their commutator $`Z`$ fixes $`a`$, impossible for nonzero $`a`$. This is valid even for non-prime fields: no unjustified $`\mathbb F_q`$-linearity of $`D\cap A`$ is being used. It follows that $`D\cong B`$ and is a Sylow $`p`$-subgroup of $`G`$.

All such group Sylows are $`B^w=wB(-w)`$ with $`w\in A`$, by ordinary Sylow conjugacy and $`G=AB`$. These representations are distinct: a vector normalizing $`B`$ centralizes it, and $`C_A(B)=0`$ since $`Z=\zeta I`$. Therefore $`\alpha`$ stabilizes $`B^w`$ exactly when $`Jw=w`$, i.e. $`w\in A^+`$. This separates stable from all complements; it is not a coprime splitting assertion about the unknown loop.

## Why the stabilizer excludes this subgroup

For $`w\in A^+`$, the possible projections of $`B^w\cap H_v`$ lie in $`\langle Z\rangle`$. The unique element of $`B^w`$ above $`Z^d`$ has vector $`(1-\zeta^d)w\in A^+`$. Above the same central element the vectors of $`H_v`$ are exactly $`A^++(1-\zeta^d)v`$. For $`v\ne0`$ these are disjoint when $`d\ne0`$, since $`v\in A^-`$ and the scalar is nonzero; when $`d=0`$ the group complement contains only the zero vector above 1. Thus $`B^w\cap H_v=1`$, and the orbit of $`H_v`$ under $`D=B^w`$ has $`p^3`$ points. This contradicts its being $`P`$, of size $`p^2`$. More generally any $`p`$-power order subloop injects into $`C_p^2`$ by the kernel argument, so a nontrivial one has order $`p`$ and is cyclic (its injective image is a subgroup of $`C_p^2`$).

For $`v=0`$ the intersection has order $`p`$ for every $`w\in A^+`$. Its orbit has $`p^2`$ points. Indeed $`K\cap B^w`$ consists of the $`p^2`$ conjugates by $`w`$ of the $`S_x`$ since $`w`$ is $`\alpha`$-fixed. All are distinct as translations of the identity, so these are exactly the marks of the orbit. They generate $`B^w`$, and their products act inside the orbit. Finiteness gives all divisions there, making it a subloop of order $`p^2`$. Conversely any such subloop gives one of these $`B^w`$ by the preceding stable-complement argument and is its full orbit. Distinct $`w\in A^+`$ have distinct marked generating subgroups and hence distinct subloops. This proves the count and the theorem.

**Order spectrum (optional).** In both basepoints, powers of a mark are its ordinary powers in $`G`$, since $`K`$ contains them all. For $`x\ne0`$, $`S_x`$ has order $`p`$ (the central correction in its $`p`$th power contains $`p(p-1)/2`$). Its fixed line in $`A`$ is contained in $`A^+`$. For a nontrivial diagonal $`S_x`$ that line is $`\mathbb F_q e_0`$; otherwise the shift is a $`p`$-cycle, so a fixed vector is determined by its zeroth entry and exists since $`S_x^p=1`$. The line is $`J`$-stable as $`JS_xJ=S_x^{-1}`$; $`J`$ preserves the zeroth entry, so fixes it pointwise. For any mark $`k`$ over $`S_x`$, $`k^p\in A^-`$ since it is inverted; it also centralizes $`k`$, so lies in the fixed line of $`S_x`$, hence vanishes. Thus every nonkernel element has order $`p`$. Every nonzero kernel element has order $`\ell`$. In particular missing a full Sylow does not mean missing its prime-order elements: in the tilted example there are $`(p+1)q^{(p-1)/2}`$ distinct cyclic $`p`$-subloops.

## Recovering the displayed table from the group construction

For $`p=3`$ and $`q=7`$, use $`\zeta=2`$, $`v=e_1-e_{-1}`$, and the two basepoints with stabilizers $`H_{ev}`$ for $`e=0,1`$; in this paragraph abbreviate them to $`H_e`$. To compare to the scalar formula, put $`S_x=Z^{x_1x_2/2}X^{x_1}Y^{x_2}`$ (index arithmetic in $`\mathbb F_3`$). Then $`S_xS_y=2^{w/2}S_{x+y}`$, $`JS_xJ=S_{-x}`$. The explicit labels are $`k_{x,h}=(S_{x/2}(hv),S_x)\in K`$. Indeed the inverted elements of $`B`$ are precisely $`S_x`$, and the negative space of $`S_xJ=S_{x/2}JS_{-x/2}`$ is $`S_{x/2}Fv`$. For $`d(u)=(u_1-u_{-1})/2`$, $`d(S_t v)=s(t)`$ by the nine substitutions. Writing $`z=x+y`$, the product representative is specified by

$$
 d(S_{-z}S_{z/2}v)r=d(S_{-z}S_{x/2}v)h+d(S_{-z}S_xS_{y/2}v)t+(2^{w/2}-1)e .
$$

Indeed $`k_{z,r}^{-1}k_{x,h}k_{y,t}`$ lies over $`Z^{w/2}`$, with vector in $`A^++(1-2^{w/2})ev`$ exactly when it belongs to $`H_e`$. Using the Weyl product above and $`1/2=-1`$ in $`\mathbb F_3`$ yields the stated formula. The coset program constructs all $`9,261`$ elements, both transversals, and all $`7,938`$ products before comparing labels.

## What the examples settle

For the singleton set of primes containing $`p`$, the group quotient has order $`p^2`$ while the native loop has no such subloop. For a prescribed prime set containing one odd prime and omitting another, the same construction gives a counterexample to universal Hall existence for that set. It does not eliminate every kind of Hall subloop in a single example: its normal additive kernel is one. These loops are solvable and not simple. No historical-priority or minimum-order claim is made. Taking opposite multiplication gives the right Bol version without changing which subsets are subloops.

The [reproducibility guide](REPRODUCE.md) links the canonical [order-63 multiplication table](evidence/order-63-no-sylow.csv), five programs and separate audit records. One independent implementation reconstructs all 3,969 native products from permutations of 63 affine planes, recovering the exact table and testing all 250,047 left Bol triples. A different independent test covers the arbitrary-prime construction, including a non-prime field where an additive subgroup need not be linear over that field. Finite tests help check the concrete construction; the proof above supplies the universal quantifiers.

**Reference and acknowledgment.** T. Foguel, M. K. Kinyon and J. D. Phillips, [*On twisted subgroups and Bol loops of odd order*](https://doi.org/10.1216/rmjm/1181069494), Rocky Mountain Journal of Mathematics 36 (2006), 183–212; [arXiv v2](https://arxiv.org/pdf/math/0208231v2), introduction, Definition 4.15, Theorem 4.18 and Problem 6.10 on p. 16. Mira Cult directed the research; OpenAI models assisted with construction, exposition and independent mathematical review. The [order-63 review](reviews/order-63.txt) and [all-prime review](reviews/every-odd-prime.txt) are separate, revision-specific AI audits. Exact model versions were not verified. No human refereeing or proof-assistant certification is claimed.
