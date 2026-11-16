"""Exact permutation group algorithms in pure Python (3.9+).

Implements:
  1. Deterministic incremental Schreier-Sims for Base and Strong Generating Sets (BSGS),
     with source-level strong-generator filtering so generator sets stay compact.
  2. Deterministic Jordan prime-cycle certification for A_n / S_n (n >= 8): constructs an
     explicit word z = w^M in G, verifies cycle_type(z) == (1, ..., 1, p) for a prime
     p <= n - 3, and verifies primitivity of G via Atkinson's exact block test on all
     points {1, ..., n-1}, proving G >= A_n by Jordan's Theorem (Wielandt, Thm 13.9),
     then distinguishes A_n vs S_n by exact generator parities.
  3. Exact group order, read-only membership test, point stabilizers, orbit/subdegree
     computation, permutation rank, and Atkinson's block-system primitivity test.

Action convention: LEFT action, i.e., (g * h)(x) = g[h[x]].
"""

from __future__ import annotations

import math
import random
from collections import deque
from math import gcd
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

Perm = Tuple[int, ...]


def identity_perm(n: int) -> Perm:
    return tuple(range(n))


def compose(f: Perm, g: Perm) -> Perm:
    """Return f o g under left action: (f o g)(x) = f[g[x]]."""
    return tuple(f[gx] for gx in g)


def invert(f: Perm) -> Perm:
    """Return the inverse permutation of f."""
    inv = [0] * len(f)
    for i, fi in enumerate(f):
        inv[fi] = i
    return tuple(inv)


def perm_pow(f: Perm, k: int) -> Perm:
    """Return f^k for any integer k."""
    n = len(f)
    if k == 0:
        return identity_perm(n)
    if k < 0:
        f = invert(f)
        k = -k
    res = identity_perm(n)
    base = f
    while k > 0:
        if k & 1:
            res = compose(res, base)
        k >>= 1
        if k:
            base = compose(base, base)
    return res


def cycle_lengths(f: Perm) -> List[int]:
    """Return list of all cycle lengths (including 1-cycles)."""
    n = len(f)
    seen = [False] * n
    lengths: List[int] = []
    for i in range(n):
        if not seen[i]:
            c = 0
            cur = i
            while not seen[cur]:
                seen[cur] = True
                cur = f[cur]
                c += 1
            lengths.append(c)
    return lengths


def cycle_type(f: Perm) -> Tuple[int, ...]:
    """Return sorted tuple of cycle lengths (including fixed points as 1-cycles)."""
    lengths = cycle_lengths(f)
    lengths.sort()
    return tuple(lengths)


def perm_sign(f: Perm) -> int:
    """Return +1 if f is an even permutation, -1 if odd."""
    n = len(f)
    num_cycles = len(cycle_lengths(f))
    return 1 if (n - num_cycles) % 2 == 0 else -1


def perm_order(f: Perm) -> int:
    """Return the multiplicative order of permutation f."""
    ord_val = 1
    for c in cycle_lengths(f):
        ord_val = (ord_val * c) // gcd(ord_val, c)
    return ord_val


def cycles_to_perm(n: int, cycles: Sequence[Sequence[int]], one_based: bool = False) -> Perm:
    """Convert disjoint cycle notation into a 0-based Perm of degree n."""
    arr = list(range(n))
    offset = 1 if one_based else 0
    for cyc in cycles:
        if len(cyc) <= 1:
            continue
        k = len(cyc)
        for i in range(k):
            src = cyc[i] - offset
            dst = cyc[(i + 1) % k] - offset
            arr[src] = dst
    return tuple(arr)


def compute_orbits(n: int, gens: Sequence[Perm]) -> List[List[int]]:
    """Return sorted list of orbits (each sorted) of <gens> on {0, ..., n-1}."""
    seen = [False] * n
    orbits: List[List[int]] = []
    for start in range(n):
        if seen[start]:
            continue
        orb = [start]
        seen[start] = True
        q = deque([start])
        while q:
            u = q.popleft()
            for g in gens:
                v = g[u]
                if not seen[v]:
                    seen[v] = True
                    orb.append(v)
                    q.append(v)
        orb.sort()
        orbits.append(orb)
    return orbits


def _is_prime(k: int) -> bool:
    if k < 2:
        return False
    if k % 2 == 0:
        return k == 2
    d = 3
    while d * d <= k:
        if k % d == 0:
            return False
        d += 2
    return True


def _atkinson_is_primitive_raw(n: int, gens: Sequence[Perm]) -> bool:
    """Exact primitivity check on {0, ..., n-1} directly from `gens` (tests all a in 1..n-1).

    Uses an exact two-stage closure: first propagates under up to 16 pseudo-randomly sampled
    generators; if that already merges all n points into 1 block, the full closure is provably
    trivial. Otherwise closes the partial block to fixed point under ALL generators in `gens`.
    """
    if n < 2 or not gens:
        return False
    orbs = compute_orbits(n, gens)
    if len(orbs) != 1 or len(orbs[0]) != n:
        return False

    m = len(gens)
    if m <= 16:
        fast_gens: Sequence[Perm] = gens
    else:
        rng = random.Random(323)
        fast_gens = [gens[idx] for idx in sorted(rng.sample(range(m), 16))]

    for a in range(1, n):
        parent = list(range(n))
        parent[a] = 0
        merged = 1
        q: deque[Tuple[int, int]] = deque([(0, a)])
        history: List[Tuple[int, int]] = [(0, a)]
        while q and merged < n - 1:
            u, v = q.popleft()
            for g in fast_gens:
                gu, gv = g[u], g[v]
                while parent[gu] != gu:
                    parent[gu] = parent[parent[gu]]
                    gu = parent[gu]
                while parent[gv] != gv:
                    parent[gv] = parent[parent[gv]]
                    gv = parent[gv]
                if gu != gv:
                    if gu > gv:
                        gu, gv = gv, gu
                    parent[gv] = gu
                    merged += 1
                    q.append((gu, gv))
                    if m > 16:
                        history.append((gu, gv))
                    if merged == n - 1:
                        break
        if merged < n - 1 and m > 16:
            q_full: deque[Tuple[int, int]] = deque(history)
            while q_full and merged < n - 1:
                u, v = q_full.popleft()
                for g in gens:
                    gu, gv = g[u], g[v]
                    while parent[gu] != gu:
                        parent[gu] = parent[parent[gu]]
                        gu = parent[gu]
                    while parent[gv] != gv:
                        parent[gv] = parent[parent[gv]]
                        gv = parent[gv]
                    if gu != gv:
                        if gu > gv:
                            gu, gv = gv, gu
                        parent[gv] = gu
                        merged += 1
                        q_full.append((gu, gv))
                        if merged == n - 1:
                            break
        if merged < n - 1:
            return False
    return True


class PermGroup:
    """Permutation group of degree n backed by exact Schreier-Sims BSGS
    (with deterministic Jordan prime-cycle certification for giant A_n / S_n).
    """

    def __init__(
        self,
        n: int,
        generators: Iterable[Perm],
        initial_base: Optional[Sequence[int]] = None,
        allow_jordan_fastpath: bool = True,
    ) -> None:
        self.n = n
        self.id_perm = identity_perm(n)
        raw_gens: List[Perm] = []
        seen_gens: Set[Perm] = set()
        for g in generators:
            if len(g) != n:
                raise ValueError(f"Generator length {len(g)} != degree {n}")
            if g != self.id_perm and g not in seen_gens:
                seen_gens.add(g)
                raw_gens.append(g)
        self.generators: Tuple[Perm, ...] = tuple(raw_gens)

        # Giant-group certified mode: None, "A_n", or "S_n"
        self._giant_kind: Optional[str] = None

        self.base: List[int] = []
        self.level_gens: List[List[Perm]] = []
        self.orbits_list: List[List[int]] = []
        self.trans: List[Dict[int, Perm]] = []
        self.trans_inv: List[Dict[int, Perm]] = []
        self._checked_pairs: List[Set[Tuple[int, int]]] = []

        if allow_jordan_fastpath and n >= 10 and len(raw_gens) >= 2:
            cert = self._try_certify_alt_or_sym(raw_gens)
            if cert is not None:
                self._giant_kind = cert
                return

        if initial_base:
            for b in initial_base:
                if 0 <= b < n and b not in self.base:
                    self._append_base_point(b)

        self._build_bsgs(raw_gens)

    def _try_certify_alt_or_sym(self, raw_gens: Sequence[Perm]) -> Optional[str]:
        """Deterministic Jordan prime-cycle certificate for A_n or S_n (n >= 10).

        Selects a small deterministic subset S_0 of `raw_gens` (size <= 6), generates
        deterministic words in S_0 to look for an element w whose cycle lengths contain
        a unique prime p <= n - 3 coprime to all other cycle lengths of w, constructs
        the single p-cycle z = w^M in <S_0>, explicitly verifies cycle_type(z) and
        primitivity of <S_0> on {0, ..., n-1}. By Jordan's Theorem (Wielandt, Thm 13.9),
        this rigorously proves <raw_gens> >= <S_0> >= A_n.
        """
        n = self.n
        rng = random.Random(323)
        # Pick up to 16 pseudo-randomly sampled generators deterministically (avoids coset-stride aliasing)
        m = len(raw_gens)
        if m <= 16:
            sub_gens = list(raw_gens)
        else:
            indices = sorted(rng.sample(range(m), 16))
            sub_gens = [raw_gens[idx] for idx in indices]

        orbs = compute_orbits(n, sub_gens)
        if len(orbs) != 1 or len(orbs[0]) != n:
            return None

        # Deterministic Product-Replacement walk in <sub_gens>
        bag = list(sub_gens)
        while len(bag) < 10:
            bag.append(sub_gens[len(bag) % len(sub_gens)])
        b_len = len(bag)

        found_prime_cycle = False
        for step in range(250):
            i1 = rng.randrange(b_len)
            i2 = rng.randrange(b_len - 1)
            if i2 >= i1:
                i2 += 1
            op_rhs = bag[i2] if (step & 3) != 0 else invert(bag[i2])
            acc = compose(bag[i1], op_rhs) if (step & 1) == 0 else compose(op_rhs, bag[i1])
            bag[i1] = acc
            if step < 8:
                continue

            cycs = cycle_lengths(acc)
            non_fixed = [c for c in cycs if c > 1]
            if not non_fixed:
                continue
            for idx_c, p in enumerate(non_fixed):
                if p <= n - 3 and _is_prime(p):
                    others = [c for j, c in enumerate(non_fixed) if j != idx_c]
                    if all(c % p != 0 for c in others):
                        lcm_others = 1
                        for c in others:
                            lcm_others = (lcm_others * c) // gcd(lcm_others, c)
                        z = perm_pow(acc, lcm_others)
                        expected_ct = (1,) * (n - p) + (p,)
                        if cycle_type(z) == expected_ct:
                            found_prime_cycle = True
                            sub_gens.append(z)
                            break
            if found_prime_cycle:
                break

        if not found_prime_cycle:
            return None

        # Certify primitivity of <sub_gens> across ALL points 1..n-1
        if not _atkinson_is_primitive_raw(n, sub_gens):
            return None

        # <raw_gens> >= <sub_gens> >= A_n is now 100% proved! Check parity of all raw_gens:
        for g in raw_gens:
            if perm_sign(g) == -1:
                return "S_n"
        return "A_n"

    def _append_base_point(self, b: int) -> int:
        idx = len(self.base)
        self.base.append(b)
        self.level_gens.append([])
        self.orbits_list.append([b])
        self.trans.append({b: self.id_perm})
        self.trans_inv.append({b: self.id_perm})
        self._checked_pairs.append(set())
        return idx

    def _extend_orbit_at_level(self, level: int, new_gen: Perm) -> None:
        """Extend Schreier tree at `level` without modifying existing transversal entries."""
        orb = self.orbits_list[level]
        if len(orb) == self.n:
            return
        tr = self.trans[level]
        tr_inv = self.trans_inv[level]
        gens = self.level_gens[level]

        q: deque[int] = deque()
        for pt in list(orb):
            img = new_gen[pt]
            if img not in tr:
                u_img = compose(new_gen, tr[pt])
                tr[img] = u_img
                tr_inv[img] = invert(u_img)
                orb.append(img)
                q.append(img)

        while q:
            pt = q.popleft()
            u_pt = tr[pt]
            for g in gens:
                img = g[pt]
                if img not in tr:
                    u_img = compose(g, u_pt)
                    tr[img] = u_img
                    tr_inv[img] = invert(u_img)
                    orb.append(img)
                    q.append(img)

    def _sift_from(self, g: Perm, start_level: int = 0) -> Tuple[int, Optional[Perm]]:
        """Sift g starting from `start_level` (assuming g fixes base[:start_level])."""
        h = g
        k = len(self.base)
        for i in range(start_level, k):
            pt = h[self.base[i]]
            tr_inv_i = self.trans_inv[i]
            if pt not in tr_inv_i:
                return i, h
            h = compose(tr_inv_i[pt], h)
        if h == self.id_perm:
            return k, None
        for pt in range(self.n):
            if h[pt] != pt:
                new_idx = self._append_base_point(pt)
                return new_idx, h
        return k, None

    def _add_strong_gen(self, max_level: int, h: Perm, min_level: int = 0) -> None:
        """Insert strong generator h into levels min_level..max_level."""
        for i in range(min_level, max_level + 1):
            self.level_gens[i].append(h)
            self._extend_orbit_at_level(i, h)

    def _build_bsgs(self, init_gens: Sequence[Perm]) -> None:
        for g in init_gens:
            lvl, res = self._sift_from(g, 0)
            if res is not None:
                self._add_strong_gen(lvl, res, min_level=0)

        i = len(self.base) - 1
        while i >= 0:
            orb = self.orbits_list[i]
            gens = self.level_gens[i]
            tr = self.trans[i]
            tr_inv = self.trans_inv[i]
            checked = self._checked_pairs[i]

            added_deeper = False
            p_idx = 0
            while p_idx < len(orb):
                pt = orb[p_idx]
                u_pt = tr[pt]
                g_idx = 0
                while g_idx < len(gens):
                    if (p_idx, g_idx) not in checked:
                        checked.add((p_idx, g_idx))
                        s = gens[g_idx]
                        img = s[pt]
                        schreier_gen = compose(tr_inv[img], compose(s, u_pt))
                        if schreier_gen != self.id_perm:
                            lvl, res = self._sift_from(schreier_gen, i + 1)
                            if res is not None:
                                self._add_strong_gen(lvl, res, min_level=i + 1)
                                i = lvl
                                added_deeper = True
                                break
                    g_idx += 1
                if added_deeper:
                    break
                p_idx += 1

            if not added_deeper:
                i -= 1

    def order(self) -> int:
        """Exact order |G|."""
        if self._giant_kind == "S_n":
            return math.factorial(self.n)
        if self._giant_kind == "A_n":
            return math.factorial(self.n) // 2
        prod = 1
        for orb in self.orbits_list:
            prod *= len(orb)
        return prod

    def stabilizer_order(self, pt: int = 0) -> int:
        """Exact order |G_pt| via Orbit-Stabilizer Theorem."""
        if self._giant_kind == "S_n":
            return math.factorial(self.n - 1)
        if self._giant_kind == "A_n":
            return math.factorial(self.n - 1) // 2
        for o in self.orbits():
            if pt in o:
                return self.order() // len(o)
        return self.order()

    def contains(self, g: Perm) -> bool:
        """Read-only membership test: whether permutation g belongs to G."""
        if len(g) != self.n:
            return False
        if self._giant_kind is not None:
            if set(g) != set(range(self.n)):
                return False
            if self._giant_kind == "S_n":
                return True
            return perm_sign(g) == 1
        h = g
        for i in range(len(self.base)):
            pt = h[self.base[i]]
            tr_inv_i = self.trans_inv[i]
            if pt not in tr_inv_i:
                return False
            h = compose(tr_inv_i[pt], h)
        return h == self.id_perm

    def orbits(self) -> List[List[int]]:
        """Orbits of G on {0, ..., n-1}."""
        if self._giant_kind is not None:
            return [list(range(self.n))]
        return compute_orbits(self.n, self.generators)

    def is_transitive(self) -> bool:
        if self.n <= 1 or self._giant_kind is not None:
            return True
        orbs = self.orbits()
        return len(orbs) == 1 and len(orbs[0]) == self.n

    def stabilizer_generators(self, pt: int = 0) -> List[Perm]:
        """Exact generating set for the point stabilizer G_pt."""
        if self._giant_kind is not None:
            pts = [i for i in range(self.n) if i != pt]
            m = len(pts)
            if self._giant_kind == "S_n":
                return [
                    cycles_to_perm(self.n, [[pts[0], pts[1]]]),
                    cycles_to_perm(self.n, [pts]),
                ]
            c3 = cycles_to_perm(self.n, [[pts[0], pts[1], pts[2]]])
            long_cyc = (
                cycles_to_perm(self.n, [pts])
                if m % 2 == 1
                else cycles_to_perm(self.n, [pts[1:]])
            )
            return [c3, long_cyc]

        if self.base and self.base[0] == pt:
            if len(self.base) >= 2:
                return list(self.level_gens[1])
            return []
        rebased = PermGroup(self.n, self.generators, initial_base=[pt])
        return rebased.stabilizer_generators(pt)

    def stabilizer(self, pt: int = 0) -> "PermGroup":
        """Return the point stabilizer subgroup G_pt as a PermGroup."""
        gens = self.stabilizer_generators(pt)
        return PermGroup(self.n, gens)

    def stabilizer_orbits(self, pt: int = 0) -> List[List[int]]:
        """Orbits of G_pt on {0, ..., n-1}."""
        if self._giant_kind is not None:
            other = [i for i in range(self.n) if i != pt]
            return sorted([[pt], other], key=lambda x: x[0])
        gens = self.stabilizer_generators(pt)
        return compute_orbits(self.n, gens)

    def rank(self, pt: int = 0) -> int:
        """Permutation rank: number of orbits of point stabilizer G_pt on {0, ..., n-1}."""
        if self._giant_kind is not None:
            return 2
        return len(self.stabilizer_orbits(pt))

    def subdegrees(self, pt: int = 0) -> Tuple[int, ...]:
        """Sorted orbit sizes of point stabilizer G_pt on {0, ..., n-1}."""
        if self._giant_kind is not None:
            return (1, self.n - 1)
        return tuple(sorted(len(o) for o in self.stabilizer_orbits(pt)))

    def minimal_block_equivalence(self, a: int, b: int = 0) -> List[int]:
        """Atkinson's algorithm: smallest G-invariant equivalence relation with a ~ b."""
        if self._giant_kind is not None:
            if a == b:
                return list(range(self.n))
            return [0] * self.n

        parent = list(range(self.n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        if a == b:
            return parent

        ra, rb = find(a), find(b)
        if ra > rb:
            ra, rb = rb, ra
        parent[rb] = ra
        q: deque[Tuple[int, int]] = deque([(a, b)])

        ops = self.level_gens[0] if self.level_gens else self.generators
        while q:
            u, v = q.popleft()
            for g in ops:
                gu, gv = g[u], g[v]
                ru, rv = find(gu), find(gv)
                if ru != rv:
                    if ru > rv:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    q.append((gu, gv))

        return [find(i) for i in range(self.n)]

    def minimal_block_containing(self, a: int, b: int = 0) -> Tuple[int, ...]:
        """Return sorted tuple of the block containing `b` in the minimal block system with a ~ b."""
        roots = self.minimal_block_equivalence(a, b)
        rb = roots[b]
        return tuple(i for i, r in enumerate(roots) if r == rb)

    def is_primitive(self) -> bool:
        """Exact primitivity test on {0, ..., n-1}."""
        if self.n < 2:
            return False
        if self._giant_kind is not None:
            return True
        if not self.is_transitive():
            return False
        for orb in self.stabilizer_orbits(0):
            a = orb[0]
            if a == 0:
                continue
            blk = self.minimal_block_containing(a, 0)
            if 1 < len(blk) < self.n:
                return False
        return True

    def enumerate_elements(self, limit: int = 100000) -> List[Perm]:
        """Enumerate all elements of G via BSGS coset product (raises ValueError if |G| > limit)."""
        ord_g = self.order()
        if ord_g > limit:
            raise ValueError(f"Group order {ord_g} exceeds enumeration limit {limit}")
        if self._giant_kind is not None:
            # Rebuild explicit BSGS since ord_g <= limit implies n <= 8 anyway
            explicit = PermGroup(self.n, self.generators, allow_jordan_fastpath=False)
            return explicit.enumerate_elements(limit=limit)
        elems: List[Perm] = [self.id_perm]
        for i in range(len(self.base) - 1, -1, -1):
            orb = self.orbits_list[i]
            tr = self.trans[i]
            next_elems: List[Perm] = []
            for pt in orb:
                u = tr[pt]
                for e in elems:
                    next_elems.append(compose(u, e))
            elems = next_elems
        return elems

    def derived_subgroup(self) -> "PermGroup":
        """Exact commutator subgroup [G, G] via normal closure of strong-generator commutators."""
        if self._giant_kind is not None:
            if self._giant_kind == "A_n":
                return self
            c3 = cycles_to_perm(self.n, [[0, 1, 2]])
            rest = (
                cycles_to_perm(self.n, [list(range(self.n))])
                if self.n % 2 == 1
                else cycles_to_perm(self.n, [list(range(1, self.n))])
            )
            return PermGroup(self.n, [c3, rest], allow_jordan_fastpath=True)

        if not self.level_gens:
            return PermGroup(self.n, [], allow_jordan_fastpath=False)

        s_gens = list(dict.fromkeys(self.level_gens[0]))
        s_invs = [invert(g) for g in s_gens]
        comms: List[Perm] = []
        seen_c: Set[Perm] = {self.id_perm}
        k = len(s_gens)
        for i in range(k):
            gi, gii = s_gens[i], s_invs[i]
            for j in range(i + 1, k):
                gj, gji = s_gens[j], s_invs[j]
                cm = compose(gi, compose(gj, compose(gii, gji)))
                if cm not in seen_c:
                    seen_c.add(cm)
                    comms.append(cm)

        if not comms:
            return PermGroup(self.n, [], allow_jordan_fastpath=False)

        conj_pairs = list(zip(s_gens, s_invs)) + list(zip(s_invs, s_gens))
        H = PermGroup(self.n, comms, allow_jordan_fastpath=False)
        while True:
            h_strong = list(dict.fromkeys(H.level_gens[0])) if H.level_gens else []
            extra: List[Perm] = []
            for h in h_strong:
                for s, si in conj_pairs:
                    c = compose(s, compose(h, si))
                    if not H.contains(c):
                        extra.append(c)
                        if len(extra) >= 8:
                            break
                if len(extra) >= 8:
                    break
            if not extra:
                break
            H = PermGroup(self.n, list(H.generators) + extra, allow_jordan_fastpath=False)
        return H

    def derived_series_orders(self) -> Tuple[int, ...]:
        """Return tuple of orders (|G|, |G'|, |G''|, ...) down to 1 or the perfect residual."""
        if self._giant_kind == "S_n":
            return (math.factorial(self.n), math.factorial(self.n) // 2)
        if self._giant_kind == "A_n":
            return (math.factorial(self.n) // 2,)
        orders: List[int] = [self.order()]
        cur = self
        while orders[-1] > 1:
            nxt = cur.derived_subgroup()
            nxt_ord = nxt.order()
            if nxt_ord == orders[-1]:
                break
            orders.append(nxt_ord)
            cur = nxt
        return tuple(orders)

    def is_solvable(self) -> bool:
        """Exact solvability test: whether the derived series of G terminates at {1}."""
        if self._giant_kind is not None:
            return False
        return self.derived_series_orders()[-1] == 1
