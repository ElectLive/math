"""Exact bases for C0010's alternating component bound with centralizer <=120.

Python 3.11+; standard library only. The recurrence, class-product/minimal-degree
arguments and analytic step-four ratios are mathematical inputs from C0007.
This script checks their new integer bases, not those proofs or all degrees.
"""

from math import factorial


def verify() -> None:
    fiber_bound = 120
    involutions = [1, 1]
    for degree in range(2, 19):
        involutions.append(involutions[-1] + (degree - 1) * involutions[-2])
    for degree in (17, 18):
        assert (
            2 * fiber_bound * involutions[degree] * 3 ** ((degree - 1) // 2)
            < factorial(degree)
        )

    for degree in range(49, 53):
        quarter = degree // 4
        rhs_times_four = (
            (degree - 2) * 2**quarter * factorial(quarter)
            * factorial(degree - 2 * quarter)
        )
        half_up = (degree + 1) // 2
        third_up = (degree + 2) // 3
        quarter_up = (degree + 3) // 4
        fifth_up = (degree + 4) // 5
        vertex_ceilings = (
            2 * 2**fifth_up * factorial(half_up) * factorial(fifth_up),
            2 * 4**degree * factorial(fifth_up),
            2 * 2**half_up * factorial(half_up),
            2 * 24**quarter_up * factorial(third_up),
        )
        assert all(4 * fiber_bound * upper < rhs_times_four for upper in vertex_ceilings)

    print("PASS: factor120 high bases17,18 and all four low vertices at49..52")


if __name__ == "__main__":
    verify()
