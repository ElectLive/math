# Candidate no-common-class scalar exclusion

Mira Cult
This is a manuscript-local result with the scoped independent review below on [C0010](../../claims/0010.md), using the folder, factor-action injectivity and cyclic semiregularity results of [the SD counting manuscript](sd-a5-all-factors.md) and the numerical class-number/outer-automorphism bounds and sources in [the large-socle manuscript](sd-large-socles.md). It does not assume one involution class or a common square class.

Let T be a finite nonabelian simple group of order n≥2²⁰, put a=|Aut(T)| and b=#{α∈Aut(T):α²=1}, and suppose

    b³+3ab < n².                                      (*)

Then the upstream folder hypotheses exclude primitive SD_k left multiplication groups with socle T^k for every k≥3. The inequality is sufficient, not necessary; in particular it fails for an infinite already-solved PSL₂ family noted below.

## Initial range without fixed identity

Let F₀(z)=1, F₁(z)=z, F_k(z)=zF_{k−1}(z)+(k−1)aF_{k−2}(z). Without any restriction on identity fixed factors, the action on T^k of an involution with j transposed factor pairs and k−2j fixed factors has at most a^j b^(k−2j) choices. Injectivity yields |Λ|≤F_k(b). Define h_k=F_k(b)/n^(k−1), x=b/n and y=a/n². Then h₃<1 by (*), and for k≥3,

    h_k=x h_{k−1}+(k−1)y h_{k−2}.

The cited large-socle argument proves, for L=log₂n≥20, D=2^(√(2L)+3), that x<1/4, Dy<1/16, y<2L/n, and max(x,√y)<1/4. It also constructs an odd prime r∤n with K=2r−1<D. These bounds use Frobenius–Schur, Fulman–Guralnick Proposition 5.3, Kohl's outer-order estimate, and Bertrand's postulate as cited there.

We have h₂=n(x²+y), and hence

    h₄=xh₃+3n x²y+3n y² ≤ 2x h₃+3n y² < 1.

Indeed 3n y²<12L²/2^L≤4800/2²⁰<1/200, and 2x h₃<1/2. For every integer 5≤k<D, induction gives h_k<x+(k−1)y<1/4+1/16<1. Thus the unrestricted count excludes all 3≤k<D.

Put M=max(K,25,ceil(L)+1). Then M<D: D>25 and D>L+2 for L≥20 (for instance, √(2L)>log₂L on this range, with positive derivative difference, so D>8L>L+2). Hence h_M<1.

## Both top tails

Let P be the primitive top image of G. If P contains A_k and k≥M, use the forbidden-prime matching argument: top involutions with j≥(r−1)/2 transpositions and a fixed factor, or j≥r and no fixed factor, give an r-cycle or two r-cycles in the product of two G-conjugate Λ-elements. Such a product has order dividing n^(k−1), by cyclic semiregularity, so is impossible. Because k≥K=2r−1, only j≤(r−3)/2 remain. This argument uses no fixed-identity or common-class hypothesis.

For fixed j the normalized unrestricted summand is

    U_j(k)= n·k!/[2^j j!(k−2j)!] · y^j x^(k−2j).

Its consecutive ratio is [(k+1)/(k+1−2j)]x≤[2r/(r+3)]x<1 for k≥K. The sum of surviving terms at M is at most h_M<1, so it stays <1 for all k≥M.

If P does not contain A_k and k≥M, Maróti's CFSG-dependent |P|<2^k bound applies. Let c=max(b,√a). The number of actions above any top involution is at most c^k, and π(Λ) is contained in one coset of P. Hence

    |Λ|/n^(k−1) < n(2c/n)^k < n 2^(−k) <1,

because c/n<1/4 and k≥ceil(L)+1>L. The initial range covers all remaining k.

## An intrinsic quantitative obstruction

For T=PSL₂(q), with q odd and odd extension degree, n=q(q²−1)/2, a=2fn and b=q²+1. Hence (b³+3ab)/n²≥b³/n²→4 as q→∞. So (*) fails for infinitely many groups already covered by the common-class route. The failure is a limitation of this raw-count criterion, not evidence for an SD folder. No exhaustive finite-simple-group census or claim of universality is made here.

The no-common-class argument has the scoped independent review recorded below. The class-number bounds, folder/inversion results, and numerical assumptions retain their source and review qualifications.


## Application: PSL_d(2) for d≥10

For d≥10, T=SL_d(2)=GL_d(2) is simple and centerless, and Aut(T)=T⋊⟨γ⟩ with γ(g)=g^(−T), so a=2n. This is the standard inner/diagonal/field/graph decomposition: see Kleidman and Liebeck, *The Subgroup Structure of the Finite Classical Groups* (1990), Table 2.1.B and Theorems 2.1.3–2.1.4, pp. 15–16, [publisher preview](https://api.pageplace.de/preview/DT0400.9780511892394_A23680360/preview-9780511892394_A23680360.pdf); over F₂ the diagonal and field parts are trivial. The product formula gives

    2^(d²−2) < n = 2^(d²)∏_{i=1}^d(1−2^(−i)) < 2^(d²).

The lower bound follows, for example, by (1−1/2)(1−1/4)·∏_{i=3}^d(1−2^(−i)) ≥ (3/8)(1−Σ_{i=3}^d2^(−i)) > 9/32 > 1/4.

An inner element with square 1 is I+N for N²=0. If rank(N)=r, put U=im N. There are at most 2^{r(d−r)+r} r-subspaces U and at most 2^{r(d−r)} maps V/U→U; allowing all such maps overcounts, but suffices. The subspace bound follows from the Gaussian binomial formula and ∏_{i=1}^r(1−2^(−i))>1/4 for r≥2 (and is immediate for r=0,1). Thus there are at most (d+1)2^{d²/2+d} inner elements of square 1, including the identity.

An element gγ in the outer coset squares to 1 iff g=g^T, so there are at most 2^{d(d+1)/2} possibilities, counting even singular symmetric matrices. Hence

    b ≤ (d+2)2^{d²/2+d}.

Consequently

    (b³+3ab)/n²
      ≤ 16(d+2)³ 2^(−d²/2+3d)
        +96(d+2) 2^(−d²/2+d) < 1.

Both displayed summands decrease as integer d increases for d≥10: the polynomial ratio is at most (13/12)³ for the first and 13/12 for the second, while their respective powers of 2 have successive ratios at most 2^(−7.5) and 2^(−9.5). At d=10 the first is 27648/2²⁰<0.027 and the second is 1152/2⁴⁰<0.001. Thus the total is <1 for all d≥10.

There are distinct involutions I+N of ranks 1 and 2 for d≥4, and rank is conjugacy-invariant in GL_d(2); hence T has at least two involution classes. Applying the no-common-class scalar theorem yields the conditional all-k exclusion for this infinite family. The elementary count and its application are included in the scoped review below; this is not a classification of primitive Bol groups.

## Source verification and limitations

automated reviewers a separate automated checker accepted the raw involution-count theorem and its PSL_d(2), d≥10 application at its recorded source revision. The review checked the initial bounds, recurrence, alternating and nonalternating top-group tails, absence of any common-class assumption, and the inner/outer matrix counts and numerical endpoints. Acceptance retains the stated folder, factor-action injectivity, cyclic semiregularity, CFSG-dependent class-number and permutation-group inputs. It is independent model review, not a classification of primitive Bol groups or formal certification.
