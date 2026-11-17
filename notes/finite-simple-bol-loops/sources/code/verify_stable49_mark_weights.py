"""Exact necklace-weight certificate for the stable 49-point exclusion.

Run with Python 3.11+ and assertions enabled. No input files are needed.
"""

from itertools import product


def rotate(mask: int) -> int:
    return ((mask << 1) & 0x7F) | (mask >> 6)


def main() -> None:
    unseen = set(range(1 << 7))
    counts = [0] * 8
    while unseen:
        start = min(unseen)
        orbit = set()
        x = start
        while x not in orbit:
            orbit.add(x)
            x = rotate(x)
        assert x == start
        assert len(orbit) in (1, 7)
        assert all(bin(y).count("1") == bin(start).count("1") for y in orbit)
        counts[bin(start).count("1")] += 1
        unseen.difference_update(orbit)
    assert counts == [1, 1, 3, 5, 5, 3, 1, 1]
    bounds = counts[1:7]
    total = 0
    divisible = []
    smooth = []
    for coefficients in product(*(range(bound + 1) for bound in bounds)):
        total += 1
        weight = 15**7 + 7 * sum(
            coefficients[d - 1] * 15**d for d in range(1, 7)
        )
        assert weight % 7 == 1
        if weight % (2**14) == 0:
            divisible.append((coefficients, weight))
        remaining = weight
        for prime in (2, 3, 5):
            while remaining % prime == 0:
                remaining //= prime
        if remaining == 1:
            smooth.append((coefficients, weight))
    assert total == 2304
    assert divisible == []
    assert smooth == [((0, 0, 0, 0, 0, 0), 15**7)]
    print("necklace counts:", counts)
    print("coefficient vectors:", total)
    print("weights divisible by 2^14:", len(divisible))
    print("2,3,5-smooth weights:", smooth)


if __name__ == "__main__":
    main()
