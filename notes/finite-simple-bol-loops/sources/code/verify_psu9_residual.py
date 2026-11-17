"""Exact arithmetic for the PSU9(2) full-socle exclusion.

Run with Python 3.11+ and assertions enabled. Standard library only.
Canonical proof: ../manuscripts/nonbruck-almost-simple-radical-bridge.md,
section "Proposed exclusion of all odd-dimensional unitary full socles".
The eight maximal-subgroup orders/indices are external classification data:
ATLAS U7(2), https://brauer.maths.qmul.ac.uk/Atlas/clas/U72/,
version 2.0, updated 15 April 2005, attributed there to Kleidman's list.
J3 order: https://brauer.maths.qmul.ac.uk/Atlas/spor/J3/.
The unitary class formula is proved in radical-free-unitary-inversion.md,
reviewed source fa462cdffd3082b37b0f100ea7e0364a97832473.
Arithmetic does not prove table completeness, the factorization classification,
parabolic structure or the loop exclusion. No network or loop enumeration.
"""

from math import gcd, prod

def unitary(n,q):
    return q**(n*(n-1)//2)*prod(q**i-(-1)**i for i in range(1,n+1))
def psu(n,q):
    return unitary(n,q)//((q+1)*gcd(n,q+1))
def sp(m,q):
    return q**(m*m)*prod(q**(2*i)-1 for i in range(1,m+1))
T=psu(7,2); S=psu(9,2); j=50232960
classes=[unitary(7,2)//(2**(r*(14-3*r))*unitary(r,2)*unitary(7-2*r,2)) for r in (1,2,3)]
assert T==227787103272960 and S==325473292721108444774400
assert classes==[2709,893970,10727640]
assert all(unitary(7,2) % (2**(r*(14-3*r))*unitary(r,2)*unitary(7-2*r,2)) == 0 for r in (1,2,3))
assert sp(3,2)==1451520 and T%sp(3,2)==0
outer=T//sp(3,2); total=1+sum(classes)+outer
assert outer==156930048 and total==168554368
assert S%j==0
X=S//j
assert X==6479277604208640
P=2**15*T
assert S%P==0 and S//P==43605
assert P*j%S==0 and P*j//S==1152
atlas_orders=[84085309440,82771476480,5945425920,2548039680,246343680,16796160,3674160,301]
atlas_indices=[2709,2752,38313,89397,924672,13561856,61997056,756767784960]
assert all(T//o==i and T%o==0 for o,i in zip(atlas_orders,atlas_indices))
small=[i for i in atlas_indices if i<=6912]
assert small==[2709,2752]
assert all((1152*a)%i for a in (1,2,3,6) for i in small)
cap=12*2**15*total
assert cap==66278274367488 and cap<X
print('PSU7, PSU9:',T,S)
print('internal rank 1,2,3:',classes,'outer:',outer,'total:',total)
print('degree, P1 index, intersection base:',X,S//P,P*j//S)
print('ATLAS maximal indices:',atlas_indices)
print('small indices:',small,'no divisor of 1152a for a|6')
print('capacity:',cap,'< degree:',X)
