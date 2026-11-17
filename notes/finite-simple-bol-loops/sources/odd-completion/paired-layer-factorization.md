# A paired-layer extension criterion for an exact-factorization witness

**Mira Cult**

**Scoped independent review recorded below.** This sufficient condition is not asserted to follow from defect one and is not an exhaustiveness theorem. It addresses the frontier in [C0010](../../claims/0010.md) and uses the [intrinsic exact-factorization criterion](../factor-permutation/exact-factorization-criterion.md). A precommit independent check considered the argument and its corrected lifting step; it is not an exact-revision review.

Let $`(G,H,K)`$ be the canonical faithful generating folder of a finite simple nonassociative left Bol loop, with $`H`$ its identity stabilizer and $`K`$ its left translations. Let $`\tau\in\mathop{\mathrm{Aut}}\nolimits(G)`$ satisfy $`\tau^2=1`$ and $`\tau(k)=k^{-1}`$ for every $`k\in K`$; the invoked existence and uniqueness are described in the linked intrinsic criterion. Suppose $`V,W=\tau(V)`$ are distinct normal elementary abelian $`p`$-subgroups of $`G`$ with $`V\cap W=1`$, $`A=VW=V\times W`$, and $`C_G(A)=A`$. Put $`C=C_G(W)`$. Assume $`|C/A|`$ is prime to $`p`$, and $`C/A`$ acts nontrivially and irreducibly on $`V`$. Write bar for images in $`G/A`$, and put $`D=H\cap A`$. Suppose in addition

 (i)  |H|=|V| |C/A|;
 (ii) D=(H∩V)×(H∩W);
 (iii) Hbar∩(Cbar·τ(Cbar))=(Hbar∩Cbar)(Hbar∩τ(Cbar)).

Then there is a canonical normal subgroup N◁G satisfying the three intrinsic witness conditions N∩τ(N)=1, [G:N]=|K|, and HN∩Hτ(N)=H. Consequently the loop is isomorphic to an exact-factorization loop.

Proof. A◁C and C/A is a p′-group, so Schur–Zassenhaus supplies a complement R to A in C. Since C centralizes W, R acts trivially on W and C=(V⋊R)×W. Put N=V⋊R. Any other complement N' to W in C is the graph of a homomorphism f:N→W. The restriction f|V is R-equivariant into the trivial R-module W, and is zero because the R-module V is nontrivial and irreducible; f|R=0 because R has order prime to p and W is a p-group. Thus f=0 and N is the unique complement to W. The subgroup W is normal in G, hence C=C_G(W) is normal in G, and this uniqueness makes N normal in G. It has N∩A=V and |N|=|V||C/A|.

Likewise τ(N) is the unique complement to V in τ(C)=C_G(V), with τ(N)∩A=W. Their intersection lies in C∩τ(C)=C_G(A)=A, so N∩τ(N)≤V∩W=1. Condition (i) and |G|=|H||K| give [G:N]=|K|.

Set P=Cbar and P'=τ(Cbar); both are normal in G/A and P∩P'=1, since C∩τ(C)=A. Hypothesis (iii) is equivalent to Hbar P∩Hbar P'=Hbar: for any subgroup L and disjoint normal P,P', one has LP∩LP'=L iff L∩PP'=(L∩P)(L∩P'). This follows by writing a point of the intersection as l1p=l2p' and comparing its coordinates.

Now take g∈HN∩Hτ(N). Because NA=CA and τ(N)A=τ(C)A, the quotient condition gives gbar∈Hbar. Write g=ha with h∈H, a∈A. We first justify HN∩A=DV. In the direct product C=N×W, projection π_W:C→W is a homomorphism. Since (H∩C)/D embeds into C/A, it has p′-order, while π_W(H∩C)/π_W(D) is both its quotient and a p-group; thus π_W(H∩C)=π_W(D). If a=h n∈A with h∈H,n∈N, then h∈H∩C and π_W(a)=π_W(h)∈π_W(D), so a∈VD. The reverse inclusion is immediate. Applying the same argument to τ(C)=τ(N)×V gives Hτ(N)∩A=DW. Hence a∈DV∩DW. By (ii), D=D_V×D_W with D_V≤V,D_W≤W, and therefore DV=V×D_W, DW=D_V×W, and DV∩DW=D. Thus g∈H, proving the third witness condition. The intrinsic criterion supplies the claimed exact factorization.

The quotient splitting (iii) records a second, genuinely separate graph obstruction in G/A; splitting the stabilizer intersection in A alone does not prove it. No assertion is made that (iii) is necessary or follows from simple odd-envelope hypotheses. The proof does not use an odd-G assumption; for p=2 its hypotheses may be incompatible with nonassociative exponent-2 simple Bol loops, as the intrinsic criterion explains.

## Control: the paired layer in $`Q_{3,13}`$

The existing [C0003](../../claims/0003.md) exact-factorization construction has $`X=\mathbb F_{27}^+\rtimes(C_{13}\rtimes C_3)`$, $`X'=\mathbb F_{27}^+\rtimes C_{13}`$, and generated folder $`\widehat G=\{(u,v)\in X^2:uv\in X'\}`$. Its coordinate swap is the inverting automorphism, and its paired elementary abelian normal subgroups are $`V=\mathbb F_{27}\times1`$ and $`W=1\times\mathbb F_{27}`$. The identity stabilizer has order $`|H|=|X'|=27\cdot13`$, whereas $`|V|=27`$. Thus $`V`$ itself fails the index condition $`[\widehat G:V]=|K|`$, even though $`H\cap(V\times W)=(\ker\mathop{\mathrm{Tr}}\nolimits)\times0`$ has defect one relative to the fixed space of the swap. The known exact-factorization witness extends $`V`$ to $`X'\times1`$, an extension of index $`13`$. This control relies on the stated C0003 construction; it does not show that every paired layer admits such an extension.

## Scoped independent review

reviewer contributor 1 accepted this sufficient criterion at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/1228403b62d5c6abbf31272ed4cb4e300424e9d9), relying on the previously reviewed intrinsic criterion and stated C0003 control data. The review checked uniqueness of the complement, normality, the swapped intersection and index, the quotient graph-splitting equivalence, and the p′-projection proof of HN∩A=DV. The Q_{3,13} control agrees with the cited folder data. All displayed hypotheses remain requirements; none is derived here from defect one or loop simplicity alone. No computation, formal proof or exhaustiveness claim is involved.
