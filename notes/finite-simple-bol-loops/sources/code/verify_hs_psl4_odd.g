# Uniform q=3 mod 4 count; positivity is proved for real q>=3.
# GAP exact rational-polynomial arithmetic, no table or group-data verification.
q:=Indeterminate(Rationals,"q");; x:=Indeterminate(Rationals,"x");;
n:=q^6*(q^2-1)*(q^3-1)*(q^4-1)/2;;
c1:=q^2*(q-1)*(q+1)^2*(q^2+1);;
c2:=q^2*(q-1)^3*(q+1)^2;;
c3:=(q^3-1)*(q^3-q)*(q^3-q^2)/2;;
c4:=q^4*(q^2-1)*(q^4-1);;
c6:=q^2*(q^2-1)^2;; c7:=q^2*(q^4-1);;
A:=n/c1+n/c2;; D:=n/c3;; S:=2*n/c4;; O:=n/c6;; H:=n/c7;;
bounds:=[2*H+2*D*S,2*(S+O)+2*A*S,2*D+2*S*H,1+2*A+2*S*O+S^2/2];;
for bound in bounds do
 r:=1-bound/n;;
 num:=CoefficientsOfUnivariatePolynomial(Value(NumeratorOfRationalFunction(r),3+x));;
 den:=CoefficientsOfUnivariatePolynomial(Value(DenominatorOfRationalFunction(r),3+x));;
 if Minimum(num)<=0 or Minimum(den)<=0 then Error("positivity failure"); fi;
od;
Print("four uniform HS bounds are strictly below |T| for real q >= 3\n");
QUIT;
