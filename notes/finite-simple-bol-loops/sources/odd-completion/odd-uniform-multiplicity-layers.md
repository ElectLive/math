# Exact elementary-layer lifts of uniform inverted multitransversals

Mira Cult
, continuing [0323:C0010](../../claims/0010.md). The inherited odd-folder inputs include the full-inverted-set and odd-involution lifting results at the recorded source revision and their source application at the recorded source revision, as recorded in the all-defect source. This extends the exact all-defect criterion of [odd-elementary-layer-all-defects](odd-elementary-layer-all-defects.md) at the recorded source revision. It treats arbitrary positive integral multiplicity μ; it is a recursive recognition interface for fixed finite extension data, not a classification, a proof of bounded complexity, or an assertion that any multitransversal defines a quotient loop.

Let p be an odd prime, V a finite Fp-space, L a finite group of odd order with involution θ, ρ:L→GL(V), S²=1 on V with Sρ(l)=ρ(θl)S, and normalized cochains c:L²→V and η:L→V satisfying the extension and involution identities in the cited source. They define an odd group G=V×_c L with involution τ. Let K={g∈G:τ(g)=g⁻¹}; Kbar={l∈L:θ(l)=l⁻¹} is its full image by coprime involution lifting. Choose J≤L and J-stable W≤V. A subgroup H≤G projecting onto J with H∩V=W is given by a single global normalized cochain f:J→V/W satisfying

f(jk)=f(j)+ρ(j)f(k)+c(j,k) mod W.

Set δ=dim V_+−dim W, which may be positive, zero or negative, and n_−=dim V_−. For every l∈Kbar choose a solution v_l of

(1+ρ(l)S)v_l=−ρ(l)η(l)−c(l,θl),

and put N_l=ker(1+ρ(l)S). Each K-fiber over l is v_l+N_l and dim N_l=n_−: the corresponding outside involution is conjugate to τ in the finite odd group extension.

For each left coset $`aJ\subseteq L`$, put B_a=Kbar∩aJ, W_a=ρ(a)W, Q_a=V/W_a. For l=aj∈B_a let

z_l=v_l−c(a,j)−ρ(a)f(j) mod W_a,
 D_l=(N_l+W_a)/W_a,       h_l=dim(N_l∩W_a).

These offsets are well-defined independently of representatives of f(j). The H-cosets in π⁻¹(aJ) are parametrized by Q_a. Each l-fiber contributes exactly p^{h_l} inverted elements to each H-coset in the affine subspace z_l+D_l and zero elsewhere. Thus, for a positive integer μ, K meets EVERY left H-coset exactly μ times if and only if, for every aJ,

Σ_{l∈B_a} p^{h_l} 1_{z_l+D_l}(x)=μ    for every x∈Q_a.      (1)

In particular every l-fiber is counted with its actual kernel multiplicity; neither injectivity nor disjointness is assumed. The left side is an affine incidence-vector sum.

The Fourier form of (1) needs only the dual space of Q_a. Let ζ be a primitive pth root of unity and let W_a^⊥≤V* be the annihilator. Fourier inversion gives the equivalent conditions

|B_a|=μ p^δ,                                                   (2)
 Σ_{l∈B_a: ν(N_l)=0} ζ^{ν(z_l)}=0     for every 0≠ν∈W_a^⊥.  (3)

Indeed the Fourier transform of the weighted affine fiber equals p^{h_l+dim D_l}ζ^{ν(z_l)}=p^{n_−}ζ^{ν(z_l)} if ν annihilates N_l, and zero otherwise. Equation (2) is the zero-frequency coefficient, since dim Q_a=n_−+δ; (3) is every nonzero frequency. It is well-defined on cosets because ν annihilates W_a. For prime p, the only rational linear dependence among 1,ζ,…,ζ^{p−1} is their sum, so (3) is equivalently the integer condition that, for every nonzero ν, the counts of selected l with ν(N_l)=0 and ν(z_l)=r are equal for all r∈Fp. Empty selections satisfy this balance. Thus no complex-number computation or iteration over elements of G is needed: calculate the N_l, their annihilators and the incidence ranks/offset residue counts in the quotient and its dual. The number of quotient cosets, fibers and dual frequencies can still grow exponentially; this is not a uniform complexity bound.

The quotient multiplicity is exactly

μ_bar=μ p^δ.                                                    (4)

In particular if δ<0, existence forces p^{−δ} to divide μ. Conversely, a quotient full-inverted multitransversal of multiplicity μ_bar and an extension/cochain f satisfying the nonzero-frequency balances lift to an actual μ-fold transversal. Multiplicity alone is not sufficient: equations (3) retain the correlations between the affine fibers and the single global f. Iterating (4) along a selected chain of τ-stable elementary normal layers gives a recursive interface, with cohomology classes and incidence balances at every stage; it does not bound the length of the chain, the intermediate groups, or the possible multiplicities.

The same μ holds for every conjugate of H, and this equivalence needs a proof beyond the μ=1 disjointness argument. In an odd group, every element of K is g⁻¹τ(g); consequently, for x∈G,

x⁻¹Kx = K c_x,       c_x=τ(x)⁻¹x∈K.

The full inverted set is twisted: c_x K c_x=K, so K c_x=c_x⁻¹K is a left translate of K. Conjugating H-cosets and then left-translating K preserves the constant intersection count μ. Thus checking (1), equivalently (2)–(3), for H suffices for all conjugates. No quotient-folder operation is used.

At μ=1, every nonempty fiber must have h_l=0 and the affine fibers partition Q_a, recovering the reviewed all-defect theorem when δ is positive. When μ>1, overlaps and h_l>0 may occur, and (3) is the exact replacement for pairwise disjointness. Section changes s′(l)=b(l)s(l) act by the actual cochain gauge laws

c′(l,m)=c(l,m)+b(l)+ρ(l)b(m)−b(lm),
 η′(l)=η(l)+Sb(l)−b(θl),
 f′(j)=f(j)−b(j) mod W,    v′_l=v_l−b(l).

All z_l in one aJ receive the common shift −b(a), and (3) is multiplied by one common pth root. A change of solution v_l by N_l leaves its contribution unchanged whenever ν(N_l)=0. Therefore (1)–(4) are independent of section, fiber-basepoint and coset-representative choices.

This is a multitransversal theorem, not by itself a Bol-folder sufficiency statement for μ>1. At μ=1, impose the separate core and generation conditions and, where desired, the strict-defect simplicity criterion under their reviewed hypotheses. For the group extension, involution, stabilizer and chosen layer, exact isomorphism uses the γ,α,u cochain identities of the all-defect theorem, with α a linear isomorphism over the same p. These maps transport the incidence and Fourier conditions. No statement is made that all odd simple Bol loops are generated by a bounded collection of such layers or that quotient multiplicities classify them.

## The first two involution-chief interfaces in every odd simple envelope

Let Q be a finite simple proper odd Bol loop with canonical (G,H,K,τ). Use the reviewed odd solvability, full-inverted set, strict-defect and G=HG′, C_G(τ)≤G′ inputs, from [the derived-envelope source](odd-folder-radicals.md#derived-envelope-constraints-on-the-fixed-stabilizer), independently, and the exact arbitrary-multiplicity interface above at the recorded source revision. No projected inverted subset below is assumed to define a loop.

For a τ-stable normal subgroup L define μ_L=|C_L(τ)|/|H∩L|, the integral multiplicity of the full inverted set in the projected H-cosets of G/L. The reviewed strict-defect criterion gives μ_L>1 for every 1<L<G, while μ_1=μ_G=1. A τ-chief series means a maximal series of subgroups normal in G and stable under τ. Choose any such series of G. Let N be its maximal proper term and M the term immediately preceding N. Since G is solvable, the quotient G/N is elementary abelian with no proper nonzero τ-stable subspace and τ acts by inversion on the abelianization, so G/N=C_p for an odd prime p. Since G=HG′ and C_G(τ)≤G′, the image of H in G/N is all of C_p, and the full inverted set there has exact multiplicity μ_N=p. Moreover M≠1: the reviewed derived-length≥3 exclusion forces the τ-chief length to be at least 3. Thus μ_M>1 by strict defect.

Put V=N/M, an elementary abelian ℓ-group irreducible under the induced action of (G/N)⋊<τ>. Let J=G/N=C_p, σ=τ|V, W=(H∩N)M/M ≤V and δ=dim V_+−dim W. W is J-invariant because H surjects onto J. The reviewed multiplicity formula gives

p=μ_N=μ_M ℓ^δ.                                               (1)

Consequently if ℓ≠p then δ≤0 and μ_M=p ℓ^{−δ}; if ℓ=p then δ≤1, with μ_M=p^{1−δ}>1.

If ℓ≠p, J acts nontrivially on V, and W<V, then necessarily

V=W ⊕ σ(W),    W≠0,    dim W=dim V_+,    δ=0,  μ_M=p.     (2)

This gives an actual paired module at the first coprime layer below the maximal normal quotient, under precisely those two displayed hypotheses. Indeed if W=0, δ≤0 forces V_+=0, so σ=−I. The compatibility σaσ=a⁻¹ for a∈J then gives a=a⁻¹; odd order implies that J acts trivially, contrary to hypothesis. Thus W≠0. Both W+σW and W∩σW are σ- and J-stable. Irreducibility of V for J⋊<σ> forces W+σW=V and W∩σW=0, because W is proper. The involution swaps the summands, proving (2). If 0<U<W were J-stable, then U+σU would be a proper nonzero σ- and J-stable subspace, contradiction; W is J-irreducible. This does not assert W and σW are nonisomorphic.

All remaining cases are explicit interfaces rather than silently discarded. If ℓ≠p and W=0, (1) forces σ=−I and J acts trivially. If ℓ≠p and W=V, then δ=−dim V_- and μ_M=p ℓ^{dim V_-}. If ℓ=p, the normal p-subgroup J acts trivially on irreducible V in characteristic p; since σ has order 2, V is one-dimensional with σ=±1. W is 0 or V, but W=0, σ=+1 would give μ_M=1, contrary to M≠1 and strict defect. The three remaining combinations have (W,σ,μ_M)=(0,−,p),(V,+,p),(V,−,p²).

This is a necessary restriction on the first two steps in every exact layer-extension construction, not a finite classification of the later layers or a sufficient admissibility test. In particular the W=V branch is not excluded, and neither actual stabilizer cochain nor full K-fiber incidence equations may be dropped. It shows a forced paired layer only when the stabilizer shadow is proper and the coprime quotient action is nontrivial; known unbounded derived-length and Fitting-height examples rule out a universal bounded-layer search. No computation is claimed; independent reviews are recorded below.

### The coprime full-shadow branch actually occurs

The W=V alternative cannot be excluded by corefreeness or strict defect. Take the reviewed simple proper cross-extraspecial loop in [the cross-extraspecial source](odd-cross-extraspecial.md), with p=3,q=13, G′=D=P₃×P₁₃ and G/D=<a₃>×<a₁₃>. Its stabilizer contains a₃z₃ and a₁₃z₁₃, and τ inverts both torus images. The construction, corefreeness and simplicity were independently; the explicit non-Moufang witness was independently.

Set N=D⋊<a₁₃>, the inverse image of <a₁₃> in G/D, and M=D. Both are τ-stable and normal in G, and the two prime-index factors give a valid top-two segment of a τ-chief series:

G/N≅C₃,    V=N/M≅C₁₃.

The stabilizer element a₁₃z₁₃ lies in H∩N and maps to a₁₃ in V, so W=(H∩N)M/M=V. On V the involution is inversion, and therefore δ=dim V_+−dim W=−1. The multiplicities are μ_N=3 and μ_M=39, agreeing with p=μ_M·13^{−1}. These are actual projected stabilizer and inverted-set multiplicities from the reviewed folder, not assumptions that the projected set is a loop transversal.

This example also pinpoints the failed core argument. W=V means the image of H∩N in N/M fills V; it does not say that an actual normal complement <a₁₃> lies in H. Indeed H contains the twisted element a₁₃z₁₃, while the central factor z₁₃ belongs to M and is absent from H. Corefreeness holds in the original group, and the full strict-defect test was proved in the source. Hence a universal top-two-layer classification must retain this full-shadow extension branch alongside the forced-pair branch; strict simplicity does not eliminate it.

### Independent review of the first-two-layer restriction

## Full-shadow compression and monolithic reinsertion

Independently reviewed continuation of 0323:C0010 under the pinned inputs. These are reductions for odd canonical envelopes using the full-inverted-set and strict-defect interfaces of [the odd source](odd-folder-radicals.md) at the recorded source revision, the elementary cochain interface in [the all-defect source](odd-elementary-layer-all-defects.md) at the recorded source revision, and the arbitrary-multiplicity theorem above. They do not assert that an inverted multitransversal on a quotient is a loop, nor give an unrestricted classification.

### Exact compression for an arbitrary odd normal block

Let P be finite of odd order with involution θ, B◁P θ-stable, L=P/B, and J≤L. Put H=π⁻¹(J), and let K_P,K_L be the complete θ-inverted sets in P and L respectively. Each element of K_L has exactly [B:C_B(θ)] lifts in K_P. To see this, lift the corresponding outside involution through odd B. Any two outside involutions of P⋊<θ> are P-conjugate, and B is normal, so their B-fixed groups have equal order. The B-conjugacy orbit of a lifted outside involution is exactly its fiber and has size [B:C_B(θ)].

H-cosets biject with J-cosets, so K_P is an exact μ_P-fold transversal to H iff K_L is an exact μ_L-fold transversal to J and

μ_P=μ_L [B:C_B(θ)].                                        (1)

The assertion also holds for all conjugates of these stabilizers, by applying the same argument to each conjugate. No elementary, abelian, split, or normal-complement hypothesis on B is required. For an actual G and τ-stable normal M≤N, the projected full-shadow condition is N/M≤HM/M, equivalently HN=HM; then one can compress the entire block N/M at once by (1). For B elementary, (1) is the W=B instance of the reviewed uniform-multiplicity interface, whose nonzero-frequency incidence conditions are empty. General B gives the same exact conclusion without choosing its chief series.

There is a canonical maximal block in every quotient state (P,J,θ). Let C=Core_P(J) and put B=C∩θ(C). It is the unique largest θ-stable normal subgroup of P contained in J. On quotienting by B, the new core is C/B and its intersection with its θ-image is 1. Thus every intermediate state admits a canonical θ-core-pruned skeleton, and its discarded full-shadow kernel can be restored by an odd group extension; its inverted-set admissibility changes exactly by (1). This does not alone decide whether the final original stabilizer is core-free or its loop simple: those properties must be reinserted with the actual extension graph. The reviewed cross-extraspecial loop (construction the recorded source revision) supplies the concrete obstruction to forgetting that graph: a projected C13 full-shadow block is represented in H by a13 z13 and can disappear under compression, while replacing that twisted lift by the pure τ-inverted torus element would immediately violate the original transversal.

### Exact reinsertion for a monolithic minimal layer

Let G be an odd candidate with unique minimal nontrivial normal subgroup V, where 1<V<G, V is elementary abelian of characteristic p and τ-stable. Put P=G/V, θ the induced involution, J=HV/V, W=H∩V, δ=dim V_+−dim W. Every nontrivial G-normal subgroup contains V. Thus inverse image induces a bijection between normal R◁P and nontrivial normal T◁G, and τ-stability corresponds to θ-stability. Coprime fixed-point lifting and the exact stabilizer sequence give

|C_T(τ)|=p^{dim V_+}|C_R(θ)|,
    |H∩T|=p^{dim W}|J∩R|.                                     (2)

Consequently the full strict-defect condition is equivalent to the quotient-normal family of inequalities

p^δ |C_R(θ)| > |J∩R|  for every proper θ-stable R◁P.      (3)

R=1 is included and gives δ>0. Under that condition W<V. Corefreeness is then automatic: every nontrivial normal subgroup of G, and in particular a nontrivial stabilizer core, contains V, which H does not contain. This replaces all strict-defect and core computations in G by quotient-normal data. The reviewed odd strict-defect criterion can be applied once the original K transversal and generation have also been verified.

Constructively, use the reviewed exact elementary extension/involution cochains (c,η), module (V,σ), actual J-stable W and a single global stabilizer cochain f:J→V/W, along with its exact affine incidence equations. They reinsert all the information lost when full projected core blocks were compressed. The monolith hypothesis on G is a separate condition; e.g. irreducible V with faithful P-action is sufficient, but is not asserted necessary. Quotienting by B=Core_P(J)∩θCore_P(J) and applying (1) reduces the recognition of the P-level full-inverted multitransversal to its pruned skeleton. The cochain f on all of J, the extension itself, and the inequality (3) must still be checked before declaring the G-folder simple; one cannot classify f by a quotient B-compression alone. Exact loop isomorphisms must still quotient these data by the reviewed extension gauges and compatible automorphisms.

This is a genuine exact reduction of one exhaustiveness branch, not yet its solution: arbitrary odd quotient groups P, compatible modules, cohomology classes and incidence balances remain unclassified, and groups with several minimal normals are outside the monolithic reduction. It gives no uniform bound on the pruned skeleton or the number of nonfull layers. Known unbounded-derived-length/Fitting-height odd families also rule out assuming a universal bounded chain length, but they do not by themselves prove the number of core-pruned nonfull stages is unbounded.

### Independent review of the full-shadow compression and monolithic reinsertion

## Publication and verification scope

This public source preserves the mathematical argument at the revision recorded in the source crosswalk. Its conclusions retain every stated hypothesis and dependency. Source-specific automated mathematical checks are not human referee acceptance, formal verification or a literature-priority audit. Computational checks, where cited, have only their stated finite scope.

All checked the actual kernel weights and overlapping affine images, constant Fourier coefficients, signed-defect zero frequency and divisibility, prime-cyclotomic residue balance, the translated-K proof for every conjugate of H, and the section/basepoint gauges. No computation or fresh primary-source audit was performed. Their scope is exact recognition and recursive lifting for the stated finite extension data, not a loop construction at multiplicity greater than one, a global classification or a uniform complexity bound.

All checked the top C_p quotient and H-surjectivity, nontrivial M, the action through J and signed-defect recursion, the proper-shadow paired module and its irreducibility, all equal-prime alternatives, and the actual p=3,q=13 construction with μ_N=3 and μ_M=39. They preserved the distinction between a projected stabilizer image and a normal subgroup of the original H. No computation, new primary-source audit, quotient-folder assertion, sufficiency theorem or unrestricted classification is claimed.

They checked constant odd-involution fiber counts, all conjugates, the canonical maximal involution-stable core, the proper monolithic normal-subgroup correspondence and exact strict-defect/core-freeness reductions. No new computation or fresh primary-source audit was performed. These are model mathematical reviews, not human or formal certification. The stated restrictions and unresolved reconstruction conditions remain: these deductions do not complete the unrestricted classification.
