# Reproducing the finite tables and checking the general construction

The [main note](README.md) proves the arbitrary-prime obstruction and gives a native order-63 multiplication. All programs run in Python 3.9+ with its standard library only. No network access, hidden inputs, random search for a counterexample, numerical tolerance or third-party algebra package is required. Run without Python optimization so the assertions remain active.

```sh
python3 -B code/verify_bol_63_no_sylow.py rebuilt.csv
cmp rebuilt.csv evidence/order-63-no-sylow.csv
python3 -B code/verify_bol_63_heisenberg_cosets.py
python3 -B code/check_native_63_independent.py
python3 -B code/verify_every_odd_prime_sylow_obstruction.py
python3 -B code/check_every_odd_prime_sections_independent.py
```

| Program | What it tests | Reference output |
| --- | --- | --- |
| [Scalar order-63 formula](code/verify_bol_63_no_sylow.py) | Both tables, every left Bol triple, graph-section ranks and all 1,512 cyclic-line pairs | [scalar](evidence/bol-63-scalar.out) |
| [Group/coset construction](code/verify_bol_63_heisenberg_cosets.py) | All 9,261 ambient group elements, both stabilizers and all 7,938 products | [cosets](evidence/bol-63-cosets.out) |
| [Independent affine-plane reconstruction](code/check_native_63_independent.py) | Every native product without the scalar formula, every left Bol triple, all 49 choices of lifts of two generators | [independent finite](evidence/native-63-independent.out) |
| [Uniform construction](code/verify_every_odd_prime_sylow_obstruction.py) | Shift/clock groups, stabilizer intersections, power norms and positive/negative based controls over six fields | [uniform](evidence/every-odd-prime-sylow-obstruction.out) |
| [Independent uniform tests](code/check_every_odd_prime_sections_independent.py) | Marked affine-flat orbits over five fields, including an additive subgroup not linear over F49 | [independent uniform](evidence/allp-sections-independent.out) |

The [canonical CSV](evidence/order-63-no-sylow.csv) contains 63 integer rows with no header and a terminal newline. The label of (a,b,h) is 21a+7b+h, starting at zero; cell (i,j) is the label of their product. Its SHA-256 is `5d3a7c768043e044bd644ffbee89bb62e36a6977d9c295c00d5bc555d13c5795`. Every one of the 49 lifts of the two coordinate basis elements generates the whole native loop; in the comparison table they instead give 49 different nine-element subloops.

The [finite audit](reviews/order-63.txt) covered the order-63 theorem and table at scientific source revision `6a676716c2b030dc5e14607d45ea652d73f21b02`. The [separate uniform audit](reviews/every-odd-prime.txt) covered the arbitrary-prime obstruction, its hypotheses, the comparison count and power spectrum at `9d8319838ff4098a2d92f4a5cce7018ddfcc6ee5`. The reviewer was not the author of either proof. The [manifest](manifest.json) records the hashes of both exact source manuscripts, both unedited mathematical audits and every component here. The stand-alone note rearranges the proofs for the reader without enlarging their claims.
