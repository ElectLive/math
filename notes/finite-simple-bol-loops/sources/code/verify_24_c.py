#!/usr/bin/env python3
"""
C-accelerated exact deterministic certificate for Sub-Target 2D.1 (100% CFSG-free):
1. Certifies n = 20 (4, D10) [both P_3 = 0 and dim P_3 = 1] -> 0 simple proper left Bol loops.
2. Certifies ALL imprimitive maximal-subgroup chains at n = 24 -> every simple proper left Bol loop
   of order 24 is explicitly isomorphic to canonical Q_24 = Q_(S_4, C_4, S_3) (C0001 Remark 2.3).

Note on element orders in a simple proper left Bol loop Q of order n:
- d = n is associative (cyclic group C_n).
- d = n/2 (when n is even) generates an index-2 subloop S = <x> <= Q; in ANY finite loop of order 2m,
  any subloop S of order m is automatically normal with quotient C_2 (Latin-square block partition
  Q = S uplus B: L_s(S)=S => L_s(B)=B, R_s(S)=S => R_s(B)=B, hence R_b(S)=B => R_b(B)=S).
Thus every nontrivial element of a simple proper left Bol loop of order n has semiregular order
d | n with 1 < d < n and d != n/2 (for n = 24: d in {2, 3, 4, 6, 8}; for n = 20: d in {2, 4, 5}).
"""

import ctypes
import os
import shutil
import subprocess
import tempfile
import time
from collections import deque
from math import gcd


C_SOLVER_SRC = r"""
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

#define MAX_M0 1152
#define MWORDS 18
#define MAX_C 10
#define MAX_B 8
#define MAX_N 24
#define MAX_DIVS 8
#define MAX_KB 32
#define MAX_HITS 2048
#define MAX_VECS 65536

typedef struct { uint64_t w[MWORDS]; } Mask;

static inline void mask_zero(Mask *m) { for (int i = 0; i < MWORDS; i++) m->w[i] = 0; }
static inline void mask_and(Mask *a, const Mask *b) { for (int i = 0; i < MWORDS; i++) a->w[i] &= b->w[i]; }
static inline void mask_or_bit(Mask *a, int bit) { a->w[bit >> 6] |= (1ULL << (bit & 63)); }
static inline int mask_test(const Mask *a, int bit) { return (int)((a->w[bit >> 6] >> (bit & 63)) & 1ULL); }
static inline int mask_nonzero(const Mask *a) {
    uint64_t x = 0;
    for (int i = 0; i < MWORDS; i++) x |= a->w[i];
    return x != 0;
}
static inline int mask_popcnt(const Mask *a) {
    int s = 0;
    for (int i = 0; i < MWORDS; i++) s += __builtin_popcountll(a->w[i]);
    return s;
}

typedef struct {
    int16_t f[MAX_C];
    int8_t s[MAX_C];
} WElem;

/* Global problem instance */
static int G_m0, G_b, G_c, G_n;
static int16_t G_mul[MAX_M0][MAX_M0];
static int16_t G_inv[MAX_M0];
static int8_t G_eval[MAX_M0][MAX_B];
static Mask G_all_mask;
static Mask G_der_mask[MAX_M0];
static Mask G_mask_by_x0[MAX_B];
static Mask G_mask_x_nonzero[MAX_B];

static int G_has_cosets;
static int G_num_cids;
static int8_t G_coset_of[MAX_M0];
static Mask G_coset_masks[8];

static int G_num_divs;
static int G_divs[MAX_DIVS]; // valid loop element orders d > 1
static Mask G_by_qord_mask[MAX_N + 1];
static int G_by_qord_cnt[MAX_N + 1];
static int16_t G_by_qord_list[MAX_N + 1][MAX_M0];

static int G_kb_size;
static int8_t G_kbar[MAX_KB][MAX_C];
static int G_kb_by_j_cnt[MAX_C];
static int G_kb_by_j_idx[MAX_C][MAX_KB];

/* Cycle decomposition of each sigma in G_kbar */
static int G_kb_ncyc[MAX_KB];
static int G_kb_cyclen[MAX_KB][MAX_C];
static int8_t G_kb_cyc[MAX_KB][MAX_C][MAX_C];
static int8_t G_kb_pre0[MAX_KB];

static int16_t G_s0[MAX_B];
static int G_s0_ords[MAX_B];

static int G_num_hits;
static uint8_t G_hit_tables[MAX_HITS][MAX_N * MAX_N];

static inline int find_kb_idx(const int8_t s[MAX_C]) {
    for (int k = 0; k < G_kb_size; k++) {
        int eq = 1;
        for (int i = 0; i < G_c; i++) if (G_kbar[k][i] != s[i]) { eq = 0; break; }
        if (eq) return k;
    }
    return -1;
}

static inline int w_eq(const WElem *a, const WElem *b) {
    for (int i = 0; i < G_c; i++) if (a->f[i] != b->f[i] || a->s[i] != b->s[i]) return 0;
    return 1;
}

static inline void w_mul(const WElem *w1, const WElem *w2, WElem *out) {
    for (int i = 0; i < G_c; i++) {
        int s2i = w2->s[i];
        out->f[i] = G_mul[w1->f[s2i]][w2->f[i]];
        out->s[i] = w1->s[s2i];
    }
}

static inline void w_inv(const WElem *w, WElem *out) {
    for (int i = 0; i < G_c; i++) {
        int si = w->s[i];
        out->s[si] = (int8_t)i;
        out->f[si] = G_inv[w->f[i]];
    }
}

static inline int w_quot_semireg(const WElem *w1, const WElem *w2) {
    int inv_s1[MAX_C];
    for (int i = 0; i < G_c; i++) inv_s1[w1->s[i]] = i;
    int p[MAX_N];
    for (int i = 0; i < G_c; i++) {
        int j = w2->s[i];
        int i2 = inv_s1[j];
        int f_comb = G_mul[G_inv[w1->f[i2]]][w2->f[i]];
        for (int x = 0; x < G_b; x++) {
            int u = i * G_b + x;
            int v = i2 * G_b + G_eval[f_comb][x];
            if (u == v) return 0;
            p[u] = v;
        }
    }
    uint32_t vis = 0;
    int req_len = 0;
    for (int u = 0; u < G_n; u++) {
        if ((vis >> u) & 1u) continue;
        int len = 0, cur = u;
        while (!((vis >> cur) & 1u)) {
            vis |= (1u << cur);
            cur = p[cur];
            len++;
        }
        if (req_len == 0) req_len = len;
        else if (len != req_len) return 0;
    }
    return 1;
}

static inline int w_is_derang(const WElem *w1, const WElem *w2) {
    for (int i = 0; i < G_c; i++) {
        if (w1->s[i] == w2->s[i]) {
            if (!mask_test(&G_der_mask[w1->f[i]], w2->f[i])) return 0;
        }
    }
    return 1;
}

static int w_semireg_valid(const WElem *w) {
    int kbi = find_kb_idx(w->s);
    if (kbi < 0) return -1;
    int d_req = -1;
    int nc = G_kb_ncyc[kbi];
    for (int ci = 0; ci < nc; ci++) {
        int ln = G_kb_cyclen[kbi][ci];
        int prod = 0;
        for (int s = 0; s < ln; s++) {
            int bi = G_kb_cyc[kbi][ci][s];
            prod = G_mul[w->f[bi]][prod];
        }
        int q_found = -1;
        for (int q = 1; q <= G_b; q++) {
            if (G_by_qord_cnt[q] > 0 && mask_test(&G_by_qord_mask[q], prod)) {
                q_found = q;
                break;
            }
        }
        if (q_found < 0) return -1;
        int d_here = ln * q_found;
        if (d_req < 0) d_req = d_here;
        else if (d_req != d_here) return -1;
    }
    for (int di = 0; di < G_num_divs; di++) {
        if (G_divs[di] == d_req) return kbi;
    }
    return -1;
}

typedef struct {
    uint32_t known_mask;
    WElem k_map[MAX_N];
    int8_t kb_idx_of[MAX_N];
} SearchState;

static int check_and_close(SearchState *st, int start_q[MAX_N], int q_len) {
    int q[MAX_N * 4];
    int qh = 0, qt = 0;
    for (int i = 0; i < q_len; i++) q[qt++] = start_q[i];

    while (qh < qt) {
        int u = q[qh++];
        const WElem *ku = &st->k_map[u];
        int kbi = st->kb_idx_of[u];
        if (kbi < 0) return 0;
        if (G_has_cosets) {
            int c0 = G_coset_of[ku->f[0]];
            for (int i = 1; i < G_c; i++) if (G_coset_of[ku->f[i]] != c0) return 0;
        }
        if (u < G_b && ku->f[0] != G_s0[u]) return 0;

        uint32_t km = st->known_mask;
        for (int v = 0; v < G_n; v++) {
            if (v != u && ((km >> v) & 1u)) {
                if (!w_quot_semireg(ku, &st->k_map[v])) return 0;
            }
        }

        WElem iku;
        w_inv(ku, &iku);
        int iu = iku.s[0] * G_b + G_eval[iku.f[0]][0];
        if ((st->known_mask >> iu) & 1u) {
            if (!w_eq(&st->k_map[iu], &iku)) return 0;
        } else {
            if (iu == 0) return 0;
            int ikbi = w_semireg_valid(&iku);
            if (ikbi < 0) return 0;
            st->known_mask |= (1u << iu);
            st->k_map[iu] = iku;
            st->kb_idx_of[iu] = (int8_t)ikbi;
            q[qt++] = iu;
        }

        uint32_t snap = st->known_mask;
        for (int v = 0; v < G_n; v++) {
            if (!((snap >> v) & 1u)) continue;
            const WElem *kv = &st->k_map[v];
            for (int dir = 0; dir < 2; dir++) {
                const WElem *g1 = (dir == 0) ? ku : kv;
                const WElem *g2 = (dir == 0) ? kv : ku;
                WElem tmp, gz;
                w_mul(g2, g1, &tmp);
                w_mul(g1, &tmp, &gz);
                int z = gz.s[0] * G_b + G_eval[gz.f[0]][0];
                if ((st->known_mask >> z) & 1u) {
                    if (!w_eq(&st->k_map[z], &gz)) return 0;
                } else {
                    if (z == 0) return 0;
                    int zkbi = w_semireg_valid(&gz);
                    if (zkbi < 0) return 0;
                    st->known_mask |= (1u << z);
                    st->k_map[z] = gz;
                    st->kb_idx_of[z] = (int8_t)zkbi;
                    q[qt++] = z;
                }
            }
        }
    }

    // Check remaining block capacity vs missing kbar elements per block j
    for (int j = 0; j < G_c; j++) {
        uint32_t used_kb = 0;
        int cnt_j = 0;
        for (int x = 0; x < G_b; x++) {
            int u = j * G_b + x;
            if ((st->known_mask >> u) & 1u) {
                cnt_j++;
                used_kb |= (1u << st->kb_idx_of[u]);
            }
        }
        int miss = 0;
        for (int t = 0; t < G_kb_by_j_cnt[j]; t++) {
            int kbi = G_kb_by_j_idx[j][t];
            if (!((used_kb >> kbi) & 1u)) miss++;
        }
        if (G_b - cnt_j < miss) return 0;
    }
    return 1;
}

static int eval_point(
    const SearchState *st,
    int z,
    const Mask forb_x_mask[MAX_C],
    int count_only,
    int limit,
    WElem *out_cands,
    int8_t *out_kbis,
    int max_out
) {
    int jz = z / G_b, xz = z % G_b;
    uint32_t used_kb = 0;
    int cnt_jz = 0;
    for (int x = 0; x < G_b; x++) {
        int u = jz * G_b + x;
        if ((st->known_mask >> u) & 1u) {
            cnt_jz++;
            used_kb |= (1u << st->kb_idx_of[u]);
        }
    }
    int miss_list[MAX_KB], n_miss = 0;
    for (int t = 0; t < G_kb_by_j_cnt[jz]; t++) {
        int kbi = G_kb_by_j_idx[jz][t];
        if (!((used_kb >> kbi) & 1u)) miss_list[n_miss++] = kbi;
    }
    if (G_b - cnt_jz < n_miss) return 0;

    int tau_list[MAX_KB], n_tau = 0;
    if (G_b - cnt_jz == n_miss) {
        for (int t = 0; t < n_miss; t++) tau_list[n_tau++] = miss_list[t];
    } else {
        for (int t = 0; t < G_kb_by_j_cnt[jz]; t++) tau_list[n_tau++] = G_kb_by_j_idx[jz][t];
    }

    int total_cnt = 0;

    for (int ti_idx = 0; ti_idx < n_tau; ti_idx++) {
        int kbi = tau_list[ti_idx];
        const int8_t *tau = G_kbar[kbi];
        int i_pre0 = G_kb_pre0[kbi];
        int nc = G_kb_ncyc[kbi];

        int d_list[MAX_DIVS], n_d = 0;
        if (jz == 0) {
            d_list[n_d++] = G_s0_ords[xz];
        } else {
            for (int di = 0; di < G_num_divs; di++) {
                int d = G_divs[di];
                int ok_d = 1;
                for (int ci = 0; ci < nc; ci++) {
                    int ln = G_kb_cyclen[kbi][ci];
                    if (d % ln != 0 || G_by_qord_cnt[d / ln] == 0) { ok_d = 0; break; }
                }
                if (ok_d) d_list[n_d++] = d;
            }
        }
        if (n_d == 0) continue;

        int cid_list[8], n_cid = 0;
        if (!G_has_cosets) {
            cid_list[n_cid++] = -1;
        } else if (jz == 0) {
            cid_list[n_cid++] = G_coset_of[G_s0[xz]];
        } else {
            for (int c = 0; c < G_num_cids; c++) {
                Mask tmp = G_coset_masks[c];
                mask_and(&tmp, &G_mask_by_x0[xz]);
                if (mask_nonzero(&tmp)) cid_list[n_cid++] = c;
            }
        }

        for (int c_idx = 0; c_idx < n_cid; c_idx++) {
            int cid_req = cid_list[c_idx];
            Mask allowed[MAX_C];
            int possible = 1;
            for (int i = 0; i < G_c; i++) {
                int ti = tau[i];
                Mask pm;
                if (i == 0) {
                    if (jz == 0) { mask_zero(&pm); mask_or_bit(&pm, G_s0[xz]); }
                    else pm = G_mask_by_x0[xz];
                } else {
                    pm = G_all_mask;
                }
                if (cid_req >= 0) mask_and(&pm, &G_coset_masks[cid_req]);
                if (i == i_pre0) mask_and(&pm, &forb_x_mask[i]);

                for (int u = 0; u < G_n; u++) {
                    if (!((st->known_mask >> u) & 1u)) continue;
                    const WElem *ku = &st->k_map[u];
                    if (ku->s[i] == ti) {
                        mask_and(&pm, &G_der_mask[ku->f[i]]);
                    }
                    if (ku->s[0] == i && ku->s[ti] == 0) {
                        int inv_l = G_inv[ku->f[ti]];
                        int inv_r = G_inv[ku->f[0]];
                        Mask sm; mask_zero(&sm);
                        for (int bx = 0; bx < G_b; bx++) {
                            mask_or_bit(&sm, G_mul[inv_l][G_mul[G_s0[bx]][inv_r]]);
                        }
                        mask_and(&pm, &sm);
                    }
                    if (jz == 0 && ti == 0 && i != 0 && ku->s[0] == i) {
                        int rhs_i = G_inv[G_mul[ku->f[0]][G_s0[xz]]];
                        Mask sm2; mask_zero(&sm2);
                        for (int bx = 0; bx < G_b; bx++) {
                            mask_or_bit(&sm2, G_mul[G_s0[bx]][rhs_i]);
                        }
                        mask_and(&pm, &sm2);
                    }
                    if (!mask_nonzero(&pm)) break;
                }
                if (!mask_nonzero(&pm)) { possible = 0; break; }
                allowed[i] = pm;
            }
            if (!possible) continue;

            int16_t allowed_lst[MAX_C][MAX_M0];
            int allowed_len[MAX_C];
            for (int i = 0; i < G_c; i++) {
                int cnt = 0;
                for (int w = 0; w < MWORDS; w++) {
                    uint64_t bits = allowed[i].w[w];
                    while (bits) {
                        int bpos = __builtin_ctzll(bits);
                        allowed_lst[i][cnt++] = (int16_t)((w << 6) + bpos);
                        bits &= bits - 1;
                    }
                }
                allowed_len[i] = cnt;
            }

            for (int di = 0; di < n_d; di++) {
                int d = d_list[di];
                if (count_only) {
                    long long prod_cnt = 1;
                    int ok_d = 1;
                    for (int ci = 0; ci < nc; ci++) {
                        int ln = G_kb_cyclen[kbi][ci];
                        int q_ord = d / ln;
                        long long cy_cnt = 0;
                        if (ln == 1) {
                            Mask m = allowed[G_kb_cyc[kbi][ci][0]];
                            mask_and(&m, &G_by_qord_mask[q_ord]);
                            cy_cnt = mask_popcnt(&m);
                        } else if (ln == 2) {
                            int b0 = G_kb_cyc[kbi][ci][0], b1 = G_kb_cyc[kbi][ci][1];
                            const Mask *las = &allowed[b1];
                            int rcnt = G_by_qord_cnt[q_ord];
                            const int16_t *rlst = G_by_qord_list[q_ord];
                            for (int a0 = 0; a0 < allowed_len[b0]; a0++) {
                                int ips = G_inv[allowed_lst[b0][a0]];
                                for (int ri = 0; ri < rcnt; ri++) {
                                    if (mask_test(las, G_mul[rlst[ri]][ips])) cy_cnt++;
                                }
                            }
                        } else {
                            // General ln >= 3: count partial products by element index 0..G_m0-1!
                            int cur_cnt[MAX_M0], nxt_cnt[MAX_M0];
                            memset(cur_cnt, 0, sizeof(int) * G_m0);
                            cur_cnt[0] = 1;
                            for (int s = 0; s < ln - 1; s++) {
                                int bi = G_kb_cyc[kbi][ci][s];
                                memset(nxt_cnt, 0, sizeof(int) * G_m0);
                                for (int ps = 0; ps < G_m0; ps++) {
                                    int cval = cur_cnt[ps];
                                    if (!cval) continue;
                                    for (int ai = 0; ai < allowed_len[bi]; ai++) {
                                        int g = allowed_lst[bi][ai];
                                        nxt_cnt[G_mul[g][ps]] += cval;
                                    }
                                }
                                memcpy(cur_cnt, nxt_cnt, sizeof(int) * G_m0);
                            }
                            int lb = G_kb_cyc[kbi][ci][ln - 1];
                            const Mask *las = &allowed[lb];
                            int rcnt = G_by_qord_cnt[q_ord];
                            const int16_t *rlst = G_by_qord_list[q_ord];
                            for (int ps = 0; ps < G_m0; ps++) {
                                int cval = cur_cnt[ps];
                                if (!cval) continue;
                                int ips = G_inv[ps];
                                for (int ri = 0; ri < rcnt; ri++) {
                                    if (mask_test(las, G_mul[rlst[ri]][ips])) cy_cnt += cval;
                                }
                            }
                        }
                        if (cy_cnt == 0) { ok_d = 0; break; }
                        prod_cnt *= cy_cnt;
                        if (prod_cnt > 1000000000LL) prod_cnt = 1000000000LL;
                    }
                    if (ok_d) {
                        total_cnt += (prod_cnt > 1000000000LL ? 1000000000 : (int)prod_cnt);
                        if (total_cnt >= limit) return total_cnt;
                    }
                } else {
                    // Materialize candidates recursively over cycles ci = 0..nc-1
                    WElem base_w;
                    for (int i = 0; i < G_c; i++) { base_w.f[i] = 0; base_w.s[i] = tau[i]; }

                    // Dynamically-grown heap cycle enumeration (zero truncation, zero fixed cap!)
                    typedef struct { int16_t f[MAX_C]; } FVec;
                    size_t cap_cur = 4096, cap_cy = 4096;
                    FVec *cur_vecs = (FVec *)malloc(sizeof(FVec) * cap_cur);
                    int16_t (*cy_tuples)[MAX_C] = malloc(sizeof(int16_t[MAX_C]) * cap_cy);
                    int n_vecs = 1;
                    memset(&cur_vecs[0], 0, sizeof(FVec));
                    int ok_d = 1;

                    for (int ci = 0; ci < nc; ci++) {
                        int ln = G_kb_cyclen[kbi][ci];
                        int q_ord = d / ln;
                        int n_cy = 0;

                        if (ln == 1) {
                            int i0 = G_kb_cyc[kbi][ci][0];
                            for (int ai = 0; ai < allowed_len[i0]; ai++) {
                                int16_t g = allowed_lst[i0][ai];
                                if (mask_test(&G_by_qord_mask[q_ord], g)) {
                                    if ((size_t)n_cy >= cap_cy) {
                                        cap_cy *= 2;
                                        cy_tuples = realloc(cy_tuples, sizeof(int16_t[MAX_C]) * cap_cy);
                                    }
                                    cy_tuples[n_cy++][0] = g;
                                }
                            }
                        } else {
                            int idx_stack[MAX_C];
                            int prod_stack[MAX_C];
                            memset(idx_stack, 0, sizeof(idx_stack));
                            prod_stack[0] = 0;
                            int depth = 0;
                            while (depth >= 0) {
                                if (depth == ln - 1) {
                                    int lb = G_kb_cyc[kbi][ci][ln - 1];
                                    int ips = G_inv[prod_stack[ln - 1]];
                                    int rcnt = G_by_qord_cnt[q_ord];
                                    const int16_t *rlst = G_by_qord_list[q_ord];
                                    for (int ri = 0; ri < rcnt; ri++) {
                                        int16_t fl = G_mul[rlst[ri]][ips];
                                        if (mask_test(&allowed[lb], fl)) {
                                            if ((size_t)n_cy >= cap_cy) {
                                                cap_cy *= 2;
                                                cy_tuples = realloc(cy_tuples, sizeof(int16_t[MAX_C]) * cap_cy);
                                            }
                                            for (int s = 0; s < ln - 1; s++) {
                                                int bi = G_kb_cyc[kbi][ci][s];
                                                cy_tuples[n_cy][s] = allowed_lst[bi][idx_stack[s]];
                                            }
                                            cy_tuples[n_cy][ln - 1] = fl;
                                            n_cy++;
                                        }
                                    }
                                    depth--;
                                    if (depth >= 0) idx_stack[depth]++;
                                } else {
                                    int bi = G_kb_cyc[kbi][ci][depth];
                                    if (idx_stack[depth] >= allowed_len[bi]) {
                                        idx_stack[depth] = 0;
                                        depth--;
                                        if (depth >= 0) idx_stack[depth]++;
                                    } else {
                                        int16_t g = allowed_lst[bi][idx_stack[depth]];
                                        prod_stack[depth + 1] = G_mul[g][prod_stack[depth]];
                                        depth++;
                                    }
                                }
                            }
                        }

                        if (n_cy == 0) { ok_d = 0; break; }
                        size_t need_nxt = (size_t)n_vecs * (size_t)n_cy;
                        FVec *nxt_vecs = (FVec *)malloc(sizeof(FVec) * (need_nxt > 0 ? need_nxt : 1));
                        int n_nxt = 0;
                        for (int vi = 0; vi < n_vecs; vi++) {
                            for (int ti2 = 0; ti2 < n_cy; ti2++) {
                                FVec fv = cur_vecs[vi];
                                for (int s = 0; s < ln; s++) {
                                    fv.f[G_kb_cyc[kbi][ci][s]] = cy_tuples[ti2][s];
                                }
                                nxt_vecs[n_nxt++] = fv;
                            }
                        }
                        free(cur_vecs);
                        cur_vecs = nxt_vecs;
                        n_vecs = n_nxt;
                    }

                    if (ok_d) {
                        for (int vi = 0; vi < n_vecs; vi++) {
                            if (total_cnt >= max_out) { fprintf(stderr, "OVERFLOW out_cands %d >= %d\n", total_cnt, max_out); abort(); }
                            WElem w = base_w;
                            for (int i = 0; i < G_c; i++) w.f[i] = cur_vecs[vi].f[i];
                            out_cands[total_cnt] = w;
                            out_kbis[total_cnt] = (int8_t)kbi;
                            total_cnt++;
                        }
                    }
                    free(cur_vecs);
                    free(cy_tuples);
                }
            }
        }
    }
    return total_cnt;
}

static int check_simple_nonassoc_hit(const SearchState *st) {
    uint8_t tab[MAX_N][MAX_N];
    for (int u = 0; u < G_n; u++) {
        const WElem *ku = &st->k_map[u];
        for (int i = 0; i < G_c; i++) {
            int base = ku->s[i] * G_b;
            int16_t fi = ku->f[i];
            int src = i * G_b;
            for (int x = 0; x < G_b; x++) {
                tab[u][src + x] = (uint8_t)(base + G_eval[fi][x]);
            }
        }
    }
    // Nonassociative check
    int nonassoc = 0;
    for (int x = 0; x < G_n && !nonassoc; x++) {
        for (int y = 0; y < G_n && !nonassoc; y++) {
            int xy = tab[x][y];
            for (int z = 0; z < G_n; z++) {
                if (tab[x][tab[y][z]] != tab[xy][z]) { nonassoc = 1; break; }
            }
        }
    }
    if (!nonassoc) return 0;

    // Simplicity check via Mlt(Q) congruences
    uint8_t gens[2 * MAX_N][MAX_N];
    for (int x = 0; x < G_n; x++) {
        for (int y = 0; y < G_n; y++) {
            gens[x][y] = tab[x][y];
            gens[G_n + y][x] = tab[x][y];
        }
    }
    for (int a = 1; a < G_n; a++) {
        int par[MAX_N];
        for (int i = 0; i < G_n; i++) par[i] = i;
        int q[MAX_N * MAX_N][2], qh = 0, qt = 0, ncomp = G_n;
        par[a] = 0; ncomp--;
        q[qt][0] = 0; q[qt][1] = a; qt++;
        while (qh < qt && ncomp > 1) {
            int u = q[qh][0], v = q[qh][1]; qh++;
            for (int g = 0; g < 2 * G_n; g++) {
                int gu = gens[g][u], gv = gens[g][v];
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

    if (G_num_hits < MAX_HITS) {
        for (int x = 0; x < G_n; x++) {
            for (int y = 0; y < G_n; y++) {
                G_hit_tables[G_num_hits][x * G_n + y] = tab[x][y];
            }
        }
    }
    G_num_hits++;
    return 1;
}

static void dfs(const SearchState *st) {
    if (st->known_mask == ((1u << G_n) - 1u)) {
        uint32_t all_kb = 0;
        for (int u = 0; u < G_n; u++) all_kb |= (1u << st->kb_idx_of[u]);
        if (all_kb == ((1u << G_kb_size) - 1u)) {
            check_simple_nonassoc_hit(st);
        }
        return;
    }

    Mask forb_x_mask[MAX_C];
    for (int j = 0; j < G_c; j++) forb_x_mask[j] = G_all_mask;
    for (int u = 0; u < G_n; u++) {
        if ((st->known_mask >> u) & 1u) {
            mask_and(&forb_x_mask[u / G_b], &G_mask_x_nonzero[u % G_b]);
        }
    }

    int rem[MAX_N], n_rem = 0;
    for (int pass = 0; pass < 3; pass++) {
        for (int u = 1; u < G_n; u++) {
            if ((st->known_mask >> u) & 1u) continue;
            int cat = (u % G_b == 0) ? 0 : ((u < G_b) ? 1 : 2);
            if (cat == pass) rem[n_rem++] = u;
        }
    }

    int best_z = -1, best_cnt = 1000000000;
    for (int ri = 0; ri < n_rem; ri++) {
        int u = rem[ri];
        int cu = eval_point(st, u, forb_x_mask, 1, best_cnt, NULL, NULL, 0);
        if (cu == 0) return;
        if (cu < best_cnt) {
            best_z = u;
            best_cnt = cu;
            if (best_cnt == 1) break;
        }
    }

    WElem *cands = (WElem *)malloc(sizeof(WElem) * (best_cnt + 4));
    int8_t *kbis = (int8_t *)malloc(sizeof(int8_t) * (best_cnt + 4));
    int nc = eval_point(st, best_z, forb_x_mask, 0, best_cnt + 4, cands, kbis, best_cnt + 4);
    for (int ci = 0; ci < nc; ci++) {
        SearchState nxt = *st;
        nxt.known_mask |= (1u << best_z);
        nxt.k_map[best_z] = cands[ci];
        nxt.kb_idx_of[best_z] = kbis[ci];
        int sq[1] = { best_z };
        if (check_and_close(&nxt, sq, 1)) {
            dfs(&nxt);
        }
    }
    free(cands);
    free(kbis);
}

/* Each source table has MAX_N^2 storage, while the caller expects packed n^2 tables. */
void copy_hit_tables(uint8_t *out, const uint8_t *in, int n, int count) {
    for (int i = 0; i < count; i++) {
        memcpy(out + (size_t)i * n * n,
               in + (size_t)i * MAX_N * MAX_N, (size_t)n * n);
    }
}

int solve_kbar_s0_c(
    int m0, int b, int c,
    const int16_t *mul_flat,
    const int16_t *inv_arr,
    const int8_t *eval_flat,
    const int8_t *der_flat,
    const int8_t *semireg_qord,
    int has_cosets, int num_cids, const int8_t *coset_of_arr,
    int num_divs, const int *divs_arr,
    int kb_size, const int8_t *kbar_flat,
    const int16_t *s0_arr, const int *s0_ords_arr,
    int num_w1s, const int16_t *w1_f_flat, const int8_t *w1_s_flat,
    uint8_t *out_tables, int max_out_tables
) {
    G_m0 = m0; G_b = b; G_c = c; G_n = b * c;
    mask_zero(&G_all_mask);
    for (int i = 0; i < m0; i++) mask_or_bit(&G_all_mask, i);

    for (int x = 0; x < b; x++) {
        mask_zero(&G_mask_by_x0[x]);
        mask_zero(&G_mask_x_nonzero[x]);
    }
    for (int q = 0; q <= G_n; q++) {
        mask_zero(&G_by_qord_mask[q]);
        G_by_qord_cnt[q] = 0;
    }

    for (int i = 0; i < m0; i++) {
        G_inv[i] = inv_arr[i];
        for (int x = 0; x < b; x++) {
            int8_t v = eval_flat[i * b + x];
            G_eval[i][x] = v;
            if (x == 0) mask_or_bit(&G_mask_by_x0[v], i);
            if (v != 0) mask_or_bit(&G_mask_x_nonzero[x], i);
        }
        mask_zero(&G_der_mask[i]);
        for (int j = 0; j < m0; j++) {
            G_mul[i][j] = mul_flat[i * m0 + j];
            if (der_flat[i * m0 + j]) mask_or_bit(&G_der_mask[i], j);
        }
        int q = semireg_qord[i];
        if (q > 0) {
            mask_or_bit(&G_by_qord_mask[q], i);
            G_by_qord_list[q][G_by_qord_cnt[q]++] = (int16_t)i;
        }
    }

    G_has_cosets = has_cosets;
    G_num_cids = num_cids;
    if (has_cosets) {
        for (int cid = 0; cid < num_cids; cid++) mask_zero(&G_coset_masks[cid]);
        for (int i = 0; i < m0; i++) {
            G_coset_of[i] = coset_of_arr[i];
            mask_or_bit(&G_coset_masks[coset_of_arr[i]], i);
        }
    }

    G_num_divs = num_divs;
    for (int i = 0; i < num_divs; i++) G_divs[i] = divs_arr[i];

    G_kb_size = kb_size;
    for (int j = 0; j < c; j++) G_kb_by_j_cnt[j] = 0;
    for (int k = 0; k < kb_size; k++) {
        for (int i = 0; i < c; i++) {
            G_kbar[k][i] = kbar_flat[k * c + i];
            if (G_kbar[k][i] == 0) G_kb_pre0[k] = (int8_t)i;
        }
        int j0 = G_kbar[k][0];
        G_kb_by_j_idx[j0][G_kb_by_j_cnt[j0]++] = k;

        int vis[MAX_C] = {0};
        int ncyc = 0;
        // Put cycle containing 0 first:
        for (int pass = 0; pass < 2; pass++) {
            for (int i = 0; i < c; i++) {
                if (vis[i]) continue;
                int cur = i, ln = 0, has0 = 0;
                int tmp[MAX_C];
                while (!vis[cur]) {
                    vis[cur] = 1;
                    if (cur == 0) has0 = 1;
                    tmp[ln++] = cur;
                    cur = G_kbar[k][cur];
                }
                if ((pass == 0 && has0) || (pass == 1 && !has0)) {
                    G_kb_cyclen[k][ncyc] = ln;
                    for (int s = 0; s < ln; s++) G_kb_cyc[k][ncyc][s] = (int8_t)tmp[s];
                    ncyc++;
                } else {
                    for (int s = 0; s < ln; s++) vis[tmp[s]] = 0;
                }
            }
        }
        G_kb_ncyc[k] = ncyc;
    }

    for (int x = 0; x < b; x++) {
        G_s0[x] = s0_arr[x];
        G_s0_ords[x] = s0_ords_arr[x];
    }

    G_num_hits = 0;
    WElem id_w;
    for (int i = 0; i < c; i++) { id_w.f[i] = 0; id_w.s[i] = (int8_t)i; }
    int id_kbi = find_kb_idx(id_w.s);

    for (int wi = 0; wi < num_w1s; wi++) {
        WElem w1;
        for (int i = 0; i < c; i++) {
            w1.f[i] = w1_f_flat[wi * c + i];
            w1.s[i] = w1_s_flat[wi * c + i];
        }
        int w1_kbi = w_semireg_valid(&w1);
        if (w1_kbi < 0) continue;

        SearchState st;
        memset(&st, 0, sizeof(st));
        st.known_mask = (1u << 0) | (1u << b);
        st.k_map[0] = id_w;
        st.kb_idx_of[0] = (int8_t)id_kbi;
        st.k_map[b] = w1;
        st.kb_idx_of[b] = (int8_t)w1_kbi;
        int sq[2] = { 0, b };
        if (check_and_close(&st, sq, 2)) {
            dfs(&st);
        }
    }

    int ncopy = (G_num_hits < max_out_tables) ? G_num_hits : max_out_tables;
    if (ncopy > 0) {
        copy_hit_tables(out_tables, &G_hit_tables[0][0], G_n, ncopy);
    }
    return G_num_hits;
}
"""


def compile_c_lib():
    cc = shutil.which("clang") or shutil.which("cc") or shutil.which("gcc")
    if cc is None:
        raise RuntimeError("No C compiler (clang/cc/gcc) found on PATH")
    tmpdir = tempfile.mkdtemp(prefix="verify24_")
    try:
        c_path = os.path.join(tmpdir, "solver.c")
        so_path = os.path.join(tmpdir, "solver.so")
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(C_SOLVER_SRC)
        subprocess.check_call([cc, "-O3", "-shared", "-fPIC", c_path, "-o", so_path])
        lib = ctypes.CDLL(so_path)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    lib.solve_kbar_s0_c.argtypes = [
        ctypes.c_int, ctypes.c_int, ctypes.c_int,
        ctypes.POINTER(ctypes.c_int16),
        ctypes.POINTER(ctypes.c_int16),
        ctypes.POINTER(ctypes.c_int8),
        ctypes.POINTER(ctypes.c_int8),
        ctypes.POINTER(ctypes.c_int8),
        ctypes.c_int, ctypes.c_int, ctypes.POINTER(ctypes.c_int8),
        ctypes.c_int, ctypes.POINTER(ctypes.c_int),
        ctypes.c_int, ctypes.POINTER(ctypes.c_int8),
        ctypes.POINTER(ctypes.c_int16), ctypes.POINTER(ctypes.c_int),
        ctypes.c_int, ctypes.POINTER(ctypes.c_int16), ctypes.POINTER(ctypes.c_int8),
        ctypes.POINTER(ctypes.c_uint8), ctypes.c_int,
    ]
    lib.solve_kbar_s0_c.restype = ctypes.c_int
    return lib


def perm_mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inv(p):
    inv = [0] * len(p)
    for i, v in enumerate(p):
        inv[v] = i
    return tuple(inv)


def is_derangement(p, q):
    return all(a != b for a, b in zip(p, q))


def is_semiregular(p):
    n = len(p)
    if p == tuple(range(n)):
        return True
    vis = [False] * n
    L = None
    for i in range(n):
        if not vis[i]:
            c = 0
            cur = i
            while not vis[cur]:
                vis[cur] = True
                cur = p[cur]
                c += 1
            if L is None:
                L = c
            elif c != L:
                return False
    return L > 1 and (n % L == 0)


def perm_order_general(p):
    n = len(p)
    vis = [False] * n
    ans = 1
    for i in range(n):
        if not vis[i]:
            c = 0
            cur = i
            while not vis[cur]:
                vis[cur] = True
                cur = p[cur]
                c += 1
            ans = ans * c // gcd(ans, c)
    return ans


def gen_group(gens, deg):
    id_p = tuple(range(deg))
    seen = {id_p}
    q = deque([id_p])
    while q:
        cur = q.popleft()
        for g in gens:
            for nxt in (perm_mul(cur, g), perm_mul(g, cur)):
                if nxt not in seen:
                    seen.add(nxt)
                    q.append(nxt)
    return sorted(seen)


def normalizer_in_sym(G, deg):
    G_set = set(G)
    gens = [g for g in G if g != tuple(range(deg))][:6]
    if set(gen_group(gens, deg)) != G_set:
        gens = G
    norm = []
    used = [False] * deg
    part = [0] * deg

    def bt(idx):
        if idx == deg:
            s = tuple(part)
            si = perm_inv(s)
            if all(perm_mul(s, perm_mul(g, si)) in G_set for g in gens):
                norm.append(s)
            return
        for v in range(deg):
            if not used[v]:
                used[v] = True
                part[idx] = v
                bt(idx + 1)
                used[v] = False

    bt(0)
    return norm


def enumerate_s0_reps(P0, b, valid_ds):
    id_b = tuple(range(b))
    P0_set = set(P0)
    P0_stab0 = [h for h in P0 if h[0] == 0]
    by_img0 = [[] for _ in range(b)]
    for g in P0:
        if g != id_b and is_semiregular(g) and perm_order_general(g) in valid_ds:
            by_img0[g[0]].append(g)

    sols = []

    def close_s0(mp):
        q = list(mp.items())
        qi = 0
        while qi < len(q):
            x, gx = q[qi]
            qi += 1
            for y, gy in mp.items():
                if y != x and not is_derangement(gx, gy):
                    return None
            ig = perm_inv(gx)
            ix = ig[0]
            if ix in mp:
                if mp[ix] != ig:
                    return None
            else:
                if not is_semiregular(ig) or perm_order_general(ig) not in valid_ds:
                    return None
                mp[ix] = ig
                q.append((ix, ig))
            for y, gy in list(mp.items()):
                for g1, g2 in ((gx, gy), (gy, gx)):
                    gz = perm_mul(g1, perm_mul(g2, g1))
                    if gz not in P0_set:
                        return None
                    if gz != id_b and (not is_semiregular(gz) or perm_order_general(gz) not in valid_ds):
                        return None
                    z = gz[0]
                    if z in mp:
                        if mp[z] != gz:
                            return None
                    else:
                        mp[z] = gz
                        q.append((z, gz))
        return mp

    def bt(mp):
        if len(mp) == b:
            sols.append(tuple(mp[i] for i in range(b)))
            return
        best_x, best_c = None, None
        for x in range(1, b):
            if x not in mp:
                cands = [g for g in by_img0[x] if all(is_derangement(g, gy) for gy in mp.values())]
                if best_c is None or len(cands) < len(best_c):
                    best_x, best_c = x, cands
        for g in best_c:
            nm = dict(mp)
            nm[best_x] = g
            nm = close_s0(nm)
            if nm is not None:
                bt(nm)

    bt({0: id_b})
    seen = set()
    reps = []
    for s in sols:
        fs_set = frozenset(s)
        if fs_set in seen:
            continue
        reps.append(s)
        for h in P0_stab0:
            ih = perm_inv(h)
            seen.add(frozenset(perm_mul(h, perm_mul(g, ih)) for g in s))
    return reps


def enumerate_kbar_pruned(Ptop, c, b, valid_ds, require_full_ptop=True):
    id_c = tuple(range(c))
    Ptop_set = set(Ptop)

    def valid_el(g):
        if g == id_c:
            return True
        vis = [False] * c
        ls = []
        for i in range(c):
            if not vis[i]:
                cur = i
                ln = 0
                while not vis[cur]:
                    vis[cur] = True
                    cur = g[cur]
                    ln += 1
                ls.append(ln)
        return any(all(d % ln == 0 and (ln * b) % d == 0 for ln in ls) for d in valid_ds)

    pool = [g for g in Ptop if valid_el(g)]
    pool_idx = {g: idx for idx, g in enumerate(pool)}

    def close_set(S):
        S = set(S)
        q = deque(S)
        while q:
            x = q.popleft()
            ix = perm_inv(x)
            if ix not in S:
                if ix not in pool_idx:
                    return None
                S.add(ix)
                q.append(ix)
            for y in list(S):
                for z in (perm_mul(x, perm_mul(y, x)), perm_mul(y, perm_mul(x, y))):
                    if z not in S:
                        if z not in pool_idx:
                            return None
                        S.add(z)
                        q.append(z)
            if len(S) > b * c:
                return None
            cnt = [0] * c
            for g in S:
                cnt[g[0]] += 1
                if cnt[g[0]] > b:
                    return None
        return frozenset(S)

    closed_single = {}
    for g in pool:
        cs = close_set([id_c, g])
        if cs is not None:
            closed_single[g] = cs

    valid_pool = sorted(closed_single.keys(), key=lambda g: pool_idx[g])
    vp_idx = {g: i for i, g in enumerate(valid_pool)}
    m_vp = len(valid_pool)

    compat = [0] * m_vp
    for i in range(m_vp):
        ci = closed_single[valid_pool[i]]
        mask = 0
        for j in range(i + 1, m_vp):
            gj = valid_pool[j]
            if gj in ci or close_set(ci | closed_single[gj]) is not None:
                mask |= (1 << j)
        compat[i] = mask

    explored = set()
    good_kbars = set()

    def is_valid_final(S):
        if len(S) < c + 1:
            return False
        if any(sum(1 for g in S if g[0] == j) == 0 for j in range(c)):
            return False
        gen_S = gen_group(list(S), c)
        if require_full_ptop:
            return len(gen_S) == len(Ptop_set)
        return len({g[0] for g in gen_S}) == c

    def search_kb(S, cand_mask):
        if S in explored:
            return
        explored.add(S)
        if is_valid_final(S):
            good_kbars.add(S)
        cur_mask = cand_mask
        while cur_mask:
            lsb = cur_mask & -cur_mask
            j = lsb.bit_length() - 1
            cur_mask ^= lsb
            gj = valid_pool[j]
            if gj in S:
                continue
            S2 = close_set(S | closed_single[gj])
            if S2 is not None and S2 not in explored:
                nxt_mask = cur_mask & compat[j]
                ok = True
                for x in S2:
                    ix = vp_idx.get(x)
                    if ix is None:
                        ok = False
                        break
                    nxt_mask &= (compat[ix] | ((1 << (ix + 1)) - 1))
                if ok:
                    search_kb(S2, nxt_mask)

    search_kb(frozenset([id_c]), (1 << m_vp) - 1)
    return sorted(good_kbars, key=lambda s: (len(s), sorted(s)))


def is_left_bol(table, n):
    for x in range(n):
        tx = table[x]
        for y in range(n):
            ty = table[y]
            txyx = table[tx[ty[x]]]
            for z in range(n):
                if tx[ty[tx[z]]] != txyx[z]:
                    return False
    return True


def build_canonical_Q24():
    S4 = gen_group([(1, 2, 3, 0), (1, 0, 2, 3)], 4)
    id4 = (0, 1, 2, 3)
    S4 = [id4] + [g for g in S4 if g != id4]
    C4 = set(gen_group([(1, 2, 3, 0)], 4))
    S3 = {g for g in S4 if g[3] == 3}
    table = [[0] * 24 for _ in range(24)]
    for i, x in enumerate(S4):
        ix = perm_inv(x)
        for j, y in enumerate(S4):
            iy = perm_inv(y)
            xy = perm_mul(x, y)
            ix_iy = perm_mul(ix, iy)
            found = None
            for k, z in enumerate(S4):
                if perm_mul(perm_inv(z), xy) in C4 and perm_mul(z, ix_iy) in S3:
                    assert found is None
                    found = k
            assert found is not None
            table[i][j] = found
    assert is_left_bol(table, 24)
    return table


def find_loop_isomorphism(tab1, tab2, n=24):
    ord1 = [perm_order_general(tuple(tab1[x])) for x in range(n)]
    ord2 = [perm_order_general(tuple(tab2[x])) for x in range(n)]
    if sorted(ord1) != sorted(ord2):
        return None
    gens = []
    cur_sub = {0}
    for x in range(1, n):
        if x not in cur_sub:
            gens.append(x)
            q = deque([x])
            cur_sub.add(x)
            while q:
                u = q.popleft()
                for v in list(cur_sub):
                    for w in (tab1[u][v], tab1[v][u]):
                        if w not in cur_sub:
                            cur_sub.add(w)
                            q.append(w)
            if len(cur_sub) == n:
                break

    def try_extend(gen_imgs):
        phi = {0: 0}
        inv_phi = {0: 0}
        q = deque()
        for g, im in zip(gens, gen_imgs):
            if im in inv_phi and inv_phi[im] != g:
                return None
            phi[g] = im
            inv_phi[im] = g
            q.append(g)
        while q:
            u = q.popleft()
            pu = phi[u]
            for v, pv in list(phi.items()):
                for a, b, pa, pb in ((u, v, pu, pv), (v, u, pv, pu)):
                    ab = tab1[a][b]
                    pab = tab2[pa][pb]
                    if ab in phi:
                        if phi[ab] != pab:
                            return None
                    else:
                        if pab in inv_phi or ord1[ab] != ord2[pab]:
                            return None
                        phi[ab] = pab
                        inv_phi[pab] = ab
                        q.append(ab)
        if len(phi) != n:
            return None
        for x in range(n):
            px = phi[x]
            for y in range(n):
                if phi[tab1[x][y]] != tab2[px][phi[y]]:
                    return None
        return tuple(phi[x] for x in range(n))

    cands_per_gen = [[y for y in range(1, n) if ord2[y] == ord1[g]] for g in gens]

    def bt_iso(idx, chosen):
        if idx == len(gens):
            return try_extend(chosen)
        for y in cands_per_gen[idx]:
            if y not in chosen:
                res = bt_iso(idx + 1, chosen + [y])
                if res is not None:
                    return res
        return None

    return bt_iso(0, [])


def solve_chain_c(lib, P0_perms, b, Ptop, c, valid_ds, require_full_ptop=True, custom_kbars=None, coset_id_map=None):
    n = b * c
    id_b_perm = tuple(range(b))
    P0_perms = [id_b_perm] + [g for g in P0_perms if g != id_b_perm]
    m0 = len(P0_perms)
    p0_idx = {g: idx for idx, g in enumerate(P0_perms)}

    mul_t = [[p0_idx[perm_mul(gi, gj)] for gj in P0_perms] for gi in P0_perms]
    inv_t = [p0_idx[perm_inv(gi)] for gi in P0_perms]
    der_flat = [1 if is_derangement(gi, gj) else 0 for gi in P0_perms for gj in P0_perms]
    eval_flat = [x for gi in P0_perms for x in gi]
    semireg_qord = []
    all_by_d_list = {}
    for i, gi in enumerate(P0_perms):
        d = perm_order_general(gi)
        if is_semiregular(gi) and (b % d == 0):
            semireg_qord.append(d)
            all_by_d_list.setdefault(d, []).append(i)
        else:
            semireg_qord.append(0)

    has_cosets = 0
    num_cids = 0
    coset_of_arr = [0] * m0
    if coset_id_map is not None:
        has_cosets = 1
        cids = sorted(set(coset_id_map.values()))
        num_cids = len(cids)
        cid_remap = {cid: k for k, cid in enumerate(cids)}
        coset_of_arr = [cid_remap[coset_id_map[g]] for g in P0_perms]

    kbars = custom_kbars if custom_kbars is not None else enumerate_kbar_pruned(Ptop, c, b, valid_ds, require_full_ptop=require_full_ptop)
    if not kbars:
        return 0, [], {"kbars": 0, "uniq_kbars": 0, "s0": 0}

    norm_Ptop = normalizer_in_sym(Ptop, c)
    norm_Ptop_0 = [h for h in norm_Ptop if h[0] == 0]
    kbar_set_all = set(kbars)
    seen_kb = set()
    uniq_kbars = []
    for kb in kbars:
        if kb in seen_kb:
            continue
        orbit_kb = []
        for h in norm_Ptop_0:
            ih = perm_inv(h)
            kbc = frozenset(perm_mul(h, perm_mul(g, ih)) for g in kb)
            if kbc in kbar_set_all:
                seen_kb.add(kbc)
                orbit_kb.append(kbc)
        best_pair, best_sc = None, None
        for kbc in orbit_kb:
            for sig in kbc:
                if sig[0] == 1:
                    vis = [False] * c
                    ncyc = 0
                    for i in range(c):
                        if not vis[i]:
                            ncyc += 1
                            cur = i
                            while not vis[cur]:
                                vis[cur] = True
                                cur = sig[cur]
                    sc = (ncyc, 0 if sig[1] == 0 else 1, sig)
                    if best_sc is None or sc < best_sc:
                        best_sc = sc
                        best_pair = (kbc, sig)
        uniq_kbars.append(best_pair)

    s0_perm_reps = enumerate_s0_reps(P0_perms, b, valid_ds)
    if not s0_perm_reps:
        return 0, [], {"kbars": len(kbars), "uniq_kbars": len(uniq_kbars), "s0": 0}
    s0_reps = [tuple(p0_idx[g] for g in s) for s in s0_perm_reps]

    cc_by_d_list = {}
    seen_cc = [False] * m0
    for i in range(m0):
        if seen_cc[i]:
            continue
        for h in range(m0):
            seen_cc[mul_t[h][mul_t[i][inv_t[h]]]] = True
        if semireg_qord[i] > 0:
            cc_by_d_list.setdefault(semireg_qord[i], []).append(i)

    c_mul = (ctypes.c_int16 * (m0 * m0))(*[x for row in mul_t for x in row])
    c_inv = (ctypes.c_int16 * m0)(*inv_t)
    c_eval = (ctypes.c_int8 * (m0 * b))(*eval_flat)
    c_der = (ctypes.c_int8 * (m0 * m0))(*der_flat)
    c_sq = (ctypes.c_int8 * m0)(*semireg_qord)
    c_coset = (ctypes.c_int8 * m0)(*coset_of_arr)
    divs_sorted = sorted(valid_ds)
    c_divs = (ctypes.c_int * len(divs_sorted))(*divs_sorted)

    all_hit_loops = []
    total_hits = 0

    for kbar, sigma_star in uniq_kbars:
        vis = [False] * c
        cycs_st = []
        for i in range(c):
            if not vis[i]:
                cur = i
                cyc = []
                while not vis[cur]:
                    vis[cur] = True
                    cyc.append(cur)
                    cur = sigma_star[cur]
                cycs_st.append(tuple(cyc))
        cycs_st.sort(key=lambda cy: 0 not in cy)

        raw_w1s = []
        if not has_cosets:
            for d in divs_sorted:
                cyc_ch = []
                ok = True
                for cyc in cycs_st:
                    ln = len(cyc)
                    pool_d = all_by_d_list if (0 in cyc) else cc_by_d_list
                    if d % ln != 0 or (d // ln) not in pool_d:
                        ok = False
                        break
                    opts = []
                    for rm in pool_d[d // ln]:
                        mp = {u: 0 for u in cyc[:-1]}
                        mp[cyc[-1]] = rm
                        opts.append(mp)
                    cyc_ch.append(opts)
                if not ok:
                    continue
                cp = [{}]
                for opts in cyc_ch:
                    cp = [{**d0, **o} for d0 in cp for o in opts]
                for mp in cp:
                    raw_w1s.append((tuple(mp[j] for j in range(c)), sigma_star))
        else:
            for cid in range(num_cids):
                reps0 = [i for i in range(m0) if coset_of_arr[i] == cid and P0_perms[i][0] == 0]
                assert len(reps0) == 1
                s_rep = reps0[0]
                for d in divs_sorted:
                    cyc_ch = []
                    ok = True
                    for cyc in cycs_st:
                        ln = len(cyc)
                        if d % ln != 0 or (d // ln) not in all_by_d_list:
                            ok = False
                            break
                        prod_s = 0
                        for _ in range(ln - 1):
                            prod_s = mul_t[s_rep][prod_s]
                        inv_ps = inv_t[prod_s]
                        opts = []
                        for rm in all_by_d_list[d // ln]:
                            flast = mul_t[rm][inv_ps]
                            if coset_of_arr[flast] == cid:
                                if ln == 1 and (0 in cyc) and P0_perms[flast][0] != 0:
                                    continue
                                mp = {u: s_rep for u in cyc[:-1]}
                                mp[cyc[-1]] = flast
                                opts.append(mp)
                        if not opts:
                            ok = False
                            break
                        cyc_ch.append(opts)
                    if not ok:
                        continue
                    cp = [{}]
                    for opts in cyc_ch:
                        cp = [{**d0, **o} for d0 in cp for o in opts]
                    for mp in cp:
                        raw_w1s.append((tuple(mp[j] for j in range(c)), sigma_star))
        raw_w1s = sorted(set(raw_w1s))
        if not raw_w1s:
            continue

        kb_sorted = sorted(kbar)
        c_kb = (ctypes.c_int8 * (len(kb_sorted) * c))(*[x for sig in kb_sorted for x in sig])

        for s0 in s0_reps:
            s0_fset = frozenset(s0)
            s0_ords = [perm_order_general(P0_perms[g]) for g in s0]
            if not has_cosets:
                aut_s0 = [
                    h for h in range(m0)
                    if P0_perms[h][0] == 0 and frozenset(mul_t[h][mul_t[g][inv_t[h]]] for g in s0) == s0_fset
                ]
                seen_w1 = set()
                norm_w1s = []
                for w in raw_w1s:
                    if w in seen_w1:
                        continue
                    norm_w1s.append(w)
                    fs_w, sig_w = w
                    for h in aut_s0:
                        ih = inv_t[h]
                        seen_w1.add((tuple(mul_t[h][mul_t[fs_w[j]][ih]] for j in range(c)), sig_w))
            else:
                norm_w1s = raw_w1s

            nw1 = len(norm_w1s)
            c_w1f = (ctypes.c_int16 * (nw1 * c))(*[x for (fw, _) in norm_w1s for x in fw])
            c_w1s = (ctypes.c_int8 * (nw1 * c))(*[x for (_, sw) in norm_w1s for x in sw])
            c_s0 = (ctypes.c_int16 * b)(*s0)
            c_s0_ords = (ctypes.c_int * b)(*s0_ords)
            max_out = 2048
            out_buf = (ctypes.c_uint8 * (max_out * n * n))()

            nhits = lib.solve_kbar_s0_c(
                m0, b, c,
                c_mul, c_inv, c_eval, c_der, c_sq,
                has_cosets, num_cids, c_coset,
                len(divs_sorted), c_divs,
                len(kb_sorted), c_kb,
                c_s0, c_s0_ords,
                nw1, c_w1f, c_w1s,
                out_buf, max_out,
            )
            total_hits += nhits
            for hi in range(min(nhits, max_out)):
                off = hi * n * n
                tab = [[int(out_buf[off + r * n + col]) for col in range(n)] for r in range(n)]
                all_hit_loops.append(tab)

    return total_hits, all_hit_loops, {
        "kbars": len(kbars),
        "uniq_kbars": len(uniq_kbars),
        "s0": len(s0_reps),
    }


def pgl2_5_small_inv_kbars(PGL2_5, PSL2_5):
    """
    Exact top twisted subgroups for c = 6, b = 4, P_top = PGL_2(5) ~= S_5:
    Since N_1 <= S_4^6 is a {2,3}-group, N_1 = Rad(G) is characteristic in G, and G / N_1 = PGL_2(5) ~= S_5.
    Projecting Lambda = tau K modulo Rad(G~) into Aut(A_5) = S_5 gives an S_5-conjugation-invariant subset
    Lambda_bar <= {1} u Inv(S_5) of size <= 24 that does not lie in a single coset of A_5 = PSL_2(5) (C0007 Thm 1.1(3)).
    In S_5 = PGL_2(5): A_5 has unique involution class I_2 of size 15, and S_5 \\ A_5 has unique involution class I_tr
    of size 10. Since 10 + 15 = 25 > 24, Lambda_bar MUST equal {1} u I_tr (size 11), and K_bar = tau_bar * Lambda_bar
    for some tau_bar in Lambda_bar.
    """
    id6 = tuple(range(6))
    psl_set = set(PSL2_5)
    I_tr = [g for g in PGL2_5 if g not in psl_set and perm_mul(g, g) == id6]
    assert len(I_tr) == 10
    lam_bar = [id6] + I_tr
    out = set()
    for tau_bar in lam_bar:
        kb = frozenset(perm_mul(tau_bar, x) for x in lam_bar)
        if all(1 <= sum(1 for g in kb if g[0] == j) <= 4 for j in range(6)):
            if len(gen_group(list(kb), 6)) == 120:
                out.add(kb)
    return sorted(out, key=lambda s: (len(s), sorted(s)))


def s6_small_inv_kbars(S6):
    """
    Exact top twisted subgroups for c = 6, b = 4, P_top = S_6:
    Since N_1 <= S_4^6 is a {2,3}-group, N_1 = Rad(G) is characteristic in G.
    Projecting Lambda = tau K modulo Rad(G~) into Aut(A_6) gives Lambda_bar <= {1} u Inv(Aut(A_6))
    of size <= 24 generating S_6.
    In Aut(A_6): |I_in(A_6)| = 45 > 24, PGL_2(9) \\ A_6 has sizes 36, 45 > 24, M_10 \\ A_6 has 0 involutions,
    and S_6^out \\ A_6 generates a subgroup of S_6^out != S_6.
    Thus Lambda_bar subset S_6 with Lambda_bar cap A_6 subset {1}, and to generate S_6 we must have
    Lambda_bar = {1} u O_15 where O_15 in {I_tr, I_3tr}.
    Then K_bar = tau_bar * Lambda_bar (with tau_bar in Lambda_bar), and we keep all subsets S <= K_bar
    closed under 1, x^-1, x y x with <= 4 elements per block j and <S> = S_6!
    """
    id6 = tuple(range(6))
    I_tr = [g for g in S6 if g != id6 and perm_mul(g, g) == id6 and sum(1 for i in range(6) if g[i] == i) == 4]
    I_3tr = [g for g in S6 if g != id6 and perm_mul(g, g) == id6 and sum(1 for i in range(6) if g[i] == i) == 0]
    out = set()
    for O15 in (I_tr, I_3tr):
        lam_bar = [id6] + O15
        for tau_bar in lam_bar:
            kb = frozenset(perm_mul(tau_bar, x) for x in lam_bar)
            if all(1 <= sum(1 for g in kb if g[0] == j) <= 4 for j in range(6)):
                if len(gen_group(list(kb), 6)) == 720:
                    out.add(kb)
    return sorted(out, key=lambda s: (len(s), sorted(s)))


def agl3_2_kbars(AGL3_2):
    """
    Exact top twisted subgroups for c = 8, b = 3, P_top = AGL_3(2) = V_8 : GL_3(2):
    Since N_1 <= S_3^8 and V_8 = O_2(AGL_3(2)) are solvable, Rad(G) is the preimage of V_8,
    and G / Rad(G) = GL_3(2) = PSL_2(7).
    Projecting Lambda = tau K modulo Rad(G~) into Aut(PSL_2(7)) = PGL_2(7) gives Lambda_GL of size <= 24
    generating PSL_2(7). Since PGL_2(7) \\ PSL_2(7) has unique involution class of size 28 > 24,
    Lambda_GL subset PSL_2(7) is either I_in (size 21) or {1} u I_in (size 22).
    Moreover |Lambda| = 24 while |Lambda_GL| >= 21, so K_bar = pi(K) <= AGL_3(2) has size |K_bar| <= 24
    and projects onto tau_GL * Lambda_GL in GL_3(2) (already the 22 valid kbars of PSL_2(7)!).
    Even simpler: every kbar in AGL_3(2) is closed under 1, x^-1, x y x, has <= 3 elements per block j,
    consists of valid semiregular projections for d in {2,3,4,6,8}, and projects onto a valid kbar of GL_3(2)!
    Let's enumerate ALL such kbars in AGL_3(2) directly!
    """
    id8 = tuple(range(8))
    valid_ds = {2, 3, 4, 6, 8}
    # Linear quotient map pi_lin: g -> x -> g(x) ^ g(0) in GL_3(2) (stabilizer of 0 in AGL_3(2))
    def pi_lin(g):
        g0 = g[0]
        return tuple(g[x] ^ g0 for x in range(8))

    GL3_2 = sorted({pi_lin(g) for g in AGL3_2})
    assert len(GL3_2) == 168

    # First enumerate all valid twisted subsets of GL_3(2) of size <= 24 generating GL_3(2) with orders dividing 24 (i.e. != 7)
    pool_gl = [g for g in GL3_2 if perm_order_general(g) != 7]
    pool_gl_set = set(pool_gl)

    def close_gl(S):
        S = set(S)
        q = deque(S)
        while q:
            x = q.popleft()
            ix = perm_inv(x)
            if ix not in S:
                if ix not in pool_gl_set:
                    return None
                S.add(ix)
                q.append(ix)
            for y in list(S):
                for z in (perm_mul(x, perm_mul(y, x)), perm_mul(y, perm_mul(x, y))):
                    if z not in S:
                        if z not in pool_gl_set:
                            return None
                        S.add(z)
                        q.append(z)
            if len(S) > 24:
                return None
        return frozenset(S)

    cs_gl = {g: close_gl([id8, g]) for g in pool_gl}
    cs_gl = {g: s for g, s in cs_gl.items() if s is not None}
    vp_gl = sorted(cs_gl.keys())
    vp_gl_idx = {g: i for i, g in enumerate(vp_gl)}
    m_gl = len(vp_gl)
    compat_gl = [0] * m_gl
    for i in range(m_gl):
        ci = cs_gl[vp_gl[i]]
        msk = 0
        for j in range(i + 1, m_gl):
            if vp_gl[j] in ci or close_gl(ci | cs_gl[vp_gl[j]]) is not None:
                msk |= (1 << j)
        compat_gl[i] = msk

    exp_gl = set()
    good_gl = set()

    def dfs_gl(S, cm):
        if S in exp_gl:
            return
        exp_gl.add(S)
        if len(gen_group(list(S), 8)) == 168:
            good_gl.add(S)
        cur = cm
        while cur:
            lsb = cur & -cur
            j = lsb.bit_length() - 1
            cur ^= lsb
            gj = vp_gl[j]
            if gj in S:
                continue
            S2 = close_gl(S | cs_gl[gj])
            if S2 is not None and S2 not in exp_gl:
                nm = cur & compat_gl[j]
                ok = True
                for x in S2:
                    ix = vp_gl_idx.get(x)
                    if ix is None:
                        ok = False
                        break
                    nm &= (compat_gl[ix] | ((1 << (ix + 1)) - 1))
                if ok:
                    dfs_gl(S2, nm)

    dfs_gl(frozenset([id8]), (1 << m_gl) - 1)
    # Up to GL_3(2)-conjugacy, pick orbit reps of good_gl, solve in AGL_3(2), then conjugate back?
    # Even simpler: union of lifts of each Q_gl in good_gl has size <= 24 * 8 = 192; enumerate_kbar_pruned on that 192-element subset!
    norm_gl = normalizer_in_sym(GL3_2, 8)
    norm_gl_0 = [h for h in norm_gl if h[0] == 0]
    seen_q = set()
    rep_qs = []
    for qset in sorted(good_gl, key=lambda s: (len(s), sorted(s))):
        if qset in seen_q:
            continue
        rep_qs.append(qset)
        for h in norm_gl_0:
            ih = perm_inv(h)
            seen_q.add(frozenset(perm_mul(h, perm_mul(g, ih)) for g in qset))

    out_kbars = set()
    for qset in rep_qs:
        sub_agl = [g for g in AGL3_2 if pi_lin(g) in qset]
        # Enumerate kbars inside sub_agl whose pi_lin equals qset and generate all of AGL_3(2):
        kbs_sub = enumerate_kbar_pruned(sub_agl, 8, 3, valid_ds, require_full_ptop=False)
        for kb in kbs_sub:
            if len(gen_group(list(kb), 8)) == 1344:
                out_kbars.add(kb)
    return sorted(out_kbars, key=lambda s: (len(s), sorted(s)))


def main():
    t0 = time.time()
    print("=== Compiling C Wreath Verifier (clang -O3) ===", flush=True)
    lib = compile_c_lib()

    print("=== Building Canonical Q_24 (C0001 Remark 2.3) ===", flush=True)
    q24_tab = build_canonical_Q24()
    print("Canonical Q_24 verified: order 24, left Bol, nonassociative, simple.\n", flush=True)

    S3 = gen_group([(1, 2, 0), (1, 0, 2)], 3)
    A4 = gen_group([(1, 2, 0, 3), (1, 0, 3, 2)], 4)
    S4 = gen_group([(1, 2, 3, 0), (1, 0, 2, 3)], 4)
    D8 = gen_group([(1, 2, 3, 0), (0, 3, 2, 1)], 4)
    V4 = gen_group([(1, 0, 3, 2), (2, 3, 0, 1)], 4)
    D10 = gen_group([(1, 2, 3, 4, 0), (0, 4, 3, 2, 1)], 5)
    S2_wr_S3 = gen_group([(1, 0, 2, 3, 4, 5), (2, 3, 4, 5, 0, 1), (2, 3, 0, 1, 4, 5)], 6)
    S3_wr_S2 = gen_group([(1, 2, 0, 3, 4, 5), (1, 0, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)], 6)
    PSL2_5 = gen_group([(1, 2, 3, 4, 0, 5), (5, 4, 2, 3, 1, 0)], 6)
    PGL2_5 = gen_group([(1, 2, 3, 4, 0, 5), (5, 4, 3, 2, 1, 0)], 6)  # wait: check order 120 below!
    # Correct PGL2(5) on P^1(F_5) = {0,1,2,3,4,5(inf)}: x+1=(1,2,3,4,0,5), 2x=(0,2,4,1,3,5), -1/x=(5,4,2,3,1,0)
    PGL2_5 = gen_group([(1, 2, 3, 4, 0, 5), (0, 2, 4, 1, 3, 5), (5, 4, 2, 3, 1, 0)], 6)
    A6 = gen_group([(1, 2, 0, 3, 4, 5), (0, 1, 3, 4, 2, 5), (0, 1, 2, 4, 5, 3)], 6)
    S6 = gen_group([(1, 2, 3, 4, 5, 0), (1, 0, 2, 3, 4, 5)], 6)
    assert len(PSL2_5) == 60 and len(PGL2_5) == 120 and len(A6) == 360 and len(S6) == 720

    trans_gens = [tuple(x ^ b_bit for x in range(8)) for b_bit in (1, 2, 4)]
    mul_alpha = (0, 2, 4, 6, 3, 1, 7, 5)
    frob = (0, 1, 4, 5, 6, 7, 2, 3)
    AGammaL1_8 = gen_group(trans_gens + [mul_alpha, frob], 8)
    gl1 = tuple(((x >> 1) & 1) | (((x >> 2) & 1) << 1) | ((((x & 1) ^ ((x >> 1) & 1))) << 2) for x in range(8))
    gl2 = tuple(((x >> 1) & 1) | ((x & 1) << 1) | (x & 4) for x in range(8))
    AGL3_2 = gen_group(trans_gens + [gl1, gl2], 8)
    assert len(AGammaL1_8) == 168 and len(AGL3_2) == 1344

    t_7 = (1, 2, 3, 4, 5, 6, 0, 7)
    inv_7 = (7, 6, 3, 2, 5, 4, 1, 0)
    dil_3 = (0, 3, 6, 2, 5, 1, 4, 7)
    PSL2_7 = gen_group([t_7, inv_7, perm_mul(dil_3, dil_3)], 8)
    PGL2_7 = gen_group([t_7, inv_7, dil_3], 8)
    assert len(PSL2_7) == 168 and len(PGL2_7) == 336

    S2_wr_S4 = gen_group([
        (1, 0, 2, 3, 4, 5, 6, 7),
        (2, 3, 4, 5, 6, 7, 0, 1),
        (2, 3, 0, 1, 4, 5, 6, 7),
    ], 8)
    assert len(S2_wr_S4) == 384

    C4 = gen_group([(1, 2, 3, 0)], 4)
    cosets_list = []
    for g in S4:
        cs = frozenset(perm_mul(g, v) for v in V4)
        if cs not in cosets_list:
            cosets_list.append(cs)
    s4_coset_V4 = {g: cosets_list.index(frozenset(perm_mul(g, v) for v in V4)) for g in S4}

    cosets_c4 = []
    for g in D8:
        cs = frozenset(perm_mul(g, v) for v in C4)
        if cs not in cosets_c4:
            cosets_c4.append(cs)
    d8_coset_C4 = {g: cosets_c4.index(frozenset(perm_mul(g, v) for v in C4)) for g in D8}

    S2 = gen_group([(1, 0)], 2)
    F20 = gen_group([(1, 2, 3, 4, 0), (0, 2, 4, 1, 3)], 5)
    A5_5 = gen_group([(1, 2, 3, 4, 0), (1, 0, 3, 2, 4)], 5)
    S5_5 = gen_group([(1, 2, 3, 4, 0), (1, 0, 2, 3, 4)], 5)
    AGL1_7 = gen_group([(1, 2, 3, 4, 5, 6, 0), (0, 3, 6, 2, 5, 1, 4)], 7)
    assert len(F20) == 20 and len(A5_5) == 60 and len(S5_5) == 120 and len(AGL1_7) == 42

    # AGL_2(3) on F_3^2 = {0..8} (3*x + y):
    def aff3(A, bv):
        return tuple(3 * ((A[0][0] * (i // 3) + A[0][1] * (i % 3) + bv[0]) % 3) + ((A[1][0] * (i // 3) + A[1][1] * (i % 3) + bv[1]) % 3) for i in range(9))
    AGL2_3 = gen_group([aff3(((1, 0), (0, 1)), (1, 0)), aff3(((1, 0), (0, 1)), (0, 1)), aff3(((1, 1), (0, 1)), (0, 0)), aff3(((0, 1), (1, 0)), (0, 0))], 9)
    assert len(AGL2_3) == 432

    # A_5 on 10 points (2-subsets of {0..4}):
    pairs5 = [(i, j) for i in range(5) for j in range(i + 1, 5)]
    A5_10 = gen_group([tuple(pairs5.index(tuple(sorted((g[a], g[b])))) for (a, b) in pairs5) for g in [(1, 2, 3, 4, 0), (1, 0, 3, 2, 4)]], 10)
    assert len(A5_10) == 60

    S4_wr_S2 = gen_group([
        (1, 2, 3, 0, 4, 5, 6, 7),
        (1, 0, 2, 3, 4, 5, 6, 7),
        (4, 5, 6, 7, 0, 1, 2, 3),
    ], 8)
    assert len(S4_wr_S2) == 1152

    print("=== PART 1: Complete Small-Order Chains for |Q| < 24 ===", flush=True)
    # First check affine AGL_2(3) at n = 9 directly (exp(Q) = 3):
    ts_9 = time.time()
    id9 = tuple(range(9))
    by_cos9 = {i: [] for i in range(9)}
    for g in AGL2_3:
        if g == id9 or (is_semiregular(g) and perm_order_general(g) == 3):
            by_cos9[g[0]].append(g)
    agl23_hits = 0
    chosen9 = {0: id9}
    def is_right_bol_9(tab):
        for z in range(9):
            for y in range(9):
                for x in range(9):
                    # ((x * y) * z) * y == x * ((y * z) * y)
                    if tab[tab[tab[x][y]][z]][y] != tab[x][tab[tab[y][z]][y]]:
                        return False
        return True

    def is_simple_9(tab):
        L_p = [tab[x] for x in range(9)]
        R_p = [[tab[x][y] for x in range(9)] for y in range(9)]
        all_p = L_p + R_p
        for z in range(1, 9):
            par = list(range(9))
            def fnd(a):
                while par[a] != a:
                    par[a] = par[par[a]]
                    a = par[a]
                return a
            par[z] = 0
            stk = [(0, z)]
            while stk:
                a0, b0 = stk.pop()
                for p0 in all_p:
                    ra, rb = fnd(p0[a0]), fnd(p0[b0])
                    if ra != rb:
                        par[rb] = ra
                        stk.append((ra, rb))
            if sum(1 for a in range(9) if fnd(a) == fnd(0)) < 9:
                return False
        return True

    def bt9(u):
        nonlocal agl23_hits
        if u == 9:
            ks = set(chosen9.values())
            if all(perm_inv(a) in ks and all(perm_mul(a, perm_mul(b, a)) in ks for b in ks) for a in ks):
                tab = [[chosen9[x][y] for y in range(9)] for x in range(9)]
                assert is_left_bol(tab, 9)
                if (not is_right_bol_9(tab)) and is_simple_9(tab):
                    agl23_hits += 1
            return
        for g in by_cos9[u]:
            ig = perm_inv(g)
            if ig[0] == u and ig != g:
                continue
            if ig[0] < u and chosen9[ig[0]] != ig:
                continue
            if all(is_derangement(g, chosen9[v]) for v in range(u)):
                chosen9[u] = g
                bt9(u + 1)
                del chosen9[u]
    bt9(1)
    print(f"  {'n=9 affine <= AGL_2(3)':42s} -> loops={agl23_hits} ({time.time()-ts_9:.3f}s)", flush=True)
    assert agl23_hits == 0

    part1 = [
        ("n=8  (S2, <=S4)", S2, 2, S4, 4, {2}, False, None),
        ("n=12 (S4, S3)", S4, 4, S3, 3, {2, 3, 4}, True, None),
        ("n=12 (S3, <=S4)", S3, 3, S4, 4, {2, 3, 4}, False, None),
        ("n=12 (S2, PSL2(5))", S2, 2, PSL2_5, 6, {2, 3, 4}, True, None),
        ("n=12 (S2, PGL2(5))", S2, 2, PGL2_5, 6, {2, 3, 4}, True, None),
        ("n=15 (S3, A5)", S3, 3, A5_5, 5, {3, 5}, True, None),
        ("n=15 (S3, S5)", S3, 3, S5_5, 5, {3, 5}, True, None),
        ("n=16 (S4, <=S4)", S4, 4, S4, 4, {2, 4}, False, None),
        ("n=18 (S2wrS3, S3)", S2_wr_S3, 6, S3, 3, {2, 3, 6}, True, None),
        ("n=18 (S3wrS2, S3)", S3_wr_S2, 6, S3, 3, {2, 3, 6}, True, None),
        ("n=18 (S3, PSL2(5))", S3, 3, PSL2_5, 6, {2, 3, 6}, True, None),
        ("n=18 (S3, PGL2(5))", S3, 3, PGL2_5, 6, {2, 3, 6}, True, None),
        ("n=18 (S3, S6) [|Lambda_-|=15]", S3, 3, S6, 6, {2, 3, 6}, True, None),
        ("n=18 (S2, <=AGL2(3))", S2, 2, AGL2_3, 9, {2, 3, 6}, False, None),
        ("n=20 (<=F20, <=S4)", F20, 5, S4, 4, {2, 4, 5}, False, None),
        ("n=20 (S4, D10)", S4, 4, D10, 5, {2, 4, 5}, True, None),
        ("n=20 (S4, F20)", S4, 4, F20, 5, {2, 4, 5}, True, None),
        ("n=20 (S4, A5)", S4, 4, A5_5, 5, {2, 4, 5}, True, None),
        ("n=20 (S2, A5_deg10)", S2, 2, A5_10, 10, {2, 4, 5}, True, None),
        ("n=21 (S3, <=AGL1(7))", S3, 3, AGL1_7, 7, {3, 7}, False, None),
    ]
    for lbl, P0, b, Ptop, c, ds_cur, req, cmap in part1:
        ts = time.time()
        ck_cur = None
        if lbl == "n=18 (S3, S6) [|Lambda_-|=15]":
            # Same fiber proof as n=24: |I_in(A6)|=45 > 18, so Lambda_bar = {1} u O_15 (O_15 in {I_tr, I_3tr}),
            # and |I_tr fixing 0| + 1 = 11 > 3 = b forces O_15 = I_3tr!
            id6 = tuple(range(6))
            I_3tr = [g for g in S6 if g != id6 and perm_mul(g, g) == id6 and sum(1 for i in range(6) if g[i] == i) == 0]
            lam_b = [id6] + I_3tr
            ck_cur = sorted({frozenset(perm_mul(tb, x) for x in lam_b) for tb in lam_b if all(1 <= sum(1 for g in (perm_mul(tb, x) for x in lam_b) if g[0] == j) <= 3 for j in range(6))})
        cnt, loops, meta = solve_chain_c(lib, P0, b, Ptop, c, ds_cur, req, ck_cur, cmap)
        print(f"  {lbl:42s} -> loops={cnt} ({time.time()-ts:.3f}s) meta={meta}", flush=True)
        assert cnt == 0

    print("\n=== PART 2: Complete Order-24 Uniqueness Chains ===", flush=True)
    ds_24 = {2, 3, 4, 6, 8}

    ts_kb = time.time()
    kbs_pgl2_5 = pgl2_5_small_inv_kbars(PGL2_5, PSL2_5)
    print(f"  Precomputed kbars ({time.time()-ts_kb:.2f}s): PGL2(5)={len(kbs_pgl2_5)}", flush=True)

    part2 = [
        ("n=24 (S3, AGammaL1(8))", S3, 3, AGammaL1_8, 8, False, None, None),
        ("n=24 (S3, PSL2(7))", S3, 3, PSL2_7, 8, True, None, None),
        ("n=24 (S3, PGL2(7))", S3, 3, PGL2_7, 8, True, None, None),
        ("n=24 (S4, PSL2(5))", S4, 4, PSL2_5, 6, True, None, None),
        ("n=24 (S4/V4-diag, PGL2(5))", S4, 4, PGL2_5, 6, True, kbs_pgl2_5, s4_coset_V4),
        ("n=24 (D8/C4-diag, PGL2(5))", D8, 4, PGL2_5, 6, True, kbs_pgl2_5, d8_coset_C4),
        ("n=24 (S2wrS3, A4)", S2_wr_S3, 6, A4, 4, True, None, None),
        ("n=24 (S3wrS2, A4)", S3_wr_S2, 6, A4, 4, True, None, None),
        ("n=24 (S2wrS3, S4)", S2_wr_S3, 6, S4, 4, True, None, None),
        ("n=24 (S3wrS2, S4)", S3_wr_S2, 6, S4, 4, True, None, None),
        ("n=24 (AGammaL1(8), S3)", AGammaL1_8, 8, S3, 3, True, None, None),
        ("n=24 (S2wrS4, S3)", S2_wr_S4, 8, S3, 3, True, None, None),
        ("n=24 (S4wrS2, S3)", S4_wr_S2, 8, S3, 3, True, None, None),
    ]

    total_hits = 0
    for lbl, P0, b, Ptop, c, req, ck, cmap in part2:
        ts = time.time()
        cnt, loops, meta = solve_chain_c(lib, P0, b, Ptop, c, ds_24, req, ck, cmap)
        print(f"  {lbl:42s} -> loops={cnt} ({time.time()-ts:.3f}s) meta={meta}", flush=True)
        assert len(loops) == cnt, f"Hit buffer overflow in {lbl}: {cnt} > {len(loops)}"
        for idx, tab in enumerate(loops):
            assert is_left_bol(tab, 24)
            iso = find_loop_isomorphism(tab, q24_tab, 24)
            assert iso is not None, f"NON-Q24 SIMPLE BOL LOOP FOUND AT ORDER 24 in {lbl}!"
            total_hits += 1
            if idx == 0:
                print(f"    -> Certified all {cnt} hit(s) isomorphic to canonical Q_24! Sample phi={iso[:8]}...", flush=True)

    assert total_hits >= 1, "Expected canonical Q_24 to appear!"
    print(f"\nALL WREATH CHECKS PASSED in {time.time()-t0:.2f}s! Total Q_24 hits certified isomorphic to canonical Q_24: {total_hits}.", flush=True)


if __name__ == "__main__":
    main()
