# Isotopy classes controlled by the negative center

**Mira Cult · Claim 0020**

## Results obtained

A loop may have many nonisomorphic isotopes even when its multiplication group is fixed. For a useful class of odd-order Bol constructions, all this freedom is concentrated in a small part of the center of the derived group.

We prove two results:

1. For the class-two normal-form folders specified below, every isotope is represented by a shift indexed by the negative center. Consequently the number of loop-isomorphism classes in one isotopy class is at most the order of that center. The exact answer is an orbit count under strict data isomorphisms, not simply the number of shifts.
2. The simple proper loop of order $`3^{75}19^3`$ in [claim 0018](../0018-non-g-loop-non-bruck-existence.md) has **exactly three** loop-isomorphism classes in its entire isotopy class.

The second assertion strengthens the previously exhibited pair of nonisomorphic isotopes. Its proof uses the explicit construction and specialized lemmas in 0018, not an exhaustion theorem for all class-two-derived Bol loops. The first assertion applies to any folder satisfying the listed structural inputs; extending it to every loop in the proposed general class-two branch depends on that branch's normal-form theorem.

## 1. Folders, centers and the scope of the argument

A left Bol loop satisfies

```math
x\bigl(y(xz)\bigr)=\bigl(x(yx)\bigr)z.
```

An *isotopy* between two loops consists of three bijections transporting one multiplication to the other; an isomorphism uses the same bijection in all three positions. A *G-loop* is isomorphic to all its loop isotopes.

We use a faithful generating folder $`(G,H,K)`$: $`G`$ is the left multiplication group, $`H`$ the stabilizer of the identity, and $`K`$ its set of left translations. Throughout the argument, $`G`$ has odd order and an involutory automorphism $`\tau`$ with

```math
K=\{g\in G:\tau(g)=g^{-1}\}.
```

The group operation is written multiplicatively; central coordinates are written additively. Put

```math
D=G',\qquad Z=Z(D),\qquad S=H\cap D,
\qquad Z^-=\{z\in Z:\tau(z)=-z\}.
```

The general shift theorem assumes the following concrete normal-form properties:

- $`G=DH`$ and $`D=C_D(\tau)Z^-S`$ as a product of sets.
- The chosen coordinates have $`G=D\rtimes A`$, with $`A`$ abelian and inverted by $`\tau`$. Its action on $`Z`$ is $`T`$, and $`\sigma=\tau|_Z`$.
- The stabilizer is a graph over $`A`$, together with its subgroup $`S`$:

```math
H=S\rtimes\{f(a)a:a\in A\},\qquad
f(ab)=f(a)+T(a)f(b).
```

- The graph cocycle satisfies the positivity equation

```math
T(a)\sigma f(a)=f(a).
```

For the proposed general class-two branch, these are inputs from the [class-two normal-form draft](../update-2026-11-16/manuscripts/odd-class-two-classification.md). For the explicit example they follow from the formulas in 0018, as verified in Section 3 below. None of the proofs below assume that the starting loop is a G-loop.

## 2. The shift theorem

**Theorem 1.** Under these hypotheses, every loop isotope is isomorphic to a loop with folder

```math
(G,zHz^{-1},K),\qquad z\in Z^-.
```

The corresponding cocycle is

```math
f_z(a)=f(a)+(1-T(a))z.                 \tag{1}
```

Thus there are at most $`|Z^-|`$ isomorphism classes in the isotopy class.

**Proof.** We first explain why arbitrary isotopes can be studied by conjugating the stabilizer while keeping the section fixed. The principal-isotope calculation in [0018, Lemma E](../0018-non-g-loop-non-bruck-existence.md#lemma-e-the-principal-isotope-interface) gives a representative folder

```math
(G,H,k^{-1}K),\qquad k\in K.
```

Every isotope is isomorphic to such a principal isotope. Because the group order is odd, $`k`$ has a unique square root $`r`$ in its cyclic subgroup. Then $`r\in K`$. The shifted section is the full inverted set for

```math
\tau_k=\mathrm{Inn}(k^{-1})\tau.
```

Conjugating by $`r`$ transports this automorphism to $`\tau`$, since

```math
\mathrm{Inn}(r)\tau_k\mathrm{Inn}(r^{-1})
 =\mathrm{Inn}(rk^{-1}\tau(r^{-1}))\tau
 =\tau.
```

Here $`\tau(r^{-1})=r`$ and $`r^2=k`$. The folder therefore becomes $`(G,rHr^{-1},K)`$.

More generally let $`g\in G`$. Write $`g=dh`$ with $`d\in D,h\in H`$, and then write $`d=czs`$ with $`c\in C_D(\tau),z\in Z^-,s\in S`$. Since $`s`$ normalizes $`H`$,

```math
gHg^{-1}=czHz^{-1}c^{-1}.
```

Conjugation by $`c^{-1}`$ commutes with $`\tau`$ and therefore preserves $`K`$. It gives a genuine folder isomorphism to $`(G,zHz^{-1},K)`$.

Finally $`z`$ centralizes $`D`$ and hence $`S`$, while conjugating a graph element gives

```math
z(f(a)a)z^{-1}=\bigl(f(a)+z-T(a)z\bigr)a.
```

This is precisely (1). The added term is a crossed coboundary, so $`f_z`$ is again a cocycle. It obeys the same positivity condition: using $`\sigma z=-z`$ and $`\sigma T(a)=T(a)^{-1}\sigma`$ gives

```math
T(a)\sigma(1-T(a))z=(1-T(a))z.
```

Every displayed shift also occurs as an actual isotope: take $`k=z^2\in K`$ and use the same conjugation calculation with $`r=z`$. This proves the assertion. ∎

**Isomorphism qualification.** Distinct shifted cocycles need not define nonisomorphic loops. To count classes exactly one must quotient the shifts by the strict isomorphism relation on the entire datum, preserving the bracket, involution, torus action and stabilizer axes, and transporting one cocycle exactly to the other. The general form of that criterion is another input from the class-two draft. The specialized form required below is proved directly in [0018, Lemma F](../0018-non-g-loop-non-bruck-existence.md#lemma-f-the-strict-isomorphism-test-for-these-examples).

## 3. Three candidate classes for the explicit example

Recall the explicit example's data:

```math
A=\langle a\rangle\times\langle d\rangle\cong C_9\times C_{19},
\quad Z_3=\mathbb F_3[\epsilon]/(\epsilon^3),
\quad T(a)=1+\epsilon,
\quad \sigma(\epsilon)=-\epsilon+\epsilon^2.
```

The 19-center is fixed by the involution. The 3-center splits into its positive and negative eigenspaces, with

```math
Z_3^-=\mathbb F_3(\epsilon+\epsilon^2),\qquad
f(a)=1-\epsilon+\epsilon^2.
```

We verify the product decomposition required by Theorem 1 directly. Each derived Sylow factor has coordinates $`W\oplus W\oplus Z`$, with the involution swapping the two copies of $`W`$ and acting as $`\sigma`$ on $`Z`$. Its multiplication is the class-two product in 0018, Lemma A. Its stabilizer intersection consists of $`(u,0,0)`$.

Given any $`(x,y,t)`$, multiply an element $`(y,y,t_+)`$ fixed by the involution, a negative central element $`(0,0,t_-)`$, and $`(x-y,0,0)`$. The vector coordinates are $`(x,y)`$. The center is

```math
t_++t_- -\tfrac12 b(x-y,y).
```

Because the center has odd order, every element has a unique positive-plus-negative decomposition for $`\sigma`$. Choose $`t_++t_-=t+\tfrac12 b(x-y,y)`$. This proves $`D=C_D(\tau)Z^-S`$. Also $`H`$ surjects onto $`A`$, so $`G=DH`$. All other hypotheses are the explicit graph and action formulas of 0018.

For $`z=k(\epsilon+\epsilon^2)`$, equation (1) becomes

```math
f_k(a)=1-\epsilon+(1-k)\epsilon^2,\qquad k\in\mathbb F_3.       \tag{2}
```

The cocycle value on the other generator $`d`$ and the 19-center component are unchanged; values on powers are determined by the cocycle law. Theorem 1 now gives at most three isomorphism classes, and each candidate is an actual isotope. It remains to prove pairwise nonisomorphism; distinguishing only the original loop from one shift would not suffice.

## 4. A rank obstruction separates all three

**Theorem 2.** The three loops in (2) are pairwise nonisomorphic. They constitute the entire isotopy class of the loop in 0018.

**Proof.** Suppose an isomorphism carries the datum with index $`i`$ to the datum with index $`j`$. Apply the specialized strict criterion of 0018, Lemma F. On the 19-axis the action of $`a`$ is the scalar $`\eta`$ of order nine over the prime field $`\mathbb F_{19}`$. If the induced torus map sends $`a`$ to $`a^u`$, intertwining forces $`\eta^u=\eta`$. Thus $`u=1`$ modulo nine.

The induced map $`M`$ on $`Z_3`$ must therefore commute with $`T(a)`$ and with $`\sigma`$. The centralizer of the single Jordan block $`T(a)`$ consists of multiplication by

```math
u+v\epsilon+w\epsilon^2\quad(u\ne0).
```

Commutation with $`\sigma`$ forces $`v=0`$. Strict cocycle transport $`Mf_i(a)=f_j(a)`$ then forces

```math
u=1,\qquad w=i-j,
\qquad M=1+(i-j)\epsilon^2.             \tag{3}
```

If $`i\ne j`$, this is one of the two nontrivial shears. The underlying map, after forgetting the cocycle, is an automorphism of the same bracket, involution and action datum. Its square is therefore also such an automorphism. One of its first two powers acts on the center as $`1-\epsilon^2`$. We show that no automorphism of the underlying datum can induce that shear.

The 3-axis is $`E^4`$, where $`E=\mathbb F_{3^{18}}`$, and $`d`$ acts by a scalar $`\lambda`$ of order nineteen which generates $`E`$ over $`\mathbb F_3`$. An intertwiner, allowing a torus map on $`d`$, is consequently semilinear over $`E`$. The bimap matrices have entries in $`\mathbb F_3`$, and the field trace is invariant under Frobenius. Removing the field automorphism leaves an invertible $`E`$-linear matrix $`L`$ satisfying the corresponding congruence equations. In particular the center shear $`1-\epsilon^2`$ requires

```math
L^TB_2L=B_2-B_0,
```

where

```math
B_0=\begin{pmatrix}
0&0&0&0\\0&0&0&1\\0&0&0&0\\0&2&0&0
\end{pmatrix},\qquad
B_2=\begin{pmatrix}
0&2&1&1\\1&1&0&2\\2&2&0&0\\0&1&0&0
\end{pmatrix}.
```

The trace-valued bimap identity implies this matrix identity by nondegeneracy of the trace pairing. But direct calculation in $`\mathbb F_3`$ gives

```math
\det(B_2-B_2^T)=1,
\qquad
\det\bigl((B_2-B_0)-(B_2-B_0)^T\bigr)=0.
```

An invertible congruence preserves the rank of the skew part, over $`E`$ as well as over the prime field. This contradiction excludes the shear. By (3), it excludes every identification with $`i\ne j`$. Together with Theorem 1 this proves the exact census. ∎

The argument does not assume that a possible isomorphism fixes the 19-torus or has trivial Frobenius component. Those possibilities are absorbed by semilinearity and by taking powers of the full underlying data automorphism, rather than powers of a proposed cocycle transport alone.

## 5. Consequences and open questions

The entire isotopy class has three classes, not merely a known subset of three. Since 0018 proves that the starting loop has no Bruck isotope, none of these three classes is Bruck. In particular this is a finite, nontrivial isotopy orbit outside the Bruck-isotope route.

More generally Theorem 1 turns an unrestricted search through principal isotopes into a bounded orbit problem in $`Z^-`$. It does not give an efficient isomorphism algorithm and does not assert that the upper bound is always attained. Nontrivial automorphisms of the bracket and action data can identify shifts.

Two natural next questions are:

- Within the admissible class-two normal-form construction, which integers occur as the number of isomorphism classes in an isotopy class of simple proper loops? In particular, can this number be made arbitrarily large?
- Can one characterize the action on shifted cocycles intrinsically from the bracket and torus modules, making the orbit count accessible without testing all strict data isomorphisms?

## Sources and verification scope

The general orbit argument and exact three-class deduction originate in [Isotope orbits for odd class-two-derived folders](../update-2026-11-16/manuscripts/odd-class-two-isotope-orbits.md), source revision `7530ae6eeeb0614d7c94ed6ab1f6761f3493ab88`, preserved in the public source snapshot. This exposition separates those results from the source's additional rank-one-center and squarefree-abelianization statements, which are not proved here.

The explicit group, bimap, simplicity and properness proofs, the principal-isotope interface, and the specialized strict isomorphism criterion are in [0018](../0018-non-g-loop-non-bruck-existence.md). The coordinate decomposition in Section 3 supplies the missing general-normal-form input directly for that example. Accordingly the exact three-class conclusion does not import the general exhaustion assertion of claim 0019.

The displayed arithmetic and the new coordinate decomposition can be checked independently of the full loop, whose order is far too large for a table census. These are conventional proof arguments, not a formal verification or a new claim of literature priority.
