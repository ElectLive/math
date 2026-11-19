"""M-first, one auxiliary perfect-matching block, including reserved future pins.

forward(board,b,rng) -> (physical rows, Odds) or None; reverse chooses a
uniform auxiliary matching of the union. Odds is exactly reverse atom/forward
atom on a fixed supported history. Raw collisions and infeasible masked fills
are genuine nulls. Matching backend: sample_matching(compact_board, rng).
"""
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import factorial, prod
from random import SystemRandom

from exact_core import delete_matching, randbelow, sample_matching
from selector import Odds
from polygon import _shuffle


def _check(board,b):
    if not isinstance(board,tuple): board=tuple(board)
    n=len(board)
    if not n or type(b) is not int or not 1<=b<=n:
        raise ValueError("require 1<=b<=n")
    if any(type(m) is not int or not 0<=m<1<<n for m in board):
        raise ValueError("invalid board")
    return board


@lru_cache(maxsize=8)
def _table(n,b):
    if type(n) is not int or type(b) is not int or not 1<=b<=n:
        raise ValueError("require 1<=b<=n")
    fn=factorial(n)
    coeff=tuple(fn*factorial(n-a)//factorial(a) for a in range(n+1))
    dp=[(1,)+(0,)*n]
    for _ in range(b):
        prev=dp[-1]
        dp.append(tuple(sum(coeff[a]*prev[t-a] for a in range(t+1))
                        for t in range(n+1)))
    z,r=divmod(fn*fn*dp[b][n],fn**b)
    if r: raise ArithmeticError("nonintegral marked-block normalizer")
    return coeff,tuple(dp),z


def normalizer(n,b):
    return _table(n,b)[2]


def sample_counts(n,b,rng=None):
    """Draw a composition with weights proportional to product (n-a)!/a!."""
    rng=SystemRandom() if rng is None else rng
    coeff,dp,_=_table(n,b)
    t=n
    amounts=[]
    for j in range(b,1,-1):
        q=randbelow(dp[j][t],rng)
        for a in range(t+1):
            weight=coeff[a]*dp[j-1][t-a]
            if q<weight: break
            q-=weight
        amounts.append(a)
        t-=a
    return tuple(amounts+[t])


def _feasible(board):
    """Bipartite augmenting paths, iterative. No permanent count or recursion."""
    n=len(board)
    left=[-1]*n
    right=[-1]*n
    for root in range(n):
        queue=[root]; visited={root}; pred={}; free=None
        for x in queue:
            bits=board[x]
            while bits:
                bit=bits&-bits; bits-=bit; y=bit.bit_length()-1
                if y in pred: continue
                pred[y]=x
                z=right[y]
                if z<0:
                    free=y; break
                if z not in visited:
                    visited.add(z); queue.append(z)
            if free is not None: break
        if free is None: return False
        while free>=0:
            x=pred[free]
            prev=left[x]; left[x]=free; right[free]=x; free=prev
    return True


def _rows_check(board,rows):
    n=len(board)
    h=list(board)
    u=[0]*n
    for row in rows:
        if (len(row)!=n or any(type(y) is not int or not 0<=y<n for y in row)
                or len(set(row))!=n): raise ValueError("invalid row permutation")
        for x,y in enumerate(row):
            bit=1<<y
            if not h[x]&bit: raise ValueError("row conflicts with host or earlier row")
            h[x]-=bit; u[x]|=bit
    return tuple(u)


def _mask(host,mark,owner,c):
    """Return free vertices and compressed masked board, reserving all other marks."""
    n=len(host)
    xs=tuple(x for x in range(n) if owner[x]!=c)
    ys=tuple(sorted(mark[x] for x in xs))
    small=[]
    for x in xs:
        allowed=host[x]&~(1<<mark[x])
        small.append(sum(1<<j for j,y in enumerate(ys) if allowed&(1<<y)))
    return xs,ys,tuple(small)


def _new_odds(n,b,masked,host,masks,union,counts):
    if not masked:
        return Odds(normalizer(n,b),(),(union,))
    k=Fraction(normalizer(n,b),factorial(n)*prod(factorial(n-a) for a in counts))
    return Odds(k,(host,*masks),(union,))


def odds_from_history(board,rows,mark,*,masked=True):
    rows=tuple(tuple(r) for r in rows); mark=tuple(mark)
    board=_check(board,len(rows)); n=len(board); b=len(rows)
    union=_rows_check(board,rows)
    if (len(mark)!=n or any(type(y) is not int or not 0<=y<n for y in mark)
            or len(set(mark))!=n or any(not union[x]&(1<<y) for x,y in enumerate(mark))):
        raise ValueError("auxiliary mark not a matching of row union")
    owner=tuple(next(j for j,row in enumerate(rows) if row[x]==mark[x]) for x in range(n))
    counts=tuple(owner.count(c) for c in range(b))
    masks=[]
    if masked:
        residual=board
        for c,row in enumerate(rows):
            _,_,m=_mask(residual,mark,owner,c)
            masks.append(m)
            residual=delete_matching(residual,row)
    return _new_odds(n,b,masked,board,masks,union,counts)


@dataclass(frozen=True)
class MarkedHistory:
    rows:tuple
    mark:tuple
    odds:Odds


def forward_history(board,b,rng=None,*,masked=True,matching_fn=None):
    board=_check(board,b)
    n=len(board)
    rng=SystemRandom() if rng is None else rng
    fn=sample_matching if matching_fn is None else matching_fn
    if masked:
        if not _feasible(board): return None
        mark=tuple(fn(board,rng))
    else:
        mark=tuple(_shuffle(range(n),rng))
    counts=sample_counts(n,b,rng)
    owner=_shuffle((c for c,a in enumerate(counts) for _ in range(a)),rng)
    residual=board
    rows=[]; masks=[]
    for c in range(b):
        xs,ys,small=_mask(residual,mark,owner,c)
        row=list(mark)  # filled only at its own pins; others replaced below
        if masked:
            if not _feasible(small): return None
            choice=fn(small,rng) if small else ()
            masks.append(small)
            vals=tuple(ys[j] for j in choice)
        else:
            vals=_shuffle(ys,rng)
        for x,y in zip(xs,vals): row[x]=y
        row=tuple(row)
        if any(not residual[x]&(1<<y) for x,y in enumerate(row)): return None
        residual=delete_matching(residual,row); rows.append(row)
    rows=tuple(rows); union=tuple(a^b0 for a,b0 in zip(board,residual))
    return MarkedHistory(rows,mark,_new_odds(n,b,masked,board,masks,union,counts))


def forward(board,b,rng=None,*,masked=True,matching_fn=None):
    hist=forward_history(board,b,rng,masked=masked,matching_fn=matching_fn)
    return None if hist is None else (hist.rows,hist.odds)


def reverse_history(board,rows,rng=None,*,masked=True,matching_fn=None):
    rows=tuple(tuple(row) for row in rows); board=_check(board,len(rows))
    union=_rows_check(board,rows)
    fn=sample_matching if matching_fn is None else matching_fn
    rng=SystemRandom() if rng is None else rng
    mark=tuple(fn(union,rng))
    return MarkedHistory(rows,mark,odds_from_history(board,rows,mark,masked=masked))


def reverse(board,rows,rng=None,*,masked=True,matching_fn=None):
    return reverse_history(board,rows,rng,masked=masked,matching_fn=matching_fn).odds
