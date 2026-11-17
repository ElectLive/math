# Code and reproducibility

## Running code

No finite-simple-loop classification implementation or formal proof accompanies
the original intake. The graph-native continuation below adds separately scoped
checks of central-extension laws and graph/subloop theorems.

For future finite examples, record the construction parameters and test identity, unique divisions, the left Bol identity, an explicit failure of Moufang, and simplicity. Checking only the absence of proper subloops is not a valid simplicity test. Record the isomorphism-deduplication method and distinguish exhaustive runs from sampled searches.

The research repository has a separate `check.py` integrity suite, not included in this standalone public packet. It does not establish mathematical claims.

## Reproducibility

Keep generators and small canonical inputs in source; record software versions
and commands. Do not commit generated build products or large enumeration dumps.

## Graph-native loop checks

From the repository root, with Python 3.11 or later and no third-party packages:

```sh
python notes/finite-simple-bol-loops/graph-loops/code/check_graph_loop_laws.py
python notes/finite-simple-bol-loops/graph-loops/code/check_graph_subloops.py
```

The first program performs symbolic integer-polynomial reductions for the
all-ring left Bol identity, the two-parameter obstruction and associator,
plus the ternary Moufang and binary cubic identities. It builds actual finite
multiplication tables, checks the Latin property, and checks 5,475,158 triples
across twelve table cases. For the order-625 case, 1,953,125 triples use all
quotient-coordinate triples with central coordinates zero; central shifts
add equally to both sides, giving an exact central-extension reduction.
The other table cases check every triple of loop elements. It also checks
805,252 product compatibilities for transports and deletion maps, including
seeded permutation samples; general naturality rests on the proof.

Arithmetic in Z[omega]/(2), /(3), and /(7) is checked separately, including
unit counts, conjugation and explicit zero divisors. Each ring has 2,048 sampled
law triples with seed 2468; these do not exhaust the rings' loops. Directed
examples include an empty graph, one edge, reversal, recoloring, a path,
a four-cycle, transitive and directed triangles, and a bidirected pair with
its doubled-role repair. The F7 checker uses omega=2 at the prime (2-omega);
the manuscript also describes the conjugate factor omega=4.

The independently written second program enumerates all vector subspaces via
RREF and compares actual maximal isotropic spaces with the complete predicted
component-line spaces, not only their counts. Default scope is 152 graph/field
cases through four vertices over F2 and F3, 18,236 subspace cases, 2,030 maximal
isotropic spaces, and 76 binary square-zero hyperplane classifications.
Independent factor-set evaluation checks right-alternative loci in 36 cases
through three vertices over F2, F3 and F5, with 1,076,183 discrepancy evaluations.
For the six-vertex invariant-loss pair it checks all 2,825 binary subspaces of
each graph and the exact dominating-component coefficient table.

All computations use exact arithmetic. Both scripts print concise JSON; raw
stdout and generated tables are not tracked. They supplement general proofs
and do not establish them. Integrity testing is a separate metadata/tool check.
Actual runtime, source hashes, independently reproduced outputs and review
provenance are in the [review/evidence record](../../graph-loops/evidence/graph-loops-review.md),
pinned to scientific revision `9059767c0ef28809bbe17de8a71ba0a8b11d0485`.

## Decomposition and intrinsic deletion checks

The separate [decomposition continuation](../README.md) adds four
standalone Python 3.11+ programs, each using only the standard library:

```sh
python notes/finite-simple-bol-loops/loop-decomposition/code/check_bruck_decomposition.py
python notes/finite-simple-bol-loops/loop-decomposition/code/check_loop_deletion_decks.py
python notes/finite-simple-bol-loops/loop-decomposition/code/check_loop_deck_census.py
python notes/finite-simple-bol-loops/loop-decomposition/code/check_loop_defect_graphs.py
```

The decomposition checker solves centroid and small factor-set linear systems
over F2, F3 and F5, tests common-marker fiber-product quotients, and verifies a
Z/4 obstruction to splitting the center. The deck checker exhausts 2,323 small
frames, samples 2,304 larger frames with fixed seeds, checks generated subloops
and arbitrary central lifts, and enumerates 607 scalar-form hyperplanes. It
also checks the bad-marker, dependent-frame and central-identification examples.

The census checker compares RREF subspaces with the isotropic and associative
projection formulas, verifies the component/domination and deletion transforms
on all labeled graphs through five vertices, and enumerates all actual subloops
in five small binary Bruck loops. Its five-vertex pair tests equality of the
entire associative census alongside unequal maximal-associative counts.

The defect-graph checker constructs actual multiplication tables, divisions and
left translations. It compares translated graph components with a separately
computed least congruence forcing associativity, checks both weighted-matrix
collisions, evaluates eleven scalar-spectrum cases, and verifies the order-27
full element/subgroup-incidence control. The eight table examples include a
non-Bol loop to test the scope of the symmetry statement.

Each program prints concise deterministic JSON. Exact commands, source and
stdout hashes, independent reruns and review limits are in the continuation's
[review record](../evidence/loop-decomposition-review.md), bound to scientific
revision `61f86bbbab630fc45a5ad4a6258e5562dceb1e9b`. Generated output is not tracked. Passing these finite diagnostics
does not prove universal identities, graph reconstruction or classification.
