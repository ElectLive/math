#!/usr/bin/env python3
"""Exact arithmetic for the proposed solvable-stabilizer alternating screen.

Scope: 0323-finite-simple-non-moufang-bol-loops:C0010, m>=7, with an
actual solvable stabilizer H. This checks arithmetic only; the cycle-product
lemmas, Dixon bound, m=8 arguments and Aut(A6) cases are separate proof inputs.
Python standard library only. No subgroup-classification data are used.
"""
from math import factorial


def involutions(n):
    values = [1, 1]
    for d in range(2, n + 1):
        values.append(values[-1] + (d - 1) * values[-2])
    return values[n]


def class_size(m, k):
    return factorial(m) // (2**k * factorial(k) * factorial(m - 2*k))


def verify_stabilizer_screen():
    survivors = []
    for m in range(7, 26):
        sizes = [class_size(m, k) for k in range(m // 2 + 1)]
        for kind in ('A', 'S'):
            order = factorial(m) // (2 if kind == 'A' else 1)
            for mask in range(1, 1 << len(sizes)):
                indices = tuple(k for k in range(len(sizes)) if mask & (1 << k))
                if max(indices) == 0:
                    continue
                parity_count = len({k % 2 for k in indices})
                if kind == 'A' and parity_count != 1:
                    continue
                if kind == 'S' and parity_count != 2:
                    continue
                size = sum(sizes[k] for k in indices)
                if not 2 < size < order or order % size:
                    continue
                h = order // size
                # Dixon, cubed to avoid floating point.
                if h**3 > 24**(m - 1):
                    continue
                # If k_max>=floor(m/4), every nonidentity involution of A_m
                # lies in Λ². Thus H∩A_m is odd; [H:H∩A_m] is at most 2.
                if max(indices) >= m // 4:
                    h_even = h if kind == 'A' else h // 2 if h % 2 == 0 else h
                    if h_even % 2 == 0:
                        continue
                survivors.append((m, kind, indices, h))
    assert survivors == [(8, 'A', (1,), 720), (8, 'A', (1, 3), 45)], survivors
    # Infinite range base: m!/(2j_m) > 24^((m-1)/3), m=26.
    assert factorial(26)**3 > 8 * 24**25 * involutions(26)**3
    # Recurrence-induction base for 4 <= j_m/j_(m-1) <= (m+3)/4.
    assert 4*involutions(15) <= involutions(16)
    assert 4*involutions(16) <= 19*involutions(15)
    # 4m/(m+3)>cube_root(24) for all m>=26, by monotonicity.
    assert (4*26)**3 > 24 * 29**3
    return survivors


def verify_reversed_subsets():
    # Actual Li–Xia 4.3(b) exceptional group orders, with f=2 or 4.
    exceptional = [(25, 2, 25*24*4), (49, 2, 49*24*6),
                   (121, 2, 121*24*10), (529, 2, 529*24*22),
                   (81, 4, 81*32*20)]
    for n, f, order in exceptional:
        assert order <= 2*n*(n-1)*f
    # n>=10 recurrence base, and n=9 separately.
    assert factorial(8) > 4*10*involutions(8)
    assert factorial(7) > 8*2*involutions(7)
    # n=7 uses the nonexceptional |I|<=7*6, not the factor-two bound.
    assert factorial(5) > 4*involutions(5)
    # 3-subsets, n=32, actual solvable I<=AΓL1(32), order 32·31·5.
    assert factorial(32) > 12*(32*31*5)*involutions(29)


def main():
    survivors = verify_stabilizer_screen()
    verify_reversed_subsets()
    print('solvable-stabilizer arithmetic passed; m=8 cases:', survivors)
    print('reversed 2-subset and n=32 3-subset arithmetic passed')


if __name__ == '__main__':
    main()
