"""Small finite model tests; a bit path, not a Monte Carlo tolerance, is the oracle."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations,product
from random import Random
from unittest import TestCase, main

import glmp_pm as g


class Tape:
    def __init__(self,values):self.values=iter(values)
    def getrandbits(self,k):
        t=next(self.values);assert 0<=t<1<<k
        return t


class GLMP(TestCase):
    def test_every_single_step_bit_pair(self):
        for b in ((3,2),(2,1),(3,3)):
            n=len(b); a=tuple(g.cooling(b))[-1]; w=(F(2,3),F(9,7),F(4),F(1))
            states=set(permutations(range(n)))
            for s in list(states):
                for i in range(n):states.add(s[:i]+(-1,)+s[i+1:])
            for s in states:
                ref=defaultdict(F)
                for i,j in product(range(8),repeat=2):
                    ref[g.step(b,a,w,s,3,Tape([i,j]))]+=F(1,64)
                self.assertEqual(ref,g.kernel(b,a,w,s,3))

    def test_unrounded_jsv_reversible(self):
        n=3;b=(3,7,6); a=tuple(g.cooling(b))[-1];w=tuple(F(i+3,i+1) for i in range(9))
        states=set(permutations(range(n)))
        for s in list(states):
            for i in range(n):states.add(s[:i]+(-1,)+s[i+1:])
        from collections import Counter
        for s in states:
            for t,k in Counter(g._neighbor(s,i) for i in range(4*n)).items():
                k2=sum(g._neighbor(t,i)==s for i in range(4*n))
                self.assertEqual(k,k2)
                u,v=g._weight(b,a,w,s),g._weight(b,a,w,t)
                self.assertEqual(u*k*min(F(1),v/u),v*k2*min(F(1),u/v))

    def test_full_attempt_and_restarts_bit_enumeration(self):
        b=(3,3); c=g.Clock(1,1,2,2,2,F(1,2))
        counts=defaultdict(F)
        for tape in product(range(4),repeat=4):
            counts[g.attempt(b,c,Tape(tape))]+=F(1,4**4)
        self.assertEqual(set(counts)|{None},set(g.attempt_law(b,c)))
        for s,q in counts.items():self.assertEqual(q,g.attempt_law(b,c)[s])
        capped=defaultdict(F)
        for x,px in counts.items():
            if x is not None: capped[x]+=px
            else:
                for y,py in counts.items():
                    capped[g.fallback(b) if y is None else y]+=px*py
        self.assertEqual(capped,g.approximate_law(b,c))

    def test_cooling_update_and_correction(self):
        b=(7,7,6); c=g.Clock(10,5,8,2,4,F(5,6))
        sched=list(g.cooling(b));self.assertEqual(sched[-1],(1,1,F(1,6)))
        self.assertTrue(all(F(3,4)<=v/u<=1 for a,z in zip(sched,sched[1:]) for u,v in zip(a,z)))
        one=g.attempt_law(b,c)
        self.assertGreater(one[None],0);self.assertLess(one[None],1);self.assertEqual(sum(one.values()),1)
        Q=g.approximate_law(b,c);h=g.correction_table(b,c);self.assertEqual(len(h),4)
        self.assertEqual({(1-c.correction)*Q.get(s,0)+c.correction*v for s,v in h.items()},{F(1,4)})
        sample=g.checked_sampler(b,c)
        out={sample(Random(i)) for i in range(70)}
        self.assertEqual(out,set(h))
        invalid=g.Clock(1,1,1,1,3,F(1,100))
        with self.assertRaises(ValueError):g.correction_table(b,invalid)

    def test_empty_impossible_and_reset(self):
        for b in [(),(1,)]:
            c=g.Clock(1,1,1,1,1,F(1))
            self.assertEqual(g.sample_admitted(b,c),tuple(range(len(b))))
        with self.assertRaises(ValueError):g.fallback((1,1))
        self.assertEqual(g.fallback((2,1)),(1,0))
        self.assertEqual(g.chain_law((2,1),(1,1),(2,)*4,0,3),{(1,0):F(1)})


if __name__=='__main__':main()


class Lazy(TestCase):
    def test_exact_rounded_lazy_kernel(self):
        for b in ((3,2),(2,1),(3,3)):
            a=tuple(g.cooling(b))[-1]; w=(F(2,3),F(9,7),F(4),F(1))
            states=set(permutations(range(2)))
            for s in list(states):
                for i in range(2): states.add(s[:i]+(-1,)+s[i+1:])
            for s in states:
                law=defaultdict(F)
                for tape in product(range(2),repeat=6):
                    law[g.step_lazy(b,a,w,s,3,Tape(tape))]+=F(1,64)
                self.assertEqual(law,g.kernel(b,a,w,s,3))
    def test_big_clock_construction_and_first_coin(self):
        c=g.research_clock((3,2))
        self.assertGreater(c.correction_exponent,10**9)
        self.assertFalse(g._correction_coin(c,Tape([1])))
        b=(2,1); a=(F(3,4),F(1)); w=(F(2),)*4
        t=g.step_lazy(b,a,w,(1,0),c.bits,Random(20))
        self.assertIn(t,{(1,0),(-1,0),(1,-1)})
