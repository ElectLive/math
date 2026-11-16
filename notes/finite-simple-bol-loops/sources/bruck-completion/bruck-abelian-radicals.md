# Abelian radicals in finite Bruck envelopes

**Deductions with the scoped independent reviews below.** Let (G,H,K) be the faithful canonical Baer envelope of a finite simple nonassociative right Bruck loop X of 2-power exponent, with abelian P=O₂(G), W=P∩H and D=P∩K. No exponent bound of 2 or 4 is assumed. This continues [C0010](../../claims/0010.md), with no new claim ID. The Bruck-envelope results of Baumeister–Stein, [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5, supply the inversion automorphism τ, τ|H=1, τ(k)=k⁻¹, P=WD and the stated quotient and fiber descriptions. The corresponding P=WD locator is Lemma 4.3 in v2. The [Frattini-shadow manuscript](bruck-frattini-shadow.md) records acceptance of its initial constraints at the recorded source revision; its core and all-support bounds have the separate acceptance at the recorded source revision. The elementary product input is reviewed at the recorded source revision. These are input reviews; the separate reviews below cover this manuscript.

## Inversion and the radical section

The image of K in G/P consists of involutions and identity and generates G/P. Since τ inverts K, τ induces the identity on G/P. As P is abelian, τ|P therefore commutes with conjugation by G: if g∈G, the elements g and τ(g) differ by an element of P, which centralizes P. Use additive notation in P. The factorization P=WD, τ|W=1 and τ(d)=−d for d∈D give


```math
(1+\tau)P=2W\le W.
```


The left side is G-invariant. It lies in H, so core-freeness forces it to vanish. Thus


```math
2W=0,\qquad \tau|_P=-1.                                    \tag{1}
```


For p∈P and d∈D, twisted conjugation in the formal extension by τ sends d to d−2p. Hence D is stable under translation by 2P, and 0∈D gives 2P⊆D. Because D is a transversal to W in P, W∩2P=0. It follows that D/2P is an exact transversal to W̄=W2P/2P in P/2P.

If X has exponent 2, every element of K is an involution, so τ fixes the generating set K pointwise and τ=1 on G. Equation (1) gives 2P=0. Therefore **every abelian radical P in a faithful exponent-2 Bruck envelope is elementary abelian** under the cited factorization and core-freeness hypotheses. This implication does not require the simplicity assumption used in the later parts of this manuscript. It does not establish that every radical is abelian.

## Higher-power layers

Return to the general 2-power-exponent setting, still assuming simplicity and the cited product quotient A=G/P, with A′=∏PSL₂(qᵢ). Since P is abelian, Φ(P)=2P. The reviewed Frattini functional-injection argument at the recorded source revision gives


```math
\overline W+[P/2P,A′]=P/2P.
```


Consequently P=W+[P,A′]+2P. The finite abelian 2-group P/(W+[P,A′]) is equal to twice itself and is therefore zero, so P=W+[P,A′]. Since 2W=0,


```math
2P=2[P,A′]=[2P,A′],\qquad
2^jP=[2^jP,A′]\quad(j\ge1).                                \tag{2}
```


Thus every nonzero layer 2^jP/2^{j+1}P has no nonzero A′-trivial quotient. This is a necessary module condition, not an assertion that all its composition factors are nontrivial or that P is elementary.

## The S₅ quotient and shadow defect

Suppose in addition A≅S₅. If 2P≠0, the elementary module 2P/4P is nonzero and has no trivial S₅ quotient by (2). The only simple F₂S₅-modules are 1,M,N, with dim M=dim N=4, by Nagy, [arXiv:0709.4544v1](https://arxiv.org/html/0709.4544v1), Lemma 4.1. Hence dim(2P/4P)≥4 and |2P|≥16.

For a transposition t, P-twisted conjugacy moves each element of the t-fiber through a coset of (1+t)P. If 2P⊆(1+t)P, that entire fiber is 2P-periodic; conjugacy gives the same for all ten transposition fibers. As D is also 2P-periodic, 2P·K=K. Now 2P is normal in G, W∩2P=0, and H(2P)<G because its image in S₅ is F₂₀. The image of K modulo 2P would therefore be a transversal yielding a proper nontrivial loop quotient, contrary to simplicity. Thus, whenever 2P≠0,


```math
2P\not\subseteq(1+t)P\quad\text{for every transposition }t. \tag{3}
```


This necessary condition alone does not prove elementaryness: for the free Z/4 swap module the subgroup 2P is not contained in (1+t)P.

More generally, return to any of the product quotients A above. Let V=P/2P, W̄=W2P/2P and n=|V:W̄|. Since D/2P is an exact transversal, its shadow cardinality is exactly n. For each nonempty component support I, use the notation r_I, ρ_I and s_I from the reviewed [all-support shadow bounds](bruck-frattini-shadow.md#core-reduced-module-and-all-support-shadow-bounds) at the recorded source revision. If 2P≠0, strict total shadow overlap and the individual lower bounds force at least one nonempty I to satisfy


```math
r_I>n/2^{s_I},\qquad \rho_I\le\dim\overline W+s_I-1.       \tag{4}
```


Indeed, if every r_I attained its lower bound, adding the radical cardinality n would make the total shadow section size equal its coset index, contrary to simplicity. The rank bound follows from the shadow upper bound r_I≤2^{dim V−ρ_I} and n=2^{dim V−dim W̄}. For a single PGL₂(q) factor there is only one nonempty support, so (4) applies to it. In the S₅ case q=5 and s_I=1, giving the one-unit improvement ρ_t≤dim W̄ over the general bound ρ_t≤dim W̄+1. These are conditions on an overlapping shadow section, not a claim that it is a quotient folder.

The higher-exponent conditions do not exclude abelian non-elementary radicals or construct a simple example. The general nonabelian-radical branch is untouched. The scoped reviews below cover these deductions.

## Head and mixed-exponent obstructions

**Deductions with scoped independent review below.** Continue under the abelian-radical and simple-envelope hypotheses above, and suppose 2P≠0. Put V=P/2P. Multiplication by 2 induces a surjective A-module map


```math
V\longrightarrow 2P/4P,\qquad p+2P\longmapsto2p+4P.
```


Its target is nonzero and has no nonzero A′-trivial quotient by (2). Every A-simple module on which A′ acts trivially is trivial, because A/A′ is a 2-group and the group algebra is over F₂. Thus **V must have a nontrivial simple quotient**: if its head contained only trivial simples, every nonzero quotient of V would have a trivial simple quotient, contradicting the target's property. This condition applies to every allowed product A and does not require the Frattini shadow to be a folder.

For A=S₅, the six-point quotient J has unique simple head 1; the same is true of each 1 or R=F₂C₂ summand. Hence V cannot be J⊕1ᵘ⊕Rᵛ when 2P≠0. In particular an integral Z/4 lift whose mod-2 module is J cannot occur, regardless of the choice of doubling layer. This does not exclude modules with nontrivial simple heads.

There is a separate S₅ obstruction to homocyclic P. The reviewed Frattini action in [bruck-frattini-shadow.md](bruck-frattini-shadow.md#faithful-shadow-action) is faithful, so a transposition t acts nontrivially on V. The strengthened q=5 shadow bound (4) gives rank(1+t|V)≤dim W̄; thus W̄≠0. If P≅(C_{2^k})^r with k≥2, every involution of P lies in 2P. But W is elementary by (1) and W∩2P=0, forcing W=0, a contradiction. Thus any abelian non-elementary radical in the S₅ branch has mixed cyclic exponents and at least one C₂ direct factor. This homocyclic exclusion is asserted only for S₅; the rank estimate above does not establish it for the other PGL₂(q) factors.

In the same S₅ setting, dim(2P/4P)≥4 by the preceding section. The doubling map's kernel contains W̄, which has dimension at least one, so dim V≥dim(2P/4P)+dim W̄≥5. Therefore


```math
|P|=|P/2P|\,|2P|\ge2^5\cdot2^4=2^9.                  \tag{5}
```


Equivalently, the cyclic decomposition has at least four factors of order at least 4 and at least one of order 2. These are necessary conditions and do not construct or exclude all mixed-exponent radicals. The head and homocyclic deductions have the scoped independent reviews below.

## Independent review

Independent checks an independent check and an independent check independently accepted this manuscript through (5) at exact source the recorded source revision, conditional on its cited Baumeister–Stein and previously reviewed product and Frattini-shadow inputs. Both checked inversion on the abelian radical, the core-free image argument, radical periodicity, higher-layer coinvariants, strict shadow overlap, the nontrivial-head obstruction, and the S₅ homocyclic exclusion and mixed-exponent lower bound. The latter reviewer relied on the earlier direct inspection of Baumeister–Stein v1 Lemmas 3.2, 3.4 and 4.1–4.5. Neither review proves elementaryness for all abelian radicals, treats arbitrary nonabelian radicals, or supplies a classification. No computation or formal verification was used.

## Further norm-image constraint

**Deduction with scoped independent review below.** For each nonempty quotient support I and an element t in its prescribed outer class, let s_I be the fiber exponent from the product constraints. Since P is abelian and τ=-1 on P, twisted conjugation by p∈P changes a chosen section lift k over t to ((1+t)p)k. Thus the entire fiber is a union of cosets of (1+t)P, and transversality forces

    W∩(1+t)P=0.

Indeed a nonzero norm in W gives two selected lifts in the same right-folder H-coset. The original source fiber size is |P:W|/2^{s_I}. Its orbit size is |(1+t)P|, and the full inversion equation, relative to one selected lift, has solution space C_P(t). Hence

    |ker(1+t on P)| ≥ 2^{s_I}|W|,
    |P| ≤ 2^{s_I}|W|·|C_P(t)|.

These are necessary conditions in the original envelope, not assertions about a quotient folder. They neither classify the mixed-exponent radicals nor imply the conditions are sufficient.

Independent checks an independent check accepted the norm-image intersection and both counting inequalities at exact source the recorded source revision, conditional on the previously reviewed inversion result and original fiber formula. The reviewer checked the coset collision, norm-orbit count and full inversion solution bound. No sufficiency, classification, computation or formal verification is claimed.

