# The binary rank-three case: nonsplit extensions and actual marked collisions

**Mira Cult**

**Scope.** There is no finite simple nonassociative left Bol loop whose faithful canonical group is an extension of $`T^2`$, $`T=\mathrm{GL}_3(2)=\mathrm{SL}_3(2)`$, by the additive $`V=L\boxtimes L=\mathrm{Mat}_3(2)`$, $`L=\mathbb F_2^3`$, with $`(a,b)X=aXb^\mathsf t`$ and the canonical inversion swapping the two quotient factors in these matched coordinates. We allow an initially nonsplit extension and arbitrary actual point stabilizer. Combined with the [all-field capacity theorem](tensor-capacity.md), this completes that precise family for $`d\ge3`$, not the classification of finite simple proper left Bol loops. In particular the argument below does **not** assert $`H^1(T,L)=0`$; in fact the finite checker detects its nonzero class.

## Fibers and endpoints without a prior splitting

We use the original canonical inversion extension $`G\rtimes\langle t\rangle`$, the invariant set $`\Lambda`$ of outside marked involutions (containing $`t`$), and $`H\cap\Lambda^2=1`$. By the [single-orbit calculation](odd-field-foundation.md), the projection of $`\Lambda`$ is exactly the outside swap class, all actual mark fibers have size $`r`$, $`W=H\cap V`$ is additive, the projected $`J\le T^2`$ has $`|J|=m|T|`$, and $`m=[V:W]/r>1`$ divides $`|T|`$. The action of $`t`$ on $`V`$ is transpose by the scalar commutant argument.

Above the quotient swap, all outside involutions are $`zt`$ for symmetric $`z`$; conjugating by $`V`$ adds every alternating matrix (symmetric with zero diagonal). These two spaces have orders 64 and 8. The inverse image of the diagonal $`T`$ acts by conjugation on the eight resulting labels $`\mathrm{Sym}/\mathrm{Alt}`$. Its $`V`$-kernel acts trivially there, so it gives a genuine **affine** $`T`$-action whose linear part is ordinary congruence on the diagonal vector, that is, the natural binary action. There is no assertion that a fixed point exists. The number of selected labels divides a power of two, since $`r\mid[V:W]`$. An invariant subset of size 2 or 4 consists of fixed points: the nonabelian simple $`T`$ of order 168 cannot inject into $`S_4`$. Its affine action cannot have two fixed points because their nonzero difference would be globally fixed in $`L`$. Thus $`r=8`$ or 64.

Both endpoint projections of $`J`$ have even order because $`m`$ divides each of their orders, and one contains seven in its order. Every proper subgroup has index at least seven: its simple coset action cannot embed $`T`$ in $`S_6`$. A proper subgroup with order divisible by 14 could therefore only have order 14; its Sylow 7 would be normal. But the number of Sylow 7-subgroups of $`T`$ is eight by Sylow and simplicity, hence their normalizer has odd order 21. Thus an endpoint is full. Interchanging coordinates if needed, Goursat and $`|J|>|T|`$ give $`J=T\times P,\ |P|=m`$.

With $`r=64`$ the differences over the swap cover the symmetric space; its $`T^2`$-conjugates cover every matrix, giving $`W=0,m=8`$. With $`r=8`$, differences over any one phase still include every alternating matrix, whose orbit union contains all rank-two matrices. Pure left $`T`$ invariance forces $`W=L\otimes D`$ for a subspace $`D\le L`$ (isolate rows with matrix units). Rank two is forbidden, so $`|W|\le8`$. But $`m|W|=64,\ m\mid168`$ is a power of two, whence $`|W|=8,m=8`$. In either case conjugate coordinates simultaneously so $`P`$ is upper unitriangular; it is now a full Sylow 2-subgroup with unique invariant line $`L_0=\langle e_1\rangle`$. Write $`K=0`$ or $`L_0`$ respectively, $`M=L/K`$; then $`W=L\otimes K`$.

## A subgroup splitter detects the original extension class

Over the field $`\mathbb F_2`$, Künneth for the two finite-group bar resolutions and $`L^T=0`$ give

```math
H^2(T^2,V)=H^1(T,L)\otimes H^1(T,L).
```

On restriction to $`T\times P`$ followed by coefficient projection to $`L\boxtimes M`$, this entire source maps to the degree $`(1,1)`$ Künneth summand by $`1\otimes\phi`$, where $`\phi:H^1(T,L)\to H^1(P,M)`$ is restriction followed by reduction. This is natural already on the tensor bar complexes. Crucially, $`H/W`$ is a complement in the preimage of $`T\times P`$ modulo $`W`$, so the original extension class maps to zero.

The map $`\phi`$ is injective in **both** cases. A nonprincipal cocycle defines an affine $`T`$-action on eight vectors with no global fixed point. Every orbit of size at most six is trivial by the simple coset-action observation. With no fixed points, the only possible partition of eight is therefore a single orbit of eight. Its stabilizers have odd order 21, so $`P`$ acts freely and transitively on this affine space. If reduction to $`M`$ on $`P`$ were principal, some $`K`$-coset, of size at most two, would be invariant, a contradiction. Thus $`1\otimes\phi`$ is injective and the extension **of any candidate** splits. This does not say all such extensions split.

## A marked-square collision even for a nonprincipal stabilizer cocycle

Fix a split identification, and let $`t_0`$ implement the ordinary swap and transpose. Since $`H^1(T^2,V)=0`$ by the same Künneth calculation, the original inversion differs from this automorphism by conjugation by a vector $`v`$. Its square forces $`v=v^\mathsf t`$, since $`V^{T^2}=0`$. Thus multiplying the original outside $`t`$ by $`v`$ actually gives an outside involution implementing $`t_0`$. The split diagonal $`T`$ fixes $`t_0`$ and has just two phase orbits, 0 and the seven nonzero phases. With the allowed cardinalities, the original marks contain $`t_0^G`$ in both cases. More precisely over $`k(x)=(x,x^{-1})`$ the set $`t_0\Lambda`$ consists of $`(xZ,k(x))`$ for $`Z`$ in $`\mathcal D=\mathrm{Alt}`$ (small case) or $`\mathrm{Sym}`$ (full). Indeed the pure split conjugates give the zero vector over every projected mark, conjugation by vectors fills the image of $`1-\rho(k(x))t_0`$, and its kernel is the full set of involution lifts. On writing $`Y=xZ`$ these two spaces are $`x\,\mathrm{Alt}`$ and $`x\,\mathrm{Sym}`$. The set $`\Lambda`$ is invariant under conjugation by $`t_0`$, since it is invariant under $`G`$ and the original $`t`$. Hence $`\Lambda^2=(t_0\Lambda)^2`$; for any $`b\in P`$ of order two it contains all $`(D,(b,b))`$ with $`D\in\mathcal D+b\mathcal D`$, by multiplying the fibers at $`1`$ and $`b`$.

Now $`H/W`$ is a cocycle graph inside the split restriction. By Künneth,

```math
H^1(T\times P,L\boxtimes M)=H^1(T,L)\otimes M^P,
```

since $`L^T=0`$. The fixed space $`M^P`$ is the line of $`e_1`$ in the full case, of $`\bar e_2`$ in the small case, by upper unitriangular matrices. Therefore after one $`V`$-conjugation (preserving the marked-square test) the stabilizer cocycle on $`(a,p)`$ is $`\delta(a)\otimes m_0`$ modulo $`W`$, for an arbitrary derivation $`\delta:T\to L`$ and the indicated generator $`m_0`$. These are the actual Künneth representatives by the external product with a degree-zero invariant.

Choose $`b=1+E_{23}`$. Its order two gives $`\delta(b)=\alpha e_1+\beta e_2`$.
* If $`W=0`$, the stabilizer entry is $`\alpha E_{11}+\beta E_{21}`$. Both are in the indicated marked-square vector space: $`E_{11}\in\mathrm{Sym}`$ and $`(1+b)(E_{31}+E_{13})=E_{21}`$.
* If $`W=L\otimes L_0`$, the stabilizer vector modulo $`W`$ is $`\alpha E_{12}+\beta E_{22}`$. Here $`E_{12}+E_{21}\in\mathrm{Alt}`$, $`E_{21}\in W`$, and $`(1+b)(E_{32}+E_{23})=E_{22}\in\mathrm{Alt}+b\,\mathrm{Alt}`$.

In either case the actual stabilizer meets $`\Lambda^2`$ over the **nonidentity** $`(b,b)`$, a contradiction. No passage to a quotient-loop or normality of $`H`$ was needed.

The [exact finite control](../code/verify_binary_three_tensor_residual.py) constructs all 168 matrices and all 16 derivations (8 principal); it checks every cocycle identity, the Sylow detection on both coefficient quotients, and both concrete marked-square intersections for each derivation. A [separate independent checker](../code/check_d9c9_bar_obstruction_independent.py) tests the nonzero mixed extension class and every stabilizer cocycle in the two quotients. The exact model-review scope is given in the [theorem overview](../../manuscripts/0100-matched-tensor-radicals.md).
