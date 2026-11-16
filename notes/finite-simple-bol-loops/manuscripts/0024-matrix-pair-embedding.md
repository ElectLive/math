# 0024. Matrix-pair similarity inside simple odd Bol loops

**Mira Cult**

## The question and the result

A classification of finite simple Bol loops need not resemble a short list of
isolated examples and one-parameter families. This note explains a precise
reason: an existing odd-order construction can encode an arbitrary ordered
pair of matrices, retaining exactly its simultaneous-similarity class.

The linear-algebra reduction below is self-contained. Its translation into
loops is **conditional on the alternating-form construction and its exact
loop-isomorphism criterion**, stated explicitly in the next section. That
construction is claim 0025, not a consequence proved anew here. This distinction
matters: a congruence theorem for forms alone does not prove a loop-isomorphism
theorem.

**Theorem (0024, with the stated loop-construction input).** Fix odd primes
$`p,q`$ with $`p\mid q-1`$, and put $`r=\mathrm{ord}_q(p)`$. For every
$`n\geq1`$ and ordered pair $`(A,B)\in M_n(\mathbb F_p)^2`$, there is an
explicit construction of a finite simple proper left Bol G-loop $`L(A,B)`$
of order

```math
|L(A,B)|=p^{r(44n+22)+5}q^{11}.
```

For two pairs of the same size,

```math
L(A,B)\cong L(A',B')
\quad\Longleftrightarrow\quad
\exists S\in\mathrm{GL}_n(\mathbb F_p):
\quad A'=SAS^{-1},\quad B'=SBS^{-1}.
```

Here *proper* means non-Moufang, and a G-loop is a loop isomorphic to each of
its loop isotopes. The compact output consists of five alternating matrices
of dimension $`44n+22`$. For fixed primes, their description has size polynomial
in $`n`$; the exponentially larger multiplication table is not the output of
that polynomial-size construction.

## The loop-construction input

Set $`E=\mathbb F_{p^r}`$ and fix elements of orders $`q`$ in $`E^\times`$
and $`p`$ in $`\mathbb F_q^\times`$. The
[alternating-form construction (0025)](../packet/manuscripts/odd-alternating-form-family.md)
asserts the following interface.

Given $`k`$ alternating $`m\times m`$ matrices over $`E`$, independent over
$`\mathbb F_p`$ and having zero common radical, it constructs a simple proper
odd left Bol G-loop of order

```math
p^{rm+k}q^{2k+1}.
```

For fixed parameters and the fixed choices of elements above, two inputs
$`(C_i)`$ and $`(C'_i)`$ yield isomorphic loops exactly when there are
$`\pi\in S_k`$, $`\theta\in\mathrm{Gal}(E/\mathbb F_p)`$, and
$`L\in\mathrm{GL}_m(E)`$ such that

```math
L^tC'_{\pi(i)}L=\theta(C_i)\qquad(1\leq i\leq k).
```

The linked construction uses class-two groups, trace-valued alternating
maps and a symmetric factorization. Its proofs of simplicity, properness
and the strict isomorphism criterion have their own stated dependencies.
We require the entire interface, including the *only if* direction; merely
knowing that congruent inputs give isomorphic loops would not suffice.

We now build five forms over the prime field. Three devices remove the extra
freedoms in this interface: an intrinsic quotient recovers the ordered pair,
different ranks prevent permutations, and descent removes extension-field
similarities.

## 1. Encoding the ordered pair in four operators

Let $`U=\mathbb F_p^n\oplus\mathbb F_p^n`$ and define endomorphisms

```math
P=\begin{pmatrix}I&0\\0&0\end{pmatrix},\qquad
D=\begin{pmatrix}0&I\\0&0\end{pmatrix},\qquad
D_A=\begin{pmatrix}0&A\\0&0\end{pmatrix},\qquad
D_B=\begin{pmatrix}0&B\\0&0\end{pmatrix}.
```

On $`X=U\oplus U^*`$, put

```math
J=\begin{pmatrix}0&I_{2n}\\-I_{2n}&0\end{pmatrix},
\qquad F(T)=\begin{pmatrix}T&0\\0&T^t\end{pmatrix}.
```

For every $`T`$, the matrix $`JF(T)`$ is alternating: its upper-right block
is $`T^t`$ and its lower-left block is $`-T`$. We use the five active forms

```math
J,\quad JF(P),\quad JF(D),\quad JF(D_A),\quad JF(D_B).
```

No assertion that $`F`$ is an algebra homomorphism is needed or intended.

**Recovery lemma.** Simultaneous similarity of the four operators
$`F(P),F(D),F(D_A),F(D_B)`$ determines simultaneous similarity of $`A,B`$.
This holds after any field extension.

**Proof.** Write the coordinates of $`X`$ as
$`(U_1,U_2,U_1^*,U_2^*)`$. Intrinsically define

```math
X_2=\ker F(P),\qquad K=\ker(F(D)|_{X_2}).
```

In these coordinates, $`X_2=U_2\oplus U_2^*`$ and $`K=U_2^*`$.
The induced map $`\overline{F(D)}:X_2/K\to U_1`$ is an isomorphism.
Both $`F(D_A)`$ and $`F(D_B)`$ kill $`K`$ and have image in $`U_1`$.
Consequently the two endomorphisms of $`X_2/K`$

```math
\overline{F(D)}^{-1}\overline{F(D_A)},\qquad
\overline{F(D)}^{-1}\overline{F(D_B)}
```

are precisely $`A,B`$ in the evident coordinates. An intertwiner of the four
operators induces an intertwiner of these endomorphisms. The construction
uses only kernels, images and induced maps, so it is invariant under change
of coordinates and under extension of the field. In particular, it introduces
no ambiguity between a pair and its transpose or dual. ∎

Conversely, suppose $`A'=SAS^{-1}`$ and $`B'=SBS^{-1}`$. With
$`T=\mathrm{diag}(S,S)`$ on $`U`$, set

```math
L_X=\mathrm{diag}(T,T^{-t}).
```

Then $`L_X^tJL_X=J`$, and for each matching pair of active operators
$`M\in\{P,D,D_A,D_B\}`$ and $`M'\in\{P,D,D_{A'},D_{B'}\}`$,

```math
L_X^tJF(M')L_X=JF(M).
```

Thus simultaneous similarity gives an ordered congruence of the active forms.
In the other direction, preserving $`J`$ converts such a congruence into
similarity of the four operators, to which the recovery lemma applies.

## 2. Making the labels intrinsic

The loop interface permits permutation of the forms, so an ordered encoding
is not yet sufficient. We attach symplectic marker spaces with different sizes.
For $`1\leq i\leq4`$, set $`d_i=i(2n+1)`$. Take symplectic spaces
$`C_0,C_1,\ldots,C_4`$ with dimensions $`2,2d_1,\ldots,2d_4`$,
and let $`C`$ be their direct sum.

On $`X\oplus C`$, define $`B_0`$ to be $`J`$ on $`X`$ and the standard
symplectic form on every marker space. For $`i=1,2,3,4`$, let $`B_i`$ be
the corresponding active form on $`X`$, the symplectic form on $`C_i`$,
and zero on the other marker spaces. All these direct sums are orthogonal.

The dimension is

```math
m=4n+2+2\sum_{i=1}^4i(2n+1)=44n+22.
```

The common radical is zero because $`B_0`$ is nonsingular. The forms are
linearly independent even over $`E`$: restriction of a linear relation to
$`C_0`$ first kills the coefficient of $`B_0`$, and restriction to each
$`C_i`$ then kills its remaining coefficient. In particular they satisfy the
weaker prime-field independence required by the interface.

The ranks satisfy

```math
2d_i\leq\mathrm{rank}(B_i)\leq2d_i+4n\quad(1\leq i\leq4).
```

These four intervals are disjoint: adjacent lower endpoints differ by
$`4n+2`$, exceeding the interval width $`4n`$. Also
$`\mathrm{rank}(B_0)=44n+22`$ exceeds the largest upper endpoint
$`20n+8`$. Rank therefore identifies every label, for every input pair and
over every extension field. Any permuted congruence between output tuples
must in fact preserve their order.

## 3. Removing the markers without assuming they are preserved

A congruence need not carry the chosen active space to the other chosen
active space. It would be incorrect simply to restrict it to $`X`$.
Instead we cancel the marker module after passing from forms to operators.

Write $`B_i=B_0T_i`$ for $`1\leq i\leq4`$. An ordered congruence gives
simultaneous similarity of these four $`T_i`$. Regard the underlying vector
space as a module for the free associative algebra on four generators, with
the generators acting by $`T_1,\ldots,T_4`$. It decomposes as

```math
M(A,B)\oplus C,
```

where $`M(A,B)`$ is the active four-operator module and the marker module
$`C`$ is independent of $`A,B`$. Thus a congruence implies

```math
M(A,B)\oplus C\cong M(A',B')\oplus C.
```

**Cancellation lemma.** For finite-dimensional modules over an algebra over
a field, a common direct summand can be cancelled. Also
$`M^{\oplus r}\cong N^{\oplus r}`$ for a positive integer $`r`$ implies
$`M\cong N`$.

**Proof.** Finite-dimensional modules decompose into indecomposables by
induction on dimension. For an endomorphism $`f`$ of an indecomposable module,
the stabilized kernel and image give its Fitting decomposition. Hence $`f`$
is either invertible or nilpotent, and in the latter case $`1-f`$ is invertible.
Its endomorphism ring is local: products involving a nonunit cannot be units
in finite dimension, and if two nonunits had invertible sum, normalization
by that sum would give two nonunits of the form $`f,1-f`$, a contradiction.

Compare two decompositions into indecomposables. The identity of any summand
is the sum of its composites through the summands of the other decomposition.
Locality makes at least one composite invertible. That identifies the first
summand with one on the other side: it is a direct summand of an indecomposable
module, and hence the whole module. Block elimination cancels this matched
summand. Induction proves equality of all indecomposable multiplicities.
Both cancellation assertions follow. ∎

Apply the lemma to cancel $`C`$, then apply the recovery lemma. We obtain
simultaneous similarity of $`A,B`$ from congruence of the five marked forms.
Conversely, the explicit map $`L_X`$ above extends by the identity on $`C`$,
giving congruence of the marked tuples. This establishes the exact reduction
from simultaneous similarity to unordered congruence, over any extension
field. Only ordinary module cancellation was used, not a cancellation theorem
for symplectic representations.

## 4. Descent and the loop conclusion

Every matrix constructed above has entries in $`\mathbb F_p`$. The field
automorphism $`\theta`$ in the loop interface therefore fixes every output
matrix. Ranks remove its permitted permutation. A loop isomorphism consequently
gives an $`E`$-congruence of the ordered tuples and hence an $`E`$-linear
simultaneous similarity of the original pairs.

That similarity descends. Regard $`(A,B)`$ as a module $`V`$ for the free
associative algebra on two generators over $`\mathbb F_p`$, and similarly
form $`V'`$. An isomorphism after extension to $`E`$, restricted back to the
prime field, gives

```math
V^{\oplus r}\cong (V')^{\oplus r}.
```

Indeed, a prime-field basis of $`E`$ splits each restricted module into
$`r`$ copies, since the action matrices lie in the prime field. The cancellation
lemma yields $`V\cong V'`$, exactly the required simultaneous similarity over
$`\mathbb F_p`$. The converse follows from the explicit congruence and scalar
extension. Finally use the loop interface with $`m=44n+22`$ and $`k=5`$
to obtain the asserted order and properties. ∎

## What this contributes to classification

This is an exact orbit encoding, not a theorem that loop isomorphism is
NP-hard, and not an obstruction to all useful classification algorithms.
It shows that a classification of this family must retain at least the
information in simultaneous similarity of arbitrary matrix pairs. Simplicity
of the resulting loops does not eliminate that representation-theoretic data.

The reduction is uniform and uses only five forms, regardless of $`n`$.
It does not enumerate loops without repetition, classify all odd loops, or
address the separate existence of non-G-loops. These examples are G-loops.
It also does not turn the compact-data reduction into a polynomial-time
reduction on explicit multiplication tables.

Two natural further questions are whether the dimension overhead can be
reduced while retaining the exact orbit correspondence, and which restricted
matrix-pair classes yield particularly transparent loop families and invariants.
Neither question is required for the theorem above.

## Sources and proof boundary

- [0024: source construction](../packet/manuscripts/odd-matrix-pair-embedding.md).
  This exposition reorganizes its encoding, rank separation, cancellation and
  descent arguments; it asserts no stronger theorem.
- [0025: alternating-form loop family](../packet/manuscripts/odd-alternating-form-family.md).
  This is the precise conditional input for the loop conclusion, including
  simplicity, properness, the G-loop property and strict isomorphism detection.
- [Research catalogue](../CLAIMS.md) and [programme references](../REFERENCES.md).

The proof here is conventional mathematics, not a formal certificate. No
multiplication-table computation or exhaustive loop enumeration is asserted.
The self-contained part establishes the linear-algebra reduction; the loop
conclusion retains the dependency stated at the start.
