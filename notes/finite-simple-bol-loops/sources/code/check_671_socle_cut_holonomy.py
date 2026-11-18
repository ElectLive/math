"""Independent S5/A5-controls. No loop assertion for the samples."""
from itertools import permutations,product,combinations
from collections import Counter,deque
P=list(permutations(range(5)));E=0;ii={p:i for i,p in enumerate(P)}
M=[[ii[tuple(a[t] for t in b)] for b in P] for a in P];I=[r.index(E) for r in M]
sign=[sum(x>y for x,y in combinations(p,2))%2 for p in P]
cyc=lambda z:sum(a!=b for a,b in enumerate(P[z]))
inv=[a for a in range(120) if I[a]==a]; ctr=Counter(cyc(a) for a in inv); dbl=next(a for a in inv if cyc(a)==4)

def cuts():
 K=[(I[g],g,s) for g,s in product(range(120),inv)]
 H=[(g,g,dbl if sign[g] else E) for g in range(120)]
 A=[h for h in H if not any(sign[a] for a in h)];w=0;collapse=0;corr=0
 def parity(x):return sum(sign[g]<<i for i,g in enumerate(x))
 for D in range(8):
  C=[i for i in range(3) if not (D>>i)&1];B=[i for i in range(8) if i&D==i];ss=[frozenset((0,))]
  for v in B:
   for F in ss[:]:
    G=F|{x^v for x in F}
    if G not in ss:ss.append(G)
  for Bprime in ss:
   cos=lambda v:min(v^x for x in Bprime)
   test=lambda a:parity(a) in Bprime and all(a[i]==E for i in C)
   images={(cos(parity(k)),tuple(k[i] for i in C)) for k in K}
   # One class for either swap parity and actual third involution class.
   sig={}
   for p,t in product((0,1),ctr):
    top=3*p+4*(t==2); key=(cos(top),t if 2 in C else None)
    sig[key]=(60 if 0 in C or 1 in C else 1)*(ctr[t] if 2 in C else 1)
   assert len(images)==sum(sig.values());collapse+=len(sig)<6
   Nker=sum(all(h[i]==E for i in C) for h in A);Ac={tuple(h[i] for i in C) for h in A};J={parity(h) for h in H};pred=0
   for j in J&Bprime:
    h=next(h for h in H if parity(h)==j)
    if tuple(h[i] for i in C) in Ac:pred+=Nker
    else:corr+=1
   assert pred==sum(test(h) for h in H);w+=1
 print('S5^3/A5^3, all parity subspaces supported on each deleted coordinate set: cases / observed signature collisions / correlated stabilizer-coset misses',w,collapse,corr)

def holonomy():
 # Reverse a 3-cycle of A5 factors, represented by real S5 arrows (parity outer). Use positive orientation i->i+1; a sends i->-i.
 Eset=[j for j in range(120) if not sign[j]];rot=(1,2,0);rev=(0,2,1)
 def mul(g,h):return tuple(g[0][k] for k in h[0]),tuple(M[g[1][h[0][j]]][h[1][j]] for j in range(3))
 def iso(p,h):return(p,tuple(h))
 one=((0,1,2),(0,0,0));S=0;candidates=0
 for fix,c,top0,top1 in product([next(g for g in inv if cyc(g)==k) for k in (0,2,4)],(0,next(g for g in range(120) if sign[g])),(0,1),(0,1)):
  a=iso(rev,[fix,c,I[c]]);j=(top0,top1,top0^top1);u=tuple(sign[t] for t in a[1]);tops=(rot,j)
  def om(g,h):return tuple(g[0][k] for k in h[0]),tuple((g[1][h[0][i]]^h[1][i]) for i in range(3))
  if om(om((rev,u),tops),(rev,u))!=om(tops,tops):continue
  found=0;tot=set()
  for b in range(120):
   if sign[b]!=j[0]:continue
   for h in range(120):
    if sign[h]!=j[1]:continue
    z=iso(rot,[b,h,I[M[h][b]]]);assert mul(mul(z,z),z)==one;tot.add(z);found+=mul(mul(a,z),a)==mul(z,z)
  assert found and len(tot)==3600;candidates+=len(tot);S+=1
  # Verifies conjugacy order, independently of the chosen fixed a: stabilizer of one cyclic lift in A5^3 has order 60 via transported single base element.
  z=next(iter(tot));stab=0
  for g in Eset:
   t=g;arr=[t]
   for h in z[1][:-1]:t=M[M[h][t]][I[h]];arr.append(t)
   f=iso(one[0],arr);stab+=mul(f,z)==mul(z,f)
  assert stab==60 and 60**3//stab==len(tot)
 print('Odd dihedral reversal with actual S5 arrows, fixed actual classes / full-order lifts checked: ',S,candidates)
if __name__=='__main__':cuts();holonomy()
