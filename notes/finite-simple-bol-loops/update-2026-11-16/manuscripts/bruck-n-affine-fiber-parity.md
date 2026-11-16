# Affine marked-fiber parity for multiple N Frattini factors

**Theorem with scoped independent reviews**, continuing 0323:C0010 [dependency/context not reproduced in this update: `../claims/C0010.md`]. Retain the faithful simple nonassociative Bruck-envelope and marked-fiber hypotheses in [the multiple-N source](bruck-multiple-n-frattini.md), with P class≤2, exponent≤4, Z=Φ(P)≅N^a central in P, G/P≅S5, and V=P/Z≅P6⊕U^b. Write W=H∩P, w=dim W=4s+e, where e is the F20-fixed multiplicity of its shadow. The marked-rank and original-fiber inputs are as in the reviewed `123933cc594b601dd317d62b333a949d20431d35`; the multiple-N transport of the augmentation pushout, including the actual H and marked lifts, is checked for a=2 in the independently reviewed multiple-N source at `6fe18de73836f5babe8bff5be255ff80fc864fb7`. The N-module and projectivity inputs are at `dec9a5f13aa4504ed2e1cb81d7cc1df4ea1aa499`. No quotient is assumed to be a folder.

The invariant-functional pushout in the one-N central-socle source at `bf11794257554b943a1b26ca15acd861f9faaa7f` applies to arbitrary a: for any invariant linear functional V→F2 vanishing on Wshadow, its pullback kernel L contains Z irrespective of a. The resulting G/L is a central C2-extension of S5 split over F20 by actual H lifts. The actual τ-fixed H lifts make the induced τ trivial, and a selected transposition marked lift supplies an involutory transposition lift. The cited F20/transposition detection forces this central extension to split, yielding a nontrivial loop homomorphism to C2, contrary to simplicity. Hence augmentation does not vanish on Wshadow. Averaging over the normal C5 in F20 preserves augmentation and projects Wshadow to its F-fixed part, because the F20-fixed part of P6 is two-dimensional and U^b has none. Therefore e≥1. This proof does not rely on a one-copy assumption on Z.

Fix a quotient transposition t and a selected marked involution λ above it. Since P6 and U restrict freely to ⟨t⟩, C_V(t)=(1+t)V. The reviewed marked identity makes

 d:(1+t)V→C_Z(t)/(1+t)Z,  d((1+t)v)=β(v,tv)+(1+t)Z,

equal to ℓλ on C_V(t). Its image is an S3-submodule, where S3=C_{S5}(t)/⟨t⟩ acts diagonally on a copies of the natural 2-dimensional F2S3-module. In particular r=rank d=rank ℓλ is even. Its quotient M=H¹(t,Z)/im d is a direct sum of natural C3-modules as a C3-module: restriction to odd-order C3 is semisimple, and the natural module has no fixed vector.

Every P-conjugacy orbit of involutory marked lifts over t contains a representative zλ, z∈C_Z(t). Indeed the V-shadow of any lift is t-fixed, and conjugation by P adjusts that shadow by (1+t)V=C_V(t). For two such representatives, the P-conjugators preserving zero relative shadow have t-fixed shadow; their central displacements are precisely (1+t)Z plus representatives of im ℓλ. Thus the set of all P-orbits over t is a torsor for M. This argument uses actual lifts and does not identify a quotient folder.

A lift to G of an order-three element centralizing t permutes these P-orbits. Its cube lies in P, so the induced permutation has order dividing three. Its action on the torsor is affine, with linear part the order-three action on M, because conjugation carries zλ to the conjugate of λ translated by the conjugate of z. Since 1−g is invertible on M, this affine transformation has exactly one fixed point. All other orbits have length three. Any selected G-invariant marked fiber thus consists of a number of P-orbits congruent to 0 or 1 modulo 3.

The original selected fiber has cardinality |P:W|/2, and each of its P-orbits has size 2^{ρ_V+ρ_Z+r}, where ρ_V=3+4b and ρ_Z=a. Therefore the number of selected P-orbits is

  2^{4b+3a+2−w−r}.

It is a positive power of two, and hence congruent to 1 modulo 3. Its exponent is even. Since w=4s+e and r is even,

  e≡a (mod 2).

In particular a=2 and 1≤e≤2 force e=2: the shadow contains the entire two-dimensional F-fixed plane of P6, including the S5-fixed constant vector 1.

Further, the polar map β(1,−):V→Z is S5-equivariant. The reviewed N-block decomposition gives Hom_S5(P6,N)=0 and Hom_S5(U,N)=F2·top, so β(1,−) is a binary matrix on U-top. W is elementary, hence this map vanishes on Wshadow. It cannot vanish on all V: if it did, the full preimage in P of ⟨1⟩ would be central elementary, because q(1)∈Z^F=0. It would be an actual S5-module extension of 1 by N². Reviewed block separation splits that extension, and Z^F=0 makes its unique F-fixed lift of 1 S5-fixed. The actual W lift is that same lift, giving a nontrivial normal subgroup of G contained in H, contrary to core-freeness. This also works for N^a. Consequently its top matrix is nonzero. If c is the socle-intersection multiplicity, the W-shadow nonfixed multiplicity is b+1 for a=2, so top(Wshadow) has codimension at most c, and this matrix has rank at most c. In particular c≥1. No conclusion that the whole branch is impossible is claimed.

## Selected labels for two central factors

Take $`a=2`$. The preceding argument gives $`e=2`$, and the dimension alternatives in the reviewed multiple-N source give $`w=4b+6`$. The natural $`S_3`$-constituents imply $`r\in\{0,2\}`$. The selected number of $`P`$-orbits over $`t`$ is therefore

```math
2^{4b+8-w-r}=2^{2-r}=\begin{cases}4,&r=0,\\1,&r=2.\end{cases}                                                \tag{1}
```


The order-three subgroup has a unique fixed point in the affine orbit-label torsor. It is fixed by the full $`S_3`$: the order-three subgroup is normal there, so every element of $`S_3`$ carries its unique fixed point to itself. Translating this point to zero makes the entire $`S_3`$-action linear. The $`C_2`$ factor generated by $`t`$ in $`C_{S_5}(t)`$ acts trivially on the labels. Its linear part on the translation module is the identity, so its affine action is a translation. It commutes with the order-three action on $`P`$-orbits, since commutators of their lifts lie in $`P`$. The translation vector must therefore be fixed by the order-three action, hence is zero. Any two lifts of a centralizer element differ by an element of $`P`$, which acts trivially on $`P`$-orbits. Thus a nonsplit extension introduces no additional centralizer action on this torsor beyond the described affine $`S_3`$-action.

If $`r=0`$, the translation module is two natural $`\mathbb F_2S_3`$-modules. Its $`S_3`$-orbits have sizes $`1,3,3,3,6`$: the three 3-orbits are the nonzero vectors in the three natural submodules $`(v,0)`$, $`(0,v)`$, and $`(v,v)`$, while pairs of independent vectors form the 6-orbit. Every invariant 4-subset is therefore the fixed origin together with one 3-orbit, equivalently an affine natural two-dimensional submodule of the label torsor. If $`r=2`$, the selected set consists of the unique $`S_3`$-fixed point. These are necessary descriptions of the original selected transposition fiber; they do not select an extension, establish the other fiber or collision conditions, or define a quotient loop.

For comparison, if the actual extension has a pure $`S_5`$-complement and the induced centralizer action fixes the pure transposition label, the $`r=0`$ selected 4-set necessarily contains that label. Whether this produces a stabilizer collision depends on the actual $`H`$ and the remaining folder data; the label theorem alone does not assert an exclusion. This section and the parity theorem have the exact-source reviews below.

## Independent mathematical review

At exact source `3c3cafff03f9e9d79640b68f03883c22e57210d6`, GPT-6.1 Terra reviewers [model reviewer], [model reviewer] and [model reviewer] independently accepted the full manuscript, conditional on the cited original-fiber, central-extension detection, module/block and actual-lift inputs. All checked arbitrary-a augmentation, the actual nonsplit P-orbit torsor, even rank of d, affine C3 unique-origin argument, orbit-count parity, the two-N fixed-plane and actual fixed-line obstruction, and the full centralizer action giving the four-label or single-label alternatives. No pure S5 complement, quotient-folder or whole-branch exclusion is assumed. No new computation or primary-source audit was claimed.
