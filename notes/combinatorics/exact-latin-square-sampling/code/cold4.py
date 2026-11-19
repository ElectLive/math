"""Four-edge short-word rescue, with an exact decorated reference law.

Rows are in exposure order; draw/shuffle row labels outside this module.
A word is four row slots around an alternating column-symbol cycle. The
distinguished slot (the next row to fill) occurs one or two times. The
selection rule uses only integer comparisons. Backend defaults to the
finite matching-count DP; that backend does not meet the large-n theorem.
"""

from fractions import Fraction
from itertools import product
from math import factorial

from exact_core import full_board, delete_matching, permanent, sample_matching, randbelow
from selector import Odds


def _inv(row):
    out = [0] * len(row)
    for i, j in enumerate(row):
        out[j] = i
    return tuple(out)


def _advance(v, edge, row, inv):
    return row[v] if edge % 2 == 0 else inv[v]


def _cut(word, slot):
    return tuple(j for j, c in enumerate(word) if c == slot)


def _admissible(word, slot):
    return slot in word and all(c <= slot for c in word) and all(
        word[i] != word[(i + 1) % 4] for i in range(4)
    )


def _coordinates_from_starts(word, slot, before, starts):
    """Reconstruct vertices at cyclic positions 0,1,2,3 by open paths."""
    invs = tuple(map(_inv, before))
    cuts = _cut(word, slot)
    if len(cuts) != len(starts):
        raise ValueError("one coordinate per cut")
    vs = [None] * 4
    for cut, start in zip(cuts, starts):
        p = (cut + 1) % 4
        vs[p] = start
        while word[p] != slot:
            c = word[p]
            vs[(p + 1) % 4] = _advance(vs[p], p, before[c], invs[c])
            p = (p + 1) % 4
    if vs[0] == vs[2] or vs[1] == vs[3]:
        return None
    return tuple(vs)


def _vertices(vs):
    return frozenset((i % 2, v) for i, v in enumerate(vs))


def _pairs(word, slot, vs):
    ans = []
    for p in _cut(word, slot):
        u, v = vs[p], vs[(p + 1) % 4]
        ans.append((u, v) if p % 2 == 0 else (v, u))
    return tuple(ans)


def _packing(rows, slot, word):
    invs = tuple(map(_inv, rows))
    starts = set()
    for x in range(len(rows[0])):
        vs = [x]
        for p, c in enumerate(word):
            vs.append(_advance(vs[-1], p, rows[c], invs[c]))
        if vs[4] == x and vs[0] != vs[2] and vs[1] != vs[3]:
            starts.add((tuple(vs[(p + 1) % 4] for p in _cut(word, slot)), tuple(vs[:4])))
    occupied = set()
    out = []
    for root, v in sorted(starts):
        w = _vertices(v)
        if not occupied.intersection(w):
            out.append(root)
            occupied.update(w)
    return tuple(out)


def canonical_recipe(rows, slot, pin_divisor=16):
    """Return the profitable exact token and its canonical roots, or None."""
    if len(rows) != slot + 1 or pin_divisor < 1:
        raise ValueError("expected prefix through the distinguished row")
    n = len(rows[0])
    if n // pin_divisor < 1 or slot < 1:
        return None
    best, result = 1, None
    for word in product(range(slot + 1), repeat=4):
        if not _admissible(word, slot):
            continue
        m = len(_cut(word, slot))
        roots = _packing(rows, slot, word)[:n // (pin_divisor * m)]
        k = len(roots)
        # Threshold pays the exact token probability and an integer switch bound.
        gain = Fraction(factorial(k), (n ** 4) * (n + 1) * (4 ** (m * k)))
        if gain > best:
            best, result = gain, (word, roots)
    return result


def _conditional(board, pairs):
    n = len(board)
    a, b = dict(pairs), {v: u for u, v in pairs}
    if len(a) != len(pairs) or len(b) != len(pairs) or any(
        not (board[u] & (1 << v)) for u, v in pairs
    ):
        return None
    free_x = tuple(i for i in range(n) if i not in a)
    free_y = tuple(i for i in range(n) if i not in b)
    small = tuple(sum(((board[i] >> j) & 1) << k for k, j in enumerate(free_y))
                  for i in free_x)
    return small, free_x, free_y


def _pins(word, slot, before, roots):
    used, pairs = set(), []
    for root in roots:
        vs = _coordinates_from_starts(word, slot, before, root)
        if vs is None or used.intersection(_vertices(vs)):
            return None
        used.update(_vertices(vs))
        pairs.extend(_pairs(word, slot, vs))
    return tuple(pairs)


def forward(n, rng=None, *, pin_divisor=16, matching_fn=sample_matching,
            count_fn=permanent):
    """One subprobability trial. Return ordered rows and inverse odds or None."""
    board = full_board(n)
    history, factors = [], []
    multiplier = Fraction(1)
    for slot in range(n):
        early = slot < n // 4
        recipe = None
        if early:
            multiplier *= 2
        predicted = early and randbelow(2, rng)
        if predicted:
            word = tuple(randbelow(n, rng) for _ in range(4))
            k = randbelow(n + 1, rng)
            if not _admissible(word, slot):
                return None
            m = len(_cut(word, slot))
            if k == 0 or m * k > n // pin_divisor:
                return None
            roots = tuple(tuple(randbelow(n, rng) for _ in range(m)) for _ in range(k))
            pairs = _pins(word, slot, history, roots)
            if pairs is None:
                return None
            reduced = _conditional(board, pairs)
            if reduced is None or not count_fn(reduced[0]):
                return None
            factor, fx, fy = reduced
            row = dict(pairs)
            row.update((u, fy[v]) for u, v in zip(fx, matching_fn(factor, rng)))
            row = tuple(row[i] for i in range(n))
            recipe = word, tuple(sorted(roots))
            multiplier *= Fraction((n ** 4) * (n + 1) * n ** (m * k), factorial(k))
        else:
            factor = board
            row = matching_fn(board, rng)
        history.append(row)
        if early and canonical_recipe(history, slot, pin_divisor) != recipe:
            return None
        factors.append(factor)
        board = delete_matching(board, row)
    return tuple(history), Odds(multiplier, tuple(factors))


def reverse(ordered, *, pin_divisor=16):
    """Exact effective reciprocal forward atom after aggregating cycle orders."""
    n = len(ordered)
    board = full_board(n)
    factors, multiplier = [], Fraction(1)
    for slot, row in enumerate(ordered):
        recipe = None
        if slot < n // 4:
            multiplier *= 2
            recipe = canonical_recipe(ordered[:slot + 1], slot, pin_divisor)
        if recipe is None:
            factor = board
        else:
            word, roots = recipe
            m, k = len(_cut(word, slot)), len(roots)
            pairs = _pins(word, slot, ordered[:slot], roots)
            reduced = _conditional(board, pairs)
            assert reduced is not None and all(row[u] == v for u, v in pairs)
            factor = reduced[0]
            multiplier *= Fraction((n ** 4) * (n + 1) * n ** (m * k), factorial(k))
        factors.append(factor)
        board = delete_matching(board, row)
    return Odds(multiplier, tuple(factors))
