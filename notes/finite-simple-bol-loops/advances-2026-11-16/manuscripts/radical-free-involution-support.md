# Involution support in paired simple envelopes

**Independently reviewed continuation of 0323:C0010 (dependency `claims/C0010.md` not included in this update).** The obligation is to control correlations in the actual stabilizer leaf group of a paired simple canonical envelope. The general parity lemma below gives a Sylow-2 restriction in every forest component. Its applications exclude all paired powers of PSL₂(9), Suzuki groups and small Ree groups. The hypotheses refer to the entire canonical group; no exclusion of sections inside arbitrary envelopes is asserted.

## Folder interface

Let T be a nonabelian finite simple group, k≥1, and let a faithful generated canonical folder (G,H,K) of a finite simple nonassociative left Bol loop have G=T^k×T^k and canonical inversion τ swapping the two blocks. The [paired-envelope theorem](../../update-2026-11-16/manuscripts/radical-free-paired-simple-envelopes.md) (earlier public snapshot) at `4c93742a59ccdd786f23598f0374f674c6f75fff` gives K=Λ={(x,x⁻¹):x∈T^k}; a paired coordinate belongs to Λ² exactly when its two entries are conjugate inverses. The [full-strip forest theorem](../manuscripts/radical-free-strip-forests.md), independently reviewed at `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede`, expresses H as the direct product of independent full twisted T-strips and a possibly correlated leaf group R≤∏A_i with every A_i<T. Its graph is a forest with c components and ℓ proper-coordinate leaves, every component has at least two leaves, and

|R|=|T|^(ℓ−c).                                                        (1)

For a component C with h leaves, its actual leaf projection R_C satisfies |R_C|≥|T|^(h−1), with strict inequality when C is a proper component. These are the reviewed normal-quotient restrictions; they do not assert that R_C defines a quotient loop. All canonical-folder and CFSG-dependent inputs of those sources remain dependencies.

## Support-parity lemma

Let P≤∏_{i∈I}P_i be a finite 2-group, and partition I into nonempty blocks I_j. If

|P| > (∏_i |P_i|)/(∏_j min_{i∈I_j}|P_i|),                           (2)

then P contains a nonidentity involution whose coordinate identity/nonidentity support is constant on every block. Neither P nor the P_i need be abelian.

For x∈P with x²=1 put e_i(x)=1 if x_i=1 and 0 otherwise. Over F₂ the indicator that all entries on a block are simultaneously identity or simultaneously nonidentity is

∏_{i∈I_j}e_i + ∏_{i∈I_j}(1+e_i) = Σ_{J⊊I_j}∏_{i∈J}e_i.           (3)

Expand the product of (3) over the blocks and sum over x²=1. Each term counts such x in the kernel of projection to a set J omitting at least one coordinate in each block. The order of that projection's target is at most the right side of (2), so each kernel is a nontrivial 2-group. In any nontrivial 2-group the number of x with x²=1, including identity, is even: the other elements pair with their distinct inverses, while the group has even order. Every summand is therefore even. The number of matched-support elements with x²=1 is even and includes identity, so includes another element. This proves the lemma.

### At most one deficient leaf per component

Assume T has a single conjugacy class of involutions, and put s=|T|₂. Every forest component has at most one leaf A_i with |A_i|₂<s.

Indeed, choose P∈Syl₂(R) and let P_i be its coordinate images. They have orders at most s, and |P|=s^(ℓ−c). For a component with h leaves, the product of |P_i| divided by their minimum is at most s^(h−1). If two leaf groups have 2-part less than s, at least two P_i have order less than s; deleting one minimum still leaves a deficient factor, so the inequality is strict. Thus any such component makes (2) strict globally.

The lemma supplies an actual nonidentity involution in R whose support is constant on each component. Choose an involution on each independent full strip in an active component, and identity on inactive components. Every full strip twist preserves the unique T-involution class. All paired coordinates are consequently conjugate inverses, so this is a nonidentity element of H∩Λ², contrary to the folder condition. Correlations in R have not been discarded.

### Prime and subgroup-order obstruction

Still assume that T has one involution class. Suppose a prime r divides |T| and every proper r-bearing subgroup of T has 2-part less than s. Let M_r bound the orders of proper r-bearing subgroups, and M₂ bound the orders of proper subgroups with full 2-part s. If

M_r M₂ < |T|,                                                       (4)

there are no folders with the preceding paired canonical model, for any k≥1.

By (1), the r-valuation requires at least ℓ−c r-bearing leaves, since each contributes at most v_r(|T|). Each is deficient. The preceding restriction gives at most c deficient leaves, hence ℓ≤2c. The forest lower bound gives ℓ=2c. Every component is a path with exactly one r-bearing deficient leaf and one full-2-part leaf. Thus |R|≤(M_r M₂)^c<|T|^c=|R|, a contradiction. This argument uses only projection orders, not independence.

<a id="paired-psl9-exclusion"></a>

## Paired PSL₂(9) exclusion

Let T=PSL₂(9)≅A₆, of order 360=2³·3²·5. The required finite subgroup input is: the maximal subgroups are two classes of A₅ (order 60), one class of 3²:4 (order 36), and two classes of S₄ (order 24); T has one involution class. In particular, every full-2-part proper subgroup lies in S₄. The [ATLAS A₆ page](https://brauer.maths.qmul.ac.uk/Atlas/alt/A6/), sections “Maximal subgroups” and “Conjugacy classes”, accessed 15 November 2026, supplies those data. The asserted [GAP 4.15.1 certificate](../../update-2026-11-16/code/verify_psl2_nine_subgroups.g) (earlier public snapshot) additionally checks all 22 subgroup classes and that the proper 5-bearing types are C₅, D₁₀ and A₅. These are explicit finite classification inputs, not consequences of the parity lemma.

The one-deficient-leaf bound means a component with h leaves has at least h−1 full-2-part leaves, each of order at most 24. Every remaining proper leaf has order at most 60. If h≥3 then

|R_C|≤60·24^(h−1)<360^(h−1),

because 60<15^(h−1), contradicting the component lower bound. Hence all components are paths. Each has a chosen full-2-part S₄ leaf. Since these are 5-free and |R|₅=5^c, every opposite leaf contains a factor 5. If such a leaf has type C₅ or D₁₀, its component projection has order at most 24·10<360, again impossible. Therefore every opposite leaf is A₅, and after choosing containing S₄ subgroups,

R≤S₄^c×A₅^c, with ambient index 4^c.                              (5)

The projection to A₅^c has 2-power index. Each coordinate projection must be A₅: a proper subgroup of 2-power index would have index 2 or 4, and the faithful coset action contradicts simplicity and |A₅|>|S₄|. By the subdirect-product form of Goursat's lemma, the projection is a product of diagonal A₅ strips. A nonsingleton strip gives index divisible by 60, incompatible with 2-power index, so the projection is all A₅^c. Goursat now separates

R=R₀×A₅^c,  R₀≤S₄^c,  |R₀|=6^c,

because S₄^c is solvable and has no nontrivial quotient in common with A₅^c. Choose a nonidentity involution of R₀. Independently select an A₅ involution at the opposite end of each path where its S₄ coordinate is nonidentity, and identity elsewhere. Fill each active full strip with an involution. The single T-involution class makes this a nonidentity member of H∩Λ², a contradiction. Thus no paired PSL₂(9) folder exists for any k.

## Paired Suzuki exclusion

Let T=Sz(q), q=2^f, f odd and f≥3. Its order is q²(q²+1)(q−1), its 2-part is q², and it has one involution class. The precise subgroup input is Patassini, *The probabilistic zeta function of PSL(2,q), of the Suzuki groups ²B₂(q) and of the Ree groups ²G₂(q)*, Pacific J. Math. 240 (2009), Theorem 10, printed p.192 ([publication PDF](https://msp.org/pjm/2009/240-1/pjm-v240-n1-p07-s.pdf)). Every maximal subgroup is a Borel q²:(q−1), a dihedral group of order 2(q−1), a torus normalizer of order 4(q±√(2q)+1), or a proper subfield Suzuki group. Arumugam–Bamberg–Giudici, *Low Rank Groups of Lie Type Acting Point- and Line-Primitively on Finite Generalised Quadrangles*, Electron. J. Combin. 32(1) (2025), Lemma 10, printed p.6 ([published PDF](https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i1p43/pdf/)), states the single involution class, citing Suzuki's Proposition 7. The underlying original classification and Suzuki proof have not been reverified here.

Zsigmondy's theorem, in the version pinned in [the PSL₂ source](../manuscripts/radical-free-psl2-path-classification.md#all-nonprime-fields-of-characteristic-at-least-seven), gives a primitive prime divisor r of 2^(4f)−1; 4f≥12 avoids both exceptions. Then ord_r(2)=4f and r≥4f+1>5. It divides q²+1 but not q−1 or any proper subfield Suzuki order. Indeed a divisor of 2^(2d)+1 or 2^d−1 would have order dividing 4d or d, with d<f. Thus every proper r-bearing subgroup lies in a torus normalizer, has 2-part at most 4<q², and has order at most M_r=4(q+√(2q)+1). Every full-2-part proper subgroup lies in a Borel, so M₂=q²(q−1).

For q≥8,

4(q+√(2q)+1)<q²+1:

since √(2q)≤q/2, the left side is at most 6q+4, and q²−6q−3>0 for q≥8. Therefore M_r M₂<|T|. The prime and subgroup-order obstruction excludes every paired Suzuki power.

## Paired small Ree exclusion

Let T=²G₂(q), q=3^f, f odd and f≥3. Its order is q³(q³+1)(q−1), its 2-part is 8, and it has one involution class. Bäärnhielm, *Recognising the small Ree groups in their natural representations*, arXiv:1206.0411v3 (28 August 2014), Proposition 3.1(1), Proposition 3.3(4), Proposition 3.6 and Proposition 3.7(1), gives respectively the order, involution class, maximal-subgroup list and involution-centralizer order ([versioned full text](https://arxiv.org/html/1206.0411v3)); published in J. Algebra 416 (2014), 139–166, DOI 10.1016/j.jalgebra.2014.06.017. The maximal subgroups are the point stabilizer q³:(q−1), C₂×PSL₂(q), a normalizer of order 6(q+1), the two torus normalizers of orders 6(q±√(3q)+1), and proper subfield Ree groups. The earlier classification proofs cited by that source are not independently reverified here.

Zsigmondy supplies a prime r with ord_r(3)=6f≥18; thus r≥6f+1>3. It divides q²−q+1 and no point-stabilizer, involution-centralizer or order-6(q+1) normalizer. Nor does it divide a proper subfield Ree(s) order: writing s=3^d with d<f, a divisor of s³+1 or s−1 has multiplicative order dividing 6d or d. Hence every proper r-bearing subgroup lies in one of the two torus normalizers, has 2-part at most 2, and order at most M_r=6(q+√(3q)+1).

Every proper full-2-part subgroup has order at most M₂=q(q²−1). The point stabilizer and the two r-torus normalizers have 2-part 2 because q≡3 mod8. The involution centralizer has order M₂. The remaining torus normalizer has order 6(q+1)≤M₂. Finally, for a proper subfield q=s^d, d≥3 odd, its order is s³(s³+1)(s−1)<s⁷≤s⁹−s³≤q(q²−1); this includes s=3. The maximal list is exhaustive.

After cancelling q(q²−1), inequality (4) becomes

6(q+√(3q)+1)<q²(q²−q+1).

For q≥27 its left side is at most 6(2q+1), which is smaller than the right side. The prime and subgroup-order obstruction therefore excludes every paired small Ree power.

## Evidence and review boundary

The coordinator read and ran the exact A₆ certificate with GAP 4.15.1: all asserted maximal-subgroup types/counts, involution classes, Sylow containment, 22 subgroup classes, 5-bearing types, C₅ normalizer and A₅ index checks passed. The computation relies on GAP's subgroup algorithms and data and does not prove the general parity or forest deductions. The coordinator inspected the cited ATLAS, Patassini, Arumugam–Bamberg–Giudici and versioned Bäärnhielm source statements. Independent mathematical/source/code reviews are recorded below. The unrestricted classification, other socle actions and arbitrary radical extensions remain open.


### Independent review

GPT-6.1 Terra reviewers `review_s5_h3`, `review_hs_full` and `review_small_order_complete` independently accepted this full manuscript, the all-field paired-PSL₂ assembly and the A₆ certificate at exact source `e30af949531c0ebcc9f7533b04fc1e7fc6858563`. All checked the parity count for nonabelian correlated 2-groups, actual-R and full-strip lifting into H, one-deficient-leaf and order-product consequences, the q=9 component bound and Scott/Goursat split, all Suzuki/Ree maximal cases and primitive-prime exclusions, and the all-field table's exhaustive coverage and inherited isomorphism counts. Each extracted, read and ran the exact committed certificate with GAP 4.15.1; every assertion passed.

All three inspected the ATLAS A₆ maximal list, Patassini Theorem 10 and Bäärnhielm v3 Propositions 3.6 and 3.7(1). `review_hs_full` and `review_small_order_complete` additionally inspected the Suzuki involution source, Arumugam–Bamberg–Giudici Lemma 10, and Bäärnhielm's order/involution statements in Propositions 3.1 and 3.3(4). These are source-statement checks, not reproofs of the cited classifications or GAP algorithms. The mathematical acceptances remain conditional on the pinned canonical-folder, forest/component, path, Dickson and Zsigmondy interfaces. They are model reviews, not human or formal certification, and do not classify arbitrary envelopes.


## Prime-order support extension

**Independently reviewed continuation of 0323:C0010.** Let p be prime, P≤∏_{i∈I}P_i a finite p-group, and I partitioned into nonempty blocks I_b. If

 |P| > (∏_{i∈I}|P_i|)/(∏_b min_{i∈I_b}|P_i|),

then P has an element x of order p whose coordinate support is constant on every block: on each block all coordinates are identity or all are nonidentity. The P_i may be arbitrary finite p-groups, and the coordinate projections need not be surjective.

For x∈P with x^p=1 put e_i(x)=1 if its i-coordinate is identity and 0 otherwise, as an element of Fp. For a block of size h define

 F_b(x)=∏_{i∈I_b}(1−e_i(x))−(−1)^h∏_{i∈I_b}e_i(x)
       = Σ_{J⊊I_b}(−1)^{|J|} ∏_{i∈J}e_i(x).

On a mixed block F_b=0, on an all-nonidentity block F_b=1, and on an all-identity block F_b=(−1)^{h+1}, nonzero in Fp. Summing ∏_b F_b(x) over x^p=1 and expanding gives a signed sum of the numbers of p-torsion elements in the kernels P∩ker π_J, where J omits at least one coordinate in each block. The strict order bound makes each such kernel nontrivial: its image has order at most ∏_{i∈J}|P_i|, at most the threshold. In any nontrivial finite p-group Q, the number of solutions of x^p=1 is divisible by p: choose a central element z of order p, and its cyclic group acts freely on the solution set by multiplication, since (xz)^p=x^p. Thus the weighted sum is 0 in Fp. The identity contributes ∏_b(−1)^{|I_b|+1}≠0, so some nonidentity x with x^p=1 has nonzero weight, i.e. constant support. For p=2 this recovers the unweighted support-parity lemma.

### Folder consequence

Suppose the reviewed paired strip-forest interface applies to T^k×T^k with τ exchanging paired simple factors, and that all elements of order p in T form one T-conjugacy class. Let R be the actual global projection of H onto its proper-coordinate leaves, partitioned by forest component. Apply the lemma to a Sylow p-subgroup P of R, taking P_i to be its coordinate images. If the displayed strict order inequality holds, there is a global leaf element x of order p with constant support on components. On each active component, every nonidentity leaf coordinate has order p; as the unique class is invariant under inversion and every automorphism, choose order-p elements on full internal diagonal strips so that paired coordinates are conjugate to inverses. Set every inactive component to identity. The resulting nonidentity element of H lies in Λ², using the paired-mark collision interface, contradicting transversality. The leaf element is in the actual global R, so its lift respects correlations across components; no componentwise projection is falsely promoted to a supported global element.

It suffices instead to assume a single Aut(T)-stable, inverse-stable T-class of order-p elements only if every nonidentity coordinate of the lemma's selected x is known to lie in that class. Existence of such a class alone is not enough: the lemma does not control which order-p class appears in each projection. This distinction matters for multiple classes. In particular, if s=|T|_p, the forest order gives |Syl_p(R)|=s^(ℓ−c). Exactly as in the involution proof, each component has at most one leaf whose p-part is less than s. A second prime r whose proper r-bearing subgroups are all p-deficient then gives the same path and strict subgroup-order obstruction with p replacing 2. These extensions have the scoped independent reviews below; they retain the full paired marking and the stated class condition, and never assume a quotient loop.


### Independent review of the prime-order extension

GPT-6.1 Terra reviewers `review_hs_full`, `review_small_order_complete` and `review_s5_h3` independently accepted the prime-order extension and folder consequence at exact source `ada92bab7c75898127ee367a33f68329ed3cdacc`. All checked the signed block weights, projection-kernel order bound, central order-p free action on the torsion solutions, nonzero identity contribution and actual global-R lift. They explicitly retained the single T-conjugacy-class hypothesis; the lemma alone does not control which class occurs. The reviews use the pinned paired-folder and strip interfaces, with no new computation or primary-source audit.


## Mixed private-prime obstruction

**Independently reviewed continuation of 0323:C0010.** This gives a sufficient exclusion, not a classification of mixed folders. Its input is the canonical faithful-folder/normal-subloop interface of C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, together with the reviewed strip-forest and support-parity arguments in `radical-free-strip-forests.md`, `radical-free-involution-support.md` at `e30af949531c0ebcc9f7533b04fc1e7fc6858563`, and the mixed-type quotient interface in `radical-free-mixed-simple-quotients.md` at `ada92bab7c75898127ee367a33f68329ed3cdacc`. The conclusion is conditional on these and the exact subgroup hypotheses below. It concerns the entire canonical group, not sections inside arbitrary groups.

### Transferable criterion

Let G=∏_{i=1}^d S_i^{2k_i}, d≥2, where k_i≥1, the S_i are pairwise nonisomorphic finite nonabelian simple groups, and τ swaps the two members of each prescribed pair. Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop. As every outside involution for this swap action belongs to a single G-class, K is the full anti-diagonal set.

Assume:

1. Every S_i has one conjugacy class of involutions.
2. For the actual stabilizer H, its full-coordinate projections split off as independent full twisted simple strips, with a residual group R on all proper-projection coordinates. (It suffices, for example, that every proper subgroup of every S_i be solvable. The application below uses a slightly weaker direct composition-factor check.)
3. For some distinguished type T=S_j there is a prime r dividing |T| but not |S_i| for i≠j. Write s=|T|_2. Every proper r-bearing subgroup of T has 2-part less than s and order at most M_r; every proper subgroup of T with 2-part s has order at most M_2. Finally M_r M_2<|T|.

Then no such folder exists.

#### Proof under these hypotheses

For each type i, construct the graph of its full strips and proper-coordinate leaves, with one edge for each τ-pair. The normal-quotient criterion applied to any nonempty component, retaining its complete pairs and killing all other coordinates, gives |R_C|>|S_i|^(k_C−m_C), where k_C is the number of edges, m_C the number of full strips, and R_C the actual leaf projection. This is always a proper quotient because another type occurs. If C has no leaves, every strip vertex has degree at least two, so k_C≥m_C, contradicting R_C=1. If it has h leaves, all proper coordinate projections have order below |S_i|; comparing with the strict inequality gives k_C−m_C<h. The connected graph cycle rank k_C−m_C−h+1 is therefore zero. Every component is a tree with at least two leaves.

Let ℓ_i and c_i be the number of leaves and components of type i. The strip splitting, forest identities, and |H|=|K| give

 |R|=∏_i |S_i|^(ℓ_i−c_i).                                     (1)

The mixed version of the support-parity lemma shows that every component of every type has at most one leaf whose actual projection has 2-part smaller than |S_i|_2. Indeed choose P∈Syl₂(R) and use each component's leaves as a block. If some component has at least two deficient leaves, the product of all coordinate 2-image orders divided by one smallest image per block is strictly below |P|: each other block contributes at most |S_i|_2^(h−1), while this block contributes strictly less. The parity lemma supplies a nonidentity involution with support constant on each component. Populate each full strip of each active component with an involution from its type's unique class and set all inactive strips to identity. At every τ-pair the resulting coordinates are conjugate inverses, contradicting H∩K²=1. Correlations inside R have not been discarded.

By private r, (1) has r-valuation v_r(|T|)(ℓ_T−c_T) and no leaf of another type contributes. Every T leaf contributes at most v_r(|T|), and every r-bearing leaf is deficient. Hence at least ℓ_T−c_T leaves are deficient, while there are at most c_T. Together with ℓ_T≥2c_T, this forces ℓ_T=2c_T. All T components are paths and each has exactly one r-bearing deficient endpoint and one full-2-part endpoint. For every such component,

 |R_C|≤M_r M_2<|T|,

contradicting the strict tree bound |R_C|>|T|. This proves the criterion.

The argument uses actual leaf projections only. No projection is assumed to be a subgroup quotient loop, no Sylow subgroup is taken to be normal, and no independence of R across components is needed. If r occurs in another type, the valuation step does not apply as stated.

### A5 paired with every finite Suzuki simple group

Let T=Sz(q)={}²B₂(q), q=2^f with f≥3 odd, and let a,b≥1. Under the pinned subgroup and folder inputs, there is no finite simple nonassociative left Bol folder with

 G=A5^{2a}×Sz(q)^{2b},

and canonical inversion swapping all indicated pairs.

For the subgroup and involution inputs, use Patassini, *The probabilistic zeta function of PSL(2,q), of the Suzuki groups ²B₂(q) and of the Ree groups ²G₂(q)*, Pacific J. Math. 240 (2009), Theorem 10, printed p.192, https://msp.org/pjm/2009/240-1/pjm-v240-n1-p07-s.pdf; and Arumugam–Bamberg–Giudici, *Low Rank Groups of Lie Type Acting Point- and Line-Primitively on Finite Generalised Quadrangles*, Electron. J. Combin. 32(1) (2025), Lemma 10, printed p.6, https://www.combinatorics.org/ojs/index.php/eljc/article/download/v32i1p43/pdf/. The latter cites Suzuki's Proposition 7 for the unique involution class; these are source-statement inputs and their original classification proofs are not independently reverified here. The group order is q²(q²+1)(q−1), with 2-part q².

Strip splitting follows even when f is composite and a proper subfield Suzuki subgroup is nonsolvable. Full Sz(q) strips split from all other coordinates because every possible remaining simple section has smaller order. For full A5 strips, every proper A5 projection is solvable, and every Sz(q) subgroup is 3-free: q≡−1 mod 3 makes q²(q²+1)(q−1) indivisible by 3. Thus no residual section is A5. Goursat splits both types of full strips from the proper-coordinate residual. A5 and Sz(q) each have one involution class.

Zsigmondy's theorem supplies a primitive prime r of 2^(4f)−1; its multiplicative order is 4f, so r≥4f+1>5. The exception at exponent 6 does not apply. Then r divides q²+1 and r∤|A5|=60. The reviewed Suzuki calculation shows that no proper subfield subgroup or other listed maximal type contains r, so a proper r-bearing subgroup has order at most

 M_r=4(q+√(2q)+1)

and 2-part at most 4<q². Every full-2-part proper subgroup lies in a Borel, so M_2=q²(q−1). The inequality

 4(q+√(2q)+1)<q²+1

holds for q≥8: √(2q)≤q/2 and q²−6q−3>0. Therefore M_r M_2<q²(q²+1)(q−1)=|Sz(q)|, and the private-prime criterion applies.

For q=8, this is already visible numerically: r=13, M_r=52, M_2=448, and 52·448=23296<29120=|Sz(8)|. This example is a check of the all-f calculation, not an exhaustive computation of folders.

The Zsigmondy source is Ö. Avcı, *Large Zsigmondy Primes*, arXiv:2011.06136v2, §1, first paragraph, https://arxiv.org/html/2011.06136v2; the original primitive-divisor proof is not rederived. The proof above does not settle mixtures in which every such r also divides another simple type, or which violate the independent-full-strip hypothesis. This extension has the scoped independent exact-source reviews below.


### Independent review of the mixed private-prime obstruction

GPT-6.1 Terra reviewers `review_paired_simple`, `audit_c9_full` and `review_folder_criterion` independently accepted this appended section at exact source `dd2f0fc5c4db866f93afe898d3a9a25382774489`, conditional on its pinned structural, source and cohomological inputs where applicable. They checked mixed-capacity parity in the actual residual, private-prime valuation saturation, strict component bounds, and the A₅/Suzuki application including nonsolvable subfield subgroups and 3-free composition-factor splitting. No new computation or fresh primary-source audit was performed. These are model mathematical reviews, not human or formal certification. The stated restrictions and unresolved reconstruction conditions remain: these deductions do not complete the unrestricted classification.
