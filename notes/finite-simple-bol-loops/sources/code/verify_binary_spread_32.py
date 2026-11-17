"""Verify the fixed F32 spread witness using Python 3.11+ and assertions."""

from collections import Counter

if not __debug__:
    raise RuntimeError("run this verifier with assertions enabled")

P = 0b100101  # X^5 + X^2 + 1
COLS = (813, 201, 812, 499, 143, 634, 838, 938, 484, 459)

def degree(a):
    return a.bit_length() - 1

def rem(a, b):
    while a and degree(a) >= degree(b):
        a ^= b << (degree(a) - degree(b))
    return a

# A reducible degree-five polynomial has a factor of degree at most two.
assert degree(P) == 5
assert all(rem(P, d) for d in range(2, 8) if 1 <= degree(d) <= 2)

def mul(a, b):
    out = 0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & 32:
            a ^= P
    return out

def trace(a):
    result = 0
    for _ in range(5):
        result ^= a
        a = mul(a, a)
    assert result in (0, 1)
    return result

def pairing(u, v):
    return trace(mul(u & 31, v >> 5) ^ mul(u >> 5, v & 31))

def image(x):
    out = 0
    for i in range(10):
        if x >> i & 1:
            out ^= COLS[i]
    return out

# Check invertibility and preservation on all pairs of binary basis vectors.
assert len({image(x) for x in range(1024)}) == 1024
assert all(pairing(image(1 << i), image(1 << j)) == pairing(1 << i, 1 << j)
           for i in range(10) for j in range(10))
# Lines of slopes t, plus the vertical line; zero is included.
lines = [{a | (mul(t, a) << 5) for a in range(32)} for t in range(32)]
lines.append({a << 5 for a in range(32)})
assert all(len(line) == 32 for line in lines)
assert len(set.union(*lines)) == 1024
assert all(lines[i] & lines[j] == {0} for i in range(33) for j in range(i))
transformed_lines = [{image(x) for x in line} for line in lines]
counts = Counter(len(a & b) for a in lines for b in transformed_lines)
assert counts == {1: 480, 2: 444, 4: 144, 8: 21}
print('F32 modulus:', bin(P))
print('matrix columns:', COLS)
print('intersection cardinalities:', dict(sorted(counts.items())))
print('maximum F2 intersection dimension:', max(counts).bit_length() - 1)
