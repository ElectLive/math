# Projective radicals, actual subloops and affine quotients

**Status:** the extensions below are unreviewed. The finite [class-two multiplicity and group-host results](../projective-radicals/README.md) do have separate independent mathematical reviews. An embedding in a group of permutations is not on its own an embedding in the loop on which it acts.

## The group and loop host are different

The finite reviewed result embeds all groups $`F`$ of class at most two, exponent dividing three and order at most $`3^k`$ in the same solvable radical. The [countable version](proofs/countable-radical.md) proposes compatible embeddings and finite multiplication tables in one increasing chain, hence one countable group host. The [native promotion](proofs/native-subloops.md) instead changes to a genuine principal isotope and checks the product at its chosen basepoint, including the central correction coming from the stabilizer. The proposed hosts have an element of order nine, unlike the exponent-six precursors. The group $`F`$ would embed as an associative subloop; moreover, its elements $`g,h`$ commute precisely when $`L_{gh}^{-1}L_gL_h`$ fixes **every** ambient point. This calculation is the part not supplied by the group theorem.

A separate proposed calculation in the projective isotope gives a unique subloop of order equal to the full 3-part, but that subloop need not contain every order-nine cyclic subloop. In the elementary specimen the proposed Sylow has five maximal associative subloops. This neither restores the general native Sylow assertion nor upgrades the host theorem to a global decomposition.

## Two distinct unboundedness constructions

In the [fixed-exponent radical construction](proofs/radical-class.md) the left group has quotient $`\mathrm{PSL}_2(19)`$. For each $`n\ge3`$ its whole solvable radical would be a metabelian 3-group of **class exactly $`n`$ and exponent exactly nine** in a finite simple proper loop of exponent six. The [principal-unit variant](proofs/associator-order.md) gives two involutions $`h,k`$ in such an exponent-six loop whose native product has order three and whose permutations $`L_hL_k`$ and $`L_{hk}^{-1}L_hL_k`$ each have order exactly $`3^a`$, for any prescribed $`a\ge1`$. The radical exponent is **not kept at nine** in that second variant.

There are separate proposed restrictions in the opposite direction. For an abelian normal subgroup $`A`$ of odd order in a canonical signed envelope, use only the actual selected classes in the quotient and the projected point stabilizer $`J`$. The candidate bound is
```math
  \exp(A)\mid\prod_x [J\cap J^x : C_J(x)] .
```

The product ranges over representatives of true selected classes, not all projected involutions. In the previously reduced natural projective-line action with its actual split torus and signed fibers, a vertical abelian kernel would have to be elementary abelian of characteristic three and the quotient field would have order 19. This would **reduce to an elementary kernel, not enumerate its operations**. For Hall-regular nonabelian Sylow kernels there is a proposed power-height extension; it does not apply to arbitrary nonregular kernels. For arbitrary odd kernels in the specified signed projective quotient, chief-factor rotation-word estimates give orbit-size divisibility by $`3^8,3^{58},11^8,3^{492}`$ at field sizes 19, 163, 243 and 1459 respectively. These are lower or conditional restrictions, not field existence results.

For the elementary 19-dimensional augmentation module (the projective action has **20** points), one-step simultaneous couplings are proposed to be parametrized by Grassmannians in dimension 11 over $`\mathbb F_3`$. Iterated couplings are proposed to correspond to observable, jointly nilpotent pairs with eleven ordered output covectors. Their proposed isotope closure has six ordinary classes per framed-pair orbit (three of exponent six and three of exponent 270). These classifications are **not** consequences of the [reviewed nested embedding construction](../manuscripts/0113-infinite-augmentation-chain.md). No general classification of elementary 19-projective kernels is claimed.

## The affine Burnside successor

The [affine quotient and operator argument](proofs/affine-quotients.md) proposes that every proper quotient of the [infinite two-generator example](../bol-burnside/two-generators.md) is finite. In the separate finite class of odd-prime-exponent Bol loops with abelian associated Bruck loop and derived subloop of index $`p`$, the parameter is an invertible operator $`T`$ with no eigenvalue in the prime field. Ordinary isomorphism uses similarity and scalar changes on $`T`$; isotopy uses similarity and affine changes on $`T^{-1}`$. For a noncyclic member the minimum number of loop generators is one plus the largest **number** of primary blocks at a single irreducible polynomial, not the length of the largest block.

## Reproduction

Use Python 3 and NumPy; run the following in this directory. The four projective programs share public routines and the [same canonical matrix input](../sources/elementary-psl2-19/evidence/psl2-19-explicit-matrix-input.json.zlib.b64). The affine checker uses only the Python standard library.

```sh
export PYTHONPATH=../projective-radicals/code:../sources/augmentation-chain/code
data=../sources/elementary-psl2-19/evidence/psl2-19-explicit-matrix-input.json.zlib.b64
python code/verify_countable_universal_radical_tower.py "$data"
python code/verify_universal_native_associative_subloops.py "$data"
python code/verify_irregular_projective_radicals.py "$data"
python code/verify_unbounded_native_associator_orders.py "$data"
python code/check_affine_quotient_lattices.py
```

Expected outputs: [countable tower](checks/countable-universal-radical-tower.out), [native subloop promotion](checks/universal-native-associative-subloops.out), [unbounded class](checks/irregular-projective-radicals.out), [one associator](checks/unbounded-native-associator-orders.out), [affine normal lattices](checks/affine-quotient-lattices.out). The class controls reach classes 3, 4 and 5; the associator controls obtain actual point-orbit lengths 3, 9, 27, 81 and 243. The affine program computes congruences without assuming that they are vertical or linear, and checks the need for three generators in a repeated-block 243-element example. Passing finite checks does not by itself prove any of the universal assertions.
