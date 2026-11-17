"""Exact computational laboratory for finite Bol loops and Bol loop folders.

Conventions match `problems/0323-finite-simple-non-moufang-bol-loops/PROBLEM.md`:
  - Elements of a finite loop Q of order n are indexed {0, 1, ..., n - 1} with identity 0.
  - Left Bol identity:   x * (y * (x * z)) = (x * (y * x)) * z   for all x, y, z in Q.
  - Right Bol identity:  ((z * x) * y) * x = z * ((x * y) * x)   for all x, y, z in Q.
  - Moufang identity:    (x * y) * (z * x) = (x * (y * z)) * x   for all x, y, z in Q.
  - Proper left Bol:     left Bol and NOT Moufang (with explicit witness triple (x, y, z)).
  - Opposite loop Q^op:  x *_op y = y * x (converts right Bol <-> left Bol).
"""

from __future__ import annotations

from collections import Counter, defaultdict, deque
import ctypes
from dataclasses import dataclass
from math import gcd
import os
import shutil
import subprocess
import tempfile
from typing import Any, Dict, Iterable, List, Optional, Sequence, Set, Tuple

from perm_group import (
    Perm,
    PermGroup,
    _atkinson_is_primitive_raw,
    compose,
    cycle_type,
    identity_perm,
    invert,
)


def _lcm(a: int, b: int) -> int:
    return (a * b) // gcd(a, b)


_C_ACCEL_LIB: Any = None
_C_ACCEL_TRIED: bool = False

_C_ACCEL_SRC = r"""
#include <stddef.h>
#include <stdint.h>

int check_left_bol_c(const int32_t *tbl, int n, int32_t *wit) {
    for (int x = 0; x < n; ++x) {
        const int32_t *Lx = tbl + (size_t)x * n;
        for (int y = 0; y < n; ++y) {
            const int32_t *Ly = tbl + (size_t)y * n;
            int w = Lx[Ly[x]];
            const int32_t *Lw = tbl + (size_t)w * n;
            for (int z = 0; z < n; ++z) {
                if (Lx[Ly[Lx[z]]] != Lw[z]) {
                    wit[0] = x; wit[1] = y; wit[2] = z;
                    return 0;
                }
            }
        }
    }
    return 1;
}

int check_moufang_c(const int32_t *tbl, int n, int32_t *wit) {
    for (int x = 0; x < n; ++x) {
        const int32_t *Lx = tbl + (size_t)x * n;
        for (int z = 0; z < n; ++z) {
            int zx = tbl[(size_t)z * n + x];
            for (int y = 0; y < n; ++y) {
                int lhs = tbl[(size_t)Lx[y] * n + zx];
                int rhs = tbl[(size_t)Lx[tbl[(size_t)y * n + z]] * n + x];
                if (lhs != rhs) {
                    wit[0] = x; wit[1] = y; wit[2] = z;
                    return 0;
                }
            }
        }
    }
    return 1;
}
"""


def _get_c_accel() -> Any:
    """Optionally compile a tiny C helper in $TMPDIR for O(n^3) Bol checks at large n.
    Falls back cleanly to None (100% pure Python) if no C compiler is available.
    Never writes inside the repository workspace.
    """
    global _C_ACCEL_LIB, _C_ACCEL_TRIED
    if _C_ACCEL_TRIED:
        return _C_ACCEL_LIB
    _C_ACCEL_TRIED = True
    cc = shutil.which("clang") or shutil.which("cc") or shutil.which("gcc")
    if not cc:
        return None
    try:
        import sys as _sys

        tmpdir = tempfile.gettempdir()
        pid = os.getpid()
        ext = "dylib" if _sys.platform == "darwin" else "so"
        c_path = os.path.join(tmpdir, f"bol_accel_0323_{pid}.c")
        so_path = os.path.join(tmpdir, f"bol_accel_0323_{pid}.{ext}")
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(_C_ACCEL_SRC)
        flags = ["-O3", "-dynamiclib"] if _sys.platform == "darwin" else ["-O3", "-shared", "-fPIC"]
        subprocess.run(
            [cc, *flags, c_path, "-o", so_path],
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        lib = ctypes.CDLL(so_path)
        for p_tmp in (c_path, so_path):
            try:
                os.unlink(p_tmp)
            except OSError:
                pass
        lib.check_left_bol_c.argtypes = [
            ctypes.POINTER(ctypes.c_int32),
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_int32),
        ]
        lib.check_left_bol_c.restype = ctypes.c_int
        lib.check_moufang_c.argtypes = [
            ctypes.POINTER(ctypes.c_int32),
            ctypes.c_int,
            ctypes.POINTER(ctypes.c_int32),
        ]
        lib.check_moufang_c.restype = ctypes.c_int
        _C_ACCEL_LIB = lib
    except Exception:
        _C_ACCEL_LIB = None
    return _C_ACCEL_LIB


class Loop:
    """Finite loop (or candidate multiplication table) on {0, ..., n - 1} with identity 0."""

    def __init__(
        self,
        table: Sequence[Sequence[int]],
        name: str = "unnamed_loop",
        validate_loop: bool = True,
    ) -> None:
        self.name = name
        self.n = len(table)
        if self.n == 0:
            raise ValueError("Loop order must be >= 1")
        self.table: Tuple[Tuple[int, ...], ...] = tuple(tuple(int(v) for v in row) for row in table)
        for row in self.table:
            if len(row) != self.n:
                raise ValueError("Multiplication table must be square")

        # Left and right translation tuples: L[x][y] = x * y, R[x][y] = y * x
        self.L: Tuple[Perm, ...] = self.table
        self.R: Tuple[Perm, ...] = tuple(
            tuple(self.table[y][x] for y in range(self.n)) for x in range(self.n)
        )

        self.is_valid_loop, self.loop_error = self._validate_loop_axioms()
        if validate_loop and not self.is_valid_loop:
            raise ValueError(f"Invalid loop '{name}': {self.loop_error}")

        if self.is_valid_loop:
            self.L_inv: Tuple[Perm, ...] = tuple(invert(lx) for lx in self.L)
            self.R_inv: Tuple[Perm, ...] = tuple(invert(rx) for rx in self.R)
        else:
            self.L_inv = ()
            self.R_inv = ()

        self._lmlt: Optional[PermGroup] = None
        self._rmlt: Optional[PermGroup] = None
        self._mlt: Optional[PermGroup] = None

    def _validate_loop_axioms(self) -> Tuple[bool, str]:
        n = self.n
        for x in range(n):
            if self.table[0][x] != x:
                return False, f"0 is not left identity at x={x}: 0*{x}={self.table[0][x]}"
            if self.table[x][0] != x:
                return False, f"0 is not right identity at x={x}: {x}*0={self.table[x][0]}"
        full_set = set(range(n))
        for x in range(n):
            row = self.L[x]
            if any(v < 0 or v >= n for v in row) or len(set(row)) != n or set(row) != full_set:
                return False, f"Row L_{x} is not a permutation of 0..{n-1}"
            col = self.R[x]
            if len(set(col)) != n:
                return False, f"Column R_{x} is not a permutation of 0..{n-1}"
        return True, ""

    def mul(self, x: int, y: int) -> int:
        return self.table[x][y]

    def left_div(self, x: int, y: int) -> int:
        """Unique z such that x * z = y."""
        return self.L_inv[x][y]

    def right_div(self, x: int, y: int) -> int:
        """Unique z such that z * y = x."""
        return self.R_inv[y][x]

    def opposite(self, name: Optional[str] = None) -> "Loop":
        """Opposite loop Q^op with x *_op y = y * x."""
        op_name = name if name is not None else f"{self.name}^op"
        return Loop(self.R, name=op_name, validate_loop=self.is_valid_loop)

    # ------------------------------------------------------------------
    # Algebraic Identities
    # ------------------------------------------------------------------

    def check_left_bol(self) -> Tuple[bool, Optional[Tuple[int, int, int]]]:
        """Check x * (y * (x * z)) == (x * (y * x)) * z for all x, y, z."""
        n = self.n
        if n >= 120:
            lib = _get_c_accel()
            if lib is not None:
                flat = (ctypes.c_int32 * (n * n))(*[v for row in self.table for v in row])
                wit = (ctypes.c_int32 * 3)(0, 0, 0)
                ok = lib.check_left_bol_c(flat, n, wit)
                if ok == 1:
                    return True, None
                return False, (int(wit[0]), int(wit[1]), int(wit[2]))

        L = self.L
        tbl = self.table
        for x in range(n):
            Lx = L[x]
            row_x = tbl[x]
            for y in range(n):
                Ly = L[y]
                lhs_perm = tuple(Lx[Ly[v]] for v in Lx)
                rhs_perm = L[row_x[Ly[x]]]
                if lhs_perm != rhs_perm:
                    for z in range(n):
                        if lhs_perm[z] != rhs_perm[z]:
                            return False, (x, y, z)
        return True, None

    def check_right_bol(self) -> Tuple[bool, Optional[Tuple[int, int, int]]]:
        """Check ((z * x) * y) * x == z * ((x * y) * x) for all x, y, z.

        If false, returns (False, (x, y, z)) failing ((z * x) * y) * x == z * ((x * y) * x).
        """
        R = self.R
        tbl = self.table
        n = self.n
        for x in range(n):
            Rx = R[x]
            for y in range(n):
                lhs_perm = compose(Rx, compose(R[y], Rx))
                rhs_perm = R[tbl[tbl[x][y]][x]]
                if lhs_perm != rhs_perm:
                    for z in range(n):
                        if lhs_perm[z] != rhs_perm[z]:
                            return False, (x, y, z)
        return True, None

    def check_moufang(self) -> Tuple[bool, Optional[Tuple[int, int, int]]]:
        """Check (x * y) * (z * x) == (x * (y * z)) * x for all x, y, z.

        Returns (True, None) or (False, (x, y, z)) with an explicit witness triple!
        """
        n = self.n
        if n >= 120:
            lib = _get_c_accel()
            if lib is not None:
                flat = (ctypes.c_int32 * (n * n))(*[v for row in self.table for v in row])
                wit = (ctypes.c_int32 * 3)(0, 0, 0)
                ok = lib.check_moufang_c(flat, n, wit)
                if ok == 1:
                    return True, None
                return False, (int(wit[0]), int(wit[1]), int(wit[2]))

        L = self.L
        R = self.R
        tbl = self.table
        for x in range(n):
            Lx = L[x]
            Rx = R[x]
            for z in range(n):
                zx = tbl[z][x]
                # As a function of y:
                # LHS(y) = (x * y) * (z * x) = R_{z*x}(L_x(y))
                # RHS(y) = (x * (y * z)) * x = R_x(L_x(R_z(y)))
                lhs_perm = compose(R[zx], Lx)
                rhs_perm = compose(Rx, compose(Lx, R[z]))
                if lhs_perm != rhs_perm:
                    for y in range(n):
                        if lhs_perm[y] != rhs_perm[y]:
                            return False, (x, y, z)
        return True, None

    def check_associative(self) -> Tuple[bool, Optional[Tuple[int, int, int]]]:
        """Check (x * y) * z == x * (y * z) for all x, y, z."""
        L = self.L
        tbl = self.table
        n = self.n
        for x in range(n):
            Lx = L[x]
            row_x = tbl[x]
            for y in range(n):
                lhs_perm = L[row_x[y]]
                rhs_perm = compose(Lx, L[y])
                if lhs_perm != rhs_perm:
                    for z in range(n):
                        if lhs_perm[z] != rhs_perm[z]:
                            return False, (x, y, z)
        return True, None

    # ------------------------------------------------------------------
    # Multiplication Groups & Ranks
    # ------------------------------------------------------------------

    def LMlt(self) -> PermGroup:
        if self._lmlt is None:
            self._lmlt = PermGroup(self.n, self.L, initial_base=[0])
        return self._lmlt

    def RMlt(self) -> PermGroup:
        if self._rmlt is None:
            self._rmlt = PermGroup(self.n, self.R, initial_base=[0])
        return self._rmlt

    def Mlt(self) -> PermGroup:
        if self._mlt is None:
            self._mlt = PermGroup(self.n, list(self.L) + list(self.R), initial_base=[0])
        return self._mlt

    # ------------------------------------------------------------------
    # Exact Normal Subloop & Loop Congruence Tests
    # ------------------------------------------------------------------

    def minimal_congruence_roots(self, a: int) -> List[int]:
        """Compute smallest loop congruence with a ~ 0 directly from L_x, R_x, L_x^-1, R_x^-1
        (100% independent of PermGroup).

        Uses a two-stage exact closure: first propagates under a small subset of {L_x, R_x};
        if that already merges all n elements into a single class, the full closure is provably Q.
        Otherwise closes to fixed point under all 4n translation/division maps.
        """
        n = self.n
        parent = list(range(n))

        def find(x: int) -> int:
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        if a == 0:
            return parent

        parent[a] = 0
        merged = 1

        if n - 1 <= 24:
            idxs = list(range(1, n))
        else:
            import random as _rnd

            idxs = sorted(_rnd.Random(323).sample(range(1, n), 24))
        fast_ops: List[Perm] = []
        for idx in idxs:
            fast_ops.append(self.L[idx])
            fast_ops.append(self.R[idx])

        q_fast: deque[Tuple[int, int]] = deque([(0, a)])
        history: List[Tuple[int, int]] = [(0, a)]
        while q_fast and merged < n - 1:
            u, v = q_fast.popleft()
            for op in fast_ops:
                gu, gv = op[u], op[v]
                ru, rv = find(gu), find(gv)
                if ru != rv:
                    if ru > rv:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    merged += 1
                    q_fast.append((gu, gv))
                    history.append((gu, gv))
                    if merged == n - 1:
                        break

        if merged == n - 1:
            return [0] * n

        all_ops: Sequence[Perm] = (
            list(self.L) + list(self.R) + list(self.L_inv) + list(self.R_inv)
        )
        q_full: deque[Tuple[int, int]] = deque(history)
        while q_full and merged < n - 1:
            u, v = q_full.popleft()
            for op in all_ops:
                gu, gv = op[u], op[v]
                ru, rv = find(gu), find(gv)
                if ru != rv:
                    if ru > rv:
                        ru, rv = rv, ru
                    parent[rv] = ru
                    merged += 1
                    q_full.append((gu, gv))
                    if merged == n - 1:
                        break

        return [find(i) for i in range(n)]

    def verify_is_loop_congruence(self, roots: Sequence[int]) -> bool:
        """Directly verify that equivalence relation `roots` is a valid loop congruence
        (compatible with *, left_div, right_div) and that [0] satisfies Bruck's normal subloop laws.
        """
        n = self.n
        classes: Dict[int, List[int]] = defaultdict(list)
        for i, r in enumerate(roots):
            classes[r].append(i)

        # Check every row/col of *, \, / maps classes consistently
        for r1, cls1 in classes.items():
            u0 = cls1[0]
            for r2, cls2 in classes.items():
                v0 = cls2[0]
                target_mul = roots[self.table[u0][v0]]
                target_ldiv = roots[self.L_inv[u0][v0]]
                target_rdiv = roots[self.R_inv[v0][u0]]
                for u in cls1:
                    for v in cls2:
                        if roots[self.table[u][v]] != target_mul:
                            return False
                        if roots[self.L_inv[u][v]] != target_ldiv:
                            return False
                        if roots[self.R_inv[v][u]] != target_rdiv:
                            return False
        return True

    def check_simplicity(self) -> Tuple[bool, List[int]]:
        """Run BOTH exact simplicity tests across ALL elements a != 0 and assert agreement:
          (a) Direct normal-subloop / loop-congruence closure on ALL a in {1, ..., n - 1}.
          (b) Primitivity of full multiplication group Mlt(Q) on Q.

        Returns (is_simple, sorted_proper_normal_subloop_sizes).
        """
        if self.n < 2:
            return False, []

        if self._mlt is not None or self.n <= 250:
            is_mlt_prim = self.Mlt().is_primitive()
        else:
            is_mlt_prim = _atkinson_is_primitive_raw(
                self.n, list(self.L[1:]) + list(self.R[1:])
            )
            if is_mlt_prim:
                is_mlt_prim = self.Mlt().is_primitive()

        proper_sizes: Set[int] = set()
        for a in range(1, self.n):
            roots = self.minimal_congruence_roots(a)
            r0 = roots[0]
            blk_size = sum(1 for r in roots if r == r0)
            if 1 < blk_size < self.n:
                if self.n <= 300:
                    assert self.verify_is_loop_congruence(roots), (
                        f"Generated equivalence relation for a={a} failed loop congruence verification!"
                    )
                proper_sizes.add(blk_size)

        is_simple_cong = len(proper_sizes) == 0
        if is_simple_cong != is_mlt_prim:
            raise AssertionError(
                f"Simplicity mismatch on {self.name}: congruence={is_simple_cong}, Mlt_primitive={is_mlt_prim}"
            )
        return is_simple_cong, sorted(proper_sizes)

    # ------------------------------------------------------------------
    # Nuclei, Center, Element Orders, Inverse & Automorphic Properties
    # ------------------------------------------------------------------

    def left_nucleus(self) -> Tuple[int, ...]:
        """N_lambda = {a in Q : (a * x) * y == a * (x * y) for all x, y}."""
        tbl = self.table
        n = self.n
        res: List[int] = []
        for a in range(n):
            row_a = tbl[a]
            ok = True
            for x in range(n):
                row_ax = tbl[row_a[x]]
                row_x = tbl[x]
                for y in range(n):
                    if row_ax[y] != row_a[row_x[y]]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                res.append(a)
        return tuple(res)

    def middle_nucleus(self) -> Tuple[int, ...]:
        """N_mu = {a in Q : (x * a) * y == x * (a * y) for all x, y}."""
        tbl = self.table
        n = self.n
        res: List[int] = []
        for a in range(n):
            row_a = tbl[a]
            ok = True
            for x in range(n):
                row_x = tbl[x]
                row_xa = tbl[row_x[a]]
                for y in range(n):
                    if row_xa[y] != row_x[row_a[y]]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                res.append(a)
        return tuple(res)

    def right_nucleus(self) -> Tuple[int, ...]:
        """N_rho = {a in Q : (x * y) * a == x * (y * a) for all x, y}."""
        tbl = self.table
        R = self.R
        n = self.n
        res: List[int] = []
        for a in range(n):
            Ra = R[a]
            ok = True
            for x in range(n):
                row_x = tbl[x]
                for y in range(n):
                    if Ra[row_x[y]] != row_x[Ra[y]]:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                res.append(a)
        return tuple(res)

    def commutant(self) -> Tuple[int, ...]:
        """C(Q) = {a in Q : a * x == x * a for all x}."""
        return tuple(a for a in range(self.n) if self.L[a] == self.R[a])

    def center(self) -> Tuple[int, ...]:
        nl = set(self.left_nucleus())
        nm = set(self.middle_nucleus())
        nr = set(self.right_nucleus())
        cm = set(self.commutant())
        return tuple(sorted(nl & nm & nr & cm))

    def power_associativity_and_orders(self) -> Tuple[bool, Optional[Tuple[int, ...]], int]:
        """Check power-associativity (each 1-generated subloop is cyclic) and return
        (is_power_associative, element_orders_tuple, exponent).
        """
        orders: List[int] = [1]
        exp_val = 1
        tbl = self.table
        for x in range(1, self.n):
            pows = [0]
            seen = {0: 0}
            cur = x
            while cur not in seen:
                seen[cur] = len(pows)
                pows.append(cur)
                cur = tbl[x][cur]
            if cur != 0:
                return False, None, 0
            m = len(pows)
            # Verify pows[i] * pows[j] == pows[(i + j) % m] for all i, j
            for i in range(m):
                pi = pows[i]
                for j in range(m):
                    if tbl[pi][pows[j]] != pows[(i + j) % m]:
                        return False, None, 0
            orders.append(m)
            exp_val = _lcm(exp_val, m)
        return True, tuple(orders), exp_val

    def inverse_properties(self) -> Dict[str, bool]:
        """Check two-sided inverses, LIP, RIP, AIP (Bruck when left Bol), AAIP."""
        left_invs = [self.R_inv[x][0] for x in range(self.n)]   # z * x = 0
        right_invs = [self.L_inv[x][0] for x in range(self.n)]  # x * z = 0
        two_sided = left_invs == right_invs
        if not two_sided:
            return {
                "has_two_sided_inverses": False,
                "has_LIP": False,
                "has_RIP": False,
                "has_AIP": False,
                "has_AAIP": False,
            }
        inv_map = right_invs
        has_lip = all(self.L[inv_map[x]] == self.L_inv[x] for x in range(self.n))
        has_rip = all(self.R[inv_map[x]] == self.R_inv[x] for x in range(self.n))
        has_aip = all(
            inv_map[self.table[x][y]] == self.table[inv_map[x]][inv_map[y]]
            for x in range(self.n)
            for y in range(self.n)
        )
        has_aaip = all(
            inv_map[self.table[x][y]] == self.table[inv_map[y]][inv_map[x]]
            for x in range(self.n)
            for y in range(self.n)
        )
        return {
            "has_two_sided_inverses": True,
            "has_LIP": has_lip,
            "has_RIP": has_rip,
            "has_AIP": has_aip,
            "has_AAIP": has_aaip,
        }

    def is_automorphism(self, p: Perm) -> bool:
        """Check whether permutation p of Q is a loop automorphism."""
        if p[0] != 0:
            return False
        tbl = self.table
        n = self.n
        for x in range(n):
            px = p[x]
            row_x = tbl[x]
            row_px = tbl[px]
            for y in range(n):
                if p[row_x[y]] != row_px[p[y]]:
                    return False
        return True

    def automorphisms(self) -> List[Perm]:
        """Return all loop automorphisms of Q (verified on all n^2 Cayley entries)."""
        return loop_automorphisms(self)

    def automorphism_group(self) -> PermGroup:
        """Return Aut(Q) as an exact PermGroup on {0, ..., n-1}."""
        return PermGroup(self.n, self.automorphisms(), allow_jordan_fastpath=False)

    def automorphism_group_order(self) -> int:
        """Return exact order |Aut(Q)|."""
        return len(self.automorphisms())

    def analyze(self, check_op_iso: bool = True, compute_aut: bool = False) -> Dict[str, Any]:
        """Compute full certified structural report for Q."""
        is_lbol, lbol_wit = self.check_left_bol()
        is_rbol, rbol_wit = self.check_right_bol()
        is_mouf, mouf_wit = self.check_moufang()
        is_assoc, assoc_wit = self.check_associative()
        is_simple, normal_sizes = self.check_simplicity()

        lmlt = self.LMlt()
        rmlt = self.RMlt()
        mlt = self.Mlt()

        nl = self.left_nucleus()
        nm = self.middle_nucleus()
        nr = self.right_nucleus()
        cm = self.commutant()
        zn = self.center()

        is_pa, elem_orders, exp_val = self.power_associativity_and_orders()
        order_spec = dict(sorted(Counter(elem_orders).items())) if elem_orders is not None else {}
        inv_props = self.inverse_properties()

        linn_gens = lmlt.stabilizer_generators(0)
        inn_gens = mlt.stabilizer_generators(0)
        is_l_auto = all(self.is_automorphism(g) for g in linn_gens)
        is_full_auto = is_l_auto and all(self.is_automorphism(g) for g in inn_gens)

        # Proper left Bol => never right Bol => never isomorphic to Q^op;
        # we also verify directly via isomorphism test when requested and n <= 250.
        if check_op_iso and self.n <= 250:
            iso_to_op = are_loops_isomorphic(self, self.opposite())
        else:
            iso_to_op = is_rbol if is_lbol else None

        report: Dict[str, Any] = {
            "name": self.name,
            "order": self.n,
            "is_loop": self.is_valid_loop,
            "is_left_bol": is_lbol,
            "left_bol_witness": lbol_wit,
            "is_right_bol": is_rbol,
            "right_bol_witness": rbol_wit,
            "is_moufang": is_mouf,
            "non_moufang_witness": mouf_wit,
            "is_associative": is_assoc,
            "non_associative_witness": assoc_wit,
            "is_proper_left_bol": is_lbol and (not is_mouf),
            "is_simple": is_simple,
            "proper_normal_subloop_sizes": normal_sizes,
            "LMlt_order": lmlt.order(),
            "LInn_order": lmlt.stabilizer_order(0),
            "LMlt_rank": lmlt.rank(0),
            "LMlt_subdegrees": lmlt.subdegrees(0),
            "is_LMlt_primitive": lmlt.is_primitive(),
            "is_LMlt_solvable": lmlt.is_solvable(),
            "RMlt_order": rmlt.order(),
            "RInn_order": rmlt.stabilizer_order(0),
            "RMlt_rank": rmlt.rank(0),
            "RMlt_subdegrees": rmlt.subdegrees(0),
            "is_RMlt_primitive": rmlt.is_primitive(),
            "Mlt_order": mlt.order(),
            "Inn_order": mlt.stabilizer_order(0),
            "Mlt_rank": mlt.rank(0),
            "Mlt_subdegrees": mlt.subdegrees(0),
            "is_Mlt_primitive": mlt.is_primitive(),
            "N_lambda_size": len(nl),
            "N_mu_size": len(nm),
            "N_rho_size": len(nr),
            "commutant_size": len(cm),
            "center_size": len(zn),
            "is_power_associative": is_pa,
            "exponent": exp_val,
            "order_spectrum": order_spec,
            **inv_props,
            "is_left_bruck": is_lbol and inv_props["has_AIP"],
            "is_left_automorphic": is_l_auto,
            "is_automorphic": is_full_auto,
            "is_isomorphic_to_opposite": iso_to_op,
        }
        if compute_aut:
            report["Aut_order"] = self.automorphism_group_order()
        return report


# ======================================================================
# Exact Loop Isomorphism & Deduplication
# ======================================================================


def element_profiles(loop: Loop) -> List[Tuple[Any, ...]]:
    """Compute isomorphism-invariant structural profile for every x in Q."""
    n = loop.n
    tbl = loop.table
    sq_counts = [0] * n
    for y in range(n):
        sq_counts[tbl[y][y]] += 1

    profiles: List[Tuple[Any, ...]] = []
    for x in range(n):
        ct_l = cycle_type(loop.L[x])
        ct_r = cycle_type(loop.R[x])
        ct_t = cycle_type(compose(loop.L_inv[x], loop.R[x]))
        x2 = tbl[x][x]
        ct_lx2 = cycle_type(loop.L[x2])
        eq_lr = 1 if loop.L[x] == loop.R[x] else 0
        profiles.append((x == 0, ct_l, ct_r, ct_t, ct_lx2, sq_counts[x], eq_lr))
    return profiles


def loop_fingerprint(loop: Loop) -> Tuple[Any, ...]:
    """Fast isomorphism invariant fingerprint of `loop`."""
    profs = element_profiles(loop)
    return (loop.n, tuple(sorted(profs)))


def _greedy_generating_plan(
    loop: Loop, profs: Sequence[Tuple[Any, ...]]
) -> Tuple[List[int], List[Tuple[int, int, int]]]:
    """Select small generating tuple [g_1, ..., g_d] of `loop` and straight-line
    multiplication steps [(u, v, w = u * v), ...] generating all reachable elements.
    """
    n = loop.n
    tbl = loop.table
    freq = Counter(profs)

    generated = [False] * n
    generated[0] = True
    gen_list: List[int] = [0]
    chosen_gens: List[int] = []
    steps: List[Tuple[int, int, int]] = []

    def close_subloop(new_elem: int) -> None:
        generated[new_elem] = True
        q = deque([new_elem])
        gen_list.append(new_elem)
        while q:
            a = q.popleft()
            for b in list(gen_list):
                ab = tbl[a][b]
                if not generated[ab]:
                    generated[ab] = True
                    gen_list.append(ab)
                    steps.append((a, b, ab))
                    q.append(ab)
                ba = tbl[b][a]
                if not generated[ba]:
                    generated[ba] = True
                    gen_list.append(ba)
                    steps.append((b, a, ba))
                    q.append(ba)

    while len(gen_list) < n:
        # Pick ungenerated element from smallest profile class (tie-break: largest closure growth)
        candidates = [x for x in range(1, n) if not generated[x]]
        min_f = min(freq[profs[x]] for x in candidates)
        best_cands = [x for x in candidates if freq[profs[x]] == min_f]
        chosen = best_cands[0]
        chosen_gens.append(chosen)
        close_subloop(chosen)

    return chosen_gens, steps


def find_all_loop_isomorphisms(
    q1: Loop, q2: Loop, limit: Optional[int] = None
) -> List[Perm]:
    """Return all explicit loop isomorphisms phi: Q1 -> Q2 (or up to `limit` if set)."""
    if q1.n != q2.n:
        return []
    n = q1.n
    if n == 1:
        return [(0,)]

    profs1 = element_profiles(q1)
    profs2 = element_profiles(q2)
    if sorted(profs1) != sorted(profs2):
        return []

    by_prof2: Dict[Tuple[Any, ...], List[int]] = defaultdict(list)
    for y, p in enumerate(profs2):
        by_prof2[p].append(y)

    gens1, steps1 = _greedy_generating_plan(q1, profs1)
    # Partition steps1 by which generator index unlocked them:
    # Rebuild incremental plan per generator depth so mismatches prune immediately!
    known = [False] * n
    known[0] = True
    known_elems = [0]
    depth_steps: List[List[Tuple[int, int, int]]] = []
    step_ptr = 0
    for g in gens1:
        known[g] = True
        known_elems.append(g)
        cur_steps: List[Tuple[int, int, int]] = []
        while step_ptr < len(steps1):
            u, v, w = steps1[step_ptr]
            if known[u] and known[v]:
                known[w] = True
                known_elems.append(w)
                cur_steps.append((u, v, w))
                step_ptr += 1
            else:
                break
        depth_steps.append(cur_steps)

    # Also group local compatibility checks among already-assigned elements at each depth
    depth_elems: List[Tuple[List[int], List[int]]] = []
    seen_tmp = {0}
    for d, g in enumerate(gens1):
        new_batch = [g] + [w for _, _, w in depth_steps[d]]
        depth_elems.append((list(seen_tmp), new_batch))
        seen_tmp.update(new_batch)

    tbl1 = q1.table
    tbl2 = q2.table
    phi = [-1] * n
    used2 = [False] * n
    phi[0] = 0
    used2[0] = True
    results: List[Perm] = []

    def backtrack(d: int) -> bool:
        if d == len(gens1):
            # Final complete check (all n^2 pairs verified)
            for x in range(n):
                px = phi[x]
                r1 = tbl1[x]
                r2 = tbl2[px]
                for y in range(n):
                    if phi[r1[y]] != r2[phi[y]]:
                        return False
            results.append(tuple(phi))
            return limit is not None and len(results) >= limit

        g = gens1[d]
        cands = by_prof2[profs1[g]]
        cur_steps = depth_steps[d]
        prev_elems, new_batch = depth_elems[d]

        for img_g in cands:
            if used2[img_g]:
                continue
            phi[g] = img_g
            used2[img_g] = True
            assigned_here = [g]
            ok = True

            for u, v, w in cur_steps:
                img_w = tbl2[phi[u]][phi[v]]
                if used2[img_w] or profs2[img_w] != profs1[w]:
                    ok = False
                    break
                phi[w] = img_w
                used2[img_w] = True
                assigned_here.append(w)

            if ok:
                # Verify all products involving new_batch against prev_elems + new_batch
                for a in new_batch:
                    pa = phi[a]
                    for b in prev_elems:
                        pb = phi[b]
                        ab = tbl1[a][b]
                        if phi[ab] != -1 and phi[ab] != tbl2[pa][pb]:
                            ok = False
                            break
                        ba = tbl1[b][a]
                        if phi[ba] != -1 and phi[ba] != tbl2[pb][pa]:
                            ok = False
                            break
                    if not ok:
                        break
                if ok:
                    for a in new_batch:
                        pa = phi[a]
                        for b in new_batch:
                            if phi[tbl1[a][b]] != tbl2[pa][phi[b]]:
                                ok = False
                                break
                        if not ok:
                            break

            if ok and backtrack(d + 1):
                return True

            for w in assigned_here:
                used2[phi[w]] = False
                phi[w] = -1

        return False

    backtrack(0)
    return results


def find_loop_isomorphism(q1: Loop, q2: Loop) -> Optional[Perm]:
    """Return an explicit loop isomorphism phi: Q1 -> Q2 (as a Perm), or None if non-isomorphic."""
    found = find_all_loop_isomorphisms(q1, q2, limit=1)
    return found[0] if found else None


def loop_automorphisms(loop: Loop) -> List[Perm]:
    """Return all loop automorphisms phi: Q -> Q (each verified on all n^2 pairs)."""
    return find_all_loop_isomorphisms(loop, loop, limit=None)


def sims_automorphism_group(loop: Loop, prefer_idx_from: int = 1) -> PermGroup:
    """Compute Aut(Q) as an exact PermGroup via Sims bottom-up point-stabilizer search
    on a compact generating base B = [g_0, ..., g_{k-1}] of Q.

    Every candidate generator found at level r (mapping (g_0, ..., g_{r-1}) |-> itself
    and g_r |-> y outside the already-generated stabilizer orbit) is verified on all n^2
    Cayley entries via `loop.is_automorphism`, while impossibility of missing cosets is
    certified by exhaustive forward-checked subloop-closure search. Scales cleanly to
    order 1536+ (`|Aut(Q_1536)| = 1280` in ~12s).
    """
    n = loop.n
    if n <= 1:
        return PermGroup(n, [], allow_jordan_fastpath=False)
    tbl = loop.table
    base_profs = element_profiles(loop)
    fine_profs: List[Tuple[Any, ...]] = []
    for x in range(n):
        rx = tbl[x]
        c_comm = c_m1 = c_m2 = c_m3 = 0
        for y in range(n):
            xy, yx = rx[y], tbl[y][x]
            if xy == yx:
                c_comm += 1
            if tbl[rx[yx]][x] == xy:
                c_m1 += 1
            if tbl[yx][y] == x:
                c_m2 += 1
            if tbl[xy][yx] == 0:
                c_m3 += 1
        fine_profs.append((base_profs[x], c_comm, c_m1, c_m2, c_m3))

    freq = Counter(fine_profs)
    by_prof: Dict[Tuple[Any, ...], List[int]] = defaultdict(list)
    for y, p in enumerate(fine_profs):
        by_prof[p].append(y)

    generated = [False] * n
    generated[0] = True
    gen_list = [0]
    chosen_gens: List[int] = []
    depth_steps: List[List[Tuple[int, int, int]]] = []
    depth_checks: List[List[Tuple[int, int, int]]] = []

    while len(gen_list) < n:
        cands = [x for x in range(1, n) if not generated[x]]
        best = min(
            cands,
            key=lambda x: (
                0 if freq[fine_profs[x]] <= 16 else (1 if x >= prefer_idx_from else 2),
                freq[fine_profs[x]],
                x,
            ),
        )
        chosen_gens.append(best)
        generated[best] = True
        gen_list.append(best)
        cur_steps: List[Tuple[int, int, int]] = []
        cur_checks: List[Tuple[int, int, int]] = []
        q_bfs = deque([best])
        while q_bfs:
            a = q_bfs.popleft()
            for b in list(gen_list):
                ab = tbl[a][b]
                if not generated[ab]:
                    generated[ab] = True
                    gen_list.append(ab)
                    cur_steps.append((a, b, ab))
                    q_bfs.append(ab)
                elif len(cur_checks) < 64:
                    cur_checks.append((a, b, ab))
                ba = tbl[b][a]
                if not generated[ba]:
                    generated[ba] = True
                    gen_list.append(ba)
                    cur_steps.append((b, a, ba))
                    q_bfs.append(ba)
                elif len(cur_checks) < 64:
                    cur_checks.append((b, a, ba))
        depth_steps.append(cur_steps)
        depth_checks.append(cur_checks)

    k = len(chosen_gens)
    subloop_after: List[List[int]] = []
    acc = [0]
    for d in range(k):
        acc = acc + [chosen_gens[d]] + [w for _, _, w in depth_steps[d]]
        subloop_after.append(list(acc))

    def find_one_with_prefix(fixed: Dict[int, int]) -> Optional[Perm]:
        phi = [-1] * n
        used = [False] * n
        phi[0] = 0
        used[0] = True

        def bt(d: int) -> Optional[Perm]:
            if d == k:
                cand_p = tuple(phi)
                return cand_p if loop.is_automorphism(cand_p) else None

            g = chosen_gens[d]
            cands_d = (fixed[d],) if d in fixed else tuple(by_prof[fine_profs[g]])
            steps_d = depth_steps[d]
            checks_d = depth_checks[d]

            for img_g in cands_d:
                if used[img_g] or fine_profs[img_g] != fine_profs[g]:
                    continue
                phi[g] = img_g
                used[img_g] = True
                assigned = [g]
                ok = True

                for u, v, w in steps_d:
                    iw = tbl[phi[u]][phi[v]]
                    if used[iw] or fine_profs[iw] != fine_profs[w]:
                        ok = False
                        break
                    phi[w] = iw
                    used[iw] = True
                    assigned.append(w)

                if ok:
                    for u, v, w in checks_d:
                        if tbl[phi[u]][phi[v]] != phi[w]:
                            ok = False
                            break

                if ok and d < k - 1 and len(subloop_after[d]) <= 300:
                    sub_el = subloop_after[d]
                    for a in assigned:
                        pa = phi[a]
                        ra = tbl[a]
                        rpa = tbl[pa]
                        for b in sub_el:
                            if phi[ra[b]] != rpa[phi[b]] or phi[tbl[b][a]] != tbl[phi[b]][pa]:
                                ok = False
                                break
                        if not ok:
                            break

                if ok:
                    res = bt(d + 1)
                    if res is not None:
                        return res

                for w in assigned:
                    used[phi[w]] = False
                    phi[w] = -1
            return None

        return bt(0)

    found_gens: List[Perm] = []
    for r in range(k - 1, -1, -1):
        gr = chosen_gens[r]
        orb_gr: Set[int] = {gr}

        def expand_orb() -> None:
            q_o = deque(orb_gr)
            while q_o:
                u = q_o.popleft()
                for gen in found_gens:
                    v = gen[u]
                    if v not in orb_gr:
                        orb_gr.add(v)
                        q_o.append(v)

        expand_orb()
        base_prefix = {j: chosen_gens[j] for j in range(r)}
        for y in by_prof[fine_profs[gr]]:
            if y in orb_gr:
                continue
            pref = dict(base_prefix)
            pref[r] = y
            witness = find_one_with_prefix(pref)
            if witness is not None:
                found_gens.append(witness)
                found_gens.append(invert(witness))
                expand_orb()

    return PermGroup(n, found_gens, allow_jordan_fastpath=False)


def are_loops_isomorphic(q1: Loop, q2: Loop) -> bool:
    return find_loop_isomorphism(q1, q2) is not None


def deduplicate_loops(loops: Sequence[Loop]) -> List[Tuple[Loop, List[str]]]:
    """Group a sequence of loops into exact isomorphism classes.

    Returns list of (canonical_rep_loop, [all_member_names_in_class]).
    """
    buckets: Dict[Tuple[Any, ...], List[Tuple[Loop, List[str]]]] = defaultdict(list)
    result: List[Tuple[Loop, List[str]]] = []
    for lp in loops:
        fp = loop_fingerprint(lp)
        matched = False
        for rep, names in buckets[fp]:
            if are_loops_isomorphic(lp, rep):
                names.append(lp.name)
                matched = True
                break
        if not matched:
            entry = (lp, [lp.name])
            buckets[fp].append(entry)
            result.append(entry)
    return result


# ======================================================================
# Bol Folder Constructors
# ======================================================================


@dataclass
class FolderCheckResult:
    is_valid: bool
    reason: str
    loop: Optional[Loop] = None


def bol_folder_from_perms(
    degree: int,
    G_elements: Optional[Sequence[Perm]],
    H_elements: Sequence[Perm],
    K_elements: Sequence[Perm],
    name: str = "folder_bol_loop",
    verify_conjugate_transversals: bool = True,
) -> FolderCheckResult:
    """Construct a left Bol loop from a permutation-group folder (G, H, K).

    Folder conventions (matching Nagy arXiv:math/0703919v1 §2):
      - 1 in K
      - (F1) for all a, b in K: a * b * a in K
      - (F2) K is a left transversal to H (and hence to all conjugates H^g when G is finite and (F1) holds).
      - Loop operation on K: a o b = unique u in (a * b * H) cap K.

    Note: `G_elements` is optional (used only to cross-check |K| * |H| == |G| if supplied).
    Even when G is large, only `H_elements` and `K_elements` are needed to verify (F1),
    left-coset disjointness of kH, and build the exact multiplication table on K!
    """
    id_p = identity_perm(degree)
    H_set = set(H_elements)
    if id_p not in H_set:
        return FolderCheckResult(False, "1_G not in H")

    # Reorder K so K[0] == id_p
    K_unique = list(dict.fromkeys(K_elements))
    if len(K_unique) != len(K_elements):
        return FolderCheckResult(False, "K contains duplicate elements")
    if id_p not in K_unique:
        return FolderCheckResult(False, "1_G not in K")
    K_list = [id_p] + [k for k in K_unique if k != id_p]
    K_index: Dict[Perm, int] = {k: idx for idx, k in enumerate(K_list)}
    m = len(K_list)

    if G_elements is not None and m * len(H_set) != len(set(G_elements)):
        return FolderCheckResult(
            False,
            f"|K|*|H| = {m}*{len(H_set)} != |G| = {len(set(G_elements))}",
        )

    # Check (F1): for all a, b in K, a * b * a in K (and a^{-1} in K)
    for a in K_list:
        if invert(a) not in K_index:
            return FolderCheckResult(False, "K is not closed under inverses")
        for b in K_list:
            aba = compose(a, compose(b, a))
            if aba not in K_index:
                return FolderCheckResult(False, "(F1) failed: a*b*a not in K")

    # Map every element of K * H to its unique representative index in K
    coset_rep: Dict[Perm, int] = {}
    for idx, k in enumerate(K_list):
        for h in H_set:
            kh = compose(k, h)
            if kh in coset_rep:
                return FolderCheckResult(
                    False,
                    f"K is not a left transversal to H: {idx} and {coset_rep[kh]} share coset",
                )
            coset_rep[kh] = idx

    if verify_conjugate_transversals and m * len(H_set) <= 8000:
        # Explicitly verify (F2) on all conjugates s^{-1} H s for s in K
        for s in K_list:
            s_inv = invert(s)
            Hs = [compose(s_inv, compose(h, s)) for h in H_set]
            seen_conj: Set[Perm] = set()
            for k in K_list:
                for hs in Hs:
                    khs = compose(k, hs)
                    if khs in seen_conj:
                        return FolderCheckResult(False, "(F2) failed on conjugate H^s")
                    seen_conj.add(khs)

    # Construct multiplication table on {0, ..., m - 1}:
    # a * b in K * H must lie in coset_rep (which equals G if G = K * H!)
    table: List[List[int]] = [[0] * m for _ in range(m)]
    for i, a in enumerate(K_list):
        row = table[i]
        for j, b in enumerate(K_list):
            ab = compose(a, b)
            u_idx = coset_rep.get(ab)
            if u_idx is None:
                return FolderCheckResult(
                    False,
                    "K * H is not closed under K * K (so K is not a full transversal of <K, H>)",
                )
            row[j] = u_idx

    loop = Loop(table, name=name, validate_loop=True)
    is_lbol, wit = loop.check_left_bol()
    if not is_lbol:
        return FolderCheckResult(False, f"Constructed loop failed left Bol at {wit}")
    return FolderCheckResult(True, "ok", loop=loop)


def exact_factorization_bol_loop(
    degree: int,
    Y0_elements: Sequence[Perm],
    Y1_elements: Sequence[Perm],
    name: str = "exact_fact_bol_loop",
) -> Loop:
    """Nagy arXiv:math/0703919v1 Prop 3.2 exact-factorization left Bol loop Q_{(X, Y_0, Y_1)}.

    Given subgroups Y_0, Y_1 of a finite group X <= S_{degree} with Y_0 cap Y_1 = {1}
    and X = Y_0 * Y_1 (so |X| = |Y_0| * |Y_1|):
      Folder is G = X x X, H = Y_0 x Y_1, S = {(x, x^{-1}) : x in X}.
      For s = (x, x^{-1}) and t = (z, z^{-1}):
        Let a = x * z, b = x^{-1} * z^{-1}.
        Write a^{-1} = a_0 * a_1 and b = b_0 * b_1 uniquely with a_0, b_0 in Y_0 and a_1, b_1 in Y_1.
        Then s o t = (u, u^{-1}) where u = a_1^{-1} * b_0^{-1}.
    """
    id_p = identity_perm(degree)
    Y0 = list(dict.fromkeys(Y0_elements))
    Y1 = list(dict.fromkeys(Y1_elements))
    if id_p not in Y0 or id_p not in Y1:
        raise ValueError("1_X must belong to both Y_0 and Y_1")
    if PermGroup(degree, Y0).order() != len(Y0):
        raise ValueError("Y_0 is not closed as a subgroup")
    if PermGroup(degree, Y1).order() != len(Y1):
        raise ValueError("Y_1 is not closed as a subgroup")
    if len(set(Y0) & set(Y1)) != 1:
        raise ValueError("Y_0 cap Y_1 must be trivial ({1_X})")

    # Build X = Y_0 * Y_1 and record unique factorization z = Y0[i0] * Y1[i1]
    Y0 = [id_p] + [y for y in Y0 if y != id_p]
    Y1 = [id_p] + [y for y in Y1 if y != id_p]
    n0, n1 = len(Y0), len(Y1)
    y0_to_i = {y: i for i, y in enumerate(Y0)}
    y1_to_i = {y: i for i, y in enumerate(Y1)}

    X_list: List[Perm] = []
    decomp_pair: Dict[Perm, Tuple[int, int]] = {}
    pair_to_x_idx: List[List[int]] = [[0] * n1 for _ in range(n0)]
    for i0, y0 in enumerate(Y0):
        row_px = pair_to_x_idx[i0]
        for i1, y1 in enumerate(Y1):
            prod = compose(y0, y1)
            if prod in decomp_pair:
                raise ValueError("Product Y_0 * Y_1 has collisions (Y_0 cap Y_1 != 1)")
            idx = len(X_list)
            decomp_pair[prod] = (i0, i1)
            row_px[i1] = idx
            X_list.append(prod)

    n = len(X_list)
    if n != n0 * n1:
        raise ValueError("Size mismatch in Y_0 * Y_1")

    # Verify X = Y_0 * Y_1 is closed under inversion and multiplication via Y_1 * Y_0 <= Y_0 * Y_1!
    x_to_idx: Dict[Perm, int] = {x: idx for idx, x in enumerate(X_list)}
    inv_idx = [0] * n
    for i, x in enumerate(X_list):
        ix = invert(x)
        if ix not in x_to_idx:
            raise ValueError("Y_0 * Y_1 is not closed under inverses (not a group!)")
        inv_idx[i] = x_to_idx[ix]

    mul_Y0 = [[y0_to_i[compose(Y0[a], Y0[b])] for b in range(n0)] for a in range(n0)]
    mul_Y1 = [[y1_to_i[compose(Y1[a], Y1[b])] for b in range(n1)] for a in range(n1)]
    swap0 = [[0] * n0 for _ in range(n1)]
    swap1 = [[0] * n0 for _ in range(n1)]
    for i1, y1 in enumerate(Y1):
        s0_row = swap0[i1]
        s1_row = swap1[i1]
        for j0, z0 in enumerate(Y0):
            pair = decomp_pair.get(compose(y1, z0))
            if pair is None:
                raise ValueError(
                    "Y_0 * Y_1 is not closed under multiplication (not an exact factorization of a group!)"
                )
            s0_row[j0], s1_row[j0] = pair

    # Build integer multiplication table of X in pure array arithmetic:
    # (Y0[i0] * Y1[i1]) * (Y0[j0] * Y1[j1]) = Y0[mul_Y0[i0][t0]] * Y1[mul_Y1[t1][j1]]
    mul_X: List[List[int]] = [[0] * n for _ in range(n)]
    x_i0 = [0] * n
    x_i1 = [0] * n
    for i0 in range(n0):
        for i1 in range(n1):
            idx = pair_to_x_idx[i0][i1]
            x_i0[idx] = i0
            x_i1[idx] = i1

    for i in range(n):
        i0 = x_i0[i]
        i1 = x_i1[i]
        my0_i0 = mul_Y0[i0]
        s0_i1 = swap0[i1]
        s1_i1 = swap1[i1]
        row = mul_X[i]
        for j in range(n):
            j0 = x_i0[j]
            t0 = s0_i1[j0]
            t1 = s1_i1[j0]
            row[j] = pair_to_x_idx[my0_i0[t0]][mul_Y1[t1][x_i1[j]]]

    y0_inv_x_idx = [x_to_idx[invert(y0)] for y0 in Y0]
    y1_inv_x_idx = [x_to_idx[invert(y1)] for y1 in Y1]
    pi0_inv_idx = [y0_inv_x_idx[x_i0[i]] for i in range(n)]
    pi1_inv_idx = [y1_inv_x_idx[x_i1[i]] for i in range(n)]

    # Loop multiplication on X_list:
    # a = x * z -> a^{-1} = inv_idx[mul_X[i][j]], so a_1^{-1} = pi1_inv_idx[a_inv]
    # b = x^{-1} * z^{-1} = mul_X[inv_idx[i]][inv_idx[j]], so b_0^{-1} = pi0_inv_idx[b]
    # u = a_1^{-1} * b_0^{-1}
    loop_table: List[List[int]] = [[0] * n for _ in range(n)]
    for i in range(n):
        ix = inv_idx[i]
        row_mx = mul_X[i]
        row_mix = mul_X[ix]
        row_l = loop_table[i]
        for j in range(n):
            a_inv = inv_idx[row_mx[j]]
            b = row_mix[inv_idx[j]]
            u = mul_X[pi1_inv_idx[a_inv]][pi0_inv_idx[b]]
            row_l[j] = u

    return Loop(loop_table, name=name, validate_loop=True)
