# Selected marked involutions over an elementary two-layer

**Mira Cult**

**Scoped independently reviewed manuscript-local continuation of [0323:C0010](../../claims/0010.md).** The result gives exact local-label and cross-mark collision conditions for a selected union of involution classes above an elementary abelian normal 2-subgroup. It allows even groups, nonsplit extensions, several marked classes and τ=id. It is an elementary-layer recognition interface, not a structural classification of finite simple Bol loops.

The canonical faithful folder and normal left nucleus inputs are [C0001](../../claims/0001.md), with aggregate review at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45). The direct inversion construction is [C0007, Theorem 1.1(1)](../foundations/C0007.md); the C0011 review record says reviewer `review_foundations` checked that construction and the relevant C0001 nucleus/folder inputs at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The C0007 aggregate metadata remains unreviewed. The present deduction has the independent exact-source reviews recorded below. It does not import the odd-group full-inverted-set theorem or assume a quotient loop.

## The canonical marked model is universal

Let Q be any finite simple proper left Bol loop, and let G=LMlt(Q), H be its identity stabilizer and K={L_x:x∈Q}. C0001 makes N_λ(Q) normal; simplicity and nonassociativity force N_λ(Q)=1. The canonical folder is faithful, K generates G, K contains 1, is inverse-closed and is closed under kℓk.

For completeness, the short C0007 argument constructs inversion directly on this faithful G. Suppose k₁⋯k_m has k₁⁻¹⋯k_m⁻¹=1. Then k_m⋯k₁=1, and repeated sandwich closure gives

    (k₁⋯k_m)u=k₁⋯k_m u k_m⋯k₁ ∈K for every u∈K.

At u=1 the product is some L_a∈K. For each y, L_aL_y belongs to K and sends 1 to a*y, so it equals L_{a*y}; hence a∈N_λ(Q)=1. Interchanging k_i and k_i⁻¹ gives the converse word relation. Thus k₁⋯k_m↦k₁⁻¹⋯k_m⁻¹ defines the unique automorphism τ of G inverting K, and τ²=1. This uses no descent of an automorphism through the kernel of a doubled envelope.

Use a **formal external** group E=G⋊⟨t⟩ with t²=1 inducing τ, even when τ=id. Put Λ=tK. Its elements are involutions, t∈Λ, and Λ generates E. Sandwich closure and inverse-closure of K imply that Λ is closed under conjugation by its elements; hence it is a union of E-conjugacy classes. In even order it need not contain every involution in tG. Moreover Λ²=K⁻¹K is G-conjugacy-invariant and H∩Λ²=1. All marked sets and labels below refer to this actual selected Λ, not to an assumed full outside involution set.

## Local involution-lift labels

More generally let G be a finite group, τ∈Aut(G) with τ²=1, E=G⋊⟨t⟩ the formal extension, H≤G, and Λ⊂tG an E-conjugacy-invariant set of involutions containing t. Let V◁G be an elementary abelian 2-group invariant under τ. Write L=G/V, J=HV/V, W=H∩V and π:E→E/V. For each quotient mark λ̄∈π(Λ), choose an actual marked lift λ₀∈Λ, and set

    T_λ=conj_{λ₀}|V,  Z_λ=ker(1+T_λ),  I_λ=(1−T_λ)V.       (1)

The action T_λ depends only on λ̄, because V is abelian. It satisfies T_λ²=1 and I_λ≤Z_λ. Every involutory lift of λ̄ is vλ₀ for a unique v∈Z_λ. Conjugation by V translates v through I_λ. Thus its V-orbits are the affine cosets in

    H¹(⟨λ̄⟩,V)=Z_λ/I_λ.                                   (2)

Let A_{λ̄}⊂Z_λ/I_λ be the labels of the V-orbits actually contained in Λ. These are not arbitrary: conjugation in E relates the label sets over conjugate quotient marks. No quotient-folder assertion is made. The selected mark cardinality is

    |Λ|=Σ_{λ̄∈πΛ}|A_{λ̄}|·2^{dim I_λ}.                    (3)

The formula uses the actual selected labels, and fibers can have different dimensions over different quotient marks.

If H∩Λ²=1, then for every selected mark

    W∩I_λ=0.                                               (4)

Indeed λ₀^vλ₀ runs through I_λ as v runs through V, and both factors are marked. Distinct selected labels above the same λ̄ also remain distinct in the further quotient

    (Z_λ/I_λ)/image(W∩Z_λ).                               (5)

Otherwise adjust representatives within their marked V-orbits so that their product is a nonidentity element of W, contradicting H∩Λ²=1. Because (4) embeds W∩Z_λ in Z_λ/I_λ, this gives the necessary bound

    |A_{λ̄}|≤2^{dim H¹(⟨λ̄⟩,V)−dim(W∩Z_λ)}.               (6)

These are selected-class restrictions in characteristic two; they do not assert that the label set is full, a subgroup, or a subspace.

## Exact collision conditions across marks

Let λ̄,μ̄ be **distinct** elements of πΛ with j=λ̄μ̄∈J. Choose actual marked lifts λ₀,μ₀ and h_j∈H lifting j. Set

    c=λ₀μ₀h_j⁻¹∈V.

For selected labels represented by v∈Z_λ and w∈Z_μ, all pairs of lifts in their respective V-orbits have product V-coordinates, relative to h_j, in

    c+v+T_λw+I_λ+T_λ I_μ.

Because j≠1, any product lying in the H-fiber W h_j is nonidentity. Therefore H∩Λ²=1 forces, for every such selected label pair,

    c+v+T_λw ∉ W+I_λ+T_λ I_μ.                             (7)

The condition is independent of the representatives v,w of their V-orbits. If the subspace on the right is V, the two quotient marks cannot both occur. This cross-mark condition allows different actions and different local H¹ spaces; it does not require a quotient loop or permit replacing actual marked labels by all abstract lifts.

Conversely, for a given E-conjugacy-invariant Λ, the following three requirements are **equivalent** to H∩Λ²=1:

1. (4) for every selected quotient mark;
2. the injection in (5) for the selected labels over every single quotient mark;
3. (7) for every pair of distinct selected quotient marks whose product lies in J and every pair of their selected labels.

Necessity was proved above. For sufficiency, take λ,μ∈Λ with λμ∈H. Their quotient product belongs to J. If their quotient marks differ, (7) excludes them. If the quotient marks agree but their V-orbits differ, (5) excludes them. If they lie in the same V-orbit, their product belongs to I_λ, and (4) forces that product to be 1. This checks every pair, including equal marked involutions.

## Transversality and remaining work

For a chosen Λ as above, set K=tΛ⊂G. If the three equivalent collision conditions hold and

    |Λ|=[G:H],                                              (8)

then K is a transversal to H and every G-conjugate of H: Λ²=K⁻¹K is G-conjugacy-invariant, so the collision condition gives an injection into every coset space, and (8) gives surjectivity. Because Λ is an invariant involution set containing t, K contains 1, is inverse-closed and is sandwich-closed. If in addition ⟨K⟩=G and Core_G(H)=1, the standard faithful Bol-folder interface applies. For a simple proper-loop classification one must separately enforce the exact normal-subloop and non-Moufang conditions and then identify the canonical τ; the conditions above do not imply them.

This is an exact recognition interface for **specified** selected marks. The affine centralizer-orbit parametrization below makes conjugation covariance explicit. The unresolved structural tasks include solving the cross-mark equations without enumerating arbitrary full sections, describing isomorphism orbits, and imposing generation, core-freeness and simplicity. Characteristic choices such as Ω₁(Z(O₂(G))) can fix a layer when O₂(G)≠1; groups without a nontrivial elementary normal 2-layer, including radical-free even canonical groups, remain outside this layer reduction. Nothing here asserts a bounded group height, a global complexity bound, or an exhaustive structural classification.

## Affine centralizer action on lift labels

**Continuation with the scoped independent reviews below.** This section makes the conjugation covariance of the selected label sets explicit. It applies to the same formal extension $`E=G\rtimes\langle t\rangle`$, including $`\tau=\mathrm{id}`$. Put $`Q=E/V`$, and choose a normalized section $`s:Q\to E`$. Write the action on $`V`$ as $`x\cdot v`$ and the normalized factor set additively as

```math
s(x)s(y)=c(x,y)s(xy),\qquad
 c(x,y)+c(xy,z)=x\cdot c(y,z)+c(x,yz).                    \tag{9}
```

Only involutions $`x`$ in the outside quotient coset $`tG/V`$ are considered; the formal external $`C_2`$ ensures $`x\ne1`$, even when $`\tau=\mathrm{id}`$.

Let $`T_x=x|_V`$, $`Z_x=\ker(1+T_x)`$, and $`I_x=\mathop{\mathrm{im}}\nolimits(1+T_x)`$. Associativity gives $`c(x,x)\in Z_x`$, while the square of $`v s(x)`$ is $`(1+T_x)v+c(x,x)`$. Thus $`x`$ admits an involutory lift precisely when

```math
[c(x,x)]=0\quad\text{in }Z_x/I_x=H^2(\langle x\rangle,V). \tag{10}
```

Changing the chosen section changes $`c(x,x)`$ by an element of $`I_x`$, so this obstruction is intrinsic. If it vanishes, choose $`z_x\in V`$ with $`(1+T_x)z_x=c(x,x)`$ and set $`\lambda_x=z_xs(x)`$. The $`V`$-conjugacy orbits of involutory lifts of $`x`$ form the affine space $`Z_x/I_x=H^1(\langle x\rangle,V)`$, with origin $`\lambda_x`$, as in (2).

For $`q\in Q`$, put $`x'=qxq^{-1}`$. Equation (9) gives

```math
s(q)s(x)s(q)^{-1}=b(q,x)s(x'),\qquad
 b(q,x)=c(q,x)+c(x',q).                                   \tag{11}
```

Conjugation by a lift of $`q`$ sends the label of $`(z_x+v)s(x)`$ to

```math
F_{q,x}([v])=[q\cdot v+q\cdot z_x+b(q,x)+z_{x'}]
 \in Z_{x'}/I_{x'}.                                       \tag{12}
```

The displayed vector belongs to $`Z_{x'}`$ because conjugation preserves involutions. Replacing the lift of $`q`$ by $`u s(q)`$ changes it by $`(1+T_{x'})u\in I_{x'}`$. Thus (12) is well-defined on labels, with linear part the action of $`q`$. On $`C_Q(x)`$, these maps form an affine group action: $`F_{qr,x}=F_{q,x}\circ F_{r,x}`$, because conjugations compose. Its translation part is a 1-cocycle for the centralizer action on $`Z_x/I_x`$. Changing origins or section coordinates conjugates the description by the corresponding affine coordinate change.

Choose one representative $`x`$ of each $`Q`$-conjugacy class of involutions in $`tG/V`$, and discard it when (10) fails. For each remaining $`x`$, the actual $`E`$-conjugacy classes of marked involutions over its quotient class are in bijection with the $`C_Q(x)`$-orbits on $`Z_x/I_x`$ under (12). Indeed the points are the $`V`$-orbits, and an $`E`$-conjugation preserving $`x`$ projects to its centralizer. Consequently every invariant selected union $`\Lambda`$ is specified by choosing a union of these centralizer orbits for each representative and transporting its labels by (12). This transport is independent of the chosen transporter because any two differ by a centralizer element. The condition $`t\in\Lambda`$ selects the orbit of the actual $`t`$-lift; when its quotient class is represented by $`tV`$, one may choose $`\lambda_{tV}=t`$ so its label is zero.

The obstruction (10) can exclude quotient marks, and centralizer orbit sizes restrict possible selected-fiber cardinalities. These are structural restrictions on the selected set; they do not by themselves solve the collision equations (4)–(7), establish generation or simplicity, give isomorphism orbits, or bound the global complexity of the loop. Its exact-source independent reviews are recorded below.

## Independent mathematical review

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/ced6706720b08adb94f4497534b2208f5c1a3d51), reviewers contributor 1, contributor 2 and contributor 3 independently accepted the full manuscript, conditional on the cited C0001 and scoped C0007 inversion inputs. All checked the direct inversion construction, formal external C2, selected rather than full marked set, local H¹ conditions, exact cross-mark necessity and sufficiency, cardinality/transversality interface, H² obstruction, and affine transporter and centralizer-orbit formulas. Generation, core-freeness, simplicity and global exhaustion remain separate. No computation or fresh aggregate C0007 review was claimed; these are independent model reviews, not formal certification.
