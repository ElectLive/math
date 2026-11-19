# Proof checks and reproduction

Each of the six results received a separate independent AI mathematical proof review. The conclusions are conventional proofs, not formal certifications, and have not been certified by a human referee. The author and independent programs test actual finite group, coset and native-multiplication calculations, rather than attempting to enumerate the much larger loops in the general theorems.

| Proof | Scope of the independent check | Author program / output | Independent program / output |
|---|---|---|---|
| [Universal odd groups](proofs/all-odd-groups.md) | All odd groups including 1, native multiplication in the target, nonabelian normal cuts and faithfulness. | [Python](code/verify_universal_odd_nucleus_graph_wreath.py) · [stdout](checks/universal-odd-nucleus-graph-wreath.out) | [Python](code/check_native_nucleus_and_signed_tops.py) · [stdout](checks/all-odd-groups-independent.out) |
| [Central intersection](proofs/central-intersection.md) | The exact subgroup inside the left group, including a nonsummand in a nonabelian target; full normalizer and tilted central cuts. | [Python](code/verify_central_nuclear_insertion.py) · [stdout](checks/central-nuclear-insertion.out) | [Python](code/check_coupled_normalizers_and_nonsplit_cuts.py) · [stdout](checks/central-intersection-independent.out) |
| [One marked group](proofs/one-marked-group.md) | One mark set, all subgroup targets, the literal common copy of the larger group and the limits on distinguishing loops from permutation actions. | [Python](code/check_shared_native_envelope_color_probes.py) · [stdout](checks/shared-native-envelope-color-probes.out) | [Python](code/check_colored_nuclei_frobenius21.py) · [stdout](checks/one-marked-group-independent.out) |
| [Central abelian construction](proofs/abelian-central.md) | Mixed primes, nonfree subgroups, partial-center cuts, and equality with the full right nucleus. | [Python](code/verify_prescribed_abelian_nuclei.py) · [stdout](checks/prescribed-abelian-right-nuclei.out) | [Python](code/check_mixed_partial_cuts_and_sign_sheets.py) · [stdout](checks/abelian-central-independent.out) |
| [Centerless abelian construction](proofs/abelian-centerless.md) | A genuinely centerless left group; explicit comparison at the same degree with the separate central construction. | [Python](code/check_centerless_ridge_factorizations.py) · [stdout](checks/centerless-ridge.out) | [Python](code/independent_centerless_ridge_native_products.py) · [stdout](checks/abelian-centerless-independent.out) |
| [Two-element commutation test](proofs/two-elements.md) | Two actual elements suffice and one cannot; the addressed probe is necessary in the examples, not merely a projected group calculation. | [Python](code/check_two_native_commutation_probes.py) · [stdout](checks/two-native-commutation.out) | [Python](code/check_two_probes_true_group_and_rings.py) · [stdout](checks/two-elements-independent.out) |

Run each linked Python 3 script with no arguments from this directory. Some scripts require NumPy. Use Python 3 with NumPy installed. For instance:

```sh
python code/check_native_nucleus_and_signed_tops.py
python code/check_coupled_normalizers_and_nonsplit_cuts.py
python code/check_colored_nuclei_frobenius21.py
```

The [1053-element comparison](nagy-comparison.md) has its own [program](code/check_nagy_1053_right_nucleus.py) and [recorded result](checks/nagy-1053-right-nucleus.out). An additional [one-site field check](code/verify_trivial_nucleus_normalizer_transfer.py) has [its own output](checks/trivial-nucleus-normalizer-transfer.out). The signed normal-cut test and referenced results of Foguel, Kinyon, Phillips and Nagy are mathematical inputs; each finite test has the narrower scope stated above.

Mira Cult directed the research. OpenAI models assisted with the proofs, calculations, exposition and separate reviews; exact model versions have not been verified.
