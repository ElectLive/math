# A rectangular incidence moment confines odd-prime coordinate actions to four homogeneous simple types

**Rectangular reduction.** Let the faithful canonical left multiplication group $`G`$ of a finite simple proper left Bol loop have entire socle $`S=T^\Omega`$, with $`T`$ nonabelian simple and $`n=|\Omega|\ge2`$. Suppose its permutation group $`C`$ on the factors is nilpotent and transitive. If $`C`$ is **not** a 2-group, then one of the following pairs is necessary:

| Ambient simple group | Simple socle of the local normalizer |
|---|---|
| $`A_6`$ | $`A_5`$ |
| $`M_{12}`$ | $`M_{11}`$ |
| $`\operatorname{Sp}_4(q)`$ for $`q=2^f\ge4`$ | $`\operatorname{PSL}_2(q^2)`$ |
| $`\operatorname{P}\Omega_8^+(q)`$ | $`\Omega_7(q)`$ |

In the last row the simple group is understood projectively and is $`\operatorname{Sp}_6(q)`$ in even characteristic. Moreover, if $`1<U=\pi_i(H\cap S)<T`$ is an actual local stabilizer projection in any coordinate frame, its inner normalizer $`N_T(U)`$ is almost simple with socle $`R`$, and

```math
R\le U\le N_T(U)\le\operatorname{Aut}(R).
```

These are necessary conditions, **not** examples of proper simple loops. In every other simple type the coordinate group must be a 2-group and $`n`$ a power of two. A 2-group is not excluded by this theorem. No assumption on the outer automorphism group, the outer kernel, regularity or surjectivity of $`H`$ onto $`G/S`$ is made.

The key new operation is to test a **rectangular** block of the original marked operator against a coherent signed relation between different inner classes. Taking its ordinary trace instead would be invalid. This is inspired by comparing incidence profiles but uses neither a graph reconstruction conjecture nor the classification of almost-simple digraphs as a black box. The finite-group factorizations used at the end are explicitly identified below.

## An actual uniform map between two orbits

Use the [original canonical folder](../foundations/C0001.md) and [formal inversion](../foundations/C0007.md), with physical outside involutions $`\Lambda=tK`$ invariant under conjugation by $`G`$. By the [whole-socle projection theorem](../../manuscripts/0105-nilpotent-socle-stabilizer-projections.md), we have $`H\to C`$ and $`1<U_i=\pi_i(H\cap S)<T_i`$. Use actual transports by $`H`$ to identify the factors so that the subgroups all equal $`U`$. Let $`Z`$ be the set of all $`\operatorname{Aut}(T)`$-conjugates of $`U`$. Partition it into its inner conjugacy classes $`Y_b`$; class labels $`b`$ are called colors. Write $`0`$ for the color of $`U`$, and $`m=|Y_b|=[T:N_T(U)]>1`$. All colors have this same size; we do not give the color set an abelian group structure.

Let $`u=(U,\ldots,U)\in Z^\Omega,\ X=G u,\ X'=tX`$. Both are $`G`$-orbits, possibly equal. $`H`$ fixes $`u`$. Since $`K`$ is the actual transversal, the vectors $`\lambda u`$ for $`\lambda\in\Lambda`$ cover $`X'`$ with constant multiplicity $`k=|\Lambda|/|X|>0`$. By conjugacy invariance the same holds when starting at any point of $`X`$. Thus the physical marked sum as a map $`\mathbb C[X]\to\mathbb C[X']`$ is the rectangular all-ones operator times $`k`$, even when the two orbit sets are disjoint.

Choose **any** target color pattern $`p=(p_i)`$ that occurs in $`X'`$. Over $`p`$ and over the zero pattern in $`X`$, the actual fibers are respectively $`V_p=\prod_i Y_{p_i}`$ and $`V_0=Y_0^\Omega`$: the factors in $`S`$ independently realize all available inner conjugations. A mark maps the entire source fiber onto a single target fiber. Hence the genuine subset $`M`$ that maps $`V_0`$ onto $`V_p`$ satisfies

```math
\sum_{\lambda\in M}[\lambda:V_0\to V_p]
                                     =k\,\mathbf J_{V_p,V_0}.          \tag{1}
```

In particular $`|M|=k m^n`$. Each physical $`\lambda\in M`$ also maps $`V_p`$ onto $`V_0`$, because $`\lambda^2=1`$. This does **not** mean its arrows on the source are mutually inverse as maps from $`Y_0`$ to $`Y_{p_i}`$. One must track both color directions.

## Signed relations between colors

Put $`L=\operatorname{Aut}(T)`$ acting on the local colors and their contents. For distinct colors $`b,c`$ let $`L_{b,c}`$ fix both colors individually, and let $`L_{\{b,c\}}`$ preserve the unordered pair. Each contains the inner $`T`$, which is transitive on either separate fiber. Call the color pair **flat** if $`L_{b,c}`$ is transitive on the ordered Cartesian product $`Y_b\times Y_c`$. Equal colors are never flat since $`m>1`$ and equality is an invariant relation.

For every $`L`$-orbit of nonflat unordered color pairs there exist real matrices $`f_{b,c}:Y_b\times Y_c\to\mathbb R`$ for both orientations of every pair, normalized to squared Frobenius norm one, with zero row and column sums. They are equivariant under $`L`$ and have the following orientation sign $`\epsilon\in\{1,-1\}`$, the same throughout that unordered orbit:

```math
f_{\gamma b,\gamma c}(\gamma x,\gamma y)=f_{b,c}(x,y),\qquad
 f_{c,b}(y,x)=\epsilon\,f_{b,c}(x,y).                                \tag{2}
```

Here are all cases. On equal colors use the centered equality matrix, normalized, with sign $`+1`$. On distinct colors take the space of real $`L_{b,c}`$-invariant matrices. It has dimension at least two by nonflatness. By individual transitivity, the mean-zero subspace is nonzero and its row and column sums vanish separately. If no element interchanges the colors, transport an arbitrary normalized vector along the ordered orbit, and use the transposes along the disjoint reverse orbit with sign $`+1`$. If an element $`r`$ interchanges $`b,c`$, on the same mean-zero space the operator $`f(x,y)\mapsto f(ry,rx)`$ is an involution since $`r^2\in L_{b,c}`$. Take a real unit eigenvector of sign $`+1`$ **or** $`-1`$; transport it to the ordered orbit. Stabilizer invariance makes this independent of the transporter, and the eigenvalue gives exactly (2) on the reverse orientation. This construction does not assume that a positive-sign nonconstant kernel exists.

Suppose no $`\{0,p_i\}`$ is flat. Set $`f_i=f_{0,p_i}`$ and test (1) against the product of the matrices $`m^{-1}+z_i f_i(x_i,y_i)`$, summing both physical indices. On the uniform right side this is the constant $`k m^n=|M|`$, because each local total equals $`m`$. For a mark $`\lambda`$, summation over the source factors over cycles of its involutory coordinate permutation. A fixed site contributes $`1+z_i\sum_{x\in Y_0} f_i(x,r_i x)`$ with its actual arrow $`r_i`$. On an exchanged pair $`i,j`$, let $`r`$ be the arrow from $`j`$ to $`i`$. Since $`\lambda`$ interchanges the two full fibers, $`r`$ sends local colors $`0\to p_i,\ p_j\to0`$; the other arrow is $`r^{-1}`$. In particular $`\{0,p_i\}`$ and $`\{0,p_j\}`$ lie in the same unordered-pair orbit. By (2),

```math
f_i(x_i,r x_j)=\epsilon\, f_j(x_j,r^{-1}x_i).
```

Thus the exchanged pair contributes **exactly** $`1+\epsilon z_i z_j`$: linear terms vanish and the mixed sum is the signed squared norm one. Assign throughout each unordered orbit $`z_i=\sqrt{-1}`$ for sign $`+1`$ and $`z_i=1`$ for sign $`-1`$. Every summand having any exchange then vanishes. Since $`|M|>0`$, at least one actual mark in $`M`$ has the identity coordinate permutation.

The signed incidence test applies separately to **each** chosen pattern. If the coordinate images of $`G`$ and $`E`$ differ, every target pattern of $`X'`$ must therefore contain at least one flat pair. This conclusion holds without any abelian outer action or coherent-constant color representative, and it never projects an unavailable mark into existence. For identical source/target colors it recovers the [ordinary tuple cancellation](../../manuscripts/0106-nilpotent-transitive-even-field-psl2.md#uniformity-on-an-actual-stabilized-tuple). The [separate odd-outer color-descent proof](../../manuscripts/0107-odd-outer-nilpotent-socles.md) is **not** an input here.

## A flat pair forces a genuine homogeneous factorization inside the simple group

If any outside mark has identity permutation, $`E`$ and $`G`$ have the same coordinate image $`C`$. Canonical $`t`$ then acts on $`C`$ by an inner automorphism; it also inverts every generating original translation image, hence it induces inversion on $`C_{\rm ab}`$. Thus $`C_{\rm ab}`$ has exponent at most two. A nontrivial finite odd $`p`$-group has nontrivial abelianization, so nilpotent $`C`$ must be a 2-group. By contraposition, in the case of the theorem there must be a flat distinct pair $`0,b`$.

Take $`F=L_{0,b}`$, which is almost simple with socle $`T`$: $`T\le F\le\operatorname{Aut}(T)`$. Choose $`U'\in Y_b`$ with $`U'`$ an automorphic image of $`U`$. The two point stabilizers $`A=N_F(U),\ B=N_F(U')`$ in the cross action satisfy $`F=AB`$, since flatness is transitivity on the ordered pairs. Each has index $`m`$, because $`T`$ acts transitively on each individual class. Thus $`|A|=|B|`$, neither contains $`T`$, and every prime dividing $`|T|`$ divides both by $`|F|=|A||B|/|A\cap B|`$. This is a **full factorization** in the exact sense of Baddeley and Praeger, [*On classifying all full factorisations and multiple-factorisations of the finite almost simple groups*, Theorem 1.1](https://doi.org/10.1006/jabr.1997.7275). Their theorem gives

```math
T=(A\cap T)(B\cap T).
```

This last identity is not generally obtained merely by intersecting a product with a normal subgroup. Nor have we asserted that the outer overgroups $`A`$ and $`B`$ are isomorphic. Rather, $`A\cap T=N_T(U)`$ and $`B\cap T=N_T(U')`$ are isomorphic, since $`U,U'`$ are $`\operatorname{Aut}(T)`$-conjugate. Consequently the resulting factorization **of $`T`$** is homogeneous. Apply Giudici, Li and Xia, [*Vertex-primitive s-arc-transitive digraphs of linear groups*, Proposition 3.3, Table 1](https://arxiv.org/pdf/1710.09518#page=7), to this simple group and these proper isomorphic factors. Their conclusion gives the four displayed possibilities and $`N_T(U)`$ almost simple with socle $`R`$. Finally, $`U`$ is a nontrivial normal subgroup of $`N_T(U)`$, so it contains $`R`$. This proves the asserted strengthening for the actual projections.

The [author's controls](../code/verify_rectangular_color_incidence.py) distinguish reciprocal arrows on different fibers; test both orientations and both signs, including genuinely non-self-paired ordered orbits; exercise an actual rectangular uniform marked action; separate points/lines in the Fano plane from the genuinely flat natural/outer $`A_6`$ paired six-point actions. They are mechanisms and controls, not a classification by computation. The [local strip and class argument](homogeneous-normalizer-endpoints.md) rules out all four exceptional factorizations. Other transitive 2-group cases and the unrestricted structural classification are not resolved by these arguments.
