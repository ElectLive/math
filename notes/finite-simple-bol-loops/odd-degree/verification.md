# What was checked

Each of the five proofs has its own independent AI mathematical review. The reviews do not establish historical priority, formal correctness or human-referee acceptance. More importantly, they check different things:

| Proof | Distinct challenge checked | Rerunnable independent check |
|---|---|---|
| [Cube-free normal tower](manuscripts/odd-cubefree-normal-tower.md) | The nonscalar 3-dimensional exception, the two projections of the doubled group, and lifting the full tower inside the original loop | [Checker](code/check_cubefree_congruence_and_reflections.py) · [output](evidence/odd_cubefree_normal_tower-independent.out) |
| [Two-prime threshold](manuscripts/two-prime-exponent-threshold.md) | Coprime weights without assuming semisimplicity of the whole modular representation; the previously established existence direction is a separate input | [Checker](code/check_prime_field_threshold.py) · [output](evidence/two_prime_threshold-independent.out) |
| [Least odd simple order](manuscripts/least-odd-simple-bol-order.md) | The 675 Sylow actions with a real projection kernel, the 945 exclusion and exhaustive small-order sieve; Nagy's earlier upper witness | [Checker](code/check_min_odd_order_hostile.py) · [output](evidence/least_odd_bol_order-independent.out) |
| [Abelian Bruck associate](manuscripts/abelian-bruck-fibers-as-alternating-algebras.md) | Recovery of the bracket from native translations, the isotope action and the quadratic family; no claim of prime-cube exhaustion from this proof alone | [Checker](code/check_abelian_bruck_coset_and_isotope.py) · [output](evidence/abelian_bruck_algebra-independent.out) |
| [Complete prime-cube list](manuscripts/all-bol-loops-of-prime-cube-order.md) | The class-three power carries, actual class-four stabilizer planes and rootless-cubic equivalence; tested all 806 and 2,850 planes at the two smallest fields respectively | [Checker](code/check_distinct_cubic_action_and_engel_powers.py) · [output](evidence/prime_cube_bol_folders-independent.out) |

Run the standard-library Python 3 programs from this directory. The first command uses the independently reproduced [63-point multiplication table](../odd-bol-hall/evidence/order-63-no-sylow.csv). No display, network or computer-algebra installation is required.

```sh
python code/check_cubefree_congruence_and_reflections.py ../odd-bol-hall/evidence/order-63-no-sylow.csv
python code/check_prime_field_threshold.py
python code/check_min_odd_order_hostile.py
python code/check_abelian_bruck_coset_and_isotope.py
python code/check_distinct_cubic_action_and_engel_powers.py
```

Author-side controls are linked from each proof with their recorded outputs. The actual 63-point congruence calculation, for example, finds a 7,3,3 normal tower despite the absence of a native order-nine subloop. The finite computations supplement, rather than replace, the arguments for all orders. Mira Cult directed the research. OpenAI models assisted in discovery, exposition and the separate mathematical reviews; exact model versions were not verified.
