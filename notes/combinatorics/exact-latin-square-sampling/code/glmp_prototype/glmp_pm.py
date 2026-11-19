"""Rational/dyadic GLMP section 6 backend prototype. No default asymptotic clock.

Fast branch: finite adaptive JSV annealing, class histograms, capped restarts.
Rare branch: enumerate the law INCLUDING all failures, then exactly correct it.
The cheap branch is a *biased approximate sampler*, not usable by itself for
exact generation. See README for admission conditions, not numerical heuristics.
"""
from collections import defaultdict
from dataclasses import dataclass
from fractions import Fraction as F
from itertools import permutations
from math import comb, factorial, lcm, prod
from random import SystemRandom


@dataclass(frozen=True)
class Clock:
    phase_samples: int    # independent fresh chains per annealing update
    phase_steps: int      # steps in each such chain
    final_steps: int      # steps for a final draw
    attempts: int         # maximum independent full attempts, fallback if all fail
    bits: int             # b bits for token and b bits for acceptance per chain step
    correction: F         # delta in (0,1], exact rational
    def __post_init__(self):
        if any(type(t) is not int or t<1 for t in
               (self.phase_samples,self.phase_steps,self.final_steps,self.attempts,self.bits)):
            raise ValueError("positive integer clock parameters required")
        if type(self.correction) not in (int,F) or not 0 < self.correction <= 1:
            raise ValueError("correction must be an exact rational in (0,1]")
        object.__setattr__(self,'correction',F(self.correction))


def _board(b):
    b=tuple(b); n=len(b)
    if any(type(m) is not int or not 0<=m<1<<n for m in b):
        raise ValueError("invalid board")
    return b


def fallback(board):
    """Deterministic augmenting-path perfect matching; feasibility without counting."""
    b=_board(board); n=len(b); left=[-1]*n; right=[-1]*n
    for root in range(n):
        queue=[root]; seen={root}; parent={}; y=-1
        for u in queue:
            for v in range(n):
                if not (b[u]>>v)&1 or v in parent: continue
                parent[v]=u
                if right[v]<0:
                    y=v;break
                if right[v] not in seen:
                    queue.append(right[v]);seen.add(right[v])
            if y>=0: break
        if y<0: raise ValueError("no perfect matching")
        while y>=0:
            u=parent[y]; old=left[u]; left[u]=y; right[y]=u; y=old
    return tuple(left)


def _valid(b,s):
    return all(y>=0 and (b[i]>>y)&1 for i,y in enumerate(s))


def cooling(board):
    """Lists λ scales by left vertex; only forbidden incident edges receive λ."""
    b=_board(board); n=len(b); a=[F(1)]*n; yield tuple(a)
    floor=F(1,factorial(n))
    for u in range(n):
        if b[u]==(1<<n)-1:continue
        while a[u]>floor:
            a[u]=max(floor,3*a[u]/4)
            yield tuple(a)


def hole(s):
    """0 is the perfect bin, 1+u*n+v the two-hole bin."""
    if -1 not in s:return 0
    n=len(s); u=s.index(-1); v=n*(n-1)//2 - (sum(s)+1)
    return 1+u*n+v


def _weight(board,a,w,s):
    k=hole(s)
    x=w[k-1] if k else F(1)
    for u,y in enumerate(s):
        if y>=0 and not (board[u]>>y)&1: x*=a[u]
    return x


def _neighbor(s,token):
    n=len(s)
    if token>=2*n: return s   # standard 1/2 laziness
    k=hole(s); v=list(s)
    if not k:
        v[token%n]=-1
    else:
        u,y=divmod(k-1,n)
        if token in (u,n+y):
            v[u]=y
        elif token<n:
            v[token]=y
        else:
            z=token-n; v[v.index(z)]=-1; v[u]=z
    return tuple(v)


def _cut(b,a,w,s,t,den):
    z=F(_weight(b,a,w,t),_weight(b,a,w,s))
    return min(den,den*z.numerator//z.denominator)


def step(b,a,w,s,bits,rng):
    """One finite precision transition; total 2*bits independent random bits."""
    den=1<<bits; t=_neighbor(s,rng.getrandbits(bits)*(4*len(b))//den)
    v=rng.getrandbits(bits)
    return t if t!=s and v<_cut(b,a,w,s,t,den) else s


def kernel(b,a,w,s,bits):
    """Exact row of the same dyadic transition by token-bin widths, not samples."""
    n=len(b); den=1<<bits; out=defaultdict(int)
    for token in range(4*n):
        width=((token+1)*den+4*n-1)//(4*n)-(token*den+4*n-1)//(4*n)
        if not width:continue
        t=_neighbor(s,token)
        if t!=s:
            to_t=width*_cut(b,a,w,s,t,den)
            out[t]+=to_t
            out[s]+=width*den-to_t
        else: out[s]+=width*den
    return {t:F(v,den*den) for t,v in out.items() if v}


def _ratio(b,a,w,s,t):
    """Adjacent-state weight ratio using only changed edges and two holes."""
    h,k=hole(s),hole(t)
    z=F(w[k-1] if k else 1,w[h-1] if h else 1)
    for u,(x,y) in enumerate(zip(s,t)):
        if x!=y:
            if x>=0 and not (b[u]>>x)&1:z/=a[u]
            if y>=0 and not (b[u]>>y)&1:z*=a[u]
    return z


def _token_lazy(total,bits,rng):
    # Uniform b-bit int K -> floor(total*K/2^b), without materializing K.
    prefix=0;den=1
    for _ in range(bits):
        prefix=2*prefix+rng.getrandbits(1); den*=2
        lo=total*prefix//den
        hi=(total*(prefix+1)-1)//den
        if lo==hi:return lo
    return total*prefix//den


def _rounded_coin_lazy(p,bits,rng):
    if p>=1:return True
    if p<=0:return False
    rem,den=p.numerator,p.denominator
    for _ in range(bits):
        digit,rem=divmod(2*rem,den)
        v=rng.getrandbits(1)
        if v!=digit:return v<digit
        if rem==0:return False
    return False


def step_lazy(b,a,w,s,bits,rng):
    t=_neighbor(s,_token_lazy(4*len(b),bits,rng))
    return t if t!=s and _rounded_coin_lazy(_ratio(b,a,w,s,t),bits,rng) else s


def chain(b,a,w,length,bits,rng):
    s=fallback(b)  # real perfect matching, identical reset on every independent call
    for _ in range(length):
        s=(step if bits<=64 else step_lazy)(b,a,w,s,bits,rng)
    return s


def chain_law(b,a,w,length,bits):
    seen={}; d={fallback(b):F(1)}
    for _ in range(length):
        v=defaultdict(F)
        for s,p in d.items():
            if s not in seen:seen[s]=kernel(b,a,w,s,bits)
            for t,q in seen[s].items():v[t]+=p*q
        d=v
    return dict(d)


def _weights(w,hist):
    if not all(hist):return None
    return tuple(x*F(hist[0],h) for x,h in zip(w,hist[1:]))


def attempt(board,clock,rng=None):
    b=_board(board); n=len(b)
    if not n:return ()
    rng=SystemRandom() if rng is None else rng
    phases=tuple(cooling(b)); w=(F(n),)*(n*n)
    for a in phases[:-1]:
        h=[0]*(n*n+1)
        for _ in range(clock.phase_samples):
            h[hole(chain(b,a,w,clock.phase_steps,clock.bits,rng))]+=1
        w=_weights(w,h)
        if w is None:return None
    s=chain(b,phases[-1],w,clock.final_steps,clock.bits,rng)
    return s if _valid(b,s) else None


def _positive_histograms(total,bins):
    # Enumerate positive histograms in place via an explicit stack. All zero-bin
    # histograms are genuine failures, whose mass is recovered by complement.
    if total<bins:return
    work=[(total,bins,())]
    while work:
        rem,k,prefix=work.pop()
        if k==1:
            yield prefix+(rem,)
        else:
            for i in range(1,rem-k+2):
                work.append((rem-i,k-1,prefix+(i,)))


def _multinomial(hist,p):
    rem=sum(hist); mass=F(1)
    for h,q in zip(hist,p):
        mass*=comb(rem,h)*q**h; rem-=h
    return mass


def attempt_law(board,clock):
    b=_board(board); n=len(b)
    if not n:return {():F(1), None:F(0)}
    phases=tuple(cooling(b)); weights={(F(n),)*(n*n):F(1)}
    for a in phases[:-1]:
        nxt=defaultdict(F)
        for w,prior in weights.items():
            p=[F() for _ in range(1+n*n)]
            for s,q in chain_law(b,a,w,clock.phase_steps,clock.bits).items():
                p[hole(s)]+=q
            if not all(p):continue
            for h in _positive_histograms(clock.phase_samples,len(p)):
                nxt[_weights(w,h)]+=prior*_multinomial(h,p)
        weights=dict(nxt)
    law=defaultdict(F)
    for w,prior in weights.items():
        for s,q in chain_law(b,phases[-1],w,clock.final_steps,clock.bits).items():
            if _valid(b,s):law[s]+=prior*q
    law[None]=1-sum(law.values(),F())
    return dict(law)


def approximate(board,clock,rng=None):
    """Finite capped approximation. NOT an exact uniform matching sampler."""
    b=_board(board); failover=fallback(b)
    rng=SystemRandom() if rng is None else rng
    for _ in range(clock.attempts):
        s=attempt(b,clock,rng)
        if s is not None:return s
    return failover


def approximate_law(board,clock):
    b=_board(board); failover=fallback(b); d=attempt_law(b,clock); fail=d.pop(None)
    miss=fail**clock.attempts
    mult=F(clock.attempts) if fail==1 else (1-miss)/(1-fail)
    Q={s:p*mult for s,p in d.items()}
    Q[failover]=Q.get(failover,F())+miss
    return Q


def correction_table(board,clock):
    """Raises ValueError if the supplied clock violates pointwise admission."""
    b=_board(board); fallback(b)
    targets=[s for s in permutations(range(len(b))) if _valid(b,s)]
    Q=approximate_law(b,clock); pi=F(1,len(targets)); delta=clock.correction
    v={s:(pi-(1-delta)*Q.get(s,F()))/delta for s in targets}
    if min(v.values())<0 or sum(v.values())!=1:
        raise ValueError("clock not admitted: negative correction mass")
    return v


def _below(n,rng):
    if n==1:return 0
    while True:
        x=rng.getrandbits((n-1).bit_length())
        if x<n:return x


def _sample_vector(v,rng):
    den=1
    for p in v.values():den=lcm(den,p.denominator)
    x=_below(den,rng)
    for s,p in v.items():
        k=p.numerator*(den//p.denominator)
        if x<k:return s
        x-=k
    raise AssertionError("invalid distribution")


def sample_admitted(board,clock,rng=None):
    """REQUIRES (1-delta)*Q(x)<=1/per(board) for every valid x.

    No deduction of a mathematical admission certificate from empirical data.
    If a positive rare-branch validation is unavailable, use checked_sampler
    for a finite precheck, or the unconditional loose rate delta>=1-1/n!.
    """
    b=_board(board); fallback(b)
    if len(b)<=1:return tuple(range(len(b)))
    rng=SystemRandom() if rng is None else rng
    return (_sample_vector(correction_table(b,clock),rng)
            if _correction_coin(clock,rng) else approximate(b,clock,rng))


def checked_sampler(board,clock):
    """Exhaustively prevalidate and cache the rare law; unconditional exactness.

    Returned callable accepts rng=None. The upfront *exponential* exhaustive cost
    makes this a reference check, not a performance claim about GLMP.
    """
    b=_board(board); d=correction_table(b,clock)
    def draw(rng=None):
        rng=SystemRandom() if rng is None else rng
        return _sample_vector(d,rng) if _correction_coin(clock,rng) else approximate(b,clock,rng)
    return draw


@dataclass(frozen=True)
class DyadicClock:
    # Unlike Fraction(1, 1<<u), this object fits in O(log u) bits.
    phase_samples:int
    phase_steps:int
    final_steps:int
    attempts:int
    bits:int
    correction_exponent:int
    def __post_init__(self):
        if any(type(v) is not int or v<1 for v in self.__dict__.values()):
            raise ValueError("positive integer clock parameters required")
    @property
    def correction(self):
        # Only exact-law validation/correction requires the explicit rational.
        return F(1,1<<self.correction_exponent)


def _correction_coin(clock,rng):
    if isinstance(clock,DyadicClock):
        for _ in range(clock.correction_exponent):
            if rng.getrandbits(1):return False
        return True
    p=clock.correction
    return _below(p.denominator,rng)<p.numerator


def research_clock(board):
    """Explicit conservative JSV/GLMP parameter ledger; see the accompanying proof.

    Merely constructing this object computes only small integers, NOT the
    denominator 2**u. The real transition counts are deliberately enormous.
    """
    b=_board(board);m=len(b)
    if m<2:raise ValueError("side <2 has an immediate exact matching")
    R=sum(1 for _ in cooling(b))-1
    u=(1<<30)*(m+2)**4*(1+(m+2).bit_length())**2
    L=((1+2*m*m)*factorial(m)).bit_length()
    pre=(1<<10)*m**6*(L+20+2*m.bit_length())
    final=(1<<10)*m**6*(L+32*u)
    S=(1<<22)*(1+2*m*m)*(u+(R+1).bit_length()+m.bit_length()+1)
    runs=(1<<10)*(1+2*m*m)*u
    bits=64*u+(runs*(R*S*pre+final+2)*(4*m+2)).bit_length()+4
    return DyadicClock(S,pre,final,runs,bits,u)


def matching_backend(board,rng=None):
    """Exact research backend for a feasible compact board, including minors.

    Through side seven use finite permutation enumeration. At larger orders this
    calls the admitted, deliberately impractical GLMP research clock. Do not
    select it for speed; the small finite branch is not a timing demonstration of
    the asymptotic branch. The full Latin calibration problem is separate.
    """
    b=_board(board); fallback(b)
    rng=SystemRandom() if rng is None else rng
    if len(b)<=7:
        targets=[s for s in permutations(range(len(b))) if _valid(b,s)]
        return targets[_below(len(targets),rng)]
    return sample_admitted(b,research_clock(b),rng)
