# Verification and replay

The two theorems have distinct arguments and were checked separately. The proofs, not these bounded computations, establish the universal claims.

- **Infinite two-generated loop, all odd primes.** An independent OpenAI mathematical review reconstructed the true affine section, the two-generator argument, the finite quotients, residual finiteness, and the opposite-hand obstruction; it checked Grishkov's question against the source. The [separate reasoning and adverse tests](independent-example-check.md) include a genuinely different separating family of finite truncations. No priority determination was made.
- **Matched one-sided group at exponent three.** A distinct independent OpenAI mathematical reading checked the signed double, the ternary reflection geometry, the finite-index central kernel, the original-group projection and the sharp 27 bound. It checked the **cardinality** hypothesis in Foguel–Kinyon–Phillips Theorem 4.17: it is supplied by their Corollary 4.22 only after the relevant subgroup is known finite. This proof review is not a fresh independent reproduction of the reflection checker.

The [affine-field checker](code/verify_affine_burnside_bol.py) constructs the small loops twice, using a class-two coset calculation and the explicit native law. It checks both Latin directions, powers, actual two-generation and **all 57,206,763 left Bol triples** across orders 27, 81, 125, 243 and 343. At order 243 the two points generate all 243 sites, while their two left translations generate just 27 permutations. [Recorded output](evidence/affine-burnside-bol.out).

The [independent native checker](code/check_native_t_adic_burnside.py) tests real loop tables from finite fields and nilpotent rings, includes the associative boundary, and follows the actual wrong-hand word on higher-dimensional truncations. [Recorded output](evidence/native-t-adic-burnside.out).

The [reflection checker](code/verify_exponent_three_reflection_closures.py) uses a nonabelian group with no inversion automorphism: the conjugation action on the reflection geometry loses a central subgroup of order three. It also checks all 531,441 ternary triples in a nonassociative 81-element commutative Moufang loop. [Recorded output](evidence/exponent-three-reflection-closures.out).

From this directory, using Python 3 with NumPy and SymPy for the two author checks; the independent checker needs only the standard library:

```sh
python code/verify_affine_burnside_bol.py
python code/check_native_t_adic_burnside.py
python code/verify_exponent_three_reflection_closures.py
```

Mira Cult directed the research. OpenAI models assisted with discovery, exposition, code and independent mathematical checks; exact model versions for these contributions were not established. There was no human journal review or proof-assistant verification.
