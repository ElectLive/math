# A cyclic affine obstruction for extraspecial groups

**Independently reviewed manuscript-local theorem under pinned inputs.** This continues 0323-finite-simple-non-moufang-bol-loops:C0010 (dependency `claims/C0010.md` not included in this update). Let p be an odd prime, let B be an extraspecial p-group of order p^(2m+1), and let B act affinely and transitively on a finite cyclic Fp[B]-module M. If a generator z of Z(B) has no fixed point in M, then m≤1. In particular, a regular affine action of B on a cyclic Fp[B]-module is impossible for m≥2. No assumption on dim M or faithfulness of the linear action is needed.

Write the affine action as g:x↦ρ(g)x+η(g), and put D=ρ(z)−1 and c=η(z). Since z is central, DM is invariant under every ρ(g), so the affine action descends to V=M/DM. The action on V is transitive, V is cyclic as an Fp[B]-module, and z has identity linear part there. Its translation c̄ is nonzero: if c∈DM, then Dx=−c has a solution and z fixes x. Centrality implies every linear operator ρ(g) fixes c̄.

The linear image on V is abelian because B′=⟨z⟩ acts trivially. Let R be the image of Fp[B] in End(V). It is a finite commutative local Fp-algebra with residue field Fp: the augmentation ideal of Fp[B] is nilpotent and its image is the maximal ideal 𝔪 of R. Choose a cyclic vector v. The R-module map R→V, r↦rv, is surjective and injective: an element killing v kills all of V because R is commutative, and the image algebra acts faithfully. Identify V with R. Thus g acts as

    x ↦ u_g x+b_g,       u_g∈1+𝔪,  b_g∈R.

The central element z translates by nonzero c̄, and 𝔪 c̄=0, since each u_g fixes c̄ and the u_g generate R. Transitivity supplies g0 for which b0=b_g0 is a unit: for example, choose an element sending 0 to 1. Write a_g=u_g−1 and a0=a_g0. Because every commutator is a power of z, comparing gh and hg gives

    a_g b_h−a_h b_g = ω(g,h)c̄,

up to the chosen global commutator sign, where ω is the nondegenerate alternating commutator form on B/Z(B). Here no extra unit occurs: every u_g fixes c̄. Taking h=g0 yields a_g b0−a0 b_g=λ_g b0 c̄ for some λ_g∈Fp. Division by the unit b0 gives

    a_g = a0 b_g/b0 + λ_g c̄.

Consequently

    ω(g,h)=λ_g ε(b_h)−λ_h ε(b_g),

where ε:R→Fp is the residue map; cancellation of c̄ means comparison of scalar coefficients in its one-dimensional Fp span. The functions f(g)=ε(b_g) and λ(g)=λ_g are additive: the affine product gives b_gh=b_g+u_g b_h, hence f(gh)=f(g)+f(h), while a_gh=a_g+a_h+a_g a_h and 𝔪 c̄=0 imply λ_gh=λ_g+λ_h after subtracting a0 b_gh/b0. Both vanish on z because a_z=0 and ε(c̄)=0: the latter follows from c̄≠0 and 𝔪 c̄=0 unless 𝔪=0, in which case commutators are trivial and the nonzero central translation is impossible. Thus f and λ descend to linear forms on B/Z(B). Their wedge has rank at most two, whereas ω has rank 2m. Therefore m≤1.

## Higher-rank extraspecial regular tops

Use the exact regular-top model and the reviewed reduction in [the odd prime-power top source](../manuscripts/radical-free-a5-prime-power-top.md) at `d17efc105793622b54eb899ccac67919a555a9f8`, including its pinned faithful-folder, A5 subgroup/full-strip, normal-quotient, actual-isomorphism and properness inputs. Let P be extraspecial of order p^(2m+1), m≥2 and p odd. Put e=2m+1, n=p^e, S=A5^P⋊P with P acting regularly, G the anti-abelianization fiber in S², and τ the swap. Then a finite simple nonassociative left Bol loop with this exact canonical G and τ exists **if and only if p=5, m=2, and P has exponent 25**. Such loops have order `5^5·60^(5^5)`. This is an existence/exclusion theorem for these higher-rank extraspecial tops; it does not count the loop-isomorphism classes in the surviving case.

Indeed, the reduction first forces p∈{3,5}, gives a cyclic e-dimensional module and an affine action of the top fiber F, and then forces that image to be regular. Write W=P′=Z(P)≅Cp additively. Its kernel is

`T_α={(αw,(1−α)w):w∈W}`, α∈Fp,

and the regular image is B_α=F/T_α, of order p^e. If α≠1/2, its commutator form is the nonzero scalar (1−2α) times that of P: the center is exactly W, the derived subgroup is W, and the quotient by the center is the same elementary abelian symplectic space. Thus B_α is extraspecial of the same rank m. Its linear module is cyclic as an Fp[B_α]-module because its action is exactly the affine image's linear action. The preceding theorem rules this out for m≥2. Necessarily α=1/2 and B=B_α is abelian.

By the regular-abelian cyclic-module theorem in [the abelian-top source](../manuscripts/radical-free-a5-abelian-top.md#the-regular-cyclic-module-algebra), reviewed at `7eb6be15aa8854884eafc6f71e825d50eb149aba`, the regular affine action is the principal-unit action on `J=tFp[t]/(t^(e+1))` after identifying its nilpotent algebra. Thus B≅U_e(Fp)=1+J and its linear action is multiplication on J. The reduction requires that the inactive one-sided copy of P′ act trivially linearly; this extra constraint is retained below.

For completeness, odd extraspecial P has exponent p or p². The p-th power of every element is central, and the class-two identity `(xy)^p=x^p y^p` holds because commutators have order p and p divides p(p−1)/2. If P has exponent p, then F and its quotient B do too. But U_e contains 1+t of order exceeding p when e≥p, whereas e=2m+1≥5≥p. This excludes the exponent-p case for p=3,5 and m≥2.

If P has exponent p², the power map P/P′→P′ is a nonzero linear functional. For `(x,y)∈F`, the powers obey `y^p=(x^p)^-1`, so F^p is the anti-diagonal copy of W. The kernel T_(1/2) is diag(W), and oddness makes its intersection with the anti-diagonal trivial. Consequently B is abelian of exponent p² with |B^p|=p. The image of either one-sided copy of W is the same subgroup B^p: all three are nonzero lines in the one-dimensional central quotient W²/diag(W).

Frobenius in the principal-unit algebra gives `|U_e(Fp)^p|=p^floor(e/p)`, since `(1+Σ a_i t^i)^p=1+Σ a_i t^(ip)`. Thus |B^p|=p forces `p≤e≤2p−1`. In that range B^p corresponds exactly to `1+Fp·t^p`. On the other hand, the kernel of multiplication on J is exactly `1+Fp·t^e`, since the annihilator of J inside J is Fp·t^e. The inactive P′ has image B^p and must act trivially linearly. These two lines must therefore coincide, forcing e=p. Since e=2m+1≥5 and p∈{3,5}, this leaves p=e=5 and m=2.

The surviving case exists without a computational search. For an extraspecial P of order 5^5 and exponent 25, set B=F/diag(W). The preceding power calculation shows that B is abelian of order 5^5 with |B^5|=5, hence `B≅C25×C5³≅U_5(F5)`. Choose any such group isomorphism. On J=tF5[t]/(t^6), the action

`u:x↦u(1+x)−1`

is regular; its linear module is cyclic, generated by t under multiplication by 1+t. The characteristic subgroup B^5 corresponds to `1+F5·t^5`, which acts trivially linearly. Pull the action back from B to F. The kernel of the first-coordinate projection F→P is the inactive second copy of W, whose image in B is B^5. Therefore the linear action factors through the first P-coordinate, exactly as required for p=5. Choose a cyclic vector to produce an actual regular-coordinate quotient map. The only elements in the affine kernel are diag(W); none of its nonidentity elements is relevant, since central (w,w) is inverse-conjugate only if w²=1. Every other element of the regular affine group has no fixed point. The exact relevant-top collision criterion is satisfied. The reviewed uniform converse then constructs the faithful simple proper Bol folder and proves all normal-quotient and properness conditions.

## Evidence and remaining obligation

The cyclic-affine obstruction is elementary; no computation or external classification of affine groups is used. GPT-6.1 Terra agents `model reviewer` and `model reviewer` checked its derivation during drafting, including the quotient by DM and the wedge calculation. These drafting checks are not independent review of this exact combined source. The complete exact-source review is recorded below. The higher-rank conclusion depends on the pinned regular-top and regular-abelian reduction inputs. It does not settle the admissible-data isomorphism orbits for the surviving exponent-25 group, all rank-one extraspecial tops, or general permutation groups and radicals. The next obligation is to solve those surviving orbits under the actual coordinate normalizer. No permanent claim ID is allocated; C0010 remains partial.

## Independent mathematical review

GPT-6.1 Terra reviewers `model reviewer`, `model reviewer`, and `model reviewer` independently accepted this complete source at exact revision `417e94ec31bdba48c0ed4f6b18b34e69f13621f7`, conditional on the pinned prime-power regular-top and regular-abelian cyclic-module theorems and their recorded folder, subgroup, normal-quotient and properness inputs. They checked the cyclic quotient M/DM and nonzero central translation, the commutative local image algebra and additive scalar wedge argument, the extraspecial/abelian central-quotient split, exponent-p and exponent-p² restrictions, the exact Frobenius power count, the inactive P′ linear-kernel condition forcing e=p, and the surviving exponent-25 construction. This acceptance covers the uniform cyclic-affine obstruction and the stated higher-rank extraspecial-top existence/exclusion theorem. It does not count the surviving isomorphism orbits. No new computation, primary-source audit or reproof of upstream classifications was performed. These are independent model mathematical reviews, not human or formal certification or GitHub approval.
