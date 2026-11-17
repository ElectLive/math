# Decomposition and intrinsic-deck publication checkpoint

Mira Cult

This deliberate batch mirrors completed PR #447 at delivery `d4e65d9a75e6e4c58539b5b6658c438e1d402155`, reviewed science `61f86bbbab630fc45a5ad4a6258e5562dceb1e9b`. Its four manuscripts and four checkers are unchanged from the reviewed scientific bytes. The [source map](source-map.json) records public presentation changes separately. Its [graph-construction dependency](../graph-loops/README.md) is already public at reviewed science `9059767c0ef28809bbe17de8a71ba0a8b11d0485`.

A noncontributing independent model reviewer accepted all eight scientific files. Acceptance transferred from the full audit at `53446629822352b0682c41507832ccf04e22b446` by an exact-diff review of two notation/terminology clarifications. A second independent scoped review covers the defect manuscript/checker only and excludes that reviewer's authored decomposition work. The [historical evidence record](evidence/loop-decomposition-review.md) retains these boundaries and source inspections. No human referee acceptance or formal verification is inferred.

All four unchanged checkers were freshly replayed under Python 3.12.14 during this publication. Their exact stdout hashes equal the independent research-review records:

| Checker | SHA-256 of stdout |
| --- | --- |
| `check_bruck_decomposition.py` | `28f060df0504940e9fcbf42f84ce75c53839226aec69d6ab2b35dfa8c60ccf52` |
| `check_loop_deletion_decks.py` | `8a4a65f63791a3d1223ba2e5af662a7e9973c53f45c47b2299a74bead478fafc` |
| `check_loop_deck_census.py` | `8a073ddf9cad0dd3fedceb6b2776066cb4a929fea96c17e2deff5fa881940514` |
| `check_loop_defect_graphs.py` | `21d86e30409a7be0ccb6e180de3b042e0b10fbdf70f1d81ff5a57058adbb6962` |

The finite diagnostics support the general proofs; they do not establish unbounded reconstruction or integrability of arbitrary tensors. Reviewed scientific hashes, original Git blob hashes, executable byte fidelity and public relative links/anchors were checked. The source's 115-test integrity result and skipped CI status are historical research evidence, not a fresh integrity run or a hosted CI pass for this mirror. The public landing page was inspected in GitHub Preview after publication, including the displayed decomposition equation and its scope. A complete hosted visual audit of every proof remains unverified.

The public claim is [0093](../claims/0093.md), with precise prime-exponent, central-associator, trilinearity and graphical-competitor restrictions. He–Qiao, centroid/adjoint methods and graph reconstruction baselines retain their attributions. Source #431/#440 comparisons are not blanket imports or new reviews of their aggregate claims. No active research branch, source review pin, repository permission, or PR disposition is changed.

Published artifacts were independently fetched through Git and compared byte-for-byte with the intended files. No discrepancy was found.
