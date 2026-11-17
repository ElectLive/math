# Independent mathematical review: loop decomposition and intrinsic deletion decks

**Historical research-review record.** This public copy neutralizes worker identifiers and rewrites reproduction paths. The original hashes identify the reviewed source, not these presentation-normalized bytes. Research-workspace CI/rendering limitations below describe that earlier delivery; see the public [publication record](../PUBLICATION.md) for this mirror.

## Verdict, reviewer, and exact scientific source

**Verdict: the four reviewed manuscripts provide complete conventional proofs of their stated results under their explicit hypotheses and established dependencies. No blocking mathematical defect or counterexample was found. All four independently rerun research checkers passed.** This acceptance concerns the stated restricted reconstruction and decomposition results; it does not accept a solution of graph reconstruction or a classification of arbitrary Bol loops.


Workspace: [Mira-Cult/math-wip PR #447](https://github.com/Mira-Cult/math-wip/pull/447), branch `research/0323-loop-decomposition`, stacked on PR #446.

Final scientific revision reviewed: **`61f86bbbab630fc45a5ad4a6258e5562dceb1e9b`**.

Git tree: **`2d0abe16bcecce43746b51f9c8f78617c7c31577`**.

I verified HEAD, the tree, and byte equality between each scientific working file and `git show` at this revision. The full audit and independent executions were performed on scientific revision `53446629822352b0682c41507832ccf04e22b446`, tree `79a4f156433ecd417cb10d9d53d33da22f656dd9`. I then reviewed its exact diff to the final revision: only the indexed-family notation in condition (6) and the phrase “central coordinate space” in place of “center” changed, both in `loop-deletion-decks.md`. Both are correct clarifications of the proofs' existing conditions. The other seven scientific files, including all four checkers, are unchanged. No test rerun was needed for these two prose/notation corrections, and the final verdict binds the final source listed here.

I also compared the earlier frozen files to my preliminary review snapshot, reviewed the intervening changes, and verified that the three PR446 construction/payoff manuscripts remain byte-for-byte identical to their reviewed scientific source `9059767c0ef28809bbe17de8a71ba0a8b11d0485`. The PR446 delivery pin is `7653409e6155cd87c7f91ba810b155f517c7f44b`.

All paths in the following table are relative to `problems/0323-finite-simple-non-moufang-bol-loops/`.

| Reviewed scientific source | SHA-256 |
| --- | --- |
| `manuscripts/bruck-extension-decomposition.md` | `08db9198adae2eaa9653510b4aa9c54d87a807beeb474b692041e278261fa6d9` |
| `manuscripts/loop-deletion-decks.md` | `9b63819dc18109f76662d564f65c505eefb7cbbccd6729b4e4e4cdf37ccb92a9` |
| `manuscripts/loop-deck-subloop-census.md` | `e3a3d368e1ff0dde6fd91802526d6c9927d5b0caf7f3bddabfa5c87543f259e6` |
| `manuscripts/loop-defect-graphs.md` | `37467525dd294bd9b1a7270818a06ac256a70586fc1e69268e9dcda8af437af5` |
| `code/check_bruck_decomposition.py` | `3bcdbe48a2147c8708f94820292e0382407fcbab8381384269612f8b8a063248` |
| `code/check_loop_deletion_decks.py` | `b1e7354852ca566da9c83f4ee7d9b3cd85fb2e0a9e7071251fbf492b01697bc6` |
| `code/check_loop_deck_census.py` | `af5452f3d9bd7f5d96add27e3c9e50d5e947b61e0741f94c34d262b8aae8980b` |
| `code/check_loop_defect_graphs.py` | `804b0152cf09ddf3978d5ec6ec05199b3d756745feaf9cf5cb1254ec2953b241` |

I additionally read the frozen `LOOP_DECOMPOSITION.md`, the continuation's navigation/reference changes, and the new code README section for consistency. I checked the four pending navigation-only diffs in `LOOP_DECOMPOSITION.md`, the two affected `OPEN_PROBLEMS.md` files, and the 0354 README. Their equivalence statements and the extra composite-identity paragraph accurately reflect the accepted results; those pending metadata bytes are not part of the scientific pin. The working agreement, research protocol, research order, and the PR446 scientific/review dependencies were part of the review context. The two formula-rendering defects and incomplete Griggs–Širáň–Richter credit identified during preliminary review are corrected in the frozen source. The discrete-category wording of the deck functor is precise.

## 1. Central Bruck extension rigidity and decomposition

### Extension rigidity

Theorem ER is valid with its exact assumptions: two central extensions of the **same elementary abelian quotient and kernel**, both left Bruck loops of exponent the **prime** p, with the same associator function. It does not require trilinearity. Inverse-compatible sections are available for odd p by pairing quotient vectors with their negatives, and for p=2 because every element is an involution. Their factor sets satisfy the two identities stated in the proof.

Subtracting the factor sets gives an associative central-extension law. The inverse compatibility and automorphic inverse property make that group abelian. Subtraction of the p-th-power sums proves exponent p, so the resulting exact sequence of vector spaces splits. The displayed coboundary and the sign of the resulting coordinate-change isomorphism are correct. Thus the argument really removes the residual factor-set ambiguity; it does not infer extension uniqueness merely from the appearance of a trilinear tensor.

The automorphism exact sequence follows correctly: an isomorphism of the quotient/kernel tensor data lifts by ER, and the kernel is exactly the linear central shears. A general splitting is not claimed. The later explicit semidirect-product formula is restricted to the reduced one-marker family at p different from three, where the intrinsic hyperplane and marker line force the asserted block action.

The assumptions cannot be silently discarded. The manuscripts give appropriate controls for loss of AIP and loss of prime exponent. The two binary Moufang extensions with identical associator data later in the defect manuscript are outside the exponent-p Bruck rigidity theorem, so they do not contradict it.

### Removing the central factor and decomposing the core

For a finite prime-exponent Bruck loop whose associator subloop A is central and whose induced associator is trilinear, A and L/A are elementary abelian. The quotient is abelian because it is a group with automorphic inversion. The common radical of the tensor lifts to the nucleus. The proof that the nucleus equals the center in this setting is sound and uses the nuclear reassociation and inverse property explicitly.

A complement S to A in the center gives a genuine central direct factor: the constructed retraction onto S is a loop homomorphism. Its dimension is intrinsic. Different complements are related by central shears, which proves that the complementary core's **isomorphism type** is intrinsic without falsely asserting a characteristic embedded complement.

The balanced trilinear centroid is a commutative algebra under fullness and zero common radical. Its primitive idempotent frame is unique as an unordered family. The block restrictions are full and radical-free, and the displayed factors are actual subquotients of the existing core. ER then identifies their product with that core. This avoids an unproved integration theorem for arbitrary tensors. Conversely, a nontrivial direct decomposition yields the required centroid idempotents; a putative associative factor would contribute radical. Theorem RD therefore gives the claimed complete decomposition within its stated class.

### One marker, orthogonal blocks, and the modified graph functor

The centroid computation for a full radical-free one-marker alternating map is correct at **every prime**, including two and three. It first eliminates marker components of P(W), then eliminates the vertex component of P(m), and finally forces scalar action on domain and output. No division by 2 or 3 occurs. Thus the nonassociative core is directly indecomposable, even for a graph with several nontrivial connected components.

The common-marker fiber product and its central quotient have the stated multiplication and kernel. Independent output blocks give an isomorphism; shared output requires the central relation. The bilinear centroid and self-adjoint-idempotent arguments correctly distinguish independent-output and general orthogonal decompositions. For a graphical map, the coefficient proof eliminates all off-diagonal entries, including the characteristic-two leaf case. Graph components are therefore intrinsic bilinear blocks, while the original one-marker loop can remain directly indecomposable.

The component-marker modification has the stated order, disjoint-union/direct-product behavior, and unmarked recovery. Its reduced factors are recovered through RD and then the established graph-loop theorem. Only the isomorphism groupoid and the specified disjoint-union maps are claimed; the induced-embedding counterexample correctly explains the stronger functoriality failure. The Z/4 example correctly shows why the field splitting argument does not extend automatically to rings.

## 2. Intrinsic frame decks, recognition, and gluing

### Recognition and generated cards

For nonzero full B at a fixed prime p different from three, the right-alternative locus identifies W as its unique largest linear subspace. The codimension estimate follows from a nonzero scalar specialization of B. An admissible marker is exactly a nonzero marker scalar plus a radical vector. The repeated-argument condition is essential: merely being transverse to W is insufficient, as the explicit K2 example shows.

The recognition conditions are sufficient because the independent nonzero basis pairings identify a graphical alternating map, and ER supplies the missing central-extension uniqueness step. They are necessary by the graph construction. The associative branch and exclusion of the trivial loop are consistent with the original one-marker convention. The conditions do constitute a search for a graphical presentation; the text does not disguise this as efficient extraction of canonical vertices.

The generated-card lemma is correct for arbitrary allowed lifts. Their central coordinates extend to a linear section on the retained quotient space. Closure introduces only the span of retained associators, and those associators are generated by the retained tuple. Arbitrary central lifts therefore do not produce extra central dimensions. This is precisely why adjoining the entire parent associator group would give the wrong cards.

The graph defined by any admissible frame is equivalent to the original graphical alternating map. **He–Qiao, arXiv:2003.07200v2, Proposition 1.2** then gives graph isomorphism, so the abstract card multiset is independent of all admissible choices, with multiplicities. Its applicability over F2 and with isolates is correct. This is an established external input, not a result newly proved in this continuation.

### Intrinsic type does not mean canonical embedding

The central-shear and general-linear-group examples correctly obstruct a canonical n-member embedded deletion family. The edgeless case, complete graphs, bad-marker example, dependent-frame example, full-central-preimage error, maximal-subloop alternative, retraction-kernel alternative, and split-quotient alternative all have the claimed scope. In particular, the kernel census gives only the degree multiset, and C6 versus two triangles is a valid loss example.

The exact reconstruction equivalence is sound for n at least three and competitors restricted to the recognized graphical Bruck family. It uses faithfulness on parent and card loops separately. It does not extend to arbitrary loops. The n=2 failure is explicit, and the regular/tree/disconnected controls are properly treated as established graph reconstruction cases.

### Central gluing obstruction and all-hyperplane repair

Identifying the two edge coordinates of the matching gives a central quotient that restricts injectively to each of the four specified coordinate-deletion cards. The parent orders differ, and the scalar rank-four target has no graphical frame. These facts are stated explicitly. Thus this is a legitimate failure of naive gluing in the enlarged alternating-map universe, **not** a graph reconstruction counterexample and **not** a same-parent-order counterexample.

The all-hyperplane deck is intrinsic for the broader alternating-map suspension family at p different from three. Its reduced output spaces and generated-card rule are handled correctly. Its exact matching/scalar example and scalar rank-reconstruction theorem follow from the hyperplane restrictions of a symplectic form and its radical. The n=2 exception is sharp for the convention used. This is a genuine restricted algebraic reconstruction theorem for a different deck; it is not advertised as a new reconstructible graph class.

Aligned card embeddings recover a graphical parent for the stated elementary reason, but no proof is offered that unaligned abstract cards determine those alignments. That remains an explicit open obligation rather than an assumed lemma.

## 3. Full associative-subloop census from unaligned cards

The full-support Gaussian-binomial inclusion-exclusion formula is correct. The support-component argument classifies an arbitrary isotropic subspace by its component lines and a full-support subspace of their direct sum; it does not assume maximal isotropy. Consequently the count of all isotropic spaces has the stated transform of the established subgraph component polynomial.

For p different from three, a projected space crossing W is associative exactly when its intersection with W is isotropic and its transverse shift is orthogonal to that intersection. In those circumstances the correction vanishes on the entire projected space. Spaces contained in W also have zero correction. This proves the projected-space count and, crucially, makes every associative preimage an elementary abelian group.

An associative subloop with quotient image U and central intersection J is therefore the graph of a linear map from U to Z/J after choosing a splitting. The Gaussian factor for J and the factor `p^(dim(U) dim(Z/J))` give the full census, including subloops not containing the center. The theorem's prime-field restriction is essential and retained. The characteristic-three extension uses elementary abelian associative preimages; the binary Moufang extension claims only the narrower census its proof supports.

Reconstructing the component polynomial uses proper-subset double counting plus a correct component-count formula that handles isolates. The weighted domination expansion follows from inclusion-exclusion. Its proper-subset terms come from the cards, and its top term is recovered through component sizes, using the standard disconnected-component argument when necessary. No cross-card alignment or solution of graph reconstruction is used. The warning that a naive card sum of maximal-group polynomials picks up almost-dominating subsets is correct.

The five-vertex pair has the stated component polynomial and different degree sequences. I checked the small induced-subset counts and dominating-support formulas. Hence the two loops have the same complete multiset of abstract associative-subloop types for every allowed prime, but different maximal-associative counts. This is a valid obstruction to recovering inclusion data or the parent from the census. Their deletion decks are different, as the text states.

The payoff remains substantive but enumerative: it counts all associative pieces from every graphical deck without assembling the parent extension. Existing graph-polynomial reconstruction and isotropic-counting mechanisms receive appropriate credit.

## 4. Defect graphs and actual loop structure

The local and translated permutations are correctly defined using multiplication and division. The left Bol inverse-defect identity proves symmetry of their averaged matrices, with multiplicities. Symmetry is not asserted for arbitrary loops, and general positivity is only asserted after laziness. The trace identity and the identification of local isolated vertices with the **right** nucleus are correct. Naturality, edge collapse under general homomorphisms, and the stronger surjective Markov lumping are distinguished.

The component theorem works for every finite loop. The local defects generate the left point stabilizer; the translated defects generate all point stabilizers, a normal subgroup containing the original stabilizer. The explicitly constructed map to the corresponding regular group quotient is multiplicative. Its universal property identifies its kernel with the normal associator subloop. This proves the component/quotient statement without the invalid inference that every normal subgroup of the left multiplication group defines a loop quotient. The eigenvalue-one assertion follows from the permutation averaging argument even before a Bol symmetry assumption.

The central-family convolution calculation and rank eigenvalues are correct. The characteristic-two Bruck formula differs essentially from the binary cubic Moufang formula; the source and checker retain that distinction. Constant nontrivial character eigenvalues yield the asserted complete weighted star/triangle collision. The decomposition contrast then follows from the independently checked direct-core theorem.

The two-relation invariant correctly uses right-nucleus size, with the additional binary marker direction subtracted at p=2. It recovers the elementary abelian direct-factor rank only under the stated nonzero alternating-map Bruck-family hypothesis. The ordinary-graph gadget recovers relation labels through its two-core and pendant-path lengths; its vertex and edge bounds are correct. It is not a claim that arbitrary loop multiplication has been reconstructed from these relations.

The order-16 Moufang cocycle pair has identical associator and both full defect matrices but different square counts. The order-p-cubed group pair has identical element/subgroup incidence and directed power graphs but different commutativity. Their proofs and hypotheses check out. The table-incidence construction is correctly retained as an encoding control.

Finally, the section obstruction is valid: a subloop and then a quotient preserve the existence of a central subgroup with abelian quotient. Thus no nonassociative simple loop can be a section of these graph-loop outputs. The p-power-order conclusion is obtained from the central subgroup and additive image, not from an unproved general loop Lagrange theorem.

## 5. Dependencies, provenance, and exclusions

The central construction and original graph recovery retain the PR446 pins recorded above. He–Qiao Proposition 1.2 is the indispensable external graph-rigidity input. I verified its all-field scope during the earlier exact PR446 review and checked that the same statement is the one used here. The old scientific dependencies are unchanged.

Additional primary-source checks in this review included:

- [Wilson, arXiv:1005.0548v1](https://arxiv.org/abs/1005.0548v1), Definition 5.16, Lemmas 5.17 and 5.19, and Theorem 5.21; the centroid/direct-decomposition machinery is established.
- [Wilson, arXiv:0801.3434v2](https://arxiv.org/abs/0801.3434v2), Theorem 4.4 and Corollary 4.5; the self-adjoint-idempotent correspondence is established.
- [Tittmann–Averbouch–Makowsky, arXiv:0812.4147v2](https://arxiv.org/abs/0812.4147v2), the component polynomial and Theorem 27; the new manuscript gives its own complete component-count proof.
- [Kotek–Preen–Tittmann, arXiv:1207.2430v1](https://arxiv.org/abs/1207.2430v1), Corollary 11 and equation (5); the domination component expansion is an established mechanism.
- [Stanovský–Vojtěchovský, arXiv:1509.05730v1](https://arxiv.org/abs/1509.05730v1) and [arXiv:1509.05733v1](https://arxiv.org/abs/1509.05733v1), the associator-subloop and central-extension framework.
- [Official GAP LOOPS documentation](https://gap-packages.github.io/loops/doc/chap6_mj.html), the relevant inner-mapping and associator-subloop sections, and [Britten, arXiv:2204.07165v3](https://arxiv.org/abs/2204.07165v3), Theorems 1.1 and 2.10.

The role of Kelly's tree-reconstruction theorem is limited to an explicitly established control; the new counting arguments themselves are supplied in full. The new results do not rely on any unverified aggregate classification result from PR431 or any family-specific spectral theorem from PR440. I checked the continuation's separation of those scopes, but did not independently re-review those entire external workspaces or certify their current aggregate status.

No exhaustive historical-priority audit was performed. Existing tensor, graph-group, isotropic-counting, polynomial, and loop-extension methods are credited; the review verifies the displayed proofs and bounded source comparison, not global novelty. There is no claim of formal verification, proof of graph reconstruction, a general extension theorem for arbitrary Bol/Moufang loops, or a universal decomposition into graph-loop factors.

## 6. Independently rerun exact diagnostics

Environment: Python **3.12.14**, Linux x86_64, standard library only. All eight source hashes were verified before the following independent executions. Raw outputs were written outside the repository.

```sh
python notes/finite-simple-bol-loops/loop-decomposition/code/check_bruck_decomposition.py
python notes/finite-simple-bol-loops/loop-decomposition/code/check_loop_deletion_decks.py
python notes/finite-simple-bol-loops/loop-decomposition/code/check_loop_deck_census.py
python notes/finite-simple-bol-loops/loop-decomposition/code/check_loop_defect_graphs.py
python check.py --base 7653409e6155cd87c7f91ba810b155f517c7f44b
```

All commands exited with code zero, and all output records were inspected. These runs were performed at scientific revision `53446629822352b0682c41507832ccf04e22b446`; the exact-diff review to the final source is recorded above. The final revision changes no executable code, test expectations, or mathematical hypotheses.

| Research checker | Approximate rerun time | SHA-256 of exact stdout |
| --- | ---: | --- |
| `check_bruck_decomposition.py` | 1.006 s | `28f060df0504940e9fcbf42f84ce75c53839226aec69d6ab2b35dfa8c60ccf52` |
| `check_loop_deletion_decks.py` | 0.601 s | `8a4a65f63791a3d1223ba2e5af662a7e9973c53f45c47b2299a74bead478fafc` |
| `check_loop_deck_census.py` | 3.236 s | `8a073ddf9cad0dd3fedceb6b2776066cb4a929fea96c17e2deff5fa881940514` |
| `check_loop_defect_graphs.py` | 14.334 s | `21d86e30409a7be0ccb6e180de3b042e0b10fbdf70f1d81ff5a57058adbb6962` |

These timings came from concurrent local reruns and are descriptive, not performance guarantees. The stdout files are named `review-447-<checker-stem>.json` in local ephemeral evidence files.

The decomposition checker verified 15 centroid cases across p=2,3,5; three exact normalized factor-set linear systems; 1,024 and 59,049 quotient-product pairs for the fiber-product maps; and the Z/4 center/complement obstruction. This is finite evidence for the general proofs, not a classification of all factor sets.

The deletion checker examined **2,323 exhaustive frames**, of which 1,747 were admissible, and **2,304 sampled frames**, of which 346 were admissible. It checked **14 actual generated cards**, **6,338 card-product transports**, **607 scalar hyperplanes**, and **4,096 quotient-card products** in the central-identification example. Seeds and exhaustive/sample scopes are in the source. The sampled larger-frame cases are not being represented as exhaustive.

The census checker verified **152 isotropic graph/field cases** with **18,236 subspaces**, **88 associative-projection cases** with **33,609 subspaces**, **1,100 domination-transform cases**, and **1,096 reconstructed-component-polynomial cases**. It enumerated all subloops in five actual binary loops of orders 2,4,8,16,32. For the order-32 example it found 222 total subloops and the associative multiplicities `1,31,107,55,4`. The collision check additionally examined **5,650 binary quotient subspaces** across the two five-vertex examples.

The defect checker compared components with an independently closed associativity congruence in eight actual loop tables, including a non-Bol control. It verified the complete weighted-matrix collisions, all eleven scalar-spectrum cases, and the explicit order-27 subgroup-incidence/power-graph correspondence. In the two order-256 Bruck examples the translated matrices agree, while their local-isolate counts are 16 and 32, giving direct-factor ranks zero and one as predicted. The two order-16 Moufang examples have square-one counts 14 and 2 despite identical defects.

The integrity suite passed **115 tests**. Its combined stdout/stderr file `review-447-integrity.txt` has SHA-256 `e587e054dcc3d2d453c174537c8133a529765c5aea07696319aedbd116b39125`. This is metadata/tool integrity evidence only.

## 7. Remaining obstruction and final scope

There is no identified unpaid lemma within the accepted theorem statements. The main unpaid **research** obligation is different: obtain compatible domain/output alignments and central intersections from an unaligned graphical card multiset, or prove uniqueness without reconstructing those alignments. He–Qiao recognizes a fully assembled graphical map; it does not solve this gluing problem. The nongraphical quotient example invalidates a naive broader gluing principle but leaves same-order enlarged-family questions open.

The continuation supplies an intrinsic abstract deck for a recognized family, an exact graph-reconstruction equivalence, a broader scalar-hyperplane reconstruction theorem, a substantive central Bruck decomposition theorem, actual associative-quotient information from defect graphs, and a full associative-subloop census from unaligned cards. Those are the accepted endpoints. Neither graph reconstruction nor arbitrary finite-simple Bol classification is claimed solved.

This review binds the exact scientific revision and hashes above. Later delivery metadata may record it without changing those sources. A substantive source or dependency change requires review of the affected content; the existence of this report must not be treated as acceptance of changed mathematics.

## 8. Coordinator verification and publication handoff

This section is recorded by the coordinating agent `/root`, not attributed to
the independent reviewer. The commissioned research date is 2026-11-16 in
America/Los_Angeles; the recorded executions and publication occurred on
2026-11-17 UTC. The complete independent report preserved above has SHA-256
`6fb3b05c536af7a5c693c49f96b0d743ad3a22b9ee237f4e6c7586f00c12e415` before this
coordinator section is appended.

The source authors independently ran the same four checkers under Python 3.12.14.
Their exact stdout hashes agree with all four independent-review hashes above.
The respective observed runtimes were 0.784, 0.459, 2.935 and 13.299 seconds.
All four checkers are byte-identical between the first full-review pin and the
final scientific clarification. The final delivery changes navigation and this
evidence record only; the eight scientific hashes above remain the review boundary.

A second scoped independent review by a scoped reviewer checked the defect
manuscript and its checker, which that agent did not author. It found no
mathematical defect and independently reproduced the defect checker. Its verdict
was bound to `53446629822352b0682c41507832ccf04e22b446`; the two reviewed file
hashes are unchanged at the final scientific pin and match the table above.
The checked scope includes the point-stabilizer quotient, Bol inverse-defect
identity, both prime-dependent spectral formulas, weighted collisions,
right-nucleus correction, incidence/power-graph counterexample, ordinary-graph
conversions and section obstruction. It explicitly excludes independent review
of that agent's own extension/decomposition manuscript. Neither reviewer claims
human review, formal verification, or exhaustive historical priority.

Repository integrity passed all 115 tests locally, independently and in the
coordinator run. One preliminary coordinator invocation detected an empty,
untracked typo directory `problems/0323-finite-simple-n-moufang-bol-loops/code`;
only those empty directories were removed, and the full gate then passed.
No active research file was removed. The final delivery repeated the integrity
gate successfully (115 tests) and checked all 73 relative links/anchors and 115
fenced math blocks across the 12 changed prose pages, with no static errors.
The PR body records the actual delivery head and CI.

The mathematical manuscripts use GitHub fenced math, with all display braces
and fences checked. Before the delivery metadata, 48 local links/anchors in
eight changed prose pages passed the static check. These source checks are
distinct from actual target rendering. An attempt to inspect the published
overview at the scientific GitHub URL showed GitHub's ordinary 404 page in a
signed-out browser. Authenticated connector source access succeeded. Thus
**visual verification of GitHub's rendered manuscript pages remains incomplete**;
no clean visual-rendering claim is made. No credentials or login changes were
requested merely to clear this optional publication check.

The GitHub Actions run for the final scientific source,
[44033391149](https://github.com/Mira-Cult/math-wip/actions/runs/44033391149),
reported **skipped** for `Research integrity (not mathematical review)` on
`pull_request_target`, with exact head
`61f86bbbab630fc45a5ad4a6258e5562dceb1e9b`. The earlier full-review source run
[44032963757](https://github.com/Mira-Cult/math-wip/actions/runs/44032963757)
also reported skipped. Neither is described as a CI pass.

The five PR446 scientific files were byte-compared with delivery
`7653409e6155cd87c7f91ba810b155f517c7f44b` and remain unchanged. The PR446
branch was rechecked at that head, with main at
`8acbca2dfe371d48d4c33dab1b0bf2afccb3fe1e`. Existing PR431/PR440 ownership,
source pins and review records were preserved. The two parent problem contracts
and all permanent claim IDs remain unchanged; the 0323/0354 relationship pages
only link the proved restricted equivalence.

The recoverable workspace is [PR #447](https://github.com/Mira-Cult/math-wip/pull/447),
stacked on PR #446. Its canonical entry point is
[LOOP_DECOMPOSITION.md](../README.md). It is a completed research
checkpoint with the unresolved gluing obligation in Section 7, not a resolution
of the parent conjectures. The PR remains unmerged; no formal GitHub approval
or publication to `Mira-Cult/math` is part of this delivery.
