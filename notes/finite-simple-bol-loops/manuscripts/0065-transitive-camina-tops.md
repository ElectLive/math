# 0065. Faithful transitive tops and the Camina census

Mira Cult

## Results obtained

Let $`P`$ be a finite odd $`p`$-group acting faithfully and transitively on $`\Omega`$, put $`n=|\Omega|`$, and let $`S=A_5^\Omega\rtimes P`$. Consider exactly

```math
G=\{(x,y)\in S^2:\overline{\mathop{\mathrm{top}}\nolimits(x)}+
\overline{\mathop{\mathrm{top}}\nolimits(y)}=0\text{ in }P/P'\},
\qquad \tau(x,y)=(y,x).
```

The top action on $`\Omega`$ is not assumed regular. Three results belong together here.

1. **Structural reduction.** For nontrivial $`P`$, every faithful generated canonical folder of a finite simple nonassociative left Bol loop in this exact model has $`p\in\{3,5\}`$. It is described by an actual quotient of the permutation module $`\mathbb F_p[\Omega]`$, together with a cocycle satisfying the relevant-top collision test below. The theorem gives the converse and exact permutation-normalizer equivalence, but does not evaluate all such orbits for general $`P`$.
2. **Extraspecial census.** Across all faithful transitive actions of odd extraspecial $`P`$, the exact models give **128 classes**: the [120 regular-action classes](0064-extraspecial-regular-census.md), three additional classes of order $`27\cdot60^9`$, and five additional classes of order $`125\cdot60^{25}`$.
3. **Camina extension.** The same 128-class census exhausts these exact models for every nonabelian class-two odd $`p`$-group satisfying
   $`Z(P)=P'`$ and $`[x,P]=P'`$ for every $`x\notin P'`$.
   Higher-rank centers are excluded; the surviving groups are extraspecial.

The affine lemmas in Section 3 are standalone algebraic statements. Their Bol applications use the faithful-folder, full-strip, normal-subloop and simple-Moufang interfaces of the [prime-power source](../sources/factor-permutation/radical-free-a5-prime-power-top.md), together with the [regular abelian cyclic-module theorem](../sources/factor-permutation/radical-free-a5-abelian-top.md#the-regular-cyclic-module-algebra). The explicit regular extraspecial orbit calculations are inputs from the preceding note, not consequences of the dimension bound alone.

## 1. The actual permutation-module reduction

### The faithful transitive bound and full mark

Since P is a faithful transitive p-subgroup of Sym(Ω), n=p^a and

`e≤v_p(n!)=(n−1)/(p−1)<n/2`                                      (1)

for odd p and n>1. Here `v_p(n!)=Σ_{j=1}^a p^(a−j)=(n−1)/(p−1)` by counting the multiples of each p-power; the faithful embedding gives the order bound. The trivial P case has n=1 and is treated by the same zero-dimensional datum at the end.

Let N=A5^(2Ω), F=G/N. Outside involutions with first top x∈P form one N-conjugacy class of size 60^n. F acts on the class labels by `x↦b^-1 x a`. This action is transitive: for x,y choose a with `2 ab(a)=ab(y)−ab(x)` and take b=x a y^-1. P_ab has odd order, so this equation is solvable. G-conjugacy invariance of the actual Λ=τK therefore makes K the full anti-diagonal of S. Since F is a p-group, if HN/N were proper it would lie in a proper normal maximal subgroup; the exact normal-quotient criterion would then be contradicted by the actual K image. Hence H maps onto F and `|H0|=60^n/|P|` for H0=H∩N. Integrality forces p∈{3,5} for nontrivial P.

### Full strips and actual H0

The original H0 full strips split independently from the proper-coordinate residual. If both socle rows have full projections, an involution chosen independently in each strip matches at both ends of every τ-pair, yielding H0∩K²≠1. If only one row is full, P preserves its strip partition. A singleton would, by transitivity, force every factor of that row to be singleton and put the whole G-normal row in H, contradicting corefreeness. Thus the number m of strips is at most n/2. The residual on the proper row has order 60^(n−m)/|P|, divisible by both 3 and 5 by (1), while all its proper coordinate projections are P-conjugate. No proper A5 subgroup contains both primes, contradiction. Therefore all coordinate projections are proper.

Transitivity and the 3/5 divisors of |H0| force, up to global row swap, first-row projections C5/D10 and second-row projections C3/S3/A4. If the second projection is C3, the available 2-part is ≤2^n, smaller than |H0|_2=2^(2n). If it is S3, a Sylow-2 subgroup is a 2n-dimensional subspace of C2^n×C2^n and has nontrivial intersection with the n-dimensional matched-support diagonal, contradicting the actual marked square. Thus the second projection is A4.

Let Q≤F3[Ω] be the image of H0 in `(A4/V4)^Ω`. It has dimension n−v3(|P|). Its nonzero coordinate characters are transitively permuted by P. If two are proportional, all proportionality blocks have equal size at least p, so dim Q≤n/p≤n/3, contradicting (1). Their V4 coordinate modules are pairwise nonisomorphic simple F2[Q]-modules. Since `H0′≤C5^Ω×V4^Ω` and projects onto each V4 coordinate, semisimplicity gives `O2(H0′)=V4^Ω`. This exhausts |H0|_2, so the first projections are C5. Goursat then gives the actual subgroup

`H0=W5×preimage(Q3)`,                                               (2)

where `W5≤F5[Ω]` has codimension v5(|P|), Q3=Q≤F3[Ω] has codimension v3(|P|), and the second preimage is in A4^Ω. One codimension is e, the other zero. No independence of arbitrary residual projections or equality between projection/intersection operations is assumed.

Standardize each paired (C5,A4) containment by common even coordinate conjugations, using D10's transitivity on the five A4 point stabilizers. The first-side reflection signs of H form a cocycle F→F2[Ω]. Since |F| is odd, averaging removes every such cocycle: if r is the sign cocycle, put b=|F|^-1 Σ_f r(f) in F2[Ω]. Summing r(gf)=r(g)+g r(f) gives r(g)=b−g b. Common even coordinate reflections in D10∩A4 with this sign vector give the required τ-compatible conjugation. This averaging replaces the regular-module formula and does not assume P acts regularly. The second-side base lies in A4^Ω; the active W5 or Q3 is P-invariant.

### Actual permutation-module and collision data

Put `M5=F5[Ω]/W5`, `M3=F3[Ω]/Q3`, and M=M5⊕M3. For p=5, M=M5 and its linear F-action is through the first P-coordinate; for p=3, M=M3 and its action is through the second. The actual H lifts define a cocycle η:F→M, with dim_Fp M=e and |M|=|P|. Because P acts transitively, Fp[Ω] and M are cyclic P-modules generated by the image of a point vector δ_ω; the generator is fixed by the point stabilizer P_ω. The quotient is an actual quotient of Fp[Ω], not an arbitrary e-dimensional cyclic Fp[P]-module.

For f=(a,b)∈F call f relevant if b is P-conjugate to a^-1. The exact collision condition is

`η(f)∉im(1−ρ(f))` for every relevant f≠1.                           (3)

Necessity follows because H∩K²=1 and second wreath coordinates of K² are conjugate inverses of the first. For sufficiency, compare wreath cycle products under the two permutations on Ω: the first-side C5 products have orders 1 or5, while the second-side A4 products have orders 1,2 or3, so a collision has all products identity. Conversely, (3) failing allows H0 adjustments to make each active-row base sum zero on every cycle, because the kernel of cycle sums in the permutation module is im(1−shift); the independent V4^Ω in (2) then clears the remaining A4 cycle products. Relevance supplies an actual conjugator in P taking one top to the inverse of the other; after that permutation, base conjugation along each cycle makes the two S elements inverse-conjugate. Matching permutation cycle types alone is not substituted for conjugacy in P. At top zero the disjoint-order argument excludes every nonidentity collision. Thus (3) is exactly the original H∩K² condition, with no projected-folder assumption.

### Converse, simplicity and isomorphism

Fix a P-invariant subspace U≤Fp[Ω] of codimension e and an actual cocycle η:F→M=Fp[Ω]/U satisfying (3). Use U for the active row in (2), and use the other row's full C5^Ω or A4^Ω. Since e<n, transitivity makes every coordinate projection of U nonzero and hence onto Fp; the actual H0 coordinate projections are C5 and A4. Let H be the graph-preimage of η over F inside `G∩[(C5^Ω⋊P)×(A4^Ω⋊P)]`. It has `|H0|=60^n/|P|`, maps onto F, and `|H||K|=|G|`. Condition (3), inverse closure and sandwich closure of K, and G-conjugacy-invariance of Λ make K a transversal to H and all conjugates. The anti-diagonal generates G because `S′=A5^Ω⋊P′`.

Faithfulness of P's action gives `C_G(N)=1`. Every nontrivial normal subgroup L of G meets N, whose simple-factor intersections are P-invariant, so it contains a whole socle row. Thus H is core-free. If L misses one row, it centralizes that row and has trivial S-projection there; projection of K to G/L is injective and gives `|KL/L|=|K|=[G:H]>[G:HL]`. If L contains N, H maps onto G/N while K generates the quotient, again giving strictness for a nontrivial quotient. The exact normal-subloop criterion proves simplicity. G has proper nontrivial normal socle rows, so the loop is nonassociative. The proper intermediate endpoint-normalizer subgroup `G∩[(D10^Ω⋊P)×(A4^Ω⋊P)]` makes the canonical action imprimitive, hence the cited simple-Moufang criterion proves properness.

For isomorphism, the C5 and A4 H0 projection orders distinguish the two rows after a global orientation. A loop isomorphism intertwines canonical τ and therefore uses a common coordinate permutation on corresponding factors. It must normalize the actual transitive permutation group P, so it lies in `N_Sym(Ω)(P)`; write f for it and σ for the induced automorphism of P. Paired endpoint normalization leaves local maps in C4=N_S5(C5)∩N_S5(A4). Each first-side H lift has C5 base. Comparing the local C4 maps at x and a^-1x for each a∈P forces their ratio into C5∩C4=1; transitivity makes the local C4 multiplier uniform. The socle centralizer is trivial, excluding hidden ambient automorphisms.

Thus the exact relation on actual quotient kernels and cocycles is generated by

`U↦T_f U`,  `η'(h)=μ T_f[η(σ_F^-1(h))]` in `Fp[Ω]/T_f U`,           (4)

where f∈N_Sym(Ω)(P), σ_F acts diagonally on F, and the uniform C4 scalar μ ranges over F5* for p=5 and {±1} for p=3. Every operation in (4) comes from an actual canonical-folder automorphism. Quotient-basis changes redescribe the same datum; arbitrary GL(M) maps or arbitrary cocycle coboundaries are not additional isomorphisms. The trivial P case has n=1,e=0, yields H0=C5×A4 and recovers the unique paired A5 class.

### Class-two Camina regularity

The regularity lemma is unchanged by nonregular coordinate actions. Suppose additionally P has class two, Z(P)=P′, and [x,P]=P′ for every x outside P′. Let its top fiber F act on any set M of size |P|, and suppose no nonidentity relevant f fixes 0. The |P| anti-top elements `(x,x^-1)` give pairwise distinct images of 0, because the difference of two has second component conjugate to the inverse of the first. Thus the action is transitive and the stabilizer T has order |P′|. If (a,b)∈T with a outside P′, then b lies in a^-1P′ and is conjugate to a^-1, contradiction. Hence T≤P′×P′≤Z(F), so T is the kernel and F/T acts regularly on M. This uses |M|=|P| and the relevant-top condition, not regularity of P on Ω. It does not assert existence of admissible permutation-module data or a classification for all p-groups.

## 2. The eight nonregular extraspecial classes

### Reduction and possible nonregular stabilizers

For any admissible P, the faithful-transitive reduction forces its prime to be 3 or 5 and gives a cyclic e-dimensional Fp[P]-module M, e=log_p|P|, together with a collision-free affine action of the top fiber F. Its cyclic generator is the image w of δ_L for a point stabilizer L≤P, so w is L-fixed. The same class-two Camina lemma as in the regular case makes the affine image regular and the point stabilizer a central line. Since Ω is faithful, L is core-free. Conversely a cyclic module quotient generated by an L-fixed w, with admissible affine data, is an actual quotient of Fp[P/L], so the transitive converse constructs a simple proper folder.

For an abelian linear image R(P) and a cyclic vector w, its stabilizer in P is exactly ker R: an element fixing w fixes every R(p)w by commutativity, and these vectors span M. Every surviving active linear P-image in the cited extraspecial classification is abelian.

The cited regular-top results restrict admissible extraspecial P to order 27 exponent 3 or 9, order 125 exponent 5, and order 5^5 exponent 25. The module and affine obstructions there use the cyclic Fp[P]-module, dimension e, and actual F-action, rather than regularity of P on Ω, and therefore also constrain every permutation-module quotient. In the exponent-three 27 case, the only surviving linear module has square-zero displacement algebra and a two-dimensional displacement span. A cyclic generator w lies outside that span; every noncentral P element acts nontrivially on w. In the abelian principal-unit cases, an element fixes a cyclic generator exactly when its multiplier lies in the annihilator; in P that kernel is the center. The same applies to the exponent-25 order-5^5 principal-unit case. A nontrivial L in any of these cases would lie in the center and have nontrivial core, impossible. The excluded regular-top module types remain excluded. Thus a nonregular action can survive only in a rank-one nonabelian Jordan-block case with the second linear generator acting trivially.

For the modular order-27 top, the existing six-case calculation has linear normal forms `ρ(anti-g)=1+N`, `ρ(anti-t)=1+vN²`, N³=0≠N², with the active P-action through the second coordinate. If v≠0, the kernel of the active P-representation is central and no noncentral element fixes a cyclic generator; hence nonregularity forces v=0. For the exponent-five order-125 top, the square-zero, abelian and Jordan v≠0 cases are excluded by the same fixed-generator argument, so again v=0. In both v=0 cases the kernel of the active P-representation is `<t,z>`, an elementary abelian group of order p². An extraspecial group has every nontrivial normal subgroup intersecting its order-p center, so a subgroup is core-free exactly when it intersects the center trivially. Any nontrivial core-free point stabilizer in this kernel is therefore a noncentral line. All such lines are conjugate under top automorphisms and inner translations; normalize L=<t>. Its index is p², hence the only nonregular degrees are 9 and 25, respectively. In the modular case the surviving central-kernel parameters are α=0,1; in the exponent-five case they are α=0,1,2,4, the four non-half parameters. These are inherited from the regular top classifications, and α remains invariant under the actual common-coordinate normalizer because it is defined by a central kernel line in F.

### Coupled quotient-generator and cocycle invariant

Fix L=<t>, a cyclic permutation-module generator w=π(δ_L) fixed by t, and use the active linear action with `N=ρ(anti-g)−1`, `N³=0≠N²`. Write the anti-t cocycle displacement as

`B=η(anti-t)=b1 Nw+b2 N²w`,  `b1≠0`,  `s=b2/b1`.

Here the active P-action sends g to (1+N) for p=5 and to (1+N)^-1 for p=3, while t and z act trivially. The actual permutation quotient has a unique kernel in these coordinates: its map is `δ_(xL)↦ρ_active(x)w`, and its image algebra is Fp[N]/N³. A cyclic generator gives an injective map from that image algebra to M, so changing its basis does not introduce additional quotient kernels. The coefficient b1 is nonzero by regularity on the two-dimensional affine fiber over M/NM. It is essential to retain w: unlike a regular coordinate action, arbitrary cyclic-module unit changes cannot be declared ambient isomorphisms. Let c=(z,1), d=(1,z), and `T_α=<c^α d^(1−α)>`. Under the aligned commutator convention,

`K=η(cd)=b1 N²w`,   `D=η(cd^-1)=K/(1−2α)`.                  (1)

The first equality is the cocycle commutator, the second follows from the actual central-kernel relation. The two central values are not generally equal.

The full normalizer is controlled as follows. A permutation normalizing the transitive P-action sends the basepoint to some xL; a left P translation returns it to L. Its remaining part is an automorphism of P stabilizing L. Thus `N_Sym(P/L)(P)` is generated by left P and Aut(P)_L, not the full regular Hol(P). After normalizing the endpoint containments, the only local C4 operation is uniform. For the modular P these basepoint-preserving automorphisms have form `g↦g^i t^j z^m, t↦t`, i≠0 mod3; for exponent-five P they have `g↦g^i t^j z^m, t↦t^d`, i,d≠0 mod5. The commutator relation determines the central scaling. Write `A=η(anti-g)=a0 w+a1 Nw+a2 N²w`, with a0≠0. A basepoint-preserving shear g↦gt^j fixes the active representation, the quotient generator w and B, while changing the Nw coefficient of A by a nonzero multiple of j b1; possible central corrections affect only N²w. A central shift g↦gz^m changes the N²w coefficient of A by a nonzero multiple of D. These operations successively remove a1,a2 without changing s. A uniform scalar normalizes a0=1. For p=5, t-scaling then normalizes b1=1 and does not change s. For p=3, t cannot be independently scaled: the relations g³=z and [g,t]=z force its coefficient to be one under an automorphism. The relation (anti-g)³=anti-z gives D=N²A and hence `b1=1−2α` after a0=1. Thus the listed operations leave exactly the residual parameter s, rather than assuming two independent unit and cocycle gauges.

The remaining transformations can be computed in the actual fiber F. A left translation g^r induces the top automorphism t↦tz^r and transports the cyclic generator by ρ_active(g)^r. The transformed anti-t displacement must therefore satisfy

`B_target+r D_target=(1+N)^r B_source` for p=5,
`B_target+r D_target=(1+N)^(-r) B_source` for p=3.

The resulting change to A can be removed by the preceding shear and central shift without changing B or s. Substituting (1) gives the following exact residual actions. A basepoint translation by g^r sends L to <tz^r> and moves w at the same time. For the p=5 active-first orientation,

`s ↦ s+r[1−(1−2α)^(-1)]`.                                   (2)

For the p=3 active-second orientation,

`s ↦ s−r[1+(1−2α)^(-1)]`.                                   (3)

For a basepoint-preserving automorphism with leading exponent i, use the inverse-automorphism convention for the induced orbit action. Since `(1+N)^i−1=iN+binom(i,2)N²`, its effect is

`s+1/2 ↦ i^(-1)(s+1/2)`.                                      (4)

The t-scaling cancels in this ratio. Left translations by t or central z give no further change after normalization, and the displayed forms of Aut(P)_L show that (2)–(4), together with the already used uniform scalars and shears, exhaust the actual normalizer action. These are actual coordinate-induced transformations; a general GL(M) change or arbitrary coboundary is not included.

For p=3, the translation coefficient in (3) vanishes exactly at α=1. Thus α=0 gives one orbit of s, while α=1 gives two: the aligned value `s=−1/2` and all other values under (4). For p=5, the coefficient in (2) vanishes exactly at α=0. Thus α=0 gives two s-orbits and α=1,2,4 each give one. These are respectively **three and five** nonregular classes. Every residual value occurs. Writing a=anti-g and b=anti-t, F has central generators c,d with [a,b]=cd; in the modular case a³=cd^-1 and b³=c³=d³=1, while in the exponent-five case a⁵=b⁵=c⁵=d⁵=1. These are the presentations of the order-p⁴ top fibers. The cocycle relations are the displayed central relations, the commutator `η([anti-g,anti-t])=NB`, and, in the modular case, `(anti-g)³=anti-z`; they are satisfied by the normalized A,B and central displacements above. In characteristic five the augmented unipotent 4×4 matrices have exponent five, so the exponent-five presentation adds no further relation. A noncentral top with nonzero g exponent has a nonzero w displacement, outside im(1−ρ); when only its t exponent is nonzero, it has a nonzero Nw displacement and trivial linear action. The nonidentity relevant central tops lie on the anti-central line and have nonzero displacement D. Thus every such cocycle satisfies the actual relevant-top test. The quotient map δ_(xL)↦ρ_active(x)w is well-defined because L fixes w and is onto because w is cyclic. The faithful-transitive converse supplies all-conjugate transversality, corefreeness, all normal-quotient strictness, simplicity and properness; those properties are not inferred merely from their orders.

## 3. Central survival and the Camina obstruction

**Central survival lemma.** Let a finite p-group B act transitively affinely on M, with linear part ρ and displacement η. For a central subgroup W define C=span{η(w):w∈W} and I=Σ_w(ρ(w)−1)M. If C⊆I, then W acts trivially affinely. Consequently, if W acts nontrivially, at least one η(w) survives in M/I.

Proof. Put J for the augmentation ideal of Fp[B]. Centrality gives (ρ(w)−1)η(g)=(ρ(g)−1)η(w). Since η(B)=M by transitivity, taking spans proves I=JC. If C⊆I then I⊆JI. Nilpotence of J yields I=0 and hence C=0. Both the linear and translation parts of every w are therefore trivial. ∎

**Camina theorem.** Let B be a finite nonabelian class-two p-group with elementary abelian nontrivial derived subgroup W=B′, and suppose [x,B]=W for every x outside Z(B). If B acts faithfully and transitively affinely on a cyclic Fp[B]-module M, then dim_Fp B/Z(B)=2 and dim_Fp W=1. In particular this holds for any regular affine action. No equality Z(B)=B′ is assumed.

Proof. Take I as in the lemma with W=B′. Faithfulness and W≠1 give nonzero C in V=M/I. The induced affine action is transitive, V is cyclic, and W acts trivially in its linear part. Its linear image is therefore abelian. The image R of Fp[B] in End(V) is a finite commutative local algebra with residue Fp. A cyclic vector identifies V with R: the map R→V is onto, and its kernel annihilates all of V, so is zero. Let 𝔪 be its maximal ideal. Write g:x↦u_g x+b_g, with u_g∈1+𝔪. The central translations C are annihilated by 𝔪. Transitivity lets us choose g0 with b0 a unit. Writing a_g=u_g−1, the commutator relation implies a_g b0−a0 b_g∈C; hence a_g=a0 b_g/b0+λ_g for λ_g∈C. It follows that

 [g,h] maps to ε(b_h)λ_g−ε(b_g)λ_h in C,

where ε:R→Fp is the residue. The functions g↦ε(b_g) and g↦λ_g are additive: for the second, subtract (a0/b0)b_gh from a_gh and use a_gλ_h=0. The individual forms need not vanish on Z(B); their wedge is the commutator form, which does vanish there and therefore descends to B/Z(B).

For every nonzero ξ∈C*, the ξ-projected commutator form on B/Z(B) is a wedge of two additive characters, so has rank at most two. It is nondegenerate: if x is noncentral, [x,B]=W, and W maps onto C. Also B/Z(B) is elementary abelian because [x^p,y]=[x,y]^p=1. Therefore its dimension is two, and Λ²(B/Z(B))→W is onto, so dim W=1. ∎

**Application to central quotients of a class-two Camina top.** Let P be as in the statement, and write W=Z(P)=P′. The elementary-abelian condition is automatic. For a noncentral x, if x^p were noncentral then [x^p,P]=W by the Camina property, but class two gives [x^p,P]=[x,P]^p=W^p, a proper subgroup of the nontrivial finite abelian p-group W. Therefore x^p is central and W^p=[x,P]^p=1. Thus W is elementary abelian of rank r, and P/W is elementary abelian. In the faithful-transitive setup, for an allowed central graph kernel T_α, the quotient B_α has central subgroup W, vector-space quotient V=P/W, and commutator map (I−2α)β, where β:Λ²V→W is the original commutator map. Put L=I−2α.

If L≠0, then [x,B_α]=LW for every x outside W, because β(x,V)=W. Thus Z(B_α)=W and B_α′=LW: B_α satisfies the theorem even if L is singular, but is not asserted special. When r>1, dim V≥4: β surjects W and dim V is even, since each nonzero scalar projection of β is nondegenerate. Therefore B_α cannot have a faithful transitive cyclic affine action. In the collision reduction, the regular affine image supplies faithfulness and transitivity. Its linear image is the active P-image because F projects onto that P-coordinate, so the cyclic P-module is also cyclic for B_α. Consequently only L=0, equivalently α=(1/2)I, remains. This is conditional on the central-kernel parameterization and regularity supplied by the prime-power-top reduction, not a reproof of those interfaces.

**Elimination of the abelian fiber using the actual active linear interface.** In the faithful-transitive reduction, the original linear action factors through one of the two P coordinates. For α=(1/2)I the group B_α is abelian. The stated cyclic regular-affine algebra theorem identifies it with U_e(Fp)=1+tFp[t]/(t^(e+1)), where e=log_p|P|. The inactive copy of W embeds in B_α: the graph kernel T_α has trivial intersection with that copy. That copy acts trivially in the linear representation. In the regular abelian cyclic model, M identifies with tFp[t]/(t^(e+1)) and B_α with U_e acting by multiplication. Its linear kernel is precisely 1+Fp t^e, of order p, because the annihilator of tFp[t]/(t^(e+1)) is Fp t^e. Hence the embedded inactive W has order at most p. When r>1 this is a contradiction. Together with the nonzero-L argument, all central-graph fibers are excluded for r>1, conditional on the full actual active-coordinate and cyclic-regular-affine interfaces.

## 4. Assembly and limitations

For an extraspecial group, a nonregular action can survive only in the two rank-one cases found in Section 2. Their three and five orbit counts add to the 120 regular-action classes. The canonical group's action on the simple factors of its socle is intrinsic, so nonregular-action classes cannot coincide with regular ones. The orders separate the two new families. The total is therefore 128.

For a class-two Camina top with $`Z(P)=P'`$, Section 3 excludes center rank greater than one, both for the nonabelian central quotients (including singular nonzero quotient commutator maps) and for the abelian quotient. Center rank one makes $`P`$ extraspecial, so the same census applies. No new isomorphism identifications are introduced in this last step.

The statements concern the displayed faithful-transitive anti-abelianization model. General non-Camina class-two groups, higher-class tops, arbitrary canonical groups, mixed socles and radicals remain outside this census. Even within the general transitive $`p`$-group reduction, the module and cocycle orbits remain to be solved.

The distinction between the quotient generator and the cocycle is essential. In the nonregular action, changing the point-stabilizer representative changes the generator simultaneously; the entire regular-action unit group is not available as an ambient gauge. Likewise, the two central cocycle values in Section 2 cannot be identified. Ignoring either point changes the orbit counts.

## Sources and evidence

This exposition combines the [faithful-transitive reduction](../sources/factor-permutation/radical-free-a5-transitive-pgroups.md), [extraspecial transitive census](../sources/factor-permutation/radical-free-a5-transitive-extraspecial.md), and [central-survival/Camina argument](../sources/factor-permutation/radical-free-a5-camina-tops.md). Each source records separate automated mathematical checks conditional on its upstream inputs. These new arguments are algebraic, not finite-enumeration claims; the earlier 88-class input retains its distinct finite-certificate scope. No human refereeing, formal verification or historical priority is asserted.
