# Inversion exhaustion for nonpermuting A5-socle envelopes

**Mira Cult**

**Independently reviewed theorem under the pinned inputs.** A manuscript-local continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Let `(G,H,K,τ)` be the faithful generated canonical folder of a finite simple nonassociative Bol loop. Suppose `Soc(G)=N=A5^r`, no element of G permutes the simple factors, and G is the inverse image of a binary sign code `C≤F2^r` in `S5^r`. Let τ induce an involutory permutation of the r factors. No full-mark, nonzero-code-character, τ-fixed-point-free, or residual-independence hypothesis is imposed. Write `H0=H∩N`.

**Theorem.** Under the pinned interfaces below, τ fixes no simple factor of N. Thus r is even, τ pairs all factors, and the [reviewed paired parity-code construction and isomorphism classification](radical-free-a5-outer-codes.md#arbitrary-selected-marks-for-paired-nonpermuting-a5-codes) applies. This classifies the entire stated nonpermuting A₅-socle setting, without an initial hypothesis on canonical inversion. It does not classify factor-permuting canonical groups or other socles.

We first prove a structural reduction: the full-strip/paired-edge graph of H0 is a disjoint union of paths, each with either two proper paired-coordinate leaves and no fixed full coordinate, or one proper paired-coordinate leaf and one fixed full coordinate. No full strip contains two τ-fixed coordinates. Each component has a common coordinate sign functional on C. If a one-fixed-leg path has zero component functional, its actual proper leaf projection is `A4`, its H0 leaf projection is `A4`, its fixed local τ restriction is nontrivial inner, and every selected outside mark is a double transposition on that fixed coordinate. If its component functional is nonzero, its actual proper leaf projection is `F20=AGL1(5)` and its H0 leaf projection is `D10`.

At every τ-fixed coordinate i whose H0 projection is proper, independently of the graph, the following local alternatives hold. If its coordinate sign functional is zero, `π_i(H0)=π_i(H)=A4`, the restriction of τ is nontrivial inner, and every selected outside mark is a double transposition locally. If its sign functional is nonzero, `π_i(H0)=D10` and `π_i(H)=F20`. A proper τ-fixed coordinate does not belong to the paired-edge graph; retain it separately rather than treating it as a paired leaf.

The graph and local screens are intermediate statements; the final global argument excludes all their fixed-coordinate cases. Throughout, no identification of `π_i(H0)` with `π_i(H)∩A5` is assumed.

## Inputs and elementary character data

Use the faithful generated-folder, all-conjugate transversal and exact normal-quotient criterion in C0001 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), and canonical inversion and conjugacy-invariance of `Λ=tK` in C0007 at [the source revision](https://github.com/Mira-Cult/math-wip/commit/932ead5db5f39045e2085caa6b062f6b981b2813). The parity-code and no-factor-permutation interfaces, including the fact that τ fixes every codeword and H maps onto C by simplicity, are those in `radical-free-a5-outer-codes.md` at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6f2d59373993da9afb5101cd5c82e534ad684906). The H0 full-strip splitting and actual H-normalizer method are as in the outer-code source's reviewed path theorem at [the source revision](https://github.com/Mira-Cult/math-wip/commit/8f7cfada6d692e16fb6966c7333b337898e78bda); A5 subgroup, automorphism and involution inputs are pinned in `radical-free-a5-path-classification.md` at [the source revision](https://github.com/Mira-Cult/math-wip/commit/ad94accf574f89bf1e8487bb046cf30fb685cd0c). The local S5 normalizer/character calculations below are elementary and are stated explicitly; these input citations do not independently review the new deductions.

For every nontrivial τ-stable irreducible representation of G extended to `G⋊<t>`, the class sum `Σ_{λ∈Λ}ρ(λ)` is a scalar. If it is nonzero, the representation has no H-fixed vector: this follows from the transversal identity `(Σ_K k)(Σ_H h)=Σ_G g`; inverse closure of K handles either transversal orientation. This uses actual H and actual Λ, not a projected folder.

Let `ψ=sgn⊗(permutation character of S5 on its six Sylow-5 subgroups −1)`. The restriction to A5 is its real irreducible degree-five character. On S5 cycle types `1, 2, 2², 3, (3)(2), 4, 5`, ψ has values `5,1,1,−1,1,−1,0`, respectively, with class sizes `1,10,15,20,20,30,24`. These values follow by counting membership in F20: its nonidentity elements are five double transpositions, ten 4-cycles and four 5-cycles, so the six-point fixed counts are 2, 2 and 1 on those types and zero on the other nonidentity types. Hence `⟨ψ²,1⟩=⟨ψ³,1⟩=1`, and every tensor power `ψ^⊗d` with `d≥2` has an S5-invariant, by multiplying bilinear and cubic tensors. At a τ-fixed coordinate the local marked involution is identity, double transposition or transposition. Their ψ orbit-class scalars are `1,3,2` respectively. The natural deleted five-point character `χ4` has local scalars `1,0,5`, respectively. Its cycle-type values are `4,2,0,1,−1,0,−1`; the same class-size average gives a bilinear and a cubic invariant, hence an S5-invariant tensor in every degree at least two. For a paired edge whose two coordinates carry the same irreducible of degree d, either sign orbit contributes scalar `60/d`; trivial labels contribute the orbit size 60. All these scalars are nonnegative, and the ψ scalars are positive. A selected outside N-class contributes a product of these local scalars, so code correlations cannot cancel positive terms.

An H0 full-coordinate projection decomposes into independent full twisted diagonal A5 strips, with solvable proper-coordinate residual. H normalizes H0. Because H does not permute factors, the normalizer induces the same S5 automorphism on all coordinates of a strip after straightening its twists. Hence an S5-invariant tensor on that strip is invariant under actual H, not just H0. Since H maps onto C, all coordinate sign functionals on a strip agree. The two coordinates of any τ-pair also have the same functional because τ fixes C pointwise.

## Fixed coordinates on strips and the graph

No full H0 strip carries two τ-fixed coordinates. Put ψ on precisely those two coordinates and trivial representations elsewhere. Their strip supplies an actual-H-invariant bilinear tensor, while every actual selected outside N-class contributes a strictly positive scalar. This violates the class-sum identity.

Make a multigraph with one vertex for each original full H0 strip and one vertex for each proper coordinate belonging to a τ-pair; a τ-pair gives one edge. Attach a τ-fixed full coordinate as a leg to its strip. A proper τ-fixed coordinate lies outside the graph. Each strip has support size at least two by faithfulness/core-freeness and at most one fixed leg, hence meets a paired edge. Each connected component has one common code functional `f`, and each strip factor splits from the proper residual. No assumption is made that proper residual projections in different components are independent.

Every component has a proper paired leaf. Otherwise put ψ on both coordinates of all its paired edges and on all of its fixed legs, and the trivial representation elsewhere. Every strip has at least two labeled coordinates and supplies an S5-invariant tensor fixed by actual H. The class-sum scalar is strictly positive on every selected global outside N-class: paired factors contribute `60/5`, fixed legs contribute `1,3,2`, and all remaining factors contribute positive orbit sizes. Contradiction.

For a component let `n,m,ell,b` count paired edges, full strips, proper paired leaves, and cycle rank `b=n−m−ell+1≥0`. Let `a,u` count its fixed full legs on which τ restricts to an inner/id, respectively outer, automorphism. Let `ε=0` if f=0 and `ε=1` otherwise. Its coordinate projection `G_C` has order `2^ε60^(2n+a+u)`. Bound the **actual projected H**, not a hypothetical projected folder: its local even kernel normalizes each full strip, whose even normalizer is that strip, and on a proper coordinate lies in the proper A5 normalizer of the H0 coordinate projection, of order at most 12. If that H0 projection is trivial, the coordinate image is a quotient of the elementary abelian 2-group H/H0 and has even part of order at most 4. Consequently `|H_C|≤2^ε60^m12^ell`.

A paired edge contributes at most 60 marked elements for each common code bit. For bit zero the inner/id fixed legs contribute at most 16 each and the outer fixed legs at most 10 each; for bit one these roles reverse. Thus

`|K_C|≤60^n(16^a10^u+ε·10^a16^u)`.

The projected cover `H_C K_C=G_C` gives

`60 ≥ 5^ell 60^b · 60^(a+u)/(16^a10^u+ε·10^a16^u)`.      (1)

Here `ell≥1`. The denominator is at most `2·16^(a+u)`, so b≥1, ell≥3, or a+u≥3 is impossible in (1). Checking the remaining a+u≤2 and ell≤2 possibilities, together with the full-strip degree bound `ell+a+u≥2` when `b=0`, gives `b=0`, `ell≤2`; for `ε=0` the only possibilities `(ell,a+u)` are `(2,0),(1,1)`, and for `ε=1` they are `(2,0),(1,1),(2,1),(1,2)`. Thus all components are trees; only the last two are potential three-ended components.

## Excluding the three-ended components

In these two cases ε=1. Let Q be the image on proper leaves of the actual local-even kernel of `H_C`. The projection of H0 to those leaves is normal in Q, and the quotient is elementary abelian 2, since `H/H0≤C`. The actual H action on full strips is bounded by `60^m`; no equality with the image of H0 is asserted.

For `(ell,a+u)=(2,1)`, the cover and the bound `|K_C|≤26·60^n` give `|Q|≥3600/26>120`. Each proper even leaf normalizer has order at most 12, so both must be A4; `Q≤A4²` and its order divides 144, hence `Q=A4²`. Since f is nonzero and H maps onto C, each actual H leaf projection contains an odd normalizer of A4 and is S4. Put χ4 on every component coordinate. Each strip has an actual-H-invariant S5 tensor and both S4 leaves fix vectors. Its scalar is a sum of nonnegative terms, so every selected global class must have a double transposition at the sole fixed leg. Its local marked parity is therefore always even. But the nonzero component bit takes both values among K, since K generates C, and changing it changes this local parity. Contradiction.

For `(ell,a+u)=(1,2)`, the cover gives `|Q|≥3600/(16²+10²)>10`, so Q=A4 and the actual H leaf projection is S4. The same χ4 tensor forces every selected global class to have a double transposition at at least one of its two fixed legs. If the two restrictions of τ have the same parity, one value of f makes both local marks odd transpositions, giving a positive χ4 term; K realizes both values. Thus the restrictions have opposite parity. For each bit, the odd local mark is a transposition and the other is even, forced by χ4 to be a double transposition. Since each selected global outside N-class contains its entire N-orbit, the actual projected mark set has exactly `150·60^n` elements in each of the two code bits: `|K_C|=300·60^n`. Here `n=m`, so the cover and `|H_C|≤2·12·60^m` give equality `|H_C||K_C|=|G_C|`.

If the component coordinates form a proper normal quotient, this equality violates the pinned strict normal-subloop criterion. If they comprise all coordinates, there are no other proper residual coordinates: the H0 leaf image contains `Q'=V4` because Q modulo that image is elementary abelian 2, and full strips split from the residual. Choose a leaf involution and an involution on every full strip. Both fixed legs are active in every selected class, and every paired edge has matching involutions; independent N-conjugation in an actual selected global class realizes their nonidentity product in `H0∩Λ²`, contradiction. This final collision uses a leaf lift only when there are no other residual coordinates. The three-ended components are excluded, proving the path assertion.

## Leaf and proper fixed-coordinate screens

For a one-fixed-leg path, put ψ on every component coordinate. Its full-strip tensors are actual-H-invariant and its scalar is positive, so its actual proper leaf projection J has no ψ-fixed vector. If the H0 leaf projection is trivial, J is elementary abelian 2 and fixes a ψ vector. Otherwise J normalizes a nontrivial proper A5 subgroup. The elementary subgroup check below shows that the only possibilities are `J=A4,S4,F20`; the elementary-2 quotient condition then gives H0 leaf projection `A4,A4,D10`, respectively. If the component functional is zero, J is even and hence A4. If it is nonzero, J is odd and hence S4 or F20.

Both A4 and S4 fix a χ4 vector. If J is either, label the entire path by χ4. Every selected global class must then have a double-transposition mark at its fixed leg, because all local scalars are nonnegative. A nonzero component functional takes both values on K, so this constant-even marked parity is impossible. Thus the nonzero-functional case has `J=F20` and H0 leaf projection `D10`. The zero-functional case has `J=H0_leaf=A4`, all selected marks double locally, and τ must restrict to a nontrivial inner involution, since the mandatory class `t^N` has local marked representative `t`.

For a proper τ-fixed coordinate i, let `J=π_i(H)`, `L=π_i(H0)<A5`. Label only i by ψ. Every selected outside class gives strictly positive scalar, so ψ has no J-fixed vector. The relevant elementary normalizers are: a C2 subgroup has normalizer D8; a C3 or S3 subgroup normalizes a characteristic C3 with normalizer S3×C2; a V4 or A4 subgroup has normalizer S4; and a C5 or D10 subgroup has normalizer F20. For L=1, J is elementary abelian 2. Character averaging gives ψ-fixed dimension one on D8, S3×C2, D10 and C4, and zero on A4, S4 and F20. The maximal proper subgroups of F20 are D10 and C4; proper subgroups of S4 avoiding A4 lie in D8 or S3. It follows that J is A4, S4 or F20. Since J/L is elementary abelian 2, the corresponding L is A4, A4 or D10: for F20, commutators and squares generate D10.

If i has zero code functional, J=L=A4. Its χ4 fixed vector and nonnegative χ4 scalars force every selected mark to be double locally, and the mandatory `t^N` mark makes τ's restriction nontrivial inner. If the functional is nonzero, J is odd. The possibility J=S4 is eliminated by χ4: selected K codewords realize both local signs, so at least one selected local mark is a transposition and contributes a positive scalar, whereas χ4 has an S4-fixed vector. Thus J=F20 and L=D10. These local claims concern the original H and H0; no unproved intersection-of-projections identity is used.

## Fully active selected classes and character moments

Retain all correlations in the actual proper-coordinate residual R of H0. Let c count ordinary paths with two proper leaves, z count fixed coordinates with zero code character, and u count fixed coordinates with nonzero code character. Each fixed coordinate is either proper itself or the fixed full leg of its path; call either case a fixed unit. Its residual coordinate is A4 in the zero-character case and D10 in the nonzero case. Ordinary paths have one C5/D10 endpoint and one C3/S3/A4 endpoint by the actual-mark degree-four and degree-five screens in the [paired arbitrary-mark proof](radical-free-a5-outer-codes.md#arbitrary-selected-marks-for-paired-nonpermuting-a5-codes), reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/820e678f92b42fe80d9e6c47cfd7e3afe3536815). Those screens label only the ordinary path, so the additional fixed coordinates contribute positive orbit-size factors and do not affect them. Let r count its A4-opposite paths, s=c−r the others, and k=dim C.

Let p count all τ-pairs, m all full strips, and F the sum of the actual selected N-orbit weights after removing the common factor 60^p. Every zero-code fixed unit always has the double-transposition class. Thus

 |K|=60^p F,     F=15^z F′.

At each of the u other fixed coordinates the local class weights are 1,15,10 for identity, double transposition, transposition. A codeword and these fixed local choices specify one N-orbit; no full-mark assumption is made. The path identity p−m=c, including the isolated proper fixed coordinates separately, gives

 |R|=60^(c+z+u)/(15^z F′).                                      (2)

Use now the **untwisted** deleted-six representation θ, with values 5,1,−1 on the three local fixed classes. For any nonempty subset of the u nonzero fixed units, label those proper fixed coordinates and the entire corresponding fixed-leg paths by θ, trivially elsewhere. Each residual F20 projection fixes a θ vector, because it fixes its Sylow-5 point; each full strip on a path supplies an actual-H-invariant bilinear tensor. Thus the representation has an H-fixed vector. Its nonempty mixed marked-class moment must vanish. Precisely, the pair orbit scalars contribute positive constants 60/5 rather than 60 on labeled edges, and the fixed orbit scalars contribute the orbit weight times θ/5. Removing these constants gives

 Σ_selected w · ∏_{i∈J} θ_i = 0     for every nonempty J⊆{1,…,u},  (3)

where w is the product of the u fixed local weights after removing the common 15^z. This uses the actual selected classes; neither their code distribution nor the residual subgroup is assumed independent.

Expanding ∏(5−θ_i) in (3), its weighted sum is 5^u F′. Locally the weighted factors are 0,60,60 for identity, double transposition, transposition. Call a mark **fully active** when none of its fixed local classes is identity. For each codeword there is at most one such mark: every even fixed class must be double and every odd fixed class must be a transposition; the zero-character fixed classes are already double. Let D*⊆C consist of codewords whose fully active class is selected. Then

 5^u F′=60^u |D*|,   F′=12^u |D*|,
 |R|=60^c 4^z 5^u/|D*|.                                      (4)

For u=0 the same formula is the identity F′=|D*|. In every case D* is nonempty, but at this stage it need not contain zero or span C. We shall use only D*⊆C and the existence of an actual fully active selected class.

## Global support and the two Sylow deficits

Fix one fully active selected N-class. At every fixed coordinate its square contains the identity and the unique A5 involution class: two disjoint transpositions give a double transposition, and two commuting double transpositions do likewise. At every paired edge its square contains any pair of involutions with matched support; the required even or odd conjugator exists since an A5 involution has an odd S5 centralizer element. Consequently an involution in R that has matched support on every ordinary path gives a collision after filling the independent full strips: a fixed-leg path may have either active or inactive residual support, since its fixed local class is active. Isolated proper fixed coordinates are equally unrestricted. This supplies actual global collisions without lifting a component projection in isolation.

Put a=v₂(|D*|), b=v₃(|D*|). A Sylow-2 subgroup P of R is elementary abelian, since every residual endpoint Sylow subgroup is C2 or V4. Equation (4) gives |P|=2^(2c+2z−a). The matched-support parity expansion constrains only the c ordinary leaf pairs. Each term imposes identity on at most one endpoint per ordinary path; its projection target has order at most 4^r2^s=2^(2c−s). If a<s+2z, every such kernel is even. The count of matched-support elements, including the identity, is therefore even, forcing a nonidentity global collision. This is the [reviewed support-parity argument](radical-free-involution-support.md) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e30af949531c0ebcc9f7533b04fc1e7fc6858563), applied with all fixed units unconstrained. Hence

 a≥s+2z.                                                       (5)

Let W5 be R's intersection with the product of the characteristic C5s at its c ordinary first endpoints and u nonzero fixed units. It is the actual normal Sylow-5 subgroup, possibly correlated. Set X=R/W5. It embeds in

 F2_D^(c+u) × A4^(r+z) × ∏_{i∈S}(C3 or S3),

with a trivial D-sign coordinate at an ordinary C5 endpoint. Let Q be a Sylow-3 subgroup of X. It embeds into the c+z opposite-endpoint C3 coordinates, projects nontrivially onto every one, and has rank c−b by (4). Thus the space of relations between those coordinate characters has dimension z+b.

Let P0=X∩(F2_D^(c+u)×V4^(r+z)×1_S), E=P0∩V4^(r+z). The commutator X′ is abelian inside V4^(r+z)×C3^s and projects onto each V4 coordinate. Its 2-primary part lies in E and has those full projections. Q acts trivially on D-signs and nontrivially irreducibly on every V4 coordinate. Odd-order averaging therefore gives

 P0=U_D⊕E,    U_D=P0∩F2_D^(c+u).

For each d∈C choose an actual H lift h. Its sixth power lies in H0. At an F20-normalized first endpoint or nonzero fixed unit its D-sign is the corresponding bit of d; at an ordinary S3/C3 opposite endpoint its sixth power is identity, since its normalizer S3×C2 has exponent six; at an A4 endpoint the sixth power is in V4. Removing the independent strip factors, passing to X and averaging over Q supplies the pure D-sign vector d in U_D. Evaluation on these c+u first/unit coordinates embeds C, since all other coordinate characters are either equal along a path or zero. Thus C≤U_D as an actual binary subgroup.

Partition the A4 coordinates into Q-isotypic blocks, grouping nonzero homomorphisms Q→C3 up to inversion. Each block of n_j coordinates carries an F4-linear subspace E_j with full projection onto each coordinate. Its coordinates have a common code character: for any h∈H, multiply by an H0 lift from X to make its induced action normalize Q, using Sylow conjugacy. At an A4 coordinate the induced automorphism of A4/V4 inverts C3 exactly when that coordinate's S5 parity is odd. Proportional Q characters therefore have the same parity for every actual H lift. The adjustment is even and leaves the code unchanged. This is the sign of the permutation action on the three nonzero V4 vectors, not a determinant over F2.

A block meeting t_j zero-code fixed units has code character zero everywhere. It must also contain at least one ordinary A4 coordinate: otherwise any nonzero vector in E_j would be supported only at fixed units and give a collision of the preceding kind. To lift that vector from X through the odd normal W5, take an involution in its preimage; all zero D-sign coordinates then lie in C5 and must be the identity. The lift preserves all opposite coordinates, and the independent strips may be filled on the active fixed-leg paths. Thus a block meeting t_j fixed units has at least t_j+1 coordinates and contributes at least t_j independent signed coordinate-character relations. Summing these disjoint blocks reserves at least z relations.

Among blocks with nonzero code character, call a block bad if E_j has no vector nonzero at all of its coordinates. A bad block has n_j≥2. Their code characters restricted to C0=ker(C→F2^S) must span C0*. Otherwise choose 0≠d∈C0 annihilating every bad character. The pure D-sign vector d lies in U_D. In each active good block choose a full-support E_j vector, and set E to zero on all inactive and zero-character blocks. This matches the ordinary A4 leaf supports; the ordinary S leaves are inactive by d∈C0. Fixed nonzero D-signs may have arbitrary support because the selected class is fully active. Lift through W5 as above and fill the full strips, obtaining a forbidden nonidentity global involution. Consequently the number of bad blocks is at least dim C0≥k−s.

A block of n_j proportional Q characters contributes n_j−1 independent signed coordinate relations. The nonzero-character bad blocks are disjoint from the zero-character fixed-unit blocks already charged z relations. The total relation budget therefore gives

 z+b≥z+(k−s),     b≥k−s.                                      (6)

From (5)–(6), a+b≥k+2z. Yet 2^a3^b divides |D*|≤2^k. Thus z=0; if b>0, the strict inequality 2^a3^b>2^(a+b) gives a contradiction as well. Therefore b=0, a=k and D*=C. No spanning hypothesis on D* was used to obtain this conclusion.

## The final fixed-unit exclusion and classification

Suppose u>0. Every nonzero fixed-unit character takes each value on half of the 2^k codewords. Since D*=C, every fully active class indexed by d∈C is selected. Writing ε_i for the parity of the local τ restriction, its contribution to F′ is

 M(d)=∏_{i=1}^u (15 if ε_i+χ_i(d)=0, and 10 otherwise).

The geometric mean of these positive numbers over d∈C is 150^(u/2), regardless of correlations or repetitions among the code characters. Arithmetic–geometric mean therefore gives

 F′/2^k ≥ 2^(−k)Σ_{d∈C} M(d) ≥ 150^(u/2) > 12^u.

The first inequality permits any further selected classes having identity at fixed coordinates. But (4) and D*=C say F′/2^k=12^u. This contradiction forces u=0. Together with z=0, all τ-fixed factors are excluded.

The number of simple factors is consequently even, and gauging the restrictions along τ-pairs gives the pure pair swap without changing the sign code. The [arbitrary-mark exhaustion and paired construction/isomorphism theorem](radical-free-a5-outer-codes.md#arbitrary-selected-marks-for-paired-nonpermuting-a5-codes), with three independent reviews at [the source revision](https://github.com/Mira-Cult/math-wip/commit/820e678f92b42fe80d9e6c47cfd7e3afe3536815), now applies. It supplies the pure-A5 path class or the stated positive path lengths and strongly connected binary matrix, modulo length-preserving simultaneous permutations. This assembly retains every pinned upstream qualification and makes no assertion for canonical groups that permute their simple factors, other socles, or radical extensions.


## Independent mathematical review

reviewers contributor 1, contributor 2, and contributor 3 independently accepted this complete theorem and classification assembly at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/42e39c3cfbb5ded0d294a1a01fd6ab7dea8d6c0e), conditional on its pinned canonical-folder, actual-mark, A₅ subgroup, support-parity and paired-code classification inputs. They checked actual H-invariant tensors and normalizers, the graph bounds and both three-ended exclusions, the proper fixed-coordinate and path-leaf screens, weighted mixed moments, fully active global collisions, both Sylow deficits and the reserved Q-character relations, actual code lifts and odd averaging, and the final AM–GM contradiction. Their scope includes arbitrary code correlations and selected marks in the entire stated nonpermuting A₅-socle model, with no initial inversion assumption. It excludes factor-permuting canonical groups and other socles. No new computation, primary-source audit or reproof of upstream classifications was performed. These are independent model mathematical reviews, not human or formal certification or GitHub approval.
