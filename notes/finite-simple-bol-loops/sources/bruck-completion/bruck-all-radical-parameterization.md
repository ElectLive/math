# Extension-data parameterization for all Bruck radicals

**Mira Cult**

**Extension-data scheme with scoped independent reviews below.** This concerns [C0010](../../claims/0010.md), without a new claim ID. We describe complete finite extension, section and equivalence data, conditional on the stated inputs, for finite simple nonassociative right Bruck loops with faithful generated Baer envelope (G,H,K), P=O₂(G), and A=G/P≅∏ᵢPGL₂(qᵢ), e≥1, qᵢ=9 or a Fermat prime at least 5. We make no assumption that P is elementary, class two or extraspecial, and do not assume X has exponent 2. The intended output is a parameterization subject to explicit finite admissibility tests, not a status-closing classification of the Bruck branch.

The quotient, stabilizer, inversion and fiber inputs are Baumeister–Stein, [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5, under their faithful-envelope hypotheses. The [Frattini-shadow bounds](bruck-frattini-shadow.md#core-reduced-module-and-all-support-shadow-bounds), independently reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/70a2e52726484645897e9b64c33dd9b7563d7d18), define the positive multiplicity m below. The [all-radical bound](bruck-all-radical-constraints.md) has separate independent reviews at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6b719ad3026522f93cd9e0e027ae4027f6ee12df). The factor-system, stabilizer, marked-section, normal-subloop and isomorphism interfaces below follow the construction in [the extraspecial product parameterization](bruck-extraspecial-product-parameterization.md), but are stated and checked here for arbitrary finite 2-groups; none uses extraspeciality. The new deductions and application of the bound have the scoped independent reviews below.

## Construct the abstract radical

Let B=∏ᵢBᵢ≤A be the product of point-stabilizing Borels, and set


```math
R=\sum_i q_i(q_i-1)/2,\qquad B(A)=[1+2^e(3e+1)]|A|.
```


Fix A, r≥0 and m≥1, and set


```math
D=(r+1)B(A)m+(r+1)r^2[A:B]+r(R+3e+r).\tag{1}
```


The all-radical manuscript proves, under its cited inputs, $`\dim P/\Phi(P)\le D`$, with $`|\Phi(P)|=2^r`$. Thus $`|P|\le2^{r+D}`$. Construct a finite cover of the possible abstract groups P using central order-two towers. Start at P₀=1 and, for 0≤j<ℓ≤r+D, choose normalized cocycles $`c_j:P_j\times P_j\to C_2`$ for the trivial action, satisfying c_j(1,x)=c_j(x,1)=0 and c_j(x,y)+c_j(xy,z)=c_j(y,z)+c_j(x,yz) for every x,y,z∈P_j, and let


```math
P_{j+1}=C_2\times_{c_j}P_j,\qquad
 (z,x)(z',y)=(z+z'+c_j(x,y),xy).
```


Keep every resulting P=Pℓ with $`|\Phi(P)|=2^r`$ and $`\dim P/\Phi(P)\le D`$. Each finite 2-group has a central subgroup of order 2 and hence appears by induction. These towers are used **only to construct P abstractly**: their subgroups need not be invariant under a later G-action. Different towers and cohomologous cocycles may yield the same P; they are deliberately retained until the final isomorphism test.

## Nonabelian extensions and stabilizers

For each P choose normalized maps $`\alpha_a\in\mathop{\mathrm{Aut}}\nolimits(P)`$ and $`f(a,b)\in P`$ satisfying, for all a,b,c∈A,


```math
\alpha_a\alpha_b=\mathop{\mathrm{Inn}}\nolimits(f(a,b))\alpha_{ab},\quad
 f(a,b)f(ab,c)=\alpha_a(f(b,c))f(a,bc),\quad
 \alpha_1=\mathrm{id},\ f(1,a)=f(a,1)=1.
```


Let $`G=P\times_f A`$ have multiplication


```math
(p,a)(q,b)=(p\alpha_a(q)f(a,b),ab).
```


Every extension of A by P has this form after choosing a normalized section. The maps α are arbitrary automorphisms of the completed P; no tower preservation is imposed. Since O₂(A)=1, the constructed normal P equals O₂(G). Conjugation by lifts gives an A-action on V=P/Φ(P), since inner automorphisms of P act trivially on V.

Enumerate W≤P and elements h_b∈P, b∈B, with h₁=1, and form


```math
H=\bigcup_{b\in B}W(h_b,b).
```


Require every (h_b,b) to normalize W and


```math
h_b\alpha_b(h_c)f(b,c)h_{bc}^{-1}\in W\qquad(b,c\in B).
```


These conditions give exactly the subgroups H with H∩P=W and π(H)=B. Test Core_G(H)=1 separately. Put U=WΦ(P)/Φ(P), let C be the sum of all A-submodules of V contained in U, and compute the number of nontrivial simple composition factors of V/C. Retain exactly those data for which this number is the fixed m. This definition uses H; m is not an independently imposed count of factors of P or V.

## Inversion, marked section and admissibility

Enumerate all $`\tau\in\mathop{\mathrm{Aut}}\nolimits(G)`$ with $`\tau^2=1`$, $`\tau|_H=\mathrm{id}`$, and τ inducing the identity on A and V. Here τ²=1 includes τ=id. For every target Bruck envelope the canonical inversion has these properties: the Frattini factorization makes τ fix V, and the allowed images of K are involutions or 1, so inversion and generation make τ fix A. No assumption about τ on Φ(P) is made.

Use the formal external semidirect product $`G^+=G\rtimes\langle\hat\tau\rangle`$, even if τ=id. Enumerate every union Λ of G⁺-conjugacy classes of involutions in $`\hat\tau G`$ containing τ̂, and put K=τ̂Λ. Then 1∈K, τ(k)=k⁻¹, K is inverse-closed, and conjugation within Λ gives closure of K under sandwich products. Moreover Λ⁻¹Λ=K⁻¹K is G-conjugacy-invariant. Require


```math
H\cap K^{-1}K=\{1\},\qquad |K|=[G:H].\tag{2}
```


The first condition prevents collisions in H-cosets, its G-invariance prevents collisions for conjugates of H, and the second gives all required transversals. Since τ fixes H and Λ is invariant, H normalizes K. The usual folder criterion yields a Bol loop, and τ induces inversion as an automorphism, so the loop is Bruck.

The source fiber theorem may be imposed as an exact additional filter. For I⊆{1,…,e}, let C_I be the A-class with outer involution precisely in the coordinates in I, and put n₀=[P:W]. Retain only the coordinatewise allowed images and require, for every x∈C_I,


```math
|K\cap\pi^{-1}(x)|=n_0\,2^{|I|}/\prod_{i\in I}(q_i-1).\tag{3}
```


This includes I=∅ and applies to the original group and section. It does not infer any loop-folder property for a Frattini quotient.

Require $`\langle K\rangle=G`$. Enumerate **all** nontrivial normal subgroups $`N\trianglelefteq G`$, including those with nontrivial image in A, and reject whenever $`HN<G`$ and


```math
|KN/N|=[G:HN].\tag{4}
```


By [C0001, Theorem 2.2](../foundations/C0001.md), equality is exactly the quotient-folder condition detecting a proper nontrivial normal subloop in the faithful generated envelope; every normal subloop yields such a normal subgroup. Test nonassociativity directly on the finite folder. If selecting the proper/non-Moufang branch, impose the appropriate Moufang failure test as an additional identity filter; quotient type alone does not prove it.

Every accepted datum gives a finite simple nonassociative Bruck loop, subject to the cited folder theorem. Conversely, for every loop in the stated scope, its quotient A, Borel B, radical P, extension section, H, canonical τ and marked Λ occur among these choices. The reviewed bound (1), applied with its measured r and m, makes the fixed-parameter radical search exhaustive. These implications have the scoped independent reviews below.

## Isomorphism and scope

For two accepted data, every envelope isomorphism preserves P=O₂(G) and has the form


```math
\Phi(p,a)=(\beta(p)u(a),\gamma(a)),
```


where $`\beta:P\to P'`$ and $`\gamma:A\to A'`$ are isomorphisms and $`u:A\to P'`$ is normalized. The necessary and sufficient group-homomorphism equations are


```math
\beta\alpha_a\beta^{-1}=\mathop{\mathrm{Inn}}\nolimits(u(a))\alpha'_{\gamma(a)},\qquad
 \beta(f(a,b))u(ab)=u(a)\alpha'_{\gamma(a)}(u(b))f'(\gamma(a),\gamma(b)).
```


Enumerate all β, γ and u satisfying these equations, including factor permutations and full quotient automorphism groups, and require $`\gamma(B)=B'`$, $`\Phi(H)=H'`$, $`\Phi\tau=\tau'\Phi`$, and $`\Phi(K)=K'`$. No preservation of either chosen central tower is required of β. These tests are necessary and sufficient for faithful generated-folder isomorphism and hence loop isomorphism: loop isomorphisms carry the generated translation envelopes and the unique inversion automorphism to one another.

At each fixed A,r,m the reviewed bound makes every tower, factor system, subgroup, automorphism, marked-class union, normal-subgroup test and isomorphism search finite. The restricted semisimple quotient and bounded radical order are structural information beyond a Latin-square census. Nevertheless the parameters A,r,m remain unbounded, and no closed description of the surviving extension and section data is supplied. This is a finite extension-data search scheme conditional on the cited inputs, not a solved global family classification or a closure of the 0323 Bruck problem.


## Independent review

reviewers contributor 1 and contributor 2 independently accepted the construction, fixed-parameter exhaustiveness and isomorphism equivalence at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/6b719ad3026522f93cd9e0e027ae4027f6ee12df), conditional on the cited dimension bound, Frattini-shadow, Baumeister–Stein and C0001 inputs. They checked that the central towers construct abstract P only, retain every group extension and stabilizer, preserve no tower flag under later actions or isomorphisms, use formal marked sections even for τ=id, and test every normal subgroup required for simplicity. The bound was separately accepted at the same source by contributor 1 and contributor 3. A separate primary-source interface audit by contributor 4 is recorded in [REFERENCES.md](../foundations/references.md#global-bruck-envelope-source-interface). Both scheme reviews found structural information beyond a Latin-square census, while emphasizing the unbounded parameters, general extension and section enumeration, and absence of a closed family description or efficient search. No computation or formal verification was used; the unrestricted Bol classification remains open.
