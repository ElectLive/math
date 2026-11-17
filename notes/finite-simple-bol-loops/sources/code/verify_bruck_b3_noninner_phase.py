#!/usr/bin/env python3
"""Second-central top-shear phase using the immutable 22db phase verifier.

Run from the repository root with Python 3.12 and assertions enabled. --probe
checks the aligned base only. The full sweep is proposed evidence, not a review.
The external involution represents the automorphism eta; no loop is constructed.
"""
import ast
import contextlib
import io
import hashlib
import os
from pathlib import Path
import sys

assert __debug__
code_dir=Path(__file__).resolve().parent
root=code_dir.parents[2]
os.chdir(root)
expected={
 'verify_bruck_b3_affine_phase.py':'694b31e0463eab0f7e66501a18063a326dd71cc008e5fa70020620b7284f6298',
 'verify_bruck_n_quadratic_support.py':'68f3d80229609d2217608c69cc203fc49176a6509f3fb5c476c3805bbe0e675d',
 'verify_bruck_one_m_noncentral.py':'59c0ed355bffdf316d93c37f99f2094acc4a09b2eff3db13459f9d208782e15a',
 'verify_bruck_p6_frattini.py':'9e42fe025aaa9dce6690badef3145da2f9a2dffb56670136fe63435b02358705',
}
for name,digest in expected.items():
 assert hashlib.sha256((code_dir/name).read_bytes()).hexdigest()==digest,(name,'does not match 22db source')
text=(code_dir/'verify_bruck_b3_affine_phase.py').read_text()
tree=ast.parse(text)
SOURCES=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(x,ast.Name) and x.id=='SOURCES' for x in n.targets))

def replace_once(s,old,new):
 assert s.count(old)==1,('source transformation mismatch',old)
 return s.replace(old,new)

source=SOURCES['phase']
source=replace_once(source,'def conj(a,b):return prod(prod(a,b),inverse(a))','''def top(v):return ((v>>6)&15)^((v>>10)&15)
def eta(x):
 (v,z),g=x
 return ((v,z^(top(v)<<4)),g)
def conj(a,b):return prod(prod(eta(a),b),inverse(a))
def markprod(a,b):return prod(eta(a),b)
# Verify the derivation identity on all quotient factors and action bases.
for g in G:
 for i in range(30):
  v=1<<i;tv,_=alpha(g,v,0)
  assert top(tv)==(actZ(top(v)<<4,g)>>4)
 for h in G:
  assert top(F[g,h][0])==0
for v in s['basis']:assert top(v)==0
for g in K:
 assert top(s['xv'][g])==0
 assert eta(H[g])==H[g]
assert top(1<<6)!=0
''')
source=replace_once(source,'prod(((0,z),t),((0,z),t))==id','markprod(((0,z),t),((0,z),t))==id')
source=replace_once(source,'basep=prod(prod(lam,mu),inverse(H[dd]))','basep=prod(markprod(lam,mu),inverse(H[dd]))')
source=replace_once(source,'cols.append(prod(prod(aa,bb),inverse(H[dd]))[0][0]^basep[0][0])','cols.append(prod(markprod(aa,bb),inverse(H[dd]))[0][0]^basep[0][0])')
source=replace_once(source,'pp=prod(prod(conj(p,lam),conj(q,mu)),inverse(H[dd]))','pp=prod(markprod(conj(p,lam),conj(q,mu)),inverse(H[dd]))')
SOURCES['phase']=source
__WORKSPACE__=str(root)
# Reuse the exact committed basis checks and full two-case matrix sweep.
tail=text[text.index('\ndef load(name):'):]
exec(compile(tail,'<pinned-phase-driver>','exec'))
