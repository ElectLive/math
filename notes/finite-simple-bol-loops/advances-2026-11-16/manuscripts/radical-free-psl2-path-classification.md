# A primitive-prime PSL₂ path classification

**Independently reviewed continuation of 0323:C0010 (dependency `claims/C0010.md` not included in this update).** Let $`T=\mathop{\mathrm{PSL}}\nolimits_2(q)`$, where $`q=p^f`$, $`p\ge7`$ is prime, and there is a prime $`r>5`$ with $`\mathop{\mathrm{ord}}\nolimits_r(p)=2f`$. Consider faithful generated canonical folders of finite simple nonassociative left Bol loops with $`G=T^k\times T^k`$, $`k\ge1`$, and $`\tau`$ exchanging the two blocks coordinatewise.

Under the cited inputs, if $`q\equiv1\pmod4`$ there are no such folders. If $`q\equiv3\pmod4`$, for each $`k`$ there is exactly one loop-isomorphism class: the reviewed $`k`$-edge path folder with endpoints a Borel subgroup and a nonsplit torus normalizer. The existence and proper non-Bruck nature of those path loops are supplied by [the path construction](../../update-2026-11-16/manuscripts/radical-free-path-factorizations.md) (earlier public snapshot), at `1818e2c44bee176638f1212fd8b36c6a8a92e5ba`; its graph and isomorphism interfaces are reviewed at `c1be0daa47ca5f6befeb96378bc1937544acbde1`. The reduction to strips and a forest uses [the strip-forest theorem](../manuscripts/radical-free-strip-forests.md), at `6d3a97daa9cf20bbae0416295c8c2374c2cd8ede`. No claim is made for fields without the stated prime $`r`$.

The subgroup input is Dickson's classification as stated in Guralnick–Zieve, *Polynomials with PSL(2) monodromy*, Annals of Mathematics 172 (2010), Appendix Theorem A.1 and Lemma A.2, printed p.1354, [published paper](https://annals.math.princeton.edu/wp-content/uploads/annals-v172-n2-p11-p.pdf). It includes Borel, torus-normalizer, exceptional $`A_4,S_4,A_5`$, and subfield possibilities. Standard torus facts used here are that a Borel $`B`$ has order $`q(q-1)/2`$, a nonsplit torus normalizer $`D`$ has order $`q+1`$, all such normalizers are conjugate, and all involutions of $`T`$ form one conjugacy class. Dickson’s subgroup classification is an external input, not reproved here. The exact forest and canonical-folder dependencies, including the CFSG-dependent invariant involution-class input, remain as stated in the cited sources.

## Valuation saturation

The order assumption gives $`r\mid q+1`$. For every proper divisor $`d<f`$, $`r\nmid p^d\pm1`$; $`r>5`$ excludes the exceptional subgroups. Dickson's list therefore makes every proper subgroup containing $`r`$ cyclic or dihedral of nonsplit type. Its Sylow r-subgroup is normal, so Lemma A.2 puts the actual subgroup inside its nonsplit torus normalizer; in particular it has no $`p`$-divisor. Every proper subgroup has $`p`$-valuation at most $`f`$; if it has valuation $`f`$, it lies in a Borel. Indeed the proper subfield cases have smaller $`p`$-part and the exceptional groups have no $`p`$-divisor when $`p\ge7`$. In the remaining upper-triangular abstract type, the full Sylow p-subgroup is normal, so the actual subgroup lies in its Borel normalizer. This uses the subgroup types together with their characteristic Sylow subgroups, rather than assuming that the isomorphism-class list alone specifies embeddings.

Use the strip-forest theorem. Let $`c`$ be the number of components, $`\ell`$ the number of proper-coordinate leaves, and $`R`$ the projection of $`H`$ onto those coordinates. Since each component is a tree,

```math
|R|=|T|^{\ell-c}. \tag{1}
```

Each leaf projection has $`p`$-valuation at most $`f=v_p(|T|)`$ and $`r`$-valuation at most $`v_r(|T|)`$. The first paragraph makes the sets of leaves with positive $`p`$- and $`r`$-valuation disjoint. Equation (1) therefore requires at least $`\ell-c`$ leaves of each kind, giving $`\ell\le2c`$. Each tree has at least two leaves, so $`\ell=2c`$. Every component is a path, and exactly $`c`$ leaves have positive $`p`$-valuation and $`c`$ have positive $`r`$-valuation. All these valuations are maximal. Hence every $`p`$-leaf projection lies in a Borel and every $`r`$-leaf projection lies in a nonsplit normalizer. As $`|B||D|=|T|`$,

```math
|R|=|T|^c\le\prod_{\text{leaves}}|A_i|
 \le(|B||D|)^c=|T|^c. \tag{2}
```

Thus each leaf projection is its full containing Borel or normalizer, and $`R`$ is their entire direct product.

Every path has one end of each type. Otherwise the equal global counts would force a path with two $`D`$-ends. Set all other components to the identity; in each strip on this path choose an involution from the $`T`$-class, and choose an involution in each of its independent $`D`$-leaf groups. All paired coordinates on the path are conjugate involutions, so the resulting nonidentity element is in $`H\cap\Lambda^2`$, a contradiction. Each path therefore has a $`B`$-end and a $`D`$-end.

If $`c>1`$, retain precisely the paired coordinates of one component in the normal quotient. Its leaf projection has order $`|B||D|=|T|`$, whereas the strip-forest strict inequality requires it to have order greater than $`|T|`$. Hence $`c=1`$. Independent swaps within the $`\tau`$-pairs orient the path, and tree coordinate automorphisms remove its strip twists, giving the standard path data.

## Endpoints and uniqueness

If $`q\equiv1\pmod4`$, both $`B`$ and $`D`$ contain involutions. Their independent factors in $`R`$ supply conjugate involutions, and choosing involutions in the internal strips produces a nonidentity element of $`H\cap\Lambda^2`$. Thus no folder survives. If $`q\equiv3\pmod4`$, $`|B|`$ is odd and $`\gcd(|B|,|D|)=1`$, so $`B\cap D=1`$ and $`|B||D|=|T|`$. Consequently $`T=BD`$ is an exact factorization and the cited path construction supplies the loop.

For uniqueness, all nonsplit normalizers $`D`$ are conjugate. A Borel is a point stabilizer on the projective line. When $`q\equiv3\pmod4`$, $`D\cap B=1`$ for every point stabilizer and $`|D|=q+1`$, so $`D`$ acts regularly on the $`q+1`$ points. Hence all pairs $`(B,D)`$ are simultaneously conjugate in $`T`$. The cited path-folder isomorphism criterion, allowing reversal, now gives exactly one loop-isomorphism class for each $`k`$.

## Independent mathematical review

The deduction depends on the cited subgroup, forest, canonical-folder and path inputs, including Dickson’s classification and the stated CFSG-dependent inputs. Its scope retains the exact primitive-prime hypothesis and paired inversion.


## All nonprime fields of characteristic at least seven

**Independently reviewed continuation.** The theorem above holds for every q=p^f with p≥7 prime and f≥2, without a primitive-prime hypothesis: no folders for q≡1 mod4, and exactly one Borel/dihedral path class for each k when q≡3 mod4. The canonical group and paired inversion hypotheses are unchanged.

For f≥3, apply Zsigmondy's primitive-divisor theorem to p^(2f)−1. Neither exception, (p,2f)=(2,6) or exponent 2 with p+1 a power of two, applies. A primitive prime r satisfies 2f | r−1, so r≥2f+1>5, and the reviewed theorem applies. The exact source statement is Ömer Avcı, *Large Zsigmondy Primes*, [arXiv:2011.06136v2](https://arxiv.org/html/2011.06136v2), 3 October 2023, §1, first paragraph. Zsigmondy’s theorem is used as an external input.

If f=2, every odd prime r dividing p²+1 has order 4 modulo p in the notation ord_r(p). Unless one such r exceeds 5, p²+1=2·5^a. Reduction modulo 3 (p≥7 prime) gives 2=2(−1)^a, so a=2b≥2. In this residual case p≡±2 mod5. Dickson's proper subfield groups PSL₂(p), PGL₂(p) have no 5-divisor, nor does a Borel. Exceptional groups have no p-divisor, and their 5-part is at most 5. Thus p-bearing and 5-bearing proper subgroups have disjoint support in the leaf count. The same valuation saturation forces paths, maximal p-part p² at every p-leaf, and maximal 5-part 5^(2b) at every 5-leaf. Full p-part forces the actual subgroup into a Borel. Full 5-part excludes exceptional and subfield groups, so the actual subgroup lies in a nonsplit normalizer. The order equality (2), collisions and connectedness apply unchanged. Since q=p²≡1 mod4, the two even endpoints give a collision. No solution of a Pell-type equation is assumed or required.

## Prime fields beyond the primitive-prime hypothesis

**Independently reviewed continuation.** For every prime p≥61 and for p=31, the same Borel/dihedral conclusion holds. It also holds at p=47, while p=53 admits no folder. At p=23 and p=59 there are exactly two path isomorphism classes for each k, subject to the finite subgroup certificate below: their endpoints are respectively B with D₂₄ or S₄, and B with D₆₀ or A₅. These are all folders in the paired canonical setting for those primes, not merely examples.

For prime p≥7, every proper p-containing subgroup lies in a Borel B and has p-part p. There are no proper subfield groups. If an odd r divides p+1, no p-containing proper group contains r. For p≥61, every r-containing proper group has order at most p+1: torus subgroups lie in the nonsplit normalizer D, and exceptional orders are at most 60. The disjoint p/r valuation count gives ℓ=2c, full valuations at every leaf, and all components paths. Equality (2) forces full independent B and order-(p+1) leaf groups. Since p+1>60, the latter are all D.

If p+1 is a power of two and p≥31, B is odd. Apply the same p/2 count. Every 2-leaf must carry the full 2-part p+1≥32, whereas an exceptional subgroup has 2-part at most 8. Hence it lies in D, and the same order saturation applies. This includes p=31. The mixed-endpoint, connectedness and modulo-four arguments above finish these prime cases.

For p=23,47,53,59 take r=3. The Borels are 3-free. Dickson excludes A₅ at p=23,47,53 because p≡±2 mod5; all remaining exceptional groups have order at most p+1. At p=59, A₅ has order exactly p+1. The same saturation gives independent endpoint groups B and an order-(p+1) proper subgroup. The only types are D₂₄ or S₄ at 23, D₄₈ at 47, D₅₄ at 53, and D₆₀ or A₅ at 59. Each non-Borel type is even, so the collision argument gives one of each endpoint type per path and then c=1. The p=53 Borel is even and is excluded. For 23,47,59 each Borel is odd and coprime to its other endpoint, proving the exact factorization and existence.

For p=23 and 59 the [GAP certificate](../../update-2026-11-16/code/verify_psl2_exceptional_endpoints.g) (earlier public snapshot) gives respectively maximal-class lists [[D₂₄,1],[S₄,2]] and [[A₅,2],[D₆₀,1]] among subgroups of order p+1, and verifies that PGL₂(p) fuses the two exceptional classes. Dickson's order bounds ensure a subgroup of that order is maximal: it cannot be properly contained in a Borel, a smaller torus normalizer or any listed exceptional group. Once an endpoint X of order p+1 is fixed, coprimality makes X regular on the projective line, so all pairs (B,X) are simultaneously conjugate within that Aut(T)-class. Distinct endpoint abstract types give distinct loops by the reviewed path isomorphism criterion. Thus each prime has exactly two classes per k. The finite computation uses GAP's subgroup classification data and algorithms; it is not an independent reproof of that classification.

The small-prime frontier is substantive. Dickson supplies coprime exact pairs (C₇,S₄) in PSL₂(7), (C₁₁,A₅) and (11:5,A₄) in PSL₂(11), and (29:7,A₅) in PSL₂(29), the last Borel subgroup having index two in 29:14. Their orders multiply to |T|, so each gives a path for every k. These examples do not prove all folders at those primes are paths, or classify correlated leaf groups. The p-part count alone only bounds the number of p-bearing leaves from below; assuming equality without the second disjoint valuation would be invalid.

### Finite endpoint evidence

The certificate was run with GAP 4.15.1. It checks the PSL/PGL orders, maximal-subgroup class types and counts, and PGL fusion for p=23,59. GAP Reference Manual §39.19-5 supplies the `MaximalSubgroupClassReps` interface; the library classifications are external computational inputs.


### Scope and dependencies of the field and prime continuations

The extension and certificate depend on the canonical-folder, forest and path-isomorphism interfaces, Dickson’s classification, Zsigmondy’s theorem and GAP’s subgroup algorithms. The committed certificate was run with GAP 4.15.1 and its assertions passed. These checks do not establish a classification of unrestricted folders.

## Completing the odd nonprime fields and q=17

**Independently reviewed continuation.** Retain the preceding paired canonical hypotheses and source dependencies.

### Odd nonprime q≠9

The reviewed conclusion extends to q=p^f, p=3 or 5, f≥2, except q=9: no folders if q≡1 mod4, and exactly one Borel/nonsplit-normalizer path class per k if q≡3 mod4.

For f≥3, Zsigmondy as in the reviewed source provides r with ord_r(p)=2f; r≡1 mod 2f and r>5. At f=2,p=5 take r=13. Thus r|q+1, it does not divide p^d±1 for proper d|f, and it is absent from A4,S4,A5. Every r-bearing proper subgroup therefore lies in a nonsplit normalizer and is p-free. Unlike the p≥7 proof, exceptional groups may contain p, but their p-part is at most p, whereas the full p-part of T is p^f>p. Proper subfield groups have strictly smaller p-part. Consequently a subgroup with full p-part lies in a Borel: the remaining upper-triangular type has a normal full Sylow p-subgroup, and its normalizer is a Borel. The disjoint p/r leaf-support count and strip-forest order identity are exactly those in the reviewed valuation-saturation section. They force c paths, c p-leaves and c r-leaves, with full valuations at each, so the p-leaves lie in B and r-leaves in D. The equality |B||D|=|T| then forces full independent endpoint groups, and the reviewed collision, connectedness and endpoint-isomorphism proofs apply verbatim. No exceptional subgroup need be claimed p-free.

The only excluded nonprime field q=9 has p²+1=10 and r=5, so the r>5 exclusion of A5 fails; it is not resolved by this argument.

### q=17

Here |T|=2448=2^4·3²·17, |B|=136 and |D|=18. Take p=17 and r=3. Borels are 3-free and, by Dickson, every p-containing proper subgroup lies in a Borel; no A5 subgroup occurs because 5∤|T|. The only remaining exceptional groups A4 and S4 have 3-part 3, so every proper subgroup carrying the full 3-part 9 lies in a nonsplit torus normalizer. The p/3 disjoint-support and full-valuation count therefore gives paths and B/D containment exactly as above; order saturation forces the complete independent endpoint groups. Every path has one end of each type, and both B and D are even, so their involutions collide with the paired marked square as in the reviewed proof. Hence no folder exists for q=17.


Together with the reviewed [four exceptional prime classifications](../manuscripts/radical-free-small-psl2-paths.md) and [all even-field classification](../../update-2026-11-16/manuscripts/radical-free-even-psl2-paths.md) (earlier public snapshot), the only remaining field parameter in this paired PSL₂ model is q=9. Those continuations and the section above have the exact-source reviews at `184bc5f1b24d05d4dac1860060c6189afefda70c` recorded in their canonical sources; no conclusion about arbitrary PSL₂ overgroups follows.

The three independent mathematical reviews of this odd small-characteristic/q=17 continuation are recorded with the [even-field theorem](../../update-2026-11-16/manuscripts/radical-free-even-psl2-paths.md#independent-mathematical-review) (earlier public snapshot), at the common exact source `184bc5f1b24d05d4dac1860060c6189afefda70c`.


<a id="all-field-paired-psl-assembly"></a>

## All-field paired PSL₂ assembly

**Independently reviewed assembly at `e30af949531c0ebcc9f7533b04fc1e7fc6858563`.** Under the faithful canonical hypotheses G=PSL₂(q)^k×PSL₂(q)^k with pair-swapping inversion, every simple nonassociative folder is a single path, and its loop-isomorphism classes for every k≥1 are as follows. Here q is a prime power ≥4; D_n has order n; B_q has order q(q−1)/gcd(2,q−1). Exceptional rows are removed from the final two rows.

| Field size q | Endpoint pairs, up to reversal | Classes for each k |
| --- | --- | --- |
| q even | (B_q,C_(q+1)) | 1 |
| 5 | (A₄,C₅) | 1 |
| 7 | (7:3,D₈), (C₇,S₄) | 2 |
| 11 | (11:5,D₁₂), (11:5,A₄), (C₁₁,A₅) | 3 |
| 23 | (23:11,D₂₄), (23:11,S₄) | 2 |
| 29 | (29:7,A₅) | 1 |
| 59 | (59:29,D₆₀), (59:29,A₅) | 2 |
| Other odd q≡3 mod4 | (B_q,D_(q+1)) | 1 |
| Other odd q≡1 mod4 | none | 0 |

The proof is an assembly of the [A₅ result](../manuscripts/radical-free-a5-path-classification.md), [all even fields](../../update-2026-11-16/manuscripts/radical-free-even-psl2-paths.md) (earlier public snapshot), [four exceptional primes](../manuscripts/radical-free-small-psl2-paths.md), the preceding odd-field and prime arguments, and the new [PSL₂(9) exclusion](../manuscripts/radical-free-involution-support.md#paired-psl9-exclusion). The latter is the only new mathematical case. For prime q≥61 and all nonprime q other than 9 the preceding sections apply; among smaller primes the primitive-prime theorem covers 13,37,41,43, the separate arguments cover 17,23,31,47,53,59, and the linked small-prime and A₅ sources cover 5,7,11,19,29. Thus no field size is omitted.

Every listed loop has order |PSL₂(q)|^k and is proper and non-Bruck by the reviewed path construction. Its isomorphism criterion is the path length together with the endpoint pair up to common Aut(T) and reversal, as in the canonical path source; all orbit counts are proved in the linked family sources. The q=4 and q=5 rows describe the same T≅A₅ family and must not be counted twice. This is an exhaustive classification only for the specified paired canonical model, not for arbitrary loops with PSL₂ composition factors.


The three independent mathematical/source/code reviews of this assembly and its final q=9 input are recorded in [the parity source](../manuscripts/radical-free-involution-support.md#independent-review). Their acceptance retains all earlier input scopes; none asserts a classification outside this paired canonical model.
