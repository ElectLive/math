# Central-Frattini constraints for simple Bruck envelopes

**Argument with scoped independent reviews below.** Let X be a finite simple nonassociative right Bruck loop with faithful Baer envelope (G,H,K), P=O₂(G), and assume only that


```math
\Phi=\Phi(P)\le Z(G).\tag{1}
```


Let A=G/P≅∏ᵢPGL₂(qᵢ), e≥1, where qᵢ=9 or a Fermat prime at least 5. The loop is not assumed to have exponent 2 and P is not assumed extraspecial or elementary. Put W=P∩H, D=P∩K, V=P/Φ and U=WΦ/Φ. This continues [C0010](../../claims/0010.md); no new ID or classification is asserted.

Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5, under the full faithful Bruck-envelope hypotheses, supply A, B=HP/P=∏Bᵢ for the point-stabilizing Borels, P=WD, canonical inversion τ, marked-section conjugacy invariance, and the full singleton-support fiber classes. The [Frattini-shadow manuscript](bruck-frattini-shadow.md#core-reduced-module-and-all-support-shadow-bounds) provides the core-reduced module bound and m≥1, independently reviewed at the recorded source revision, conditional on its cited inputs. The exact group-folder quotient criterion is [C0001, Theorem 2.2](../foundations/C0001.md). Those earlier reviews cover the stated inputs; the new argument has the separate reviews below.

## The Frattini subgroup is elementary

Since Φ is central in G, every subgroup of Φ is normal in G; core-freeness of H therefore gives W∩Φ=1. Squares and commutators of W lie in W∩Φ, so W is elementary abelian. For φ∈Φ write φ=wd with w∈W and d∈D, using P=WD. As φ is central in G, w and d commute. The inversion automorphism τ fixes w, inverts d and satisfies


```math
\tau(\varphi)=wd^{-1}=(wd)^{-1}=\varphi^{-1}.\tag{2}
```


Use a formal semidirect product G⁺=G⋊⟨τ̂⟩ with an external involution even if τ=1, and let Λ=τ̂K. Lemma 3.2(2) makes Λ G⁺-conjugacy-invariant. Since every φ∈Φ is central in G, (2) shows that conjugating τ̂k by φ changes its K-coordinate to φ⁻²k. Therefore KΦ²=K.

If Φ²≠1, then Φ²⊆K because 1∈K. The image of K in G/Φ² is a transversal to HΦ²/Φ²: multiplying K by Φ² leaves it unchanged, and the original folder gives one representative in each H-coset. The quotient criterion gives a loop epimorphism whose kernel is nontrivial because Φ²⊆K and H∩Φ²=1. It is proper because HΦ² maps to the proper Borel product B<A. Simplicity gives a contradiction. Thus


```math
\Phi\cong C_2^r\quad\text{for some }r\ge0,\qquad \tau|_\Phi=1.\tag{3}
```


In particular P has class at most 2 and exponent at most 4. Moreover WΦ is elementary abelian, and τ fixes V=P/Φ by P=WD.

## The core of the stabilizer shadow

Let C be the sum of all A-submodules of V contained in U. For x∈C^A, let w∈W be its unique lift; uniqueness uses W∩Φ=1. For every g∈G, the element [w,g] lies in Φ because x is A-fixed and P acts trivially on V. Since Φ is central, the map


```math
\chi_w:G\longrightarrow\Phi,\qquad g\longmapsto[w,g],
```


is a group homomorphism. It vanishes on H because w∈H and H∩Φ=1. If χ_w is nonzero, compose it with a linear functional Φ→C₂ nonzero on its image. The resulting nonzero group homomorphism vanishes on H and induces a nontrivial loop homomorphism X→C₂, because K generates G. Its kernel is nontrivial since |X|≥[A:B]=∏ᵢ(qᵢ+1)>2, contradicting simplicity. If χ_w=0, then w∈Z(G)∩H=1 by corefreeness. Hence


```math
C^A=0.\tag{4}
```


No nondegenerate commutator form is assumed in this argument.

Let E_C be the preimage of C in P and W_C=W∩E_C. Since C⊆U and W∩Φ=1, E_C=W_CΦ is elementary abelian and W_C has codimension r=dim Φ in E_C. It is normal in G because C is A-invariant, and τ-stable because τ fixes V. For λ=τ̂k∈Λ, write t=kP∈A and let α be conjugation by λ on E_C. If im(1+α) met W_C nontrivially, conjugating λ by an element of E_C would yield a second Λ-element with K-coordinate in the same H-coset as k; τ fixes H pointwise, so this contradicts transversality. Hence im(1+α)∩W_C=0, and projection to E_C/W_C gives rank(1+α|E_C)≤r. Projecting further to C gives


```math
\mathop{\mathrm{rank}}\nolimits(1+t\mid C)\le r\qquad(k\in K).\tag{5}
```


This uses Λ-invariance and does not assume K itself is G-conjugacy-invariant. The case r=0 is included.

## A fixed-quotient rank bound

For each factor PGL₂(qᵢ), its outer involutions form a single class Tᵢ of size qᵢ(qᵢ−1)/2, embedded with the other coordinates equal to 1. Lemmas 4.4–4.5 ensure every element of this class occurs as a K-image. The class generates its factor: its normal closure contains an outer element and has a nontrivial commutator with the simple derived subgroup, whose centralizer in PGL₂(qᵢ) is trivial. Therefore it contains the derived subgroup and is the whole factor. The union of these classes generates A.

Put


```math
R=\sum_i\frac{q_i(q_i-1)}2.
```


The map C→⊕_{t∈∪Tᵢ}(1+t)C, x↦((1+t)x)_t, is injective by (4), and each target summand has dimension at most r by (5). Consequently


```math
\dim C\le rR.\tag{6}
```


Let m be the number, counted with multiplicity, of nontrivial simple A-composition factors of V/C. The reviewed core-reduced module bound supplies m≥1 and


```math
\dim(V/C)\le[1+2^e(3e+1)]\,|A|\,m.
```


Together with (6),


```math
\dim(P/\Phi(P))\le rR+[1+2^e(3e+1)]\,|A|\,m.\tag{7}
```


Every k∈K has square in P because its image in A is an involution or identity. Since P has exponent at most 4, k⁸=1 and X has exponent dividing 8. These deductions bound the Frattini rank only for fixed r, quotient A and m. They neither prove condition (1) for all radicals nor bound r, m or the quotient, and do not construct or classify loops. The new steps have the scoped independent reviews below.


## Independent review

Independent checks an independent check and an independent check independently accepted this argument at exact source the recorded source revision, conditional on the cited Baumeister–Stein, Frattini-shadow and folder inputs. They checked the marked-involution collision without assuming ordinary conjugacy invariance of K, the elementary central-Frattini deduction and fixed-core argument, singleton-class generation, dimension bound and exponent conclusion. These are mathematical reviews of the stated radical class; no computation, formal verification or unrestricted classification is claimed.

## Further cross-layer estimates

**Deductions with the scoped independent reviews below.** Retain the hypotheses and notation of this manuscript. If the stabilizer-shadow core $`C`$ is zero, then the reviewed core-reduced theorem gives $`d=\dim V\le B(A)m`$, where $`B(A)=[1+2^e(3e+1)]|A|`$. The central-Frattini conclusion (3) makes $`P`$ class at most two and $`\Phi`$ elementary. Choosing $`d`$ lifts generating $`P`$, their squares and pairwise commutators span $`\Phi=P^2[P,P]`$. Hence


```math
r\le \binom{d+1}{2}\le\binom{B(A)m+1}{2}. \tag{8}
```


This bounds $`r`$ for fixed $`A,m`$ only under $`C=0`$; it does not establish that condition.

There is also a marked-centralizer test, valid more generally without assuming central $`\Phi`$. For a nonempty support $`I`$, let $`t`$ be a prescribed outer involution, put $`s_I=\log_2(\prod_{i\in I}(q_i-1)/2^{|I|})`$, and choose $`k\in K`$ above $`t`$. Let $`\lambda=\widehat\tau k`$, $`u=\dim U`$, $`\rho=\mathop{\mathrm{rank}}\nolimits(1+t\mid V)`$, $`h=\log_2|W\cap\Phi|`$, and $`f=\log_2|C_\Phi(\lambda)|`$. Then


```math
f\ge h+u+\rho+s_I-d. \tag{9}
```


Indeed the $`P`$-conjugacy orbit of $`\lambda`$ consists of marked elements in the same quotient fiber. The source fiber count bounds its size by $`|P:W|/2^{s_I}`$, so $`|C_P(\lambda)|\ge 2^{s_I}|W|`$. Its image in $`V`$ lies in $`C_V(t)`$, with kernel $`C_\Phi(\lambda)`$; use $`|W|=2^{h+u}`$. This gives a compatibility test between a marked action on $`\Phi`$ and its shadow. It is not an upper bound on $`r`$, and it does not use a quotient-folder assumption.

## Vanishing stabilizer-shadow core for the S₅ quotient

**Core-vanishing theorem with scoped independent reviews below.** In addition to the hypotheses at the start of this manuscript, assume $`A=S_5`$ and $`B=F_{20}`$. The conclusion is $`C=0`$. First we exclude copies of the four-dimensional principal simple module $`M`$ from its socle; we then exclude the other nontrivial simple $`N`$. Equation (4) already excludes a trivial submodule. No splitting of $`G`$ over $`P`$ is assumed.

Suppose for contradiction that $`C`$ contains a nonzero $`S_5`$-submodule $`D_0\cong M^n`$. Put $`E_0=\pi^{-1}(D_0)\le P`$, $`W_0=W\cap E_0`$, and $`R_0=C_P(E_0)`$, where $`\pi:P\to V`$ is the Frattini projection. Centrality and (3) make $`E_0=W_0\Phi`$ elementary abelian. The group $`R_0`$ is normal in $`G`$, contains $`E_0`$ and $`\Phi`$, and centralizes $`E_0`$. Commutation gives an $`S_5`$-equivariant injection


```math
P/R_0\hookrightarrow\mathop{\mathrm{Hom}}\nolimits_{\mathbb F_2}(D_0,\Phi),\qquad
 pR_0\longmapsto (x\mapsto[p,\widetilde x]), \tag{10}
```


where $`\widetilde x`$ is any lift of $`x`$ to $`E_0`$. This is well-defined because $`\Phi`$ is central, and its kernel is $`R_0`$. Since $`\Phi`$ is trivial and $`M`$ is self-dual, the target is a direct sum of copies of $`M`$; every submodule is likewise a direct sum of copies of $`M`$. Thus the reviewed $`H^2(S_5,M)=0`$ calculation in [the radical argument](bruck-s5-radical.md) at the recorded source revision splits $`G/R_0`$. The restriction $`M|F`$ is projective and $`M|\langle t\rangle`$ is free for a transposition $`t`$, so $`H^1(F,P/R_0)=H^1(\langle t\rangle,P/R_0)=0`$.

Since $`W\Phi`$ is elementary, $`W\le R_0`$, so $`HR_0/R_0`$ is a complement to $`P/R_0`$ over $`F`$. Vanishing of $`H^1(F,P/R_0)`$ lets us choose a complement $`A_0\cong S_5`$ in $`G/R_0`$ with $`HR_0/R_0=A_0\cap\bar\pi^{-1}(F)`$: the two $`F`$-complements are conjugate by an element of $`P/R_0`$, and $`\bar\pi:G/R_0\to A`$ is the quotient map. As $`R_0`$ centralizes $`E_0`$, this choice makes the actual $`W_0`$ stable under $`F\subseteq A_0`$. The quotient complement gives an $`A_0`$-module extension


```math
0\longrightarrow \mathbf1^r\longrightarrow E_0\longrightarrow M^n\longrightarrow0.
```


The reviewed module inputs in [the two-M support argument](bruck-s5-two-m-support.md), including its [one-M cohomology source](bruck-s5-principal-one-m.md) at the recorded source revision, give $`\dim H^1(S_5,M)=1`$; the invariant nondegenerate form in the six-point model makes $`M`$ self-dual. Its restriction to $`F_{20}`$ is the absolutely irreducible four-dimensional module $`S`$, with $`\mathop{\mathrm{End}}\nolimits_F(S)=\mathbb F_2`$, by the module inputs cited in the preceding manuscript. Thus $`\mathop{\mathrm{End}}\nolimits_{S_5}(M)=\mathbb F_2`$, and $`\mathop{\mathrm{Ext}}\nolimits^1_{S_5}(M,\mathbf1)\cong\mathbb F_2`$. The unique nonsplit extension is $`0\to\mathbf1\to J^*\to M\to0`$, where $`J=\mathbb F_2^6/\langle\mathbf1\rangle`$.

Consequently the extension class is an $`r\times n`$ binary matrix. After changes of bases in its kernel and quotient, write its rank as $`s`$, and decompose, compatibly with the actual kernel $`\Phi`$,


```math
E_0=E_{\rm act}\oplus\mathbf1^{r-s},\qquad
 E_{\rm act}=(J^*)^s\oplus M^{n-s},\qquad
 \dim(E_{\rm act}\cap\Phi)=s. \tag{11}
```


The actual $`W_0`$ is an $`F`$-stable complement to $`\Phi`$ in $`E_0`$. Its projection to the final trivial summand is an $`F`$-map from $`M^n`$ to a trivial module, and is therefore zero: $`\mathop{\mathrm{Hom}}\nolimits_F(M,\mathbf1)=0`$. Thus $`W_0\le E_{\rm act}`$, with codimension $`s`$. A transposition acts on the six points as three swaps; $`1+t`$ has rank three on the permutation module and its image contains the constants. It therefore has rank two on $`J`$ and, by duality, on $`J^*`$. It also has rank two on $`M`$, as in the six-point module control cited in [the extraspecial argument](bruck-extraspecial-radicals.md#rank-dichotomy-and-arbitrary-jj-multiplicities). Hence


```math
\dim((1+t)E_{\rm act}\cap W_0)\ge 2n-s\ge n>0. \tag{12}
```


It remains to connect this intersection to a selected marked element. The inversion automorphism fixes $`V`$, fixes $`W_0\subseteq H`$, and fixes $`\Phi`$ by (3), hence fixes $`E_0`$ pointwise. For every $`g\in G`$, the element $`\tau(g)g^{-1}`$ centralizes $`E_0`$, because $`g`$ preserves $`E_0`$. Its image in $`A`$ acts trivially on $`D_0\cong M^n`$, and the $`S_5`$-action on $`M`$ is faithful. Therefore $`\tau(g)g^{-1}\in R_0`$: $`\tau`$ acts trivially on $`G/R_0`$.

The source fiber theorem gives a selected marked involution $`\lambda`$ above a transposition $`t\in A_0`$. Because $`\tau`$ is trivial modulo $`R_0`$, there is a homomorphism from the marked group $`G\rtimes\langle\widehat\tau\rangle`$ to $`G/R_0=(P/R_0)\rtimes A_0`$ sending $`\widehat\tau`$ to the identity. The image of $`\lambda`$ has the form $`p_0t`$. The involution equation says $`p_0`$ is $`t`$-fixed; by $`H^1(\langle t\rangle,P/R_0)=0`$ it is a $`(1+t)`$-displacement. Conjugating $`\lambda`$ by a suitable element of $`P`$ removes it. The resulting selected marked element acts on $`E_0`$ as $`t`$, because its image under this homomorphism is $`t`$, $`R_0`$ centralizes $`E_0`$, and $`\tau`$ fixes it. By (12), choose $`x\in E_0`$ such that $`x\lambda'x^{-1}\lambda'^{-1}`$ is a nontrivial element of $`W_0`$, where $`\lambda'`$ is the conjugated marked element. Marked-class invariance puts both elements in $`\Lambda`$; their $`K`$-coordinates differ by a nonidentity element of $`W_0\le H`$, contradicting the folder transversal. This proves the proposed exclusion subject to the stated inputs.


Suppose instead that the socle of $`C`$ contains a submodule $`D_0\cong N^n`$, $`n>0`$. Define $`E_0,W_0,R_0`$ exactly as above. The same commutator injection puts $`P/R_0`$ inside a direct sum of copies of $`N`$, since $`N`$ is self-dual; write $`P/R_0\cong N^k`$. The reviewed [N-block argument](bruck-s5-module-blocks.md) at the recorded source revision gives $`H^2(S_5,N)=0`$, while $`N|F`$ is projective. As before, $`G/R_0`$ splits and a quotient complement $`A_0`$ can be chosen to make the actual $`W_0`$ $`F`$-stable. Also $`H^1(S_5,N)=0`$: the decomposition $`\mathbb F_2^5=\mathbf1\oplus N`$ and Shapiro reduce it to the fact that sign restricts nontrivially from $`S_5`$ to $`S_4`$; see [the radical argument](bruck-s5-radical.md). Thus $`\mathop{\mathrm{Ext}}\nolimits^1(N,\mathbf1)=0`$, and $`E_0=N^n\oplus\mathbf1^r`$ as an $`A_0`$-module. Since $`\mathop{\mathrm{Hom}}\nolimits_F(N,\mathbf1)=0`$, its actual $`F`$-stable complement $`W_0`$ is the $`A_0`$-stable $`N^n`$ summand.

As in the M case, $`\tau`$ fixes $`E_0`$ pointwise and induces the identity on $`G/R_0`$, because the action on $`D_0`$ is faithful. Fix a transposition $`t\in A_0`$. Project the marked involutions over $`t`$ to $`G/R_0`$; their radical coordinates give classes in $`H^1(\langle t\rangle,N^k)`$. The centralizer quotient $`C_{S_5}(t)/\langle t\rangle\cong S_3`$ acts on this space diagonally through its natural two-dimensional module on each factor. Thus an element of order three has no nonzero fixed vector. The selected marked fiber is invariant under lifts of the centralizer, so its nonzero-label fibers occur in triples of equal cardinality. Its total size is $`|P:W|/2`$, a positive power of two, by the source fiber theorem; it is not divisible by three. Therefore the zero label occurs. A $`P`$-conjugate of a selected marked element projects to pure $`t`$, and so acts on $`E_0`$ as $`t`$. Since $`t`$ acts nontrivially on the $`A_0`$-stable $`W_0`$, conjugation by a suitable element of $`W_0`$ gives the same marked-transversal collision as above. The $`S_3`$-action on $`H^1(\langle t\rangle,N)`$ is recorded with its reviewed input in [the N-block argument](bruck-s5-module-blocks.md#elimination-of-all-n-only-radicals). This includes $`k=0`$, when the only label is zero.

The simple $`\mathbb F_2S_5`$-modules are $`\mathbf1,M,N`$. A nonzero finite module has a simple socle, and the preceding arguments exclude all three possible socle types for $`C`$. Consequently $`C=0`$. Combining this with (8), every such central-Frattini $`S_5`$-envelope satisfies $`r\le\binom{B(S_5)m+1}{2}`$. This is a fixed-$`m`$ bound, not a numerical bound independent of $`m`$. The N-socle deduction and the resulting bound have the scoped independent reviews below.

If $`V\cong M^d`$, then $`U`$ is an $`F`$-submodule of $`M^d`$, and $`M|F`$ is absolutely irreducible with endomorphism ring $`\mathbb F_2`$. Thus $`U`$ is an $`S_5`$-submodule and $`C=U`$. If $`C\ne0`$, the preceding core-vanishing argument gives a contradiction. If $`C=0`$, then $`W\le\Phi`$ and corefreeness gives $`W=1`$. The source factorization $`P=WD`$ gives $`P=D\subseteq K`$; inversion therefore acts on all of $`P`$ as inversion, making $`P`$ abelian. Its square map $`V\to\Phi`$ is $`S_5`$-equivariant, and $`\mathop{\mathrm{Hom}}\nolimits_{S_5}(M,\mathbf1)=0`$; hence $`\Phi=P^2=1`$. For any lift $`g`$ of a transposition $`t`$, write $`\tau(g)=a g`$ with $`a\in V`$. The equation $`\tau(vg)=(vg)^{-1}`$ is the affine linear equation $`(1+t)v=a+g^2`$. It has at most $`2^{2d}`$ solutions, whereas the source fiber count with $`W=1`$ requires $`2^{4d-1}`$ section elements above $`t`$. This is impossible for $`d\ge1`$. Thus the proposed exclusion covers **all central-Frattini envelopes with $`V\cong M^d`$**, including nonsplit $`G`$; the Frattini-shadow source rules out $`d=0`$. This corollary and the quotient-complement proof have the scoped independent reviews below.

A failed local pattern explains why full marked-class invariance is needed. For $`C=M^n`$, $`V/C=M^2`$, and central $`\Phi=\mathbb F_2^{2n}`$, a class-two Heisenberg group built from the invariant pairing $`M\otimes M\to\mathbb F_2`$ has core-free stabilizer data and admits an individual transposition lift whose displacement on $`E_C`$ is disjoint from $`W_C`$. Nevertheless its selected conjugacy class contains another marked element with a collision, as the argument above shows. This is not a construction of a loop or an unbounded family of Bruck envelopes. The estimates (8)–(12) and the core-vanishing result have the scoped independent reviews below.

## Independent review of the S₅ core-vanishing theorem

Independent checks an independent check and an independent check independently accepted the cross-layer estimates, S₅ core-vanishing theorem and pure-M corollary at exact source the recorded source revision, conditional on the cited central-Frattini, marked-fiber and module/cohomology inputs. Both checked the commutator embedding, quotient splitting and normalization of the actual stabilizer, the M extension-matrix rank collision, and the N mod-3 argument with arbitrary marked-fiber multiplicities. Neither assumes a splitting of G over P. The conclusions do not establish centrality in general or bound m. These are independent mathematical argument reviews; no new computation or formal verification was used. They do not cover the following product extension, added after that source.

## Core vanishing for products of $`S_5`$

**Product theorem with scoped independent reviews below.** Assume the central-Frattini hypotheses and notation of this manuscript, with $`A=G/P\cong S_5^e`$ for any $`e\ge1`$, and retain the full faithful simple nonassociative Bruck-envelope hypotheses and source fiber results cited above. No exponent-two or exponent-four assumption is imposed. The conclusion is $`C=0`$. In particular, with $`d=\dim(P/\Phi)`$, $`r=\dim\Phi`$, and $`m`$ the number of nontrivial simple $`A`$-composition factors of $`V/C`$ counted with multiplicity, the reviewed core-reduced bound yields

$$d\le [1+2^e(3e+1)]\,|A|\,m,\qquad
r\le \binom{d+1}{2}.\tag{13}$$

The second inequality is the central-Frattini generator bound (8): squares and pairwise commutators of $`d`$ lifts span $`\Phi`$. Thus for fixed $`e,m`$, the order $`|P|=2^{d+r}`$ is bounded without treating $`r`$ as an independent parameter. Neither $`e`$ nor $`m`$ is bounded here. The argument does not cover products with other $`\mathop{\mathrm{PGL}}\nolimits_2(q_i)`$ factors or radicals with noncentral Frattini subgroup.

*Proof.* Suppose $`C\ne0`$. A nonzero finite module has a simple submodule; $`C^A=0`$ excludes the trivial simple. The simple $`\mathbb F_2S_5`$-modules $`\mathbf1,M,N`$ are absolutely irreducible under the module inputs cited in the preceding section. Consequently every simple $`\mathbb F_2A`$-module is an outer tensor product of these modules. To see this directly, the semisimple quotient of $`\mathbb F_2S_5`$ is a product of matrix algebras over $`\mathbb F_2`$. In the tensor product of the group algebras, the sum of the ideals obtained from their Jacobson radicals is nilpotent; its quotient is the tensor product of these split semisimple algebras, again a product of matrix algebras. This ideal is therefore the full Jacobson radical, and its simple quotients give exactly the stated tensor products. Choose a nontrivial simple $`D_0\le C`$ and an index $`i`$ on which it acts nontrivially. Restricted to $`A_i\cong S_5`$, $`D_0`$ is $`M^n`$ or $`N^n`$ for some $`n>0`$.

Let $`E_0`$ be the full inverse image of $`D_0`$ in $`P`$, $`W_0=W\cap E_0`$, and $`R_0=C_P(E_0)`$. Since $`D_0\le U`$ and $`W\cap\Phi=1`$, we have $`E_0=W_0\Phi`$, with $`W_0\cap\Phi=1`$. The previously established elementary nature of $`W\Phi`$ makes $`E_0`$ elementary and gives $`W\le R_0`$. The commutator pairing is the same as (10):

$$P/R_0\hookrightarrow\mathop{\mathrm{Hom}}\nolimits_{\mathbb F_2}(D_0,\Phi).$$

It is $`A`$-equivariant, since $`\Phi\le Z(G)`$. Restricted to $`A_i`$, its target is a direct sum of copies of the self-dual simple module $`M`$ or $`N`$; hence $`P/R_0`$ is likewise isotypic for $`A_i`$. The local cohomology and module facts used next are precisely those in the preceding $`S_5`$ section: $`H^2(S_5,M)=H^2(S_5,N)=0`$, the projective irreducible restrictions to $`F_{20}`$, the $`M`$ extension matrix and rank calculation, and the $`N`$ transposition cohomology action.

The inversion automorphism $`\tau`$ fixes $`E_0`$ pointwise, since it fixes $`W_0\le H`$ and the elementary central $`\Phi`$. It induces the identity on $`A`$: images of the generating section $`K`$ are involutions and are inverted by $`\tau`$. Thus $`\tau(g)g^{-1}\in P`$ for every $`g\in G`$, and this element centralizes $`E_0`$, so it lies in $`R_0`$. Hence $`\tau=1`$ on $`G/R_0`$. This argument does **not** require $`D_0`$ to be faithful for all of $`A`$, or $`C_G(E_0)=R_0`$.

Let $`G_i/R_0`$ be the full preimage of $`A_i`$ in $`G/R_0`$. The local extension by $`P/R_0`$ splits by the cited $`H^2`$ vanishing; no global splitting over $`A`$ is assumed. Embed $`B_i\cong F_{20}`$ as the $`i`$-th factor of $`\prod_jB_j=\pi(H)`$ and put $`H_i=H\cap\pi^{-1}(B_i)`$. Then $`H_i`$ maps onto $`B_i`$, and $`H_iR_0/R_0`$ meets $`P/R_0`$ trivially because $`H\cap P=W\le R_0`$. The cited projective restrictions give $`H^1(B_i,P/R_0)=0`$, so an $`A_i`$ complement in $`G_i/R_0`$ may be chosen containing $`H_iR_0/R_0`$. This complement acts on $`E_0`$ because $`R_0`$ centralizes $`E_0`$, and its $`B_i`$ subgroup stabilizes $`W_0`$. No complement lift to $`G`$ is required.

If $`D_0|_{A_i}=M^n`$, apply the preceding $`S_5`$ local extension calculation to $`0\to\Phi\to E_0\to M^n\to0`$: for a transposition $`t_i\in A_i`$, $`\mathop{\mathrm{im}}\nolimits(1+t_i)\cap W_0\ne0`$. The product fiber theorem supplies a marked involution above the singleton element $`t_i`$ (identity in all other factors). In the split local quotient its radical coordinate is $`t_i`$-fixed. Since $`H^1(\langle t_i\rangle,M^k)=0`$ for $`P/R_0\cong M^k`$, conjugation by an element of $`P`$ makes its quotient image the pure complement $`t_i`$. Its action on $`E_0`$ is then $`t_i`$, since $`R_0`$ and $`\tau`$ centralize $`E_0`$. The nonzero displacement into $`W_0\le H`$ produces the same marked-transversal collision as in the preceding section.

If $`D_0|_{A_i}=N^n`$, the preceding local calculation gives $`E_0=N^n\oplus\mathbf1^r`$ and $`W_0=N^n`$: $`\mathop{\mathrm{Ext}}\nolimits^1(N,\mathbf1)=0`$ and $`\mathop{\mathrm{Hom}}\nolimits_{B_i}(N,\mathbf1)=0`$. The singleton marked fiber over $`t_i`$ has size $`|P:W|/2`$, a positive power of two, by the product fiber theorem. Since $`\tau=1`$ on $`G/R_0`$, the external marked group maps to that quotient with $`\widehat\tau\mapsto1`$. Projecting this fiber into the split local quotient gives labels in $`H^1(\langle t_i\rangle,N^k)`$. Lifts to $`G`$ of the $`S_3`$ factor of $`C_{A_i}(t_i)`$ in the local complement preserve the whole actual marked fiber and biject label fibers. Every nonzero $`S_3`$-orbit on the cohomology labels has size $`3`$ or $`6`$, so if the zero label were absent the total fiber size would be divisible by $`3`$, regardless of multiplicities. The zero label therefore occurs, including when $`k=0`$. A $`P`$-conjugate of a selected marked element then projects to pure $`t_i`$ and acts on $`E_0`$ as $`t_i`$. Its nonzero displacement on the $`A_i`$-stable $`W_0`$ gives the same collision.

Both possible nontrivial factor types lead to contradictions. Thus $`C`$ contains no nontrivial simple submodule; the trivial simple is excluded by $`C^A=0`$. Therefore $`C=0`$, and (13) follows. $`\square`$

Independent checks an independent check and an independent check independently accepted this product extension at exact source the recorded source revision, conditional on the cited central-Frattini, module/cohomology and product-fiber inputs. Both checked the split tensor-simple argument, use of a single local quotient complement, the actual stabilizer image, the inversion action without global faithfulness, and both marked-fiber collisions with arbitrary multiplicities. Their scope includes the bounds in (13), not a bound on e or m, other quotient factors or noncentral Frattini subgroups. Reviewer an independent check also checked the companion single-S₅ parameter-removal corollary at that source; the second review covers the product theorem and bounds only. No new computation or formal verification was used.

