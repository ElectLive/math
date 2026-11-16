#!/usr/bin/env python3
"""Candidate 192 folder, opposite of right Nagy convention; finite non-simplicity witness."""
from bol_engine import _atkinson_is_primitive_raw, bol_folder_from_perms
from known_constructions import _nagy_exp2_base_data
D=_nagy_exp2_base_data()
def pair(p,b): return tuple(p)+(41,40) if b else tuple(p)+(40,41)
J,J0=set(D['J']),set(D['J0'])
assert len(J)==32 and len(J0)==16 and J0<=J
G=[pair(g,b) for g in D['G'] for b in range(2)]
H=[pair(h,0) for h in D['H']]
K=[pair(j,int(j not in J0)) for j in sorted(J)] + [pair(c,b) for c in D['c_class'] for b in range(2)]
assert (len(G),len(H),len(K))==(7680,40,192)
result=bol_folder_from_perms(42,G,H,K,verify_conjugate_transversals=True)
print('folder:',result.is_valid,result.reason,flush=True)
assert result.is_valid and result.loop is not None
Q=result.loop
primitive=_atkinson_is_primitive_raw(192,list(Q.L[1:])+list(Q.R[1:]))
print('multiplication group primitive:',primitive,flush=True)
for i in range(1,192):
 roots=Q.minimal_congruence_roots(i); size=sum(x==roots[0] for x in roots)
 if 1<size<192:
  valid=Q.verify_is_loop_congruence(roots)
  print('witness index:',i,'normal subloop order:',size,'congruence verified:',valid,flush=True)
  assert size==96 and valid and not primitive
  break
else: raise AssertionError('no nontrivial congruence found')
