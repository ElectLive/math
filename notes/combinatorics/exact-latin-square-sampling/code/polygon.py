"""Exact decorated color-polygon seed. Forward vetoes return None, never retry.

Rows are permutations x->symbol. A labeled mark is (left_vertices, right_vertices)
in traversal order; changing the root can produce a different mark even if its
vertex sets coincide. All samplers consume only rng.getrandbits(k).
"""
from collections import Counter
from dataclasses import dataclass
from fractions import Fraction
from math import factorial
from random import SystemRandom

Row = tuple[int, ...]
Word = tuple[int, ...]
Mark = tuple[Row, Row]


def _below(n, rng):
    if n < 1:
        raise ValueError("empty integer range")
    k = (n - 1).bit_length()
    if k == 0:
        return 0
    while True:
        x = rng.getrandbits(k)
        if x < n:
            return x


def _shuffle(xs, rng):
    data = list(xs)
    for i in range(len(data) - 1, 0, -1):
        j = _below(i + 1, rng)
        data[i], data[j] = data[j], data[i]
    return data


def admissible(word):
    """The implicit prior retains proper, first-appearance numbered words only."""
    if not word or len(word) < 4 or len(word) % 2:
        return False
    next_name = 0
    for i, x in enumerate(word):
        if type(x) is not int or x < 0 or x > next_name or x == word[i - 1]:
            return False
        if x == next_name:
            next_name += 1
    return min(Counter(word).values()) >= 2


def draw_word_tagged(max_half, rng=None):
    """A canonical length-2*l word has mass 2^-l / 2^(2*l*ceil(log2(2l)))."""
    if type(max_half) is not int or max_half < 0:
        raise ValueError("max_half must be a nonnegative integer")
    rng = rng if rng is not None else SystemRandom()
    for l in range(1, max_half + 1):
        if rng.getrandbits(1):
            if l == 1:
                return None, True
            bits = (2*l - 1).bit_length()
            word = tuple(rng.getrandbits(bits) for _ in range(2*l))
            return (word if admissible(word) else None), False
    return None, False


def draw_word(max_half, rng=None):
    return draw_word_tagged(max_half,rng)[0]


def _check(n, slots, word):
    if type(n) is not int or n < 1 or type(slots) is not int or not 0 <= slots <= n:
        raise ValueError("require n>=1 and 0<=slots<=n")
    if word is not None and (not admissible(word) or max(word) >= slots):
        raise ValueError("invalid or unallocated color word")


def _validate(rows, n):
    if any(len(r) != n or any(type(i) is not int for i in r)
           or set(r) != set(range(n)) for r in rows):
        raise ValueError("each row must be a permutation of range(n)")
    if any(len({r[x] for r in rows}) != len(rows) for x in range(n)):
        raise ValueError("duplicate symbol at a column")


def mark_counts(n, slots, word):
    """Unrestricted counts (not probabilities) split by the number of marks."""
    _check(n, slots, word)
    if word is None:
        return (factorial(n)**slots,)
    l = len(word)//2
    counts = Counter(word)
    fac = [1]
    for i in range(1, n + 1):
        fac.append(fac[-1]*i)
    ws = []
    for m in range(n//l + 1):
        ordered = (fac[n]//fac[n-m*l])**2
        ordered *= fac[n]**(slots-len(counts))
        for ej in counts.values():
            ordered *= fac[n-m*ej]
        whole, rem = divmod(ordered, fac[m])
        if rem:  # free action reordering nonoverlapping labeled copies
            raise ArithmeticError("nonintegral decoration count")
        ws.append(whole)
    return tuple(ws)


def _copies(rows, word, n):
    inverses = []
    for row in rows:
        inv = [0]*n
        for x,y in enumerate(row):
            inv[y] = x
        inverses.append(inv)
    l = len(word)//2
    for root in range(n):
        x = root
        left, right = [], []
        for j in range(l):
            y = rows[word[2*j]][x]
            left.append(x)
            right.append(y)
            x = inverses[word[2*j+1]][y]
        if x == root and len(set(left)) == len(set(right)) == l:
            yield tuple(left), tuple(right)


def canonical_packing(rows, word):
    """Greedily take vertex-disjoint labeled copies in increasing root order."""
    if not rows or word is None:
        if word is None:
            return ()
        raise ValueError("real word requires row slots")
    n = len(rows[0])
    _check(n,len(rows),word)
    _validate(rows,n)
    pack, lused, rused = [], set(), set()
    for mark in _copies(rows,word,n):
        left,right = mark
        if lused.isdisjoint(left) and rused.isdisjoint(right):
            pack.append(mark)
            lused.update(left)
            rused.update(right)
    return tuple(pack)


@dataclass(frozen=True)
class PolygonSeed:
    rows: tuple[Row, ...]
    marks: tuple[Mark, ...]
    packing_size: int
    ratio: Fraction  # conditional reverse mass / forward submass (prior cancels)


def seed_forward(n, slots, word, rng=None):
    """Sample the unrestricted decorated block once, then apply both vetoes."""
    weights = mark_counts(n,slots,word)
    rng = rng if rng is not None else SystemRandom()
    z = sum(weights)
    r = _below(z,rng) if len(weights)>1 else 0
    m = 0
    while r >= weights[m]:
        r -= weights[m]
        m += 1
    pins = [dict() for _ in range(slots)]
    marks = []
    if m:
        l = len(word)//2
        left, right = _shuffle(range(n),rng)[:m*l], _shuffle(range(n),rng)[:m*l]
        for j in range(m):
            X, Y = tuple(left[j*l:(j+1)*l]),tuple(right[j*l:(j+1)*l])
            marks.append((X,Y))
            for i in range(l):
                pins[word[2*i]][X[i]]=Y[i]
                pins[word[2*i+1]][X[(i+1)%l]]=Y[i]
    rows=[]
    for p in pins:
        free = _shuffle(sorted(set(range(n)).difference(p.values())),rng)
        it = iter(free)
        rows.append(tuple(p[x] if x in p else next(it) for x in range(n)))
    rows=tuple(rows)
    if any(len({row[x] for row in rows}) != slots for x in range(n)):
        return None
    packing=canonical_packing(rows,word)
    if not set(marks).issubset(packing):
        return None
    return PolygonSeed(rows,tuple(sorted(marks)),len(packing),Fraction(z,1<<len(packing)))


def seed_reverse(rows, word, rng=None, *, n=None):
    """Draw independent fair subset of the canonical packing of a legal block."""
    rows=tuple(tuple(r) for r in rows)
    if n is None:
        if not rows: raise ValueError("empty block requires n")
        n=len(rows[0])
    _check(n,len(rows),word)
    _validate(rows,n)
    rng=rng if rng is not None else SystemRandom()
    packing=canonical_packing(rows,word)
    marks=tuple(mark for mark in packing if rng.getrandbits(1))
    z=sum(mark_counts(n,len(rows),word))
    return PolygonSeed(rows,marks,len(packing),Fraction(z,1<<len(packing)))
