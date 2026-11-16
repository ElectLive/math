# Candidate obstructions for extraspecial Bruck radicals

**The initial deductions have the scoped independent reviews below; later extensions are separately labeled.** This continues [C0010](../../claims/0010.md) and allocates no new claim ID. Assume a finite simple nonassociative exponent-2 right Bruck loop with faithful Baer envelope (G,H,K), P=O₂(G) extraspecial, Z(P)=Φ(P)=<z> of order 2, and A=G/P the product of PGL₂ factors with the Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Lemmas 4.1–4.5 hypotheses. Here τ=1, so K is G-conjugacy invariant and all k∈K are involutions. Let V=P/<z>; the commutator form b:V×V→F₂ is nondegenerate, and p²=z^{q(p<z>)} defines an A-invariant quadratic form q with polar b. Let W=H∩P. Corefreeness and z central in G give W∩<z>=1; since Φ(P)=<z> is central, this makes W elementary abelian and its image totally singular for q.

The radical section D=P∩K is z-stable. Indeed P=WD by Baumeister–Stein, Lemma 4.2. Express z=wd with w∈W and d∈D. If w≠1, nondegeneracy of b gives p∈P with [w,p]=z. Since d=zw is conjugate to w by p and K is conjugacy invariant, w∈K∩H, contrary to transversality. Thus w=1 and z=d∈D. Every d∈D outside <z> is P-conjugate to dz by nondegeneracy, so D z=D.

## A support-level necessary condition

For an arbitrary k∈K, let t=kP∈A and α be conjugation by k. If there is v∈V with b(v,tv)=1, then kz∈K. Choose p∈P lifting v and x=pα(p). Since α²=1, α(x)x⁻¹=α(p)p(α(p)⁻¹p⁻¹)=[α(p),p]=z, with commutator convention immaterial in this central order-two case. Hence k and kz are conjugate by x, and K is conjugacy invariant. Because q is t-invariant,

    q((1+t)v)=q(v)+q(tv)+b(v,tv)=b(v,tv).

Thus the condition is that (1+t)V contains a q-nonsingular vector.

Baumeister–Stein, Lemma 4.4 gives one A-conjugacy class C_J for each nonempty support set J of outer involution coordinates; Lemma 4.5 gives a positive fiber for each class. Suppose that for every nonempty J, some/every t_J∈C_J satisfies q((1+t_J)V)≠0. The preceding paragraph implies kz∈K for every k∈K outside P, and the radical argument gives the same for k∈D. Thus Kz=K. Its image in G/<z> is a full transversal to H<z>/<z>, and the folder quotient criterion [C0001, Theorem 2.2](../foundations/C0001.md) yields a loop epimorphism with nontrivial kernel. Its image has order at least [A:B]>1, so this contradicts simplicity.

Consequently any simple example with an extraspecial radical must have at least one nonempty support J such that

    q((1+t_J)V)=0  (equivalently b(v,t_J v)=0 for all v∈V).

The image (1+t_J)V is then totally singular: it consists entirely of q-zero vectors, and its polar form vanishes on it. For A=S5 this says the image of 1+t for a transposition must be totally singular. It is a necessary module condition only; it does not exclude all extraspecial radicals, assert z∉K, or construct a loop. The scoped reviews below cover this necessary condition.

## General graph-collision criterion

**Graph-collision criterion with scoped review below.** Work with a faithful Baer envelope (G,H,K) of an exponent-2 right Bruck loop; P=O₂(G) extraspecial, Z(P)=Φ(P)=<z>, V=P/<z>, and W=H∩P. Let b and q be the commutator and square forms of P. Corefreeness implies W∩<z>=1, so W is elementary abelian and identifies with a totally singular subspace U=W<z>/<z> of V. The section K is G-conjugacy-invariant and contains involutions.

Fix k∈K, let t be its induced involution on V (possibly trivial), let α be conjugation by k and define the linear space L=U∩(1+t)V. For each v∈C_V(t), a lift p∈P obeys α(p)p⁻¹=z^{ℓ_k(v)}. The map ℓ_k:C_V(t)→F₂ is linear: on such lifts α acts by central multiplication and z is fixed. It is independent of the chosen lift.

If ℓ_k≠0 and L≠0, the folder condition fails. Choose nonzero u∈L and p with (1+t)(p<z>)=u. Let r lift some fixed vector with ℓ_k=1. Then α(r)=rz, and the two commutators pα(p)⁻¹ and prα(pr)⁻¹ differ by z. Both project to u, so exactly one is the unique element of W lifting u. The corresponding conjugate of k lies in Wk, distinct from k, contradicting transversality of K for the relevant H coset. Hence any genuine section with L≠0 must have ℓ_k=0.

Assume ℓ_k=0. For u∈L, take p with (1+t)(p<z>)=u and write pα(p)⁻¹=z^{f(u)}w(u), with w(u)∈W the unique element projecting to u. This phase f is well-defined: changing p by a lift r of an element in C_V(t) leaves the commutator unchanged, since α(r)=r; changing by z also has no effect. Choose a linear section from L to V for 1+t and a coordinate section V→P given by an ordered symplectic basis. The central multiplication coordinate in P is bilinear and the central coordinate of α is quadratic (the homomorphism identity forces its polarization from those bilinear cocycles). Therefore f is a polynomial of degree at most 2 with f(0)=0. This argument uses the actual W graph; it does not assume q restricts nontrivially to L (in fact L⊂U is totally singular).

Since K contains k and all its P-conjugates, folder transversality requires f(u)=1 for every nonzero u∈L. This is impossible for dim L≥3: if u,v,w are independent, the values 1 on u,v,w and their pairwise sums force each pairwise polarization to be 1, and the quadratic identity gives f(u+v+w)=0. For dim L=2 the only permitted phase is the anisotropic form, equal to 1 on all three nonzero vectors. Thus a necessary condition for each k is

  dim(U∩(1+t)V)≤2,
  if this dimension is positive then ℓ_k=0,
  if it is 2 then the phase f is anisotropic.

This is a collision criterion, not a complete folder test; it does not exclude the anisotropic plane, assume a split extension, or assert that z∈K is incompatible with simplicity. It applies to the fixed split model below while allowing general graphs and extensions. The scoped reviews below check the handedness and affine-coordinate identities.


## Invariant singular subspace: a linear rank criterion

The following proposed criterion avoids the phase calculation when the stabilizer's shadow is invariant under the entire quotient. In the general extraspecial setting above, put $`U=WZ(P)/Z(P)`$ and suppose $`U`$ is $`A=G/P`$-invariant. Core-freeness makes $`W\cap Z(P)=1`$, so $`W`$ is elementary abelian and its full preimage $`E=WZ(P)`$ is elementary abelian, with $`W`$ of codimension 1 in $`E`$. Since $`U`$ is $`A`$-invariant and $`P`$ acts trivially on $`P/Z(P)`$, $`E\lhd G`$.

Let $`k\in K`$, let $`t=\pi(k)`$, and let $`\alpha`$ be conjugation by $`k`$ on the vector space $`E`$. If $`\mathop{\mathrm{rank}}\nolimits(1+t|_U)\ge2`$, then $`\mathop{\mathrm{im}}\nolimits(1+\alpha)`$ has dimension at least 2, because its projection onto $`U`$ is $`\mathop{\mathrm{im}}\nolimits(1+t|_U)`$. As $`W`$ has codimension 1 in $`E`$, the intersection $`\mathop{\mathrm{im}}\nolimits(1+\alpha)\cap W`$ contains a nonzero element. For a preimage $`p\in E`$, the elements $`k`$ and its $`P`$-conjugate differ by this element of $`W\le H`$; both lie in the conjugacy-invariant section $`K`$, contradicting transversality. Therefore every section element must satisfy


```math
\mathop{\mathrm{rank}}\nolimits(1+\pi(k)|_U)\le1.                       \tag{*}
```


This criterion makes no splitting assumption on $`G`$ and does not require a choice of phase or quadratic coordinates. It applies only when the full-quotient invariance of $`U`$ has been established.

### Corollary: an $`M`$-isotypic radical shadow for $`S_5`$

Suppose in addition that $`G/P\cong S_5`$ and $`P/Z(P)\cong M^a`$ for $`a\ge1`$, where $`M`$ is the four-dimensional module of Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.1. The image of $`H`$ is $`F\cong F_{20}`$. The shadow $`U`$ is $`F`$-invariant, because conjugation by $`P`$ is trivial on $`P/Z(P)`$. Nagy's lemma gives $`M|_F`$ irreducible with $`\mathop{\mathrm{End}}\nolimits_F(M)=\mathbb F_2`$; since $`M`$ is absolutely irreducible for $`S_5`$ as well, every $`F`$-submodule of $`M^a`$ is a multiplicity subspace and is therefore $`S_5`$-invariant. Thus the hypothesis of (*) holds.

The shadow $`U`$ is nonzero: otherwise $`W=1`$, and Baumeister–Stein Lemma 4.2 gives $`P=K\cap P`$, impossible because the nonabelian extraspecial group $`P`$ has elements of order 4 whereas $`K`$ consists of involutions. Hence $`U\cong M^r`$ for some $`r\ge1`$. The section has an element above a transposition by Baumeister–Stein Lemmas 4.4–4.5. A transposition has rank 2 on $`M`$, as checked in the explicit six-point module control below, so its rank on $`U`$ is $`2r\ge2`$, contradicting (*). Consequently no such exponent-2 envelope exists, for any extension of $`S_5`$ by such an extraspecial $`P`$; in particular, no splitness is assumed. This deduction has the scoped independent reviews below.

## Fixed split extraspecial group: all stabilizers

**Argument with scoped independent review below.** Let M be Nagy's four-dimensional symplectic F₂S₅-module, β its nondegenerate invariant alternating form, and t a transposition with β(x,tx)=0 for every x. Let

P={(v,w,z):v,w∈M,z∈F₂},  (v,w,z)(v',w',z')=(v+v',w+w',z+z'+β(v,w')),
G=P⋊S₅,

with diagonal S₅ action. Then |P|=512, Z(P)=⟨ζ=(0,0,1)⟩, P/Z(P)=M⊕M, and O₂(G)=P. The proposed result is: **no faithful exponent-2 Bruck envelope (G,H,K) exists**, for any H≤G. This concerns this single split group and does not cover exponent-4 loops, nonsplit extensions, different extraspecial groups or other radical types.

Suppose such an envelope exists, put W=H∩P, and write F=π(H). Baumeister–Stein arXiv:0908.2597v1 Lemma 4.1 gives F≅F₂₀ up to conjugacy. Because ζ is central in G, core-freeness implies W∩Z(P)=1. Hence W injects into P/Z(P), is elementary abelian, and its image Wbar is totally singular for the extraspecial square form q(v,w)=β(v,w). It is F-invariant: elements of P act trivially on P/Z(P). By Nagy arXiv:0709.4544v1 Lemma 4.1, M|F is an irreducible projective module with endomorphism field F₂. Thus Wbar is a submodule of its direct square and has dimension 0,4 or 8. Total singularity forces dim Wbar≤4, since the polar form is nondegenerate. If W=1, Baumeister–Stein Lemma 4.2 gives P=K∩P, impossible because P has elements of order 4 while K has exponent 2. Hence dim W=4 and Wbar is one of the first axis, second axis or diagonal in M⊕M.

For either axis, the lift has the form $`W=\{(x,0,f(x)):x\in M\}`$ or $`W=\{(0,x,f(x)):x\in M\}`$, where $`f`$ is an **arbitrary** additive functional. These subgroups need not be normal in $`G`$: conjugation by $`P`$ can add the central involution, and $`H`$-lifts of $`F`$ can also change phases. Thus neither normality nor $`F`$-invariance of $`f`$ is assumed. For the diagonal, the lift has form $`W=\{(x,x,f(x)):x\in M\}`$, where $`f`$ is an arbitrary quadratic refinement of $`\beta`$. We need not assume or classify the rest of $`H`$: $`W\le H`$ suffices.

Let L=(1+t)M=C_M(t), dimension 2. Since 1+t is self-adjoint for β and (1+t)²=0, L is totally isotropic. For either axis, the arbitrary linear functional $`f|_L`$ has a nonzero kernel vector $`x=(1+t)a`$. In the first-axis case use $`p=(a,0,0)`$: then $`ptp^{-1}=(x,0,0)t`$, with $`(x,0,0)\in W`$. The second axis is analogous with $`p=(0,a,0)`$. In the diagonal case, $`f`$ restricts to a linear functional on $`L`$, so choose $`0\ne x\in L`$ with $`f(x)=0`$ and $`(1+t)a=x`$. With p=(a,a,0),

 p t p⁻¹=(x,x,β(a,(1+t)a))t=(x,x,0)t,

because β(a,ta)=0. Again the nonidentity left factor lies in W. The same collision applies to ζt because ζ is central.

Finally, all involution lifts over t are (v,w,z)t with v,w∈L and z∈F₂: the square condition β(v,w)=0 is automatic since L is isotropic. There are 32. The P-conjugacy orbit of t has exactly 16, one for each pair (v,w)∈L²: the phase is independent of choices of preimages under 1+t, by isotropy. The remaining 16 are the orbit of ζt. The split lift of C_{S₅}(t) fixes t and preserves each P-orbit, so these are two G-classes, each of size 160 over all ten transpositions. Baumeister–Stein Lemma 4.5 gives |K∩P|=|P:W|=32 and exactly 16 elements of K above each transposition. An exponent-2 Bruck section is a union of conjugacy classes, so it selects one of those two classes; the collision above contradicts transversality to H.

## Reproducible small module control

The following standalone Python 3.11+ check uses the four-dimensional even-six-point quotient model for $`M`$ in Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.1. It checks the paired generators generate a group of order 120, preserve the displayed alternating form, and that the chosen involution has totally singular two-dimensional image; it checks **all** 16 linear and 16 quadratic graph phases on that image. It is a targeted module control, not a group-extension or folder census. Assertions must be enabled; no files are written.

```python
C=(1,5,3,14); D=(2,4,8,1); I=(1,2,4,8)
def six_quotient(v,p):
 out=0
 for i in range(4):
  if v>>i&1:out^=(1<<p[0])^(1<<p[i+1])
 if out&32:out^=63
 return (out>>1)&15
assert C==tuple(six_quotient(1<<i,(1,0,3,2,5,4)) for i in range(4))
assert D==tuple(six_quotient(1<<i,(0,2,3,4,1,5)) for i in range(4))
def act(a,x):
 return __import__('functools').reduce(int.__xor__,(a[i] for i in range(4) if x>>i&1),0)
def mul(a,b):return tuple(act(a,x) for x in b)
def beta(x,y):return ((x.bit_count()*y.bit_count())+(x&y).bit_count())&1
def q0(x):return sum(((x>>i)&1)*((x>>j)&1)*beta(1<<i,1<<j) for i in range(4) for j in range(i+1,4))&1
group={I};todo=[I]
for a in todo:
 for b in (C,D):
  z=mul(a,b)
  if z not in group:group.add(z);todo.append(z)
assert len(group)==120
assert all(beta(act(g,x),act(g,y))==beta(x,y) for g in(C,D) for x in range(16) for y in range(16))
assert mul(C,C)==I and all(beta(x,act(C,x))==0 for x in range(16))
L={x^act(C,x) for x in range(16)};assert len(L)==4 and all(beta(x,y)==0 for x in L for y in L)
for l in range(16):
 f=lambda x:q0(x)^((l&x).bit_count()&1)
 assert any(x and f(x)==0 for x in L)
 assert any(x and ((l&x).bit_count()&1)==0 for x in L)
print('S5 matrices:',len(group),'image:',sorted(L),'all 16 linear/quadratic graph phases collide')
```

A Python 3.12.14 run prints `S5 matrices: 120 image: [0, 1, 6, 7] all 16 linear/quadratic graph phases collide`. The computation does not replace mathematical review. Independent checks an independent check and an independent check independently accepted all preceding deductions and the embedded control at exact source the recorded source revision, conditional on the stated envelope, normal-subloop and module inputs. Both checked the radical z-period, support necessity, general graph phase, invariant-shadow rank criterion, nonsplit M-isotypic consequence, and the fixed split-group calculation for all stabilizer graphs. Both independently ran the embedded control with Python 3.12.14. The first reviewer directly inspected Baumeister–Stein arXiv:0908.2597v1 Lemmas 4.1–4.5 and Nagy arXiv:0709.4544v1 Lemma 4.1, including the absolute irreducibility and endomorphism field of M restricted to F₂₀. These are scoped exponent-two results, not an extraspecial-radical classification or a result for exponent four; no formal verification is claimed. The following later extension was not part of those reviews.


## Semisimple M/N Frattini module: nonsplit obstruction

Argument with scoped independent reviews below, continuing C0010. Assume a finite simple nonassociative exponent-2 right Bruck loop with faithful Baer envelope (G,H,K), P=O₂(G) extraspecial with Z(P)=Φ(P)=<z>, and G/P≅S₅. Suppose V=P/<z>≅M^a⊕N^b, with no trivial summands, using Nagy's two nonisomorphic four-dimensional irreducible modules. There is no assumption that G splits over P. Then the following proposed argument excludes these hypotheses. Its inputs are Nagy [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.1; Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Lemmas 4.1–4.5; and the support-level necessary condition above. The reviews below retain these source and prior-result hypotheses.

Let q be the square form of P on V and β its nondegenerate polar form. Both are S₅-invariant. Let t be a transposition, write T=1+t, I=TV and C=C_V(t). The prior obstruction says q(I)=0, for otherwise Kz=K and the central quotient contradicts simplicity. Since β is nondegenerate, C=I^⊥.

Both M and N are absolutely irreducible self-dual and nonisomorphic. Their unique nonzero invariant bilinear forms β_M and β_N are alternating and nondegenerate. Therefore β separates into β_M⊗s_M and β_N⊗s_N, with s_M,s_N nondegenerate symmetric forms on the multiplicity spaces. The form s_M must be alternating: otherwise some M-submodule has β_M as its induced polar form and q restricts to an S₅-invariant quadratic refinement of β_M, which does not exist. One direct proof uses M=even six-point module / constants, with the S₅=PGL₂(5) action 2-transitive on the six points. An invariant quadratic assigns the same value ε to every weight-two vector. The all-ones vector is the sum of three disjoint weight-two vectors and vanishes in M, giving ε=0; two intersecting weight-two vectors pair to 1 and sum to another weight-two vector, a contradiction. Hence a is even.

The form s_N must also be alternating. For N the even five-point module with dot-product form, choose a vector x containing one point moved by t and one fixed point; β_N(x,tx)=1. If some multiplicity vector y has s_N(y,y)=1 then q(T(x⊗y))=β(x⊗y,t(x⊗y))=1, contrary to q(I)=0. Thus s_N is alternating, and b is even.

Let W=H∩P and U=WZ/Z. Corefreeness and centrality of z give W∩Z=1; W is elementary and U totally singular. Both M|F₂₀ and N|F₂₀ are copies of the same four-dimensional absolutely irreducible module S, so dim U=4r for an integer r. Nondegeneracy of β and total singularity imply 4r≤dim V/2=2a+2b. A transposition has rank 2 on M and rank 1 on N, so ρ=rank(T)=2a+b. The fiber formula gives

   |K∩π⁻¹(t)|=|P:W|/2=2^{4a+4b−4r}=2^ρ·2^h,
   h=2a+3b−4r≥b.

If b>0, evenness of a,b makes h even and at least 2, so 2^h≡4 (mod 6).

For each involution k above t define ℓ_k:C→F₂ by kpk⁻¹p⁻¹=z^{ℓ_k(v)}, where p projects to v∈C. This is a well-defined linear functional. It vanishes on I: if v=Tu, choose p lifting u and write α=conjugation by k; the lift pα(p) of v satisfies α(pα(p))(pα(p))⁻¹=z^{β(u,tu)}=z^{q(Tu)}=1. Hence ℓ_k belongs to (C/I)*. The dimension of I is ρ, and C/I receives no contribution from M since C_M(t)=TM. On each N it is the two-dimensional even-weight subspace of the three unmoved points. A 3-cycle c centralizing t acts fixed-point-freely on this quotient and hence also on its dual, for every b.

Under conjugation by any lift of c to G, ℓ_k transforms by the natural dual c-action; this is valid even if G is nonsplit because z is central. Thus every nonzero ℓ has a 3-element orbit. The P-conjugacy orbit of k has size 2^{ρ+1} when ℓ_k≠0: it projects onto the affine I-coset and contains both central phases because some fixed-vector lift has commutator z. Hence any G-conjugacy class with nonzero ℓ contributes a multiple of 3·2^{ρ+1}=6·2^ρ elements to the t-fiber.

When ℓ=0, there are at most two P-conjugacy orbits, each of size 2^ρ, among all involutions over t. Indeed, if k' is another such involution then k'=pk for p∈P with v=pZ∈C; equality ℓ_{k'}=ℓ_k forces β(v,C)=0, so v∈C^⊥=I. P-conjugation therefore adjusts the image v, leaving at most the two central phases. The section K is G-conjugacy-invariant because it has exponent 2, so its t-fiber normalized by 2^ρ is congruent to 0, 1, or 2 modulo 6. This contradicts its required value 2^h≡4 modulo 6 when b>0.

If b=0, the nonsplit M-isotypic exclusion above applies. If a=b=0, P cannot be nonabelian extraspecial. This proves the stated exclusion under its cited inputs. Trivial summands are treated next; nonsemisimple modules, non-extraspecial radicals and exponent-four loops are outside this section.

## Removing trivial summands in a semisimple shadow

**Deduction with scoped independent reviews below.** In the same finite simple exponent-two extraspecial S₅ setting, suppose only that V=P/Z(P) is semisimple. Nagy's simple-module list gives V≅M^a⊕N^b⊕1^c. The invariant-functional restriction from the [Frattini-shadow argument](bruck-frattini-shadow.md#invariant-functional-detection-without-a-quotient-folder), independently reviewed at the recorded source revision, is injective:

    Hom_S₅(V,1) → Hom_F₂₀(U,1),   U=WZ/Z.

Here V restricted to F₂₀ is the semisimple module S^{a+b}⊕1^c, with S the nontrivial four-dimensional simple module. Hence U splits across these two nonisomorphic isotypes. Every invariant functional on V vanishes on M^a⊕N^b, so injectivity forces U∩1^c=1^c. Since U is totally singular, the polar form vanishes on 1^c. On the other hand, the nondegenerate invariant polar form on V pairs 1^c orthogonally to M^a⊕N^b, by absence of intertwining maps, and therefore restricts nondegenerately to 1^c. Thus c=0.

Together with the preceding argument this excludes every semisimple Frattini module for an extraspecial radical in the stated simple exponent-two S₅ setting, without assuming a split extension. Consequently any surviving extraspecial radical in that setting must have a nonsemisimple S₅-module P/Z(P). The assertion does not treat other quotient groups, higher Bruck exponents, or non-extraspecial radicals. Independent checks an independent check and an independent check independently accepted the preceding two semisimple sections at exact source the recorded source revision, conditional on Nagy's module data, the cited Baumeister–Stein envelope and fiber results, the reviewed extraspecial support condition, and the Frattini functional injection. Both checked the isotypic bilinear-form decomposition and multiplicity parity, the centralizer action on the fixed-space quotient, equivariance of the commutator functional for arbitrary nonsplit lifts, the zero-functional bound and mod-six contradiction, and the elimination of trivial summands. These new sections use an analytic argument; no new computation or formal verification was performed. The conclusion excludes semisimple shadows only in the stated exponent-two extraspecial S₅ setting. The subsequent hyperbolic J⊕J* continuation is separate and was not part of those reviews.

<a id="hyperbolic-j-jdual"></a>

## Hyperbolic $`J\oplus J^*`$: a nonsplit obstruction

**Deduction with scoped independent reviews below.** Retain the faithful simple nonassociative exponent-2 extraspecial-radical hypotheses of this manuscript, with $`G/P\cong S_5`$. Assume specifically that $`V=P/Z(P)\cong J\oplus J^*`$ and that its square form is the hyperbolic form $`q(x,f)=f(x)`$, with the natural contragredient action. Here $`J=\mathbb F_2^6/\langle(1,1,1,1,1,1)\rangle`$, and $`J^*`$ is its dual. We make no splitting assumption on $`G`$. The following excludes this hyperbolic module; it does not claim that every invariant quadratic form on the underlying module is hyperbolic in this model.

Put $`W=H\cap P`$, $`U=WZ(P)/Z(P)`$, and let $`F=F_{20}`$ and $`C_5\triangleleft F`$ be the quotient of $`H`$ and its normal five-subgroup. The [Frattini-shadow invariant-functional injection](bruck-frattini-shadow.md#invariant-functional-detection-without-a-quotient-folder), independently reviewed at source the recorded source revision, forces $`U`$ to map nontrivially under the unique nonzero invariant functional $`J\oplus J^*\to\mathbf1`$. As an $`F`$-module, $`V\cong\mathbf1^2\oplus S^2`$, where $`S`$ is the irreducible projective four-dimensional module. The $`C_5`$-fixed part is a hyperbolic plane with singular basis $`j\in J`$, $`j^*\in J^*`$, satisfying $`j^*(j)=1`$. The invariant functional is nonzero on $`j`$ and zero on $`j^*`$; total singularity therefore forces $`U^{C_5}=\langle j\rangle`$. The $`S`$-part of $`U`$ is a sum of copies of $`S`$. Since $`U`$ is totally singular in a nondegenerate ten-dimensional quadratic space, $`\dim U\le5`$. Hence $`\dim U=1`$ or $`5`$.

A transposition $`t`$ has rank 4 on $`V`$, so $`\dim C_V(t)=6`$. If $`\dim U=1`$, the fiber theorem requires $`|K\cap Pt|=|P:W|/2=2^9`$; yet an involution over $`t`$ has radical coordinate in $`C_V(t)`$, with at most two central lifts per coordinate, so there are at most $`2^7`$ such involutions. Thus $`\dim U=5`$. Its $`S`$-part is one of the three $`F`$-submodules isomorphic to $`S`$ in $`S^2`$.

The finite module verifier [verify_bruck_extraspecial_jdual.py](../code/verify_bruck_extraspecial_jdual.py) constructs these three spaces in the explicit six-point model and checks that their intersections with $`(1+t)V`$ have cardinalities $`4,2,2`$. Thus for every possible $`U`$, the intersection is nonzero. The first space is the invariant submodule $`J`$, already excluded by the rank criterion above; the argument below treats all three. The finite verification and this deduction have the scoped independent reviews recorded after the all-form extension.

For $`k\in K`$ above $`t`$, the graph-collision criterion above implies that the central commutator functional $`\ell_k:C_V(t)\to\mathbb F_2`$ is zero. Put $`I=(1+t)V`$, so $`|I|=2^4=16`$. The $`P`$-conjugacy orbit of $`k`$ has size 16. If $`k'=pk`$ is another involution with $`\ell_{k'}=0`$, then $`pZ(P)\in C_V(t)`$, and the difference of the two functionals is $`b(pZ(P),-)`$ on $`C_V(t)`$. Hence $`pZ(P)\in C_V(t)^\perp=I`$. Conjugation by $`P`$ removes this image, leaving only the two central phases $`k`$ and $`zk`$. Therefore the complete set of involutions over $`t`$ with zero functional consists of exactly two $`P`$-orbits of 16 elements, interchanged by $`z`$.

The fiber theorem requires $`|K\cap Pt|=|P:W|/2=2^5=32`$. Since all its elements have zero functional and $`K`$ is $`P`$-conjugacy invariant, it is exactly the full set just described and is $`z`$-stable. Conjugacy gives $`z`$-stability in every transposition fiber; the radical section $`P\cap K`$ is $`z`$-stable by the first argument in this manuscript. Thus $`Kz=K`$, and the central quotient gives a proper nontrivial loop quotient, contradicting simplicity. The argument depends on the cited shadow injection, the graph-collision criterion and the finite module calculation, and all of its new steps require independent review.

## All invariant quadratic forms on $`J\oplus J^*`$

**Extension with scoped independent reviews below.** In the same faithful simple exponent-2 extraspecial $`S_5`$-envelope setting, the hyperbolic hypothesis in the preceding section can be removed: the proposed exclusion applies to every $`S_5`$-invariant quadratic form with nondegenerate polar form on the fixed module $`V=J\oplus J^*`$. No splitting assumption is made on the group extension. This does not cover other $`S_5`$-modules or higher Bruck exponents. The scoped reviews below cover this extension and the preceding hyperbolic proof at their exact source revision.

The extended [standalone verifier](../code/verify_bruck_extraspecial_jdual.py) represents a quadratic function on the 10-dimensional space by its 10 linear and 45 squarefree quadratic coefficients. For each $`S_5`$ generator, invariance is a degree-at-most-two identity and is determined by its values on the ten basis vectors and their 45 pairwise sums. Exact linear elimination gives invariant-space dimension 3. The verifier identifies a basis on all 1,024 vectors as


```math
\lambda_J,\qquad q_{J^*},\qquad Q(x,\phi)=\phi(x),
```


where $`\lambda_J`$ is the nonzero invariant functional on $`J`$, and $`q_{J^*}(\phi)=\mathop{\mathrm{wt}}\nolimits(\phi)/2\pmod2`$ in the even six-point realization of $`J^*`$. Exactly four invariant forms have nondegenerate polar form:


```math
q_{e,d}=Q+e\lambda_J+dq_{J^*},\qquad e,d\in\mathbb F_2.
```


The verifier computes polar forms using vector addition by XOR, including the zero diagonal, and checks all four remaining forms have degenerate polar. On the two-dimensional C₅-fixed space, all four polar forms retain the nondegenerate hyperbolic cross pairing, so its totally singular subspaces have dimension at most one. It retains the preceding strict-shadow and invariant-functional bounds: $`\dim U=5`$, with one $`C_5`$-fixed line detected by $`\lambda_J`$ and one of the three four-dimensional simple $`F_{20}`$-submodules. It tests every vector of each candidate for total $`q_{e,d}`$-singularity and computes its intersection with $`(1+t)V`$:

| $`(e,d)`$ | Admissible fixed-line representatives and intersection dimensions |
| --- | --- |
| $`(0,0)`$ | $`4: 2,1,1`$ |
| $`(1,0)`$ | $`996: 2,1,1`$ |
| $`(0,1)`$ | $`4:2;\ 996:2`$ |
| $`(1,1)`$ | none |

The representatives are bit vectors in the verifier's stated basis; the entries for a line correspond to distinct simple constituents. In the last case the fixed two-space is anisotropic. In every admissible case $`U\cap(1+t)V\ne0`$. The graph-collision criterion from the preceding section therefore forces $`\ell_k=0`$ for every section element over a transposition. The same counting argument then forces the entire 32-element zero-functional fiber, which is stable under the central involution. Radical-section periodicity gives $`Kz=K`$, contradicting simplicity by the cited quotient criterion. This argument uses the actual invariant form and does not presume that the different forms are isometric.

From the repository root, run:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_extraspecial_jdual.py
```

The Python 3.12.14 run completed in 0.04 seconds in this workspace and reproduced the table. The current script includes the earlier hyperbolic checks as well as the new all-form calculation. Independent checks an independent check and an independent check independently accepted both J⊕J* sections and the standalone verifier at exact source the recorded source revision, conditional on the cited module/F₂₀ facts, Frattini functional injection, graph-collision and radical-periodicity results, and Bruck fiber and quotient inputs. Both read the pinned script and independently ran it with Python 3.12.14, reproducing the complete quadratic-form and stabilizer-shadow tables. They checked the fixed-space decomposition, all Hom-space submodules, the capacity bound, nonzero intersections, and saturation of the two zero-functional P-orbits in arbitrary extensions. This is a restricted exclusion with finite computational evidence, not a census or formal verification. The later common-vector extension is outside that source revision.

## Rank dichotomy and arbitrary $`J/J^*`$ multiplicities

**Deduction with scoped independent reviews below.** Retain the faithful simple nonassociative exponent-2 Bruck-envelope hypotheses and the extraspecial radical $`P`$ above, and suppose $`G/P\cong S_5`$. Put $`V=P/Z(P)`$, $`d=\dim V`$, $`U=(H\cap P)Z(P)/Z(P)`$, $`w=\dim U`$, $`I=(1+t)V`$ for a transposition $`t`$, and $`\rho=\dim I`$. The graph-collision criterion gives the following dichotomy, without assuming a splitting of $`G`$ or a particular square form:


```math
U\cap I\ne0\quad\Longrightarrow\quad w=\rho=d/2. \tag{7}
```


Indeed, if $`U\cap I\ne0`$, the criterion says that every selected involution over $`t`$ has zero central-commutator functional on $`C_V(t)`$. Each such $`P`$-orbit has size $`2^\rho`$, and there are at most two; if one exists, they are the orbit and its central translate. The section fiber has size $`2^{d-w}`$. If $`d-w>\rho+1`$, there are too few available involutions. If equality holds, the fiber is the full zero-functional locus and is $`z`$-stable. All transposition fibers are conjugate, and the radical section is $`z`$-stable by the first argument of this manuscript; hence $`Kz=K`$, contradicting simplicity by the central folder quotient. Thus $`d-w\le\rho`$. Since $`U`$ is totally singular, $`w\le d/2`$, while $`(1+t)^2=0`$ gives $`\rho\le d/2`$. Both inequalities are equalities, proving (7). In its boundary case the graph criterion further requires $`\dim(U\cap I)\le2`$, with an anisotropic phase if the dimension is 2. In particular, $`\rho<d/2`$ forces $`U\cap I=0`$.

We propose the following consequence: no such envelope has

    V ≅ J^a ⊕ (J*)^b ⊕ M^c ⊕ 1^s,

with any nonnegative multiplicities, for any invariant nondegenerate square form or any group extension. The modules J and J* are the nonisomorphic indecomposable six-point modules, dual to each other; M is their four-dimensional simple constituent. Their definitions and source/module inputs are the same as in the preceding sections. The nondegenerate invariant commutator form makes V self-dual. Krull–Schmidt therefore forces a=b, since M and 1 are self-dual.

Let F=F₂₀ and C₅ normal in F. Restriction gives the semisimple F-module V=1^{2a+s}⊕S^{2a+c}. Averaging over C₅ is self-adjoint for the commutator form, so the fixed and nonfixed spaces are orthogonal and the fixed space is nondegenerate. Thus the totally singular U^{C₅} has dimension at most a+s/2. On the other hand, Hom_S₅(V,1) has dimension a+s: J has trivial head, whereas J* and M have no trivial quotient. Every such functional vanishes on the S-isotypic part of U. The Frattini functional injection, reviewed at the recorded source revision, gives dim U^{C₅}≥a+s. Hence s=0. No quotient-folder assumption is used.

If a=0, the earlier nonsplit M-isotypic exclusion applies (and V=0 is incompatible with a nonabelian extraspecial group). Suppose a>0. Then d=10a+4c and ρ=4a+2c<d/2, so (7) gives U∩I=0. The source fiber has size 2^{d−w}, while all involutions over t project to C_V(t) and have at most two central lifts each. Therefore w≥ρ−1=4a+2c−1>a. Since dim U^{C₅}≤a, U contains a nonzero F-simple S-line.

The finite module interface needed here is a common nonzero x∈S whose embeddings in J and J* lie in their respective transposition images. The appended check in [verify_bruck_extraspecial_jdual.py](../code/verify_bruck_extraspecial_jdual.py) computes those two preimage spaces as {0,1,10,11} and {0,10} in one common S-basis. Its earlier code at the recorded source revision did not contain this added assertion. The same x works for M: identify M with the simple socle of J; the transposition has rank two on both, so (1+t)M=(1+t)J.

Because End_F(S)=F₂, every F-simple line in S^{2a+c} is the image of a nonzero multiplicity vector v. The vector x⊗v is nonzero, lies in that line of U, and lies in I, since t acts independently on the J, J* and M summands and x has a displacement preimage in every type. This contradicts U∩I=0.

Independent checks an independent check and an independent check independently accepted the rank dichotomy, arbitrary-multiplicity consequence and added common-vector certificate at exact source the recorded source revision, conditional on the preceding extraspecial graph, periodicity and fiber results, Frattini functional injection and stated module inputs. Both checked saturation of the zero-functional fiber, the self-duality and head arguments, fixed-space orthogonality, the capacity bound, and transport of the common vector to each summand. Both independently ran the pinned verifier with Python 3.12.14 and obtained the common preimage vector 10. This is not a classification or formal verification. They do not exclude other indecomposable principal modules or N-factors, non-extraspecial radicals, other quotient groups, or exponent-four loops.

## The 16-dimensional principal projective shadow

**Deduction and finite certificate with scoped independent review below.** Under the faithful simple nonassociative exponent-2 Bruck-envelope hypotheses of the preceding sections, let $`P=O_2(G)`$ be extraspecial and $`G/P\cong S_5`$. No group-extension splitting is assumed. We propose that $`V=P/Z(P)`$ cannot be the 16-dimensional principal projective cover of the four-dimensional simple module $`M`$.

For a precise model, let $`N`$ be the deleted five-point permutation module, let $`F=F_{20}`$ be a five-point-cycle normalizer, and let $`R=N\otimes\mathbb F_2[S_5/F]`$. The verifier constructs the paired five- and six-point permutation actions of $`S_5`$ on $`R`$. If $`z`$ is the sum of the 20 three-cycles, it defines $`V_0=(1+z^{32})R`$. It checks that $`z^{32}`$ and $`1+z^{32}`$ are complementary equivariant idempotents of ranks 8 and 16, and that the three-cycle sum acts as zero on the trivial and $`M`$ simples and as the identity on $`N`$. The module $`S=N|_F`$ is the four-dimensional projective simple $`F`$-module. Thus $`R=\mathop{\mathrm{Ind}}\nolimits_F^{S_5} S`$ is projective; Frobenius reciprocity gives one copy each of $`M`$ and $`N`$, and no trivial module, in its head. The projective-cover dimensions 16 and 8 from [the uniform principal-support calculation](bruck-s5-uniform-principal-support.md) (source the recorded source revision) identify $`V_0`$ with $`P(M)`$. The corresponding six-point description of $`M`$ and five-point description of $`N`$ are the module inputs used above, including Nagy, [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.1. The scoped reviews below cover this identification and the calculation.

The standalone [verifier](../code/verify_bruck_extraspecial_projective.py) solves all invariance equations for quadratic functions on $`V_0`$, in the 136-dimensional space of linear and squarefree quadratic coefficients. The invariant space has dimension 3; exactly four of its eight forms have nondegenerate polar form. For each of these four forms, the polar form restricted to the four-dimensional $`C_5`$-fixed subspace is nondegenerate. The nonfixed part is $`S^3`$: the verifier computes $`\dim\mathop{\mathrm{Hom}}\nolimits_F(S,V_0)=3`$, constructs its seven simple lines and hence its seven $`S^2`$-submodules, and checks that their polar restrictions have ranks $`4,4,4,8,8,8,8`$. None is totally singular. The calculation includes all four nondegenerate forms, not just those satisfying the additional necessary condition $`q((1+t)V)=0`$; it checks that exactly two satisfy that condition.

Write $`U=(H\cap P)Z(P)/Z(P)`$, $`w=\dim U`$, and let $`t`$ be a transposition. The certificate gives $`\rho=\dim(1+t)V=8`$. The cited source fiber count gives $`|K_t|=2^{16-w}`$. All involutions over $`t`$ project into $`C_V(t)`$, with at most two central lifts per vector, so $`|K_t|\le 2^{16-8+1}`$ and $`w\ge7`$. Since $`U`$ is totally singular, $`w\le8`$. Averaging over $`C_5`$ decomposes $`U`$ into its fixed and nonfixed parts; the former is singular in a nondegenerate four-space and so has dimension at most 2, while the latter has dimension divisible by 4. Consequently $`w=7`$ is impossible and $`w=8`$ requires an $`S^2`$-submodule with zero fixed part. The seven-plane calculation rules this out. This contradiction uses only the induced action and square form on $`P/Z(P)`$, so it applies to nonsplit extensions as well.

A related proposed shortcut fails: the verifier finds that six of the seven $`F`$-simple lines in $`V_0`$ meet $`(1+t)V_0`$ only in zero, while the seventh has intersection dimension 2. Thus a common nonzero displacement vector for every $`F`$-simple line cannot be asserted for arbitrary principal modules.

From the repository root, with Python 3.11 or later and assertions enabled, run:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bruck_extraspecial_projective.py
```

Independent checks an independent check and an independent check independently accepted this section and the standalone verifier at exact source the recorded source revision, conditional on the cited F₂₀-module facts, projective-cover dimensions reviewed at the recorded source revision, and Bruck envelope/fiber inputs. Both checked induction and the Frobenius-reciprocity head, the class-sum projector and module identification, completeness of the invariant quadratic and seven-plane computations, and the extraspecial dimension argument. Both read the pinned script and independently ran it with Python 3.12.14, reproducing the four nondegenerate forms, fixed-space rank four, plane ranks and failed common-vector control. This excludes the stated module for any group extension; it does not exclude other principal indecomposables or general extraspecial radicals, and is not formal verification.

