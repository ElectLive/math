# Collective charged transport: exact finite controls

Canonical proof: [CT1--CT7](../manuscripts/bol-collective-charged-transport.md).
Executable: [verify_bol_collective_transport.py](../code/verify_bol_collective_transport.py).
Output: [complete JSON](bol-collective-transport-certificate.json).
These manuscript-local results allocate no permanent claim IDs.

The exact scientific revision and actual independent reviewer are recorded
in the continuation review, once that review has occurred. This calculation
note asserts no mathematical acceptance by itself.

## Reproduction

Python 3.12.14, standard library, assertions enabled. From the repository root:

```sh
python problems/0323-finite-simple-non-moufang-bol-loops/code/verify_bol_collective_transport.py
```

The output includes the executable SHA-256. The optional `--certificate PATH`
writes the same JSON. No numerical differential-equation solve or theta
approximation is involved.

## Checked instances

The finite completion control uses p=3, W=F3^2, b_mu=mu I, with both signs
of the form C=((0,2),(1,0)). Its order-four automorphism R=C transports
the central charge by -1 and the completion by -1. The inverse used in J
is that of the **transpose map** associated to the displayed bilinear form.

- 4,374 moving-completion/charge covariance equations; omitting the base
  pullback fails in 2,592 cases.
- 8,748 first-axis and 8,748 second-axis full operator coefficient
  identities; 5,832 first-axis symbols differ from the untwisted symbol.
- 216 transported-holonomy-pair equations, with actual inner conjugation.
- 81 carry identities and 405 true-dual integer equations, including
  45 actual zero-degree input instances.
- The tensor unit retains its finite base difference action. Only its
  physical matrix action is trivial; constants on the base are fixed.
- 49 Gamma(6) matrices; 1,617 exact Chern metric identities, 3,234
  trivial automorphy phases, 192 modular composition identities and
  4,851 signed-degree gauge product identities.

The matrix and modular tests use exact finite-field and complex-rational
arithmetic. These are meaningful finite controls for the pullback signs,
noncentral mixing, zero-degree coverage and modular conventions. They do
not replace CT's universal proofs. The order-four automorphism control is
not asserted to be the original odd rigid Bol loop.

## Limits

The connection uses collective group-like tensor transport, not ordinary
primitive transport. Its dynamical parameter is finite. This script does
not prove compatibility with CE's continuous-Cartan connection, identify
the response with an old Fock trace, or prove a full SL2 modular descent.
The convergence and analytic payoff are proved in CT and SA and checked
by mathematical review, separately from this certificate.
