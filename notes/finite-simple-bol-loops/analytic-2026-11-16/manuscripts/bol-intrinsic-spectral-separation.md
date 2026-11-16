# Intrinsic spectral separation of reciprocal Bol loops with identical scalar ranks

Mira, with AI assistance

## 1. Result, conventions, and source boundary

The spread and aligned families in Section 6A of
[the collective manuscript](bol-collective-cancellation.md#6a-coupled-pencils-and-an-exact-norm-on-all-mean-zero-inputs)
are nonisomorphic as unmarked loops for every integer $`h\geq1`$.
Their canonical inner-defect operators have different traces, different
positive trace moments, and explicitly different spectral multiplicities.
Their normalized traces are their probabilities of an associative triple.
No pencil chart, marked word, or chosen scalar character is retained in
these invariants.

The same calculation gives a collective analytic separation on a canonical
spectral subspace occupying a proportion tending to one of the regular
Hilbert space. After a specified intrinsic normalization, a fixed quadratic
filter gives a ratio of root mean squared outputs asymptotic to $`27\,3^{-h}`$.
The comparison concerns a complete orthonormal collection of inputs, or
independent random signs on the actual loop elements. The two worst-case
operator norms remain equal. The complete input space and filter are specified
in Section 6.

We start from PR #440 at delivery revision
`f67b6f91c7f97fe2af1d58240de0b1debc5a2da2`. The reviewed mathematical source
of [the associator manuscript](bol-associator-quantization.md), including
(AQ.27)--(AQ.30), is `5771bfccb6707606078baf93be804f810276b8eb`.
The intervening single commit changes overview, status, and review evidence;
both mathematical manuscripts are byte-identical. The earlier reviews remain
scoped to their original sources. This continuation has its own exact-source
review in [the evidence record](../evidence/bol-metaplectic-review.md).
All theorem labels below are manuscript-local; no permanent claim IDs are
allocated. The construction is directly verified proper Bol; no simplicity
or classification premise is used.

For a loop $`\mathcal L`$, use the source's pushforward convention
$`U_g f=f\circ g^{-1}`$, so $`U_gU_h=U_{gh}`$. Measures and Hilbert norms
are normalized counting measures. The trace is the ordinary matrix trace,
not divided by the dimension. Define

```math
 \ell_{x,y}=L_{x\circ y}^{-1}L_xL_y,\qquad
 \mathcal A=\mathbb E_{x,y}U_{\ell_{x,y}},\qquad
 H=\langle\ell_{x,y}:x,y\in\mathcal L\rangle,\qquad
 P=|H|^{-1}\sum_{g\in H}U_g,                                  \tag{IS.1}
```

and $`\mathcal M=\mathbb E_zU_{L_z}^{*}\mathcal A U_{L_z}`$.
Thus $`P`$ is the intrinsic projection onto the functions constant on
$`H`$-orbits. It is generally larger than the projection onto constants.

### Theorem 1: intrinsic separation

Put $`Q=729`$, $`k=2h+1`$, and define

```math
 \begin{split}
 D_k(t)={}&(1+42\,49^{-kt})(49^k-17^k)\\
         &+6\bigl[(1+48\,9^{-t})^k-(1+16\,9^{-t})^k\bigr].
 \end{split}                                                   \tag{IS.2}
```

For either of the stated families, with any of its allowed injections,
the operators $`\mathcal A`$ are positive definite. For every real
$`t>0`$ their traces satisfy

```math
 \boxed{
 \operatorname{Tr}\mathcal A_{\rm al,h}^{\,t}
 -\operatorname{Tr}\mathcal A_{\rm sp,h}^{\,t}
 =\frac{(3^k-3)(Q^{6h-1}-Q^{4h})}{7}\,
   Q^{-4ht}(1-49^{-t})D_k(t)>0.}                              \tag{IS.3}
```

Their fixed-space dimensions are equal. Consequently the same difference
holds for $`\operatorname{Tr}(\mathcal A-P)^t`$.
In particular,

```math
 \boxed{
 \Delta\operatorname{Tr}\mathcal A
 =\frac{48}{343}(3^{2h+1}-3)(Q^{2h-1}-1)
 \left\{(1+42\,49^{-(2h+1)})(49^{2h+1}-17^{2h+1})
 +6\left[(19/3)^{2h+1}-(25/9)^{2h+1}\right]\right\}.}          \tag{IS.4}
```

Here and below $`\Delta`$ means aligned minus spread. In particular
$`\mathcal L_{\rm al,h}\not\cong\mathcal L_{\rm sp,h}`$ as loops.
The $`\mathcal M`$ spectra also differ, since
$`\operatorname{Tr}\mathcal M=\operatorname{Tr}\mathcal A`$.

## 2. The constructions and the exact incidence

We recall precisely which families are being compared. Let
$`E=\mathbf F_{729}`$, $`L_h=\mathbf F_{729^h}`$,
$`M_h=\mathbf F_{729^{2h-1}}`$, and $`k=2h+1`$. Choose injective
$`\mathbf F_3`$-linear maps
$`j_h:\mathbf F_3^k\to L_h`$ and
$`i_h:\mathbf F_3^k\to M_h`$.
For $`t=j_h(\nu)`$, put $`z(t)=(t,t^3,t^9)`$ and

```math
 c_t(x,y)=\operatorname{Tr}_{L_h/E}\det[z(t),x,y],\qquad
 B_\nu^{\rm sp}=c_t\oplus c_t.                              \tag{IS.5}
```

These are alternating forms on the $`E`$-space $`L_h^6`$ of dimension
$`6h`$. The aligned form is $`B_\nu^{\rm al}=S_\nu\oplus d_\nu`$,
where $`S_\nu`$ is the alternating star matrix with first row
$`(0,\nu_1,\ldots,\nu_k)`$ and

```math
 d_\nu((x,y),(x',y'))=
 \operatorname{Tr}_{M_h/E}\bigl(i_h(\nu)(xy'-yx')\bigr).       \tag{IS.6}
```

The family is completely specified by the finite-field representations,
ordered bases, and injections. One uniform choice is the first monic
irreducible polynomial in a fixed lexicographic order for each extension,
and the first $`k`$ vectors of its ordered absolute $`\mathbf F_3`$-basis.
The base is $`E=\mathbf F_3[\lambda]/\Phi_7(\lambda)`$.
There is no dependence of the theorems on this particular injection choice.

For either pencil use $`W=E^{6h}`$, $`V=(\mathbf F_7^2)^k`$,
$`Z=\mathbf F_3^k\oplus\mathbf F_7`$, $`\eta=2\in\mathbf F_7`$,
and $`\lambda`$ of order seven in $`E`$. With $`u=(w,v)`$, define

```math
 \begin{split}
 \beta(w,w')_i&=\operatorname{Tr}_{E/\mathbf F_3}(w^{\mathsf T}B_iw'),\\
 \gamma(v,v')&=\sum_i(v_{i,1}v'_{i,2}-v_{i,2}v'_{i,1}),\\
 b(u,u')&=(\beta(w,w'),\gamma(v,v')),\\
 R(a,s)(w,(v_i))&=(\lambda^s w,(2^{a_i}v_i)),\\
 (u,c)\circ(u',c')&=(u+R(c)u',c+c'-b(u,u')).
 \end{split}                                                  \tag{IS.7}
```

The directly verified divisions, Bol identity, non-Moufang witness, and
right nucleus $`\{0\}\times Z`$ are in Sections 2.1--2.3 of the
associator manuscript. Both pencils have zero common radical and identical
**labeled** rank data:

```math
 \operatorname{rank}_E B_0=0,\qquad
 \operatorname{rank}_E B_\nu=4h\quad(\nu\ne0),\qquad
 |\mathcal L_h|=3^{38h+1}7^{4h+3}.                            \tag{IS.8}
```

Independence over $`\mathbf F_3`$ suffices; independence of the tuple over
$`E`$ is not assumed.

### Lemma 2: image intersections, including all exceptional parameters

View matrices as maps from $`E^{6h}`$ to its coordinate dual. For nonzero
$`\alpha,\nu\in\mathbf F_3^k`$ independent over $`\mathbf F_3`$,

```math
 \dim_E(\operatorname{im}B_\nu^{\rm sp}\cap\operatorname{im}B_\alpha^{\rm sp})=2h,
 \qquad
 \dim_E(\operatorname{im}B_\nu^{\rm al}\cap\operatorname{im}B_\alpha^{\rm al})=4h-1.
                                                                  \tag{IS.9}
```

For any parameters the exact compatible-vector count is

```math
 C_{\alpha,\nu}:=
 \#\{w\in E^{6h}:B_\nu w\in\operatorname{im}_E B_\alpha\}
 =Q^{6h-r_\nu+\dim_E(\operatorname{im}B_\nu\cap\operatorname{im}B_\alpha)}.
                                                                  \tag{IS.10}
```

Thus its complete table is:

| Parameters | Spread count | Aligned count |
|---|---:|---:|
| $`\nu=0`$, any $`\alpha`$ | $`Q^{6h}`$ | $`Q^{6h}`$ |
| $`\alpha=0,\nu\ne0`$ | $`Q^{2h}`$ | $`Q^{2h}`$ |
| $`\alpha\ne0,\nu=\alpha`$ or $`-\alpha`$ | $`Q^{6h}`$ | $`Q^{6h}`$ |
| nonzero $`\alpha,\nu`$ independent over $`\mathbf F_3`$ | $`Q^{4h}`$ | $`Q^{6h-1}`$ |

**Proof.** The perfect $`E`$-linear trace pairing on $`L_h`$ identifies
the image of $`c_t`$ with
$`\{\xi\in L_h^3:\xi\cdot z(t)=0\}`$. The condition is an equation
in $`L_h`$: annihilation must hold on the entire radical line
$`L_hz(t)`$. It is not enough for a single scalar trace to vanish.
The trace pairing is nondegenerate even when $`3\mid h`$.

For nonzero $`s,t`$, equality of the lines $`L_hz(s)=L_hz(t)`$ forces
$`s/t=(s/t)^3`$, hence $`s/t\in\mathbf F_3^\times`$. Conversely such
a ratio makes the lines equal. Since $`j_h`$ is injective and
$`\mathbf F_3`$-linear, independent parameters therefore give distinct
$`L_h`$-lines. The two annihilating hyperplanes intersect in one
$`L_h`$-dimension in each copy, giving $`2h`$ dimensions over $`E`$.
Possible $`E`$-proportionality of the scalar values $`s,t`$ does not
alter this argument.

For the aligned star block,
$`\operatorname{im}S_\nu=Ee_0\oplus E(0,\nu)`$ for $`\nu\ne0`$.
Two $`\mathbf F_3`$-vectors proportional over $`E`$ are already
proportional over $`\mathbf F_3`$: inspect a nonzero coordinate.
Thus independent parameters have star-image intersection $`Ee_0`$.
The remaining block is nonsingular for every nonzero parameter and
contributes $`4h-2`$ common dimensions. The sum is $`4h-1`$.

Finally, the map $`B_\nu:E^{6h}\to\operatorname{im}B_\nu`$ has
fibers of size $`Q^{6h-r_\nu}`$. Taking the inverse image of the
intersection proves (IS.10) and all zero/proportional cases.
Changing an $`E`$-basis sends every matrix to $`S^{\mathsf T}B S`$,
so the images are all transported by the same invertible dual map.
The dimension calculation is basis-independent. The unmarked invariant
will be the full spectral sum, not the individual parameter labels. $`\square`$

## 3. Orbit sizes and a complete multiplicity table

For this section set

```math
 S=3^k,\quad T=Q^{6h},\quad K=Q^{2h},\quad r=Q^{-4h},\quad
 X_{\rm sp}=Q^{4h},\quad X_{\rm al}=Q^{6h-1},\quad
 c_j=\binom{k}{j}16^j.                                      \tag{IS.11}
```

The letters $`S,T,K,X`$ in (IS.11) denote numbers, not vector spaces
or operators. For a choice $`X=X_{\rm sp}`$ or $`X_{\rm al}`$, put

```math
 \begin{array}{ll}
 a_0=\dfrac{T-1+(S-1)(K-1)}7,&
 b_0=\dfrac{(S-1)(T-K)}7,\\[4pt]
 a_1=\dfrac{3(T-1)+(S-3)(X-1)}7,&
 b_1=\dfrac{(S-3)(T-X)}7.
 \end{array}                                                \tag{IS.12}
```

All these are nonnegative integers. In particular
$`a_0+b_0=a_1+b_1=S(T-1)/7`$.

### Theorem 3: full spectral multiplicities

For each $`0\leq j\leq k`$, multiply the following base multiplicities
by $`c_j`$, then multiply their eigenvalues and multiplicities by the
appropriate entries in the ring table. Sum multiplicities when numerical
eigenvalues coincide.

| Vector case | Base eigenvalue | Base multiplicity |
|---|---:|---:|
| $`w=0`$ | $`1`$ | $`S`$ |
| $`w=0`$ | $`r`$ | $`S(3^j-1)`$ |
| $`w\ne0`$ | $`1`$ | $`a_0`$ |
| $`w\ne0`$ | $`1/49`$ | $`b_0`$ |
| $`w\ne0`$ | $`r`$ | $`(3^j-1)a_1`$ |
| $`w\ne0`$ | $`r/49`$ | $`(3^j-1)b_1`$ |

| Ring multiplier | Multiplicity | Allowed vector case |
|---|---:|---|
| $`1`$ | $`1`$ | both |
| $`9^{-j}`$ | $`6`$ | both |
| $`49^{-k}`$ | $`42`$ | only $`w\ne0`$ |

This gives every eigenvalue of $`\mathcal A`$ on all of
$`L^2(\mathcal L)`$, with total multiplicity

```math
 7ST49^k=|\mathcal L|.                                      \tag{IS.13}
```

The exact fixed-space dimension is

```math
 \operatorname{rank}P=(S+a_0)(17^k+6),                      \tag{IS.14}
```

independent of the family. In particular constants, the full fixed vector
axis, nonzero scalar radicals, and every zero character are included.

**Proof.** In the notation of (AQ.27)--(AQ.29), the nucleus character
is $`(\nu,\rho)\in\mathbf F_3^k\times\mathbf F_7`$.
A nonzero $`w\in W`$ has a seven-element scalar orbit. Each nonzero
$`z_i\in\mathbf F_7^2`$ has a three-element scalar orbit, giving
$`(49-1)/3=16`$ distinct nonzero orbits in that plane.
If exactly $`j`$ planes are active, there are $`c_j`$ choices of their
support and plane orbits. The allowed orbit labels are precisely
$`\alpha_i=0`$ off that support and arbitrary on it, hence $`3^j`$
choices. The allowed $`\sigma`$ are all seven values when $`w\ne0`$,
and only zero when $`w=0`$.

For $`\alpha=0`$, summing compatible nonzero $`w`$ over all $`\nu`$
gives $`T-1+(S-1)(K-1)`$. Incompatible vectors number
$`(S-1)(T-K)`$. Each invariant set is a union of seven-cycles, so
division by seven gives $`a_0,b_0`$, not the raw vector counts.
For each nonzero $`\alpha`$, the three parameters
$`\nu=0,\alpha,-\alpha`$ are fully compatible; each of the other
$`S-3`$ parameters has $`X`$ compatible vectors. Removing the zero
vector and dividing by seven gives exactly $`a_1,b_1`$.
The singleton $`w=0`$ orbit is counted separately, with all $`S`$
nucleus parameters. This is the origin of the $`-1`$ corrections.

Equation (AQ.28) gives the base eigenvalues: compatibility contributes
$`Q^{-r_\alpha}`$ and incompatibility contributes
$`Q^{-r_\alpha}/49`$. Its ring factor at conductor one is

```math
 s_\sigma(z_V,\rho)=
 \begin{cases}
 1,&\sigma=0,\rho=0,\\
 9^{-j},&\sigma=0,\rho\ne0,\\
 49^{-k},&\sigma\ne0.
 \end{cases}                                               \tag{IS.15}
```

The multiplicities are $`1,6,6\cdot7=42`$, respectively.
There are no imprimitive characters at the level seven used here;
the all-conductor source is being specialized, not truncated.
All factors are strictly positive.

For the dimension check, the $`w=0`$ part has total
$`7S\sum_jc_j3^j=7S49^k`$. The other part has total
$`49S(T-1)\sum_jc_j3^j/7=7S(T-1)49^k`$.
Eigenvalue one occurs only in the base-eigenvalue-one rows, with
ring multiplier one, plus the six $`\rho\ne0`$ terms when $`j=0`$.
Since $`\sum_jc_j=17^k`$, this gives (IS.14). It agrees exactly with
the intrinsic fixed-space criterion (AQ.30). $`\square`$

## 4. Trace separation, spectral ordering, and intrinsic meaning

Only $`a_1,b_1`$ in the table depend on the pencil geometry. Write

```math
 \delta=\frac{(S-3)(X_{\rm al}-X_{\rm sp})}{7}>0.             \tag{IS.16}
```

For each $`j`$ and each ring multiplier $`s`$ with its ring
multiplicity $`m_s`$, the aligned spectrum is obtained from the spread
spectrum by transferring
$`\delta c_j(3^j-1)m_s`$ eigenvalues from $`rs/49`$ to $`rs`$.
These are nonnegative integer transfers; their removal never exceeds the
available spread multiplicity because $`b_{1,\rm al}\geq0`$.
All other entries agree. This gives a coupling of the two empirical
spectral measures with aligned eigenvalue at least spread eigenvalue.
It is a statement about spectra, not an operator inequality between
different Hilbert spaces under an arbitrarily chosen labeling.

For any increasing function $`F`$ on $`[0,1]`$, therefore,
$`\operatorname{Tr}F(\mathcal A_{\rm al})\geq
\operatorname{Tr}F(\mathcal A_{\rm sp})`$. It is strict for strictly
increasing $`F`$. For $`F(x)=x^t`$, the difference is

```math
 \delta r^t(1-49^{-t})\sum_{j=0}^k
 c_j(3^j-1)\bigl(1+6\,9^{-jt}+42\,49^{-kt}\bigr).           \tag{IS.17}
```

The binomial theorem identifies the sum as $`D_k(t)`$, proving (IS.3)
and then (IS.4). The $`j=1`$ contribution is positive, and
$`Q^{6h-1}>Q^{4h}`$ for every $`h\geq1`$. The transfers all lie
strictly below one, while (IS.14) is common. Subtracting the fixed-space
projection therefore preserves every positive-moment difference.

### Isomorphism transport and return probabilities

For an actual loop isomorphism $`\phi:\mathcal L\to\mathcal L'`$,
the unitary $`C_\phi f=f\circ\phi^{-1}`$ satisfies

```math
 C_\phi U_{L_x}C_\phi^{-1}=U_{L'_{\phi(x)}},\qquad
 C_\phi U_{\ell_{x,y}}C_\phi^{-1}
   =U_{\ell'_{\phi(x),\phi(y)}}.                            \tag{IS.18}
```

Uniform averaging transports $`\mathcal A,\mathcal M,H,P`$.
No additivity of a coordinate map is required. Therefore different
traces prove nonisomorphism of the loops themselves. Coordinate changes
and right-nucleus section gauges used in the calculation are changes of
presentation; they are not an extra isomorphism hypothesis or an assertion
of invariance under arbitrary isotopy.

For every finite loop, even without the Bol hypothesis,

```math
 \frac{\operatorname{Tr}\mathcal A}{|\mathcal L|}
 =\mathbb P_{x,y,z}\bigl[x\circ(y\circ z)=(x\circ y)\circ z\bigr].
                                                                  \tag{IS.19}
```

Indeed $`\operatorname{Tr}U_g=\#\operatorname{Fix}(g)`$, and the
displayed associativity equality is equivalent to $`\ell_{x,y}z=z`$.
Thus (IS.4), divided by the common order, is the exact difference in
associativity probabilities. This established statistic acquires a new
exact family-specific evaluation here.

For every integer $`t\geq1`$, $`\operatorname{Tr}\mathcal A^t/|\mathcal L|`$
is the return probability averaged over a uniform starting point for
independent uniform inner-defect steps. Equation (IS.3) separates all
these probabilities. Their stationary limit
$`\operatorname{rank}P/|\mathcal L|`$ agrees, so the excess return
probabilities separate as well.

Conjugation averaging preserves trace, and it also makes the diagonal of
$`\mathcal M`$ constant:

```math
 \mathcal M(x,x)=\mathbb E_z\mathcal A(z\circ x,z\circ x)
               =\operatorname{Tr}\mathcal A/|\mathcal L|.     \tag{IS.20}
```

The last equality uses right division: $`z\mapsto z\circ x`$ is a
permutation. Hence the one-step return probability of $`\mathcal M`$
differs at **every** starting point, and its spectra differ. No formula
for higher moments of $`\mathcal M`$ is inferred from this trace identity.

## 5. A canonical large spectral subspace

All eigenvalues with orbit label $`\alpha\ne0`$ lie in $`(0,r]`$.
All those with $`\alpha=0`$ are at least $`49^{-k-1}`$ by the tables.
For $`h\geq1`$,

```math
 r=3^{-24h}<7^{-4h-4}=49^{-k-1}.                            \tag{IS.21}
```

For example, $`3^{24}>7^8`$, and $`4h+4\leq8h`$ proves the whole
range. Thus the two sets of eigenvalues are disjoint and separated.
Define by spectral calculus

```math
 E_h=\mathbf1_{(0,r]}(\mathcal A),\qquad
 T_h=r^{-1}\mathcal A E_h.                                 \tag{IS.22}
```

Here $`E_h`$ is a projection, not the field $`E`$. These operators are
defined on all of $`L^2(\mathcal L_h)`$, with $`T_h=0`$ on
$`\operatorname{ker}E_h`$. The chart merely proves which modes the
spectral definition selects. Even $`h`$ can be recovered without a chart
from the loop order: $`h=(v_3(|\mathcal L_h|)-1)/38`$.
Therefore the filter and normalization commute with every loop isomorphism.

The tables give

```math
 d_h:=\operatorname{rank}E_h=7ST(49^k-17^k),\qquad
 \frac{d_h}{|\mathcal L_h|}=1-(17/49)^k.                     \tag{IS.23}
```

The largest eigenvalue of $`T_h`$ is one, and its multiplicity is

```math
 m_h(X)=\frac{49^k-17^k}{7}
             \bigl[3T+(S-3)X+6S\bigr].                    \tag{IS.24}
```

Every other eigenvalue of $`T_h`$ is at most $`1/9`$.
To see (IS.24), the top value requires compatible field data and
$`\rho=\sigma=0`$. For $`\alpha\ne0`$ some ring plane is active,
so $`\rho\ne0`$ gives at most $`1/9`$, and $`\sigma\ne0`$ gives
$`49^{-k}`$. Summing the top multiplicities gives
$`(S+a_1)\sum_jc_j(3^j-1)`$, which is (IS.24).
The term $`6S`$ retains the singleton zero-vector correction.

In particular the normalized top multiplicity in the low subspace is

```math
 a_h(X):=\frac{m_h(X)}{d_h}
   =\frac{3T+(S-3)X+6S}{49ST},\qquad
 a_h(X_{\rm sp})\sim\frac{1}{49\,9^h},\qquad
 a_h(X_{\rm al})\longrightarrow\frac{1}{49Q}.               \tag{IS.25}
```

The spectral filter is finite and exact. It can also be written as a
polynomial in $`\mathcal A`$ by Lagrange interpolation on the distinct
rational eigenvalues in Theorem 3, assigning zero to the upper band and
one to the lower band. There are $`O(k)`$ possible eigenvalues in each
band. This observation requires no marked chart; it does not assert an
efficient implementation on a loop supplied as a black box.

## 6. An intrinsic collective analytic estimate

### Theorem 4: exact normalization and exponential RMS separation

For either family and every integer $`t\geq1`$,

```math
 a_h(X)\leq\frac{\operatorname{Tr}T_h^{2t}}{d_h}
 \leq a_h(X)+(1-a_h(X))9^{-2t}.                             \tag{IS.26}
```

For $`t=h`$ this gives

```math
 \boxed{
 \frac{\bigl(|\mathcal L_h|^{-1}
                 \operatorname{Tr}T_{\rm sp,h}^{2h}\bigr)^{1/2}}
      {\bigl(|\mathcal L_h|^{-1}
                 \operatorname{Tr}T_{\rm al,h}^{2h}\bigr)^{1/2}}
       \sim 27\,3^{-h}.}                                   \tag{IS.27}
```

Both norms $`\|T_{\rm sp,h}^t\|_{2\to2}`$ and
$`\|T_{\rm al,h}^t\|_{2\to2}`$ are exactly one.

**Proof.** The top $`m_h`$ eigenvalues are one; the other
$`d_h-m_h`$ nonzero eigenvalues are in $`(0,1/9]`$.
This proves (IS.26). The error $`9^{-2h}`$ is negligible relative to
$`a_h(X_{\rm sp})\sim (49\,9^h)^{-1}`$, while the aligned quantity
tends to $`1/(49Q)`$. Their squared ratio is asymptotic to
$`Q\,9^{-h}`$. Taking square roots gives (IS.27), since
$`\sqrt Q=27`$. The factors $`d_h/|\mathcal L_h|`$ cancel exactly.
The top eigenspaces are nonempty, proving the norm assertion. $`\square`$

This estimate has two full-input interpretations. For **any** complete
orthonormal basis $`\{e_i\}_{i=1}^{|\mathcal L_h|}`$ of the normalized
regular Hilbert space,

```math
 \frac1{|\mathcal L_h|}\sum_i\|T_h^t e_i\|_2^2
       =\frac{\operatorname{Tr}T_h^{2t}}{|\mathcal L_h|}.      \tag{IS.28}
```

Equivalently, choose independent uniform signs $`f(x)\in\{-1,1\}`$
on the actual loop elements. Every such $`f`$ has $`\|f\|_2=1`$,
and

```math
 \mathbb E_f\|T_h^t f\|_2^2
       =\frac{\operatorname{Tr}T_h^{2t}}{|\mathcal L_h|}.      \tag{IS.29}
```

The input law is invariant under all relabelings. Neither interpretation
imposes tensorwise centering, a selected pencil frequency, or a preferred
basis. The baseline is the aligned loop with the same order, the same
labeled scalar ranks, the same canonical normalization, and the same
complete input averaging. The filter retains the fraction in (IS.23).
This is a collective mean-square bound, not a bound with the small factor
for each individual input. The fixed sharp norms of the original
$`\mathcal A-P`$ and $`\mathcal M-\Pi`$ are unchanged.

### Theorem 5: a fixed quadratic filter suffices

The iteration in (IS.27) can be replaced by a fixed polynomial. Define on
the same whole regular Hilbert space

```math
 G_h=F(T_h),\qquad F(x)=\frac{49x^2-x}{48}.                  \tag{IS.30}
```

This is a signed self-adjoint observable; it is not asserted to be Markov.
Its norm is one in both families. Put

```math
 b_k=\frac{(43/27)^k-(97/81)^k}{49^k-17^k},\qquad
 \epsilon_h=\frac6{49}\left(1+\frac6T\right)b_k
       +\frac67\left(1-\frac1T\right)49^{-2k}.              \tag{IS.31}
```

Then, for either choice of $`X`$,

```math
 a_h(X)\leq\frac{\operatorname{Tr}G_h^2}{d_h}
       \leq a_h(X)+\epsilon_h,\qquad
 \boxed{\frac{\bigl(|\mathcal L_h|^{-1}\operatorname{Tr}G_{{\rm sp},h}^2\bigr)^{1/2}}
 {\bigl(|\mathcal L_h|^{-1}\operatorname{Tr}G_{{\rm al},h}^2\bigr)^{1/2}}
 \sim27\,3^{-h}.}                                          \tag{IS.32}
```

**Proof.** $`F(1)=1`$, $`F(1/49)=F(0)=0`$, and
$`|F(x)|\leq x\leq1`$ on $`[0,1]`$. Thus the top multiplicity is
preserved and gives the lower bound. All other $`\rho=\sigma=0`$
modes are killed exactly. For $`\rho\ne0,\sigma=0`$, bound the
squared filtered eigenvalue by $`9^{-2j}`$. The table gives their total
normalized bound

```math
 \frac6{49}\left(1+\frac6T\right)
 \frac{\sum_j c_j(3^j-1)9^{-2j}}{49^k-17^k}
 =\frac6{49}\left(1+\frac6T\right)b_k.                      \tag{IS.33}
```

The factor includes the $`w=0`$ singleton; omitting it would lose the
$`6/T`$ correction. Nonzero $`\sigma`$ modes have total low-space
mass $`(6/7)(1-1/T)`$ and scaled eigenvalue at most $`49^{-k}`$,
giving the other term in (IS.31). Finally
$`b_k=O((43/1323)^k)`$ and $`k=2h+1`$, so
$`\epsilon_h=o(9^{-h})`$. Applying (IS.25) proves (IS.32).
The top eigenvalue of $`G_h`$ is one and all other absolute values are
at most one, proving its norm assertion. $`\square`$

The complete-basis and independent-sign interpretations (IS.28)--(IS.29)
apply verbatim with $`G_h`$ replacing $`T_h^t`$.
The fixed polynomial has the same coefficients for all $`h`$ and both
families; the canonical cutoff and scale still depend on the intrinsic
order parameter. Thus this strengthens the collective bound without
claiming a fixed-length Markov walk or a better single-input norm.

## 7. Distinct limiting intrinsic spectral distributions

Let $`\mu_{X,h}`$ be the empirical spectral measure of $`T_h`$ on
$`\operatorname{ran}E_h`$, divided by $`d_h`$. Then

```math
 \begin{split}
 \mu_{{\rm sp},h}&\Longrightarrow
      \frac{48}{49}\delta_0+\frac1{49}\delta_{1/49},\\
 \mu_{{\rm al},h}&\Longrightarrow
      \frac{48}{49}\delta_0+
      \frac{1-Q^{-1}}{49}\delta_{1/49}+
      \frac1{49Q}\delta_1.
 \end{split}                                                \tag{IS.34}
```

The same limits hold if the empirical measure uses the whole regular
space, adding its zero eigenvalues and dividing by $`|\mathcal L_h|`$,
because $`d_h/|\mathcal L_h|\to1`$.

**Proof.** The $`\rho=\sigma=0`$ low modes have total mass
$`(T+6)/(49T)`$. Their only scaled eigenvalues are one and $`1/49`$.
The mass at one is (IS.25), giving the indicated limiting split.
Modes with $`\sigma\ne0`$ have scaled eigenvalue at most
$`49^{-k}\to0`$. For $`\rho\ne0,\sigma=0`$, the scaled eigenvalue
is at most $`9^{-j}`$, and the relative support counts are proportional
to $`\binom{k}{j}16^j(3^j-1)`$. For every fixed $`J`$,

```math
 \frac{\sum_{j=0}^{J}\binom{k}{j}16^j(3^j-1)}{49^k-17^k}
 \longrightarrow0.                                        \tag{IS.35}
```

Hence these modes converge in distribution to zero. The singleton
$`w=0`$ contribution has mass $`1/T`$ and creates no exception.
All measures are supported on $`[0,1]`$, completing the proof.
The unscaled empirical spectra of $`\mathcal A`$ themselves converge
to $`\delta_0`$ in both families; the canonical scale in (IS.22) retains
the distinction that this unscaled limit loses. $`\square`$

## 8. Established methods, new calculation, and the remaining question

The fixed-point trace identity is ordinary permutation-character theory;
[Evans, Section 1](../REFERENCES.md#evans-permutation) gives this interface
explicitly. Counting associative triples is also established: see
[Kepka, Section 1](../REFERENCES.md#kepka-associative-triples) for
commutative Moufang loops, and
[Levin, introductory theorems and Section 2](../REFERENCES.md#levin-associativity)
for Moufang loops with nuclear commutators. Their hypotheses and theorems
do not evaluate this proper Bol family. The existing
[Johnson--Smith comparison](../REFERENCES.md#js-action) supplies Bol
permutation-action context, and the earlier
[rank-support](../REFERENCES.md#rank-support) and
[trace-form](../REFERENCES.md#galois-alternating) references explain why
joint image geometry can carry more information than individual ranks.

No new general permutation-character identity, functional calculus, or
Hilbert--Schmidt principle is claimed. The new calculation is the exact
aggregation of (AQ.29) for these two families, including all orbit and
character multiplicities; its consequences are unmarked nonisomorphism,
all positive-moment separation, the two limiting laws, and the intrinsic
collective bounds (IS.27) and (IS.32). A bounded primary-source comparison is not a
literature-wide priority certification. Nor does the small difference in
raw associativity probabilities establish an efficient sampling-based
isomorphism test.

The sharp remaining analytic question is whether the **unfiltered**
translation-conjugated defect walk $`\mathcal M`$, or an explicitly
specified correlated average of actual defects, admits a collective
mean-square or return-profile separation with a quantified ratio tending
to zero on its entire intrinsic nonstationary space. The present result
provides the one-step $`\mathcal M`$ separation, but not its full spectrum
or higher-time comparison. Its first decisive next calculation is
$`\operatorname{Tr}(\mathcal M-\Pi)^2`$ for these same pencils, keeping
the shared translation and character phases. Replacing those phases by
separately averaged scalar ranks would lose precisely the correlations
that need testing. A proposed worst-case improvement must use a different
specified operator or explicitly justified intrinsic subspace, since the
existing norms are sharp.

## 9. Executable evidence and review scope

The [spectrum checker](../code/verify_bol_intrinsic_spectrum.py) constructs
the rational spectral multiset, checks dimensions, exceptional eigenvalues,
fixed spaces, moment differences, the spectral cutoff, and the collective
bounds. The [independent incidence and orbit checker](../code/verify_bol_intrinsic_incidence_independent.py)
constructs the smallest actual extension-field pencils and checks image
intersections and orbit-label aggregation independently of the compressed
formula. Exact commands, finite coverage, toolchain, and limitations are
recorded in [the code guide](../code/README.md#intrinsic-spectral-separation).
These computations support the uniform proofs; they do not enumerate the
enormous loop tables or certify theorems by extrapolation. The noncontributing
reviewer and exact frozen source are recorded separately in the existing
[review record](../evidence/bol-metaplectic-review.md).

