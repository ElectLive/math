# A chief-factor obstruction for arbitrary Bruck radicals

**Theorem with scoped independent reviews below, conditional on the cited inputs.** This continues [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md), without a new permanent ID. Work with the faithful canonical Bruck envelope $`(G,H,K)`$, $`P=O_2(G)`$, $`A=G/P=\prod_j A_j`$, $`A_j=\mathrm{PGL}_2(q_j)`$, $`\pi(H)=\prod_j B_j`$, $`W=P\cap H`$, and canonical inversion $`\tau`$. Take one singleton factor $`D=A_i`$, its Borel $`B=B_i`$, a prescribed nonsplit outer involution $`t\in D`$, and an odd subgroup $`R\le C_D(t)`$ of prime-power order $`p^a`$. The Bruck-envelope input is Baumeister–Stein [arXiv:0908.2597v1](https://arxiv.org/html/0908.2597v1), Theorem 1 and Lemmas 3.2(1)–(2), 3.4 and 4.1–4.5, in the form scoped in [the elementary product source interface](bruck-elementary-product-constraints.md) at the recorded source revision: $`\tau`$ fixes $`H`$ pointwise, induces identity on $`A`$, $`\Lambda=\widehat\tau K`$ is invariant under conjugation by $`G`$, and every original singleton marked fiber has positive 2-power cardinality.

Assume there is a finite series

```math
P=P_0\triangleright P_1\triangleright\cdots\triangleright P_n=1\tag{1}
```

whose terms are normal in $`G_i=\pi^{-1}(D)`$, invariant under $`\tau`$, and satisfy $`[P,P_j]\le P_{j+1}`$. Put $`L_j=P_j/P_{j+1}`$, an elementary abelian $`D`$-module, and assume:

* $`\tau`$ acts trivially on each $`L_j`$;
* $`H^1(D,L_j)=H^2(D,L_j)=0`$;
* $`L_j|_B`$ is semisimple projective and $`L_j^B=0`$;
* $`H^1(\langle t\rangle,L_j)^R=0`$.

Under these conditions the envelope cannot exist, conditional on the cited Bruck inputs. No centrality or bound on the nilpotency class of $`P`$ is assumed. The final section explains how a chief-factor hypothesis may supply (1); that implication has the independent reviews below, and the modular inputs retain their cited review scope.

## Local complement aligned to the actual Borel

Successive abelian-kernel lifting gives a complement $`D^*\le G_i`$: the kernels are central in the corresponding quotient of $`P`$, but need not be central in the quotient of $`G_i`$. At stage $`j`$, the obstruction to lifting a complement from $`G_i/P_j`$ to $`G_i/P_{j+1}`$ lies in $`H^2(D,L_j)=0`$. Inductively any two such $`D`$-complements are $`P`$-conjugate: after aligning their images modulo $`P_j`$, their remaining difference is a 1-cocycle with values in $`L_j`$, removed using $`H^1(D,L_j)=0`$.

Let $`H_i=H\cap\pi^{-1}(B)`$; it maps onto $`B`$ with kernel $`W`$. The series $`W\cap P_j`$ has elementary factors that embed as $`B`$-submodules of $`L_j`$. They are projective because $`L_j|_B`$ is semisimple projective. Inductively $`H^2`$ of each factor vanishes, so the extension $`1\to W\to H_i\to B\to1`$ splits. Similarly $`H^1(B,L_j)=0`$ for every $`j`$, so any two $`B`$-complements in $`\pi^{-1}(B)`$ are $`P`$-conjugate, by the same successive lifting. Conjugating $`D^*`$ by an element of $`P`$ therefore lets us arrange

```math
B^*:=D^*\cap H_i\cong B.\tag{2}
```

This constructs no complement for the other factors.

Each $`L_j^B=0`$, so $`C_P(B^*)=1`$: a nonidentity centralizing element would have a nonzero image in the first series quotient in which it appears. The automorphism $`\tau`$ preserves $`G_i`$, fixes $`B^*`$ pointwise, and takes $`D^*`$ to another $`D`$-complement. Thus $`\tau(D^*)=(D^*)^x`$ for some $`x\in P`$. For $`b\in B^*`$, the two unique lifts of $`\pi(b)`$ in $`\tau(D^*)`$ coincide, giving $`x^{-1}bx=b`$; hence $`x=1`$. Since $`\tau`$ induces identity on $`D`$, it fixes $`D^*`$ pointwise. It need not fix $`P`$, nor any other factor.

## Nonabelian cocycles centralizing the odd torus

Let $`\widehat\tau`$ denote the formal involution inducing $`\tau`$, put $`a=\widehat\tau t^*`$, and identify $`R`$ with its pure lift in $`D^*`$. Then $`a^2=1`$ and $`[a,R]=1`$. Consider the original marked fiber $`\Lambda_t`$ over $`t`$. It is $`R`$-invariant and has positive 2-power cardinality. Since $`R`$ is a $`p`$-group for odd $`p`$, its nontrivial orbits have size divisible by $`p`$; hence $`R`$ fixes **an actual marked element** $`\lambda\in\Lambda_t`$, not merely a conjugacy class. Write $`\lambda=ax`$ with $`x\in P`$. Then $`[x,R]=1`$, and $`\lambda^2=1`$ gives the nonabelian cocycle equation $`a(x)x=1`$.

Put $`Q=C_P(R)`$, $`Q_j=Q\cap P_j`$. The coprime fixed-coset lemma below gives surjectivity $`Q_j\to L_j^R`$ with kernel $`Q_{j+1}`$, hence $`Q_j/Q_{j+1}\cong L_j^R`$. The $`a`$-action on $`L_j`$ equals that of $`t`$, since $`\tau`$ acts trivially there. Odd averaging makes fixed points exact and yields

```math
H^1(\langle a\rangle,L_j^R)\cong H^1(\langle t\rangle,L_j)^R=0.\tag{3}
```

By successive central lifting, every cocycle for $`\langle a\rangle`$ in $`Q`$ is a coboundary: kill its image in $`Q_0/Q_1`$ using (3), then continue down the series. Explicitly each step conjugates $`ax`$ by an element of $`Q_j`$ to put its new radical coordinate in $`Q_{j+1}`$. Thus $`\lambda`$ is $`Q`$-conjugate to $`a`$. Marked invariance gives $`a=\widehat\tau t^*\in\Lambda`$, hence $`t^*\in K`$.

For every $`d\in D^*`$, $`\tau(d)=d`$, so conjugating the marked element shows $`(t^*)^d\in K`$. The outer involution class has $`q_i(q_i-1)/2>q_i`$ elements, all outside the point Borel. Two lie in one of the $`q_i`$ nontrivial $`B^*`$-cosets. Their quotient is a nonidentity element of $`B^*\le H`$, contradicting the transversal property of $`K`$.

## Lower exponent-two layers and the common-prime formulation

The [Frattini-shadow manuscript](bruck-frattini-shadow.md) establishes, with scoped input review at the recorded source revision, that $`\tau`$ acts trivially on every layer of the lower exponent-two central series $`P_1=P`$, $`P_{j+1}=P_j^2[P_j,P]`$. Each layer is an elementary $`D=G_i/P`$-module, because $`P`$ acts trivially on it. Refine these characteristic layers by $`D`$-submodules to simple factors. Their inverse images are normal in $`G_i`$, the refined series is still central relative to $`P`$, and $`\tau`$ acts trivially on each term of each layer and on each refined quotient. The resulting simple factors count **all** chief factors in $`P`$ for the local group $`G_i`$, including layers below $`\Phi(P)`$; they are not merely composition factors of $`P/\Phi(P)`$.

Assume every such factor is a nonprincipal binary simple and the nonprincipal module inputs in [the uniform module theorem](bruck-central-frattini-all-quotients.md) at the recorded source revision hold: for each factor $`L`$, the two cohomology groups of $`D`$ vanish; $`L|_B`$ is semisimple projective and $`L^B=0`$; and over a splitting field the weights of the odd nonsplit torus $`R_0\cong C_{(q_i+1)/2}`$ on $`H^1(\langle t\rangle,L)`$ are $`\theta,\theta^{-1}`$ and their Frobenius conjugates. All weights attached to one binary simple have a common nontrivial odd order $`d_L`$, independent of choice of a Frobenius conjugate or inversion.

If one odd prime $`p`$ divides every $`d_L`$, choose $`R`$ to be the Sylow $`p`$-subgroup of cyclic $`R_0`$. Every displayed weight restricts nontrivially to $`R`$, so $`H^1(\langle t\rangle,L)^R=0`$ by semisimplicity of the odd group action and faithful scalar extension. The conditions of the candidate obstruction above hold. Consequently, conditional on the representation and Bruck inputs, the following is a necessary condition for an envelope: **either some local $`G_i`$-chief factor inside $`P`$ is principal, or the nonprincipal factors have $`\gcd_L d_L=1`$**. The formulation includes the trivial module among principal factors. If $`P=1`$, the source singleton-fiber formula already fails integrality for every allowed $`q_i\ge5`$, so there is no empty-family exception.

For $`q_i=5,9,17`$, the odd nonsplit torus has respective order $`3,5,9`$. Every nontrivial $`d_L`$ is divisible by the same prime, so at least one principal chief factor must occur inside $`P`$. For $`q_i=257`$, its order is $`129=3\cdot43`$; if all factors are nonprincipal, gcd one forces at least one factor of order $`3`$ and at least one of order $`43`$, though factors of order $`129`$ may also occur. These are necessary chief-factor conditions, not claims about the Frattini shadow and not a classification of loops.

The single-isotype representation interface and source matching have the reviews recorded in that theorem; the present nonabelian application has the independent exact-revision reviews below. In particular the argument uses the layerwise fixed-space vanishing for one chosen $`p`$-subgroup; it does not infer that arbitrary mixed-isotype nonzero label orbits all have a common divisor.

## Coprime fixed-coset input

Let a finite odd-order group R act on a finite 2-group Y, and let N be an R-invariant subgroup. An R-fixed coset in Y/N is an R-stable transitive N-set X. More generally, if a finite 2-group N acts transitively on a nonempty finite set X compatibly with R, then X has an R-fixed point. Indeed the stabilizer S of a point under N⋊R maps onto R, since N is transitive, and has normal 2-subgroup S∩N of odd index. Schur–Zassenhaus supplies a complement R′≤S. In N⋊R the two complements R′ and R are N-conjugate, so an N-translate of the chosen point is fixed by R. Applied with Y=P_j and N=P_{j+1}, this proves the fixed-point surjectivity used above, even though the kernel is not abelian.

The exact group-theory input is David A. Craven, [*Finite Group Theory*, Hilary Term 2012](https://web.mat.bham.ac.uk/D.A.Craven/docs/lectures/finitegroups2012.pdf), §2.1, Theorem 2.1, printed p.22: complement existence and conjugacy for a normal Hall subgroup when that subgroup or its quotient is soluble. All normal Hall kernels here are finite 2-groups and hence soluble, so no odd-order theorem is needed for this step. Conjugacy can be taken by the normal Hall subgroup: factor an arbitrary conjugator using the fixed complement. Reviewer an independent check directly checked this source statement before the assembled argument was committed; this source inspection is not independent review of the new loop theorem.

No computation is needed or claimed for this argument. The scope is a necessary condition on all local chief factors inside the arbitrary radical, with its explicit source and modular assumptions. It does not force a principal summand in P/Φ(P), bound the radical, or classify the surviving principal-factor or mixed-character cases.

## Independent review

Independent checks an independent check, an independent check and an independent check independently accepted the arbitrary-radical local obstruction and its common-prime chief-factor application at exact source the recorded source revision, conditional on the cited Bruck-envelope/fiber, lower exponent-two inversion, uniform module/torus-weight and Schur–Zassenhaus inputs. They checked successive complement lifting and conjugacy, the actual H_i using W∩P_j without assuming W normal in P, and C_P(B*)=1 forcing inversion to fix the local complement. They checked the actual R-fixed marked element, fixed-coset surjectivity, averaging and layerwise nonabelian cocycle elimination, and the final pure-class collision. All three retained the distinction between all local chief factors inside P and just the Frattini shadow. Reviewer an independent check directly checked Craven's stated Schur–Zassenhaus interface; the prior module/source limitations remain as recorded in their canonical sources. No computation or formal verification was used. None of these reviews establishes a bound, a principal factor in P/Φ(P), or a classification of the remaining cases.

