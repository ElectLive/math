exec(open('bruck_two_n_c1_b3_control.py').read().split('for v in basis+')[0])
# q-basis indexed X, U(i,k), cross(i,k), pair(i,j,k), using full d equations.
from functools import lru_cache
full=d['allrows'];QX=sols(d['groups']['X'],full);QU=sols(d['groups']['U0'],full);Qpair=sols(d['groups']['U0U1'],full)
def pairval(c,x,y):return qco(c,U(x,0)|U(y,1))
psi=next(c for c in [Qpair[0],Qpair[1],Qpair[0]^Qpair[1]] if all(pairval(c,v,v)==0 for v in range(256)))
epspsi=next(c for c in [Qpair[0],Qpair[1],Qpair[0]^Qpair[1]] if all(pairval(c,x,y)==pairval(psi,eps(x),y) for x in (1,2,4,8,16,32,64,128) for y in (1,2,4,8,16,32,64,128)))
terms=[('X',0,0,QX[0])]
for i in range(3):
 for k,c in enumerate(QU):terms.append(('U',i,k,c))
for i in range(3):
 for k,c in enumerate(cross):terms.append(('XU',i,k,c))
for i in range(3):
 for j in range(i+1,3):
  for k,c in enumerate((psi,epspsi)):terms.append(('PAIR',3*i+j,k,c))
@lru_cache(None)
def termval(index,v):
 typ,i,k,c=terms[index];x=v&63;u=[(v>>(base+8*j))&255 for j in range(3)]
 if typ=='X':return qco(c,x)
 if typ=='U':return qco(c,U(u[i],0))
 if typ=='XU':return qco(c,x|U(u[i],0))
 return qco(c,U(u[i//3],0)|U(u[i%3],1))
samples=basis+[x^y for x,y in itertools.combinations(basis,2)]
eq=[]
for v in samples:
 for bit in range(4):eq.append(sum(((termval(i,v)>>bit)&1)<<i for i in range(len(terms))))
# find one form with β(1,U) row e1 and C0_12=1. use affine solve via extra RHS variable.
def solve(required):
 rows=eq[:]
 for i,val in required.items():rows.append((1<<i)|((val&1)<<len(terms)))
 homogeneous=null(rows,len(terms)+1)
 good=next((x for x in homogeneous if x>>len(terms)&1),None)
 return None if good is None else good&((1<<len(terms))-1)
# identify β(1,U) from each term as binary top row (3 bits)
def r1(idx):
 v=0
 for j in range(3):
  u=U(Dc[0],j)
  if termval(idx,one^u)^termval(idx,one)^termval(idx,u):v|=1<<j
 return v
rowsR=[]
for j in range(3):rowsR.append(sum(((r1(i)>>j)&1)<<i for i in range(len(terms))))
psi12=next(i for i,t in enumerate(terms) if t[:3]==('PAIR',1,0))
# impose the linear rows, values 100 (e1) and noncentral C0_12=1.
reqrows=rowsR+[1<<psi12];rhs=[1,0,0,1]
mat=eq+[r|(v<<len(terms)) for r,v in zip(reqrows,rhs)]
sol=next((x for x in null(mat,len(terms)+1) if x>>len(terms)&1),None)
print('terms',len(terms),'equation rank',rank(eq),'noncentral allowed',bool(sol))
if sol:
 coef=sol&((1<<len(terms))-1);print('chosen form',[(terms[i][:3]) for i in range(len(terms)) if coef>>i&1])
 # find independent zero-d form with β(1)=0 (so total R1 rank1) and output pair
 d0indices=[i for i,(typ,ii,kk,_) in enumerate(terms) if typ=='X' or (typ=='U' and kk==1)]
 mat0=eq+rowsR+[1<<i for i in d0indices]
 cand=[x for x in null(mat0,len(terms)) if x and x!=coef]
 print('d0 candidates basis',len(cand))
 if cand:print('d0 form',[(terms[i][:3]) for i in range(len(terms)) if cand[0]>>i&1])
if sol:
 def evalform(v):
  out=0
  for i in range(len(terms)):
   if coef>>i&1:out^=termval(i,v)
  return out
 def tact(v):
  out=d['baseact'](v&63,d['c6'])
  for j in range(3):out^=U(a['uact']((v>>(base+8*j))&255,d['c5']),j)
  return out
 im=[(1<<i)^nact(1<<i,d['c5']) for i in range(4)]
 vectors=[1<<i for i in range(30)]; samples=vectors+[x^y for x,y in itertools.combinations(vectors,2)]
 img=[evalform(v)^evalform(tact(v))^evalform(v^tact(v)) for v in samples]
 print('marked d rank mod im',rank(im+img)-rank(im))
