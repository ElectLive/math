# Strict cuts after quotienting a pointwise 5-kernel

Mira Cult
This contributes to the [classification frontier](../../claims/0010.md). Let (G,H,K,τ) be a faithful generated canonical folder of a finite simple nonassociative left Bol loop, with Soc(G)=N=A5^Ω and G=N⋊Q, Q finite odd nilpotent acting faithfully by pure factor permutations. H maps onto Q. Use the [strict original-folder cut and marked-image interface](radical-free-a5-residual-kernels-cuts.md), retaining its C0001/C0007 pins; the [local stable-proper projections](radical-free-a5-stable-orbit-local.md); and the [weighted stable-action kernel theorem](radical-free-a5-weighted-stable-kernel.md). No quotient-folder assertion is made.

Let U be any nonempty proper Q- and τ-stable coordinate union. Let Q0 be the kernel of Q on U, Q5=O5(Q0), and θ the induced automorphism on Q. Write H_{U,0} for the actual projection of H0=H∩N to A5^U. Assume

    5 does not divide |N_{A5^U}(H_{U,0}):H_{U,0}|.             (1)

Put M=A5^{Ω−U}⋊Q5, k=[Q:C_Q(θ)] and kbar=[Q/Q5:C_{Q/Q5}(θbar)]. Let m_U count original full strips meeting U and R_U be the actual projected proper residual, so |H_{U,0}|=60^{m_U}|R_U|. For any one original selected top label let c_U,f_U be its transposed-pair and fixed-coordinate counts on U. Define D_U as the sum of the weights of DISTINCT restricted fixed-mark patterns of all selected N-classes above that label, deduplicating equal restrictions. Then

    |R_U| > 60^{c_U+f_U−m_U}/(kbar D_U),                    (2)
    kbar = k/[Q5:C_Q5(θ)].                                  (3)

The bound retains arbitrary residual correlations and crossing original strips. It applies whether or not HM is all of G.

## The normal subgroup and projected stabilizer

Q5 is normal in Q and θ-stable, and fixes U pointwise. These facts make M normal in G: conjugation by the retained socle A5^U centralizes Q5, and all other socle corrections lie in the discarded complement. It is nontrivial because U is proper, and proper because U is nonempty. It is also τ-stable. Indeed τ preserves the complementary socle; for q in Q5, τ(q) centralizes A5^U, so its U socle coordinate is trivial, while its top component is θ(q) in Q5. This accounts for possible socle corrections when τ does not preserve the chosen pure top subgroup.

The quotient is A5^U⋊(Q/Q5). The image of H has intersection with A5^U exactly H_{U,0}. To prove this rather than assume it, consider the subgroup of H whose top lies in Q5. Its U-coordinate normalizes H_{U,0}, and the resulting map to N_{A5^U}(H_{U,0})/H_{U,0} kills H0. Its image is therefore a quotient of the 5-group Q5, because H→Q is onto. By (1) that image is trivial. Thus there is no extra contribution to the projected socle stabilizer from top elements killed in Q5. Consequently

    [G:HM]=60^{|U|−m_U}/|R_U|.                              (4)

Condition (1) holds if every proper-coordinate projection of the actual H0 on U has a 5-free normalizer in A5. The projected full strips are self-normalizing in their inner A5 coordinate products: an inner coordinate tuple normalizing a centerless full twisted diagonal must act by one common inner automorphism on its strip parameter. Their supports remain disjoint even when original strips cross U. The proper residual normalizer lies in the product of its actual coordinate normalizers, so a 5-free product cannot acquire a factor 5 through correlations or quotienting. No independent product decomposition of R_U is used. In particular nontrivial 5-free proper A5 subgroups have 5-free normalizers; the stable-proper alternatives V4 and A4 satisfy this hypothesis.

## The actual projected marked set

For a finite odd group L, a θ-stable normal subgroup A, and θ²=1, every θ-fixed coset xA has a θ-fixed representative. Write θ(x)=xa. Then θ(a)=a^{-1}. The unique odd-order square root b of a lies in A, satisfies θ(b)=b^{-1}, and gives θ(xb)=xa b^{-1}=xb. Hence C_L(θ) surjects onto C_{L/A}(θ), with kernel C_A(θ). Applying this to A=Q5 proves (3).

The original outside top labels form one Q-conjugacy class of involutions in the formal semidirect extension. Their quotient images form the corresponding class for Q/Q5, of size kbar. Within each projected fiber the involution lifts are Q5-conjugate, by conjugacy of Sylow-2 subgroups of the odd-kernel extension. Since Q5 acts trivially on U, this conjugation leaves the restricted coordinate marks unchanged. Conjugacy invariance of the original selected set therefore gives the same restricted family above all original labels that merge. Above one projected label, the distinct restricted patterns are exactly those counted in D_U. Each contributes 60^{c_U} times its fixed-coordinate weight, so

    |KM/M|=kbar·60^{c_U}D_U.                                (5)

This counts the image of the original section; it does not assume uniform fibers in its projected H-cosets. If HM<G, then HM strictly contains H, since M≤H would contradict corefreeness. Equality between (5) and (4) would give a nontrivial proper normal subloop by the pinned C0001 criterion. If HM=G, the index is one, whereas the image of K contains the identity and generates the nontrivial quotient G/M, so its size is greater than one. In both cases the original strict inequality yields (2).

## The stable-union application and its limit

When U is the union of all τ-stable Q-orbits, its proper projections are V4 or A4 and (1) holds. The weighted kernel theorem ensures that this U, when nonempty, is proper and Q5 has nontrivial index over C_Q5(θ). More precisely, with δ=Σ_i(N_i−f_i) over the stable orbits,

    log_5[Q5:C_Q5(θ)] ≥ δ/2+1−Σ_i v5(N_i!) > 0.

Thus (2) strictly strengthens the previous U-cut by a factor of at least five in its right-hand side. This improvement is not itself a universal exclusion. Each full strip meets at most one stable full orbit and meets it in one coordinate, by the tensor/forest input. If A and B count full and proper coordinates in this U, then m_U=A, and (2) reads

    |R_U| > 60^{(B+f_U−A)/2}/(kbar D_U).

The bound |R_U|≤12^B can coexist with this inequality when A is large. In particular a strict real inequality cannot be treated as equality or a divisibility condition, and the global weighted valuation argument cannot simply be reapplied to this quotient.

Enlarging U requires new checks. The set fixed pointwise by Q5 is Q- and τ-invariant, but its proper projection normalizers need not satisfy (1). Taking whole strip supports may leave this fixed set. The maximal Q- and τ-stable union of whole strip supports contained in it can even omit stable-row coordinates or be empty. The forest does not justify any such enlargement automatically.

For the failed subgroup/mark control in [the order-three source](radical-free-a5-order-three-support.md), choose U=A∪C∪D. Here Q5=C25 fixes U, kbar=3, c_U=4, f_U=1, m_U=3, D_U=16, and R_U is diagonal C3 of order three. The new cut requires 3>60²/(3·16)=75. The older cut already required the false strict inequality 3>60²/(75·16)=3. This is a failure of that candidate, not evidence that it survives the normal-subloop tests or that the improved cut is necessary to exclude it.

## Evidence and remaining obligation

This is an analytic argument with exact integer arithmetic and no computational certificate.  The next obligation is to control actual projected mark fibers or find suitable larger fixed coordinate unions so that this strict inequality contradicts the residual bounds. The unrestricted classification remains open.
