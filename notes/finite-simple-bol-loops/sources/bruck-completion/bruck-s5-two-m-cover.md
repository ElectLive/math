# Candidate fixed-free two-M cover and support count

**Mira Cult**

**Finite module classification with scoped independent review recorded below.** This manuscript considers finite $`\mathbb F_2S_5`$-modules with exactly two composition factors $`M`$ and all remaining factors trivial, in the notation of [bruck-s5-radical.md](bruck-s5-radical.md). It proposes ten fixed-free isotypes, four of them indecomposable, and gives a finite support-subspace cover for arbitrary such modules. It does not classify group extensions, stabilizers, sections, envelopes, or loops.

This continues [C0010](../../claims/0010.md) and allocates no new claim ID. The fixed-free $`J`$-submodule and general support theorem in [bruck-s5-two-m-support.md](bruck-s5-two-m-support.md) were independently accepted at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/8b091f64620504d07eadfe4186f265eb5afc18e2). The 17 one-$`M`$ isotypes and their exact intertwiner enumeration were reviewed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/359875203abdbf7033ab04843fba2197aac2aafe), conditional on the one-$`M`$ cover at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6a563df3804682acb6bd4191fff2ac749cb0bd16) and its splitting test at [the source revision](https://github.com/Mira-Cult/math-wip/commit/f6c7e01a4337b51c703b4d9ffc94d3b84a732fe5); see [bruck-s5-principal-isotypes.md](bruck-s5-principal-isotypes.md). The new computations below are not covered by those reviews.

## Fixed-free extension cover

Let $`Q^{S_5}=0`$. If $`Q`$ has no trivial composition factor, the reviewed $`\mathop{\mathrm{Ext}}\nolimits^1(M,M)=0`$ gives $`Q\cong M^2`$. Otherwise the cited support theorem embeds $`J=P_6/\mathbf1`$ in $`Q`$, and $`Z=Q/J`$ has one $`M`$ factor and $`\dim Z^{S_5}\le1`$. The one-$`M`$ classification decomposes $`Z\cong Z_0\oplus A`$, where $`Z_0`$ is one of 17 indecomposable isotypes and $`A`$ is sign-only. Each nonzero indecomposable sign module has a fixed line, so $`A`$ is at most one of $`\mathbf1`$ or $`R`$. Testing those possibilities gives 20 labelled $`Z`$ presentations with fixed dimension at most one. They are a finite cover, not asserted pairwise distinct.

For each $`Z`$, extensions $`0\to J\to Q\to Z\to0`$ with fixed kernel and quotient identifications are parametrized by $`H^1(S_5,\mathop{\mathrm{Hom}}\nolimits_{\mathbb F_2}(Z,J))`$. The new [classify_bruck_s5_two_m_fixed_free.py](../code/classify_bruck_s5_two_m_fixed_free.py) constructs these Hom actions, imposes cocycle consistency on every edge of the 120-element Cayley graph, quotients by principal cocycles, and constructs block matrices for every class. It checks Nagy's four presentation relators on all 48 extension representatives. Filtering for zero fixed space leaves 12 representatives of dimensions 9–12.

The program computes each endomorphism space by the generator-commutation equations and exhausts its elements for nontrivial idempotents; the largest dimension encountered is 4. Five of the 12 representatives are indecomposable, with dimensions $`10,10,11,11,12`$. It exhausts the Hom spaces for same-dimensional isomorphism comparisons, with maximum Hom dimension 3, and verifies every positive intertwiner. The 12 representatives form nine isotypes containing $`J`$. The two 11-dimensional indecomposable representatives are isomorphic; the proposed four indecomposable isotypes have dimensions $`10,10,11,12`$. Adding the separately handled $`M^2`$ gives ten proposed fixed-free isotypes, of maximum dimension 12. As a control, an exact intertwiner identifies the previously constructed 10-dimensional indecomposable from [verify_bruck_s5_two_m10.py](../code/verify_bruck_s5_two_m10.py) with exactly one of these isotypes. None is thereby asserted to occur in a loop envelope.

## Support-subspace cover

For an arbitrary two-$`M`$ principal module $`X`$, let $`A\cong\mathbf1^a\oplus R^b`$ be its maximal sign-only submodule and $`Q=X/A`$ its fixed-free quotient, as in the reviewed support theorem. For each of the ten proposed $`Q`$ isotypes, its extension class is a tuple in

```math
\mathop{\mathrm{Ext}}\nolimits^1(Q,\mathbf1)^a\oplus\mathop{\mathrm{Ext}}\nolimits^1(Q,R)^b.
```

Independent $`GL_a(\mathbb F_2)`$, $`GL_b(\mathbb F_2)`$ row operations reduce each tuple to a basis of its span followed by zeroes; the unsupported sign summands split. Thus a pair of subspaces of the two Ext spaces suffices to cover the supported classes, with a chosen basis for each subspace. Further automorphisms may identify different pairs, and arbitrary additional split sign tails remain. By Shapiro the relevant dimensions are $`e_1=\dim H^1(S_5,Q^*)`$ and $`e_R=\dim H^1(A_5,Q^*)`$.

The program computes these dimensions using the dual-matrix and all-Cayley-edge routine in [verify_s5_principal_h1_bounds.py](../code/verify_s5_principal_h1_bounds.py), last changed at [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9), checking group orders 120 and 60. The row entries are $`(\dim Q,e_1,e_R,\text{subspace pairs},\dim Q+e_1+2e_R)`$:

| Candidate $`Q`$ | Dimensions and support count |
| --- | --- |
| $`M^2`$ | $`(8,2,4,335,18)`$ |
| cluster 0 | $`(9,3,4,1072,20)`$ |
| clusters 1, 4 | $`(10,2,4,335,20)`$ each |
| cluster 2 | $`(10,1,2,10,15)`$ |
| cluster 3 | $`(10,4,4,4489,22)`$ |
| cluster 5 | $`(11,3,4,1072,22)`$ |
| cluster 6 | $`(11,2,1,10,15)`$ |
| cluster 7 | $`(12,2,4,335,22)`$ |
| cluster 8 | $`(12,0,0,1,12)`$ |

Here the subspace count is the product of the sums of Gaussian binomial coefficients over $`\mathbb F_2`$ in dimensions $`e_1,e_R`$. The total is 7,994 pairs and the maximum displayed supported dimension is 22. Conditional on the fixed-free isotypes and these $`H^1`$ values, that would sharpen the purely analytic supported bound 126. It is not a count of module isomorphism types or an actual indecomposable maximum. **The program counts these 7,994 pairs; it does not construct their extension matrices.** The $`N`$-block and split sign tails are not bounded by this support table.

## Reproduction and review boundary

From the repository root, use Python 3.11 or newer:

```sh
python3 problems/0323-finite-simple-non-moufang-bol-loops/code/classify_bruck_s5_two_m_fixed_free.py
```

The optional `--representatives` flag prints generator columns and the extension labels for the ten candidates. The program imports the reviewed sibling routines with their exact source and review scopes linked above, restores command-line arguments after each import, and requires assertions to be enabled. It hard-fails if an endomorphism or Hom space exceeds its exhaustive limit. A focused Python 3.12.14 run gave 20 $`Z`$ presentations, 48 extensions, 12 fixed-free representatives, nine isotypes plus $`M^2`$, four indecomposable isotypes of dimensions $`10,10,11,12`$, and the table above in about 2.8 seconds.

The new Hom cocycle construction, fixed-space and idempotent checks, isotype clustering, $`H^1`$ table and 7,994 count require independent exact-revision review. The prior reviews do not certify this computation, and no conclusion about simple loops is drawn from it.

## Independent review

reviewer contributor 1 accepted this manuscript and its certificate at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/691940048ad65ae4db2c13576e210d973e6e5f81), conditional on the pinned prior one-M isotypes, J-embedding and sibling helper routines. The review checked completeness of the 20 quotient presentations and 48 extension classes, all-Cayley-edge Hom cocycles and principal quotient, fixed-space and exhaustive idempotent tests, invertible-intertwiner clustering, the ten isotypes and four indecomposable isotypes, and the dual H¹ and Gaussian-subspace counts. An independent Python 3.12.14 run reproduced the displayed results. The review accepts 7,994 pairs as a surjective support cover of dimension at most 22, not an isotype count; the script does not construct those extension matrices. No loop, envelope, N-block or split-tail classification is asserted.
