# Odd simple Bol loops of unbounded Fitting height

**Mira Cult**

**Continuation of [0323:C0010](../../claims/0010.md), with the exact-source reviews recorded below.** For every h≥0, the construction gives a finite simple proper odd left Bol loop whose canonical left multiplication group has Fitting height h+3, under the cited folder inputs. Fitting height is the minimum length of a normal series with nilpotent factors; it is distinct from derived length. The construction uses iterated regular wreath products and an affine exact factorization, not loop-table enumeration. Its endpoint is unboundedness, not an isomorphism census or exhaustive classification.

The exact-factorization folder, generated faithful group and properness interface is [C0002, Proposition 1.1](../foundations/C0002.md), at historical source [the source revision](https://github.com/Mira-Cult/math-wip/commit/9431ade99316d6bc62efb389492fef385b510b45), with the C0001 canonical-folder and simple-Moufang primitivity inputs specified there. The simplicity proof below uses the separately reviewed odd τ-normal strict-defect criterion at [the source revision](https://github.com/Mira-Cult/math-wip/commit/65a3e58df517df59656ab948ac9d122208f62c4a) in [odd-folder-radicals.md](odd-folder-radicals.md), rather than assuming a simple quotient is the whole loop. It generalizes the [reviewed Q_{p,q} group calculation](odd-stabilizer-alignment.md#the-known-simple-family-realizes-the-orbit-obstruction) at [the source revision](https://github.com/Mira-Cult/math-wip/commit/9d806247691956ef2dfb7a39ff32fe2934fde351); that source is context, not a review of the new construction.

## Odd monomial groups of increasing height

Fix p=7, q=29 and E=F_{7⁷}. The prime q has ord_q(7)=7, since 7⁷−1=6·29·4733 and 7 is not 1 modulo 29. Choose distinct primes r₁,…,r_h, all congruent to 1 modulo 7 and distinct from 7,q. They exist elementarily: given finitely many forbidden primes, take a=7 times their product. Every prime divisor ℓ of Φ₇(a)=1+a+⋯+a⁶ is new and different from 7; ord_ℓ(a)=7, so ℓ≡1 mod 7. Pick k_i∈F_{r_i}× of order 7.

Set U₀=1 and recursively define the regular wreath product

    U_i = C_{r_i} wr U_{i−1} = C_{r_i}^{U_{i−1}} ⋊ U_{i−1}.

Define an automorphism ψ_i of order 7 recursively: on U_{i−1} use ψ_{i−1}; on a base function b:U_{i−1}→C_{r_i}, set

    (ψ_i b)(u) = b(ψ_{i−1}^{−1}u)^{k_i}.

For U₀ the automorphism is identity; ψ₁ is the nontrivial power map k₁. Whenever U₀⋊<ψ₀> occurs, the bracket denotes a formal C7 acting trivially, not the trivial subgroup of Aut(U₀). The definition respects the regular translation action. Its seventh power is identity, and it is nontrivial for i≥1. Since the coinvariants of a regular permutation base are C_{r_i},

    U_i,ab ≅ C_{r_i}×U_{i−1,ab},

and ψ_i acts on each cyclic factor by the corresponding k_j. Thus ψ_i−1 is invertible on U_i,ab.

The action of U_{i−1}⋊<ψ_{i−1}> on the new base is faithful: an element uψ^j acts by a regular coordinate permutation followed by scalar k_i^j. Identity forces j=0 and then u=1. Since r_i divides none of the previous groups, the Fitting subgroup of U_i⋊<ψ_i> is precisely its r_i-base: any nilpotent normal subgroup centralizes the base in all other prime components, and the displayed action has trivial centralizer. Therefore

    h_F(U_i⋊<ψ_i>)=i+1.                                      (1)

For i=0 this says h_F(C7)=1; the same reasoning without ψ gives h_F(U_i)=i for i≥1.

## Monomial affine group and exact factorization

Put U=U_h, ψ=ψ_h, Q=C_q^U, and T=Q⋊U using the regular action. Let V=E^U as an F7-vector space. Q acts by independent q-th-root scalars on coordinates and U by the regular coordinate permutation. Each coordinate is an irreducible 7-dimensional F7 C_q-module, the coordinate modules are pairwise nonisomorphic for Q, and U acts transitively on them. Therefore V is a faithful irreducible F7 T-module.

Let φ apply field Frobenius a↦a⁷ to each coordinate and permute indices by ψ. Then φ normalizes T, induces ψ on U and the power map 7 plus index permutation on Q, and has order 7. In the special case h=0, the index permutation is trivial and φ is the field Frobenius. The group

    T_ab ≅ C_q × U_ab

has φ acting on its C_q factor by seventh power and on the others by k_i. Thus φ−1 is invertible on T_ab. For any 1≤i<7 and t∈T, the automorphism α=inn(t)φ^i has the same fixed-point-free action on T_ab. The subgroup [T,α] is normal in T; in T/[T,α], α acts trivially, so its abelianization is both a quotient of T_ab and fixed by α. It is trivial. As T is solvable, the quotient is trivial; hence

    [T,inn(t)φ^i]=T.                                         (2)

Set X=V⋊(T⋊<φ>). Equation (2) gives X′=V⋊T and X/X′≅C7. Let Y1=T⋊<φ>. Choose a φ-invariant F7-hyperplane W containing (φ−1)V and v∉W; it exists because a 7-element in characteristic 7 has nonzero fixed quotient. Put g=(v,φ) and Y0=⟨W,g⟩. Since the norm 1+φ+⋯+φ⁶=(φ−1)⁶, g⁷∈W and |Y0|=|V|. For 1≤i<7, every element w g^i has translation component congruent to i v mod W, whereas (1−φ^i)V⊆W, so it has no fixed point on V. Nonzero translations in W have none. Hence Y0 is regular on V and

    X=Y0Y1,  Y0∩Y1=1,  X′Y0=X′Y1=X.                         (3)

The action of T⋊<φ> on V is faithful: a trivial monomial transformation has trivial index permutation and all q-scalars trivial, while a nonzero φ power induces nontrivial Frobenius and hence cannot be canceled by scalar multiplication. Therefore C_X(V)=V and V is a minimal normal subgroup. Y1 is corefree by the faithful affine action. A nontrivial normal subgroup inside Y0 would meet V and contain V, impossible since |Y0|=|V| and Y0≠V. Thus Y0 is corefree too. By the cited exact-factorization interface the canonical faithful generated folder has

    G={(x,y)∈X²:xy∈X′},  H=G∩(Y0×Y1),
    K={(x,x⁻¹):x∈X},     τ(x,y)=(y,x).

The resulting loop has odd order |X|. Its canonical stabilizer has order |X′|>1, so the loop is nonassociative. Properness follows after the simplicity check below. The full multiplication group is not being identified with G.

## Simplicity without quotient-folder assumptions

Put M=V×V. As the affine complement acts faithfully, C_G(M)=M. The two V coordinates are pairwise nonisomorphic irreducible T²-modules, and |T| is prime to 7 because all the selected primes differ from 7. Every nonzero normal subgroup of G meets M; a τ-stable one therefore contains all M by semisimplicity and the coordinate swap.

Modulo M,

    G/M=(T×T)⋊<t>,  t=(φ,φ⁻¹),
    HM/M={ (φ^i,aφ⁻i) : a∈T, i∈F7 }.

Let 1≠N◁G be τ-stable. If its image Nbar modulo M contains an element with nonzero t exponent, equation (2), applied separately to the two coordinates, shows commutators with T×T generate T×T. Then Nbar is all of G/M and N=G. Thus for a proper N, Nbar≤T×T. Its two coordinate projections agree by τ-invariance; write this subgroup as R≤T. We do not assume Nbar=R×R. The displayed H image gives

    [G:HN]=[T:R].

If two diagonal-inverse section elements have equal image modulo N, their first coordinates differ by an element of V⋊R. Consequently

    |KN/N|≥[X:V⋊R]=7[T:R]>[G:HN].

The reviewed odd τ-stable-normal strict-defect criterion implies simplicity: because fixed points lift in this odd group, |KN/N|/[G:HN]=|C_N(τ)|/|H∩N|. No projection of K to a normal quotient is assumed to be a loop transversal.

For properness, the nontrivial normal subgroup X′×1 of G has its identity orbit contained in the section points indexed by Y1, a proper subset of X. Indeed (x,x⁻¹)∈(X′×1)H forces x⁻¹∈Y1. The faithful action makes this normal subgroup's orbit nontrivial; hence canonical LMlt is imprimitive. The C0001 simple-Moufang primitivity input used in C0002 Proposition 1.1(3) then excludes Moufang. This is the explicit properness interface, not an inference from solvability alone.

## Fitting height

In L=T⋊<φ>, the action of U⋊<φ> on Q is faithful: U acts by regular coordinate permutations and a nonzero φ power applies the nontrivial seventh-power scalar automorphism on each C_q. As q is new to U and 7, the same nilpotent-normal-centralizer argument as in (1) gives Fit(L)=Q. By (1),

    h_F(L)=h+2.

Also O_7(L)=1: a normal 7-subgroup centralizes the normal q-subgroup Q and hence lies in C_L(Q)=Q. In X=V⋊L the Fitting subgroup contains V; its non-7 components centralize V and are trivial because C_X(V)=V, while its 7-component has no nontrivial image in L. Thus Fit(X)=V and h_F(X)=h+3.

The canonical folder group G is a subgroup of X×X projecting onto X. Fitting height does not increase under subgroups or quotients of finite solvable groups, so h_F(G)=h_F(X)=h+3. As h is arbitrary this proves, subject to the stated inputs, unbounded Fitting height of canonical LMlt among finite simple proper odd Bol loops. It does not claim an exhaustion theorem or novelty. No computation, formal verification or fresh primary-source audit is claimed.

At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/feaf33e8b9f2725ac9b835a49dca95de4332171d), reviewers contributor 1, contributor 2 and contributor 3 independently accepted the full construction under the cited exact-factorization, canonical-folder, odd strict-defect and simple-Moufang primitivity interfaces. Their reviews covered the wreath automorphisms and faithful actions, fixed-point-free abelianization argument, affine regular factorization, every relevant τ-stable normal subgroup, properness interface and exact Fitting-height calculation. These are mathematical model reviews at that source, not fresh primary-source audits, computational tests or formal verification.


## General eligible odd inputs and intrinsic recovery

**Conditional construction for 0323-finite-simple-non-moufang-bol-loops:C0010, independently reviewed at the source recorded below.** Fix E=F_(7⁷) and its order-29 scalar subgroup. Let U be any finite odd solvable group with gcd(|U|,7·29)=1, equipped with ψ∈Aut(U) satisfying ψ⁷=1 and such that ψ−1 is bijective on U_ab. If U≠1 this forces ψ to have order seven; the trivial U is allowed with trivial ψ. The construction above, using this U instead of U_h and the specified hyperplane below, gives a finite simple proper odd left Bol loop L(U,ψ), under the same pinned exact-factorization and strict-defect interfaces. Its canonical left multiplication group determines U up to group isomorphism. An isomorphism of pairs (U,ψ)→(U′,ψ′) suffices for loop isomorphism. The converse claimed here is only that isomorphic output loops have U≅U′; no full isomorphism criterion for ψ or arbitrary-group encoding is asserted.

Use exactly the preceding definitions Q=C29^U, T=Q⋊U, V=E^U over F7, φ=Frob7 combined with the ψ-index permutation, X=V⋊(T⋊⟨φ⟩), and Y1=T⋊⟨φ⟩. Choose

    L(v)=Σ_(u∈U) Tr_(E/F7)(v_u),    W=ker L,

and choose v supported at the identity coordinate of U with entry e∈E of trace one. The finite-field trace is a nonzero F7-linear map, so such e exists, even though Tr(1)=0. Then L(v)=1, L is φ-invariant and (φ−1)V≤W. Define Y0=⟨W,(v,φ)⟩ as above. Changing e to any other trace-one element changes v by an element of W and leaves Y0 unchanged. The loop is the preceding exact-factorization loop for X=Y0Y1, of order |X|=7^(7|U|+1)·29^|U|·|U|.

Here is the complete check that the earlier construction proof applies under these broader hypotheses, without extending its special Fitting-height formula. The independent Q-coordinate modules are still pairwise nonisomorphic irreducible seven-dimensional F7 modules, and U acts transitively on the coordinates by its regular action. Thus V is faithful and irreducible for T. The regular-base coinvariant computation gives T_ab=C29×U_ab; every nontrivial power of φ has no fixed point there. For α=inn(t)φ^i, 1≤i≤6, the normal subgroup [T,α] has quotient whose abelianization is both a quotient of T_ab and fixed by α, hence trivial. Solvability of T makes this quotient trivial, proving equation (2) for every eligible U. Faithfulness of T⋊⟨φ⟩ on V follows from the same scalar-versus-Frobenius argument. Therefore X′=V⋊T and C_X(V)=V.

The specified trace hyperplane meets every hypothesis of the affine exact-factorization proof: (φ−1)V≤W and v∉W give g⁷∈W, |Y0|=|V| and fixed-point-free action of each w g^i with i≠0; Y0 is regular. Irreducibility and C_X(V)=V imply every nontrivial normal subgroup of X meets and then contains V. Thus both Y0 and Y1 are core-free, and X′Y0=X′Y1=X. The exact-factorization interface yields precisely the faithful generated canonical G,H,K,τ displayed above, with τ swapping the coordinates.

The simplicity proof also applies without a wreath hypothesis. Since |T| is prime to seven, M=V×V consists of two nonisomorphic irreducible T² modules and C_G(M)=M. A nontrivial normal subgroup N of G meets M: otherwise it centralizes M and is contained in M, a contradiction. If N is τ-stable, semisimplicity and coordinate interchange force M≤N. The earlier nonzero-φ-exponent argument uses only equation (2), so it makes such N equal G. Otherwise N/M≤T² with equal coordinate projections R, and the displayed H image gives [G:HN]=[T:R] while |KN/N|≥7[T:R]. The pinned odd strict-defect criterion proves simplicity, without assuming a quotient loop or that N/M=R². The properness proof using the nontrivial intransitive normal subgroup X′×1 is unchanged and invokes the same simple-Moufang primitivity input. Thus these are actual simple proper loops, conditional on the stated prior interfaces.

For intrinsic recovery, let ̄G=G/M=(T×T)⋊C7. Its normal Q² has centralizer exactly Q²: a nonidentity regular U-permutation acts nontrivially on its coordinate set, and a nonzero φ power acts by a nontrivial seventh-power scalar on its C29 values, so these cannot combine to centralize Q². A normal 7-subgroup of ̄G centralizes its normal 29-subgroup Q² and must therefore be trivial. Hence M=O7(G) is characteristic. Moreover O29(̄G)=Q², since the remaining quotient (U×U)⋊C7 has order prime to 29. In that quotient the largest normal subgroup of order prime to seven is exactly U×U: it contains the normal U² and has trivial image in the C7 quotient. Consequently the fully characteristic extraction is

    O_(7′)((G/O7(G))/O29(G/O7(G))) ≅ U×U.                  (4)

Here O_(7′)(A) means the largest normal subgroup of A whose order is prime to seven; products of such normal subgroups again have order prime to seven, so the subgroup is well-defined and characteristic. This is not a quotient of loops. Every loop isomorphism induces an isomorphism of canonical left multiplication groups and hence of the extracted groups in (4).

For completeness, direct-square cancellation for finite groups has a short elementary proof. If A×A≅B×B, then for every finite group F the nonnegative integers |Hom(F,A)| and |Hom(F,B)| have equal squares and are equal. Sorting homomorphisms by kernel gives

    |Hom(F,A)|=Σ_(N normal in F) |Inj(F/N,A)|.

Induction on |F|, subtracting the terms N≠1, shows |Inj(F,A)|=|Inj(F,B)| for every F. Taking F=A gives an embedding A→B. Equal direct-square orders give |A|=|B|, so A≅B. Applying this to (4) recovers U from the loop, without a separate group-decomposition theorem.

Finally, an isomorphism θ:U→U′ with θψ=ψ′θ reindexes Q,V and the regular U actions, intertwines φ, preserves the trace-sum hyperplane and the identity-coordinate v, and carries (X,Y0,Y1) to its primed data. The canonical exact-factorization interface therefore gives L(U,ψ)≅L(U′,ψ′). The stated group-isomorphism necessity and pair-isomorphism sufficiency deliberately leave a gap: an arbitrary U may admit no eligible ψ, and different eligible automorphisms on isomorphic U are not proved to give isomorphic loops. This construction is not a classification of all odd or all solvable-LMlt Bol loops.

The old construction and all its pinned review statements remain unchanged; the preceding argument owns this new general-input/recovery extension. Preliminary development was by contributor 4, with the project supplying the general odd-solvable scope and elementary cancellation proof. No computation, new external theorem or fresh primary-source audit is used. At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/e9cf89aa90a6e3ecd245458839c3030a4a70daa1), reviewers contributor 5, contributor 3 and contributor 6 independently accepted this extension under the pinned exact-factorization, canonical-folder, odd strict-defect and simple-Moufang primitivity interfaces. They checked the general-input adaptation, trace hyperplane, simplicity/properness, characteristic recovery and finite-group cancellation. These were mathematical model reviews, without new computation, formal verification or fresh primary-source audits. Their acceptance covers the limited isomorphism scope stated above; the strengthening below is a separate proposal.


## Exact pair recovery from the pointed canonical group

**Conditional strengthening for 0323-finite-simple-non-moufang-bol-loops:C0010, independently reviewed at the exact source recorded below.** For eligible pairs in the preceding construction, under its pinned theorem inputs,

    L(U,ψ) ≅ L(U′,ψ′)  if and only if
    there is θ:U→U′ with θψ=ψ′θ.                            (5)

Here all isomorphisms of loops preserve the identity, and the recovered data are their canonical left multiplication group together with its identity stabilizer. This is a classification of this constructed family by eligible pairs; it does not assert exhaustion of odd simple Bol loops. The reverse direction was proved at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e9cf89aa90a6e3ecd245458839c3030a4a70daa1). We prove the forward direction by recovering the full pair from (G,H), with no chosen complement or quotient loop.

Let M=O7(G)=V1×V2 as in (4). The conjugation action of G/M on M is faithful. Its only minimal normal subgroups are V1 and V2: these are the two nonisomorphic irreducible T² summands, and every nontrivial normal subgroup of G meets M. The actual stabilizer satisfies H∩M=W×0, because Y0∩V=W and Y1∩V=0. Since dim_F7 W=7|U|−1>0, V1 is the unique minimal normal subgroup meeting H nontrivially. Thus (G,H) distinguishes and preserves the labels V1,V2, including when U=1.

Use the natural action of G/M on M to define

    C1=C_(G/M)(V2),    A1=O29(C1),    U1=C1/A1.

Faithfulness of T⋊⟨φ⟩ on V gives C1=T×1. Indeed a second coordinate centralizes V2 precisely when its image in X/V is trivial; the fiber condition defining G then forces the first φ exponent to be zero. Since |U| is prime to 29, A1=Q×1 and U1≅U. These objects are intrinsic to the pointed group (G,H), and an isomorphism of pointed groups carries them to the corresponding primed objects.

The image Hbar=HM/M acts on C1 by conjugation. Its concrete form is

    Hbar={ (φ^i,aφ^−i) : a∈T, i∈F7 }.

Consequently its image B in Aut(C1) is exactly ⟨φ⟩. This image is cyclic of order seven, since nonzero φ powers act nontrivially on Q. The coinvariant group

    A1/[A1,C1] ≅ C29

is canonical: the regular U-permutation identifies all coordinate generators of Q, and Q itself is abelian. The automorphism φ acts on this quotient by seventh power. Because ord_29(7)=7, exactly one element of B acts by seventh power on this quotient, namely φ. The power-map description does not choose a generator of C29, so it is invariant under every group isomorphism. It canonically orients the recovered order-seven action, rather than leaving an unspecified power or inner conjugacy.

The induced automorphism on U1=C1/A1 is therefore exactly ψ. Any loop isomorphism conjugates its left translations and identity stabilizer to those of the other loop, inducing an isomorphism of pointed canonical groups. The preceding extraction then gives θ:U→U′ satisfying θψ=ψ′θ. Together with the proved reindexing construction this establishes (5) under the stated earlier interfaces.

The proposed argument was supplied by contributor 7 and assembled by the project. It requires no new computation or external theorem. The three reviews of [the source revision](https://github.com/Mira-Cult/math-wip/commit/e9cf89aa90a6e3ecd245458839c3030a4a70daa1) above cover only the earlier construction. At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/6c55b3a3e2f5522f58366522213b1147e48612a5), reviewers contributor 5, contributor 3 and contributor 6 separately accepted this full pair-isomorphism equivalence, conditional on that reviewed construction and its pinned folder interfaces. Each checked the intrinsic module labels, actual centralizer and conjugation image, unique seventh-power orientation, the U=1 case and the induced pair map. None ran a computation, performed a fresh primary-source audit or claimed formal verification. The result classifies the constructed family by eligible pairs only.


## Seven-coordinate inputs and faithful recovery below the characteristic

**Conditional continuation of 0323-finite-simple-non-moufang-bol-loops:C0010, independently reviewed at the source recorded below.** For every prime p≡1 mod 7 with p≠29, the preceding construction admits an isomorphism-preserving and isomorphism-reflecting assignment from all finite p-groups of nilpotency class strictly less than p, of arbitrary exponent, to finite simple proper odd Bol loops. The assignment is described below. Its output is a subfamily of the reviewed eligible-pair family, not an exhaustion of odd simple loops or an encoding theorem for arbitrary finite groups. The separate Lie-ring reflection lemma does not require nilpotence.

### Eligibility for every odd solvable input of coprime order

Let P be any finite odd solvable group with gcd(|P|,7·29)=1 and write A=P/P′ additively. Define

    U(P)=ker(P⁷→A),    (x0,…,x6)↦Σ_j xjP′,

and let ψ cyclically shift the seven coordinates, using (ψx)_j=x_(j−1) with indices modulo seven. The map defining the kernel is a homomorphism because its target is abelian. Each coordinate projection U(P)→P is onto: place x and x⁻¹ in two distinct coordinates. Its order is |U(P)|=|P|⁷/|A|.

We have U(P)′=(P′)⁷. Inclusion from left to right is immediate. For the reverse, fix three distinct coordinates i,j,l. Elements supported as (x,x⁻¹) in (i,j) and (y,y⁻¹) in (i,l) lie in U(P); their commutator is supported only at i and equals [x,y] there. These generate P′ independently at every coordinate. Therefore

    U(P)_ab ≅ ker(A⁷→A) ≅ A⁶.

A ψ-fixed tuple in this abelianization is constant, with value a satisfying 7a=0, hence zero. Thus ψ−1 is bijective on U(P)_ab. All other eligibility hypotheses follow from those on P. In particular the reviewed construction at [the source revision](https://github.com/Mira-Cult/math-wip/commit/e9cf89aa90a6e3ecd245458839c3030a4a70daa1) gives an actual simple proper loop

    B(P)=L(U(P),ψ),

of order 7^(7m+1)·29^m·m, where m=|P|⁷/|P_ab|. An isomorphism P→P̃ acts coordinatewise on U and commutes with ψ, so it induces an isomorphism B(P)→B(P̃). Conversely the reviewed exact pair recovery at [the source revision](https://github.com/Mira-Cult/math-wip/commit/6c55b3a3e2f5522f58366522213b1147e48612a5) shows that a loop isomorphism determines an isomorphism of the pairs (U(P),ψ) and (U(P̃),ψ). This last conclusion does not by itself recover P for unrestricted inputs.

Two immediate invariants clarify that gap. The fixed subgroup C_U(ψ) consists of constant tuples x with x⁷∈P′, equivalently x∈P′, and is isomorphic to P′. Also U_ab≅P_ab⁶ determines P_ab: the Hom-count cancellation proof used above works for any fixed positive direct-power exponent, replacing squares by that exponent. These two invariants generally omit the extension data. The following argument recovers those data for the stated class<p inputs.

### A reflection lemma for finite Lie rings

Let L and L̃ be finite Lie rings whose additive groups are p-groups, where p≡1 mod 7. Put D=[L,L] and define the Lie ring

    V(L)=ker(L⁷→L/D)

using the coordinate-sum map, with ψ the same cyclic shift. If (V(L),ψ) and (V(L̃),ψ) are isomorphic as Lie rings with automorphism, then L≅L̃. No nilpotence or centrality of D is assumed in this lemma.

First V(L)′=D⁷: the additive two-support tuples (x,−x) and (y,−y), with their compensating coordinates distinct, have bracket supported at just their common coordinate. These brackets generate D in every coordinate. Choose e so that p^e annihilates both additive groups. A primitive seventh root ζ in Fp lifts to one in Z/p^e: at each lifting step the derivative 7ζ⁶ is a unit, giving a unique correction. For 1≤i≤6, ζ^i−1 is a unit, as is seven. The commuting projection operators

    e_i = (1/7) Σ_(j=0)^6 ζ^(−ij) ψ^j,    i∈Z/7,

give the intrinsic eigenspace decomposition, without any assumption that the additive groups are elementary abelian.

The ζ^i-eigenspace for i≠0 is additively isomorphic to the whole L, by

    x ↦ (x,ζ^(−i)x,…,ζ^(−6i)x).

The tuple sums to zero and lies in V(L). Its intersection with D⁷ is precisely the embedded copy of D. The fixed eigenspace is a copy of D, since a constant tuple x lies in V(L) exactly when 7x∈D, equivalently x∈D. Coordinatewise brackets add eigenvalue degrees and agree with the original bracket on these identifications.

Consequently a pair isomorphism yields additive isomorphisms F_i:L→L̃ for i=1,…,6 and G_j:D→D̃ for j∈Z/7, with F_i|D=G_i, satisfying

    [F_i x,F_j y]_L̃ = G_(i+j)[x,y]_L    (i,j≠0).          (6)

Here and below subscripts on G and eigenvalue indices are read modulo seven, and compositions are read right to left. Define T_i=F_1^−1 F_i and C_j=G_2^−1 G_j. Comparing (6) with its i=j=1 instance gives

    [T_i x,y]_L = C_(i+1)[x,y]_L = [x,T_i y]_L.             (7)

Applying (7) to the two inputs in either order and then using (6) shows, since brackets generate D,

    C_(i+j)=C_(i+1) C_(j+1),    C_2=1,    i,j≠0.           (8)

The products commute wherever used, because evaluating [T_i x,T_j y] in the two orders gives the same map on every bracket. Write C=C_3. Taking (i,j)=(2,2),(2,3),(2,4),(2,5),(2,6) gives C_4=C², C_5=C³, C_6=C⁴, C_0=C⁵, C_1=C⁶. Taking (i,j)=(3,6) then gives 1=C_2=C_4 C_0=C⁷. In particular C_1=C^−1.

On the embedded D we now have T_2|D=G_1^−1G_2=C, while (7) says [T_2x,y]=C[x,y]. Define F=F_1 T_2^−1, an additive isomorphism L→L̃. Its restriction to D is G_1 C^−1. Its bracket action is

    [Fx,Fy]_L̃ = G_2 C^−2[x,y]_L
               = G_1 C^−1[x,y]_L = F([x,y]_L),

where G_2=G_1 C. Thus F is a Lie-ring isomorphism. This correction is essential: T_2 itself need not preserve the bracket, and the maps F_1|D and G_2 need not initially agree. When D=0, F_1 already is an additive isomorphism of abelian Lie rings and the conclusion is immediate. The argument preserves the actual additive inclusion D≤L, so it does not discard nonsplit additive extensions or power torsion.

### Transfer and scope of the group-isomorphism criterion

For finite p-groups of class<p, the Lazard correspondence supplies mutually inverse group and Lie-ring operations at arbitrary exponent. The precise source is [the additional arbitrary-exponent Lazard interface](../foundations/references.md#lazard-bch-interface), Glauberman (2007), Theorem 4.8, printed p.439, with the finite specialization stated in its introduction. Take π to be the primes other than p in that theorem; class<p ensures that every required denominator is invertible. The rational-word operations commute with homomorphisms and products. They preserve kernels and identify the two abelianizations, since the operations coincide on abelian objects and the transformations are inverse. Therefore the Lie ring of U(P) is exactly V(L(P)), including the coordinate-shift automorphism.

Suppose P and P̃ are finite p-groups of class<p, for a fixed p≡1 mod 7, p≠29. An isomorphism B(P)≅B(P̃) gives the pair isomorphism by the reviewed theorem (5), then a Lie-pair isomorphism by Lazard. The reflection lemma gives L(P)≅L(P̃), and the inverse correspondence gives P≅P̃. The coordinatewise construction proves the converse. Thus, under the stated construction and source inputs,

    B(P)≅B(P̃)  if and only if  P≅P̃.                       (9)

This covers arbitrary order and exponent within class<p, including all class-two 43-groups and abelian inputs. It does not extend the group conclusion to class≥p: the general Lie-ring lemma alone supplies no correspondence there. Nor does the general eligibility argument for all coprime odd solvable P establish reflection for those unrestricted inputs. The earlier uniform matrix-pair encoding remains a separate reviewed result; no computational complexity bound or literature novelty is claimed here.

Development of the seven-coordinate eligibility and exponent-43 class-two step was by the project and contributor 8; contributor 4 supplied the arbitrary-exponent correction, and the project observed and checked its general Lie-ring scope. The project and that agent directly inspected the cited arbitrary-exponent theorem. No computation or formal verification is used. At exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/0d040b63256de50bd57933bcf324de46519ba643), reviewers contributor 5, contributor 3 and contributor 6 independently accepted the complete section under the previously reviewed construction/pair-recovery inputs and the cited Lazard theorem. All checked the general eligibility, full additive eigenspaces, bracket identities, the correction F=F_1 T_2^−1 and the class<p group transfer. Each also directly inspected Glauberman’s primary PDF introduction and Theorem 4.8 on printed p.439, confirming the arbitrary-exponent scope. No computation or formal verification was performed, and none reverified the theorem’s full external proof. Their acceptance does not extend group reflection to class≥p or arbitrary odd solvable inputs.
