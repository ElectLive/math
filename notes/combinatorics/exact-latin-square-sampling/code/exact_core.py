"""Exact finite reference algorithms for labeled Latin squares and bipartite PMs.

Boards are tuples of n masks: bit s of board[j] permits symbol s in column j.
Outputs are tuples of rows, with labels 0,...,n-1. No third-party packages.
The public random APIs default to system randomness. A supplied rng must
provide getrandbits(k); exact distribution assumes independent fair bits.
Neither backend in this module claims polynomial expected asymptotic time.
"""

from functools import lru_cache
from math import factorial
from random import SystemRandom

_SYSTEM = SystemRandom()


def _natural(x, positive=False):
    if type(x) is not int or x < int(positive):
        raise ValueError("expected a positive integer" if positive else "expected a nonnegative integer")
    return x


def randbelow(bound, rng=None):
    """Uniform integer on [0,bound), using fair bits and rejection, never modulo."""
    _natural(bound, positive=True)
    if bound == 1:
        return 0
    bits = (bound - 1).bit_length()
    draw = (_SYSTEM if rng is None else rng).getrandbits
    while True:
        r = draw(bits)
        if r < bound:
            return r


def coin(numerator, denominator, rng=None):
    _natural(denominator, positive=True)
    _natural(numerator)
    if numerator > denominator:
        raise ValueError("probability above 1")
    return numerator == denominator or (numerator != 0 and randbelow(denominator, rng) < numerator)


def full_board(n):
    _natural(n, positive=True)
    return ((1 << n) - 1,) * n


def _board(board):
    b = tuple(board)
    lim = 1 << len(b)
    if any(type(x) is not int or x < 0 or x >= lim for x in b):
        raise ValueError("invalid board mask")
    return b


def _bits(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit


def _rows(b):
    """Iterate all perfect matchings; explicit stack so depth needn't fit Python recursion."""
    n = len(b)
    if not n:
        yield ()
        return
    chosen = [0] * n
    used = [0] * (n+1)
    todo = [0] * n
    j, todo[0] = 0, b[0]
    while j >= 0:
        if not todo[j]:
            j -= 1
            continue
        bit = todo[j] & -todo[j]
        todo[j] ^= bit
        chosen[j] = bit.bit_length()-1
        if j+1 == n:
            yield tuple(chosen)
        else:
            used[j+1] = used[j] | bit
            j += 1
            todo[j] = b[j] & ~used[j]


def matchings(board):
    """All allowed row permutations in lexicographic order, lazy."""
    return _rows(_board(board))


def _del(b, row):
    return tuple(mask ^ (1 << s) for mask, s in zip(b, row))


def delete_matching(board, row):
    b, row = _board(board), tuple(row)
    n = len(b)
    if (len(row) != n or any(type(s) is not int or s < 0 or s >= n for s in row)
            or len(set(row)) != n or any(not (mask & (1 << s)) for mask, s in zip(b, row))):
        raise ValueError("row is not a perfect matching of this board")
    return _del(b, row)


def _suffix(b):
    """table[u] counts completions when the bit set u of symbols is already used."""
    n = len(b)
    end = (1 << n)-1
    tab = [0] * (end+1)
    tab[end] = 1
    for u in range(end-1, -1, -1):
        avail = b[u.bit_count()] & ~u
        acc = 0
        while avail:
            bit = avail & -avail
            acc += tab[u | bit]
            avail ^= bit
        tab[u] = acc
    return tab


def permanent(board):
    """Integer 0/1 permanent, O(n 2^n) additions, including per(empty)=1."""
    return _suffix(_board(board))[0]


def _unrank_pm(b, table, rank):
    if type(rank) is not int or not 0 <= rank < table[0]:
        raise ValueError("matching rank out of range")
    u, out = 0, []
    for mask in b:
        for bit in _bits(mask & ~u):
            size = table[u | bit]
            if rank < size:
                out.append(bit.bit_length()-1)
                u |= bit
                break
            rank -= size
    return tuple(out)


def unrank_matching(board, rank):
    b = _board(board)
    return _unrank_pm(b, _suffix(b), rank)


def sample_matching(board, rng=None):
    b = _board(board)
    table = _suffix(b)
    if not table[0]:
        raise ValueError("board has no perfect matching")
    return _unrank_pm(b, table, randbelow(table[0], rng))


def _permutation(rank, n):
    """Lehmer unranking on [n]."""
    items = list(range(n))
    result = []
    for i in range(n-1, -1, -1):
        q, rank = divmod(rank, factorial(i))
        result.append(items.pop(q))
    return tuple(result)


def _root(m, d):
    """floor(m**(1/d)) for m>=1, exact integer binary search."""
    low = 1 << ((m.bit_length()-1)//d)
    high = low*2
    while high-low > 1:
        v = (high+low)//2
        if v**d <= m:
            low = v
        else:
            high = v
    return low


@lru_cache(maxsize=1024)
def row_envelope(n, d):
    """Always at least the permanent of a d-regular n+n board."""
    _natural(n, positive=True)
    if type(d) is not int or not 1 <= d <= n:
        raise ValueError("degree must be 1,...,n")
    if d == 1: return 1
    if d == 2: return 1 << (n//2)  # at most floor(n/2) alternating cycles
    if d == n: return factorial(n)
    if d == n-1:  # complement of a perfect matching: exactly the derangement count
        a, b = 1, 0
        for i in range(2, n+1): a, b = b, (i-1)*(a+b)
        return b
    return _root(factorial(d)**n, d)  # integral floor of the Brégman bound


def rejection_trial(n, rng=None):
    """One finite row-gated trial; None is an explicit rejection, never a square."""
    board = full_board(n)
    result = []
    for d in range(n, 0, -1):
        table = _suffix(board)
        if not coin(table[0], row_envelope(n, d), rng):
            return None
        row = _unrank_pm(board, table, randbelow(table[0], rng))
        result.append(row)
        board = _del(board, row)
    return tuple(result)


def _mode_key(board):
    # Exchange of any two columns except column zero preserves the number of
    # completions with the prescribed first column. Columns remain labeled
    # for enumeration: this only merges equal *count* queries.
    return board[:1] + tuple(sorted(board[1:]))


class ReducedSpace:
    """Completion counting and unranking in the first-row/first-column identity chart.

    A local memo is shared across draws from this object, not retained globally.
    Finite DP, not an asymptotically polynomial algorithm.
    """
    def __init__(self, n):
        self.n = _natural(n, positive=True)
        self.first = tuple(range(n))
        self.start = _del(full_board(n), self.first)
        self._cache = {}

    def _count(self, board):
        k = self.n - board[0].bit_count()
        if k >= self.n - 1:
            return 1  # final perfect matching forced; its first symbol is k
        key = _mode_key(board)
        if key not in self._cache:
            constrained = (1 << k,) + key[1:]
            self._cache[key] = sum(self._count(_del(key, row)) for row in _rows(constrained))
        return self._cache[key]

    @property
    def reduced_count(self):
        return self._count(self.start)

    @property
    def labeled_count(self):
        return self.reduced_count * factorial(self.n) * factorial(self.n-1)

    def unrank_reduced(self, rank):
        if type(rank) is not int or not 0 <= rank < self.reduced_count:
            raise ValueError("reduced square rank out of range")
        rows = [self.first]
        board = self.start
        for k in range(1, self.n):
            for row in _rows((1 << k,) + board[1:]):
                rem = _del(board, row)
                weight = self._count(rem)
                if rank < weight:
                    rows.append(row)
                    board = rem
                    break
                rank -= weight
            else:
                raise AssertionError("unranking inconsistent with completion count")
        return tuple(rows)

    def unrank(self, rank):
        if type(rank) is not int or not 0 <= rank < self.labeled_count:
            raise ValueError("labeled square rank out of range")
        q, irow = divmod(rank, factorial(self.n-1))
        ired, isym = divmod(q, factorial(self.n))
        reduced = self.unrank_reduced(ired)
        symbols = _permutation(isym, self.n)
        order = (0,) + tuple(j+1 for j in _permutation(irow, self.n-1))
        return tuple(tuple(symbols[s] for s in reduced[i]) for i in order)

    def sample(self, rng=None):
        return self.unrank(randbelow(self.labeled_count, rng))


def sample_latin(n, rng=None, *, method="auto"):
    """Uniform on all labeled n-by-n squares under fair random bits; 0-based symbols.

    auto uses reduced DP for n<=7 and direct row rejection otherwise. For a
    batch of small squares, reuse ReducedSpace(n).sample() to share its memo.
    """
    _natural(n, positive=True)
    if method == "auto":
        method = "reduced" if n <= 7 else "rejection"
    if method == "reduced":
        return ReducedSpace(n).sample(rng)
    if method == "rejection":
        while True:
            square = rejection_trial(n, rng)
            if square is not None:
                return square
    if method in ("decorated","huber"):
        from decorated import sample_decorated, sample_huber
        return (sample_decorated if method=="decorated" else sample_huber)(n,rng)
    raise ValueError("unknown sampler method")


def iter_latin(n):
    """All labeled squares, directly by row DFS. Intended for small truth tables."""
    initial = full_board(n)
    def visit(board, rows):
        if len(rows) == n:
            yield rows
            return
        for row in _rows(board):
            yield from visit(_del(board, row), rows + (row,))
    return visit(initial, ())


def is_latin(square):
    try:
        s = tuple(tuple(row) for row in square)
    except TypeError:
        return False
    n = len(s)
    alphabet = set(range(n))
    return (n > 0 and all(len(row) == n and all(type(x) is int for x in row)
                           and set(row) == alphabet for row in s)
            and all(set(col) == alphabet for col in zip(*s)))
