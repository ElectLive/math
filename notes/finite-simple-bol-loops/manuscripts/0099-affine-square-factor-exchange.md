# Operation classification for factor-swapping affine squares

**Mira Cult**

## Theorem

Let q=p^f≥4 and X=F_q²⋊SL₂(q) in its natural action. Suppose a finite simple proper left Bol loop has canonical left multiplication group X×X and its canonical inversion exchanges the displayed factors. Conditional on the pinned canonical-folder, construction and isomorphism inputs, its operation belongs to the root-graph family. Conversely every member of that family has these data. Nonzero F_p-linear maps from F_q to itself, modulo the specified semilinear equivalence, parameterize its isomorphism classes. The loop order is q³(q²−1).

This is an operation classification under a specified canonical group and inversion, not a full-multiplication-socle theorem. The [complete exhaustion proof](../sources/full-socle-completion/paired-affine-swap-exhaustion.md) includes all field sizes, both characteristics, the q=9 exception and the original stabilizer.

## Recovering the original stabilizer

Identify the factors so that inversion is ordinary interchange. All outside involutions form one conjugacy class, so the selected marks force K={(x,x⁻¹):x∈X}. The original stabilizer H has order |X| and contains no nonidentity pair whose coordinates are conjugate to mutual inverses.

With V=F_q², put W=H∩(V×V), and let J be the image of H in SL₂(q)², with projections B and C. The collision rule forces W into one coordinate module. The factorization gives SL₂(q)=BC and |J|/|SL₂(q)|=q²/|W|=p^k. Simplicity forces k≥1 by the exact normal-subloop criterion.

If both B and C are proper, Dickson's subgroup classification and their p-parts leave only a small number of actual factor possibilities. For odd fields the q=9 exceptional factorization is not discarded numerically: the lifted central involutions collide. In characteristic two the remaining torus-normalizer case would force an invariant hyperplane incompatible with the split torus action. Hence one projection is the whole SL₂(q).

Goursat's lemma then gives J=B×SL₂(q), with B a nontrivial p-group. Writing the original stabilizer modulo W as a cocycle separates its two coordinate components. A simultaneous affine automorphism absorbs the cocycle, including nonprincipal ones, and carries H to Y×SL₂(q), where Y is a nontranslation regular subgroup of X. The prior regular-subgroup exhaustion identifies Y with a root graph. Its construction and semilinear isomorphism theorem supply the converse and exact equivalence relation.

## Scope and next boundary

The exhaustion and its new deductions have two exact-source model mathematical reviews at the revision recorded in the source. The reviewers retain the prior canonical, construction and isomorphism hypotheses; this is not human refereeing or formal verification.

The [odd-field all-inversions theorem](../sources/full-socle-completion/paired-affine-odd-inversions.md) establishes, under its stated inputs, that the same classification covers every canonical group abstractly ASL₂(q)² for odd q≥5, without prescribing inversion or stabilizer type. It analyzes automorphisms, excludes factor-preserving inversion and reduces to exchange. Two independent model reviewers accepted its new deductions at exact source `bb5a92abe1c4963c1218fbea4508987a9e88c118`, retaining the linked original-folder and paired-affine inputs. They did not repeat the upstream construction and isomorphism proofs or use a finite census. Factor-preserving inversion in characteristic two and arbitrary canonical groups remain open.
