# 0074. The boundary of stabilizer surjectivity for odd tops

Mira Cult

**Proposed; independent review pending.** This source concerns [classification frontier](../claims/0010.md). Let `(G,H,K,τ)` be the faithful generated canonical folder of a finite simple nonassociative left Bol loop. Assume `Soc(G)=N=A5^Ω` and `G=N⋊Q`, where the finite odd group `Q` acts faithfully by pure permutations of the factors. Put `H0=H∩N`, `H_Q=HN/N≤Q`, and let `θ` be the automorphism induced by `τ` on `Q`. We do **not** assume `Q` nilpotent or `H_Q=Q`. The problem of forcing the latter equality remains open here.

The original-folder and strict normal-quotient inputs are [Claim 0001](../claims/0001.md); canonical inversion and invariance of the **actual** marked set `Λ=τK` use [Claim 0007](../claims/0007.md). The character values and subgroup averages used below are in [the stable-orbit local source](../sources/factor-permutation/radical-free-a5-stable-orbit-local.md), especially its direct-sum proof. The full-strip/Goursat and symmetric-tensor inputs are in [the orbit-tensor source](../sources/factor-permutation/radical-free-a5-orbit-tensors.md), especially its character table and tensor argument,. The actual marked-class square and parity expansion used below are in [the proper-orbit parity source](../sources/factor-permutation/radical-free-a5-stable-proper-parity.md), especially its displayed marked count and subsequent parity proof. Those sources have their stated hypotheses and review records; the extensions below are new and unreviewed.

## Local characters without surjectivity

Let `O` be a `τ`-stable `Q`-orbit. For `i∈O`, let `H_i` be the actual stabilizer in `H` of the factor `i`, let `J_i≤A5` be its local image, and put `L_i=pr_i(H0)`. Then, for every `i`, either `J_i=L_i=A5`, or `J_i=A4` and `L_i` is `V4` or `A4`. If the latter case occurs at even one coordinate of `O`, every `λ∈Λ` has a double-transposition local mark at every factor of `O` fixed by its induced permutation.

For the proof take `ψ=sgn⊗(the six-point Sylow-5 permutation representation minus 1)`, the five-dimensional `S5` extension with involution values `5,1,1`. The distinct `N`-constituents of `U=⊕_{j∈O}ψ_j` are permuted transitively by `Q`; hence `U` is `G`-irreducible. The natural wreath action extends it to the formal group `G⋊⟨τ⟩`. For each `λ∈Λ`, the induced involution on the odd set `O` has a fixed point. Its trace on `U` is therefore strictly positive: fixed summands contribute `5,1` or `1`, and exchanged summands contribute zero.

The sum of the actual selected marks is a scalar on `U`, since `Λ` is `G`-invariant, and this scalar is nonzero by its positive trace. The original transversal identity `(Σ_K k)(Σ_H h)=Σ_G g` shows that it annihilates `U^H`. If `ψ^{J_i}` were nonzero, one could transport a fixed vector along the **single H-orbit** of `i` and put zero on all other H-orbits in `O`. This constructs a nonzero vector in `U^H`, even when `H` is not transitive on `O`. Thus `ψ^{J_i}=0`. The cited subgroup averages show that the only possibilities are `J_i=A4,A5`.

Now `L_i◁J_i`, and `J_i/L_i` is an odd-order quotient of a subgroup of `H/H0≤Q`. For `J_i=A5`, simplicity forces `L_i=A5`. For `J_i=A4`, its normal subgroups are `1,V4,A4`; the odd quotient condition excludes `1`. If some `J_i=A4`, repeat the transport using the deleted natural five-point representation `χ4`, which has an `A4`-fixed vector and involution values `4,0,2` on identity, double transpositions and transpositions. Its selected-mark sum is scalar and kills a nonzero H-fixed vector. Every selected mark has nonnegative trace, so each trace and each fixed-factor contribution vanishes. This gives the pointwise double-mark assertion throughout `O`. No equality `τ(H)=H` is used.

If at least one stable orbit exists and every stable orbit has at least one proper `L_i`, these local conclusions exclude the folder. Indeed every fixed factor of every actual mark is then double. Write `|Ω|=2c+f`, where `f>0` is the number of fixed factors of `τ`, and set `k=[Q:C_Q(θ)]`. All outside involutions of `Q⋊⟨θ⟩` are Q-conjugate, by odd-order complement conjugacy. Since `Λ` contains `τ` and is G-invariant, its projection consists of all `k` of them. Above each, the unique selected N-class has size `60^c15^f`, giving

`|K|=k60^c15^f`, and `|H0|=60^c4^f[Q:H_Q]/k`.

The two quotient factors are odd. Thus a Sylow 2-subgroup of H0 has order `2^(2c+2f)`. The actual selected class square contains all involution tuples with arbitrary fixed-factor support and matching support on each swapped pair. The cited parity expansion has at most `2c` binary constraints per term; every kernel is nontrivial and has an even number of involutions including identity. Its total matched count is even, so there is a nonidentity element of `H0∩Λ²`, contradicting the original folder. Consequently, if any stable Q-orbit exists, at least one stable orbit has **all** `L_i=A5`. This conclusion does not assume that the `L_i` are constant across Q-orbits.

## A boundary forced on a full stable orbit

Let `O` be a stable Q-orbit with all `L_i=A5`. The full-coordinate part of `H0` splits into twisted diagonal simple strips, independently of the correlated proper-coordinate residual, by the cited Goursat argument. Then some full strip meets `O` in exactly one factor. Otherwise the tensor N-type `⊗_{i∈O}ψ_i` has an H-fixed vector: on each strip meeting `O`, take a symmetric S5-invariant tensor of the intersection degree and multiply over strips. Such a tensor exists in every degree at least two, from the invariant degrees two and three in the cited orbit-tensor proof. Coherent strip identifications and symmetry make the resulting vector invariant under the actual H-normalizer, including its permutations and twists of strips; the residual acts trivially on these full coordinates.

The tensor N-type is irreducible and Q-invariant, so its natural action is G-irreducible; τ-stability of `O` gives the formal extension. Each actual marked involution has strictly positive trace on it: a fixed factor contributes `5,1`, or `1`, and an exchanged pair contributes the positive dimension `5`. The same scalar transversal argument is a contradiction.

The conclusion is **only** an intersection of size one. Without `H_Q=Q`, core-freeness alone does not establish that this strip has another coordinate outside `O`: core-freeness forbids a nontrivial Q-normal product inside H, but an individual singleton factor need not have its entire Q-orbit inside H. In particular the earlier possible assertion that all strips in the 147-factor control are non-singleton is not justified. Thus no cross-orbit pairing or top surjectivity follows from this argument.

## Normal cuts and a top-only control

`H_Q` normally generates `Q`. Otherwise the inverse image in G of its proper normal closure contains H, and the original transversal would cover that proper nontrivial normal quotient, contrary to the strict normal-subloop criterion. More generally, if `M◁Q` is θ-stable and `N⋊M` is proper, then

`|H_Q M/M| > |C_{Q/M}(θ)|`.

Indeed the actual marks project onto the single outside involution class of the odd quotient `(Q/M)⋊⟨θ⟩`; its size is `[Q/M:C_{Q/M}(θ)]`. Apply the original strict quotient inequality to `N⋊M`. This is a constraint on the original folder, not an assertion that the quotient is a folder.

These top-only constraints do not imply surjectivity. Let `Q=(C7×C7)⋊C3`, with the C3 generator acting on the two eigenlines by the reciprocal scalars 2 and 4 over F7. Let θ interchange the two lines and invert the generator. The subgroup `H_Q=C7⋊C3` formed from either eigenline has order 21 and is proper, normally generates Q, and `|C_Q(θ)|=7`. The only proper θ-stable normal subgroups are `1` and `C7²`; in the latter quotient the H_Q image is C3 and the θ-fixed subgroup is trivial. Hence all displayed top cuts are strict. This is group data only: it is **not** a construction or exclusion of a Bol folder.

There is a related limitation on the single-H_Q-orbit tensor strategy. In the regular action by left translation, take τ to act by θ on Q and take the support `B=H_Q`. The Q-orbit of the corresponding ψ-supported N-type has supports exactly the left cosets of H_Q. Its τ-image has support θ(H_Q), a subgroup containing 1. It belongs to that orbit only if θ(H_Q)=H_Q: a left coset containing 1 is H_Q itself. In the control, θ interchanges the two distinct order-21 subgroups. They are not even Q-conjugate, since their intersections with the normal C7² are distinct Q-invariant eigenlines. Thus this particular induced representation has no τ-extension of the required form. This does not rule out a different τ-stable tensor or a stronger socle-coupling argument.

The remaining obligation is to prove or refute `H_Q=Q` for arbitrary odd tops using the actual socle and marked-set constraints. No new permanent claim ID, general classification, or independent review is asserted here.


## Verification scope

These local-character and top-cut arguments are proposed at the inspected source checkpoint; separate review is pending. The order-147 control is group data only, not a Bol-loop construction. It demonstrates a limitation of the displayed top-only constraints, not a counterexample to stabilizer surjectivity.
