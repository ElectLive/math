# Extension-field and subfield stabilizers over larger even fields

**Independently reviewed theorems for [0323:C0010](../foundations/research-C0010.md).** Let S=Sp₂ₘ(q), q=2^f, m≥3, and S≤M≤Aut(S) in the original primitive loop action. Write I for the identity stabilizer. The following actual geometric stabilizers are excluded under the subgroup and automorphism inputs of the [even-field stabilizer theorem](symplectic-even-maximal-stabilizers.md):

1. I∩S is the embedded subfield group Sp₂ₘ(r), q=rˢ, s≥2.
2. I∩S is the standard extension-field group Sp₂ₐ(qˢ).s, m=as, with s=2, a≥3 and q≥4.
3. The same extension-field group occurs with s an odd prime, a≥2 and gcd(a,s)=1, or a is a sum of integers greater than one each coprime to s.

These assertions are about the original stabilizer. Containment in a subfield or extension-field *overfactor* alone is insufficient. The [binary high-rank theorem](binary-symplectic-extension-spreads.md) independently covers every surviving orientation for q=2, m≥5. No completeness claim for larger fields is made here.

## Recognizing the original actions

The full group acts projectively by semilinear symplectic similitudes for m≥3. Since S is a nontrivial normal subgroup in a primitive faithful action, it is transitive and M=SI. If I preserves a set of points or subspaces D, the coset action maps M-equivariantly onto M·D=S·D. The [translation condition](binary-symplectic-extension-spreads.md#reduction-to-the-action-on-extension-field-structures) applies to relations on that orbit by pullback. In either coset convention the same criterion holds.

For the extension-field cases set E=F_(qˢ) and realize the alternating form as the trace from E. The last term of the derived series of I∩S is K=Sp₂ₐ(E) since this group is nonabelian simple and the quotient is cyclic. Hence I normalizes K. Its Fq-linear endomorphism centralizer consists precisely of the E-scalars: an endomorphism commuting with K preserves the image of u−1 for every E-transvection u, and these images are all the individual E-lines. Any additive map preserving every E-line is multiplication by one fixed scalar. Indeed comparing the two coordinates of the image of x+y gives the same multiplier on any two E-independent nonzero vectors, and a third vector compares dependent ones. Conversely E-scalars commute with K. Semilinear conjugation therefore normalizes the scalar algebra and permutes its lines. The original coset space thus maps to the S-orbit Ω of the standard spread D of E-lines, even when M contains field automorphisms. Field models below realize that same orbit because symplectic forms in the same E-dimension admit matching symplectic bases.

## The subfield group

Put J=I∩S=Sp₂ₘ(r). Let C be the set of projective points PG(2m−1,r) in PG(2m−1,q). Since I normalizes J, it preserves C. The lines occurring as images of u−1 for rank-one transvections u∈J are exactly C. Indeed rank over r and q is the same for a matrix over r, and J has a transvection centered at each r-rational point. Semilinear conjugation preserves rank and carries image lines to image lines. Below we construct an element of S moving C, so its stabilizer in M is proper and contains I. Maximality forces I=Stab_M(C). As S is transitive on M/I, the loop domain identifies with the S-orbit of C.

First, every t∈M has an orbit member D such that D∩tD is nonempty. Pick a projective point x. The pair (x,t(x)) is either equal, distinct orthogonal, or nonorthogonal. C contains representatives of all three types; S is transitive on ordered pairs of each type, by extension of the relevant symplectic partial bases. Choose D in the S-orbit of C containing x and t(x). Then t(x)∈D∩tD.

Next construct g∈S with C∩gC empty. Take a hyperbolic decomposition V=F_q^m⊕F_q^m and let B∈M_m(F_r) have irreducible characteristic polynomial of degree m. For each nonzero x∈F_r^m the vectors x,Bx are linearly independent over F_r. Choose α∈F_q\F_r such that A=1+αB is invertible. If m does not divide s, the polynomial of B has no root in F_q and every such α works. If m divides s, there are at most m forbidden α, while q−r≥r^m−r>m, so a choice exists. For nonzero x∈F_r^m, Ax is not proportional over F_q to a nonzero r-vector: in an r-basis beginning x,Bx, its first two coefficients are 1,α. The same proof applies to A^T; hence (A^T)^−1 likewise sends no r-rational projective point to one, since A^T maps the finite set of r-rational points disjointly from itself. Thus the symplectic element g=diag(A,(A^T)^−1) sends every rational projective point to a nonrational point (inspect either nonzero coordinate block). Hence C∩gC=∅.

The disjointness relation on translates of C is nonempty and invariant, and each element of M has a translate meeting its image. This contradicts the translation condition.

## Quadratic extension fields

Write s=2, E=F_(q²) and m=2a. On Ω take the nonempty relation of pairs with no entire E-line in common. Its nonemptiness and the failure of universal displacement are proved below.

## Separated spreads

For each construction below, we give a symplectic Fq-linear h such that for λ∈E\Fq and μ∈E the map hMλ−Mμh is invertible. Here Mλ denotes multiplication by λ on the original E-space. If a member L of D and a member hL′ of hD share an Fq-plane, take independent preimages x and λx in L′, λ∈E\Fq. Their images lie on the E-line L, so h(λx)=μh(x) for some μ∈E, contradicting invertibility. Thus D and hD have no common member.

We use trace-dual doubling. Let X be an E-space with nondegenerate Fq-bilinear pairing identifying X* with the Fq-dual and with Mλ self-adjoint. If P∈GL_Fq(X), let P* be its adjoint and put h=diag(P,(P*)⁻¹) on X⊕X*, with its hyperbolic alternating form. This h is symplectic. Moreover

P* ((P*)⁻¹ Mλ − Mμ (P*)⁻¹) P* = MλP*−P*Mμ = (PMλ−MμP)*.

Thus invertibility on X implies it also on X*. The E-action on the dual is the adjoint action, and the symplectic form is the trace of a nondegenerate alternating E-form: the E-linear dual identifies with the Fq-dual by composition with Tr(E/Fq). Consequently the resulting spread is in Ω.

### Odd a

Let K=F_{q^{2a}}, C=F_{q^a}, E=Fq²⊂K, and σ(x)=x^{q^a}. Since a is odd, σ generates Gal(K/C) and restricts to the nontrivial automorphism of E/Fq. Choose α∈K* with N_{K/C}(α)∉Fq*, possible because the norm is onto C* and C properly contains Fq. On X=K set P(x)=x+ασ(x). Its kernel is zero: a nonzero kernel vector would force N(α)=1. For λ∈E\Fq, μ∈E,

PMλ−MμP = M_{λ−μ}+M_{α(λ^σ−μ)}σ.

The coefficients cannot both vanish. If exactly one is zero, the map is invertible. If both are nonzero and the map has a nonzero kernel, taking K/C norms gives N(α)=N((λ−μ)/(λ^σ−μ)), which lies in Fq* because N_{K/C} restricted to E equals N_{E/Fq}. This contradicts the choice of α. Doubling X by its trace dual gives h.

### Even a

Let K=F_{q^a} contain E and take X=K² with E-action Mλ=diag(λ,λ^q). Pick A=[[u,v],[w,z]]∈GL₂(K) with all entries nonzero and uz/(vw)∉Fq; for example use [[c,1],[1,1]] with c∈K outside Fq. With the standard trace pairing Tr_{K/Fq}(x₁y₁+x₂y₂), the operators Mλ are self-adjoint. For λ∈E\Fq, μ∈E,

det(A Mλ−Mμ A) = uz N_{E/Fq}(λ−μ)−vw N_{E/Fq}(λ^q−μ).

The two norm terms cannot both vanish. If exactly one vanishes, the determinant is nonzero. If neither vanishes, determinant zero would force uz/(vw)∈Fq, contrary to choice. Therefore P=A satisfies the required invertibility. Doubling by the trace dual supplies h. This applies in particular to a=4; the statement assumes a≥3.

## A common member for every semilinear element

Let g be an invertible σ-semilinear symplectic similitude, where σ is an automorphism of Fq and B(gx,gy)=c B(x,y)^σ for c∈Fq*. If g stabilizes a totally isotropic Fq-plane U, choose D₀∈Ω containing U; then U is in both D₀ and gD₀. Every isotropic plane is a line of some spread in Ω, by Witt's lemma.

Otherwise, for every λ∈Fq* the additive kernel Kλ=ker(g−λ) has size at most q². To see this, let Fq0 be the fixed field of σ. Standard semilinear descent (equivalently, a minimal linear-dependence argument) shows that Fq0-independent vectors of Kλ are Fq-independent. For x,y∈Kλ, their pairings satisfy c B(x,y)^σ=λ²B(x,y). All nonzero solutions of this scalar equation form a single Fq0-line, so the restricted pairing, after scaling, is an alternating Fq0-valued form. If dim_Fq0 Kλ≥3, it contains a 2-dimensional isotropic Fq0-subspace. Its Fq-span is an isotropic g-stable plane, contradiction. Hence dim_Fq0 Kλ≤2 and |Kλ|≤q0²≤q².

We construct an isotropic plane U with U⊕gU totally isotropic. Starting with U=0, suppose dim U=j<2 and W=U⊕gU is totally isotropic. Put H=(g⁻¹U+U+gU)^⊥; its Fq-dimension n is at least 4a−3j. For w∈H, the extra condition B(w,gw)=0 ensures that w and gw are orthogonal to each other and to W. To make their images independent modulo W, avoid W, g⁻¹W, and (g−λ)⁻¹W for all λ∈Fq*. Although g−λ need not be Fq-linear, it is additive, so each nonempty fiber of its restriction over W has at most |Kλ| points. The total number of forbidden points is at most

q^{2j} [2+(q−1)q²].

Count the admissible zeros of B(w,gw) on H. In nf binary coordinates, its f coordinate functions are Boolean polynomials of degree at most 2, since g is F₂-linear and B is F₂-bilinear. The indicator that all f vanish is the product of their complements, a nonzero Boolean polynomial of degree at most 2f because it equals 1 at zero. A nonzero Boolean polynomial in N variables of degree at most d has support at least 2^{N−d}; this follows by induction on N, splitting into two restrictions and, when they differ, applying induction to their nonzero derivative. Thus the zero set has at least q^{n−2} points. For a≥3 and j≤1, n≥4a−3≥9, so the lower bound is at least q⁷, strictly exceeding q²[2+(q−1)q²]. Choose w outside the forbidden set. Repeating twice gives U and gU as required.

The two disjoint isotropic planes U and gU, with totally isotropic sum, occur together in one spread D₀∈Ω: take two independent E-lines in an E-Lagrangian and extend an isometry of their four-dimensional Fq-sum by Witt's lemma. Since U∈D₀, gU∈gD₀; by construction gU also belongs to D₀. Hence D₀ and gD₀ share a member. This contradicts the translation condition.

## Odd prime extension degrees

Let s be an odd prime, a>1 and gcd(a,s)=1. In the odd-a binomial construction above replace K by F_(q^(sa)), C by F_(q^a), and E by F_(q^s). The automorphism σ:x↦x^(q^a) generates Gal(K/C) and restricts to a generator of Gal(E/Fq). For z∈E its K/C norm is the E/Fq norm and belongs to Fq. Choose α with K/C norm outside Fq. The same kernel and adjoint argument gives a symplectic h with h Mλ−Mμ h invertible for all λ∈E outside Fq, μ∈E. Thus no E-line in hD intersects any E-line in D in Fq-dimension at least two. If a is a sum of such block sizes, take the orthogonal direct sum of these symplectic maps. For each common pair of scalars the difference is block diagonal with invertible blocks, giving the same conclusion, including for lines running across blocks. In particular all a≥2 are covered for odd prime s except possibly s=a=3: if s divides a≥5, use 2 and a−2.

For every semilinear symplectic similitude on the original Fq-space, the [nearly invariant isotropic space lemma](binary-symplectic-extension-spreads.md#a-nearly-invariant-isotropic-subspace) yields an isotropic s-space U with dim(U∩gU)≥s−1≥2. Every such U is a member of some conjugate spread by Witt's lemma. Hence the invariant relation of having no such two-dimensional intersection cannot satisfy universal displacement. This proves the claimed action exclusion.

The field and group classifications used here remain the pinned inputs of the even-field stabilizer theorem. The arguments are algebraic and use no new finite census. Three independent GPT-6.1 Terra reviewers accepted the three stated cases at exact source `5d481bb2f8feb2ccb271986c71cf313140e11e9f` under their cited original-action and geometric inputs. contributor 1, contributor 2 and contributor 3 checked subfield point recovery, extension-field recognition, dual doubling, norm determinants, the semilinear count and the prime-degree blocks. The semilinear reviewer freshly inspected Holt–Roney-Dougal (2005) Propositions 6.4 and 8.2, noting that the latter classifies maximal subfield groups at prime index while the conditional geometric argument here also works at composite index. The scalar and semilinear reviewers checked the cited nearly invariant space and translation arguments. No reviewer re-proved the full automorphism classification or the entire prior theorem chain. No computation was used.
