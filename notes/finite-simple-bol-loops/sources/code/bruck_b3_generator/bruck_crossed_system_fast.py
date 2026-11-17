import runpy,contextlib,io,collections,time,functools
with contextlib.redirect_stdout(io.StringIO()):
 t=runpy.run_path('bruck_b3_action_lifts.py')
assert not t['bad']; sh=t['sh']; d=t['d']; sol=t['sol']; f=t['f']; beta=t['beta']; G=sh['G']; unit=sh['unit']; mul=sh['mul']; e=sh['e']; actV=t['actV'];actZ=t['actZ'];gens=t['Gens']; inv=sh['inverse']; n=30
# Apply the two corrected generator automorphisms. Corrections are indexed by output v.
def step(i,v,z):
 w,z=t['step'](i,v,z)
 if i>0:
  for j in range(n):
   if w>>j&1:z^=(sol>>((i-1)*n*8+j*8))&255
 else:
  # undo L on the original input, before applying the inverse action on Z
  g=-i-1; raw=0
  for j in range(n):
   if v>>j&1:raw^=(sol>>(g*n*8+j*8))&255
  z^=actZ(raw,inv(gens[g]))
 return w,z
# Positive words only; section word has quotient kernel component shadow w_g.
words={unit:()}; queue=collections.deque([unit])
while queue:
 g=queue.popleft()
 for i,h in enumerate(gens):
  gh=mul(g,h)
  if gh not in words:words[gh]=words[g]+(i+1,);queue.append(gh)
assert len(words)==120
shadow={}
for g in G:
 v,h=sh['word'](sh['C'],sh['D'],words[g]);assert h==g;shadow[g]=v
# The word lift has shadow w; correcting on the left by w gives section action.
@functools.lru_cache(None)
def alpha(g,v,z):
 for i in reversed(words[g]):v,z=step(i,v,z)
 return v,z^beta(shadow[g],v)
# central symbolic bits hold 1920 variables and one constant bit.
NV=120*2*8;CONST=1<<NV; index={g:i for i,g in enumerate(G)}
def symfactor(g,k):return [1<<((index[g]*2+k)*8+j) for j in range(8)]
def applyz(g,z):
 out=[0]*8
 for j in range(8):
  a=actZ(1<<j,g)
  for k in range(8):
   if a>>k&1:out[k]^=z[j]
 return out
def xor(*vs):return [__import__('functools').reduce(int.__xor__,xs,0) for xs in zip(*vs)]
def const(v):return [CONST if v>>i&1 else 0 for i in range(8)]
# Factors as (V, symbolic Z); inverse (v,z+f(v,v)).
def pmul(a,b):return (a[0]^b[0],xor(a[1],b[1],const(f(a[0],b[0]))))
def pinv(a):return (a[0],xor(a[1],const(f(a[0],a[0]))))
def pa(g,a):
 v,z=alpha(g,a[0],0);return v,xor(applyz(g,a[1]),const(z))
zero=[0]*8; fac={}
for g in G:
 fac[g,unit]=(0,zero)
 for h in G:
  if h==unit:continue
  pr=unit
  for j,i in enumerate(words[h]):
   hk=mul(pr,gens[i-1]); gh=mul(g,pr)
   # equation alpha_g(f(pr,k)) f(g,pr*k)=f(g,pr) f(g*pr,k)
   z=pmul(pinv(pa(g,(e(pr,gens[i-1]),symfactor(pr,i-1)))),pmul(fac[g,pr],(e(gh,gens[i-1]),symfactor(gh,i-1))))
   assert z[0]==e(g,hk)
   if (g,hk) not in fac:fac[g,hk]=z
   pr=hk
# row reduction streaming; low-bit pivots and descending substitution.
piv={}; bad=0; count=0; mask=CONST-1

def add(row):
 global bad,count
 count+=1
 while row&mask:
  j=(row&-row).bit_length()-1
  if j in piv:row^=piv[j]
  else:piv[j]=row;return
 if row&CONST:bad+=1
for k in range(2):
 for row in symfactor(unit,k):add(row)
for gi,g in enumerate(G):
 for h in G:
  for kidx,k in enumerate(gens):
   l=pmul(pa(g,fac[h,k]),fac[g,mul(h,k)])
   r=pmul(fac[g,h],fac[mul(g,h),k]);assert l[0]==r[0]
   for row in xor(l[1],r[1]):add(row)
 if gi%20==0:print('processed',gi,'rank',len(piv),'inconsistent rows',bad,flush=True)
print('central associativity:',NV,'variables',count,'equations rank',len(piv),'inconsistent rows',bad,flush=True)
if bad:raise SystemExit(1)
ans=0
for j in sorted(piv,reverse=True):
 if ((piv[j]&ans).bit_count()&1)^bool(piv[j]&CONST):ans|=1<<j
assert all(((row&ans).bit_count()&1)==bool(row&CONST) for row in piv.values())
print('solution integer',ans,flush=True)
def evaluate(a):return a[0],sum(((r&ans).bit_count()&1 ^ bool(r&CONST))<<j for j,r in enumerate(a[1]))
F={(g,h):evaluate(v) for (g,h),v in fac.items()}
f=functools.lru_cache(None)(f)
mul=functools.lru_cache(None)(mul)
def mult(a,b):return (a[0]^b[0],a[1]^b[1]^f(a[0],b[0]))
print('fast mode: exhaustive audits omitted')
