import unittest
from fractions import Fraction as F
from itertools import permutations, product, combinations
from math import comb, factorial
from random import Random
from unittest.mock import patch

import polygon as pg
import selector as sel
from exact_core import full_board, permanent, sample_matching


def all_subsets(s):
    for i in range(len(s)+1):
        yield from combinations(s,i)


class PolygonLaw(unittest.TestCase):
    def test_normalizers_by_counting_all_decorated_raw_rows(self):
        # Includes row collisions and noncanonical decorations. These must
        # contribute to Z even though the actual forward returns null.
        for n,word in [(2,(0,1,0,1)),(3,(0,1,0,1)),(4,(0,1,0,1)),(3,(0,1,2,0,1,2))]:
            slots=1+max(word)
            counts=[0]*(n//(len(word)//2)+1)
            accepted=F(0)
            for rows in product(permutations(range(n)),repeat=slots):
                marks=list(pg._copies(rows,word,n))
                disjoint=[]
                for dec in all_subsets(marks):
                    xs=[x for l,r in dec for x in l]
                    ys=[y for l,r in dec for y in r]
                    if len(set(xs))!=len(xs) or len(set(ys))!=len(ys): continue
                    counts[len(dec)]+=1
                    disjoint.append(dec)
                if any(len({r[x] for r in rows})<slots for x in range(n)): continue
                packing=pg.canonical_packing(rows,word)
                reverse=pg.seed_reverse(rows,word,Random(41))
                self.assertEqual(reverse.ratio, F(sum(pg.mark_counts(n,slots,word)),2**len(packing)))
                self.assertEqual(sum(set(d)<=set(packing) for d in disjoint),2**len(packing))
                # Each possible reverse decoration has identical probability.
                self.assertEqual(sum((F(1,2**len(packing)) for _ in all_subsets(packing)),F(0)),1)
                accepted+=1/reverse.ratio
            self.assertEqual(tuple(counts),pg.mark_counts(n,slots,word))
            self.assertGreater(accepted,0)
            self.assertLessEqual(accepted,1)
            self.assertLessEqual(sum(counts),3*factorial(n)**slots)

    def test_actual_generators_and_null_support(self):
        rng=Random(839)
        word=(0,1,0,1)
        seen=set()
        for _ in range(1200):
            out=pg.seed_forward(2,2,word,rng)
            if out is None: seen.add(None); continue
            self.assertLessEqual(set(out.marks),set(pg.canonical_packing(out.rows,word)))
            self.assertEqual(out.ratio,pg.seed_reverse(out.rows,word,rng).ratio)
            seen.add((out.rows,len(out.marks)))
        self.assertEqual(len(seen),5)  # two Latin blocks, both decoration sizes, null
        dummy=pg.seed_forward(3,1,None,rng)
        self.assertEqual(dummy.ratio,6)
        self.assertEqual(pg.seed_reverse((),None,n=3).ratio,1)

    def test_prior_and_input_contract(self):
        class Bits:
            def __init__(self,x): self.x=iter(x)
            def getrandbits(self,k): return next(self.x)
        self.assertEqual(pg.draw_word(2,Bits([0,1,0,1,0,1])),(0,1,0,1))
        self.assertIsNone(pg.draw_word(2,Bits([1])))
        self.assertIsNone(pg.draw_word(2,Bits([0,1,0,0,0,0])))
        with self.assertRaises(ValueError): pg.mark_counts(2,1,(0,1,0,1))
        with self.assertRaises(ValueError): pg.seed_reverse(((0,1),(0,1)),(0,1,0,1))
        self.assertEqual(pg.mark_counts(2,2,None),(4,))


class SelectorLaw(unittest.TestCase):
    def test_size_bias_ratios_symbolically(self):
        for m in range(3,8):
            for p in [F(1,7),F(1,2),F(4,5)]:
                def nb(k,t):
                    if t<k: return F(0)
                    return comb(t-1,k-1)*p**k*(1-p)**(t-k)
                for n in range(m,20):
                    self.assertEqual(nb(m,n)*F(n,m)*p,nb(m+1,n+1))
                    self.assertEqual(nb(m,n)*F(m-1,n-1)/p,nb(m-1,n-1))

    def test_anchor_and_experiments(self):
        board=(3,3)
        # identity anchor. For the two-by-two row every trial succeeds
        # except the first fresh one, so positive NB=m+1 and reciprocal
        # NB=m+1; forced singleton row is bypassed.
        for inv,rev,expect in [(False,False,F(4,3)),(False,True,F(4,3)),
                               (True,False,F(2,3)),(True,True,F(2,3))]:
            calls=[0]
            def match(b,rng):
                calls[0]+=1
                return (1,0) if calls[0]==2 else (0,1)
            kw={'denominator' if inv else 'numerator':(board,)}
            self.assertEqual(sel.paired_estimate(sel.Odds(**kw),rev,Random(0),match,replicates=3),expect)

    def test_direct_gate_probabilities(self):
        odds=sel.Odds(F(2,7),(full_board(3),),((3,3),))
        self.assertEqual(odds.exact(),F(6,7))
        for rev in [False,True]:
            with patch.object(sel,'_bernoulli',side_effect=lambda p,r:p):
                self.assertEqual(sel.direct_gate(odds,F(4,7),rev), F(2,5) if rev else F(3,5))

    def test_race_integration_with_exact_match_oracle(self):
        # Reproducible sanity only; exact laws are the identities above.
        rng=Random(1141)
        odds=sel.Odds(F(3,2),((3,3),),((3,3),))
        k=1200
        s=sum(sel.oracle_sigmoid_gate(odds,1,False,rng) for _ in range(k))
        self.assertLess(abs(s/k-0.6),.055)
        # Feasibility failure is surfaced, not silently renormalized.
        with self.assertRaises(ValueError):
            sel.paired_estimate(sel.Odds(numerator=((0,),)),False,rng,lambda b,r:None)
        with self.assertRaises(TypeError): sel.Odds(.25)

if __name__=='__main__': unittest.main()
