# Joint digit switches in two coprime bases

**Mira Cult**

A single irrational number can have very long runs of identical digits in one base. This note shows that its expansions in two coprime bases cannot both be sparse in switches across too many scales.

## Statement

Let $`d_{r,n}`$ be the $`n`$th fractional digit of an irrational real number $`x`$ in base $`r`$. To count only pairs entirely within the first $`N`$ fractional digits, write

```math
S_r(N;x)=\#\{1\le n\lt N:d_{r,n}\ne d_{r,n+1}\}.
```

**Claim 0001 (joint digit switches).** For every fixed pair of coprime integers $`b,c\ge2`$, there is an effective constant $`c_{b,c}\gt 0`$ such that for every irrational real $`x`$,

```math
S_b(N;x)+S_c(N;x)\ge c_{b,c}(\log N)\log\log N
\qquad\text{for every }N\ge N_0(x,b,c).
```

All logarithms are natural. The cutoff is effective given a positive lower bound for the distance from $`(b-1)(c-1)\{x\}`$ to the nearest integer, where $`\{x\}`$ is the fractional part of $`x`$. In particular the result applies in bases 2 and 3 to the unchanged numbers $`e`$ and $`\log 2`$.

[Bugeaud, Theorem 2.3](https://ems.press/content/serial-article-files/38399) proves a joint lower bound of order $`\log N`$. The argument here adds a factor of $`\log\log N`$. It does not distinguish which of the two bases supplies the switches, give a positive limiting frequency, or imply normality.

## Proof outline

Replace a string of digits by its signed adjacent differences, without changing the number whose digits are counted. If both bases have few switches at a given scale, group those switches into short clusters. The two truncated expansions give a rational vector whose coordinates satisfy unusually strong real and $`p`$-adic inequalities. The quantitative Subspace Theorem places such vectors in exponentially many subspaces. The order of the clusters keeps the number of inequality systems exponential, and a valuation argument bounds how many well-separated scales can land in a single subspace.

For the proof use $`D_r(N;x)=S_r(N+1;x)`$, which counts switch positions through index $`N`$. Also put

```math
J_r(X;x)=\#\{n\ge1:X/4\lt n\log r\le X,\ d_{r,n}\ne d_{r,n+1}\}.
```

The quantitative step shows that for any positive integer $`K`$, a sequence of scales with successive ratio at least $`4`$ contains at most $`e^{C_{b,c}K}`$ scales with $`J_b(X;x)+J_c(X;x)\le K`$ above $`X_0(x,b,c)+C_{b,c}(K+1)\log(2K+2)`$. Here the same constant can be enlarged to accommodate both bounds. This counts sparse scales; it does not locate the last such scale.

## 1. A sparse shell produces actual grouped switch coordinates

Set $`M=(b-1)(c-1)`$, $`y=\{x\}`$, and
```math
 F_r(U)=\frac M{r-1}
       \left(d_{r,1}+\sum_{n\log r\le U}(d_{r,n+1}-d_{r,n})r^{-n}\right),
 \qquad r\in\{b,c\}.
```
By shifting the digit series, $`\sum_{n\ge1}d_{r,n+1}r^{-n}=ry-d_{r,1}`$, so $`F_r(U)=My+O_{b,c}(e^{-U})`$ and $`F_r(U)\in\mathbb Z[1/r]`$, with denominator dividing $`r^{\lfloor U/\log r\rfloor}`$. This uses signed differences of the true digits, not the digits of $`My`$.

Fix $`K\ge1`$, and let $`X`$ be a shell with $`J_b(X;x)+J_c(X;x)\le K`$. For each radix $`r`$, the $`K`$ or fewer switches in $`[X/4,X/3]`$ leave an open gap of length at least $`X/[12(K+1)]`$, by including both interval endpoints in the gap count. Choose $`U_r`$ at the midpoint of such a gap. Every retained switch with $`U_r\lt n\log r\le X`$ has log-place at least $`U_r+X/[24(K+1)]`$. An endpoint switch excluded from the count at $`X/4`$ does not affect the claimed open gap.

Within each radix group successive retained switches if their log-place gap is less than $`hX`$, where $`h=1/[100(K+1)]`$. A group of log-places between $`s_i`$ and $`t_i`$, inclusive, is a coordinate $`g_i=A_i r^{-m_i}`$, $`m_i=t_i/\log r`$, where $`A_i`$ is an integer, and the negative sign is included for the radix $`c`$. List groups first from $`b`$, then from $`c`$, each in chronological order. There are $`q\le K`$ groups. Within either list, last log-places of successive groups differ by at least $`hX`$. Their total width satisfies
```math
                        \sum_{i=1}^{q}(t_i-s_i)\le KhX.
                                                               \tag{2}
```
Let $`C=F_b(U_b)-F_c(U_c)`$ and $`E=F_b(X)-F_c(X)=C+\sum_i g_i`$. Once $`X\ge X_0(x,b,c)`$, both $`C`$ and $`E`$ are nonzero: all four $`F_r`$'s are near the nonintegral $`My`$ and hence nonintegral, while $`\mathbb Z[1/b]\cap\mathbb Z[1/c]=\mathbb Z`$. Moreover
```math
                |C|\ge e^{-2X/3},\qquad |E|\ll_{b,c}e^{-X}.
                                                               \tag{3}
```
The first inequality follows from the explicit denominator bound. It makes $`q=0`$ impossible for all large $`X`$.

Write $`\mathbf v=(C,g_1,\ldots,g_q)`$, $`d=q+1\ge2`$, and $`S=\{\infty\}\cup\{\text{primes dividing }bc\}`$, with $`s=|S|`$. Use local sup norms $`\|\mathbf v\|_v`$ and projective height $`H(\mathbf v)=\prod_v\|\mathbf v\|_v`$. Clearing by $`b^{\lfloor X/\log b\rfloor}c^{\lfloor X/\log c\rfloor}`$ and then dividing by the gcd gives a primitive integral representative $`\mathbf w`$, with $`H(\mathbf v)=\|\mathbf w\|_\infty\ll_{b,c}e^{2X}`$. Conversely $`E/C=(\sum_{i=0}^{d-1} w_i)/w_0`$ is a nonzero rational, with denominator at most $`\|\mathbf w\|_\infty`$. By (3) it has absolute value $`O_{b,c}(e^{-X/3})`$. This gives the uniform **lower** height bound
```math
             e^{X/3}/O_{b,c}(1)\le H(\mathbf v)
                               \le O_{b,c}(1)e^{2X}.         \tag{4}
```
In particular $`X/4\le L:=\log H(\mathbf v)\le3X`$ at large $`X`$.

## 2. Only exponentially many fixed systems of local weights

At each finite $`p\in S`$, take coordinate forms $`L_{ip}=Z_i`$ for $`0\le i\lt d`$. At $`\infty`$ change only $`L_{0\infty}`$ to $`\sum_{i=0}^{d-1}Z_i`$. All systems have determinant one; their at most $`d+1`$ distinct rational forms have inhomogeneous height one. By (3), also $`|L_{0\infty}(\mathbf v)|=|E|\lt |C|`$ once $`X`$ is large. Consequently all normalized local absolute values
```math
                        |L_{iv}(\mathbf v)|_v/\|\mathbf v\|_v
```
are at most one.

Let $`A\ge2`$ be a fixed constant depending on $`b,c`$, large enough for both $`|E|\le A e^{-X}`$ and $`|g_i|\le A e^{-s_i}`$ (the latter follows by summing the absolute geometric tail of group terms). We choose the following *upper bounds* $`G_{iv}`$ for $`\log |L_{iv}(\mathbf v)|_v`$; no lower bound for a group coefficient at the opposite prime is needed. If $`p\mid r`$, write $`\lambda_{p,r}=v_p(r)\log p/\log r`$; then $`\sum_{p\mid r}\lambda_{p,r}=1`$.
```math
\begin{array}{c|c|c}
 & i=0 & i\ge1\text{ in radix }r\\ \hline
 v=\infty &\log A-X &\log A-s_i\\
 v=p\mid r'& \lambda_{p,r'} U_{r'}&
        \lambda_{p,r}t_i\quad(p\mid r),\qquad 0\quad(p\nmid r).
\end{array}
```
For the finite bounds use only integral numerators and the displayed unreduced denominators. From $`U_b+U_c\le2X/3`$ and (2),
```math
     \sum_{v\in S}\sum_i G_{iv}
         \le -X+2X/3+KhX+(K+1)\log A \le -X/4
                                                               \tag{5}
```
for $`X`$ larger than a fixed multiple of $`K+1`$. Set $`m_v=\log\|\mathbf v\|_v`$ and
```math
          u_{iv}=\min\{0,(G_{iv}-m_v)/L\}.
```
These numbers bound $`\log(|L_{iv}(\mathbf v)|_v/\|\mathbf v\|_v)/L`$ from above. They all lie in a fixed interval $`[-10,0]`$: at a finite place $`m_p\le X`$, $`G_{ip}\ge0`$; at $`\infty`$, $`m_\infty=O_{b,c}(1)`$, $`G_{i\infty}\ge-X`$; use $`L\ge X/4`$. Since $`\mathbf v\in\mathbb Z[1/(bc)]^d`$, $`\sum_{v\in S}m_v\ge L`$. Thus (5) and $`L\le3X`$ give
```math
                           \sum_{v,i}u_{iv}\le-d-1/12.        \tag{6}
```
Crucially, for each place the list of $`u_{iv}`$ on each radix's groups is monotone: nonincreasing at $`\infty`$, nondecreasing at the radix's own primes, constant at the other radix's primes. The singleton $`i=0`$ has no ordering constraint.

Round each $`u_{iv}`$ upwards to a multiple of $`\Delta=1/(128sd)`$, preserving these orders (take the constant lists as nondecreasing). This adds at most $`1/128`$ to the sum in (6). Raise grid entries further so their sum is exactly $`-d-1/32`$, preserving the weak orders and keeping all entries $`\le0`$. This is possible one upward grid step at a time: in a nondecreasing list take the last strictly negative entry, in a nonincreasing list the first; if one list is all zero move to another list or an available singleton. Each step leaves all orders intact. The desired sum is a grid multiple between the current sum and zero. Denote the resulting weights by $`u'_{iv}`$. We have
```math
              |L_{iv}(\mathbf v)|_v/\|\mathbf v\|_v
                                       \le H(\mathbf v)^{u'_{iv}}.  \tag{7}
```
For a fixed $`d`$ there are at most $`d`$ radix splits of the group list. For each split and place, each monotone list is of length at most $`d`$ in a grid of $`1280sd+1`$ values; its number of choices is at most $`\binom{1280sd+d+1}{d}\le 2^{(1280s+2)d}`$. The $`s`$ singleton entries contribute only $`(1280sd+1)^s`$. Thus the number of possible arrays $`u'_{iv}`$ is $`\exp(O_{b,c}(d))`$, not $`\exp(O_{b,c}(d\log d))`$. This savings uses ordered physical switches, not a probabilistic model for the digits.

Apply [Evertse–Ferretti, *A further improvement of the Quantitative Subspace Theorem*, Annals of Mathematics 177 (2013), Theorem 3.1, equations (3.1)–(3.10)](https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p04-p.pdf) to (7), with ground field $`\mathbb Q`$ (so no conjugate factor), $`R=d+1`$, $`D=H^*=1`$, $`A_v=1`$ and $`\varepsilon=1/32`$. The weights sum to $`-d-\varepsilon`$ and are nonpositive. The required height is $`H\gt d^{32d}`$, which follows from (4) for $`X\ge X_0(x,b,c)+C_{b,c}(K+1)\log(2K+2)`$. Each fixed array gives at most
```math
 10^9\,2^{2d} d^{14}32^3\log(96(d+1))\log(32\log(3(d+1)))
                          =\exp(O(d))
```
proper rational linear subspaces. Taking all arrays together, we conclude that, at dimension $`d`$, the sparse-shell vectors satisfying the threshold are contained in $`\exp(O_{b,c}(d))`$ proper rational linear subspaces.

## 3. A proper subspace captures few separated shells

Here the exact signed group numerator, rather than just an upper bound for it, matters. Let a nonzero integer linear relation with coefficient vector $`\mathbf a`$ be proposed for $`\mathbf v`$. If any group coefficient is nonzero, take the latest active group of one radix $`r`$. Write its numerator as
```math
          A_i=\pm \frac M{r-1}\,(a_{\rm last}+rB),
          \qquad 0\lt |a_{\rm last}|\lt r,\quad B\in\mathbb Z.
```
There is a prime $`p\mid r`$ with $`v_p(a_{\rm last})\lt v_p(r)`$, since $`r\nmid a_{\rm last}`$. For this prime $`v_p(A_i)=v_p(M/(r-1))+v_p(a_{\rm last})=O_{b,c}(1)`$ exactly. With $`V_p(z)=v_p(z)\log p`$, the selected term in the relation has $`V_p`$ at most
```math
             -\lambda_{p,r}t_i+\log\|\mathbf a\|_\infty+O_{b,c}(1).
```
An earlier active group in the same radix has $`V_p\ge-\lambda_{p,r}t_{i'}`$, with $`t_i-t_{i'}\ge hX`$. The old coordinate term, when present, has $`V_p\ge-\lambda_{p,r}U_r`$, and $`t_i-U_r\ge X/[24(K+1)]`$. Opposite radix contributions are $`p`$-integral by coprimeness. It follows that no nonzero relation can hold if
```math
           \log\|\mathbf a\|_\infty+C'_{b,c}
             \lt  \lambda_* hX,\qquad
      \lambda_*=\min_{r\in\{b,c\},\,p\mid r}\lambda_{p,r}\gt 0:   \tag{8}
```
the selected term would have uniquely smallest $`p`$-valuation. If the relation has only the old coordinate coefficient active, $`C\ne0`$ rules it out at once.

Suppose now $`X_1\lt X_2\lt \cdots`$ are sparse shells of the same dimension $`d`$ with successive ratio at least $`R_K=C''_{b,c}(K+1)^2`$. If fewer than $`d`$ preceding rows have been taken, their integral representatives $`\mathbf w`$ have some common nonzero integral annihilator with
```math
       \log\|\mathbf a\|_\infty\le 4(K+1) X_{\rm prev}.
```
Indeed take a basis of $`m\lt d`$ previous rows, use $`m`$ independent columns and one other column, and take the vector of $`m\times m`$ signed minors on these $`m+1`$ columns (zero elsewhere). By (4) the minors are at most $`m!(O_{b,c}(1)e^{2X_{\rm prev}})^m`$; the stated bound holds by the existing threshold on $`X_{\rm prev}`$, enlarging the base-dependent constant there if needed. Make $`C''_{b,c}`$ large enough that (8) holds at the next $`X`$. This annihilator cannot also vanish on the next row, so the next row is independent of all preceding ones. A proper subspace of the $`d`$-dimensional ambient space therefore contains at most $`d-1`$ rows of any such sequence of shells.

For any sequence of ratio at least $`4`$, split into the index residue classes modulo $`\lceil\log R_K/\log 4\rceil`$, giving ratio at least $`R_K`$ per class. Count the sparse shells in each dimension $`2\le d\le K+1`$ by the number of subspaces from §2 times $`d-1`$. The number of classes is $`O_{b,c}(\log(2K))`$, so the total number of sparse shells past the stated threshold is at most $`\exp(C_{b,c}K)`$ after increasing the effective constant.

## 4. All-prefix inversion

For a large prefix length $`N`$, take the disjoint log-place windows $`(X_j/4,X_j]`$, where $`X_j=4^j`$, $`j\ge1`$, and $`X_j\le N\min(\log b,\log c)`$. At most $`O_{b,c}(\log(2K)+\log(2+X_0(x,b,c)))`$ initial windows fail the threshold in §2. Choose $`K=\lfloor(\log\log N)/(2C_{b,c})\rfloor`$. Then $`\exp(C_{b,c}K)\le\sqrt{\log N}`$, so all but $`o(\log N)`$ of the $`(\log N)/\log 4+O_{b,c}(1)`$ selected windows contain more than $`K`$ changes in the two strings together. Every change is an actual adjacent unequal pair at an index $`\le N`$, counted at most once within each radix. Summation gives the stated order of growth for $`D_b(N;x)+D_c(N;x)`$. Applying this with $`N-1`$ gives the result for the first $`N`$ digits, after reducing the positive constant if necessary. The only dependence on $`x`$ is the initial cutoff described above.

## References and verification

- Yann Bugeaud, [*On the expansions of a real number to several integer bases*](https://ems.press/content/serial-article-files/38399), Revista Matemática Iberoamericana 28 (2012), 931–946, Theorem 2.3.
- Jan-Hendrik Evertse and Roberto G. Ferretti, [*A further improvement of the Quantitative Subspace Theorem*](https://annals.math.princeton.edu/wp-content/uploads/annals-v177-n2-p04-p.pdf), Annals of Mathematics 177 (2013), 513–590, Theorem 3.1.

This is a conventional argument using the cited quantitative theorem, with a scoped independent model review of the proof. It is not a formal verification and makes no claim of external referee acceptance or priority. OpenAI model assistance contributed to the research and preparation of this writeup under Mira's guidance.
