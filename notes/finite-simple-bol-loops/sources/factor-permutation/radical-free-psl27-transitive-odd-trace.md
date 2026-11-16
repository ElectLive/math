# Transitive odd tops for PSL₂(7): a trace reduction

Mira Cult

**Independently reviewed, conditional on the pinned inputs.** This is a bounded continuation of [0323-finite-simple-non-moufang-bol-loops:C0010](../../claims/0010.md), not a classification. Let `(G,H,K,τ)` be the faithful generated canonical folder of a finite simple nonassociative left Bol loop, with `G=T^Ω⋊Q`, `T=PSL₂(7)`, and `Q` an arbitrary finite odd group acting faithfully and transitively by pure factor permutations. Neither `H→Q` surjectivity nor nilpotence of `Q` is assumed. Use the canonical-folder and strict original normal-quotient inputs [C0001](../../claims/0001.md), inversion and actual marked-class input [C0007](../foundations/C0007.md), and the `PSL₂(7)` characters, subgroups and marked-square/parity inputs in [the fixed-factor source](radical-free-fixed-factors.md). Those source qualifications remain in force.

Write `|Ω|=2c+f`, where `f>0` counts the fixed factors of `τ`; `|Ω|` is odd. The local outer coset of `τ` is constant on the sole `Q`-orbit. Put `H0=H∩T^Ω`, `H_Q=HN/N` for `N=T^Ω`, `t=[Q:H_Q]`, and `k=[Q:C_Q(θ)]`, where `θ` is induced by `τ` on `Q`. Both `k` and `t` are odd. Let `Λ=τK` be the actual selected outside set. Its top labels are all `k` outside-involution labels, and it consists of complete actual `N`-classes above them.

## The outer case

At a fixed factor an outer involution has the unique local class of size `28`; at a swapped pair the class has size `168`. Thus `|K|=k·168^c·28^f`, and original transversality gives

 `|Syl₂(H0)|=2^(3c+f)`.

The square of that fixed outside class contains the unique inner involution class. On every swapped pair, the class square contains matched pairs of involutions. The original matched-support parity expansion imposes identity at at most one coordinate of each swapped pair, with target a 2-group of order at most `8^c`. Every kernel in the expansion is nontrivial, since `f>0`, and has an even number of elements of order at most two: pair all other elements with their inverses. Hence a nonidentity involution in `H0∩Λ²` exists, a contradiction. This uses the original subgroup and marked set, not a quotient folder.

## The inner trace and polynomial constraints

Now suppose the local coset is inner or identity. The degree-six deleted Fano-plane character has trace `2` on the inner involution class and has fixed vectors for every proper subgroup except `C7` and `7:3`. Its coordinate direct sum is irreducible for `G`, because the coordinate `N`-types are distinct and `Q` acts transitively. Each selected mark has positive trace on that sum: its fixed-factor contributions are `6` or `2`, and swapped summands contribute zero. The original transversal identity excludes an `H`-fixed vector. If an actual factor-stabilizer image `J` fixed a nonzero local vector, transport it along that factor's single actual `H`-orbit and put zero on the other `H`-orbits. Thus each `J` is `T`, `C7` or `7:3`, without using `H→Q`.

The actual `H0` projection is `T` when `J=T` and is odd when `J` is proper. Full-coordinate Goursat splitting therefore gives independent original full Scott strips together with an odd proper-coordinate residual. Let `s` be the number of full strips. There is no singleton strip. Indeed, a singleton `T_i≤H0` and any selected fixed factor with a nonidentity local automorphism would give a collision: use transitivity of `Q` and `G`-invariance of `Λ` to move it to `i`, and choose `a∈T_i` moved by it; then `λ^aλ` is a nonidentity element of `H0∩Λ²`. Thus a singleton forces every selected fixed mark to be identity. In that case `|K|=k·168^c`, and transversality yields

 `|H0|=168^(c+f)t/k`.

The odd residual and `|Syl₂(T)|=8` give `s=c+f` and make the residual order `t/k≥1`. If `Q≠1`, the original strict normal quotient by `N` gives `k>t`: when `HN=G`, the equality above would force `k=1`, and generation by the projected marked section would force `Q=1`. This contradicts `t/k≥1`. When `Q=1`, transitivity gives a single factor, excluded by the cited entire-`T` theorem. Thus no singleton occurs.

For clarity the needed degree-eight character can be obtained directly. Take a nontrivial linear character λ of B/C7 for B=7:3, and induce it to T. On the classes of orders 1,2,3,4,7a,7b it has values (8,0,−1,0,1,1): the projective coset action has no fixed points for orders 2 or 4, two for order 3 with the inverse λ-values summing to −1, and one for order 7 with λ-value 1. The class sizes are (1,21,56,42,24,24), so its squared norm is (64+56+24+24)/168=1 and it is irreducible. Its fixed dimensions are (8+6)/7=2 for C7 and (8−14+6)/21=0 for 7:3; its involution trace is zero.

If some actual `J=C7`, the coordinate direct sum of this character has an `H`-fixed vector by the same one-`H`-orbit construction. Its selected trace is nonnegative and vanishes only when every fixed mark is nonidentity. Then `|K|=k·168^c·21^f`, so the odd residual and the class count force `s=c+f`. But no strip is a singleton and f>0, whereas `s≤⌊(2c+f)/2⌋<c+f`. Hence every proper actual `J` is `7:3`.

Let `𝔉` be the actual nonempty family of selected active subsets of the `f` fixed factors for one outside top label, and put

 `F(z)=Σ_{A∈𝔉}z^|A| = Σ_{a=0}^f b_a z^a`,  `0≤b_a≤binom(f,a)`.

Transport by actual top conjugation identifies the pattern families above the other selected labels. The fixed inactive and active classes have sizes `1` and `21`, respectively, so

 `|K|=k·168^c F(21)`.

The degree-seven deleted projective-line representation has a fixed vector for `7:3` and an Aut(`T`)-invariant symmetric tensor in every degree at least two: products of the quadratic and cubic power sums on the deleted eight-point permutation module suffice. The full tensor over `Ω` therefore has an `H`-fixed vector, even with correlated proper residuals. Its inner-involution trace is `−1`; hence the scalar of an active local class is `21(−1)/7=−3`, while an inactive mark contributes `1`. The selected-mark scalar obstruction gives

 `F(−3)=0`.                                                (1)

The odd residual gives `|Syl₂(H0)|=8^s`; comparing 2-parts in the original class count gives

 `v₂(F(21))=3(c+f−s) ≥ 3(f+1)/2`.                         (2)

The inequality uses `s≤⌊(2c+f)/2⌋=c+(f−1)/2` because every strip has at least two coordinates and `f` is odd.

The selected family has an additional symmetry. Let σ be the factor involution induced by τ. The group `C_Q(θ)` acts transitively on its fixed factors. For fixed x,y choose q∈Q with qx=y. Both σ and q⁻¹σq fix x and lie in Q_x⋊⟨σ⟩. Their outside involutions are conjugate by the odd group Q_x, using the same square-root argument as for Q. Thus some a∈Q_x satisfies σ^(qa)=σ, and qa sends x to y while centralizing σ. Faithfulness identifies this centralizer in Q with C_Q(θ). Conjugation by it permutes the fixed coordinates and preserves identity/nonidentity local labels and the actual selected N-classes above θ. Therefore `𝔉` is invariant under an odd transitive permutation group on its f positions. No solvability theorem is needed for this step.

## The valuation conditions alone do not exclude the inner case

The following explicit Boolean-pattern family satisfies (1), (2), and odd transitive invariance; it is **not** a folder construction. Let

 `F7(z)=6z+11z²+30z³+3z⁴+7z⁵+6z⁶+z⁷`.

Direct arithmetic gives `F7(−3)=0` and `F7(21)=2^19·4473`. On 11 positions, cyclic rotation has respectively `15,30,42,42,30,15,5` orbits of subsets of weights `3,...,9`. Choose respectively `6,11,30,3,7,6,1` such orbits. Their union `D11` has weight enumerator `A(z)=11z²F7(z)`.

On 33 positions in three labeled 11-position blocks, take the Cartesian product `D11³`. Simultaneous rotation and cyclic block permutation give a regular `C11×C3` action preserving the family. Its weight enumerator `F=A³` satisfies `F(−3)=0` and `v₂(F(21))=57≥3(33+1)/2=51`; its coefficients obey the binomial bounds because it is an actual set of subsets. These data do not verify any stabilizer, marked-fiber, transversal, class-square or normal-subgroup condition. In particular, no exclusion follows from (1), (2) and odd transitive pattern invariance alone.

The outer case is excluded under the pinned inputs. The inner case remains open in this transitive-top model: the trace and valuation restrictions above are necessary, and further original-folder structure is required. No new permanent claim ID or computation certificate is asserted.

## Independent mathematical review

Four separate automated mathematical reviews accepted the complete source, conditional on its pinned canonical-folder, local-character, subgroup and class-square inputs. They checked the outer nonabelian Sylow parity, actual H-orbit direct sums, singleton exclusion, degree-eight character, selected-family trace and valuation constraints, centralizer transitivity and Boolean-family counterexample. One reviewer independently ran a small arithmetic/enumeration check of the displayed polynomial values and cyclic subset-orbit counts; another reviewer independently checked those arithmetic values. These checks do not realize a folder. No fresh primary-source audit or independent reproof of all upstream inputs was performed. These are model mathematical reviews, not human/formal certification or GitHub approval; the inner case remains open.

