# 0037. A cyclic-affine obstruction and extraspecial regular tops

**Mira Cult**

## Results obtained

A group action can be transitive as an affine action even when its linear part is far from faithful. Nevertheless, a cyclic linear module imposes a strong restriction on extraspecial groups: a fixed-point-free central element forces their commutator form to have rank at most two.

We first prove this statement without any Bol-loop assumptions. We then explain its application to the exact paired-wreath models with an extraspecial regular permutation group. For rank at least two, the only surviving top has order 5⁵ and exponent 25. The application uses the structural reductions specified below; it is not an unrestricted classification of finite simple Bol loops or of groups with an extraspecial permutation quotient.

## 1. The affine obstruction

An extraspecial p-group B has center and derived group equal to a cyclic group of order p, and B/Z(B) is an elementary abelian group. Its commutator pairing on that quotient is a nondegenerate alternating form. Say that an Fₚ[B]-module M is **cyclic** if a single vector generates M under the linear B-action.

**Theorem 1.** Let p be odd, let B be extraspecial of order $`p^{2m+1}`$, and let B act transitively by affine transformations on a finite cyclic Fₚ[B]-module M. If a generator z of Z(B) acts without fixed points, then m≤1. In particular, for m≥2 there is no regular affine action of B on a cyclic Fₚ[B]-module.

The theorem assumes neither faithfulness of the linear representation nor a prescribed dimension for M. A regular action means a transitive action with trivial point stabilizers.

### 1.1. Make the central element a translation

Write the action as

```math
g:x\longmapsto \rho(g)x+\eta(g),\qquad
\eta(gh)=\eta(g)+\rho(g)\eta(h).
```

Put D=ρ(z)−1 and c=η(z). Since z is central, DM is invariant under every ρ(g). The action therefore descends to V=M/DM. This quotient remains cyclic and the affine action remains transitive. On V, z is translation by the image c̄ of c. This image is nonzero: otherwise c∈DM, so Dx=−c has a solution and z fixes x in M. Centrality also gives ρ(g)c̄=c̄ for every g.

Since B′=⟨z⟩ acts linearly as the identity on V, the linear image of B is abelian. Let R be the image of Fₚ[B] in End(V). The augmentation ideal of the group algebra of a finite p-group in characteristic p is nilpotent. Thus R is a commutative local Fₚ-algebra with residue field Fₚ; denote its maximal ideal by 𝔪 and residue map by ε.

For completeness, the nilpotence assertion follows by induction on the group order. Choose a central element of order p. The ideal it generates through z−1 has p-th power zero; modulo this ideal the group algebra is that of the smaller quotient group. Nilpotence of its augmentation ideal lifts to nilpotence of the original augmentation ideal.

Choose a cyclic vector v of V. The surjection R→V, r↦rv, is injective: if rv=0, commutativity implies that r kills every sv, and hence all of V; R is an algebra of actual operators. Identify V with R. The action now has the form

```math
g:x\longmapsto u_gx+b_g,\qquad u_g\in1+\mathfrak m.
```

We continue to write c̄ for the nonzero central translation in R. Each $`u_g`$ fixes it, and the elements $`u_g`$−1 generate 𝔪 as an ideal, so 𝔪c̄=0. Moreover 𝔪≠0: if R=Fₚ, all $`u_g`$ are 1, the affine image is a group of translations and hence abelian, contradicting that its commutator z translates nontrivially. Consequently c̄∈𝔪, since a unit annihilated by 𝔪 would force 𝔪=0.

### 1.2. Express the commutator form as a wedge

Fix the sign of the commutator form ω by comparing gh with hg. Since every commutator is a power of z and every $`u_g`$ fixes c̄,

```math
(u_g-1)b_h-(u_h-1)b_g=\omega(g,h)\bar c.
```

Transitivity gives an element g₀ sending 0 to 1, so b₀=1. Set $`a_g`$=$`u_g`$−1 and a₀=$`u_{g_0}`$−1. Taking h=g₀ gives a uniquely determined scalar $`\lambda_g`$∈Fₚ such that

```math
a_g=a_0b_g+\lambda_g\bar c.
```

Substitute this expression in the commutator identity. Since 𝔪c̄=0, multiplication of c̄ by any r∈R is multiplication by ε(r). As c̄≠0, comparison in its one-dimensional Fₚ-span gives

```math
\omega(g,h)=\lambda_g f(h)-\lambda_h f(g),
\qquad f(g)=\varepsilon(b_g).
```

Both f and λ are additive functions of g. The affine multiplication rule gives $`b_{gh}`$=$`b_g`$+$`u_g`$$`b_h`$ and hence f(gh)=f(g)+f(h). To check λ directly, use $`a_{gh}`$=$`a_g`$+$`a_h`$+$`a_g`$$`a_h`$:

```math
\begin{aligned}
a_{gh}-a_0b_{gh}
&=(a_g-a_0b_g)+(a_h-a_0b_h)+a_g(a_h-a_0b_h)\\
&=(\lambda_g+\lambda_h)\bar c,
\end{aligned}
```

because $`a_g`$∈𝔪. Both homomorphisms vanish on B′=Z(B), so descend to Fₚ-linear forms on B/Z(B). Thus ω is the wedge λ∧f, of rank at most two. Its nondegeneracy gives rank 2m, proving m≤1. In a regular action each nonidentity element is fixed-point-free, giving the final assertion. ∎

## 2. The exact Bol-loop model and its dependencies

Let P be extraspecial of order $`p^e`$, where p is odd and e=2m+1 with m≥2. Write W=P′=Z(P) additively, and let n=|P|. Define

```math
\begin{aligned}
S&=A_5^P\rtimes P,\\
F&=\{(a,b)\in P^2:ab\in P'\},\\
G&=\{(x,y)\in S^2:(\operatorname{top}(x),\operatorname{top}(y))\in F\},\\
\tau(x,y)&=(y,x).
\end{aligned}
```

Here P permutes the coordinates by its regular left action. The condition ab∈P′ is a condition in the abelianization; it does not assert b=a⁻¹ in P.

**Theorem 2, under the reduction inputs below.** There is a finite simple nonassociative left Bol loop with this exact faithful canonical group G and inversion τ if and only if p=5, m=2, and P has exponent 25. The construction in the surviving case is proper, meaning non-Moufang, and its loop order is $`5^5\cdot60^{5^5}`$.

We use the following specific inputs rather than claim to reprove their loop-theoretic content:

1. The [prime-power regular-top reduction](../advances-2026-11-16/manuscripts/radical-free-a5-prime-power-top.md) forces p∈{3,5} and supplies a cyclic e-dimensional Fₚ-module with an affine F-action. The action is regular after quotienting its kernel. For an extraspecial top that kernel has the form

```math
T_\alpha=\{(\alpha w,(1-\alpha)w):w\in W\},\qquad \alpha\in\mathbb F_p.
```

2. The same reduction supplies the converse. The linear action must factor through the first P-coordinate when p=5, and through the second when p=3. Its collision test is that every nonidentity pair (a,b) with b conjugate to a⁻¹ acts without fixed points. An admissible action and cyclic generator construct the faithful simple proper folder, with loop order $`n\cdot60^n`$.
3. The [regular-abelian cyclic-module theorem](../advances-2026-11-16/manuscripts/radical-free-a5-abelian-top.md#the-regular-cyclic-module-algebra) identifies a regular abelian affine image on a cyclic e-dimensional module with the principal-unit action of

```math
U_e(\mathbb F_p)=1+J,\qquad J=t\mathbb F_p[t]/(t^{e+1}),
```

whose linear part is multiplication on J.

These reductions depend in turn on the faithful-folder and strict normal-quotient interface, subgroup and full-strip analysis for A₅, and the simple-Moufang primitivity obstruction. Their statements and dependency records are linked in the two sources. Theorem 1 has none of these dependencies.

## 3. Exclude every higher-rank case but one

Put $`B_\alpha`$=F/$`T_\alpha`$. If α≠1/2, the commutator form of $`B_\alpha`$ is (1−2α) times that of P. Its center and derived group both equal W, and its central quotient is the same symplectic vector space as for P. Thus $`B_\alpha`$ is extraspecial of rank m. Its affine action is regular and its linear module cyclic. Theorem 1 excludes it when m≥2.

Therefore α=1/2. The kernel is the diagonal subgroup of W², and B=F/diag(W) is abelian. By input 3, B is isomorphic to $`U_e(\mathbb F_p)`$, with the specified multiplication action. We must retain the coordinate-factorization requirement from input 2; an abstract group isomorphism alone is insufficient.

An odd extraspecial group has exponent p or p². Indeed its p-th powers are central, and in a class-two group with commutators of order p,

```math
(xy)^p=x^py^p
```

because p divides p(p−1)/2. Hence the power map P/W→W is linear.

If P has exponent p, then so do F and B. But 1+t∈$`U_e(\mathbb F_p)`$ has order exceeding p whenever e≥p. Here e≥5 and p∈{3,5}, so this case is impossible.

If P has exponent p², the power map is nonzero and onto W. For (x,y)∈F, one has y^p=(x^p)⁻¹. Thus F^p is the anti-diagonal subgroup of W². Its intersection with diag(W) is trivial because p is odd. It follows that B has exponent p² and |B^p|=p. The images of either one-sided copy of W also equal B^p: each is the full one-dimensional central quotient W²/diag(W).

In the principal-unit group, Frobenius gives

```math
\left(1+\sum_{i=1}^e a_it^i\right)^p
=1+\sum_{ip\le e}a_it^{ip},\qquad
|U_e(\mathbb F_p)^p|=p^{\lfloor e/p\rfloor}.
```

Consequently p≤e≤2p−1, and B^p corresponds to 1+Fₚt^p. The kernel of multiplication on J is exactly 1+Fₚt^e: multiplication by 1+r is the identity precisely when rJ=0.

The inactive one-sided copy of W must act trivially linearly. Its image is B^p, so the lines Fₚt^p and Fₚt^e must coincide. Hence e=p. Since e=2m+1≥5 and p∈{3,5}, necessarily p=e=5 and m=2.

## 4. Construct the surviving action

Let P have order 5⁵ and exponent 25. The preceding power calculation shows that B=F/diag(W) is abelian of order 5⁵, exponent 25, with |B^5|=5. The elementary classification of finite abelian groups therefore gives

```math
B\cong C_{25}\times C_5^3\cong U_5(\mathbb F_5).
```

Choose such an isomorphism. On J=tF₅[t]/(t⁶), let $`U_5(\mathbb F_5)`$ act by

```math
u:x\longmapsto u(1+x)-1.
```

This is regular because the orbit map u↦u−1 is a bijection onto J. Its linear module is cyclic: starting from t, successive applications of multiplication by (1+t)−1 produce t²,…,t⁵. The subgroup B^5 corresponds to 1+F₅t⁵ and acts trivially linearly.

Pull back the action to F. The kernel of the first-coordinate projection F→P is the inactive second copy of W, whose image in B is B^5. Thus the linear action factors through the first P-coordinate, as required for p=5. A cyclic vector gives a quotient of the regular coordinate module F₅[P].

The affine kernel is diag(W). No nonidentity element (w,w) in this kernel is relevant to the collision test: centrality would require w=w⁻¹, impossible in an odd-order group. Every element outside the kernel acts fixed-point-freely in the regular quotient. Input 2 now supplies the faithful simple proper Bol folder and its order. This proves the converse in Theorem 2. ∎

## 5. Consequences, boundaries and further questions

The affine obstruction is a general result about group actions, not merely a calculation in one loop. Its mechanism is that cyclicity and a central translation reduce the nondegenerate commutator form to a wedge of two scalar characters.

The Bol consequence concerns exactly the displayed group G and swap τ. It does not exclude other canonical envelopes with the same composition factors or an extraspecial quotient. Nor does its existence proof count isomorphism classes in the surviving case. The [results overview](../RESULTS.md#regular-permutation-tops-in-the-a₅-construction) records subsequent reported orbit counts and distinguishes them from the proofs presently public; reproducing those counts is not a new open classification target here.

Two mathematical extensions remain beyond this argument:

- For a general odd p-group acting transitively on a cyclic module, determine which central fixed-point-free translations constrain its commutator pairings. The proof here uses both extraspeciality and the fact that quotienting by ρ(z)−1 makes the linear image commutative.
- For nonextraspecial regular tops in the paired A₅ model, classify the admissible module/cocycle data, retaining the active-coordinate condition and the actual coordinate-normalizer equivalence. An arbitrary change of module basis is not automatically a loop isomorphism.

## Sources and evidence

This exposition develops the argument in [the source manuscript](../advances-2026-11-16/manuscripts/radical-free-a5-extraspecial-tops.md). It separates the elementary affine proof from the conditional application and spells out the additive-character and inactive-coordinate steps. The source records automated mathematical checks conditional on its upstream inputs. Those records are not human referee acceptance or formal verification, and do not by themselves certify this rewritten exposition. No numerical experiment or computational classification is used in the proofs above.
