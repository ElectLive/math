# Code and reproducibility

## Running code

No finite-simple-loop classification implementation or formal proof accompanies
the original intake. The graph-native continuation below adds separately scoped
checks of central-extension laws and graph/subloop theorems.

For future finite examples, record the construction parameters and test identity, unique divisions, the left Bol identity, an explicit failure of Moufang, and simplicity. Checking only the absence of proper subloops is not a valid simplicity test. Record the isomorphism-deduplication method and distinguish exhaustive runs from sampled searches.

The research repository has a separate `check.py` metadata-integrity suite. It is not included in this standalone public packet and does not prove mathematical claims.

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
provenance are in the [review/evidence record](../evidence/graph-loops-review.md),
pinned to scientific revision `9059767c0ef28809bbe17de8a71ba0a8b11d0485`.
