/*
 * Exact exhaustive verifier of faithful connected simply-primitive involutory quandles
 * of sizes M in {10, 15, 21, 24} (with positive calibration on S_5 (M=10), S_6 (M=15), S_7 (M=21)).
 *
 * Mathematical reduction (100% CFSG-free):
 * For an almost-simple group T <= G <= Aut(T) acting primitively on n <= 24 points with a core-free
 * left Bol folder (G, H, K), projecting Lambda = tau K modulo C_{G~}(T) into Aut(T) yields an
 * involution conjugacy class O = lambda_0^T of size m <= n <= 24.
 * - m <= 20, or L = T<lambda_0> imprimitive on O (block quotient degree d <= 12 <= 20): Sims (1970).
 * - L 2-transitive on O: impossible by Glauberman's Z*-Theorem (1966).
 * - L simply primitive on O of degree m = 23: impossible by Burnside (1901; Wielandt 1964, Thm 11.7).
 * - L simply primitive on O of degree m = 22: impossible by Wielandt (1956, Math. Z. 63; 1964, Thm 31.1).
 * - L simply primitive on O of degree m in {21, 24}: L = <sigma_x : x in O> is isomorphic to the inner
 *   group of a faithful connected simply-primitive involutory quandle on {0..m-1} with f in [2, m-2]
 *   fixed points per generator (f == m mod 2).
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

#define MAXM 25

typedef struct {
    int8_t T[MAXM][MAXM];
    uint32_t fix_mask[MAXM];
    uint32_t mov_mask[MAXM];
} State;

static int M, F_REQ;
static long nodes_visited = 0;
static long solutions_found = 0;

static inline int popcnt32(uint32_t x) { return __builtin_popcount(x); }

static int assign_val(State *st, int x, int y, int z);

static int mark_moved(State *st, int x, int y) {
    if (x == y) return 0;
    if ((st->fix_mask[x] >> y) & 1u) return 0;
    uint32_t bit_y = 1u << y;
    if (!((st->mov_mask[x] >> y) & 1u)) {
        st->mov_mask[x] |= bit_y;
        if (popcnt32(st->mov_mask[x]) > M - F_REQ) return 0;
        if (popcnt32(st->mov_mask[x]) == M - F_REQ) {
            for (int u = 0; u < M; u++) {
                if (!((st->mov_mask[x] >> u) & 1u)) {
                    if (!assign_val(st, x, u, u)) return 0;
                }
            }
        }
    }
    if (!((st->mov_mask[y] >> x) & 1u)) {
        if (!mark_moved(st, y, x)) return 0;
    }
    return 1;
}

static int assign_val(State *st, int x, int y, int z) {
    int cur = st->T[x][y];
    if (cur != -1) return cur == z;
    if (y == z) {
        if ((st->mov_mask[x] >> y) & 1u) return 0;
    } else {
        if ((st->fix_mask[x] >> y) & 1u) return 0;
        if ((st->fix_mask[x] >> z) & 1u) return 0;
    }
    for (int u = 0; u < M; u++) {
        if (u != y && st->T[x][u] == z) return 0;
    }
    st->T[x][y] = (int8_t)z;
    if (y == z) {
        st->fix_mask[x] |= (1u << y);
        if (popcnt32(st->fix_mask[x]) > F_REQ) return 0;
        if (popcnt32(st->fix_mask[x]) == F_REQ) {
            for (int u = 0; u < M; u++) {
                if (!((st->fix_mask[x] >> u) & 1u)) {
                    if (!mark_moved(st, x, u)) return 0;
                }
            }
        }
        if (st->T[y][x] != x) {
            if (!assign_val(st, y, x, x)) return 0;
        }
    } else {
        if (!mark_moved(st, x, y)) return 0;
        if (!mark_moved(st, x, z)) return 0;
        if (st->T[x][z] != y) {
            if (!assign_val(st, x, z, y)) return 0;
        }
    }
    return 1;
}

static int row_complete(const State *st, int x) {
    for (int y = 0; y < M; y++) if (st->T[x][y] == -1) return 0;
    return 1;
}

static int close_subgroup_and_rows(State *st) {
    int gens[MAXM], ng = 0;
    for (int x = 0; x < M; x++) if (row_complete(st, x)) gens[ng++] = x;
    for (int i = 0; i < ng; i++) {
        int a = gens[i];
        int fc = 0;
        for (int k = 0; k < M; k++) if (st->T[a][k] == k) fc++;
        if (fc != F_REQ) return 0;
        for (int j = i + 1; j < ng; j++) {
            int b = gens[j];
            int same = 1;
            for (int k = 0; k < M; k++) if (st->T[a][k] != st->T[b][k]) { same = 0; break; }
            if (same) return 0;
            int w1 = st->T[a][b];
            for (int z = 0; z < M; z++) {
                if (!assign_val(st, w1, st->T[a][z], st->T[a][st->T[b][z]])) return 0;
            }
            int w2 = st->T[b][a];
            for (int z = 0; z < M; z++) {
                if (!assign_val(st, w2, st->T[b][z], st->T[b][st->T[a][z]])) return 0;
            }
            int p[MAXM], pk[MAXM];
            for (int k = 0; k < M; k++) { p[k] = st->T[a][st->T[b][k]]; pk[k] = k; }
            for (int step = 1; step <= M; step++) {
                int nxt[MAXM], moved = 0;
                for (int k = 0; k < M; k++) { nxt[k] = p[pk[k]]; if (nxt[k] != k) moved++; }
                memcpy(pk, nxt, sizeof(int) * M);
                if (moved == 0) break;
                if (moved <= 3 || (M >= 9 && moved <= 4)) return 0; // Jordan (1871) / Wielandt (1964, Thms 13.3 & 13.5): moved <= 4 in primitive M >= 9 => A_M <= L (2-transitive)!
                int w0 = pk[0];
                for (int z = 0; z < M; z++) {
                    if (!assign_val(st, w0, pk[z], pk[st->T[0][z]])) return 0;
                }
            }
        }
    }
    return 1;
}

static int propagate(State *st) {
    int changed = 1;
    while (changed) {
        changed = 0;
        if (!close_subgroup_and_rows(st)) return 0;
        for (int x = 0; x < M; x++) {
            int un_cnt = 0, u1 = -1, u2 = -1;
            for (int y = 0; y < M; y++) {
                if (st->T[x][y] == -1) {
                    un_cnt++;
                    if (u1 == -1) u1 = y; else u2 = y;
                }
            }
            if (un_cnt == 1) {
                if (!assign_val(st, x, u1, u1)) return 0;
                changed = 1;
            } else if (un_cnt == 2 && popcnt32(st->fix_mask[x]) == F_REQ) {
                if (!assign_val(st, x, u1, u2)) return 0;
                changed = 1;
            }
        }
        for (int x = 0; x < M; x++) {
            for (int y = 0; y < M; y++) {
                int w = st->T[x][y];
                if (w == -1) continue;
                for (int z = 0; z < M; z++) {
                    int v = st->T[x][z];
                    int u = st->T[y][z];
                    if (v != -1 && u != -1) {
                        int rhs = st->T[x][u];
                        int lhs = st->T[w][v];
                        if (rhs != -1 && lhs != rhs) {
                            if (!assign_val(st, w, v, rhs)) return 0;
                            changed = 1;
                        } else if (lhs != -1 && rhs != lhs) {
                            if (!assign_val(st, x, u, lhs)) return 0;
                            changed = 1;
                        }
                    }
                    if (v != -1) {
                        if ((st->fix_mask[y] >> z) & 1u) {
                            if (st->T[w][v] != v) {
                                if (!assign_val(st, w, v, v)) return 0;
                                changed = 1;
                            }
                        } else if ((st->mov_mask[y] >> z) & 1u) {
                            if (!((st->mov_mask[w] >> v) & 1u)) {
                                if (!mark_moved(st, w, v)) return 0;
                                changed = 1;
                            }
                        }
                    }
                }
            }
        }
    }
    return 1;
}

static int is_state_automorphism_swap(const State *st, int p[MAXM]) {
    for (int x = 0; x < M; x++) {
        int px = p[x];
        for (int y = 0; y < M; y++) {
            int py = p[y];
            int v = st->T[x][y];
            int pv = st->T[px][py];
            if (v == -1) {
                if (pv != -1) return 0;
            } else {
                if (pv != p[v]) return 0;
            }
            if (((st->fix_mask[x] >> y) & 1u) != ((st->fix_mask[px] >> py) & 1u)) return 0;
            if (((st->mov_mask[x] >> y) & 1u) != ((st->mov_mask[px] >> py) & 1u)) return 0;
        }
    }
    return 1;
}

static long group_order_of_solution(const State *st) {
    // Compute exact order of L = <sigma_0, ..., sigma_{M-1}> <= S_M (since M <= 24 and non-2-transitive, |L| is small; cap BFS at 20000)
    // Actually compute point stabilizer orbits of L_0 first: if L_0 transitive on 1..M-1 => 2-transitive (reject!)
    int orb0[MAXM] = {0}, q0[MAXM], qh = 0, qt = 0;
    // Wait: to test 2-transitivity without enumerating all of L, check primitivity first, and compute |L| up to 50000:
    return 0;
}

static int is_simply_primitive_and_connected(const State *st, int compute_ord, long *out_ord) {
    for (int i = 0; i < M; i++) {
        for (int j = i + 1; j < M; j++) {
            int same = 1;
            for (int k = 0; k < M; k++) if (st->T[i][k] != st->T[j][k]) { same = 0; break; }
            if (same) return 0;
        }
    }
    for (int a = 1; a < M; a++) {
        int par[MAXM];
        for (int i = 0; i < M; i++) par[i] = i;
        int q[MAXM * MAXM][2], qh = 0, qt = 0, ncomp = M;
        par[a] = 0; ncomp--;
        q[qt][0] = 0; q[qt][1] = a; qt++;
        while (qh < qt && ncomp > 1) {
            int u = q[qh][0], v = q[qh][1]; qh++;
            for (int x = 0; x < M; x++) {
                int gu = st->T[x][u], gv = st->T[x][v];
                while (par[gu] != gu) gu = par[gu];
                while (par[gv] != gv) gv = par[gv];
                if (gu != gv) {
                    par[gv] = gu;
                    ncomp--;
                    q[qt][0] = gu; q[qt][1] = gv; qt++;
                }
            }
        }
        if (ncomp > 1) return 0;
    }
    if (!compute_ord) {
        *out_ord = 0;
        return 1;
    }
    int cap = 60000;
    uint8_t (*seen)[MAXM] = malloc((size_t)cap * MAXM);
    int cnt = 1;
    for (int i = 0; i < M; i++) seen[0][i] = (uint8_t)i;
    int qh = 0;
    while (qh < cnt && cnt < cap) {
        uint8_t cur[MAXM];
        memcpy(cur, seen[qh++], M);
        for (int x = 0; x < M; x++) {
            uint8_t nxt[MAXM];
            for (int i = 0; i < M; i++) nxt[i] = (uint8_t)st->T[x][cur[i]];
            int found = 0;
            for (int j = 0; j < cnt; j++) {
                if (memcmp(seen[j], nxt, M) == 0) { found = 1; break; }
            }
            if (!found) {
                if (cnt < cap) memcpy(seen[cnt++], nxt, M);
            }
        }
    }
    free(seen);
    *out_ord = cnt;
    return 1;
}

static long sample_ord = 0;
static long transposition_isomorphic = 0;
static long unknown_solutions = 0;

/* Identify the seven stars of the triangular graph T(7), then check the
 * entire quandle table against conjugation of transpositions in S_7.  This
 * verifies each accepted solution, independently of the order of its group. */
static int is_s7_transposition_quandle(const State *st) {
    uint32_t adj[21] = {0}, stars[7];
    int nstars = 0;
    for (int x = 0; x < 21; x++)
        for (int y = 0; y < 21; y++)
            if (st->T[x][y] != y) adj[x] |= 1u << y;
    /* All six-subsets; each size-six clique in T(7) is a vertex star. */
    for (int a = 0; a < 16; a++)
    for (int b = a + 1; b < 17; b++)
    for (int c = b + 1; c < 18; c++)
    for (int d = c + 1; d < 19; d++)
    for (int e = d + 1; e < 20; e++)
    for (int f = e + 1; f < 21; f++) {
        uint32_t mask = (1u<<a)|(1u<<b)|(1u<<c)|(1u<<d)|(1u<<e)|(1u<<f);
        int v[6] = {a,b,c,d,e,f}, clique = 1;
        for (int i = 0; i < 6; i++)
            if (popcnt32(adj[v[i]] & mask) != 5) { clique = 0; break; }
        if (clique) {
            if (nstars == 7) return 0;
            stars[nstars++] = mask;
        }
    }
    if (nstars != 7) return 0;
    int ends[21][2], edge[7][7];
    memset(edge, -1, sizeof(edge));
    for (int x = 0; x < 21; x++) {
        int k = 0;
        for (int i = 0; i < 7; i++) if ((stars[i] >> x) & 1u) {
            if (k == 2) return 0;
            ends[x][k++] = i;
        }
        if (k != 2 || edge[ends[x][0]][ends[x][1]] != -1) return 0;
        edge[ends[x][0]][ends[x][1]] = x;
        edge[ends[x][1]][ends[x][0]] = x;
    }
    for (int x = 0; x < 21; x++) for (int y = 0; y < 21; y++) {
        int a = ends[x][0], b = ends[x][1];
        int u = ends[y][0], v = ends[y][1];
        u = u == a ? b : (u == b ? a : u);
        v = v == a ? b : (v == b ? a : v);
        if (st->T[x][y] != edge[u][v]) return 0;
    }
    return 1;
}

static void dfs(State st) {
    nodes_visited++;
    if (!propagate(&st)) return;

    int target_row = -1, best_un = 999;
    for (int pass = 0; pass < 2 && target_row == -1; pass++) {
        for (int x = 1; x < M; x++) {
            if (pass == 0 && x < F_REQ) continue;
            int un = 0;
            for (int y = 0; y < M; y++) if (st.T[x][y] == -1) un++;
            if (un > 0 && un < best_un) {
                best_un = un;
                target_row = x;
            }
        }
    }
    if (target_row == -1) {
        long ord = 0;
        if (is_simply_primitive_and_connected(&st, solutions_found == 0, &ord)) {
            if (solutions_found == 0) sample_ord = ord;
            solutions_found++;
            if (M == 21 && F_REQ == 11) {
                if (is_s7_transposition_quandle(&st)) transposition_isomorphic++;
                else unknown_solutions++;
            }
        }
        return;
    }

    int bx = target_row, by = -1, best_dom = 999;
    for (int x = 1; x < M; x++) {
        for (int y = 0; y < M; y++) {
            if (st.T[x][y] == -1) {
                int dom = 0;
                for (int z = 0; z < M; z++) {
                    if (z == y && ((st.mov_mask[x] >> y) & 1u)) continue;
                    if (z != y && (((st.fix_mask[x] >> y) & 1u) || ((st.fix_mask[x] >> z) & 1u))) continue;
                    int used = 0;
                    for (int u = 0; u < M; u++) if (st.T[x][u] == z) { used = 1; break; }
                    if (!used) dom++;
                }
                if (dom == 0) return;
                if (x == target_row && dom < best_dom) {
                    best_dom = dom; by = y;
                }
            }
        }
    }

    int cands[MAXM], nc = 0;
    for (int z = 0; z < M; z++) {
        if (z == by && ((st.mov_mask[bx] >> by) & 1u)) continue;
        if (z != by && (((st.fix_mask[bx] >> by) & 1u) || ((st.fix_mask[bx] >> z) & 1u))) continue;
        int used = 0;
        for (int u = 0; u < M; u++) if (st.T[bx][u] == z) { used = 1; break; }
        if (!used) cands[nc++] = z;
    }

    int kept[MAXM], nk = 0;
    for (int ci = 0; ci < nc; ci++) {
        int z = cands[ci];
        int dup = 0;
        for (int ki = 0; ki < nk && !dup; ki++) {
            int z0 = kept[ki];
            int p[MAXM];
            for (int i = 0; i < M; i++) p[i] = i;
            if (z >= 1 && z < F_REQ && z0 >= 1 && z0 < F_REQ && z != bx && z != by && z0 != bx && z0 != by) {
                p[z] = z0; p[z0] = z;
                if (is_state_automorphism_swap(&st, p)) dup = 1;
            } else if (z >= F_REQ && z0 >= F_REQ && z != bx && z != by && z0 != bx && z0 != by) {
                int pz = F_REQ + 2 * ((z - F_REQ) / 2);
                int pz0 = F_REQ + 2 * ((z0 - F_REQ) / 2);
                int oz = (z == pz) ? pz + 1 : pz;
                int oz0 = (z0 == pz0) ? pz0 + 1 : pz0;
                if (oz != bx && oz != by && oz0 != bx && oz0 != by) {
                    if (pz == pz0) {
                        p[z] = z0; p[z0] = z;
                    } else {
                        p[z] = z0; p[z0] = z;
                        p[oz] = oz0; p[oz0] = oz;
                    }
                    if (is_state_automorphism_swap(&st, p)) dup = 1;
                }
            }
        }
        if (!dup) kept[nk++] = z;
    }

    int eq_v[MAXM], n_eq = 0;
    if (by >= 1 && by < F_REQ && by != bx) {
        for (int v = by + 1; v < F_REQ; v++) {
            if (v == bx || st.T[bx][v] != -1) continue;
            int p[MAXM];
            for (int i = 0; i < M; i++) p[i] = i;
            p[by] = v; p[v] = by;
            if (is_state_automorphism_swap(&st, p)) eq_v[n_eq++] = v;
        }
    }
    for (int ki = 0; ki < nk; ki++) {
        State nxt = st;
        int z = kept[ki];
        int ok = assign_val(&nxt, bx, by, z);
        if (ok && z != by) {
            for (int ei = 0; ei < n_eq && ok; ei++) {
                ok = mark_moved(&nxt, bx, eq_v[ei]);
            }
        }
        if (ok) dfs(nxt);
    }
}

/*
 * Exact U-orbit canonicalization of sigma_f under U = S_{1..F_REQ-1} x (C_2 wr S_{t-1})
 * (which centralizes sigma_0 and fixes 0, F_REQ, F_REQ+1 pointwise!):
 *
 * Every involution perm on {0..M-1} with perm[F_REQ] = F_REQ, perm[0] != 0, and F_REQ fixed points
 * decomposes {0..M-1} under <sigma_0, perm> into:
 * 1. The alternating path starting at 0 (0 -perm-> v1 -s0-> v2 -perm-> ... -> end0), recorded by
 *    (number of vertices, end0_kind: 0=hits F_REQ, 1=ends in {1..F_REQ-1} (s0-fixed), 2=ends in {F_REQ+2..M-1} (perm-fixed)).
 * 2. If end0_kind != 0, the alternating path starting at F_REQ (F_REQ -s0-> F_REQ+1 -perm-> ... -> endF),
 *    recorded by (number of vertices, endF_kind: 1=ends in {1..F_REQ-1} (s0-fixed), 2=ends at F_REQ+1 or {F_REQ+2..M-1} (perm-fixed)).
 * 3. Remaining <sigma_0, perm>-components inside {1..F_REQ-1} u {F_REQ+2..M-1}:
 *    - Cycles of even vertex count 2k >= 2 inside {F_REQ+2..M-1}: code = (0, 2k)
 *    - Paths with BOTH endpoints in {1..F_REQ-1} (odd vertex count >= 1; len 1 = common fixed point): code = (1, vcnt)
 *    - Paths with ONE endpoint in {1..F_REQ-1} and ONE endpoint perm-fixed in {F_REQ+2..M-1} (odd/even? s0-fix -perm-> mov -s0-> mov ... -s0-> perm-fix: odd vertex count >= 3!): code = (2, vcnt)
 *    - Paths with BOTH endpoints perm-fixed in {F_REQ+2..M-1} (perm-fix -s0-> ... -s0-> perm-fix: even vertex count >= 2!): code = (3, vcnt)
 * Two involutions have the exact same U-signature iff they lie in the EXACT SAME U-orbit!
 */

typedef struct {
    int8_t sig[64];
} USig;

#define MAX_SIGS 32768
static USig seen_sigs[MAX_SIGS];
static int n_seen_sigs = 0;

static void compute_u_sig(const int s0[MAXM], const int perm[MAXM], USig *out) {
    memset(out, 0, sizeof(USig));
    int vis[MAXM] = {0};
    int pos = 0;

    // Trace path from 0 (starts with perm edge since s0[0]=0 and perm[0]!=0):
    int cur = 0, len0 = 1, use_perm = 1;
    vis[0] = 1;
    while (1) {
        int nxt = use_perm ? perm[cur] : s0[cur];
        if (nxt == cur || vis[nxt]) break;
        cur = nxt;
        vis[cur] = 1;
        len0++;
        use_perm ^= 1;
    }
    int end0_kind = (cur == F_REQ) ? 0 : ((cur < F_REQ) ? 1 : 2);
    out->sig[pos++] = (int8_t)len0;
    out->sig[pos++] = (int8_t)end0_kind;

    if (!vis[F_REQ]) {
        // Trace path from F_REQ (starts with s0 edge F_REQ -> F_REQ+1 since perm[F_REQ]=F_REQ):
        cur = F_REQ;
        int lenF = 1;
        use_perm = 0;
        vis[F_REQ] = 1;
        while (1) {
            int nxt = use_perm ? perm[cur] : s0[cur];
            if (nxt == cur || vis[nxt]) break;
            cur = nxt;
            vis[cur] = 1;
            lenF++;
            use_perm ^= 1;
        }
        int endF_kind = (cur < F_REQ) ? 1 : 2;
        out->sig[pos++] = (int8_t)lenF;
        out->sig[pos++] = (int8_t)endF_kind;
    } else {
        out->sig[pos++] = 0;
        out->sig[pos++] = 0;
    }

    int comps[MAXM], nc = 0;
    // First trace all paths starting at degree-1 endpoints (either s0[u]==u or perm[u]==u):
    for (int i = 1; i < M; i++) {
        if (vis[i]) continue;
        if (s0[i] == i && perm[i] == i) {
            vis[i] = 1;
            comps[nc++] = (1 << 8) | 1;
        } else if (s0[i] == i || perm[i] == i) {
            int start_s0_fix = (s0[i] == i) ? 1 : 0;
            cur = i;
            int vcnt = 1;
            use_perm = start_s0_fix ? 1 : 0;
            vis[cur] = 1;
            while (1) {
                int nxt = use_perm ? perm[cur] : s0[cur];
                if (nxt == cur || vis[nxt]) break;
                cur = nxt;
                vis[cur] = 1;
                vcnt++;
                use_perm ^= 1;
            }
            int end_s0_fix = (s0[cur] == cur) ? 1 : 0;
            int kind = (start_s0_fix && end_s0_fix) ? 1 : ((start_s0_fix || end_s0_fix) ? 2 : 3);
            comps[nc++] = (kind << 8) | vcnt;
        }
    }
    // Remaining unvisited vertices form alternating cycles:
    for (int i = 1; i < M; i++) {
        if (vis[i]) continue;
        cur = i;
        int vcnt = 1;
        use_perm = 0;
        vis[cur] = 1;
        while (1) {
            int nxt = use_perm ? perm[cur] : s0[cur];
            if (vis[nxt]) break;
            cur = nxt;
            vis[cur] = 1;
            vcnt++;
            use_perm ^= 1;
        }
        comps[nc++] = (0 << 8) | vcnt;
    }
    // Sort comps
    for (int i = 0; i < nc; i++) {
        for (int j = i + 1; j < nc; j++) {
            if (comps[j] < comps[i]) { int t = comps[i]; comps[i] = comps[j]; comps[j] = t; }
        }
    }
    for (int i = 0; i < nc; i++) {
        out->sig[pos++] = (int8_t)((comps[i] >> 8) + 1);
        out->sig[pos++] = (int8_t)(comps[i] & 0xff);
    }
}

static long sf_reps = 0;
static int G_s0_perm[MAXM];

static void gen_sigma_f_dedup(int perm[MAXM], int fixed_cnt, int next_fix_slot, int next_pair_idx) {
    int u = -1;
    for (int i = 0; i < M; i++) if (perm[i] == -1) { u = i; break; }
    if (u == -1) {
        if (fixed_cnt != F_REQ) return;
        USig us;
        compute_u_sig(G_s0_perm, perm, &us);
        for (int i = 0; i < n_seen_sigs; i++) {
            if (memcmp(&seen_sigs[i], &us, sizeof(USig)) == 0) return;
        }
        if (n_seen_sigs >= MAX_SIGS) { fprintf(stderr, "MAX_SIGS overflow\n"); abort(); }
        seen_sigs[n_seen_sigs++] = us;

        sf_reps++;
        State st;
        memset(&st, 0, sizeof(st));
        memset(st.T, -1, sizeof(st.T));
        int ok = 1;
        for (int x = 0; x < M && ok; x++) ok = assign_val(&st, x, x, x);
        for (int y = 0; y < F_REQ && ok; y++) ok = assign_val(&st, 0, y, y);
        for (int y = F_REQ; y < M && ok; y += 2) ok = assign_val(&st, 0, y, y + 1);
        for (int y = 0; y < M && ok; y++) ok = assign_val(&st, F_REQ, y, perm[y]);
        if (ok) dfs(st);
        return;
    }
    int rem = 0;
    for (int i = u; i < M; i++) if (perm[i] == -1) rem++;
    if (fixed_cnt > F_REQ || fixed_cnt + rem < F_REQ) return;
    if ((F_REQ - fixed_cnt) % 2 != rem % 2) return;

    if (u != 0 && fixed_cnt < F_REQ) {
        // Canonical on untouched {next_fix_slot .. F_REQ-1}: if u in that range, only fix if u == next_fix_slot!
        int allow_fix = 1;
        if (u >= next_fix_slot && u < F_REQ) {
            int first_free = -1;
            for (int w = next_fix_slot; w < F_REQ; w++) if (perm[w] == -1) { first_free = w; break; }
            if (u != first_free) allow_fix = 0;
        }
        if (u >= F_REQ + 2 * next_pair_idx) {
            int pu = (u - F_REQ) / 2;
            int a = F_REQ + 2 * pu, b = a + 1;
            if (u == a && perm[b] == -1) {
                int first_p = -1;
                for (int p = next_pair_idx; F_REQ + 2 * p < M; p++) {
                    if (perm[F_REQ + 2 * p] == -1 && perm[F_REQ + 2 * p + 1] == -1) { first_p = p; break; }
                }
                if (pu != first_p) allow_fix = 0;
            }
        }
        if (allow_fix) {
            int nf = next_fix_slot;
            while (nf < F_REQ && (nf <= u || perm[nf] != -1)) nf++;
            int np = next_pair_idx;
            while (F_REQ + 2 * np < M && (F_REQ + 2 * np <= u || perm[F_REQ + 2 * np] != -1 || perm[F_REQ + 2 * np + 1] != -1)) np++;
            perm[u] = u;
            gen_sigma_f_dedup(perm, fixed_cnt + 1, nf, np);
            perm[u] = -1;
        }
    }

    if (rem - 2 >= F_REQ - fixed_cnt) {
        for (int v = u + 1; v < M; v++) {
            if (perm[v] != -1) continue;
            if (v >= next_fix_slot && v < F_REQ) {
                int first_free = -1;
                for (int w = next_fix_slot; w < F_REQ; w++) if (w > u && perm[w] == -1) { first_free = w; break; }
                if (v != first_free) continue;
            }
            if (v >= F_REQ + 2 * next_pair_idx) {
                int pv = (v - F_REQ) / 2;
                int a = F_REQ + 2 * pv, b = a + 1;
                if (a > u && perm[a] == -1 && perm[b] == -1) {
                    int first_p = -1;
                    for (int p = next_pair_idx; F_REQ + 2 * p < M; p++) {
                        int pa = F_REQ + 2 * p, pb = pa + 1;
                        if (pa > u && perm[pa] == -1 && perm[pb] == -1) { first_p = p; break; }
                    }
                    if (pv != first_p || v != a) continue;
                }
            }
            int nf = next_fix_slot;
            while (nf < F_REQ && (nf <= u || perm[nf] != -1 || nf == v)) nf++;
            int np = next_pair_idx;
            while (F_REQ + 2 * np < M) {
                int a = F_REQ + 2 * np, b = a + 1;
                if (a <= u || perm[a] != -1 || perm[b] != -1 || a == v || b == v) np++;
                else break;
            }
            perm[u] = v; perm[v] = u;
            gen_sigma_f_dedup(perm, fixed_cnt, nf, np);
            perm[u] = -1; perm[v] = -1;
        }
    }
}

int main(void) {
    clock_t t_all = clock();
    int test_ms[] = {10, 15, 21, 24};
    for (int mi = 0; mi < 4; mi++) {
        M = test_ms[mi];
        printf("=== Testing Simply-Primitive Involutory Quandles of Size M = %d ===\n", M);
        fflush(stdout);
        // By Jordan (1871) / Wielandt (1964, Thms 13.3 & 13.5), for M >= 9 any primitive L <= S_M with
        // minimal degree <= 4 contains A_M (hence is 2-transitive), so each generator moves M - f >= 6 points (f <= M - 6).
        int f_max = (M >= 9) ? (M - 6) : (M - 2);
        /* For odd M, f=1 is excluded analytically: the centralizer of a
         * generator has odd index M, so a Sylow 2-subgroup of that
         * centralizer is Sylow in L and the generator is central in it.
         * It commutes with no distinct conjugate, hence is weakly closed
         * in this Sylow subgroup. Glauberman's Z* theorem puts it
         * in the center modulo O_{2'}(L).  Its conjugacy class generates L,
         * hence L/O_{2'}(L) has order at most 2; Feit--Thompson makes L
         * solvable.  A solvable primitive group has prime-power degree,
         * whereas the only odd degrees searched here, 15 and 21, do not.
         * Source: G. Glauberman, J. Algebra 4 (1966), 403--420, Thm. 1;
         * W. Feit and J. Thompson, Pacific J. Math. 13 (1963), 775--1029.
         */
        for (int f = (M % 2 == 0 ? 2 : 3); f <= f_max; f += 2) {
            F_REQ = f;
            nodes_visited = 0;
            solutions_found = 0;
            sample_ord = 0;
            transposition_isomorphic = 0;
            unknown_solutions = 0;
            sf_reps = 0;
            n_seen_sigs = 0;
            for (int y = 0; y < f; y++) G_s0_perm[y] = y;
            for (int y = f; y < M; y += 2) { G_s0_perm[y] = y + 1; G_s0_perm[y + 1] = y; }

            clock_t t0 = clock();
            int perm[MAXM];
            memset(perm, -1, sizeof(perm));
            perm[f] = f;
            gen_sigma_f_dedup(perm, 1, 1, 1);
            printf("  M=%2d f=%2d -> U_orbits=%4ld sols=%3ld sample_|L|=%5ld nodes=%8ld (%.3fs)\n",
                   M, f, sf_reps, solutions_found, sample_ord, nodes_visited,
                   (double)(clock() - t0) / CLOCKS_PER_SEC);
            fflush(stdout);
            if (M == 21 && f == 11) {
                printf("    S7-isomorphic=%ld unknown=%ld\n", transposition_isomorphic, unknown_solutions);
                fflush(stdout);
                if (unknown_solutions || transposition_isomorphic != solutions_found) {
                    fprintf(stderr, "UNCLASSIFIED M=21 f=11 SOLUTION!\n");
                    return 1;
                }
            }
            if (M == 10 && f == 4 && (solutions_found == 0 || sample_ord != 120)) {
                fprintf(stderr, "EXPECTED S_5 (|L|=120) AT M=10 f=4!\n");
                return 1;
            }
            if (M == 15 && f == 7 && (solutions_found == 0 || sample_ord != 720)) {
                fprintf(stderr, "EXPECTED S_6 (|L|=720) AT M=15 f=7!\n");
                return 1;
            }
            if (M == 21 && f != 11 && solutions_found != 0) {
                fprintf(stderr, "UNEXPECTED HIT AT M=21 f=%d\n", f);
                return 1;
            }
            if (M == 21 && f == 11 && (solutions_found == 0 || sample_ord != 5040)) {
                fprintf(stderr, "EXPECTED S_7 (|L|=5040) AT M=21 f=11!\n");
                return 1;
            }
            if (M == 24 && solutions_found != 0) {
                fprintf(stderr, "UNEXPECTED HIT AT M=24 f=%d\n", f);
                return 1;
            }
        }
    }
    printf("\nALL QUANDLE CHECKS PASSED in %.3fs! Only M=21 f=11 (S_7, |L|=5040) exists at M in {21, 24}.\n",
           (double)(clock() - t_all) / CLOCKS_PER_SEC);
    return 0;
}
