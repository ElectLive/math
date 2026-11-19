import unittest
from collections import defaultdict
from fractions import Fraction as F
from itertools import permutations,product
from math import factorial,prod
from random import Random
import marked
from exact_core import full_board,matchings,permanent

def brute(board,b,masked):
    """Independent exact forward decision tree, aggregating ordered rows+mark."""
    n=len(board); perms=list(permutations(range(n)))
    mlist=list(matchings(board)) if masked else perms
    ws={}
    for owners in product(range(b),repeat=n):
        ws[owners]=prod(factorial(n-owners.count(j)) for j in range(b))
    tot=sum(ws.values())
    out=defaultdict(F)
    for mark in mlist:
        for owners,w in ws.items():
            def rec(rows,prob):
                c=len(rows)
                if c==b:
                    out[tuple(rows),mark]+=prob
                    return
                options=[]
                for row in perms:
                    if any(owners[x]==c and y!=mark[x] for x,y in enumerate(row)): continue
                    if masked and any(not (board[x]>>y)&1 or
                            any(old[x]==y for old in rows) or
                            (owners[x]!=c and y==mark[x]) for x,y in enumerate(row)): continue
                    options.append(row)
                for row in options:
                    if any(not (board[x]>>y)&1 or any(old[x]==y for old in rows)
                           for x,y in enumerate(row)): continue
                    rec(rows+[row],prob/len(options))
            rec([],F(w,tot*len(mlist)))
    return out

class Marked(unittest.TestCase):
    def test_forward_reverse_measure_identity_exhaustively(self):
        for n,b,board in [(2,1,full_board(2)),(3,2,full_board(3)),
                          (3,2,(6,5,3)),(3,3,full_board(3))]:
            for masked in (True,False):
                probs=brute(board,b,masked)
                self.assertTrue(probs)
                self.assertLessEqual(sum(probs.values()),1)
                if b>=2: self.assertLess(sum(probs.values()),1)
                for (rows,m),value in probs.items():
                    support=tuple(sum(1<<r[i] for r in rows) for i in range(n))
                    rev=F(1,permanent(support))
                    odds=marked.odds_from_history(board,rows,m,masked=masked)
                    self.assertEqual(value*odds.exact(),rev)
                rng=Random(192)
                for _ in range(24):
                    a=marked.forward_history(board,b,rng,masked=masked)
                    if a is None: continue
                    self.assertIn((a.rows,a.mark),probs)
                    self.assertEqual(a.odds,marked.odds_from_history(board,a.rows,a.mark,masked=masked))
                    r=marked.reverse_history(board,a.rows,rng,masked=masked)
                    self.assertIn((r.rows,r.mark),probs)
    def test_composition_and_feasibility(self):
        for n in (1,2,3,4):
            for b in range(1,n+1):
                ways=sum(prod(factorial(n-k.count(c)) for c in range(b)) for k in product(range(b),repeat=n))
                self.assertEqual(marked.normalizer(n,b),factorial(n)*ways)
                self.assertEqual(sum(marked.sample_counts(n,b,Random(4))),n)
        for masks in product(range(8),repeat=3):
            self.assertEqual(marked._feasible(masks),bool(permanent(masks)))
        self.assertIsNone(marked.forward((0,0),1,Random(0)))
if __name__=='__main__': unittest.main()
