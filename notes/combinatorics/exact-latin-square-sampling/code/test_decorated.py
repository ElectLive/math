"""Independent finite path-mass audit for the three-family composition.

Restrict public max_half=2 and max_b=2 (valid reference settings). Every
possible row schedule, target square and latent matching is summed exactly.
The numerator forward probability of each fixed history is reconstructed from
its primitive draws, never by defining it to be its reverse mass / T.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations,product
from math import factorial,prod
from random import Random
import unittest

import cold4, decorated as d, exact_core as e, marked, polygon
from selector import Odds


@lru_cache(maxsize=None)
def per(b):
    return sum(1 for _ in e.matchings(b))


def brute_mark_probability(board,rows,witness):
    n,b=len(board),len(rows)
    owners=tuple(next(j for j in range(b) if rows[j][x]==witness[x]) for x in range(n))
    weight=prod(factorial(n-owners.count(c)) for c in range(b))
    mass=F(weight,per(board)*sum(prod(factorial(n-o.count(c)) for c in range(b))
                              for o in product(range(b),repeat=n)))
    for c,row in enumerate(rows):
        options=sum(all((board[x]>>y)&1 and all(old[x]!=y for old in rows[:c]) and
                   ((y==witness[x])==(owners[x]==c)) for x,y in enumerate(r))
                    for r in permutations(range(n)))
        mass/=options
    return mass


def head(rows,word):
    # Each eligible subset of the canonical packing gives the same inverse
    # odds and same raw atom, so summing its 2^k histories here is exact.
    if word is None: return F(1), 0
    n=len(rows[0]); k=len(polygon.canonical_packing(rows,word))
    # Independent direct counts from two raw permutations and brute labeled
    # marked cycles, summed over all raw permutation arrays (including conflicts).
    z=raw_partition(n)
    return F(1<<k,z), k


@lru_cache(maxsize=None)
def raw_partition(n):
    rows=list(permutations(range(n)))
    total=0
    for a,b in product(rows,repeat=2):
        copies=[]
        for x in range(n):
            for z in range(n):
                if x!=z and a[x]==b[z] and a[z]==b[x]:
                    copies.append(frozenset(((0,x),(0,z),(1,a[x]),(1,a[z]))))
        def rec(i,used):
            if i==len(copies): return 1
            return rec(i+1,used)+(rec(i+1,used|copies[i]) if not used&copies[i] else 0)
        total+=rec(0,frozenset())
    return total


@lru_cache(maxsize=None)
def ordered_audit(rows):
    n=len(rows); h=d.safe_scale(n)
    forward,reverse,sub,tagmass=F(0),F(0),F(0),F(0)
    def add(prior,q,r,t,tag=False):
        nonlocal forward,reverse,sub,tagmass
        assert q*t==r
        forward+=prior*q*t/(h+t)
        reverse+=prior*r*h/(h+t)
        sub+=prior*r*(h/(h+t)-F(1,2)*int(tag))
        tagmass+=prior*r*int(tag)
    for family in range(3):
        if family==1:
            # Through order 4 no predictor recipe can exist with the n/16 cap;
            # each of the n//4 early slots must draw raw with probability 1/2.
            b=e.full_board(n); q=F(1,2**(n//4))
            for row in rows:
                q/=per(b); b=e.delete_matching(b,row)
            add(F(1,3),q,F(1),cold4.reverse(rows).exact(per))
            continue
        # max_half=2: exactly one retained real word with probability 1/1024.
        for word,prior,tag in [(None,F(1,2),True),(None,F(511,1024),False),
                              ((0,1,0,1),F(1,1024),False)]:
            nh=int(word is not None)*2
            b=e.full_board(n)
            q,k=head(rows[:nh],word)
            z=(sum(polygon.mark_counts(n,nh,word)))
            t=F(z,1<<k)
            for row in rows[:nh]: b=e.delete_matching(b,row)
            groups=d._group_count(n,nh,2) if family==2 else 0
            # n=3,4 with b=2 has at most one group.
            assert groups<=1
            i=nh
            if groups:
                rr=rows[i:i+2]
                union=tuple(sum(1<<r[x] for r in rr) for x in range(n))
                pieces=[(q*brute_mark_probability(b,rr,w), F(1,per(union)),
                         t*marked.odds_from_history(b,rr,w).exact(per))
                        for w in e.matchings(union)]
                for row in rr: b=e.delete_matching(b,row)
                i+=2
            else: pieces=[(q,F(1),t)]
            tail=1
            for row in rows[i:]:
                tail*=per(b); b=e.delete_matching(b,row)
            for mq,mr,mt in pieces:
                add(prior/3,mq/tail,mr,mt*tail,tag and family==0)
    return forward,reverse,sub,tagmass


class DecoratedTests(unittest.TestCase):
    def test_every_labeled_target_and_schedule_3_4(self):
        for n in (3,4):
            h=d.safe_scale(n); c=d.SAFE_C
            for target in e.iter_latin(n):
                values=[ordered_audit(tuple(s)) for s in permutations(target)]
                f,g,sub,tagmass=(sum(col,F())/factorial(n) for col in zip(*values))
                self.assertEqual(tagmass,F(1,6))
                self.assertEqual(f,g/h)
                self.assertEqual(sub,g-c)
                self.assertEqual(f*c/(c+sub),c/h)
                self.assertEqual(f*(c/4)/g,c/(4*h))
    def test_seeded_endtoend(self):
        for n in (1,2,3,4,5):
            self.assertTrue(e.is_latin(d.sample_decorated(n,Random(n))))
        self.assertTrue(e.is_latin(d.sample_huber(3,Random(5))))
    def test_invalid_inputs(self):
        with self.assertRaises(ValueError): d.Parameters(4,0)
        with self.assertRaises(ValueError): d.Parameters(4,max_b=5)
        with self.assertRaises(ValueError): d.reverse_path(d.Parameters(2),((0,1),(0,1)))
        with self.assertRaises(ValueError): d.safe_residual_coin(d.Parameters(3),(),1)
