# 0102. Recovering a simple Bol loop across a characteristic elementary layer

**Mira Cult**

Let $`Q`$ be a finite simple proper left Bol loop, and let $`G`$ be its faithful left multiplication group. A normal subgroup of $`G`$ gives blocks in its action on the elements of $`Q`$, but these blocks need not be the elements of a quotient **loop**. There is a second difficulty: two lifted subgroups may have the same image in the quotient and the same intersection with the kernel, while their product picks up extra elements of the kernel. A classification by extensions has to distinguish those lifts.

**Theorem.** If the solvable radical of $`G`$ is nontrivial, choose the least prime $`p`$ with nontrivial normal $`p`$-core, and take $`V=\Omega_1(Z(O_p(G)))`$. This choice is intrinsic to the loop. Its quotient $`Y=G/V`$, a module over the formal extension $`X=Y\rtimes C_2`$, and the finite cochain tests (1)–(11) below recognize exactly the possible canonical folders. The orbits in (12) are in bijection with their ordinary **loop-isomorphism classes**: no marking of $`V`$ is required. The tests see every actual normal subgroup, including those not preserved by inversion. Although general subgroups mapping onto the quotient may be nonnormal, invariance of the actual marks makes normal subgroups sufficient to test generation. They do not require an irreducible module, a faithful quotient action, a split group extension, or a whole-group subgroup lattice.

The strict order comparisons are $`|Y|<|G|`$ and $`|X|<|G\rtimes C_2|`$. When $`|V|=2`$, the auxiliary $`X`$ can have the same order as $`G`$. The theorem is not a structural list of the admissible quotient groups and modules, a reduction to a smaller simple loop, or an efficient enumeration algorithm. It does not address groups with trivial solvable radical.

We use the [canonical faithful left folder and normal-subloop criterion](../sources/foundations/C0001.md), the [canonical inversion, Theorem 1.1(1)](../sources/foundations/C0007.md), and the finite-simple-Moufang result identified below. In this convention $`H`$ is the identity-point stabilizer, $`K`$ the set of genuine left translations and $`t`$ the formal involution which inverts the translations. The outside involutions in $`tK`$ are called *marks*. In odd characteristic this description specializes to the [older odd-kernel orbit and lifting result](0098-odd-kernel-stabilizer-orbits.md); in characteristic two the individual marks can have more than one phase.
## Lower data and the genuine mark fibers

Choose a finite $`Y\ne1`$, an automorphism $`\theta^2=1`$ (possibly the identity), $`X=Y\rtimes\langle t\rangle`$ with a **formal** involution even for trivial action, and a nonzero finite $`\mathbf F_p X`$-module $`V`$. Choose $`J\le Y`$, a $`J`$-submodule $`W\le V`$, and an $`X`$-invariant set $`P`$ of outside involutions containing $`t`$. For each $`a\in P`$ let

```math
D_a=(1-a)V,\qquad Z_a=\ker(1+a),\qquad E_a=Z_a/D_a .
```

Choose a nonempty subset $`B_a\subset E_a`$ containing zero, choose lifts $`\widetilde i\in Z_a`$ of its elements, with $`\widetilde0=0`$, and introduce a variable $`u_a\in V`$, $`u_t=0`$. A change in any chosen phase representative has no effect. In odd characteristic $`E_a=0`$, so $`B_a=\{0\}`$; in characteristic two distinct shapes and their actual offsets matter.

Let $`f:X^2\longrightarrow V`$ be a normalized 2-cocycle with $`f(t,t)=0`$, and $`s:J\longrightarrow V/W`$ a normalized map satisfying

```math
s(jj')=s(j)+j s(j')+f(j,j')\pmod W .
```

Use coordinates $`(v,x)(w,y)=(v+xw+f(x,y),xy)`$ only to specify the construction/proof; the tests below do not enumerate the extension. Write $`G`$ for the preimage of $`Y`$, $`\widehat t=(0,t)`$, $`H=\{(v,j):v\bmod W=s(j)\}`$. Above $`a`$ take the actual marked vector set

```math
S_a=u_a+\bigcup_{i\in B_a}(\widetilde i+D_a),\qquad
 (1+a)u_a+f(a,a)=0.                                                     \tag{1}
```

Its marked elements form $`\Lambda`$; set $`K=\widehat t\Lambda`$. For $`x\in X,\ b=xax^{-1}`$, require

```math
x u_a+f(x,a)-f(b,x)-u_b+xB_a=B_b\quad\text{in }E_b .                  \tag{2}
```

Indeed (1) ensures involutions; the entire solution fiber is a translate of $`Z_a`$; conjugation by $`V`$ adds $`D_a`$. Conjugation by a lift of $`x`$ gives (2) by comparing the products on its two sides. Thus (1),(2) parametrize precisely all actual invariant mark sets containing $`\widehat t`$. For a fixed pair of shapes the translations carrying one onto the other are empty or a coset of the additive period subspace, so (2) is an affine condition. The identified full fiber, not a particular anchor, is meaningful.

For $`a,b\in P,\ i\in B_a,\ k\in B_b`$ put $`z=ab`$ and

```math
A_{a,b;i,k}=u_a+\widetilde i+a(u_b+\widetilde k)+f(a,b),\qquad
 F_{a,b}=D_a+D_b .
```

The product of these two actual phase sheets over $`z`$ has exactly the vectors $`A_{a,b;i,k}+F_{a,b}`$: adding $`aD_b`$ instead of $`D_b`$ gives the same sum since $`(a-1)V\subseteq D_a`$. In particular these full formulas persist for $`a=b`$, in characteristic two and for genuinely nonsplit extensions. Demand

```math
\sum_{a\in P}|D_a||B_a|=[Y:J][V:W],\qquad
 \big(A_{a,b;i,k}+F_{a,b}\big)\cap(\widetilde s(z)+W)
 \ \begin{cases}
 =\varnothing & z\in J\setminus\{1\},\\
 \subseteq\{0\} & z=1 .
 \end{cases}                                                           \tag{3}
```

There is no restriction from (3) for $`z\notin J`$. The tildes denote any lifts. Invariance, (3) and $`K^{-1}K=\Lambda^2`$ give a sharp transversal to every stabilizer conjugate. Also $`K`$ is inverse- and sandwich-closed: writing $`a=\widehat t k,b=\widehat t l`$, the conjugate $`aba=\widehat t(kl^{-1}k)`$ is marked, and conjugation by $`\widehat t`$ gives inverses. Standard folder construction gives the left Bol operation on $`G/H`$, with $`k\in K`$ acting as its left translation. Core-freeness and generation still have to be imposed.

## Do the marks generate the whole original group?

First require $`\langle tP\rangle=Y`$, and put $`\sigma=t|_V`$. For each **proper $`Y`$-submodule** $`U<V`$, rule out a normalized $`\gamma:Y\to V/U`$ satisfying

```math
\gamma(y y')=\gamma(y)+y\gamma(y')+f(y,y')\pmod U,                    \tag{4}
```

together with, for all $`a,i`$,

```math
\sigma D_a\subseteq U,\qquad
 \sigma(u_a+\widetilde i)+f(t,a)=\gamma(ta)\pmod U .                  \tag{5}
```

This is necessary and sufficient: any proper subgroup containing $`K`$ surjects on $`Y`$, so its kernel on $`V`$ is $`Y`$-invariant, and it is exactly a section graph modulo that kernel. Conversely (4) gives such a subgroup and (5) includes every physical element of $`K`$ in it. 

There is a shorter equivalent filter once the invariance (2) has been imposed. Write $`L=\langle K\rangle`$. Since $`\widehat t\in\Lambda`$ and all marks are involutions,

```math
K=\widehat t\Lambda\subseteq\Lambda^2=K^{-1}K\subseteq L,
       \qquad L=\langle\Lambda^2\rangle\lhd G .
```

Indeed $`\Lambda^2`$ is conjugation-invariant under the whole extension. If $`\langle tP\rangle=Y`$ but $`L<G`$, then $`L`$ itself is a proper **normal** surjection onto $`Y`$. Conversely any proper normal section graph containing $`K`$ prevents generation. Hence one may restrict (4)–(5) to the normal graphs from (6) with $`D=Y,\ U<V`$, including the condition that $`Y`$ acts trivially on $`V/U`$. An arbitrary list of proper surjections can include nonnormal subgroups and is still a correct but redundant filter. Without invariance it is not generally safe to discard them. When $`Y`$ acts ineffectively the generation test need not hold merely because the projected marks generate.

## All actual normal cuts, without an original-group subgroup-lattice oracle

Enumerate $`Y`$-submodules $`U\le V`$ and $`D\lhd Y`$ such that $`D`$ acts trivially on $`V/U`$. For each pair enumerate the normalized cochains $`\eta:D\to V/U`$ satisfying the section equation (4) restricted to $`D`$ and the additional equations

```math
\eta(y d y^{-1})=y\eta(d)+f(y,d)-f(y d y^{-1},y)\pmod U
 \qquad(y\in Y,\ d\in D).                                               \tag{6}
```

These triples are bijective with **all** $`N\lhd G`$, not just inversion-invariant normals:

```math
N=N_{U,D,\eta}=\{(v,d): d\in D,\ v\bmod U=\eta(d)\}.
```

Necessity: take $`U=N\cap V`$, $`D=\pi N`$; $`[V,N]\le U`$; (4) is multiplication and (6) compares $`(0,y)(v,d)`$ to $`(v',ydy^{-1})(0,y)`$. Conversely (4) gives a subgroup, trivial action modulo $`U`$ makes it normal under $`V`$, and (6) under all $`(0,y)`$. The parameters are recovered uniquely from the graph. In particular the lower tests distinguish different normal lifts with identical intersection and projection.

**Faithfulness.** For every graph with $`|U||D|>1`$, reject if

```math
U\subseteq W,\quad D\subseteq J,\quad \widetilde\eta(d)-\widetilde s(d)\in W
 \quad(d\in D).                                                        \tag{7}
```

This is exactly $`N\le H`$, hence precisely the obstruction to core-freeness.

**Simplicity.** For every graph with $`1<|U||D|<|V||Y|`$, require the following strict witness. Select $`a,b,i,k`$ as in (3) and $`j\in J,d\in D`$ with $`z=ab=jd`$. Form the intersection of the two affine subspaces

```math
I=(A_{a,b;i,k}+F_{a,b})\ \cap\
 \big(\widetilde s(j)+j\widetilde\eta(d)+f(j,d)+W+U\big).              \tag{8}
```

It must be nonempty and, if $`z\in D`$, **not wholly contained** in $`\widetilde\eta(z)+U`$. Compute the latter by comparing one solution and the direction $`F_{a,b}\cap(W+U)`$ to that coset. All calculations for each fixed set of indices are affine over $`\mathbf F_p`$. The quantifiers over admissible cochains and over labels matter: this is a finite Boolean combination/projection of affine tests, not necessarily the single monolith-complement arrangement. In particular $`HN\cap V`$ need not equal $`W+U`$; summing over every $`j,d`$ is essential. The checks do not require $`\sigma U=U`$ or $`\theta D=D`$.

To prove equivalence, the second affine space in (8) is precisely the set of vectors of actual products of elements of $`H`$ over $`j`$ and $`N`$ over $`d`$; $`jU=U`$. Running through all choices, (8) therefore says precisely $`\Lambda^2\cap(HN\setminus N)\ne\varnothing`$. The projection $`KN/N\to G/HN`$ hits every block, and two of its distinct elements map to the same block precisely when their quotient lies in $`HN\setminus N`$. Thus the test is $`|KN/N|>[G:HN]`$. In a generated core-free folder, failure with $`1<N<G`$ cannot have $`HN=H`$ (core-freeness), nor $`HN=G`$ (then equality would imply $`K\subseteq N`$). In the remaining case equality makes $`K N/N`$ a transversal to $`H N/N`$ and every conjugate by invariance of $`\Lambda^2`$; the projection onto that nontrivial smaller coset loop is a loop homomorphism, contradicting simplicity. Conversely a proper loop congruence induces on $`G`$ the kernel of its action on the quotient loop; this kernel is nontrivial (contains the translations of the nontrivial identity class), is proper, and its orbits are all the congruence classes. The image of $`K`$ contains exactly the distinct left translations of the quotient, one for each class. This cuts with equality. This is the [strict normal-cut argument](../sources/foundations/C0001.md), not a claim that every block quotient is a loop.

## Remove the layer marking canonically

For any radical-positive finite $`G`$ a nontrivial abelian characteristic subgroup in its solvable radical (last nonzero derived subgroup) supplies some nontrivial $`O_p(G)`$. Conversely a nonzero $`O_p(G)`$ lies in the radical. Let $`p`$ be the **least** prime with $`O_p(G)\ne1`$, and choose

```math
V=\Omega_1\!\left(Z(O_p(G))\right).                \tag{9}
```

Here $`\Omega_1`$ in an abelian $`p`$-group is the subgroup of elements killed by $`p`$. It is nonzero, elementary, characteristic in $`G`$, and hence inversion-stable. It is proper in every nonassociative canonical example: if $`G=V`$ is abelian, its faithful transitive action is regular and the loop is the group $`G`$. The chosen $`p,V`$ are carried to one another by every loop isomorphism, since it conjugates the faithful left groups.

We now test (9) without assembling $`G`$. With $`P_0=O_p(Y)`$, the preimage of $`P_0`$ is a normal $`p`$-group and contains every normal $`p`$-subgroup; hence it is exactly $`O_p(G)`$. Require $`P_0`$ to act trivially on $`V`$. For each nonidentity $`d\in Z(P_0)`$ of order $`p`$, prohibit the *simultaneous* conditions

```math
f(d,y)=f(y,d)\quad(y\in P_0),\qquad
                \sum_{i=1}^{p-1} f(d^i,d)=0.                          \tag{10}
```

Under the trivial-action condition every lift of $`d`$ then commutes with all of $`O_p(G)`$ exactly when its commutator equations in (10) hold, because the vector lift coordinate cancels. Its $`p`$-th power is the displayed sum, again independent of the lift. Every extra central order-$`p`$ element outside $`V`$ would project to one of these $`d`$. Conversely $`V=\Omega_1(Z(O_p(G)))`$ implies $`V`$ is central in $`O_p(G)`$ and no such extra element exists. This proves the equivalence, also at $`p=2`$, where merely using the center or assuming an exponent-two whole preimage would be wrong.

Finally, for every prime $`\ell\ne p`$, projection induces

```math
O_\ell(G)\ \simeq\ O_\ell(Y)\cap\ker(Y\to\operatorname{GL}(V)).      \tag{11}
```

The original $`\ell`$-core intersects $`V`$ trivially, centralizes $`V`$, and projects to the right side. Conversely the preimage of the right side has $`V`$ central and normal Hall, hence is a direct product of $`V`$ and its $`\ell`$-complement by Schur--Zassenhaus; all such complements are conjugate (the normal Hall subgroup is abelian) and actually equal. The unique Sylow $`\ell`$-subgroup is characteristic in this preimage, normal in $`G`$, and maps onto the right side. Thus the least-prime requirement says exactly that the right side of (11) is trivial for all primes $`\ell<p`$. There is no need to declare that all coprime quotient normal subgroups survive a nonsplit lift.

## Isomorphisms and precise scope

Every actual canonical loop supplies the above coordinates: take the [inversion of its genuine left translations](../sources/foundations/C0007.md) from the trivial left nucleus, form the formal semidirect product, and choose a normalized section fixing its formal involution. Its invariant mark fibers have shape (1); all other equations have just been proved necessary. Conversely (1)--(8) yield a simple faithful generated left Bol folder with $`1<V<G`$. It cannot be an associative simple loop, since then its left group would be a simple group. Nor can it be Moufang: in a Moufang loop the Moufang identity gives $`R_x L_y R_x^{-1}=L_x^{-1}L_{xy}`$, so the left group is normal in the full multiplication group. For a finite nonassociative simple Moufang loop the latter group is simple by the Paige classification and multiplication-group theorem of [Nagy and Vojtěchovský, Corollaries 4.7 and 6.8](https://arxiv.org/pdf/math/0701707); the nontrivial left group would therefore also be simple, contradicting $`1<V<G`$. This is the specific source dependency for properness.

The canonical inversion on a generated folder is unique. Two marked data therefore give isomorphic loops preserving the chosen layer precisely when there are a quotient isomorphism $`\beta:X\to X'`$ respecting $`Y,t,J,P`$, an intertwiner $`A:V\to V'`$ carrying $`W`$ onto $`W'`$, and a cochain $`r:X\to V'`$, $`r(1)=r(t)=0`$, with

```math
A f(x,y)+r(xy)=r(x)+\beta(x)r(y)+f'(\beta x,\beta y),\qquad
 A s(j)+r(j)=s'(\beta j)\pmod {W'},\qquad
 A S_a+r(a)=S'_{\beta a}.                                             \tag{12}
```

The last equality is of the actual unions of phase cosets, so shifts of their anchors and duplicate shape representatives have already been removed. Indeed $`(v,x)\mapsto(Av+r(x),\beta x)`$ is then exactly an extension isomorphism matching the physical stabilizer, involution and marked sets; conversely any such isomorphism has precisely that form. Canonical-folder uniqueness proves both directions for the loop. With (9)--(11) the word “preserving” is automatic. Thus (1)--(12) give a full orbit description on quotient groups of smaller order and module cochains for the radical-positive branch, though assigning structural types to its possible quotient groups and all feasible shapes remains open. If a chosen noncharacteristic elementary layer is used instead, only the marked statement follows. No reduction to a *smaller simple loop* is asserted.

## Boundary examples and finite checks

The extra normal-cut test in (8) matters even in a small group. In $`Q_8\times C_2`$, let $`i,j`$ be quaternion generators, $`e`$ the nontrivial element of the last factor, and $`V=Z(Q_8\times C_2)`$. The subgroups $`\langle i\rangle`$ and $`\langle i e\rangle`$ have the same quotient projection and the same intersection $`\langle i^2\rangle`$ with $`V`$. Yet their product contains $`e`$: its intersection with $`V`$ has order four, not two. The automorphism interchanging $`i,j`$ need not preserve either subgroup. The four proper subgroups of $`S_4`$ mapping onto $`S_4/V_4\simeq S_3`$ are point stabilizers, none normal. A noninvariant set of two transpositions generates one of them; an invariant marked set cannot. This explains why nonnormal section graphs in (4) provide a valid test, but are redundant once (2) holds.

The [direct finite checker](../sources/code/verify_canonical_abelian_descent.py) constructs small subgroup lattices and compares the cochain tests with actual group multiplication. Eight fixtures include nonsplit groups of order 27 and reducible or ineffective actions. Among 1,635 normal-cut comparisons it finds 192 where the actual vertical intersection is larger than $`W+U`$. The [independent controls](../sources/code/check_dd7_radical_hostile.py) cover the two examples just given and two different choices of phase anchors which give exactly the same marked set. The separate [generation check](../sources/code/verify_invariant_mark_generation.py) compares actual generation and normal closure for 104 invariant masks and the contrasting noninvariant example. None of the fixtures are asserted to be new simple loops.

The remaining structural question is to identify the quotients, module actions and subsets of phase fibers for which these equations have solutions. The [evidence record](../normal-layer-evidence.md) gives the exact mathematical review, source revision and replay commands.
