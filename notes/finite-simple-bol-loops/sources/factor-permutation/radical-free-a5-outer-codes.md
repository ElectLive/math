# Nonpermuting A5-socle extensions and paired parity-code classification

Mira Cult
A structural result for [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). The exact-source independent reviews are recorded below. The faithful generated-folder and normal-quotient interface is [C0001](../../claims/0001.md); canonical inversion/conjugacy-invariance uses the scoped [C0007](../../claims/0007.md) input. The A₅ subgroup/automorphism input is pinned in [the paired A₅ source](radical-free-a5-path-classification.md). The proposed universal reduction `LMlt(Q)=Soc(LMlt(Q))` is **false**, already for socle A5² and a nontrivial outer-action quotient C2. The example is an instance of G. P. Nagy, *A class of simple proper Bol loops*, `arXiv:math/0703919v1`, 30 March 2007, Proposition 3.2, Lemma 3.4 and Theorem 3.6, https://arxiv.org/html/math/0703919v1. Those primary statements were inspected. It is not a new family or a claim of literature novelty. The elementary canonical group, radical, and normal-quotient computations below make this particular instance explicit.

## Explicit factorization and canonical group

Let X=S5 acting on F5. Take

 Y0=AGL1(5)={x↦ax+b : a∈F5*, b∈F5},  |Y0|=20,
 Y1=Stab_X(0,1)≅S3,                         |Y1|=6.

An affine map fixing 0 and 1 is the identity. Hence Y0∩Y1=1 and |Y0||Y1|=120=|X|, so X=Y0Y1. Both are core-free: the only nontrivial proper normal subgroup of S5 is A5, too large for either. Each contains an odd permutation: multiplication by 2 is a 4-cycle on F5*, and Y1 contains a transposition. Thus A5Y0=A5Y1=S5. Nagy's Theorem 3.6 applies to this faithful almost-simple factorization triple and gives a finite simple proper left Bol loop Q of order 120.

For the canonical generated folder, put

 K={(x,x^-1):x∈S5},
 G=⟨K⟩={(u,v)∈S5×S5 : sign(u)=sign(v)},
 H=G∩(Y0×Y1),   τ(u,v)=(v,u).

The description of G follows directly: products of anti-diagonal elements and their inverses generate A5×1 and 1×A5 because S5′=A5, and the displayed parity subgroup is then the product of A5×A5 with K. Nagy's Lemma 3.4 identifies this generated action with LMlt(Q); the inversion automorphism τ is the coordinate swap and sends every member of K to its inverse. Here |G|=7200, |K|=120 and |H|=60, with H projecting onto each Y_i.

Set N=A5×A5. The two factors are minimal normal in G, and C_G(N)=1, because C_{S5}(A5)=1. Every nontrivial normal subgroup of G meets N nontrivially: otherwise its commutator with N is trivial, putting it in the trivial centralizer. Consequently every minimal normal subgroup is one of the two simple factors, so

 Soc(G)=A5×A5,    G/Soc(G)≅C2,    G≠Soc(G).

Any solvable normal subgroup intersects N trivially and hence centralizes N; it is therefore trivial. Thus the **solvable radical is 1**. The quotient's nontrivial coset acts by the outer automorphism on each A5 factor, simultaneously. The simple factors are not permuted by G in this example; τ exchanges them as an external canonical automorphism. This distinction matters for the remaining permutation-extension question.

## Direct normal-quotient verification

The nontrivial proper normal subgroups of G are exactly N1=A5×1, N2=1×A5, and N=A5×A5. To see this, any normal subgroup L has L∩N∈{1,N1,N2,N}. Trivial intersection gives L=1 by C_G(N)=1. If L∩N=N1, then [L,N2]≤L∩N2=1, so L≤C_G(N2)=N1 and L=N1; similarly for N2. If L contains N, its image lies in G/N≅C2, so L=N or G.

For each proper nontrivial L, the exact normal-subloop criterion in repository C0001 compares |KL/L| with [G:HL]. The following strict inequalities hold:

 L=N1: |KL/L|=120 > 20=[G:HN1];
 L=N2: |KL/L|=120 >  6=[G:HN2];
 L=N:  |KL/L|=  2 >  1=[G:HN].

The first two K-images are injective under projection to the untouched S5 coordinate; the H projections are Y1 and Y0. For the third, both K and H meet the odd-odd coset, so HN=G and KN/N=G/N. Thus the exact normal criterion independently confirms simplicity, without assuming the old false converse to a normal-transitivity criterion. The full Mlt(Q) is not being identified or used.

## A general quotient restriction and next case

More generally let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop, and let N◁G be nontrivial and proper. Put bar G=G/N, bar H=HN/N and bar K=KN/N. The strict normal criterion gives

 |bar K| > [bar G:bar H].                                       (*)

Consequently bar H≠1 and bar K≠{1}. If G/N≅C2, both bar H and bar K equal C2. Thus H surjects to G/N, and, writing H0=H∩N,

 |K|=[G:H]=[N:H0],    |K∩N|<[N:H0].

The strict inequality follows since K has at least one element outside N. If additionally τ(N)=N, then K∩N contains the τ-twisted commutator orbit of 1 under N, of cardinality [N:C_N(τ)], so

 |H0|·[N:C_N(τ)] < |N|.                                        (**)

The additional inequality (**) requires τ(N)=N; the strict quotient inequality (*) applies to every normal N, including N1 and N2 above. These are necessary conditions on the actual section and original H; the projected set bar K need not be a canonical loop section, and no normality of H0 in N is assumed. For the S5 example τ swaps the two A5 factors, so [N:C_N(τ)]=60, while |H0|=30 and |N|=3600, giving strict inequality 1800<3600.

For the general nontrivial quotient P=G/Soc(G), τ induces an involutory automorphism on P and every bar k∈bar K satisfies bar τ(bar k)=bar k^-1. In particular, if bar τ=id, P is generated by the involutions in bar K, because K generates G. This supplies a concrete screen on allowed permutation/outer quotients but does not prove P=1 or classify the overgroups.

## Parity codes with no factor permutation

Suppose G is finite and radical-free with Soc(G)=A5^r, and conjugation by G does not permute the r simple factors. The solvable radical being trivial forces C_G(Soc(G))=1: any nontrivial centralizer is a normal subgroup containing a minimal normal subgroup disjoint from the socle, contradiction. Therefore conjugation embeds G into Aut(A5)^r=S5^r, with N=A5^r contained, so G is exactly the inverse image of a binary linear code C≤F2^r under the coordinate sign map.

Let τ be the canonical inverting automorphism of G. Its induced action on C is the involutory permutation σ of simple-factor coordinates. Since the images of K generate C and τ(k)=k^-1, every image of k is fixed by σ (C has exponent 2). Hence σ acts trivially on C: each codeword has equal bits on every τ-swapped pair. This is a necessary condition even when τ also fixes factors. It uses LMlt only.

Specialize to r=2p and τ swapping every pair. Conjugating inside Aut(N)=S5^(2p) gauges the restrictions of τ on paired factors to the pure coordinate swap; coordinate conjugation does not change the parity code. Regard C≤F2^p by its common sign on each pair. For each c∈C, all τ-outside involutions with sign c form a single N-orbit, represented in K-coordinates by

 {(x_i,x_i^-1)_i : sign(x_i)=c_i}.

Indeed N=A5^(2p) acts transitively on the choices of each x_i of specified sign. Thus actual K is exactly the union K_D of these orbits for some D⊆C with 0∈D, and |K|=60^p|D|. Since K generates G and the even anti-diagonals generate N, span(D)=C. Transversality gives |D| | 60^p·2^dim(C), and |H|=60^p·2^dim(C)/|D|. With V=HN/N≤C, the exact normal criterion gives |D|>2^(dim C−dim V), while folder transversality gives V+D=C. These conditions do not assert D is a subspace.

For future subgroup analysis, the K_D-square is explicit. Write h=((u_i,v_i)) with sign(u_i)=sign(v_i) the i-th bit of c+d. Then h∈K_D² iff there exist c,d∈D and, for each i, x_i∈S5 with sign(x_i)=c_i and

 v_i=x_i^-1 u_i^-1 x_i.

The converse takes y_i=x_i^-1u_i, whose sign is d_i. This retains the parity of the actual conjugator and hence does not incorrectly fuse the two A5 classes of 5-cycles. One must enforce H∩K_D²=1 and every original normal-quotient strictness; generic code/subgroup enumeration is not automatically an exhaustion of loops.

## Two-class exhaustion for the r=2 swap case

For the group G={(u,v)∈S5²:sign(u)=sign(v)} and τ the swap, the preceding paragraph forces D={0,1}, so K is the full S5 anti-diagonal. Under the pinned folder and subgroup inputs, there are exactly two loop-isomorphism classes of simple nonassociative folders: the factorization triples (S5,F20,S3) and (S5,F20,C6), where F20=AGL1(5), S3 acts naturally on a 3-subset and fixes its complement pointwise, and C6 is generated by a 3-cycle on that subset and the disjoint transposition.

Proof of necessity. Socle quotient strictness gives HN=G; hence H0=H∩N has order 30, and H0∩(K²∩N)=1. Each projection of H0 to A5 is proper. A proper A5 subgroup carrying 5 lies in D10 and is 3-free; the other projection must carry 3 and lies in an A4 or D6≅S3. Each projection order divides |H0|=30, so a projection cannot be A4 itself; an A4 has no subgroup of order 6. The projection orders therefore reduce, up to coordinate interchange, to D10×C3, C5×S3, or an index-2 subdirect subgroup of D10×S3. In the last case the common quotient is C2 and both sign maps are unique. It contains a pair of nonidentity involutions, conjugate in A5, violating H0∩K²=1.

If H0=C5×S3, any element of H\H0 has odd coordinates and normalizes H0. Its first coordinate lies in N_{S5}(C5)=F20. Every odd element of F20 has multiplier 2 or 3 in its affine action and its square is a nontrivial involution in D10\C5, so it cannot have square in H0. Hence this case is impossible.

Thus H0=D10×C3. All such pairs are conjugate by the diagonal Aut(A5)=S5 action: N_{S5}(D10)=F20 acts sharply 2-transitively on five points, hence transitively on 3-subsets and their C3 groups. The normalizer of C3 in S5 is S3×C2, and N_G(H0)/H0 has order four. The first quotient F20/D10 is C2; the second quotient (S3×C2)/C3 is C2²; the sign-matching condition leaves two quotient choices over the nontrivial first coordinate. They give exactly two subgroups H over H0. Their second-coordinate projections are the natural S3 and C6 respectively; their first projection is F20. Equivalently H=G∩(F20×Y1) in each case. Both order-6 subgroups consist, outside C3, of transpositions or elements of order 6; the odd elements of F20 have order 4, so the intersections are trivial. Since 20·6=120, both are exact factorizations of S5. Each Y1 contains odd permutations, as does F20, so Nagy's Theorem 3.6 proves both associated loops simple and proper. Their canonical folder groups and K are as above. The direct normal-subgroup argument given earlier applies to either choice, with the same three strict quotient inequalities.

For isomorphism, a canonical-folder isomorphism commutes with τ because K generates G and τ is uniquely determined on K. Since C_G(N)=1, an automorphism is determined by its action on the two A5 factors; commuting with the swap forces the same S5 automorphism on both factors, up to interchanging the coordinates. Thus the two H are inequivalent: their order-6 coordinate projections have nonisomorphic abstract types S3 and C6. The resulting two classes are instances of Nagy's exact-factorization construction, with literature novelty not asserted. The two-subgroup finite classification uses the elementary A5 subgroup list from the reviewed paired-simple source; no new computation is used. Properness comes from the cited theorem, not from order120; the simple Paige loop of that order is not being conflated with these two Bol folders.

## Full paired outer code: a uniform classification

A continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Fix p≥1, let N=A5^{2p}, and put

 G={((u_i,v_i))∈S5^{2p}: sign(u_i)=sign(v_i) for every i}.

Thus Soc(G)=N, G/N=C=F2^p, and G is radical-free. Let τ swap u_i and v_i in each pair. This note concerns faithful generated canonical folders of finite simple nonassociative left Bol loops with this exact G and τ and with full selected mark D=C; equivalently

 K={((x_i,x_i^-1)) : x_i∈S5 for every i}.                     (1)

It proposes that their stabilizers and isomorphism classes correspond to p×p binary matrices A whose off-diagonal support digraph is strongly connected, modulo simultaneous row/column permutation. The diagonal entries are unrestricted. At p=1 the graph condition is vacuous and there are two classes; at p=2 the offdiagonal entries are both one and there are three orbits. No conclusion is asserted for D≠C, smaller codes, τ-fixed factors, or factor-permuting overgroups.

The canonical-folder and all-normal-subgroup criterion are C0001; the selected mark and inversion interface is C0007. The nonpermuting-code and p=1 setting are reviewed in `radical-free-a5-outer-codes.md`; the full-strip and support arguments use the sources pinned there and in `radical-free-involution-support.md`. A5 subgroup and automorphism facts are the inputs pinned by those sources.

### The stabilizer covers the full code

Let H0=H∩N, and V=HN/N≤C. Since C is abelian, HN is normal in G. If V<C, then HN is a nontrivial proper normal subgroup containing H, and the image of K covers G/HN by the transversal property; equality would hold in the normal-subloop criterion, contradicting simplicity. Thus HN=G. The full-mark hypothesis |D|=2^p gives

 |H0|=|N|/|K|=60^(2p)/120^p=30^p.                             (2)

This step needs only HN=G, not the selected mark to be full; (2) and all later uses of |H0| do use D=C.

### Full strips, 5-support and squares of outer lifts

All individual coordinate projections of H0 to A5 are proper. Indeed, the full-coordinate projection is a product of disjoint full twisted A5 strips and splits from the residual proper-coordinate group by Goursat, since proper A5 subgroups are solvable. H normalizes H0 and cannot permute simple coordinates. On any full strip its induced automorphisms must agree modulo Inn(A5), so the sign-code functionals of all supported coordinates agree on H/N=C. For full C this means all supported coordinates lie in one τ-pair. A singleton full strip violates corefreeness; a two-coordinate strip has a pair of conjugate involutions and meets K². Both are impossible.

A 5-bearing proper A5 projection is C5 or D10. It cannot be C5: since H maps onto the full code, an odd coordinate element h normalizes it, but every odd element of N_S5(C5)=F20 has square a reflection outside C5, whereas h²∈H0. Thus each 5-bearing projection is D10.

Let W=H0∩∏ C5 over those D10 coordinates. It is elementary abelian of order 5^p: every 5-element of H0 has support only on these coordinates, and (2) gives the full 5-part. It is normal in H because H normalizes H0, its coordinate projections and their characteristic C5 subgroups. For every i choose h∈H with code e_i. Its action on W is diagonal, with eigenvalues ±2 on the i-th pair and ±1 on every other pair. These sets are disjoint in F5, so polynomial spectral projections split W into its i-th pair-supported subspace and its complement. Repeating for all i gives W=⊕W_i.

No W_i can contain a vector nonzero on both endpoints of pair i. The full mark includes both possible signs of a conjugator at this pair, and all 5-cycles are S5-conjugate, so such an element of H0 is in K². Hence W_i lies in a single coordinate axis and has dimension at most one. Since dim W=p, each W_i is a full coordinate C5. Therefore there is exactly one D10 projection in each pair, W=C5^p, and the other projection is a 5-free proper subgroup of A5. Orient each pair with D10 first.

For any h∈H with code c, each first coordinate lies in N_S5(D10)=F20. If c_i=0 it lies in D10 and its square is in C5; if c_i=1 it is an odd affine map with multiplier ±2 and its square is a reflection in D10\C5. As h²∈H0, the D10-sign vector of h² is exactly c. Thus H0 realizes every vector of D10 signs, not merely each sign separately.

### Determination of H0 and the matrix

Quotient by W. The group H0/W has order 6^p and its D10-sign map is onto C2^p by the square calculation. Its kernel J is a normal 3-group of order 3^p. J is trivial on all first coordinates modulo W and injects into the product of the p opposite-coordinate projections. Each is a proper subgroup of A5 with 3-part at most 3, so equality of orders forces J to be the full product of one C3 in each opposite coordinate. Multiplying representatives by W removes their first-coordinate values, so this also supplies the literal subgroup 1×C3^p in H0. The kernel J is H-invariant: H normalizes H0 and W, and conjugation in each F20 acts trivially on D10/C5. Hence H normalizes every opposite C3 projection of J, and each opposite H coordinate lies in N_S5(C3)=S3×C2. For every code vector c, choose h∈H lifting c. Its square has D10-sign vector c, while its opposite coordinates are in C3, since squaring kills the S3 sign and the complementary C2. Multiplying by the independent C3 values supplied by J gives an element with D10-sign vector c and identity at all opposite coordinates. Together with W=C5^p these elements generate all independent D10 factors. Therefore, after simultaneous pairwise coordinate conjugation,

 H0=(D10×C3)^p.                                                  (3)

The normalizer quotient is

 N_G(H0)/H0 ≅ F2^p_c ⊕ F2^p_t.

The first coordinate c is the paired sign code. At the C3-side endpoint write N_S5(C3)=S3×C2, with the first factor acting on the support three-set; t_i is the sign of that S3 factor. The sign of the complementary transposition is determined by c_i+t_i. This normalizer quotient is elementary abelian; because H/H0 maps isomorphically onto C, it is the graph

 t=A c,              A∈M_p(F2).                                 (4)

Conversely every binary A defines a subgroup H containing H0 and of order 60^p.

### Folder and collision test

For every A, H∩K²=1. If h∈H has c_i=1 for some pair i, its D10-side coordinate is an odd element of F20 of order 4, whereas its C3-normalizer-side odd coordinate has order 2 or 6. They cannot be conjugate inverses in S5, so h∉K². If c=0, then t=0 and h∈H0; D10 and C3 have no common nonidentity element order in a pair. Thus h∈K² forces h=1.

Since |G|/|H|=|K|, this makes K a transversal to H and all its conjugates; K² is G-conjugacy-invariant. K is inverse- and sandwich-closed. It generates G: commutators of the anti-diagonals generate every A5 socle coordinate and the selected signs span C. Every coordinate projection of H is proper in S5, so it contains no simple socle coordinate. Any nontrivial normal subgroup of G meets N nontrivially because C_G(N)=1; hence H is core-free. The cited faithful-folder interface supplies the generated Bol loop and canonical inversion τ.

### Every normal quotient

For a normal L◁G, its socle intersection is the product N_J of the A5 coordinates it kills. Modulo N_J, the group L/N_J centralizes all remaining simple factors, because its intersection with their product is trivial. Since C_S5(A5)=1, its outer image W≤C is supported only on pairs whose two simple coordinates are both killed. Conversely the full preimage of any such W is normal. Thus L is specified by J and such a subspace W.

For the corresponding quotient, let d be the number of retained D10-side coordinates, a the number of retained C3-side coordinates, f the number of pairs with both retained, S the set of retained C3-side indices, and Z the set of pairs with neither retained. Then W≤F2^Z and

 |π_L H|/(|G/L|/|π_L K|)
   =10^d 3^a · 2^{p−dim(W∩ker A_S)} / 60^f.                   (5)

For (5), a pair with at least one retained simple coordinate contributes 120 possibilities to the K-image. Fully killed pairs contribute their independent parity bits modulo W, so |π_L K|=120^{p−|Z|} 2^{|Z|−dim W}. Meanwhile |G/L|=60^{d+a}2^{p−dim W}, giving |G/L|/|π_L K|=60^f. The image of H0 has size 10^d3^a; the remaining H/H0 variables are c modulo the kernel of c↦(c mod W,(Ac)_S), namely W∩ker A_S. This proves (5), including non-τ-stable L.

If at least one pair is partially retained, write I for the fully retained pairs and P for partially retained pairs. Since dim W≤|Z|=p−|I|−|P|, the binary factor in (5) is at least 2^{|I|+|P|}; each full pair contributes 10·3/60=1/2, while each partial endpoint contributes at least 3. Thus the ratio is at least 6^{|P|}>1.

If every pair is either fully retained or fully killed, let I be the retained set, so S=I. If I is nonempty and proper, the minimum ratio over all allowed W occurs at W=F2^{I^c} and equals

 2^{rank(A_{I,I^c})}.                                             (6)

Thus strictness for every such I is equivalent to every nonempty proper I having an outgoing edge to its complement in the digraph i→j when A_ij=1, i≠j; this is strong connectivity. If I=∅, (5) is 2^{p−dim W}, strictly greater than 1 for proper W<C; W=C is L=G. If I is all vertices, W=0 and L=1, the trivial kernel. Therefore the exact normal-subloop criterion makes the constructed loop simple exactly when the support digraph is strongly connected.

The stabilizer is nontrivial, so the loop is nonassociative. It lies properly in the group given by the product of its proper endpoint normalizers with the permitted parity code, which itself is proper in G. Hence the canonical left multiplication action is imprimitive; the cited simple-Moufang primitivity interface makes the loop proper. This uses the C0001 hypothesis and is not a statement about full Mlt.

### Isomorphism orbits

A loop isomorphism gives a canonical-folder isomorphism, hence intertwines τ because K generates G and τ is uniquely determined on K. Since C_G(N)=1, it is determined by its action on the socle factors. Commuting with τ permits permutation of τ-pairs, a common Aut(A5)=S5 automorphism on both coordinates of each pair, and interchange of coordinates within individual pairs. The projections of H0 have distinct orders 10 and 3, so after orienting each pair by its D10 endpoint, an isomorphism of normalized data cannot additionally interchange its coordinates.

All pairs (D10,C3) are simultaneously S5-conjugate: N_S5(D10)=F20 is sharply 2-transitive on five points, hence transitive on the ten complementary 3-subsets. Its stabilizer of a fixed C3 subgroup has order 2, is even, and acts trivially on the elementary-abelian normalizer quotient N_G(H0)/H0. Therefore once the endpoint pairs are normalized, the only remaining action on A is simultaneous permutation of rows and columns. This gives the proposed isomorphism criterion stated at the start. For p=1 it recovers the two reviewed p=1 classes; for p=2 the two offdiagonal ones are forced, and the two diagonal bits have three orbits.

Every use of the full code and full mark is explicit above. No assertion about other mark sets, outer-code actions, literature novelty or general radical-free exhaustiveness is made.

### Independent review of the full-code/full-mark classification

## Full A₅ outer code forces the full mark

A continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). In the exact paired setting of `radical-free-a5-outer-codes.md`, let p≥1 and

 G={((u_i,v_i))∈S5^{2p}:sign(u_i)=sign(v_i) for all i},
 N=Soc(G)=A5^{2p},  C=G/N=F2^p,

with canonical inversion τ swapping every pair. Let K=K_D be the actual union of selected N-orbits indexed by D⊆C, with 0∈D and span(D)=C, in a faithful generated canonical folder of a finite simple nonassociative left Bol loop. Under the pinned canonical-folder, normal-quotient, selected-mark class-sum and A5 subgroup inputs, the argument below proposes D=C. It does not concern smaller outer codes, τ-fixed factors, factor permutation by G, or arbitrary extensions.

### Stabilizer, character screens, and 5 axes

Let H0=H∩N. Simplicity gives HN=G: otherwise HN is a nontrivial proper normal subgroup containing H and K's image covers its quotient, contrary to the strict normal-subloop test. Thus H→C is onto and

 |H0|=60^p/|D|.                                                  (1)

No individual H0 projection to A5 is full. Full-coordinate projections decompose into disjoint full twisted A5 strips, split from the residual proper-coordinate projection because proper A5 subgroups are solvable. H normalizes H0 and does not permute factors. For each strip its supported sign-code functionals must agree on all C; because C is full, its support lies within one τ-pair. A singleton gives a normal coordinate contained in H, contrary to faithfulness; a two-coordinate strip contains a pair of conjugate involutions, contrary to H∩K²=1.

We use the actual selected Λ=τK class-sum obstruction in `radical-free-fixed-factors.md`. For either of the real representations of S5 obtained by deleting the constants from the natural five-point action (degree 4) or its six-point action on Sylow-5 subgroups (degree 5), the restriction to A5 is irreducible. For the six-point action, the stabilizer D10 contains a C5 which fixes only its own Sylow subgroup and cycles the other five, proving two-transitivity; the natural five-point action is also two-transitive. Thus deleting the constants gives precisely these irreducible representations. On one paired tensor ρ⊗ρ, extend τ by the flip and act trivially on other coordinates. Every local 60-element selected sign-class sum is a positive scalar 60/d: it commutes with the irreducible A5² action, and each outside mark has flip trace d. Thus, if both H endpoint projections have nonzero fixed vectors, their tensor contradicts the transversal class-sum identity. This argument uses the actual selected classes and does not assume their number or D=C.

On each τ-pair at least one H0 endpoint carries 5: otherwise both H endpoint projections are 5-free, since H/H0 is a 2-group, hence intransitive on five points and each fixes a nonzero vector of the deleted natural representation. A proper 5-bearing A5 projection is C5 or D10. C5 is impossible because an odd code lift in H normalizes it but has square outside C5. Hence a 5-bearing projection is D10.

The H projection above a D10 normalizes it in F20=5:4 and fixes its normal C5 in the six-point Sylow-5 action. If the opposite H0 projection has neither 5 nor 3, it and its H extension are 2-groups; the latter is intransitive on six points, so both endpoints have fixed vectors in the deleted degree-five representation, a contradiction. Thus the opposite endpoint carries 3 once it is known to be 5-free.

Let W be H0's intersection with the product of the characteristic C5s in all its D10 projections. It is the actual normal Sylow-5 subgroup of H0 and is H-invariant: all 5-elements of H0 are supported on these coordinates, and H normalizes H0 and its coordinate projections. For each i, an H-lift of code e_i acts on W with eigenvalues ±2 at pair i and ±1 elsewhere. Polynomial spectral projections split W into pair-supported subspaces. Each is nonzero because every pair has a 5-bearing projection. Since D spans full C, its i-th bit takes both values; a pair-supported element with nonzero 5-coordinates on both endpoints would be in K² using a selected sign of the S5 conjugator. Hence each pair-supported subspace is a single C5 coordinate. It follows that W=C5^p, there is exactly one D10 endpoint per pair, and the other endpoint has 3 and no 5. Its proper A5 projection is therefore C3, S3, or A4. Orient the D10 endpoints first.

### The normal kernel and its pure V4 factors

For any h∈H with code c, h²∈H0 has first-endpoint D10-sign vector c: odd F20 elements square to reflections and even elements square into C5. Define

 J=ker(H0/W → C2^p),                                            (2)

where the homomorphism is the first-endpoint D10-sign vector. It is surjective and J is H-normal: H normalizes H0,W and F20 conjugation acts trivially on D10/C5. After removing W, J embeds in the direct product of the opposite endpoint projections. Each J projection contains a 3-element, because all 3-elements of H0 lie in the sign kernel and every opposite projection contains 3. If an opposite H0 projection is A4, the corresponding J projection is all of A4, since it is normal in A4 and contains 3. For S3/C3 endpoints the corresponding J projection is C3 or S3.

Let I be the set of A4 endpoints. The commutator J′ is abelian and lies in V4^I×C3^{I^c}, because A4′=V4 and S3′=C3. Its characteristic 2-primary part E=O2(J′) is H-normal, lies in V4^I, and projects onto every V4_i: projection commutes with derived subgroups and J projects onto A4_i.

At every i∈I, H's coordinate projection is S4=N_S5(A4): it contains A4 from H0 and an odd element from the e_i code lift. Its induced S4/V4≅S3 action on V4_i is irreducible over F2, and the sign of its permutation of the three nonzero V4 vectors is exactly the code character c_i, via S4/V4≅S3. This is not the determinant over F2, which is always 1. For distinct i,j these H-modules cannot be isomorphic, since their induced S3-sign characters are distinct coordinate functionals on the full code. The ambient module V4^I is a direct sum of pairwise nonisomorphic simple H-modules, hence is semisimple; any H-submodule projecting onto every summand is the full sum. Thus E=V4^I. Clearing first-coordinate C5 values using W gives literal pure V4_i subgroups inside H0, supported only at the i-th opposite endpoint.

### An A4 endpoint gives a collision

Suppose i∈I. Choose h∈H of code e_i. Its square has first-endpoint D10 signs e_i. For j≠i, its opposite coordinate is the square of an even element normalizing the relevant A4, S3 or C3 projection; it therefore has order 1 or 3. At i, the opposite coordinate is the square of an odd S4 element, hence has order 1 or 2 and lies in V4_i. Replacing h² by (h²)^3 kills all opposite coordinates outside i and preserves the i-th opposite square. Clear the residual first-endpoint C5 values using W. The resulting element of H0 has a single D10 reflection at first endpoint i, identity at all other first endpoints, and either identity or an involution at the opposite endpoint i. If necessary multiply by a pure V4_i element to make that opposite value nonidentity.

This is an involution with matched support on the one τ-pair i and identity elsewhere. The two nonidentity A5 involutions are conjugate; the selected 0-orbit of K realizes it in K². This contradicts H∩K²=1. Therefore no opposite H0 projection is A4.

### Full mark

Every opposite projection is now S3 or C3. Its C3 subgroup is characteristic, so H normalizes it at that coordinate and the full opposite H projection lies in N_S5(C3)=S3×C2. For any code c choose h∈H lifting it. Every opposite coordinate of h² lies in C3, while the first D10-sign vector is c. Cubing h² kills those opposite coordinates; clearing W removes residual first-endpoint C5 values, producing an element of H0 supported on the first endpoints with D10-sign vector c. As c is arbitrary and W=C5^p, H0 contains the independent product D10^p on the first endpoints.

Consequently H0=D10^p×L for an actual subgroup L≤S3^p on the opposite endpoints. If L has a nonidentity involution, choose D10 reflections on exactly the same coordinate support; the resulting element lies in H0∩K² by the unique involution class of A5 and the selected 0-mark. Hence L has odd order. Every odd-order subgroup of S3^p lies in C3^p, so |L|≤3^p. Equation (1) now gives

 60^p/|D|=|H0|≤10^p3^p=30^p,

hence |D|≥2^p. Since D⊆C and |C|=2^p, D=C. Moreover equality forces L=C3^p and H0=(D10×C3)^p.

Combined with the independently reviewed full-mark matrix classification, this removes its full-mark hypothesis for the stated full code. No source/classification proof has been rederived here, no literature novelty is asserted, and this argument does not resolve any other outer-code or factor-permuting case.

## Distinct parity-code characters collapse to the full code

A continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). In the paired canonical A5 setting of `radical-free-a5-outer-codes.md`, let G be the parity-code inverse image of C≤F2^p, τ swap each pair, and let the p coordinate functionals C→F2 be nonzero and pairwise distinct. Under the pinned canonical-folder, selected-class-sum and A5 subgroup inputs, a faithful generated canonical folder of a finite simple nonassociative left Bol loop has C=F2^p and D=C. Thus the reviewed full-code matrix classification applies. Repeated or zero code characters and factor-permuting overgroups are outside scope.

### Screens, 5 axes, and the A4 kernel

Simplicity and the normal-quotient criterion force H→C onto, since HN is normal and a proper HN would give equality in the quotient test. Write H0=H∩N. The selected Λ-class-sum proof in [the preceding full-code mark argument](#full-a₅-outer-code-forces-the-full-mark) applies to arbitrary C and actual spanning D: at every paired edge one proper H0 endpoint carries 5 and the other carries 3. The degree-four and degree-five real S5 representations used there have 60/d positive scalar for each selected local parity class. The explicit hypotheses of that argument are retained; no full-mark assumption is used.

H0 has no full A5 coordinate. Its full strips split from proper-coordinate projections by solvability. Since H normalizes H0, supported coordinates in a full strip have the same sign-code functional. By distinctness, such a strip lies within a single τ-pair: a singleton violates corefreeness and a two-coordinate strip has a matched involution collision. Each coordinate character is nonzero, so an odd H-lift rules out a C5 H0 projection: odd elements normalizing C5 square outside it. Thus the 5-bearing endpoint is D10.

Let W be H0's normal Sylow-5 subgroup, embedded in the characteristic C5s of the D10 endpoint projections. Each paired edge has nonzero W projection. For any two distinct code characters there is c∈C separating them; a lift h of c acts on the corresponding F5 coordinates with eigenvalues in disjoint sets {±2} and {±1}. Repeated polynomial spectral projections split W by code character, i.e. by τ-pair. Since D spans C, the selected signs cover both parity choices at each nonzero character. A pair-supported 5-element nonzero at both endpoints would therefore be in K². Every pair-supported W summand is at most one-dimensional and lies on one endpoint axis. Since every pair has a nonzero summand, W=C5^p and there is exactly one D10 endpoint per pair. The opposite H0 endpoint is a proper 5-free, 3-bearing A5 subgroup: C3, S3, or A4.

Use first-endpoint D10 signs to define J=ker(H0/W→F2^p). This is H-normal because F20 conjugation fixes D10/C5. Each J opposite projection contains 3. On an A4 endpoint, it is normal in A4 and contains 3, hence is all A4. Denote the A4 endpoints by R and the remaining C3/S3 endpoints by S. The subgroup J′ is abelian, lies in V4^R×C3^S and surjects onto V4 at each R coordinate. Its characteristic 2-primary subgroup E is H-normal, lies in V4^R and projects onto each V4_i. Each H-module V4_i is irreducible: H projects onto S4 at that endpoint because H0 projects to A4 and the sign character is nonzero. Its induced S3 sign, namely the sign of the permutation of the three nonzero V4 vectors, is the code coordinate functional c_i; it is not the determinant over F2. Distinctness makes these modules pairwise nonisomorphic. A submodule of their explicit semisimple direct sum that surjects onto every summand is the full direct sum. Thus E=V4^R, and clearing W supplies literal independent opposite-coordinate V4_i in H0.

### Parity forcing of the selected mark

Let c∈C be supported on R and h∈H a code-c lift. The first-endpoint D10 signs of h² are c. At every S endpoint h is even and normalizes C3, so its square has order 1 or 3. At every R endpoint its square has order 1 or 3 when c_i=0, and order 1 or 2 in V4_i when c_i=1. Taking h^6, clearing first-endpoint C5 values with W and adjusting the independent V4_i makes exactly the paired endpoints in supp(c) simultaneously involutory. If c≠0, this lies in K² through the selected 0-orbit, contradiction. Therefore the restriction C→F2^S is injective. Set k=dim C; then k≤|S|.

Put P=H0/W and choose a Sylow-2 subgroup P2. It embeds in C2^p_D×V4^R×C2^S, whose Sylow-2 factors are all elementary abelian, and

 dim_F2 P2 = 2p−v2(|D|).

The normal pure V4^R lies in P2. Consider the linear map P2→F2^S taking the differences between first D10 signs and opposite S3 signs on S. Its kernel is exactly pure V4^R. Indeed, if a kernel element has any nonzero first D10 sign, multiply by pure V4 factors to make every R endpoint support match the D signs; the S endpoint supports already match by the kernel condition. The resulting nonidentity element of P2 is an involution, and its inverse image has normal odd-order kernel W; Schur–Zassenhaus supplies an involution lift to H0. Its matched coordinate support is unchanged, giving an element of H0∩K². If all first signs vanish, the kernel condition also forces all S signs to vanish, leaving only pure V4^R. Hence

 2p−v2(|D|)−2|R| ≤ |S|,

so v2(|D|)≥|S|. As D⊆C and C→F2^S is injective,

 |S| ≤ v2(|D|) ≤ log2|D| ≤ dim C ≤ |S|.

All are equal: |D|=|C|, D=C, dim C=|S|, and C→F2^S is an isomorphism.

### The actual H0 and the normal-quotient collapse

The dimension equality says the difference map above is onto. For any c∈C, an H-lift h has h² cubed with first D10-sign vector c and all S opposite 2-signs zero. Clearing W and then the independent V4^R gives a pure first-coordinate sign element in H0/W with sign vector c and identity at all opposite coordinates. Choosing fixed reflections at the D10 endpoints gives the elementary subgroup C_D of all such sign vectors. Together with the normal pure V4^R it forms an elementary subgroup Q of dimension 2|R|+|S|, the full Sylow dimension. Choose P2=Q; the preceding difference-kernel argument applies to any Sylow subgroup. In particular, the S3-sign homomorphism vanishes on P2 and hence on all H0/W, and the first Dsign image of P2, and therefore of H0/W, is C.

The kernel of Dsign in H0/W therefore lies in A4^R×C3^S. Its order is

 |H0|/(5^p·2^dim C)=60^p/(2^dim C·5^p·2^dim C)
 = 4^|R| 3^p,

which equals the entire ambient A4^R×C3^S. Hence, with C_D the product of chosen D10 reflections indexed by C,

 H0=(C5^p⋊C_D)×A4^R×C3^S.                                   (3)

If R≠∅, kill exactly the two A5 socle factors on every pair in R and retain all pairs in S. This is a proper nontrivial normal subgroup: S is nonempty because its code projection is an isomorphism and C has positive dimension. The quotient of G is the full paired S5 group on |S| pairs, since C→F2^S is an isomorphism. Its K-image is the full anti-diagonal section, of order 120^|S|, so |Gbar|/|Kbar|=60^|S|. By (3), the H0 image has order 30^|S|; H maps onto C and its image contributes a further factor 2^|S|, hence |Hbar|=60^|S|. Equality contradicts the strict normal-subloop criterion. Thus R=∅. The isomorphism C→F2^S now has S all p coordinates, so C=F2^p and D=C.

The full-code/full-mark matrix theorem can now be invoked under its own exact hypotheses and review record. This proposed collapse does not classify repeated or zero coordinate characters, and it does not infer the independence of arbitrary stabilizer projections.

### Independent review of mark exhaustion and distinct-character collapse

## Full marks for arbitrary nonzero paired A₅ parity codes

A continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md). Let C≤F2^p be a binary code whose coordinate functionals are all nonzero, but possibly repeated, and let G≤S5^{2p} be its paired sign inverse image. Let τ swap each indicated pair. In a faithful generated canonical folder of a finite simple nonassociative left Bol loop, assume the selected mark is full, D=C, in the notation of `radical-free-a5-outer-codes.md`. Under the pinned canonical-folder, class-sum, A5 subgroup and involution inputs, the following argument proposes that all H0 strip components are paths and the code characters of distinct path components form a basis of C*. Thus repeated coordinate characters occur exactly along the edges of individual paths. The stabilizer is parameterized by a binary matrix on path components; the support digraph must be strongly connected. Path lengths and the simultaneous permutation orbit of this matrix are proposed complete loop-isomorphism data.

This is not an assertion for D≠C, zero coordinate characters, τ-fixed factors, factor-permuting overgroups, or groups merely containing A5 sections. The full-code input is reviewed; the selected-mark screens and distinct-character inputs are reviewed.

### Paths with constant component character

Simplicity forces H→C onto, since the preimage of its code image is normal and would otherwise give equality in the exact quotient test. H0=H∩Soc(G) has order 60^p/2^k, k=dim C. Full A5-coordinate strips of H0 split from the solvable proper-coordinate residual R, and have support size at least two. H normalizes H0 without permuting coordinates; thus the sign-code functionals on the coordinates of any one full strip are identical. Each τ-pair has the same character on both ends, so every connected component of the strip/leaf graph has a single character. It is nonzero by hypothesis.

For a component with n paired edges, m full strips, ℓ leaves and cycle rank b=n−m−ℓ+1, its projected G has order 2·60^{2n}; its K image has at most 2·60^n elements because D=C and the component character is nonzero. To bound the **actual** projected H, take its local even kernel. It normalizes each projected full H0 strip: no element of G permutes coordinates, and H normalizes H0. The normalizer of a twisted diagonal A5 strip in the corresponding product of A5 coordinates is exactly that strip, so these coordinates contribute at most 60^m. For a leaf with nontrivial proper H0 projection L, the local even image lies in N_A5(L), which is a proper subgroup of order at most 12 because A5 is simple. If L=1, the coordinate image of H is a quotient of H/H0≤C and is a 2-group, whose even part has order at most 4. Thus the local even kernel has order at most 60^m12^ℓ, and the full projected H has order at most 2·60^m12^ℓ. This bound does not identify the local even kernel with the projection of H0: code bits elsewhere may induce hidden even actions here. The cover G=KH gives 5^ℓ60^b≤120. With ℓ>0 this forces b=0 and ℓ=2. A leafless component has b=1 and is a cycle; populate each independent full strip by an involution from the unique A5 involution class and all other factors by identity. Every edge then has matched involutions, producing H0∩K²≠1. Hence all components are paths. Let c be their number and m the total number of internal strips. Since p=m+c,

 |R|=60^c/2^k.                                                   (1)

The [positive selected-Λ class-sum screen](#full-a₅-outer-code-forces-the-full-mark) applies componentwise: label its edges with the real deleted natural degree-four S5 representation, use invariant tensors across full strips, and use fixed vectors at proper leaves. Straighten strip twists along the path using τ-compatible coordinate automorphisms. On every full strip the actual H-normalizer acts through the same S5 automorphism on its two coordinates, so its real orthogonal representation fixes the canonical bilinear tensor; the invariant is for H, not merely H0. Each component has at least one 5-bearing leaf. Every such projection is D10: C5 is impossible because its nonzero code character has an odd H-lift which normalizes it but whose square is outside it. Since |R|_3=3^c and each proper A5 leaf has at most one factor 3, two 5-bearing leaves on one path would leave fewer than c 3-bearing leaves globally. Thus every component has exactly one D10 leaf and one opposite 3-bearing C3, S3, or A4 leaf. The normal C5^c is contained in R by full 5-saturation. A Sylow-3 subgroup of R embeds in the product of the c opposite-endpoint Sylow-3 groups, has their full order 3^c, and hence is their direct product. These are actual independent C3_i subgroups of R.

### Parity, modules, and collapse of the code

Write R_indices for the components whose opposite projection is A4 and S_indices for those whose opposite projection is S3 or C3. Put r=|R_indices|, s=|S_indices|, so c=r+s. Let W=C5^c and let J be the kernel of the D10-sign map on R/W. It is H-normal. It contains all independent C3_i. At an A4 opposite endpoint J projects normally onto an A4 subgroup containing 3, so its projection is A4. Its commutator is abelian and lies in V4^r×C3^s; E=O2(J′) projects onto each V4_i and is H-normal. The independent C3_i in R distinguish the V4_i as simple H-modules even if code characters repeat: C3_i acts nontrivially only on V4_i. Consequently E=V4^r, and clearing W produces pure opposite-endpoint V4_i factors in R.

The projection C→F2^{S_indices} is injective. If a nonzero code vector is supported only on R_indices, take an H-lift, square and cube it. Its D10 endpoint signs are the chosen code vector; its S endpoints are identity after cubing. Clear W and use the pure V4_i to match the signs on R. Full strips are independent, so clear them on inactive paths and choose appropriate involutions along active paths. The unique A5 involution class then gives a nonidentity H0∩K² element. Thus k≤s.

A Sylow-2 subgroup P of R/W is elementary abelian in C2^c_D×V4^r×C2^s, of dimension 2c−k by (1). Its kernel under the map of S-coordinate differences between D10 and S3 signs is exactly pure V4^r: any further element can be adjusted by those pure V4s to match support on all components, yielding an involution collision after lifting through the normal odd-order subgroup W by Schur–Zassenhaus and filling independent strips. Therefore 2c−k−2r≤s, so s≤k. It follows that s=k, the projection C→F2^S is an isomorphism, and P has dimension 2r+s.

For every c0∈C, an H code-c0 lift, squared and cubed and then adjusted by W, pure full strips and pure V4^R, supplies a pure D-sign element with sign c0 and zero opposite S3 signs. These elements together with pure V4^R form an elementary subgroup of dimension k+2r=dim P, hence a Sylow subgroup. Therefore all R/W have zero S3 signs and their D-sign image is C. Its D-sign kernel lies in A4^R×C3^S and has order 4^r3^c, equal to that ambient product. Thus

 R=(C5^c⋊C_D)×A4^R×C3^S,                                    (2)

where C_D denotes chosen D10 reflections indexed by C.

If r>0, kill all socle coordinates on R components and retain all S components. This is a proper nontrivial normal quotient. Since C→F2^S is an isomorphism, the quotient has independent common-parity S5 code on the retained paths and full marked section. Its |Gbar|/|Kbar| is ∏_{i∈S}60^{n_i}. The H0 image has size ∏60^{n_i−1}30; H contributes the full code factor 2^k=2^{|S|}. Thus |Hbar|=∏60^{n_i}, contradicting the strict normal-quotient criterion. Therefore r=0, c=k, and component code characters form a basis. In particular all repeated coordinates lie on a common path component, and H0 is the product of internal full A5 strips and D10×C3 endpoints on each path.

### Matrix and all normal quotients

Normalize the c path components and their endpoint pairs by τ-compatible coordinate automorphisms. The quotient N_G(H0)/H0 has one fixed outer sign bit c_i per component and one hidden endpoint bit t_i from N_S5(C3)/C3. H/H0 is the graph t=A c for a binary c×c matrix A; odd components of a code lift on full internal strips are unique modulo H0. Conversely every A gives an actual subgroup of the right order. For positive path lengths n₁,…,n_c, every constructed loop has order 2^c·60^(n₁+⋯+n_c); its entire canonical group is the product, over i, of the common-parity subgroups of S5^(2n_i).

The marked-square collision test holds for every A: if an element has a nonzero code bit on any component, its D10-side endpoint is an odd F20 element of order 4 whereas its opposite odd endpoint has order 2 or 6, so the endpoint values cannot have the conjugate-inverse relation propagated along that path. If its code is zero, its opposite endpoints are C3 while its first endpoints are D10; their only common nonidentity orders are absent. Thus H∩K²=1, K is a transversal to all H conjugates, K generates G, and H is core-free.

For any normal quotient, let t_i count touched internal strips of component i, f_i count its edges with both incidences retained, and eD_i,eC_i indicate selected endpoints. Let S be the set of selected C3 endpoint components. The socle-coordinate kernel consists of any subset of A5 coordinates; its allowed outer kernel W is a code subspace supported only on fully killed components. Then

 |πH|/(|πG|/|πK|) =
  ∏_i 60^{t_i−f_i}10^{eD_i}3^{eC_i} · 2^{c−dim(W∩ker A_S)}. (3)

Here the H0 image is the product of the indicated full-strip and endpoint orders. The image of H/H0 is controlled by c mod W and the selected hidden signs A_Sc. The factor in (3) is its image size. Every touched paired edge contributes 60 possibilities per allowed sign to the K image, and fully killed component signs are counted modulo W; cancellation gives |πG|/|πK|=60^{Σ f_i}.

For a fully retained component the baseline factor before the final binary term is 1/2, for an empty component it is 1, and for a nonempty partial component it is at least 3: a partial path has t_i−f_i≥0, and if no endpoint is retained then t_i−f_i≥1. The binary factor is at least 2^{number of nonempty components}, since W is supported on empty components. Thus any partial component forces strictness. If components are only fully retained or fully killed, and I is the nonempty proper retained set, the worst W is all code supported on I^c and (3) reduces to 2^{rank A_{I,I^c}}. The remaining empty/full endpoint cases correspond to the socle and trivial normal subgroups. Therefore the exact normal-subloop test is equivalent to strong connectivity of the digraph i→j when A_ij=1, i≠j. The constructed action is imprimitive because H is strictly inside the proper product of its vertex normalizers, so simple nonassociative Moufang loops are excluded by the pinned C0001 interface.

### Isomorphism interface

The full A5 strips are intrinsic as the nonabelian minimal normal subgroups of H0; the residual leaf group is solvable. Their supports and the τ-pairs recover the individual paths and their lengths. Endpoint projections D10 and C3 have different orders, so after orienting paths an isomorphism cannot reverse a path while retaining that orientation. A τ-compatible canonical-folder automorphism permutes equal-length paths and applies the same Aut(A5)=S5 automorphism along each connected path. All pairs (D10,C3) are simultaneously conjugate because N_S5(D10)=F20 acts transitively on the ten C3 subgroups. Its stabilizer of a fixed pair has order 2 and acts trivially by conjugation on the elementary-abelian endpoint normalizer quotient. Hence it does not change A. The proposed isomorphism criterion is simultaneous permutation of rows and columns preserving path lengths; the exact-source reviews below include this isomorphism argument.

The p=1 path recovers the two reviewed S5-factorization loops, and the single all-ones character case forces c=1 and gives the two common-parity loops of every path length. No literature novelty or completion outside the stated scope is claimed.

### Independent review of the repeated-character full-mark theorem

## Zero characters in the full-mark classification

Let C≤F2^p be any paired parity code, including zero or repeated coordinate characters, with the same faithful canonical group, pair-swapping τ and full mark D=C. If C is nontrivial, no coordinate character is zero and the preceding path/matrix classification applies. If C={0}, the group is A₅^(2p) and the [reviewed pure-A₅ path theorem](radical-free-a5-path-classification.md), with inversion exhaustion, gives its unique class of order 60^p. Thus these two branches give the proposed full-mark classification for every paired nonpermuting A₅ parity-code group. Arbitrary marks, τ-fixed factors and factor-permuting overgroups remain outside scope.

Here are the changes needed to allow zero characters; all folder and source interfaces are those of the preceding theorem reviewed. A strip component still has a constant character. For a zero-character component its projected group and K have orders 60^(2n) and 60^n; the actual even-normalizer argument bounds its H image by 60^m12^ℓ. For a nonzero character the same three bounds have the factor two from the preceding proof. Hence the component inequality is 5^ℓ60^b≤60α, with α=1 or2. Both regimes force paths after the same leafless-cycle collision. If c is the number of paths and k=dim C, the proper residual has |R|=60^c/2^k.

The degree-four positive class-sum screen also works on an entirely even component. Every path has a 5-bearing leaf; the full 3-part 3^c then forces exactly one such leaf and a 3-bearing opposite leaf. The first projection may now be C5 as well as D10, but C5 is possible only for a zero character: an odd lift still has square outside C5. The 5/3 saturation again supplies actual independent W=C5^c and opposite C3_i subgroups.

In the previous parity argument assign D-sign zero to a first endpoint with projection C5. Let r count A4-opposite paths and s count the remaining C3/S3-opposite paths. The same J′ argument, using the independent C3_i, gives literal pure V4^r. If a nonzero code vector vanishes on all s remaining paths, squaring and cubing a code lift, clearing W and adjusting pure V4 factors gives the same matched-involution collision; a zero-character first endpoint automatically has sign zero. Thus C→F2^s is injective. The Sylow-two difference-kernel argument is unchanged with those zero sign coordinates: its dimension is 2c−k, its kernel is pure V4^r, and so s≤k. Therefore s=k and C→F2^s is an isomorphism.

The pure D-sign lifts indexed by C and the independent V4^r form a full-dimensional Sylow subgroup as in the preceding proof. Thus every residual D-sign lies in C and all opposite S3 signs vanish. In particular a zero-character first endpoint must have H0 projection C5, not D10. The same order calculation for the D-sign kernel now gives the actual residual

 R=(C5^c⋊C_D)×A4^r×C3^s,

where C_D is zero on zero-character coordinates. If k>0 then s=k>0, and the s component characters are a basis, so none is zero. If r>0, retain exactly these s complete components and kill all r others. The projected H has order ∏60^(n_i−1)·30·2^s=∏60^n_i, exactly |Gbar|/|Kbar|, contradicting the strict normal-subloop criterion. Hence r=0 and there are no zero-character components. The preceding construction and isomorphism theorem then applies.

If k=0, the parity calculation gives s=0 and R=C5^c×A4^c. Retaining a single component gives the same forbidden equality whenever c>1. Thus c=1, the already reviewed pure-A₅ path. Its existence and unique isomorphism class are supplied by that source; this argument does not claim a new construction in the trivial-code branch.

### Independent review of the zero-character full-mark assembly

## Arbitrary selected marks for paired nonpermuting A5 codes

Let C≤F2^p be any binary code, including zero or repeated coordinate functionals. Let G≤S5^{2p} be its paired-sign inverse image, and let τ exchange the two members of each prescribed pair. In a faithful generated canonical folder of a finite simple nonassociative left Bol loop with these exact G and τ, write K=K_D for the actual selected union indexed by D⊆C, with 0∈D and span(D)=C. Subject to the cited folder, character and A5 subgroup inputs, this note proposes that **D=C**. The already reviewed full-mark assembly then classifies this entire paired, nonpermuting setting. No claim concerns τ-fixed factors, factor permutations by G, other socles, or arbitrary groups merely having A5 sections.

The selected-mark and canonical-folder interface is `radical-free-a5-outer-codes.md`; its C0001 and C0007 dependencies and source qualifications apply. The positive actual-Λ class-sum test is the reviewed A5 character interface in `radical-free-fixed-factors.md`, and the full-mark path/matrix assembly is. The support-parity, A5 subgroup and normal-quotient inputs are pinned in `radical-free-involution-support.md`. The new proof below is not an exact-source independent review or a reproof of these inputs.

### Path and endpoint structure for the actual mark

Simplicity forces H→C onto: HN is normal for N=Soc(G), and a proper HN containing H gives equality in the exact normal-subloop test. Write H0=H∩N, k=dim C and α=|D|. Then |H0|=60^p/α. The full-coordinate A5 strips of H0 split independently from the residual proper-coordinate group R, because proper A5 groups are solvable. H normalizes each strip and cannot permute the socle coordinates, so every strip support has a single code functional; the τ-edge graph consequently has one constant character per connected component. Full strips have degree at least two by corefreeness.

For a component with n edges, m strips, ℓ proper-coordinate leaves, cycle rank b_graph=n−m−ℓ+1 and local character ε, let t=1 if ε=0 and t=2 otherwise. The projected G has order t·60^{2n}, and the projected K has at most t·60^n elements. Its actual projected H has order at most t·60^m12^ℓ: the local even kernel normalizes each twisted diagonal full strip, whose normalizer inside its A5 coordinate product is the strip; at a nontrivial proper leaf L it lies in the proper normalizer N_A5(L), of order at most 12; at a trivial leaf the coordinate H-image is a quotient of H/H0≤C and is a 2-group, with even part of order at most 4. This bound explicitly allows hidden local even actions not arising from H0. The cover G=KH implies

 5^ℓ60^{b_graph}≤60t.                                           (2)

A component with leaves must be a tree with precisely two leaves. A leafless component is a cycle; put transported involutions from the unique A5 class on all its independent full strips and identity elsewhere. This produces a matched-support involution in H0∩K² using the selected zero orbit. Thus every component is a path.

On each path, the actual positive Λ-class-sum screen gives exactly one 5-bearing leaf and one 3-bearing, 5-free leaf. For the first assertion, label its edges by the deleted natural degree-four real S5 representation. If neither H0 leaf carried 5, neither H leaf would, since H/H0 is a 2-group; both H projections would be intransitive on five points and fix nonzero vectors. Together with the strip-invariant tensors, the positive selected class sum yields a contradiction. A proper 5-bearing A5 leaf is C5 or D10. Its H projection normalizes its characteristic C5, so lies in F20, which fixes a point in the six-point action on Sylow-5 subgroups. If both endpoints carried 5, their H projections would both fix vectors of the deleted degree-five representation; if the other endpoint were 3-free, its H projection would be a 2-group, intransitive on six points, and likewise have a fixed vector. Either contradicts the degree-five class sum. The 5-bearing leaf is D10 when its component character is nonzero: an odd H-lift normalizing C5 would square outside C5. For a zero character it may be C5 or D10. The opposite proper projection is C3, S3 or A4.

For completeness, the scalar positivity used here is independent of the actual selected D. For a real orthogonal S5 representation ρ of degree d whose A5 restriction is irreducible, extend the local tensor ρ⊗ρ to τ by the flip. A local 60-element selected outside class has trace d per element and commutes with irreducible A5², so its sum is the scalar 60/d>0. Tensoring these local sums and summing the actual selected global classes remains positive; no projected subgroup is treated as a folder.

Let c be the number of paths, r the number of A4-opposite paths and s=c−r the number of C3/S3-opposite paths. Put a=v2(α), b=v3(α). The forest identity gives

 |R|=60^c/α.                                                     (3)

### The 2-deficit and the actual residual kernel

Assume a<s. Let P be a Sylow-2 subgroup of the actual R. It is elementary abelian, since the endpoint Sylow-2 groups are C2 or V4. Its order is 2^{2c−a}. Apply the matched-support parity lemma, using the two leaves of each path as a block. A D10/C5 first endpoint has 2-part at most 2; an A4 opposite has 2-part at most 4 and an S3/C3 opposite at most 2. Thus the lemma's projection target bound is at most 4^r2^s=2^{2c−s}<|P|. It gives a nonidentity involution of R with constant support across every pair of leaves. Fill the independent full strips with the unique A5 involution class on active paths and identity otherwise, yielding an H0∩K² collision. Hence

 a≥s.                                                             (4)

Let W=R∩C5^c, using the characteristic C5 in each C5/D10 leaf projection. Every 5-element of R lies in this product, so W is the actual normal Sylow-5 subgroup; it need not be the full product and may be correlated. Put X=R/W. It embeds in

 C2_D^c × A4^r × ∏_{i∈S}(C3 or S3),

with the first sign coordinate possibly trivial at a C5 leaf. Let P0 be the intersection of X with C2_D^c×V4^r×1_S, and E=P0∩V4^r. These are normal elementary abelian 2-groups in X. The opposite-coordinate projection of X′ lies in V4^r×C3^s and X′ is abelian. At an A4 endpoint, X′ projects onto A4′=V4. Therefore the 2-primary part O2(X′), a characteristic subgroup of X′ and hence normal in X, lies in E and projects onto every V4_i. In particular E has full coordinate support; no subdirect-product splitting is assumed.

Choose Q∈Syl3(X). Its order is 3^{c−b}. It embeds in the product of the chosen opposite-coordinate C3 subgroups, since first D-sign coordinates are 2-groups. Its projection onto every C3 coordinate is nonzero: the corresponding actual 3-bearing endpoint projects to C3, S3 or A4, and a Sylow-3 subgroup projects onto a Sylow-3 subgroup of that projection. The conjugation action of Q on P0 is trivial on D signs and nontrivial irreducible on each V4 coordinate. Maschke averaging in characteristic two gives

 P0=U_D⊕E,  U_D=P0∩F2_D^c.                                    (5)

For any code vector d∈C, choose h∈H lifting it. At each first endpoint the D-sign of h^6 is the component character evaluated on d: an odd F20 coordinate has square a reflection, while an even coordinate has square in C5. At each S3/C3 opposite endpoint h normalizes its characteristic C3 in N_S5(C3)=S3×C2, whose exponent is 6; at an A4 endpoint h normalizes A4 in S4, whose sixth powers lie in V4. Project h^6 to R/W after removing full-strip coordinates. It belongs to P0 and has D-sign vector d. Averaging it over Q preserves its D signs and kills the nontrivial V4 isotypic constituents, yielding the pure vector d in U_D. Therefore

 C⊆U_D.                                                           (6)

This uses the actual selected component characters, including zero characters, and no assumption that Q is H-normal.

### The 3-deficit and bad blocks

For each A4 endpoint i, Q acts on V4_i through a nonzero character λ_i:Q→C3. Group coordinates into blocks of proportional characters {λ_i,−λ_i}. On block j, of size n_j, the Q-isotypic submodule E_j is F4-linear and has nonzero projection to every coordinate. Call j **bad** if E_j contains no vector with all n_j coordinates nonzero. Such a block has n_j≥2.

All coordinates of one block have the same code character χ_j∈C*. To see this, for any h∈H, multiply h by an H0-lift of an element of X so that its induced leaf action normalizes Q; Sylow conjugacy supplies the adjustment and its lift lies in H0, so the code is unchanged. At an A4 endpoint, conjugation on its C3 quotient is inversion exactly when the corresponding S5 parity bit is 1. Since one automorphism of Q acts on proportional nonzero characters, their inversion signs agree. This uses the sign of S4/V4≅S3 acting on the three nonzero V4 vectors, not the determinant over F2. Zero code characters are allowed.

Let C0=ker(C→F2^S), where S indexes the s non-A4 opposite paths. The restrictions of the bad-block characters must span C0*. Otherwise choose 0≠d∈C0 annihilating each bad character. The pure D-sign vector d is in U_D by (6). For each good block on which d is active, select an E_j vector with all coordinates nonzero; set E to zero on inactive blocks and all bad blocks. Coordinates in each block have a common code character, so the selected E support agrees exactly with d on all A4 paths, while both supports are zero on S. This produces a nonzero involution in P0 with matched leaf support. Lift it to an involution through the odd normal W by Schur–Zassenhaus. A first-endpoint coordinate of zero D-sign lies in C5 and must therefore be the identity in this involution lift; all opposite endpoint coordinates are unchanged. Thus the matched supports persist. Fill the independent full strips on active paths; the selected zero orbit gives a forbidden H0∩K² element. Hence

 #bad blocks ≥ dim C0 ≥ k−s.                                     (7)

The coordinate homomorphisms λ_i on the Sylow-3 group Q have relation space of dimension b. Indeed Q injects into the product of opposite-coordinate Sylow-3 groups C3^c, since all first coordinates are 2-groups, and |Q|=3^{c−b} by (3). In a block of n_j proportional coordinates, the n_j−1 signed coordinate equalities are independent. For distinct blocks these relations have disjoint support, so they remain independent. Therefore

 b≥∑_{j bad}(n_j−1)≥#bad blocks≥k−s.                            (8)

Combining (4) and (8) gives a+b≥k. But 2^a3^b divides |D|≤|C|=2^k. If b>0, then 2^a3^b>2^{a+b}≥2^k, contradiction. Thus b=0, and a≥k. The same cardinality bound forces |D|=2^k and hence D=C. For k=0 this conclusion is immediate, and the argument is consistent with zero characters.

The reviewed full-mark assembly then supplies the classification in the stated paired nonpermuting A5 setting. This deduction is not a review of that assembly or any general radical-free classification.

### Independent review of arbitrary-mark exhaustion
