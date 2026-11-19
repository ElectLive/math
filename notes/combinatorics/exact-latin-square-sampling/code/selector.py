"""Forward/reverse matching-product gates, using rational probabilities.

direct_gate uses *exact permanent evaluation* (the bundled backend is exponential).
paired_gate needs only an exact uniform matching draw on each feasible board or
minor. It does not evaluate a permanent. For T=odds the conditional pass rates
a,h always obey a/T=h/H. Do not mix gate families between the two directions.
Neither alone implements the terminal inverse-g factory or a full square sampler.
"""
from dataclasses import dataclass
from fractions import Fraction
from math import prod
from random import SystemRandom

from exact_core import coin, permanent, sample_matching


def _positive(x):
    if type(x) not in (int,Fraction):
        raise TypeError("use a positive int or Fraction, not a float")
    x=Fraction(x)
    if x<=0: raise ValueError("positive rational required")
    return x


def _board(b):
    b=tuple(b)
    if any(type(x) is not int or not 0<=x<(1<<len(b)) for x in b):
        raise ValueError("invalid board mask")
    return b


@dataclass(frozen=True)
class Odds:
    """T = scalar * product(per(N)) / product(per(D)); all factors feasible."""
    scalar: Fraction=Fraction(1)
    numerator: tuple=()
    denominator: tuple=()

    def __post_init__(self):
        object.__setattr__(self,"scalar",_positive(self.scalar))
        for attr in ("numerator","denominator"):
            object.__setattr__(self,attr,tuple(_board(b) for b in getattr(self,attr)))

    def exact(self,permanent_fn=None):
        fn=permanent if permanent_fn is None else permanent_fn
        n=prod(fn(b) for b in self.numerator)
        d=prod(fn(b) for b in self.denominator)
        if min(n,d)<=0: raise ValueError("all permanent factors must be positive")
        return self.scalar*Fraction(n,d)


def _bernoulli(p,rng):
    return coin(p.numerator,p.denominator,rng)


def direct_gate(odds,H,reverse=False,rng=None,permanent_fn=None):
    """Exact sigmoid gate: forward T/(T+H), reverse H/(T+H)."""
    H=_positive(H)
    t=odds.exact(permanent_fn)
    return _bernoulli((H if reverse else t)/(H+t),rng)


def _minor(b,j):
    """Delete first row and column j, compacting symbol labels."""
    low=(1<<j)-1
    return tuple((x&low)|((x>>(j+1))<<j) for x in b[1:])


def _draw(fn,b,rng):
    m=fn(b,rng)
    if m is None:
        raise ValueError("empty matching support")
    m=tuple(m)
    if (len(m)!=len(b) or any(type(y) is not int or not 0<=y<len(b)
                              or not(b[x]&(1<<y)) for x,y in enumerate(m))
                              or len(set(m))!=len(b)):
        raise ValueError("backend did not give a legal perfect matching")
    return m


def _trials(fn,b,rng,j,successes):
    if b[0].bit_count()==1:
        return successes
    count=0
    while successes:
        count+=1
        successes-=int(_draw(fn,b,rng)[0]==j)
    return count


def paired_estimate(odds,reverse=False,rng=None,matching_fn=None,*,replicates=None):
    """An unbiased estimate Y of T, or a sample Y* from its size-biased law.

    Fresh full anchors are independent on each block. At a fixed anchor step
    with child probability p, NB(k,p) here counts trials INCLUDING successes.
    A positive factor averages m geometric waits (mean 1/p); its size bias is
    (NB(m+1,p)-1)/m. A reciprocal factor uses (m-1)/(NB(m,p)-1)
    (mean p), whose size bias has NB(m,p) replaced by 1+NB(m-1,p).
    Conditional means telescope separately for every anchor, so anchors
    must NOT themselves be tilted on the reverse call.
    """
    rng=SystemRandom() if rng is None else rng
    fn=sample_matching if matching_fn is None else matching_fn
    sites=sum(map(len,odds.numerator))+sum(map(len,odds.denominator))
    m=sites+2 if replicates is None else replicates
    if type(m) is not int or m<3:
        if replicates is None and sites==0: return odds.scalar
        raise ValueError("replicates must be an integer >=3")
    score=odds.scalar
    for inv,boards in ((False,odds.numerator),(True,odds.denominator)):
        for full in boards:
            if not full: continue
            anchor=_draw(fn,full,rng)
            cols=list(range(len(full)))
            b=full
            for chosen in anchor:
                j=cols.index(chosen)
                if inv:
                    if reverse:
                        den=_trials(fn,b,rng,j,m-1)
                    else:
                        den=_trials(fn,b,rng,j,m)-1
                    score*=Fraction(m-1,den)
                else:
                    total=_trials(fn,b,rng,j,m+int(reverse))-int(reverse)
                    score*=Fraction(total,m)
                del cols[j]
                b=_minor(b,j)
    return score


def paired_gate(odds,H,reverse=False,rng=None,matching_fn=None,*,replicates=None):
    """Forward min(Y/H,1), reverse min(H/Y*,1), preserving exact submass.

    Default m=2+#sites yields E[(Y/T)^2]<=e on each fixed anchor. Consequently
    h>=min(1,H/T)/(8e); the two tails require no unknown optimal cap.
    Per trial the expected # of oracle draws is polynomial, since the random
    anchor prefix has E[1/p|past] at most the number of available columns.
    The shipped uniform-PM backend uses exponential subset DP, not GLMP.
    """
    H=_positive(H)
    y=paired_estimate(odds,reverse,rng,matching_fn,replicates=replicates)
    p=H/y if reverse else y/H
    return p>=1 or _bernoulli(p,rng)


def oracle_sigmoid_gate(odds,H,reverse=False,rng=None,matching_fn=None):
    """Exact sigmoid via Bernoulli race; NO permanent evaluations or sum gadget.

    Draw a fair side, run an independent paired_gate on that side, retry on
    failure. Its first winner has probabilities a/(a+h) and h/(a+h), exactly
    T/(T+H), H/(T+H). At default m, Paley-Zygmund gives a+h>=1/(8e),
    so the expected number of rounds is at most 16e for every feasible input.
    The output bit has the SAME law as direct_gate; performance is conditional
    on the matching backend. No nested failure is promoted to a board retry.
    """
    H=_positive(H)
    rng=SystemRandom() if rng is None else rng
    while True:
        side=bool(rng.getrandbits(1))
        if paired_gate(odds,H,side,rng,matching_fn):
            return side==bool(reverse)
