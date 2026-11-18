# Reproducing the elementary PSL₂(19) loop

The [construction and proof](../../manuscripts/0112-elementary-radical-example.md) use one finite datum: eight matrices over the field of three elements. The input and two different verifiers are provided here. No enormous multiplication table, classification software or network lookup is needed for either verification.

## Verify the supplied data

From this directory, with Python assertions enabled, run:

```sh
python3 code/verify_explicit_psl2_19_bol.py
python3 code/check_explicit_bol_datum_independent.py evidence/psl2-19-explicit-matrix-input.json.zlib.b64
```

The [first verifier](code/verify_explicit_psl2_19_bol.py) uses only the Python standard library. The [second](code/check_explicit_bol_datum_independent.py) requires NumPy. Compare the [first output](evidence/explicit-standalone.out) and [independent output](evidence/explicit-independent.out). Both programs first check the SHA-256 of the canonical decompressed JSON: `c5965e0fdc104b529bf3eac790bac48d83e1c8ef03d8cb04f284893eaeb53ddb`. Its 100,486 bytes specify the generators on both modules, the graph map, and the cocycle vector. All matrix entries are trits; row ordering is part of the data.

The author verifier traces group relations on spanning vector orbits and uses a dual algorithm for invariant-subspace cores. The independent verifier instead establishes the actions from twenty Schreier representatives, checks all 29,241 products of the point stabilizer, uses primal subspace intersections, and gives eight direct failures of right alternativity. Both test all eight actual two-sign affine systems, not just a necessary scalar condition.

## Optional: regenerate the input rather than trusting its origin

The [deterministic generator](code/rebuild_from_atlas.py) uses NumPy, the projective action on twenty points, the indicated three signs and lengths of explicit flag modules, an 18-dimensional prime-field representation, and two fixed lists of 71 and 12 coefficient trits. The coefficient lists are literal in the source, not regenerated from a changing random-number API. The fixed input itself is the theorem's definition; no classification of candidate modules is needed.

Obtain the four original GAP generator files from the [ATLAS of Finite Group Representations](https://brauer.maths.qmul.ac.uk/Atlas/lin/L219/), preserving their names. Direct links:

- [20-point permutation generator 1](https://brauer.maths.qmul.ac.uk/Atlas/lin/L219/gap/L219G1-p20B0.g1) and [generator 2](https://brauer.maths.qmul.ac.uk/Atlas/lin/L219/gap/L219G1-p20B0.g2).
- [9-dimensional generator 1 over the field of nine elements](https://brauer.maths.qmul.ac.uk/Atlas/lin/L219/gap/L219G1-f9r9aB0.g1) and [generator 2](https://brauer.maths.qmul.ac.uk/Atlas/lin/L219/gap/L219G1-f9r9aB0.g2). See the [representation record](https://brauer.maths.qmul.ac.uk/Atlas/v3/matrep/L219G1-f9r9aB0).

Run `python3 code/rebuild_from_atlas.py /path/to/atlas-files reconstructed.json`. The program checks all four raw file hashes, reconstructs the canonical JSON, and checks its expected digest before writing it. No ATLAS files are redistributed here. The two verifiers do not need the ATLAS inputs.

## Exact evidence and limitations

The [frozen independent audit](evidence/frozen-audit.txt) accepts the specified datum and the mathematical proof: its sharp action, left Bol law, all proper normal cuts, faithfulness, solvable radical, non-Moufang witness, spectrum and two named family comparisons. Its SHA-256 is `80e047343ee5c5148c343ae79161ac5e4215abf070429f81721e167ecba31dfe`. The source revisions for the data and the forward proof are respectively `a62ed7be932309f66f389a7d82d1dc0ad4433a70` and `b0d934df3d80bfc5b60d1995b22c6eb2eb06f675`; the audited proof's SHA-256 is `e06faf864643c450102adbde0b4f783a05c47dfefd0a6529ab6469f0eee500a3`. The [manifest](manifest.json) records the published artifact hashes.

The construction and exposition used OpenAI model assistance under Mira Cult's research direction, and a separate OpenAI model process independently checked the fixed mathematical result and wrote the second verifier. Exact model versions for these contributions have not been established. This is independent AI mathematical review, not human refereeing or proof-assistant verification. The independent audit does not certify historical priority, uniqueness, minimum dimension, the optional generator's historical search pathway, or a classification of other loops.
