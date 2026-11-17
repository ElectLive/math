# G₂(4) as a full multiplication socle

Mira Cult

Continuation of [0323:C0010](../foundations/research-C0010.md). Three independent exact-source mathematical reviews are recorded below.

**Conditionally proved theorem.** No finite simple proper left Bol loop Q has Soc(Mlt(Q))≅G₂(4), under the explicit inputs below. Both actual factor orientations and the outer extension are covered. This is a bounded exclusion, not a classification of all exceptional full socles or of loop operations.

## Inputs and interfaces

Use the [canonical definitions](../foundations/problem-contract.md), C0001 at `9431ade99316d6bc62efb389492fef385b510b45`, scoped canonical inversion/marked-set interface at `932ead5db5f39045e2085caa6b062f6b981b2813`, C0008's primitive almost-simple full-group result at `06857e28349ca4529c31a9855ce12cfbb191c1b7`, and the inner-inversion/component obstruction at `84eba0ffd4dfab4b6d64853a3131010ad2b945b8`. The canonical almost-simple PSU₃(4) exclusion is pinned at `114ce1b011fd47589eb762ed7cd5492a190002d8`; the scoped rank-three result C0017 is pinned at `7b1c9e8786ceb5e7d8e6a6709adee1aefe736efd`. The latter's nonassociative simple Bol alternatives have orders120 and1080. These inputs do not promote unrelated aggregate claims.

[Li–Xia arXiv:1408.0350v3](https://arxiv.org/html/1408.0350v3), Proposition4.2, printed p.28, excludes a factorization of an almost-simple exceptional group by two core-free factors with either factor solvable. The finite inputs are the complete ATLAS/CTblLib maximal-subgroup class lists for S=G₂(4), A=Aut(S)=G₂(4).2 and U=PSU₃(4), together with the stored subgroup fusions and the compatible normal embeddings U◁U.2◁U.4. Here U.2 is maximal in S and U.4 is maximal in A. These group identifications, normal structures and completeness are external classification inputs, not consequences of character-table arithmetic. Exact primary metadata and its version limitation are recorded in [REFERENCES](../foundations/references.md).

The [certificate](../code/verify_g24_full_factor_sieve.g) pins GAP4.15.1 and CTblLib1.3.11, asserts the complete stored maximal lists and checks the order sieves, available fusions, permutation-character ranks and class data used below. It does not reconstruct the subgroup classification. No actual-factor classification from Hering–Liebeck–Saxl is required: in particular the correction in Li–Wang–Xia arXiv:2106.03109v2 p.1 footnote1 is not silently omitted by an incomplete actual-factor list.

Write M=Mlt(Q), G=LMlt(Q), I=M₁, H=G∩I, G₀=G∩S and I₀=I∩S. Then S≤M≤A, I is core-free maximal, and M=GI. The nontrivial normal socle is transitive in the faithful primitive action, so |Q|=[M:I]=[S:I₀]. The actual marked set Λ is a nonempty G-invariant set of involutions outside G in the canonical split extension; |Λ|=[G:H] and Λ²∩H={1}.

## The socle-containing case

Suppose S≤G. If G=A, restriction to the characteristic socle embeds Aut(G) into Aut(S)=G: an automorphism fixing S pointwise is trivial since C_G(S)=1. Inner automorphisms already realize every restriction, so every automorphism of G is inner, contrary to the pinned canonical inversion obstruction.

If G=S, an inner canonical involution is likewise excluded. For an outer involution the split extension identifies with A. There is one outside involution class, of size20800 and S-centralizer12096. Its A-class is a single S-class, since an outside representative itself centralizes the representative and A=S C_A(λ). Thus Λ is that entire class and |H|=|S|/20800=12096. The square of this class contains both S-involution classes: its class multiplication coefficients are320 and80. Consequently every involution of S lies in Λ², whereas even H contains an involution. This contradicts Λ²∩H={1}. The certificate checks the two socle involution classes and their actual fusion into A. This is another finite proof of the earlier reviewed canonical G₂(4) result, without replacing its historical source or review pins.

## Reduction to a unitary factor

Now S is not contained in G. Both G and I are core-free in M, hence nonsolvable by Li–Xia. Their quotients by G₀ and I₀ embed in M/S of order at most2, so G₀ and I₀ are nonsolvable proper subgroups of S. The factorization order identity implies

    |S| divides 2 |G₀| |I₀|.

Indeed, if d=[M:S] and e_G=[G:G₀], e_I=[I:I₀], then |S|=e_G e_I |G₀||I₀|/(d|G∩I|), with d∈{1,2} and e_G,e_I dividing d. This entails the displayed divisibility even when G₀I₀≠S.

Enlarge the two actual intersections to maximal subgroups A₀,B₀ of S. The complete maximal list and |S| dividing2|A₀||B₀| leave, up to interchange, precisely these overpairs:

    U.2 versus J₂, 3.L₃(4).2₃, or U₃(3).2.

This is only a necessary sieve; it does not assert that every overpair factors S. Each opposing group has order prime to13. Hence the actual subgroup on the U.2 side has order divisible by13. Its intersection with U has index at most2 and is still nonsolvable and13-bearing. The complete U-maximal list has orders960,300,150,39; its only13-bearing member is the solvable13:3. Thus the actual subgroup on this side contains U. In particular it is U or U.2 and has perfect residual U.

The stated embeddings give N_A(U)=U.4: the normalizer contains the maximal U.4 and cannot equal A, since then U would be a nontrivial proper normal subgroup of S. Similarly N_S(U)=U.2. The simple group U has order62400 and trivial center. Therefore C_A(U) embeds in N_A(U)/U, of order4. If nontrivial, it contains an involution t, forcing62400 to divide |C_A(t)|. The complete involution-centralizer list in A is122880,7680,24192; none is divisible by62400. Hence C_A(U)=1.

## Both actual orientations

If G₀ is on the U.2 side, U=G₀^(∞) is characteristic in G₀◁G. Thus U≤G≤N_A(U), and C_A(U)=1 embeds G faithfully between U and Aut(U). Its socle is U. The reviewed canonical almost-simple PSU₃(4) exclusion applies and gives a contradiction.

If I₀ is on that side, U=I₀^(∞) is characteristic in I₀◁I. Hence I≤N_M(U). The normalizer is proper, so maximality of I forces I=N_M(U), namely U.2 for M=S and U.4 for M=A. For both stored embeddings the induced trivial character has degree2016 and inner product3 with itself. Therefore the actual full action has rank three and |Q|=2016, contrary to the C0017 order alternatives120 and1080. This closes the second orientation.

## Evidence and remaining scope

The source authors read and ran the committed certificate with GAP4.15.1/CTblLib1.3.11; it checks all maximal overpairs, both rank-three actions and all required involution data without randomness. The raw log is outside Git. Repository integrity is checked separately with Python3.11+ and does not prove the theorem. Independent mathematical reviews are recorded below. Other exceptional and classical socles, and the natural alternating loop operations, remain separate obligations.


### Independent review

automated-model reviewer A, reviewer B and reviewer C independently accepted exact source `c488dbb75c3ba1f7936d158b92ddb5c5951c20c5`. Each checked the actual-factor divisibility without assuming G₀I₀=S, the complete maximal overpair sieve, the nonsolvable13-bearing intersection, normalizers and faithful centralizer, the canonical outer-class square and both actual orientations. Each read, extracted and independently ran the exact committed certificate under GAP4.15.1/CTblLib1.3.11; all assertions passed. The paired reviewer freshly inspected Li–Xia v3 Proposition4.2 and the ATLAS G₂(4) order/Out/maximal-list page. The other two retained their recent Li–Xia inspection and the recorded metadata inputs without freshly browsing those pages in this pass. All retained the compatible normal embeddings, complete classifications and stored fusions as external inputs. The source authors's separate Python3.12.14 integrity run passed115 tests. These are model mathematical/code reviews of this bounded full-socle exclusion, not formal or human certification, GitHub approval or a solution of C0010.
