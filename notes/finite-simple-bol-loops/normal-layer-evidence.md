# Evidence for the matched tensor and odd block-kernel theorems

**Mira Cult**

This is the supporting record for [0100: matched tensor radicals](manuscripts/0100-matched-tensor-radicals.md) and [0101: the kernel of the action on blocks](manuscripts/0101-odd-kernel-block-action.md). All necessary new proof dependencies are publicly readable; the frozen source identifiers below distinguish research revisions rather than serving as required private links.

| Public assertion | Exact scientific source | Mathematical evidence |
| --- | --- | --- |
| 0100, ranks at least three except the binary rank-three residual | `c4791c77dfb778c368006c71abad7eef2b58a777` | One independent OpenAI model accepted the [rank-capacity proof](sources/tensor-layers/tensor-capacity.md) within its hypotheses, including the actual characteristic-two phases, maximal-factorization table rows and binary rank-four endpoints. It read the [odd-field foundation](sources/tensor-layers/odd-field-foundation.md); this is not a separate new audit of every imported classification. |
| 0100, binary rank three alone | `d9c959216f10dea547baf82fdabc18c17dd36ca5` | The same reviewer separately accepted the [binary supplement](sources/tensor-layers/binary-three.md), including the nonsplit obstruction and arbitrary stabilizer cocycles. |
| 0101, odd kernels and the radical of the block-action kernel | `2756e74daf61aaed60f017ebbf6369026cced801` | The same reviewer independently accepted the [odd-kernel proof](manuscripts/0101-odd-kernel-block-action.md), including the difference between the stable-splitting assumption for the cohomological statement and the unconditional block-radical conclusion under faithful irreducibility. |

These are three separately pinned mathematical reviews by **one** AI reviewer. The immutable source manuscript SHA-256 digests, in the order above, are `5bb482b3dfa5c87b893ae295a74fa2edb07a09d073c53ffe6b0238ba9c7bd157`, `63df04a5c59dc91ad8f1ed9fa28c49b0b3c4c57f0db627c11350c3d5b5481661` and `d2b446551c3b3de0a5c7ce52342e260bdfecf8a905153f71178bb35e822d1277`. The public exposition is edited for readers. Substantive claims about broader projective actions, higher-rank arbitrary inversions, and a canonical descent for general positive solvable radical are **not independently established by these reviews** and are not needed for these two public theorems. The unrestricted classification remains open.

## Reproduce the finite controls

From this notes directory, with Python 3.10 or newer and no third-party packages:

```sh
python3 sources/code/verify_swapped_tensor_radical.py
python3 sources/code/verify_tensor_parity_capacity.py
python3 sources/code/verify_binary_three_tensor_residual.py
python3 sources/code/verify_odd_kernel_core_obstruction.py
python3 sources/code/check_c479_even_phase_and_algebra.py
python3 sources/code/check_d9c9_bar_obstruction_independent.py
python3 sources/code/check_odd_kernel_block_independent.py
```

The first four are [odd tensor](sources/code/verify_swapped_tensor_radical.py), [capacity](sources/code/verify_tensor_parity_capacity.py), [binary residual](sources/code/verify_binary_three_tensor_residual.py) and [odd block kernel](sources/code/verify_odd_kernel_core_obstruction.py) controls. The last three, [nonprime-field phases and algebra](sources/code/check_c479_even_phase_and_algebra.py), [mixed cocycles and all binary stabilizer gauges](sources/code/check_d9c9_bar_obstruction_independent.py), and [odd block-kernel boundary examples](sources/code/check_odd_kernel_block_independent.py), were written independently of the corresponding original checks. The odd-kernel program explicitly verifies a nonsplit congruence extension; it does not purport to construct a simple loop from that group.

## Contributions

Under Mira Cult’s research direction, OpenAI models contributed the mathematical arguments, finite checks, independent review and public exposition. The research record used here does not identify the exact model version for each contribution. Neither model review nor a successful finite replay is human peer review, a proof-assistant formalization or a general loop census.
