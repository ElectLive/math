# Prescribing an entire odd abelian right nucleus

**Mira Cult**

This construction places every right nuclear translation inside the left multiplication group. Its use of a product of finite rings permits noncyclic and mixed-prime abelian right nuclei. The [extraspecial field construction](../../extraspecial-cores/extraspecial-odd-bol-construction.md) has a different aim.

**Theorem.** Let $`P\ne1`$ be any finite abelian group of odd order $`u`$. Write

```math
P=\prod_{i=1}^k C_{r_i}
```

with $`r_i>1`$ odd prime powers (repetitions allowed), and put $`r=\exp P`$. For **every** prime $`q\equiv1\pmod r`$ and integer $`m\ge1`$, set $`d=mu(q-1)`$. There is a finite simple non-Moufang left Bol loop $`Q`$ of order $`u^{d+1}q^k`$ with the following properties:

1. Its **whole native right nucleus** is isomorphic to $`P`$. As permutations of $`Q`$, the right translations by nuclear elements form exactly $`Z(\mathrm{LMlt}(Q))`$, also isomorphic to $`P`$. Thus this right nucleus is proper and nonnormal.
2. $`Q`$ is a G-loop: all its loop isotopes are isomorphic to it. Its exponent is $`r^2q`$, and it contains genuine elements of orders $`r^2`$ and $`rq`$.
3. Its faithful left multiplication group has a class-two normal subgroup $`N`$ with $`N'=Z(N)\cong P`$, $`\exp N=r`$, and $`|N|=u^{2d+1}`$. Its quotient by $`N`$ is $`(\mathbb F_q^k\oplus\mathbb F_q^k)\rtimes P`$. If $`P=C_{p^e}`$ then $`N=O_p(\mathrm{LMlt}(Q))`$ and the **entire native element-order set** is $`\{p^i:0\le i\le 2e\}\cup\{qp^i:0\le i\le e\}`$.

There is such a $`q`$ for every $`P`$, without invoking primes in progressions. This is the positive realization for **every nontrivial** finite odd abelian group. It does not assert impossibility for the trivial group or that all right nuclei in this class are abelian. An ancillary inference to exclude the trivial group at the first working revision was withdrawn: the center assertion in FKP's arXiv Corollary 6.24 is incompatible with a known centerless left multiplication group, and is not used here. See the separate [primary-source and 1053 control](../nagy-comparison.md).

## 1. A group and an actual subgroup, over a product of finite rings

Let $`S=\prod_i\mathbb Z/r_i`$. Identify the additive group of $`S`$ with $`P`$ by the given decomposition; write $`\iota:P\to S^+`$ for this identification. Both $`2`$ and $`q`$ are units in $`S`$. Let $`C`$ be cyclic shift on $`S^q`$, and put $`E_0=\{x:\sum x_j=0\}`$, a free $`S`$-module of rank $`q-1`$. The standard dot product is perfect on $`E_0`$: the complementary line of constants is its orthogonal summand, since $`q`$ is a unit. Every $`C^a-I`$ for $`a\not\equiv0\bmod q`$ is invertible on $`E_0`$: only constants are fixed on $`S^q`$, hence the kernel there is zero on $`E_0`$, which is finite. The form

```math
g_0(x,y)=\langle x,(C-C^{-1})y\rangle
```

is alternating and perfect on $`E_0`$, since $`C^{-1}(C^2-I)`$ is invertible. Take $`m`$ orthogonal copies $`(E,g)`$ and let $`z`$ act by $`C`$ on each. This gives an explicit fixed-point-free order-$`q`$ symplectic action over each actual ring, not an argument that lifts a field dimension over a nonfield.

Set $`L=E^P`$ of free $`S`$-rank $`d`$, $`U=L\oplus L`$, and write

```math
B(x,y)=\sum_{j\in P}g(x_j,y_{-j}),\qquad
 \omega((x,y),(x',y'))=B(x,y')+B(y,x').
```

Both forms are perfect and alternating; the two copies $`L_0,L_1`$ of $`L`$ in $`U`$ are complementary Lagrangians. Each $`(R_a x)_j=x_{j+a}`$ on $`L`$ is self-adjoint for $`B`$. Put $`N=U\times S^+`$ with group law $`(v,c)(w,b)=(v+w,c+b+\omega(v,w)/2)`$. The two-step group has $`N'=Z(N)=0\times S^+`$: the form has zero radical and its values generate all of $`S`$ (a free basis functional can take the value $`1`$). Its exponent is $`r`$ by $`(v,c)^a=(av,ac)`$.

On $`V=\mathbb F_q^k\oplus\mathbb F_q^k`$ denote the positive and negative coordinate axes by $`A_i,B_i`$ respectively, and their sums by $`A,B_*`$. Choose characters $`\chi_i:P\to\mathbb F_q^\times`$ faithful on the $`i`$th cyclic factor and trivial on the others. The $`2k`$ characters $`\chi_i^{\pm1}`$ are pairwise distinct, even for repeated factors, since $`r_i`$ is odd and bigger than one. Let $`X=V\rtimes P`$ acting on each pair of axes by these reciprocal characters. The signed involution $`t`$ exchanges $`A_i,B_i`$ and negates $`P`$. Put $`D=N\rtimes X`$ with the following action. For $`v=(a,b)\in V`$ and $`j\in P`$ define

```math
\ell_j(a,b)=\sum_i\bigl(\chi_i(j)a_i+\chi_i(j)^{-1}b_i\bigr)\in\mathbb F_q.
```

On the two copies in $`U`$, $`v`$ acts at $`j`$ by $`z^{\ell_j(a,b)}`$, $`z^{\ell_j(b,a)}`$ respectively. An element $`h\in P`$ acts by $`(R_h,R_{-h})`$; $`t`$ exchanges copies. These are symplectic actions and fix the center pointwise: the exponents in each cross-pairing at $`j,-j`$ coincide, the shifts are adjoint, and swapping preserves $`\omega`$. Shifting $`j`$ to $`j+h`$ implements the specified character action, so the semidirect relations hold. The $`X`$-action on $`U`$ is faithful: a nontrivial $`P`$-component moves sites, while the linear independence of the $`2k`$ distinct characters as functions $`P\to\mathbb F_q`$ detects all coefficients of $`v`$. For instance multiply a putative relation by the inverse of one character and sum over $`P`$; nontrivial character sums vanish and $`q\nmid |P|`$. Crucially, every nonzero element of **each separate** axis $`A_i`$ or $`B_i`$ has invertible difference from identity on **all** of $`U`$, by the explicit construction of $`z`$.

The actual point stabilizer is

```math
H=\{\,((x,0),\iota(h))\,b h: x\in L,\ b\in B_*,\ h\in P\,\}\le D.
```

Here $`B_*\rtimes P=J`$ preserves $`L_0`$ and $`L_0`$ is isotropic, so the formula defines a group, with projection onto all of $`J`$. In particular $`H\cap Z(N)=1`$ and $`H\cap N=L_0`$ on its zero central sheet. Replacing $`\iota`$ by a noninjective map is not innocent: any nonzero $`h`$ it kills is in $`H`$ and is a product of the projected sign lifts $`t,(-h)t`$ with zero vector and phase.

## 2. Sharpness, generation and faithfulness

In $`\widehat D=D\rtimes\langle t\rangle`$ let $`\mathcal C=t^D`$ and $`T=\mathcal C t`$. Since $`|D|`$ is odd, all outside involutions form $`\mathcal C`$, and $`T`$ is the full set of elements of $`D`$ inverted by $`t`$. In $`N`$ the fixed vector is a diagonal pair and all of $`S`$ is fixed. In $`X`$ the fixed group is the diagonal $`\mathbb F_q^k`$ and the top is zero. Thus

```math
|T|=[D:C_D(t)]=|L|\,u\,q^k=[D:H].
```

The group generated by $`T`$ is the even part of the normal group generated by $`\mathcal C`$, hence normal in $`D`$. Its projection contains all $`P`$ and the antidiagonal in $`V`$. Conjugating the latter by $`P`$ fills both axes in each separate pair, since $`\chi_i\ne\chi_i^{-1}`$. It therefore surjects onto $`X`$. Its commutators with $`N`$ surject onto $`U=N/Z(N)`$ by the axis difference above. A subgroup $`F`$ of $`N`$ surjecting onto $`U`$ contains $`[N,N]`$ because $`N=F Z(N)`$ implies $`[N,N]=[F,F]`$; hence $`F=N`$. This proves $`\langle T\rangle=D`$ without a Frattini shortcut across mixed primes.

We check $`H\cap\mathcal C^2=1`$ on *all true lifts*. For each projected involution $`a\in Xt`$, its involutory lifts are exactly $`(v,0)a`$ with $`av=-v`$. The square fixes the anti-invariance first, then $`2c+\omega(v,-v)/2=0`$ forces $`c=0`$. Given signs $`a,b`$, the two vectors added in any product belong to $`U^-_a`$ and $`aU^-_b=U^-_{aba}`$. Each sign interchanges the two Lagrangians. If the sum is in $`L_0`$, write the summands as $`(ay,-y)`$ and $`(-(aba)y,y)`$ with $`y\in L_1`$ (here the first coordinate denotes the image in the first half). Their $`\omega`$-pairing is zero. Indeed $`\omega(sy,y)=\omega(y,sy)=-\omega(sy,y)`$ for a symplectic involution $`s`$, hence $`\omega(sy,y)=0`$, and similarly with the two arguments reversed. Both cross terms vanish; same-Lagrangian terms already vanish. Thus **the actual central phase above any product whose vector belongs to $`L_0`$ is zero**, componentwise in $`S`$.

If the top $`h`$ of the projected product is nonzero, that phase disagrees with the required $`\iota(h)`$. If the projection is a nonzero $`b\in B_*`$, the first projected sign would invert $`b`$; every outside sign takes $`B_*`$ onto $`A`$ and $`A\cap B_*=0`$. If the projection is the identity, the two negative spaces are the same and have zero intersection with $`L_0`$, so the vector and phase are both zero. This exhausts the stabilizer. As $`T^{-1}T=\mathcal C^2`$ is conjugacy invariant, every coset of every conjugate stabilizer contains exactly one mark. The marks act sharply transitively on $`D/H`$. They include $`1`$, and $`aba\in T`$ for $`a,b\in T`$ by inversion under the signed automorphism. The unique marks taking $`H`$ to each coset therefore define a left Bol loop: evaluating $`L_xL_yL_x`$ at $`H`$ identifies it with $`L_{x(yx)}`$.

Every nonzero normal subgroup of $`N`$ meets $`Z(N)`$ nontrivially: a noncentral vector has a nonzero scalar commutator, and a nontrivial central subgroup already meets it. If a normal subgroup of $`D`$ is disjoint from $`N`$, it centralizes $`N`$; but $`C_D(N)=Z(N)`$ by the faithful action of $`X`$ on $`U`$. Since $`H\cap Z(N)=1`$, $`H`$ is core-free and $`D`$ really is $`\mathrm{LMlt}(Q)`$. In particular $`Z(D)=Z(N)=S^+`$. For $`P=C_{p^e}`$, a normal $`p`$-subgroup of $`X`$ would centralize $`V`$ since their orders are coprime and both are normal; faithfulness of $`P`$ on $`V`$ gives $`C_X(V)=V`$. Hence $`O_p(D)=N`$ in this case.

## 3. All normal cuts, including subgroups that see only part of the center

Use the independently reviewed [odd signed-normal-cut criterion](../../extraspecial-cores/signed-cut-test.md): in the faithful generating odd folder with full inverted set just proved, simplicity is equivalent to $`[C:C\cap H]>[C:C_C(t)]`$ for every proper nontrivial $`t`$-stable normal $`C\triangleleft D`$.

For $`1<C\le N`$, put $`C_0=C\cap Z(N)\ne1`$ and $`Y=C Z(N)/Z(N)\le U`$, a $`t`$-stable additive subgroup. Do **not** assume $`C_0=Z(N)`$, $`Y`$ free, or $`C`$ the full preimage of $`Y`$. The projection injects $`C\cap H`$ into $`Y\cap L_0`$. On fixed points, $`C_C(t)\to Y^+`$ is onto: for a lift $`x`$ of a fixed vector, $`x^{-1}t(x)\in C_0`$ and is inverted by $`t`$, but all of $`C_0`$ is fixed of odd order, hence $`x`$ itself is fixed. Thus $`[C:C_C(t)]=|Y^-|`$, using the plus/minus decomposition of an odd abelian group. Since $`Y^-\cap(Y\cap L_0)=0`$,

```math
[C:C\cap H]\ \ge\ |C_0|\frac{|Y|}{|Y\cap L_0|}\ \ge\ |C_0|\,|Y^-|\ >\ |Y^-|.
```

For $`C\not\le N`$ write $`Y=CN/N\ne1`$, normal in $`X`$ and $`t`$-stable. Then $`W=Y\cap V\ne0`$: if an element of $`Y`$ has a nontrivial top component, some $`\chi_i`$ detects it and its commutators with the corresponding axis are nonzero. Otherwise $`1<Y\le V`$. The $`P`$-invariant $`W`$ is a sum of coordinate axes by the pairwise distinct character idempotents over $`\mathbb F_q`$; $`t`$ makes it a sum of **whole paired coordinates**. Picking one nonzero axis element in $`W`$ and lifting it to $`C`$, its commutators with $`N`$ surject onto $`U`$, by the separate-axis property. As in Section 2, $`N\le C`$; thus $`C`$ is the entire inverse image of $`Y`$. The top image $`P_0`$ of $`Y`$ is proper in $`P`$, or $`[Y,V]=[P,V]=V`$ would give $`Y=X`$ and $`C=D`$. For $`J=B_*\rtimes P`$,

```math
|Y\cap J|\le |W\cap B_*|\,|P_0|,\qquad |W\cap B_*|=|C_W(t)|.
```

Using the split section of the preimage of $`Y`$, we have $`|C_C(t)|=|L|u|C_Y(t)|`$, whereas $`|C\cap H|=|L||Y\cap J|`$. Since $`|P_0|<u`$ and $`C_W(t)\le C_Y(t)`$, the strict cut inequality holds. This includes proper correlated subgroups of the top, not only coordinate deletions. Simplicity follows. The stabilizer in the faithful left multiplication group is nontrivial, excluding associativity. Odd Moufang loops are classically solvable by [FKP, Proposition 6.11](https://arxiv.org/pdf/math/0208231), so this simple nonassociative loop is not Moufang.

## 4. The whole right nucleus and all loop isotopes

In any loop, a permutation commuting with every left translation has the form $`R_c`$ with $`c`$ in the right nucleus: evaluate it on $`x=L_x(1)`$, and the commutation relation is exactly $`(xy)c=x(yc)`$. In a faithful transitive left coset action the centralizer is the opposite of $`N_D(H)/H`$: the image of $`H`$ must be $`gH`$ fixed by $`H`$, which for finite groups is equivalent to $`g\in N_D(H)`$; the map is right multiplication on cosets. In our case $`N_X(J)=J`$. Indeed after multiplying by an element of $`J`$ a prospective normalizer lies in $`A`$; conjugating every pure top element must then produce no $`A`$-component. No nonzero vector in $`A`$ is fixed by all $`P`$, as each coordinate character is nontrivial. Since $`H\to J`$ is onto, reduce any $`D`$-normalizer to an element $`(v,c)\in N`$. Normalizing $`H\cap N=L_0`$ on its **zero** central sheet forces $`\omega(v,L_0)=0`$, or $`v\in L_0`$. Conversely $`H Z(N)`$ normalizes $`H`$. Thus

```math
N_D(H)=H Z(N),\qquad C_{\mathrm{Sym}(Q)}(D)=Z(D)\cong P.
```

For the latter equality central coset-right and coset-left actions agree and faithfulness separates them. Consequently these are all nuclear right translations, not merely a nuclear subgroup of the correct size. Since $`1<|P|<|Q|`$ and $`Q`$ is simple the right nucleus is not normal.

The fixed group $`K=C_D(t)`$ has order $`|Q|`$ and $`K\cap H=1`$ by projecting first to the diagonal in $`V`$ and then intersecting $`L_0`$ with the diagonal in $`U`$. Thus $`D=H K`$. For every $`a\in T`$ take $`b\in\langle a\rangle`$ with $`b^2=a^{-1}`$, possible by oddness and $`b\in T`$. Then $`b T b^{-1}=a^{-1}T`$ since $`b^{-1}T b^{-1}=T`$ (sandwich closure and its inverse). Writing $`b=h k`$, conjugation by $`h\in H`$ induces this same translate of $`T`$, as $`k`$ centralizes $`t`$ and normalizes $`T`$. Now [Nagy, Lemma 2.3](https://arxiv.org/pdf/math/0703919) is precisely the G-loop criterion for a left Bol loop.

## 5. Native powers, parameter availability, and a same-degree distinction

The order of the element attached to a mark $`a`$ equals its group order: every $`a^j`$ is again a mark and supplies the corresponding loop power, while no mark except $`1`$ fixes $`H`$. The odd group $`N`$ has exponent $`r`$, $`X`$ has exponent dividing $`rq`$, so the exponent of $`D`$ divides $`r^2q`$. Choose a top element $`h\in P`$ of order $`r`$ and a primitive vector $`w`$ of additive order $`r`$ in $`E`$. Let $`x\in E^P`$ be supported at $`0`$ with value $`w`$. The mark

```math
((x,-R_{-h}x),0)\,h
```

is inverted by $`t`$ (on its vector this is $`tv=-h^{-1}v`$). Its $`r`$th power has in its first half one $`w`$ at every site of $`\langle h\rangle`$, hence has order $`r`$ in $`N`$ regardless of its central phase. This mark has order $`r^2`$. A nonzero antidiagonal $`v\in V`$ is inverted by $`t`$ and fixes both copies at site zero, since $`\ell_0(a,-a)=0`$. The pure vector mark $`((x,-x),0)`$ of order $`r`$ commutes with it, giving a mark of order $`rq`$. These certify the exact loop exponent. If $`P=C_{p^e}`$ and $`k=1`$, every projected element with nonzero top is conjugate in $`X`$ to its top because the unique pair of reciprocal characters is faithful and neither eigenvalue is $`1`$. Lifts over these elements have $`p`$-power order; lifts over $`V`$ have order dividing $`qr`$. The exhibited two marks and their powers give exactly the orders stated. This last full order-set assertion is **not** being extended to mixed or multi-axis tops.

For existence of $`q`$, take a prime divisor of $`\Phi_r(2r)>1`$. It does not divide $`2r`$, since the cyclotomic polynomial has constant term $`1`$ for $`r>1`$. The polynomial $`x^r-1`$ has no repeated root modulo $`q`$, so a root of its factor $`\Phi_r`$ lies in no lower-order cyclotomic factor. Thus $`2r\bmod q`$ has order exactly $`r`$ and $`q\equiv1\pmod r`$.

A direct byproduct is large multiplicity at the *same* order via intrinsically **different centers**. For fixed odd prime $`p`$ and $`s\ge2`$, choose $`q\equiv1\bmod p^{s-1}`$ and use $`P_j=C_{p^j}\times C_{p^{s-j}}`$ for $`1\le j\le\lfloor s/2\rfloor`$ with the same $`m`$. All have the common loop degree $`(p^s)^{1+m p^s(q-1)}q^2`$, but the full centers of their left multiplication groups are nonisomorphic, hence so are the loops; the G-loop conclusion also makes them pairwise nonisotopic. This does not distinguish loops with the same center or count *all* loops at that order.

[Review and replication](../verification.md) · [Right nuclei](../README.md)
