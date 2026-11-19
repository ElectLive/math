# Counting and seven-value coverage for a trace–exponential family

Mira Cult

## Results and context

This paper studies an explicit equation over $`\mathbb F_7`$, with variables
in growing vector spaces over $`\mathbb F_{729}`$. It proves:

* an exact classification of its output degrees, including zero-degree rows;
* a sharp pair-collision and source-variance theorem, giving counting for
  arbitrary correlated output sets even when the input set is very small;
* seven-value coverage for almost every parameter whenever the input-set
  cardinality tends to infinity, and an explicit 37-point existence theorem;
* the full degree-aware consequences of the earlier collective norm;
* exactly biregular fixed-value relations with a proved restriction cost; and
* actual incidence-free and coverage obstructions for the matched-rank
  aligned family.

The sharp collision theorem, its small-source applications, degree calculation,
regularization, and attainable-count comparisons are the contributions here.
The exact full-space centered norm is an **existing result**, reproduced
below for self-containment. It is Theorem D of
[the collective manuscript](bol-collective-cancellation.md#6a-coupled-pencils-and-an-exact-norm-on-all-mean-zero-inputs),
which has received independent AI mathematical review. Later intrinsic spectral work is separate and is not a premise of this application.

Fourier orthogonality, expander mixing, Moore polynomial root bounds,
complete weight enumerators, and almost-universal hashing are established
methods. In particular the abstract collision-to-count conversion is covered
by [LHL, Lemma 3.1](../INCIDENCE_REFERENCES.md#incidence-lhl).
The exact collision profile and its equality cases below concern this
specified family. We do not establish a new general incidence method, a new
rank-metric code, a better general extractor, or literature-wide priority.
The theorem-by-theorem comparison in Section 9 makes these boundaries explicit.

The [verification note](../evidence/bol-collective-incidence-review.md) describes the independent review and computational scope.

## 1. The equation, measures, and constants

Fix an integer $`h\ge1`$, and put
```math
 Q=729,\quad E=\mathbb F_Q,\quad L=\mathbb F_{Q^h},\quad
 k=2h+1,\quad W=L^3\oplus L^3,\quad N=|W|=Q^{6h}.
```
Choose any injective $`\mathbb F_3`$-linear map
$`j:\mathbb F_3^k\longrightarrow L`$. Such maps exist since $`k\le6h`$.
For $`t=j(\nu)`$ set $`z(t)=(t,t^3,t^9)`$ and define the alternating
$`E`$-bilinear form
```math
 B_\nu(x,y)=\operatorname{Tr}_{L/E}
 \left(\det[z(t),x^{(1)},y^{(1)}]
       +\det[z(t),x^{(2)},y^{(2)}]\right).
 \tag{1.1}
```
Here $`x=(x^{(1)},x^{(2)})`$, with each block in $`L^3`$; the notation also
denotes its matrix in a fixed $`E`$-basis.
Let $`B_i=B_{e_i}`$ and
```math
 \beta_i(u,y)=\operatorname{Tr}_{E/\mathbb F_3} B_i(u,y),\qquad
 S(a)=\sum_{i=1}^k2^{a_i}\in\mathbb F_7,\qquad
 F(u,a,y)=S(a-\beta(u,y)).
 \tag{1.2}
```
The exponent is in $`\mathbb F_3`$, with representatives $`0,1,2`$, so its
values are $`1,2,4`$ in $`\mathbb F_7`$.

Take
```math
 X=W,\quad Z=W\times\mathbb F_3^k,\quad
 Y=Z\times\mathbb F_7,\quad M=|Y|=7N3^k.
```
Every space has uniform probability measure unless a cardinality sum is
explicitly written. For $`A\subseteq X`$, $`D\subseteq Y`$, define
```math
 e(A,D)=\#\{(y,(u,a,s))\in A\times D:F(u,a,y)=s\},\quad
 \alpha=|A|/N,\quad \beta_D=|D|/M.
 \tag{1.3}
```
We usually abbreviate $`\beta_D`$ to $`\beta`$; the vector-valued bilinear map
always has arguments. Every input has exactly $`N3^k=M/7`$ neighbors.
An output $`(u,a,s)`$ has degree
$`d(u,a,s)=\#\{y:F(u,a,y)=s\}`$, which need not equal $`N/7`$.

The fixed constants used throughout are
```math
 a_*=\frac29,\qquad b_*=\frac{7-\sqrt{21}}{18},\qquad
 m_*=\frac{7+\sqrt{21}}{18}<1,\qquad
 P_j=a_*^j+b_*^j+m_*^j,
```
```math
 g_h=P_{2h}-a_*^{2h+1},\quad
 \ell_h=b_*^k+m_*^k,\quad
 \varepsilon_h^2=\frac6{49}Q^{-4h}g_h.
 \tag{1.4}
```
In particular $`g_h\sim m_*^{2h}`$ and $`P_k\sim m_*^{2h+1}`$ as
$`h\to\infty`$. The primes and $`Q`$ stay fixed. Writing
```math
 \delta_*=\frac{\log(1/m_*)}{6\log Q}
       =0.011147140626\ldots
```
gives $`m_*^{2h}=N^{-2\delta_*}`$.

We will use the distribution
```math
 p_k(s)=3^{-k}\#\{a\in\mathbb F_3^k:S(a)=s\},\quad
 \lambda_k=7\min_s p_k(s),\quad r_*=\sqrt2/3.
 \tag{1.5}
```
For $`k\ge3`$ every $`p_k(s)`$ is positive.

## 2. Exact output degrees

### Theorem DEG: all degree strata

Put $`v=(3^k-1)/2`$. For each projective parameter $`[\nu]`$ define
```math
 R_{[\nu]}=Lz(j\nu)\oplus Lz(j\nu)\subseteq W.
```
These $`v`$ subspaces have cardinality $`Q^{2h}`$ and meet pairwise only at
zero. Define
```math
 G=W\setminus\bigcup_{[\nu]}R_{[\nu]},\qquad
 \tau=\frac{1+v(Q^{2h}-1)}N,\qquad \gamma=1-\tau.
 \tag{2.1}
```
Then the following exhaustive formulas hold.

1. For $`u=0`$, $`d(0,a,s)=N\,1_{\{s=S(a)\}}`$.
2. For $`u\in G`$, $`d(u,a,s)=Np_k(s)`$, independently of $`a`$.
3. For $`0\ne u\in R_{[\nu]}`$,
   ```math
   d(u,a,s)=\frac{N}{3^{k-1}}C_\nu(\nu\cdot a,s),\qquad
   C_\nu(c,s)=\#\{b:\nu\cdot b=c,\ S(b)=s\}.
   \tag{2.2}
   ```
   There are exactly $`v(Q^{2h}-1)`$ such nonzero $`u`$.

In particular the ranks over $`\mathbb F_3`$ of $`y\mapsto\beta(u,y)`$
are respectively $`0,k,k-1`$.

**Proof.**
For $`\nu\ne0`$, the radical of the determinant form on one block is
$`Lz(j\nu)`$. If $`x`$ is outside that line, its determinant pairing with
$`y`$ is onto $`L`$, and the trace is nonzero. Thus $`B_\nu`$ has radical
$`R_{[\nu]}`$ and $`E`$-rank $`4h`$.

If $`z(s)`$ and $`z(t)`$ are proportional, comparison of their first and
second coordinates gives $`s/t=(s/t)^3`$, so $`s/t\in\mathbb F_3^\times`$.
Injectivity of $`j`$ proves the asserted disjointness. For
```math
 H_u=\{\nu:B_\nu u=0\},
```
nondegeneracy of the absolute trace pairing gives
$`\operatorname{im}\beta(u,\cdot)=H_u^\perp`$. If $`u\ne0`$, the
disjointness implies that $`H_u`$ is zero or a single parameter line.
Every fiber of this linear map has the same size. The vector
$`a-\beta(u,y)`$ is therefore uniform on $`a+H_u^\perp`$, proving all
formulas and counts. This also works when $`3\mid h`$; no trace-of-one
assumption is used. $`\square`$

### Exact generic distribution

Let $`U_0=2`$, $`U_1=-1`$, and $`U_j=-U_{j-1}-2U_{j-2}`$. With
$`H=\{1,2,4\}\subseteq\mathbb F_7`$,
```math
 3^k p_k(s)=
 \begin{cases}
 (3^k+3U_k)/7,&s=0,\\
 (3^k+2U_{k-1})/7,&s\in H,\\
 (3^k+U_{k+1})/7,&s\in-H.
 \end{cases}
 \tag{2.3}
```
To prove this, put $`\zeta=e^{2\pi i/7}`$ and
$`T=\zeta+\zeta^2+\zeta^4`$. Then $`T+\bar T=-1`$, $`T\bar T=2`$,
and $`U_j=T^j+\bar T^j`$. Fourier inversion on $`\mathbb F_7`$,
separating its two nonzero multiplicative orbits, gives (2.3). It also gives
```math
 |7p_k(s)-1|\le6r_*^k=:\Delta_h,
 \tag{2.4}
```
with the sharper $`2\sqrt2\,r_*^k`$ for $`s\ne0`$.

| $`k`$ | $`3^kp_k(0)`$ | $`3^kp_k(s)`$, $`s\in H`$ | $`3^kp_k(s)`$, $`s\in-H`$ |
|---:|---:|---:|---:|
| 3 | 6 | 3 | 4 |
| 5 | 30 | 35 | 36 |
| 7 | 318 | 315 | 308 |
| 9 | 2814 | 2803 | 2820 |
| 11 | 25278 | 25323 | 25300 |

These degrees are never exactly $`N/7`$: $`N`$ is a power of three.
Even typical output degrees depend on $`s`$.

### Proposition DEG-U: uniform control away from zero

Put
```math
 \eta_h=6\left(a_*^{k/2}+b_*^{k/2}+m_*^{k/2}\right).
```
For every $`u\ne0`$ and every $`a,s`$,
```math
 \left|\frac{7d(u,a,s)}N-1\right|\le\eta_h=O(m_*^h).
 \tag{2.5}
```
All these degrees are positive for $`h\ge3`$; for $`h=1,2`$ some are zero.

**Proof of (2.5).**
For a nonzero additive character $`\rho`$ of $`\mathbb F_7`$, set
```math
 c_\rho(t)=\frac13\sum_{b\in\mathbb F_3}
                  e_7(\rho2^b)e_3(tb).
```
The squared moduli are $`a_*,b_*,m_*`$, with the last two possibly
interchanged. This follows from $`T+\bar T=-1`$, $`T\bar T=2`$ and
Fourier inversion; it is also the one-coordinate weight calculation in the
collective manuscript, Section 4.

Conditioning uniform $`b`$ on $`\nu\cdot b=c`$ expresses its nonzero
$`\mathbb F_7`$ Fourier coefficient as three products of these $`c_\rho`$.
If the normal $`\nu`$ has coordinate counts $`n_0,n_1,n_2`$, its modulus is
at most
```math
 r_*^k+
 r_*^{n_0}\left(m_*^{n_1/2}b_*^{n_2/2}
               +b_*^{n_1/2}m_*^{n_2/2}\right)
 \le r_*^k+m_*^{k/2}+b_*^{k/2}.
```
For fixed support, the sum is maximized when all nonzero signs agree:
$`x^j+x^{w-j}\le1+x^w`$ for $`x>1`$. Increasing support increases
$`r_*^{k-w}(m_*^{w/2}+b_*^{w/2})`$, since the successive power-sum
ratio is at least $`(\sqrt{m_*}+\sqrt{b_*})/2>r_*`$.
Fourier inversion over the six nonzero $`\rho`$ proves (2.5).
Generic rows obey the sharper (2.4). $`\square`$

For an exact positive finite bound, $`d/N\ge35/729`$ for every nonzero
$`u`$ when $`k\ge7`$. Here is a finite integer certificate, rather than an
extrapolation. Starting $`C_{0,0,0}(0,0)=1`$, adjoining a coordinate of
normal type $`j\in\{0,1,2\}`$ replaces
```math
 C(c,s)\quad\text{by}\quad
 \sum_{b=0}^2 C(c-jb,s-2^b),
 \tag{2.6}
```
with indices modulo three and seven. At $`k=7`$ the minima and maxima
over $`n_1+n_2=7-n_0`$, $`c`$, and $`s`$ are:

| $`n_0`$ | minimum | maximum |
|---:|---:|---:|
| 0 | 35 | 210 |
| 1 | 45 | 180 |
| 2 | 71 | 135 |
| 3 | 86 | 123 |
| 4 | 90 | 117 |
| 5 | 95 | 108 |
| 6 | 101 | 108 |

These entries are finite identities obtained by (2.6), reproduced by two
implementations. For larger $`k`$, select seven coordinates containing a
nonzero coefficient, condition on all the rest, and apply this table.
For $`k=3,5,7,9,11`$, the exact minima are
$`0,\ 0,\ 35/729,\ 378/6561,\ 5610/59049`$.
For example at $`k=5`$, $`\nu=(1,1,1,1,1)`$, $`c=0`$, $`s=3`$ gives zero.
The uniform asymptotic (2.5), rather than this coarse positive bound,
is used for the large-$`h`$ density range.

## 3. A sharp collision theorem and small-source counting

Write
```math
 w(\nu)=\prod_i w_{\nu_i},\qquad
 (w_0,w_1,w_2)=(a_*,b_*,m_*)
```
up to interchanging $`w_1,w_2`$, and put
```math
 K(z)=\sum_\nu w(\nu)1_{\{B_\nu z=0\}}.
 \tag{3.1}
```
For $`A\ne\varnothing`$, write $`n=|A|`$ and
```math
 P_A(u,a;s)=\frac1n\#\{y\in A:F(u,a,y)=s\}.
```

### Theorem COL: exact collision profile and optimal source variance

For distinct $`y,z`$,
```math
 \Pr_{(u,a)\in Z}\{F(u,a,y)=F(u,a,z)\}
             =\frac{1+6K(y-z)}7.
 \tag{3.2}
```
For a nonzero difference $`d`$,
```math
 K(d)=
 \begin{cases}
 a_*^k,&d\in G,\\
 a_*^k+w(\nu)+w(-\nu),&0\ne d\in R_{[\nu]}.
 \end{cases}
 \tag{3.3}
```
In particular $`K(d)\le P_k`$, with equality for every nonzero
$`d\in R_{[(1,\ldots,1)]}`$. For each fixed input, the seed-averaged
output law is $`p_k`$.

Define
```math
 \theta_h(n)=\frac{1-a_*^k}{n}
              +\left(1-\frac1n\right)\ell_h,\qquad
 \Theta_h(n)=\frac1n+\left(1-\frac1n\right)P_k
             =\theta_h(n)+a_*^k.
 \tag{3.4}
```
Then
```math
 \mathbb E_{u,a}\sum_s(P_A(u,a;s)-p_k(s))^2
 =\frac6{7n^2}\sum_{y,z\in A}(K(y-z)-a_*^k)
 \le\frac67\theta_h(n),
 \tag{3.5}
```
and
```math
 \mathbb E_{u,a}\sum_s(P_A(u,a;s)-1/7)^2
 \le\frac67\Theta_h(n).
 \tag{3.6}
```
For every integer $`1\le n\le Q^{2h}`$, **both upper bounds are attained**:
take any $`n`$-element subset of $`R_{[(1,\ldots,1)]}`$.
Thus these are the exact worst-case second moments in that cardinality range.

**Proof.**
Insert $`1_{\{x=y\}}=7^{-1}\sum_{\rho\in\mathbb F_7}e_7(\rho(x-y))`$
and average in $`a`$. The Fourier labels on $`\mathbb F_3^k`$ must agree.
Averaging in $`u`$ then leaves exactly $`B_\nu(y-z)=0`$. All six nonzero
$`\rho`$ give the same kernel: multiplication by $`2`$ translates the shifts,
and changing its sign conjugates and replaces $`\nu`$ by $`-\nu`$.
This proves (3.2). Theorem DEG proves (3.3).

For a parameter vector having $`\ell`$ nonzero coordinates,
```math
 w(\nu)+w(-\nu)\le
 a_*^{k-\ell}(m_*^\ell+b_*^\ell)\le m_*^k+b_*^k.
```
The first inequality follows from $`x^j+x^{\ell-j}\le1+x^\ell`$.
For the second, the successive ratio
$`(m_*^{\ell+1}+b_*^{\ell+1})/(m_*^\ell+b_*^\ell)`$ is at least
$`(m_*+b_*)/2>a_*`$. Equality is obtained with all coordinates equal
and nonzero.

Uniform $`a`$ makes $`a-\beta(u,y)`$ uniform for every fixed $`u,y`$,
so $`\mathbb E_{u,a}P_A(s)=p_k(s)`$.
Two independent uniform shift vectors have collision probability
```math
 \sum_s p_k(s)^2=\frac17+\frac67a_*^k.
```
This also follows by Parseval from $`|T/3|^2=a_*`$.
Expand the square in (3.5) and use (3.2). Diagonal pairs contribute
$`K(0)-a_*^k=1-a_*^k`$; every off-diagonal pair contributes at most
$`\ell_h`$. This proves (3.5). Orthogonal centering around $`p_k`$ and
the uniform law adds exactly $`(6/7)a_*^k`$, giving (3.6).
All nonzero differences of a subset of the displayed radical lie in that
same radical, proving the equality assertion. $`\square`$

The collision bound is an almost-universal hash statement for this particular
seven-symbol family:
```math
 \max_{y\ne z}\Pr[F(u,a,y)=F(u,a,z)]
      =\frac17+\frac67P_k.
 \tag{3.7}
```
Its alphabet is $`\mathbb F_7`$ and its seed set has cardinality $`N3^k`$.
This terminology records the verified property, not an extractor-performance
claim.

### Theorem SMALL: arbitrary-output counts from small sources

For every nonempty $`A\subseteq W`$ and every $`D\subseteq Y`$,
```math
 \boxed{\quad
 \left|e(A,D)-\frac{n|D|}{7}\right|
 \le \frac{nM}{7}
       \sqrt{6\Theta_h(n)\,\beta(1-\beta)} .
 \quad}
 \tag{3.8}
```
A more informative biased main term has the bound
```math
 \left|e(A,D)-n\sum_{(u,a,s)\in D}p_k(s)\right|
 \le\frac{\sqrt6}{7}nM
       \sqrt{\theta_h(n)\,\beta(1-\beta)}.
 \tag{3.9}
```
These formulas do not assume uniform output degrees.
The degree error has been paid through the source's entire collision variance.

For $`0<\beta\le1`$, (3.8) gives relative error at most
```math
 R_{\mathrm{small}}=
       \sqrt{6\Theta_h(n)\frac{1-\beta}{\beta}}.
 \tag{3.10}
```
There is an incidence whenever
```math
 \frac{\beta}{1-\beta}>6\Theta_h(n),
 \tag{3.11}
```
with $`\beta=1`$ interpreted directly. In cardinalities this is
$`|D|>6M\Theta_h(n)/(1+6\Theta_h(n))`$.
Every incidence-free $`D`$ satisfies the reverse weak inequality.

In particular, for arbitrary sequences $`A_h,D_h`$ as $`h\to\infty`$,
```math
 n_h\beta_h\longrightarrow\infty,\qquad
 \frac{\beta_h}{P_{2h+1}}\longrightarrow\infty
 \quad\Longrightarrow\quad
 e(A_h,D_h)\sim\frac{|A_h||D_h|}{7}.
 \tag{3.12}
```
This allows, for example, $`n_h=h`$ and $`\beta_h=h^{-1/2}`$.
There is no product condition on $`D_h`$.

**Proof.**
On $`Y`$ with its uniform measure,
$`\mathbb E_Y(P_A-1/7)=0`$ and
$`\|P_A-1/7\|_2^2\le6\Theta_h(n)/49`$ by (3.6).
Now
```math
 e(A,D)-n|D|/7=nM\langle P_A-1/7,1_D-\beta\rangle.
```
Cauchy--Schwarz gives (3.8); (3.5) gives (3.9) in exactly the same way.
The remaining assertions follow by dividing by the positive main term.
For (3.12), use $`\Theta_h(n)\le1/n+P_k`$.
These are deterministic statements about all sets, not random-set hypotheses.
$`\square`$

At $`n=1`$, taking $`D`$ to be the complement of the input's neighbors
gives $`\beta=6/7`$ and equality in the zero-incidence threshold (3.11).
For larger $`n`$, sharpness of the variance does not assert sharpness of every
indicator discrepancy or existence threshold.

### Theorem COVER: all seven values

For every nonempty $`A\subseteq W`$,
```math
 \Pr_{u,a}\bigl[F(u,a,A)\ne\mathbb F_7\bigr]
 \le \min\left\{1,\ 36\Theta_h(n),\
                    \frac{36\theta_h(n)}{\lambda_k^2}\right\}.
 \tag{3.13}
```
Consequently:

* if $`h\to\infty`$ and $`|A_h|\to\infty`$, the fraction of parameters
  producing every value is $`1-o(1)`$, uniformly over all such sets;
* for every $`h\ge8`$, **every set of at least 37 inputs has a parameter
  pair $`(u,a)`$ for which all seven values occur**.

**Proof.**
A probability distribution supported on at most six symbols has collision
sum at least $`1/6`$. Hence its squared distance from the uniform seven-symbol
law is at least $`1/6-1/7=1/42`$. Markov's inequality and (3.6) give
$`36\Theta_h(n)`$. If a symbol $`s`$ is missing, its deviation from $`p_k`$
is $`-p_k(s)`$. The other six deviations sum to $`p_k(s)`$, so their
squares sum to at least $`p_k(s)^2/6`$. Applying (3.5) gives
$`36\theta_h(n)/\lambda_k^2`$.

For the numerical endpoint, $`P_{17}<1/1700`$. One entirely rational
certificate is
```math
 (2/9)^{17}+(29/45)^{17}+(7/50)^{17}<1/1700,
```
using $`m_*<29/45`$ and $`b_*<7/50`$. The $`P_j`$ decrease, and
$`\Theta_h(n)`$ decreases in $`n`$. Thus for $`h\ge8,n\ge37`$,
```math
 36\Theta_h(n)\le
 \frac{36}{37}+\frac{1296}{37\cdot1700}
 =\frac{62496}{62900}<1.
```
In fact at least $`101/15725`$ of all seeds cover the alphabet under this
conservative bound. This proves existence without enumerating the ambient
space. No optimality of the number 37 is claimed. $`\square`$

If seeds are themselves constrained to an arbitrary set $`C\subseteq Z`$,
its density exceeding the right side of (3.13) guarantees a **single**
seed in $`C`$ that realizes all seven equations, with separate inputs in $`A`$.
No product structure of $`C`$ is needed. In particular its density may tend
to zero if $`|A||C|/|Z|\to\infty`$ and $`|C|/|Z|\gg P_k`$.

### Theorem TRANS: removing the collision floor on an explicit class

Let
```math
 T_0=\{(x,x')\in L^3\oplus L^3:x_1=x'_1=0\},
 \qquad |T_0|=Q^{4h}.
```
Every nonzero difference of points in an affine coset of $`T_0`$ lies in
$`G`$: a vector in $`R_{[\nu]}`$ has blocks $`c\,z(j\nu),c'\,z(j\nu)`$,
and their first coordinates can both vanish only when $`c=c'=0`$.
Consequently for every nonempty $`A`$ in such a coset,
```math
 \mathbb E_{u,a}\sum_s(P_A(s)-p_k(s))^2
       =\frac67\,\frac{1-a_*^k}{|A|}.                 \tag{3.14}
```
For arbitrary $`D`$, (3.9) therefore holds with
$`\theta_h(n)=(1-a_*^k)/n`$. In particular
```math
 \left|\frac{e(A,D)}{|A||D|/7}-1\right|
 \le \Delta_h+
    \sqrt{\frac{6(1-a_*^k)(1-\beta)}{n\beta}}.       \tag{3.15}
```
Thus $`n\beta\to\infty`$ alone suffices for the flat asymptotic as
$`h\to\infty`$ in this explicitly stated input class.

There is also exact pairwise independence with marginal $`p_k`$:
for distinct $`y,z`$ in the coset, $`\beta(u,z-y)`$ is uniform on
$`\mathbb F_3^k`$, while $`a-\beta(u,y)`$ is uniform and independent of $`u`$.
Their two translated exponent vectors are independent and uniform,
so $`(F(u,a,y),F(u,a,z))`$ has law $`p_k\otimes p_k`$.
This proves (3.14) directly as well. The improvement comes from a proved
difference-avoidance property, not from inheriting a full-space estimate on
an input slice.

## 4. The earlier collective norm and the correct baseline

Define
```math
 (If)(u,a,s)=\mathbb E_y f(y)1_{\{F(u,a,y)=s\}}.
```
Then $`I1=d/N`$ and $`I^*1=1/7`$. The earlier Bol-word observable is
$`Rf=\mathbb E_y f(y)\vartheta(s-F(u,a,y))`$, where
$`\vartheta(0)=1`$ and $`\vartheta(t)=\omega^{-1}`$ for $`t\ne0`$,
$`\omega=e^{2\pi i/3}`$. Therefore
```math
 Rf=(1-\omega^{-1})If,\qquad \mathbb E f=0,\qquad
 |1-\omega^{-1}|=\sqrt3.
 \tag{4.1}
```
The exact incidence norm is the word norm divided by $`\sqrt3`$, not by
three. The latter division applies to its square.

### Lemma SPEC (existing norm, reproduced)

For the spread family,
```math
 \|I|_{L^2_0(W)}\|^2=\varepsilon_h^2
                    =\frac6{49}Q^{-4h}g_h.
 \tag{4.2}
```
For the aligned family of Section 7 it is
```math
 \varepsilon_{\mathrm{al},h}^2
       =\frac6{49}Q^{-4h}(1-a_*^k).
 \tag{4.3}
```
The latter is the sharp separate-rank bound with these weights.

**Proof.**
Fourier expansion in $`s`$ and $`a`$ gives the Gram identity
```math
 I^*I=\frac1{49}\Pi+\frac6{49}T^*T,\qquad
 (Tf)(u,a)=\mathbb E_y f(y)e_7(S(a-\beta(u,y))).
```
The normalized convolution kernel of $`T^*T`$ is $`K`$ in (3.1).
For a nonzero spatial frequency $`\xi`$ its multiplier is
```math
 Q^{-4h}\sum_{\substack{\nu\ne0\\\xi\in\operatorname{im}B_\nu}}w(\nu).
 \tag{4.4}
```
Using the absolute trace pairing on $`L^6`$, the common parameter constraint is
```math
 \xi^{(j)}_1t+\xi^{(j)}_2t^3+\xi^{(j)}_3t^9=0,\qquad j=1,2.
```
A nonzero polynomial here has at most nine roots, so the allowed parameter
subspace $`D_\xi\le\mathbb F_3^k`$ has dimension at most two.
The zero parameter must be removed.

For completeness, for $`1\le d<k`$ the largest product mass of a
$`d`$-dimensional subspace of $`F^k`$, with identical coordinate law $`w`$, is
```math
 \max\{w(0)^{k-d},\ \sum_{t\in F}w(t)^{k-d+1}\}.
```
Choose $`d`$ information coordinates and express the others as linear forms.
Hölder bounds the product by the corresponding $`(k-d)`$-th moments.
Conditioning all but one nonzero coefficient makes each form's law a
convex combination of affine permutations of $`w`$; rearrangement bounds
its moment by $`\sum w^{k-d+1}`$. A zero form contributes $`w(0)^{k-d}`$.
Taking all extra coordinates zero, or all equal to the first free coordinate,
attains the alternatives. Here $`P_2=13/27>a_*`$, so the dimension-two
maximum is $`P_{2h}`$. Removing zero leaves $`g_h`$.

Every parameter plane occurs as $`D_\xi`$: for its image
$`\langle a,b\rangle_{\mathbb F_3}\le L`$, let
$`u=b^3-a^2b\ne0`$. The polynomial
```math
 (X^3-a^2X)^3-u^2(X^3-a^2X)
 =X^9-(a^6+u^2)X^3+u^2a^2X
```
has exactly this plane as its roots. Its coefficients form one spatial
block, with the other zero. Choose the plane
$`\{(s,\ldots,s,t):s,t\in\mathbb F_3\}`$ for equality.
In the aligned family every nonzero scalar image contains its first
star-coordinate axis, giving (4.3). $`\square`$

The extra exponent does not require the exact product-mass constant:
the elementary bound $`|D_\xi\setminus0|\le8`$ and
$`w(\nu)\le m_*^k`$ already gives
$`\varepsilon_h^2\le(48/49)Q^{-4h}m_*^k`$.
It has the same exponent, with asymptotic squared-constant loss $`8m_*`$.
The exact formula sharpens this established Fourier/Moore route.

### Theorem MIX: arbitrary subsets, with their actual degrees

For all $`A,D`$,
```math
 \boxed{\quad
 \left|\frac{e(A,D)-\alpha e(X,D)}{NM}\right|
 \le\varepsilon_h\sqrt{\alpha(1-\alpha)\beta(1-\beta)} .
 \quad}
 \tag{4.5}
```
**Proof.**
Since $`I^*1=1/7`$,
```math
 \frac{e(A,D)-\alpha e(X,D)}{NM}
 =\langle I(1_A-\alpha),1_D-\beta\rangle.
```
Apply (4.2) and the exact variances of the two indicators. $`\square`$

For nonempty $`D`$, write $`\bar d_D=e(X,D)/|D|`$ and
$`r_D=\bar d_D/N`$. The exact relative-error upper bound from (4.5) is
```math
 R_{\mathrm{spec}}=
 \frac{\varepsilon_h}{r_D}
 \sqrt{\frac{(1-\alpha)(1-\beta)}{\alpha\beta}}.
 \tag{4.6}
```
If $`r_D>0`$, existence follows from
```math
 \frac{\alpha\beta}{(1-\alpha)(1-\beta)}
       >\frac{\varepsilon_h^2}{r_D^2}.
 \tag{4.7}
```
Equivalently,
```math
 \frac{|A||D|}{(1-\alpha)(1-\beta)}
       >\frac{\varepsilon_h^2 NM}{r_D^2}.
```
Relative error at most $`t>0`$ follows by dividing the right side by $`t^2`$.
Incidence-free pairs satisfy the reverse weak inequality.
These statements include very unequal densities and the finite-population
factors; endpoints with an empty set are trivial. If $`\alpha=1`$ the
degree baseline is exact, regardless of $`r_D`$.
If $`\beta=1`$, then $`e(A,Y)=|A|M/7`$ exactly; the odds-ratio
conditions are interpreted directly at this endpoint.

For outputs of normalized degree at least $`\lambda/7`$, (4.7) is implied by
```math
 \frac{\alpha\beta}{(1-\alpha)(1-\beta)}
       >\frac{6g_hQ^{-4h}}{\lambda^2},
 \tag{4.8}
```
or in cardinalities by
$`|A||D|>42\,3^kQ^{8h}g_h(1-\alpha)(1-\beta)/\lambda^2`$.
The aligned/separate-rank version replaces $`g_h`$ by $`1-a_*^k`$,
with its **own** degree condition. The spread degree theorem must not be
applied to arbitrary aligned outputs.

### When the flat baseline is correct

It is exactly correct for a particular $`D`$ precisely when
$`\sum_D(d-N/7)=0`$. On $`G\times\mathbb F_3^k\times\mathbb F_7`$,
$`e(X,D)=N\sum_Dp_k(s)`$, so the incidence main term is
$`|A|\sum_Dp_k(s)`$. Equal numbers of outputs at each
symbol make it flat, but a single-symbol selection generally does not.
At $`u=0`$, select $`s=S(a)`$ or its complement: the proposed flat baseline
can be wrong by a factor seven or can be positive when all degrees vanish.

For arbitrary $`D`$, (2.5) and the size of the zero slice give
```math
 \left|\frac{e(X,D)}{NM}-\frac{\beta}{7}\right|
 \le\frac{\eta_h\beta}{7}+\frac6{7N}.
```
Consequently, for $`\alpha\beta>0`$,
```math
 \left|\frac{e(A,D)}{|A||D|/7}-1\right|
 \le \eta_h+\frac6{N\beta}
  +\sqrt{6g_hQ^{-4h}\frac{(1-\alpha)(1-\beta)}{\alpha\beta}}.
 \tag{4.9}
```
There is also the useful generic-mass lower bound
```math
 \frac{e(X,D)}{NM}
 \ge\frac{1-\Delta_h}{7}\max(\beta-\tau,0),
 \tag{4.10}
```
when $`1-\Delta_h\ge0`$; alternatively use $`\lambda_k`$ exactly.

Thus, uniformly over **all** subsets of the full spaces,
```math
 \frac{\alpha_h\beta_h}{g_hQ^{-4h}}\longrightarrow\infty
 \quad\Longrightarrow\quad
 e(A_h,D_h)\sim|A_h||D_h|/7 .
 \tag{4.11}
```
Indeed $`\eta_h\to0`$, and the hypothesis forces
$`N\beta_h\gg Ng_hQ^{-4h}\ge(Q^2m_*^2)^h\to\infty`$.
There is no extra exceptional-set hypothesis in this asymptotic assertion.

## 5. The full useful regimes and their limitations

The two main estimates answer different sparse questions. Take the smaller
of the explicit relative-error bounds (3.10) and (4.9), or retain the
degree-dependent formula (4.6) when it is better. The sufficient regions are:

| Situation | Sufficient condition for relative error $`o(1)`$ as $`h\to\infty`$ | Main term |
|---|---|---|
| Separate-rank spectral estimate, with suitable degrees | $`\alpha\beta\gg Q^{-4h}`$ | $`\alpha e(X,D)`$; flat only with degree control |
| Collective spectral estimate, arbitrary full-space sets | $`\alpha\beta\gg Q^{-4h}m_*^{2h}`$ | $`|A||D|/7`$ |
| Sharp collision estimate, arbitrary full-space sets | $`|A|\beta\to\infty`$ and $`\beta\gg m_*^{2h+1}`$ | $`|A||D|/7`$ |
| Input in an affine coset of $`T_0`$, arbitrary outputs | $`|A|\beta\to\infty`$ | $`|A||D|/7`$ |
| Fixed nonzero value, generic $`u`$, arbitrary correlated parameters | $`|A||C|\gg3^kQ^{8h}m_*^{2h}`$ | $`p_k(s)|A||C|`$ |
| All-seven-value coverage | $`|A|\to\infty`$ | covering fraction $`1-o(1)`$ |
| Finite all-seven-value existence | $`h\ge8`$, $`|A|\ge37`$ | at least one covering seed |

Here $`\gg`$ in the asymptotic rows means that the displayed ratio tends to
infinity, not an unspecified fixed constant. Finite constants and endpoint
factors are (3.10), (3.11), (3.13), (4.7), and (6.5) below.

For the full spectral regime the threshold gain is exactly
$`g_h/(1-a_*^k)\sim m_*^{2h}`$ in a degree comparison with the same
$`\lambda`$. In terms of $`N`$ the density-product scale improves from
$`N^{-2/3}`$ to $`N^{-2/3-2\delta_*}`$.
Balanced densities therefore improve from order $`N^{-1/3}`$ to
$`N^{-1/3-\delta_*}`$. Unequal densities are allowed without changing
their product criterion.

The collision region is materially different. For $`|A|=h`$ and
$`\beta=h^{-1/2}`$ its error tends to zero, while the centered spectral
bound is vacuous. Conversely, at $`\alpha=\beta=Q^{-2h}`$ the collective
spectral estimate tends to zero, whereas (3.10) is vacuous.
Thus neither region contains the other.

For fixed $`n\le N^{1/3}`$, the exact second-moment envelope in (3.5)
cannot be improved uniformly: a single radical realizes it.
This does not prove optimal empty-rectangle bounds, which concern indicators
on both sides and may improve on Cauchy--Schwarz. No exhaustive
characterization of all incidence-free pairs is claimed.

## 6. Exact regularization and a fixed-value counting theorem

The degree calculation suggests a repair rather than an uncharged slice.
Fix $`s\in\mathbb F_7`$ and use
```math
 X=W,\qquad Y_s=G\times\mathbb F_3^k,\qquad
 M_s=|Y_s|=\gamma N3^k,\qquad p=p_k(s).
```
The relation $`F(u,a,y)=s`$ is **exactly biregular**, with left degree
$`M_sp`$ and right degree $`Np`$. The left degree follows by averaging $`a`$;
the right degree is Theorem DEG.

Let $`J_s^G:L^2(X)\to L^2(Y_s)`$ be its probability-normalized incidence
operator. On centered inputs,
```math
 \|J_s^G\|^2\le
 \begin{cases}
 (2/(7\gamma))Q^{-4h}g_h,&s\ne0,\\
 (36/(49\gamma))Q^{-4h}g_h,&s=0.
 \end{cases}
 \tag{6.1}
```
For comparison, the direct separate-rank bound is
```math
 \|J_s^G\|^2\le\gamma^{-1}Q^{-4h}p(1-p).
 \tag{6.2}
```

**Proof, including the restriction cost.**
Restriction from $`W`$ to $`G`$ in the output costs at most
$`\gamma^{-1/2}`$ in normalized $`L^2`$. For fixed $`s`$ and centered $`f`$,
write $`J_sf(u,a)=If(u,a,s)`$ before restriction.
Translation $`a\mapsto a+(1,\ldots,1)`$ takes $`F`$ to $`2F`$.
Thus the three Gram operators for $`s\in H`$ are equal, and those for
$`s\in-H`$ are equal. Since
$`I^*I=(1/7)\sum_sJ_s^*J_s`$, positivity gives
$`\|J_sf\|^2\le(7/3)\|If\|^2`$ for $`s\ne0`$.
For $`s=0`$, $`\sum_sJ_sf=0`$ pointwise and
$`|J_0f|^2\le6\sum_{s\ne0}|J_sf|^2`$, giving
$`\|J_0f\|^2\le6\|If\|^2`$.
Combine with (4.2) and restriction to get (6.1).
For (6.2), Fourier-expand the function $`a\mapsto1_{\{S(a)=s\}}`$.
Parseval gives nonzero-label mass $`p-p^2`$; apply the rank $`4h`$
bound to each label and then restrict. $`\square`$

There is also a two-sided control of trimming. For every nonzero
spatial frequency and every fixed-$`s`$ or full-$`s`$ centered Gram multiplier,
the ratio of its restricted value to its unrestricted value, when nonzero, lies in
```math
 \left[\frac{1-(v-1)Q^{-2h}}{\gamma},\ \frac1\gamma\right].
 \tag{6.3}
```
For $`B_\nu u=\xi\ne0`$ there are $`Q^{2h}`$ solutions.
No solution is in $`R_{[\nu]}`$, and at most one lies in each other
$`R_{[\mu]}`$, since the restriction of $`B_\nu`$ to that radical is
injective. Fourier expansion in $`a`$ expresses each multiplier as a
positive sum of these fiber counts. This proves (6.3), including zero
multipliers. The removal therefore does not manufacture a new spectral
saving; it repairs the degrees at an explicitly controlled cost.

### Theorem VALUE: prescribed-value solvability on arbitrary subsets

Set
```math
 c_s=\begin{cases}2/7,&s\ne0,\\36/49,&s=0,\end{cases}\qquad
 L_{h,s}=3^kQ^{8h}\min\{c_sg_h,\ p_k(s)(1-p_k(s))\}.
 \tag{6.4}
```
For arbitrary $`A\subseteq W`$, $`C\subseteq Y_s`$, with
$`\alpha=|A|/N`$, $`\sigma=|C|/M_s`$,
```math
 |e_s(A,C)-p_k(s)|A||C||
 \le\sqrt{L_{h,s}}\,
      \sqrt{|A|(1-\alpha)|C|(1-\sigma)}.
 \tag{6.5}
```
Hence a solution exists if
```math
 \frac{|A||C|}{(1-\alpha)(1-\sigma)}
       >\frac{L_{h,s}}{p_k(s)^2},
 \tag{6.6}
```
and relative error is at most the square root of the right side of
(6.6) divided by its left side. Incidence-free pairs satisfy the reverse
weak inequality. These odds ratios concern nonempty, nonfull sets;
empty-set endpoints are trivial, and a full $`A`$ or full $`C`$ has the
exact main term by biregularity. For $`s\ne0`$ the collective sufficient cardinality scale is
```math
 \frac{2}{7p_k(s)^2}\,3^kQ^{8h}g_h
       \sim14\,3^kQ^{8h}m_*^{2h}.
 \tag{6.7}
```
The direct rank comparator gives
$`[(1-p_k(s))/p_k(s)]3^kQ^{8h}\sim6\,3^kQ^{8h}`$.
Their threshold ratio is
$`2g_h/[7p_k(s)(1-p_k(s))]\sim(7/3)m_*^{2h}`$.
It is below one for $`h\ge2`$; at $`h=1`$ taking the minimum in (6.4)
retains the stronger rank bound. Finite values follow directly from
(2.3) and (1.4), and for $`h\ge3`$ the inequalities
$`g_h\le g_3<1/12`$, $`p_k(s)\in[(1-\Delta_h)/7,(1+\Delta_h)/7]`$
give the uniform comparison.

**Proof.**
Biregularity permits centering both indicators. Multiply the smaller of
(6.1), (6.2) by $`NM_s`$ to obtain the unnormalized nonconstant
singular-value bound $`L_{h,s}`$. Apply Cauchy--Schwarz.
All factors of $`\gamma`$ cancel in this unnormalized bound.
No product structure of $`C`$ has been imposed. $`\square`$

The same $`A,C`$ contain solutions for all seven prescribed values if
(6.6) holds with the largest of its seven right sides; applying the
seven deterministic estimates incurs no unproved independence assumption.
For coverage of nearly all parameters by a small $`A`$, Theorem COVER
is substantially stronger than what (6.5) alone supplies.

## 7. Attainable behavior: the matched-rank aligned obstruction

Let $`M_h=\mathbb F_{Q^{2h-1}}`$ and choose an injective
$`\mathbb F_3`$-linear map $`i:\mathbb F_3^k\to M_h`$.
On
$`W_{\mathrm{al}}=E\oplus E^k\oplus M_h^2`$, define
```math
 B_\nu^{\mathrm{al}}((x_0,x',v,w),(y_0,y',v',w'))
 =x_0(\nu\cdot y')-y_0(\nu\cdot x')
  +\operatorname{Tr}_{M_h/E}i(\nu)(vw'-wv').
 \tag{7.1}
```
Its dimension over $`E`$ is $`6h`$ and its nonzero scalar rank is $`4h`$,
exactly as for spread. Use the same trace, shifts and $`\mathbb F_7`$
readout. The rank assertion follows because the star block has rank two
and the trace-symplectic block has rank $`4h-2`$.

### Theorem SEP: an incidence-free rectangle that spread forbids

For every $`h\ge3`$, the aligned relation has sets of cardinalities
```math
 |A|=Q^{4h},\qquad |D|=6\,3^k(Q^{4h}-1)
 \tag{7.2}
```
with no incidence. The spread relation has an incidence for **every**
pair of sets of these cardinalities. There is no generic-output,
nonzero-$`u`$, product, or block-centering restriction on the spread sets.

**Proof.**
For aligned, take the common totally isotropic subspace
```math
 T=\{(y_0,y',v,w):y_0=0,\ w=0\},\qquad\dim_E T=4h,
```
and let $`A=T`$,
$`D=\{(u,a,s):u\in T\setminus0,\ s\ne S(a)\}`$.
All bilinear traces vanish on $`T\times T`$, so the rectangle is empty.
Most of its $`u`$ have $`v\ne0`$; for such $`u`$, the row map
$`\beta(u,\cdot)`$ is full rank by injectivity of $`i`$.
Thus emptiness is not a zero-output-degree trick.

For spread, $`\alpha=Q^{-2h}`$ and
$`\beta=(6/7)(1-Q^{-4h})Q^{-2h}`$.
Equation (2.1) gives $`\tau<vQ^{-4h}`$ and
```math
 \frac{\tau}{\beta}
 <\frac{7v}{6Q^{2h}(1-Q^{-4h})}<\frac1{100}.
```
The last inequality already holds at $`h=1`$ and decreases thereafter.
For $`h\ge3`$, $`r_*<1/2`$ gives $`\Delta_h<3/64`$, and
```math
 g_h\le g_3=\frac{340018}{4782969}<\frac1{12}.
```
Using (4.10), the squared main term exceeds the squared error in (4.5)
as soon as
```math
 (1-\Delta_h)^2
 \frac{\alpha(\beta-\tau)^2}{(1-\alpha)\beta(1-\beta)}
       >6g_hQ^{-4h}.
```
Its left side is at least
```math
 (61/64)^2(6/7)(99/100)^3 Q^{-4h}
 >\tfrac12 Q^{-4h}>6g_hQ^{-4h}.
```
This proves strict positivity for all such spread sets. $`\square`$

A very unbalanced obstruction is also explicit. For aligned, take
$`A=\{y_0=0\}`$ and
$`U=\{u_0=0,\ u_v=u_w=0\}\setminus0`$, with the same six-forbidden-symbol
definition of $`D`$. Then
```math
 \alpha=Q^{-1},\qquad
 \beta=(6/7)(Q^k-1)/Q^{6h},\qquad
 \alpha\beta=(6/7)(1-Q^{-k})Q^{-4h}.
```
For spread and arbitrary sets of these sizes with $`D`$ excluding $`u=0`$,
(4.8) forces an incidence for $`h\ge5`$. For a rational uniform check,
$`\eta_5<3/5`$, $`g_5<1/60`$, so
$`6g_h/(1-\eta_h)^2<5/8<(6/7)(1-Q^{-k})`$ for all $`h\ge5`$.
These bounds follow by
$`\sqrt{a_*}<1/2`$, $`\sqrt{b_*}<3/8`$, $`\sqrt{m_*}<81/100`$ and
direct rational powers. This second comparison states its nonzero-$`u`$
condition explicitly.

### Theorem CSEP: actual coverage separation

For every $`h\ge8`$ there is already a separation at **37 inputs**.
In the aligned family choose any 37 distinct points on one star-vector
$`E`$-axis, with all other coordinates zero. For any seed, only one trace
coordinate can vary on this axis, so $`F`$ takes at most three values.
No seed covers $`\mathbb F_7`$. In contrast every 37-element spread subset
has a covering seed by Theorem COVER. The pencils still have identical
labeled scalar ranks. This is a fixed-cardinality existence separation.

For aligned, put $`A_0=\{(0,y',0,0):y'\in E^k\}`$.
Whenever $`u_0=0`$, $`F(u,a,\cdot)`$ is constant on $`A_0`$.
This occurs for exactly $`1/Q`$ of all seeds. When $`u_0\ne0`$,
$`\beta(u,A_0)=\mathbb F_3^k`$, so all seven values occur.
Thus the fraction of noncovering seeds for $`A_0`$ is **exactly $`1/Q`$**.

More generally any subset of $`A_0`$ retains the lower bound $`1/Q`$.
Choose any cardinalities $`n_h\to\infty`$ with $`n_h\le Q^k`$.
Aligned has subsets of these sizes with failure fraction at least $`1/Q`$;
spread has failure fraction tending to zero for every subset of the same
size, by (3.13). This is an actual distributional separation, not just a
comparison of operator estimates.

One can keep the aligned fraction exactly $`1/Q`$ while making the source
grow slowly: use $`E^r`$ in $`r`$ star coordinates, $`3\le r\le k`$.
For $`u_0\ne0`$ the varying part has law $`p_r`$, translated by the fixed
coordinates, and hence full support. Taking $`r=r_h\to\infty`$ slowly
keeps this example far below the source sizes where the spectral estimate
alone gives useful coverage.

For aligned a difference in a single star-vector coordinate also has
$`K(d)=a_*`$, giving pair collision exactly $`1/3`$.
Spread's maximum distinct-pair collision is (3.7), tending to $`1/7`$.
The differing radical intersection geometry is visible at the pair level.

## 8. Sharpness, trivial products, and complexity

The full centered norm (4.2) is exact, and an input indicator can attain its
input-side norm: if $`\xi`$ is a maximizing frequency, then $`-\xi`$ also
maximizes it, and
$1_{\{\operatorname{Tr}(\xi\cdot y)=0\}}-1/3
=(\chi_\xi+\chi_{-\xi})/3$.
This does not show that an output indicator attains Cauchy--Schwarz.
Theorem COL proves an additional exact extremum for nonnegative sources;
Theorems SEP and CSEP prove attainable count/distribution separations.
We have not proved the optimal spread empty-rectangle size.

At $`h=1,2`$ some nonzero output rows are empty; at every $`h`$ the zero
slice contains empty rows. No finite theorem can assert existence for
every $`D`$ with positive size. The exact main term (4.5) and the finite
error conditions retain these obstructions.

Leaving all shift coordinates unrestricted can trivialize an apparent
application. For any $`U'\subseteq W`$ and $`S'\subseteq\mathbb F_7`$,
```math
 e(A,U'\times\mathbb F_3^k\times S')
   =|A||U'|3^k\sum_{s\in S'}p_k(s)
```
without any spread geometry. Our counting theorems permit arbitrary
correlations among the output coordinates, and the fixed-value theorem
permits arbitrary subsets of $`(u,a)`$, so they are not this identity.

One can specify the fields uniformly by
$`E=\mathbb F_3[\lambda]/(1+\lambda+\cdots+\lambda^6)`$, and a
chosen irreducible degree-$`h`$ polynomial over $`E`$ for $`L`$.
The injection $`j`$ is a full-column-rank $`6h`$ by $`k`$ matrix over
$`\mathbb F_3`$. Given these representations, a field element has $`6h`$
ternary coordinates; $`y`$ and $`u`$ each have $`36h`$ ternary coordinates,
and a seed $`(u,a)`$ has $`38h+1`$. The output has seven symbols.

After precomputing traces and $`z(j(e_i))`$, schoolbook field arithmetic
evaluates (1.2) in $`O(h^3)`$ operations over the fixed field $`E`$.
Membership of $`G`$ can be tested by rank of the explicitly formed
$`k`$ by $`36h`$ trace matrix; direct formation and elimination take a
polynomial number of operations (a conservative $`O(h^4)`$ bound suffices).
These are evaluation bounds with a field presentation supplied.
Lexicographically searching for the first irreducible polynomial is a uniform
construction, but no polynomial preprocessing bound is claimed for that search.
No fast algorithm for finding a solution inside arbitrarily presented subsets
is implied by an existence proof.

The fixed-value relations are dense biregular graphs, with the exact degrees
and singular bounds in Section 6. We make no sparse-expander claim.
Section 9 gives a smaller-seed classical hash control; the present family
is valuable for retaining this particular trace–exponential equation.


## 9. Comparison with primary literature

The table records theorem-level applicability, not a comparison of titles.
Precise versions and source locators are in [REFERENCES](../INCIDENCE_REFERENCES.md).

| Result here | Applicable established result | Hypotheses and transfer | Conclusion of the comparison |
|---|---|---|---|
| COL, SMALL, COVER | Barak–Dodis–Krawczyk–Pereira–Pietrzak–Standaert–Yu, *Leftover Hash Lemma, Revisited*, Lemma 3.1, pp.7–8 | Arbitrary finite output alphabet and side information; take the side information to be the uniform seed, output alphabet of size seven, and test function $`1_D`$ | Gives exactly the collision-to-count variance method, including $`\sqrt{\beta(1-\beta)}`$. The new input is the exact family collision profile, its extremizers, and their constrained-equation consequences |
| SPEC and MIX | Weighted projection Gram/frame operator; Casazza–Kutyniok, Definition 3.15 and Proposition 3.16 | Fourier Gram is a positive weighted sum of commuting image projections; no assumption that every form is nondegenerate | Computes the norm once joint images are known. The application does not improve this abstract method |
| Degree and weight identities | MacWilliams, Lemma 2.7, p.88 | Character orthogonality on a finite linear code, with complete symbol weights | Supplies established complete-weight-enumerator duality; no new transform |
| Image-overlap bound | Sheekey, Section 2, root-count paragraph before Theorem 2 and Remark 2 | A nonzero $`\mathbb F_3`$-linearized polynomial of degree nine has at most nine roots, restricted to $`j(\mathbb F_3^k)`$ | The Moore/Gabidulin ingredient is established. Even maximum atom weight plus this root bound already gives the collective exponent |
| Scalar bilinear counts | Vinh, arXiv:0903.1156v1, Lemma 2.1 and Theorem 2.2 | Nondegenerate bilinear form on $`\mathbb F_q^d`$, nonzero target; error $`q^{(d-1)/2}\sqrt{|U||V|}`$ | Does not directly apply to the composite mixed-characteristic readout. The scalar rank-quotient version gives the separate-rank estimate; an explicit $`\mathbb F_7`$ feature encoding is too large |
| Full affine-flat counts | Phuong–Pham–Vinh, Theorems 1.5–1.6; Lemma 2.1 for biregular mixing | Points and affine flats in one field; incidence of our rows requires unions of many flats and multiplicity weights | The exact ambient point-flat Gram below gives a vacuous sparse product-size criterion in these parameters |
| Compound exponentials | Friedlander–Shparlinski, Theorem, p.1618 | Scalar sums $`e_p(c\eta^{xy})`$ on exponent subsets, varying scalar parameters | At $`p=7`$ and exponent order three the scalar parameters are fixed; it gives no direct $`h`$-decay for arbitrary common-input subsets |
| Trace-form construction | Gow–Quinlan, Section 2 | Alternating forms made from Galois traces; trace duality controls radicals | Established construction technique, not a source for the seven-symbol readout theorem |

### 9.1 The generalized leftover hash lemma applies literally

[LHL, Lemma 3.1](../INCIDENCE_REFERENCES.md#incidence-lhl) permits any finite
alphabet $`\mathcal Y`$, not just bit strings. Its inequality is
```math
 |\mathbb Ef(Y,Z)-\mathbb Ef(U_{\mathcal Y},Z)|
 \le \sigma_c[f(U_{\mathcal Y},Z)]
           \sqrt{|\mathcal Y|\operatorname{Col}(Y\mid Z)-1}.
```
Take $`\mathcal Y=\mathbb F_7`$, let $`Z=(u,a)`$ be the seed, and let
$`Y=F(u,a,Y_A)`$ for uniform $`Y_A\in A`$ independent of the seed.
With $`f=1_D`$ and $`c=\beta`$ the variance factor is
$`\sqrt{\beta(1-\beta)}`$. Theorem COL gives
$`7\operatorname{Col}(Y\mid Z)-1\le6\Theta_h(n)`$.
This is exactly (3.8) after converting probability to counts.
No alphabet encoding or restriction loss is needed.

Thus the sparse theorem survives comparison as a sharp almost-universality
calculation for this specified constrained family and an application of a known
lemma. It is not a stronger general leftover hash lemma. The $`p_k`$-centered
identity additionally records the exact nonuniform marginal rather than
absorbing it in distance from uniform.

For comparison, ordinary affine universal hashing does better if the equation
is discarded. Encode $`W`$ injectively in $`\mathbb F_7^d`$,
$`d=\lceil\log_7N\rceil`$, and take
$`H_{r,b}(y)=r\cdot\operatorname{enc}(y)+b`$ with uniform $`(r,b)`$.
Distinct inputs have independent uniform outputs, so
```math
 \mathbb E_{r,b}\sum_s
  \bigl(\Pr_{y\in A}[H_{r,b}(y)=s]-1/7\bigr)^2
       =\frac6{7n}.
```
The same Cauchy--Schwarz proof gives joint seeded total variation
(equivalently, seed-averaged output distance) at most
$`\tfrac12\sqrt{6/n}`$ and (3.8) with $`\Theta=1/n`$.
Its seed length is
$`(d+1)\log_2 7<\log_2N+2\log_2 7`$,
whereas the trace–exponential seed uses $`\log_2N+k\log_2 3`$ bits.
This elementary pair-count proof, with the historical
[Carter–Wegman reference](../INCIDENCE_REFERENCES.md#incidence-universal-hashing),
prevents a general extractor-superiority claim. What is retained here is
the original trace–exponential arithmetic and its matched-rank comparison.

### 9.2 What the full point-flat spectrum actually gives

Identify $`W`$ with $`\mathbb F_3^d`$, $`d=36h`$. For generic $`u`$ each row
is a disjoint union of codimension-$`k`$ flats; put $`b=d-k=34h-1`$.
Let $`C`$ be the full incidence matrix between points and all affine
$`b`$-flats. Counting flats through one point and two distinct points gives
```math
 CC^{\mathsf T}=(R-c)I+cJ,\quad
 R={d\brack b}_3,\quad c={d-1\brack b-1}_3.
```
Hence the exact squared nonconstant singular value is
```math
 \Lambda^2=3^b{d-1\brack b}_3\ge3^{bk}.
 \tag{9.1}
```
Here Gaussian binomial coefficients count linear subspaces. The inequality
follows directly from their product formula. This is the ordinary exact
Gram calculation, used to avoid importing a $`q\to\infty`$ error term
into the present fixed-$`q`$, growing-dimension problem.

For selected generic rows $`D`$, let $`w(H)`$ count the multiplicity of each
flat among their decompositions. Then
```math
 n_D:=\sum_Hw(H)=3^k e(X,D)/N,\qquad
 e(A,D)=\sum_Hw(H)|A\cap H|.
```
The generic point-flat estimate is
```math
 |e(A,D)-\alpha e(X,D)|
       \le\Lambda\sqrt{|A|(1-\alpha)}\,\|w\|_2.
 \tag{9.2}
```
If maximum multiplicity is $`R_{\mathrm{mult}}`$, one may bound
$`\|w\|_2^2\le R_{\mathrm{mult}} n_D`$; treating repeats as distinct would be
incorrect. Even optimistically taking multiplicity one and typical degrees,
the usual product-size sufficient criterion has scale at least
```math
 |A||D|\gg 7\,3^{k(b+1)}
          =7\,3^{34h(2h+1)}.
```
This exceeds $`NM=7\,3^{74h+1}`$ for every $`h\ge1`$.
Therefore this ambient bound supplies no comparable sparse range.
We do not claim it is useless at trivial endpoints such as $`A=X`$,
or that every use of flat geometry is exhausted: retaining this family's
normal-space geometry is precisely what the collective Gram does.

### 9.3 An exact dot-product encoding and its cost

Let $`\mathcal L`$ be the $`\mathbb F_3`$-dual of $`W`$, of cardinality $`N`$.
Over $`\mathbb F_7`$ set $`v(y)_\ell=2^{\ell(y)}`$, and let
$`w(u,a)_\ell`$ be the sum of $`2^{a_i}`$ over those $`i`$ with
$`-\beta_i(u,\cdot)=\ell`$. Then $`F(u,a,y)=v(y)\cdot w(u,a)`$.
Homogenization gives the exact equation
```math
 (v(y),1)\cdot(w(u,a),1-s)=1
```
in dimension $`N+1`$ over $`\mathbb F_7`$.
Vinh's nonzero-target bilinear estimate now has coefficient $`7^{N/2}`$,
far too large. Repeated parameter features require multiplicity weights.
Restricting the feature set to $`\bigcup_i\operatorname{im}B_i`$ still
leaves at least $`Q^{4h}`$ features, with the same qualitative failure.
This excludes these natural encodings as competitive transfers, not
every conceivable encoding.

The nearby double-exponential theorem bounds
```math
 \left|\sum_{x\in U,y\in V}e_p(c\eta^{xy})\right|
 \ll_\epsilon |U|^{1/2}|V|^{5/6}t^{1/2}p^{1/8+\epsilon}
```
for $`\eta`$ of order $`t`$. In our equation $`p=7,t=3`$ are fixed;
the arbitrary restrictions lie in a growing vector space and retain shifts
and many forms on the same input. A tensor/product assumption cannot be
silently added to apply that scalar theorem.

### 9.4 Familiar spectra, and the actual novelty boundary

The full relation has nonconstant output degrees and zero-degree outputs.
That invariant rules out a permutation equivalence with the full standard
biregular point-hyperplane graph. Its Gram is nevertheless a familiar
translation-invariant weighted sum of radical indicators. We have not
classified all graphs isomorphic to the regularized slices or excluded every
previously named construction.

The new collision result exploits a particularly strong geometric property:
the nonzero radical sets are disjoint. The earlier norm exploits a dual,
different property: a nonzero spatial frequency lies in images from a
parameter space of dimension at most two. Both are concrete evaluations
inside established Fourier/coding theory. The intrinsic Bol classification
is not used in either proof.

The defensible contribution is therefore a self-contained arithmetic family
with sharp collision statistics, explicit degree-aware counting regimes,
small-source simultaneous seven-value solvability, and actual same-rank
obstructions. The inspected primary sources do not state this particular
package for (1.1)–(1.2). That bounded finding is not a historical priority
certification.

## 10. Remaining questions and verification scope

The initial bottleneck was degree variation: ignoring it makes even the main
term false. Theorem DEG resolves it. Removing the explicit radical region
repairs it exactly at a controlled spectral cost (Section 6).
A second bottleneck was signed $`L^2`$ control applied to a very small
nonnegative source; Theorem COL improves this by counting differences
directly and yields the new regime (3.12).

The next precise questions are:

* Determine the least $`n`$ for which every $`n`$-element subset of the spread
  input admits a seven-value-covering seed for all sufficiently large $`h`$.
  The present theorem gives $`n\le37`$, while $`n\ge7`$ is necessary.
  Improving 37 requires information beyond the available second moments
  if the proof is to be uniform over all almost-universal families.
* Determine optimal incidence-free cardinality products for this particular
  spread relation. Exact norm and variance equality do not settle the
  two-indicator extremum.
* Compute the exact fixed-symbol spectrum after regularization; (6.1) is
  a proved upper bound with a fully paid restriction, not its exact value.
* Extend the exact collision/degree analysis to other readouts or alphabets.
  A new readout needs its own marginal, weights and extremizers; the current
  formulas do not transfer unchanged.

The first methodological limitation has a finite sharp control.
On a 36-point source, choose a missing symbol uniformly among seven and then
choose a uniform balanced assignment to the other six symbols, six source
points per symbol. Each source point is uniform on $`\mathbb F_7`$.
Two distinct points collide with probability $`5/35=1/7`$; output permutation
symmetry then makes their joint output exactly uniform on $`\mathbb F_7^2`$.
Nevertheless every seed misses a symbol. Thus even exact pairwise
independence cannot guarantee coverage of seven symbols from 36 inputs.
This does not exhibit a 36-point obstruction in our spread family.

The reproducible programs are
[the rational/combinatorial checker](../code/verify_bol_incidence.py) and
[the independent actual-field checker](../code/verify_bol_incidence_independent.py).
They check integer degree recurrences, all small coefficient-type classes,
rational thresholds and coverage constants, full-field normalizations using
linear-fiber compression, actual $`\mathbb F_{729}`$ radical directions, and
variance equality cases. The full ambient set of size $`729^{6h}`$ is not
enumerated. The proofs establish the uniform statements; finite checks are
supplementary evidence. Commands, source hashes, actual review attribution and
repository-integrity limitations are in the linked code/evidence records.
