# When do two quotient directions have commuting lifts?

**Mira Cult**

The [tilted Heisenberg family](README.md#a-construction-over-any-finite-field-containing-a-primitive-pth-root) has no Sylow subloop at any nonzero tilt. That does not mean every pair of independent quotient directions fails to have commuting lifts. The theorem below characterizes commutativity in the loop itself, not commutativity of the marked permutations.

Let $`p,\ell`$ be distinct odd primes and let $`q`$ be a power of $`\ell`$ such that $`\mathbb F_q`$ has an element $`\zeta`$ of order $`p`$. On $`A=\mathbb F_q^p`$, with coordinates indexed by $`j\in\mathbb F_p`$, put

```math
Xe_j=e_{j+1},\qquad Ye_j=\zeta^j e_j,\qquad Je_j=e_{-j}.
```

Write $`A^+,A^-`$ for the two eigenspaces of $`J`$, and $`r=\dim A^-=(p-1)/2`$. For $`x=(a,b)\in\mathbb F_p^2`$ put $`S_x=\zeta^{ab/2}X^aY^b`$, with exponents in $`\mathbb F_p`$. In the affine marking group $`A\rtimes\langle X,Y\rangle`$, use the automorphism induced by $`J`$ and all of its inverted marks. The loop $`Q_v`$ is based at the actual stabilizer $`H_v=v(A^+\rtimes\langle\zeta I\rangle)(-v)`$ for $`v\in A^-`$. Sharp transitivity and the quotient $`\mathbb F_p^2`$ are proved in the linked construction.

**Theorem.** For each ordered independent pair $`x,y\in\mathbb F_p^2`$, there is a linear hyperplane $`T_{xy}`$ in $`A^-`$ with the following properties.

1. Commuting ordered pairs of native lifts of $`x,y`$ exist exactly when $`v\in T_{xy}`$. There are then exactly $`q^{r+1}`$ pairs.
2. At zero tilt each such pair lies in exactly one $`p^2`$-subloop, giving all $`q^{r+1}`$ sections. No nonzero tilt has a $`p^2`$-subloop. Nevertheless, for every $`p\ge5`$ some nonzero tilts admit commuting lift pairs.
3. For each nonzero determinant, there are $`r`$ ordered bases whose hyperplanes intersect only at zero. For every nonzero tilt at least a $`1/r`$ fraction of the ordered bases of each prescribed determinant have no commuting pair of lifts.

## The actual affine lifting equation

Let B=⟨X,Y⟩. The affine flat v+A⁺ realizes the required G/H_v point: the stabilizer in B of the linear subspace A⁺ is exactly ⟨ζI⟩. Indeed Z^cX^aY^b takes the J-fixed e_0 to a scalar multiple of e_a, forcing a=0, and fixing A⁺ setwise then forces b=0 by e_1+e_{−1}. Here Z=ζI. Thus equality of two flat images is equality of true loop elements. For each x all its marks are (u,S_x) with u∈S_{x/2}A⁻; the involution condition S_xJu=−u follows by conjugating J by S_{x/2}. Each mark gives one lift (sharp transitivity).

Write a=(u,S_x), b=(t,S_y), x=(x₁,x₂), y=(y₁,y₂). Let λ=ζ^{(x₂y₁−x₁y₂)/2}; then S_xS_y=λS_{x+y}, S_yS_x=λ^{-1}S_{x+y}. The two terminal flats after ab and ba have the same direction. Project their difference of origins by S_{−(x+y)} and then π₋=(1−J)/2. Native commutation is **equivalent** to


```math
L_{xy}(u,t)+(\lambda-\lambda^{-1})v=0,\qquad
L_{xy}(u,t)=\pi_- S_{-(x+y)}\!\bigl((1-S_y)u+(S_x-1)t\bigr).
```


The domain is an F_q-space of dimension 2r; the scalar multiplying v is nonzero. Hence the set of permissible tilts is the image of L (up to the nonzero scalar), and all nonempty lift counts equal |ker L|. It remains to compute this kernel, not merely exhibit part of it.

## Computing the entire zero-tilt kernel

Suppose lifts commute at 0. With composition rightmost first put g=(ba)^{-1}ab. Its affine linear part is a **nonidentity central scalar**; g∈H_0 since the based products agree. Thus α(g)=g, and g has a unique fixed vector w∈A, necessarily in A⁺. Now α(g)=(ab)g(ab)^{-1} since a,b are inverted. Consequently ab commutes with g, so it fixes w; ba does as well, since ab=ba g. Move the origin to w; α is still the old linear J involution because w∈A⁺. Denote the translated vector parts by U,T and the old linear parts by A₁=S_x,B₁=S_y. Then U+A₁T=T+B₁U=0, so A₁B₁U=U, while A₁JU=−U.

First take x=(1,0), y=(0,d). A₁B₁=XY^d. A fixed vector of XY^d has coordinates U_j=ζ^{d j(j−1)/2}U_0 for all j. It is therefore invariant under j↦1−j, or equivalently under XJ. As the characteristic is odd, the simultaneous XJ-negation forces U=0, hence T=0. The original two marks both fix w: explicitly they are ((1−S_x)w,S_x), ((1−S_y)w,S_y). Conversely these two inverted marks commute at base 0 for every w∈A⁺, since their commutator lies in H_0. Two different w do not give the same pair: their difference would be fixed by S_x,S_y and their nonidentity scalar commutator. The same conjugate stabilizer B^w=wB(−w) gives a section, and any genuine p²-section through both marks must have this stable B^w by the cited section description (alternatively, their projections generate B, and w is unique).

To transfer this calculation to every ordered basis of determinant d, use the explicitly invertible linear operators


```math
Ce_j=\zeta^{j^2/2} e_j,\qquad
Fe_j=\sum_{i\in\mathbb F_p}\zeta^{ij}e_i.
```


Fourier inversion needs only that p is invertible, not a square root of p in F_q. Both commute with J, normalize B and fix its center pointwise. They send an inverted S_x to the unique inverted representative of its transformed role. The induced actions on roles are respectively (a,b)↦(a,b+a) and (a,b)↦(−b,a); these generate SL₂(F_p) by elementary row operations. Therefore all ordered pairs of a fixed nonzero determinant are conjugate in this physical family, with basepoints transported as v↦Cv,Fv. In particular every ker L has exactly |A⁺|=q^{r+1} elements, so rank L=r−1. This proves the first two statements.

## Why a bad basis always exists

The intersection of all T_xy with det(x,y)=d is C- and F-invariant because maps of the marking data send ordered commuting pairs at Q_v to actual ordered commuting pairs at Q_{Cv}, Q_{Fv}. Their action on A⁻ is irreducible over F_q. On the odd basis e_j−e_{−j} (1≤j≤r), C has the distinct eigenvalues ζ^{j²/2}, so its invariant subspaces are spanned by subsets of these basis vectors (use the polynomial projections). Every coefficient of F(e_j−e_{−j}) in that basis is ζ^{ij}−ζ^{-ij}≠0 for 1≤i,j≤r. There is no nonzero proper common invariant subspace. As every T itself is proper, the intersection is zero; elementary linear algebra selects r independent defining normals. This argument includes r=1, where T={0}.

For the quantitative fraction, fix such r test pairs and a nonzero v. Choose a uniform role transformation in SL₂(F_p), and a word in C,F lifting it. The r transformed hyperplanes still have zero intersection, so at least one of the transformed r pairs forbids all commuting lifts at v. Each individual transformed pair is uniform among all ordered bases of the given determinant. Taking expectations gives r·Pr[no commuting lifts]≥1. No assumption that a given v is uniform in its linear orbit is made.

## Controls and scope

The [finite checker](code/check_physical_commuting_lifts.py) builds marks and tests equality of the two actual affine flat images. It checks ranks on native pairs and implements exhaustive fixed-tilt comparisons at the two smallest tested primes, including a nonzero permissible tilt at p=5 where merely searching for one commuting pair cannot detect the missing Hall section. It is not an exhaustive check in every characteristic. The family, isotope, full section count, and nonzero-tilt Hall obstruction are antecedents, not claimed as new here. The hyperplanes, exact local multiplicity, two-role test and fixed-determinant fraction are the present theorem; no claim of historical priority or human peer review.

From this directory run:

```sh
python3 -B code/check_physical_commuting_lifts.py
python3 -B code/review_two_role_commutator_layers.py
```

An independent AI mathematical review accepted the local theorem conditional on the antecedent family. The reviewer contributed to that earlier family, not to this theorem. The separate checker computes defining functionals from the raw affine difference matrices, without the proof's odd-space projection; it uses the original finite-field arithmetic module. The tests include the field of order 81, exhaustive projective tilts there, and both actual commuting pairs and absent pairs. [Author output](evidence/two-lifts.out) · [Independent output](evidence/two-role-commutator-hostile.out). This is not human refereeing or formal verification.

Mira Cult directed the research; OpenAI models contributed to the mathematics, exposition and checking. Exact model versions were not verified.
