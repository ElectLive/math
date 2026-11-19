# Verifying the two-prime extraspecial constructions

The two manuscripts received separate independent AI proof reviews. Both reviews check the actual coset transversals, the central phase for products of two marked involutions, every relevant signed normal cut, the faithful generated left multiplication group, and the intrinsic extraspecial core. The axial review additionally checks the mixed fixed-space invariant and its preservation under isotopy. These are mathematical reviews, not human refereeing or formal verification. They do not establish historical priority, least degrees, or completeness of the isotype counts.

The following Python programs use only the standard library. Run them from this directory:

```sh
python3 -B code/verify_extraspecial_bol_construction.py
python3 -B code/check_extraspecial_native_sheets_independently.py
python3 -B code/check_axial_cotangent_families.py
```

- [Nonaxial author output](evidence/extraspecial-bol-construction.out): actual rational matrices and all 33,489 pairs of projected involutions at the example with primes 3 and 61.
- [Nonaxial independent output](evidence/extraspecial-native-sheets-independent.out): separate field construction, two different characteristic primes, both rational-degree parities, and both zero-phase and nonzero-phase controls.
- [Axial author output](evidence/axial-cotangent.out): genuine signed operators and the fixed-rank distinction in mixed sums. The independent axial proof review also replayed the author program and used a separately constructed rational representation to check the dimensions, action, and central phases at three prime pairs.

Finite programs test the physical constructions; they do not enumerate the entire loops or substitute for the all-parameter proofs. Mira Cult directed the research. OpenAI models contributed to the mathematics, exposition and separate reviews. Exact version assignments were not verified.
