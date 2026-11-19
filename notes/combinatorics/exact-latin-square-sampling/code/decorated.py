"""End-to-end decorated exact reference sampler, using all three proposal families.

The default SAFE scale is a proved Brégman envelope, not the theorem-calibrated
scale. Matching is by subset DP. This executable mode has exact target law but
is not the claimed expected-polynomial implementation. Public words, schedules
and witnesses are fresh in every reverse experiment.
"""
from dataclasses import dataclass
from fractions import Fraction
from functools import lru_cache
from math import prod
from random import SystemRandom

import cold4
import marked
import polygon
from exact_core import (_natural, _root, coin, delete_matching, full_board,
                       is_latin, permanent, randbelow, row_envelope, sample_matching)
from selector import Odds, direct_gate


def _rng(rng):
    return SystemRandom() if rng is None else rng


def _add(a, b):
    return Odds(a.scalar*b.scalar, a.numerator+b.numerator, a.denominator+b.denominator)


@dataclass(frozen=True)
class Parameters:
    n: int
    max_half: int | None = None
    max_b: int | None = None

    def __post_init__(self):
        n = _natural(self.n, positive=True)
        if self.max_half is None:
            object.__setattr__(self,"max_half",n)
        if type(self.max_half) is not int or not 1 <= self.max_half <= n:
            raise ValueError("max_half must be in 1,...,n")
        if self.max_b is None:
            # floor(n^(1/200)) with nonvacuous small-order exercise of b=2.
            object.__setattr__(self,"max_b",min(n,max(2,_root(n,200))))
        if type(self.max_b) is not int or not 1 <= self.max_b <= n:
            raise ValueError("max_b must be in 1,...,n")


@lru_cache(maxsize=32)
def safe_scale(n):
    return prod(row_envelope(n,d) for d in range(1,n+1))


def _word(p,rng):
    return polygon.draw_word_tagged(p.max_half,rng)


def _group_count(n,head,b):
    return min((n-head)//b,_root(n**9,10)//b)


@dataclass(frozen=True)
class Path:
    square: tuple
    odds: Odds
    family: int
    raw_tag: bool  # exactly "family=generic and first word coin stopped at l=1"


def _run(p, rng, given=None, *, matching_fn=sample_matching):
    n = p.n
    fam = randbelow(3,rng)
    order = polygon._shuffle(range(n),rng)
    target = tuple(given[i] for i in order) if given is not None else None
    if fam == 1:
        if target is None:
            result = cold4.forward(n,rng,matching_fn=matching_fn,count_fn=marked._feasible)
            if result is None: return None
            rows, odds = result
        else:
            rows, odds = target,cold4.reverse(target)
        raw_tag = False
    else:
        word, tag = _word(p,rng)
        raw_tag = fam==0 and tag
        head = max(word)+1 if word is not None else 0
        if given is None:
            seed = polygon.seed_forward(n,head,word,rng)
            if seed is None: return None
        else:
            seed = polygon.seed_reverse(target[:head],word,rng,n=n)
        rows, odds, board = list(seed.rows),Odds(seed.ratio),full_board(n)
        for row in rows:
            board = delete_matching(board,row)
        if fam==2 and p.max_b>=2:
            b = 2+randbelow(p.max_b-1,rng)
            for _ in range(_group_count(n,head,b)):
                if target is None:
                    block = marked.forward(board,b,rng,matching_fn=matching_fn)
                    if block is None: return None
                    more, z = block
                else:
                    more = target[len(rows):len(rows)+b]
                    z = marked.reverse(board,more,rng,matching_fn=matching_fn)
                odds = _add(odds,z)
                for row in more:
                    rows.append(row)
                    board = delete_matching(board,row)
        while len(rows)<n:
            row = target[len(rows)] if target is not None else matching_fn(board,rng)
            odds = _add(odds,Odds(numerator=(board,)))
            rows.append(row)
            board = delete_matching(board,row)
    square = [None]*n
    for label,row in zip(order,rows):
        square[label] = row
    return Path(tuple(square),odds,fam,raw_tag)


def forward_path(params,rng=None,*,matching_fn=sample_matching):
    """One forward decoration, or None for an actual protocol veto."""
    return _run(params,_rng(rng),matching_fn=matching_fn)


def reverse_path(params,square,rng=None,*,matching_fn=sample_matching):
    """Independent complete reverse decoration on a fixed valid labeled target."""
    square = tuple(map(tuple,square))
    if len(square)!=params.n or not is_latin(square):
        raise ValueError("reverse source is not a Latin square of the specified order")
    return _run(params,_rng(rng),given=square,matching_fn=matching_fn)


def _fcoin(p,rng):
    return coin(p.numerator,p.denominator,rng)


RAW_TAG_MASS = Fraction(1,6)  # independent public family=0 (1/3), length=1 (1/2)
SAFE_C = RAW_TAG_MASS/2


def safe_residual_coin(params,square,H,rng=None):
    """A (g-c)-coin at safe H; not an estimator of g truncated to [c,1]."""
    if H<safe_scale(params.n):
        raise ValueError("safe inverse requires H >= product of the row envelopes")
    rng = _rng(rng)
    rev = reverse_path(params,square,rng)
    t = rev.odds.exact()
    prob = Fraction(H,H+t)
    if rev.raw_tag:
        # tag forces an *ordinary* ordered path: T=prod per(A_d)<=H. Its
        # probability 1/6 is target-independent. Subtracting 1/2 only here
        # changes the unconditional success probability by exactly c=1/12.
        prob -= Fraction(1,2)
    return _fcoin(prob,rng)


def safe_inverse_coin(params,square,H,rng=None):
    """Exact c/g: a two-coin Bernoulli race with probabilities c and g-c."""
    rng = _rng(rng)
    while True:
        if randbelow(2,rng):
            if _fcoin(SAFE_C,rng): return True
        elif safe_residual_coin(params,square,H,rng):
            return False


def decorated_trial(params,rng=None):
    """Default finite end-to-end trial: single-target submass (1/12)/H."""
    rng = _rng(rng)
    H = safe_scale(params.n)
    path = forward_path(params,rng)
    if path is None or not direct_gate(path.odds,H,rng=rng): return None
    return path.square if safe_inverse_coin(params,path.square,H,rng) else None


def sample_decorated(n,rng=None,*,max_half=None,max_b=None):
    p = Parameters(n,max_half,max_b)
    rng = _rng(rng)
    while True:
        result = decorated_trial(p,rng)
        if result is not None:
            return result


def _reciprocal_gate(gcoin,gamma,rng):
    """Requires the caller to have proved g>=gamma>0. No probability estimates."""
    from huber_double import double_low
    c=Fraction(gamma,4)
    def qcoin():
        while True:
            if randbelow(2,rng):
                if _fcoin(c,rng): return True
            elif gcoin():
                return False
    # Independent geometric(1/2) count on 1,2,..., short-circuited on failure.
    while True:
        if not double_low(qcoin,rng.getrandbits): return False
        if randbelow(2,rng): return True


def certified_trial(params,H,gamma,rng=None,*,matching_fn=sample_matching,oracle_gate=False):
    """Low-level theorem trial conditional on CERTIFIED 0<gamma<=min_S g_H(S).

    No test can infer this premise from observed paths. Use safe_huber_trial for
    runnable unconditional defaults. For certified inputs, the per-target mass
    is gamma/(4H). oracle_gate=True avoids permanent evaluation in sigmoid gates
    but is deliberately slow with the shipped exponential matching backend.
    """
    if type(H) not in (int,Fraction) or H<=0:
        raise ValueError("H must be a positive rational")
    if type(gamma) not in (int,Fraction) or not 0<gamma<=1:
        raise ValueError("gamma must be a positive rational <=1")
    rng=_rng(rng)
    if oracle_gate:
        from selector import oracle_sigmoid_gate
        def gate(o,rev): return oracle_sigmoid_gate(o,H,rev,rng,matching_fn)
    else:
        def gate(o,rev): return direct_gate(o,H,rev,rng)
    path=forward_path(params,rng,matching_fn=matching_fn)
    if path is None or not gate(path.odds,False): return None
    def gcoin():
        return gate(reverse_path(params,path.square,rng,matching_fn=matching_fn).odds,True)
    return path.square if _reciprocal_gate(gcoin,gamma,rng) else None


def safe_huber_trial(params,rng=None,*,oracle_gate=False):
    """Unconditional theorem-style trial at conservative scale and proved gamma."""
    return certified_trial(params,safe_scale(params.n),SAFE_C,rng,oracle_gate=oracle_gate)


def sample_huber(n,rng=None,*,oracle_gate=False):
    params,rng=Parameters(n),_rng(rng)
    while True:
        square=safe_huber_trial(params,rng,oracle_gate=oracle_gate)
        if square is not None: return square
