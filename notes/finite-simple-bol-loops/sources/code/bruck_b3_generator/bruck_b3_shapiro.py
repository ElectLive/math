"""Nonzero S5 extension by P6 via explicit Shapiro C5:C8 carry cocycle."""
import runpy,contextlib,io,itertools
with contextlib.redirect_stdout(io.StringIO()):a=runpy.run_path('../verify_bruck_one_m_noncentral.py')
comp=a['comp'];inv=a['inv'];power=a['power'];G=a['queue'];F=a['F'];unit=a['I'];fixed=a['fixed'][0];p=a['p'];q=a['qgen'];
def mul(x,y):return (comp(x[0],y[0]),comp(x[1],y[1]))
def inverse(x):return (inv(x[0]),inv(x[1]))
Fdata={mul((power(p[0],i),power(p[1],i)),(power(q[0],j),power(q[1],j))):(i,j) for i in range(5) for j in range(4)}
assert len(Fdata)==20 and set(Fdata)==set(F)
rep={}
for g in G:rep.setdefault(g[1][fixed],g)
assert len(rep)==6 and rep[fixed]==unit

def schreier(g,x):
 y=g[1][x];z=mul(mul(inverse(rep[y]),g),rep[x]);return Fdata[z]

def e(g,h):
 bits=0
 for x in range(6):
  i,j=schreier(g,h[1][x]);k,l=schreier(h,x)
  if j+l>=4:bits|=1<<(g[1][h[1][x]])
 return bits

def act(g,v):return a['pact'](v,g[1])
def extmul(x,y):
 v,g=x;w,h=y;return (v^act(g,w)^e(g,h),mul(g,h))
def extinv(x):
 v,g=x;gi=inverse(g);return (act(gi,v^e(g,gi)),gi)
def word(c,d,terms):
 out=(0,unit)
 for i in terms:
  out=extmul(out,c if i==1 else d if i==2 else extinv(c if i==-1 else d))
 return out
C=((0,(a['c5'],a['c6'])));D=((0,(a['d5'],a['d6'])))
rels=[[1,1],[2,2,2,2],[1,2]*5,[-1,-2,1,2]*3]
for R in rels:
 v,g=word(C,D,R);assert g==unit;print('relator',len(R),'P6-shadow',v)
for g in G:
 for h in G:
  for k in (unit,C[1],D[1]):
   assert e(g,h)^e(mul(g,h),k)==act(g,e(h,k))^e(g,mul(h,k))
print('Shapiro cocycle passed 43200 generator cocycle checks; stabilizer F',len(F))
X=(0,q);xx=(0,unit)
for _ in range(4):xx=extmul(xx,X)
# C5 average kills the S-block and retains the induced fixed line.
v=xx[0];avg=0
for i in range(5):avg^=act((power(p[0],i),power(p[1],i)),v)
assert avg==63
print('F C4 fourth-power shadow',v,'C5 average',avg,'= constant')

