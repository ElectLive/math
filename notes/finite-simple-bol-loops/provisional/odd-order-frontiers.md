# Odd-order research beyond the reviewed theorems

**Status:** these are proposed extensions and open audit targets, not entries in the reviewed catalogue. They should not be cited as consequences of the [1053 lower bound](../odd-degree/README.md), [Sylow counterexamples](../odd-bol-hall/README.md), or [extraspecial constructions](../extraspecial-cores/README.md).

## Which multiple of a prime can first support a simple loop?

Let $`p,q`$ be distinct odd primes and consider nonassociative simple left Bol loops of order $`p^a q`$. The [reviewed threshold](../odd-degree/manuscripts/two-prime-exponent-threshold.md) requires $`q>p`$ and $`a\ge p+1`$ and characterizes existence at $`a=p+1`$. It does not classify the first possible exponent for every fixed pair.

The stronger proposed answer is: such a loop exists at *some* exponent precisely if $`p\mid q-1`$, and then
```math
 a_{\min}(p,q)=1+\mathrm{lcm}\big(p,\mathrm{ord}_q(p)\big).
```
The positive direction and the obstruction to smaller exponents are separate. The latter must rule out nonabelian normal $`p`$-cores, not just establish the extremal dimensions of abelian modules. The candidate proof controls the actual stabilizer on the Frattini quotient and tests whether the central pairing can occur in a signed normal cut. At the boundary $`a=p+1`$ a separate rigidity argument proposes uniqueness. **No fixed-pair uniqueness beyond its stated cases is inferred.**

At the proposed first exponent, write $`f=\mathrm{ord}_q(p)`$. An abelian-core model is proposed to give one class. The additional possibilities when $`f`$ is even and prime to $`p`$ would come from graph stabilizers on two matched character spaces of an extraspecial core, with either preserved or exchanged spaces. In this residual case the proposed total is $`p+1+\sum_i D_i`$, where $`1\le i<f/2`$ and $`f/\gcd(f,i)`$ is odd or divisible by four. Here $`D_i`$ counts orbits of $`j\mapsto pj+(p-1)/2`$ modulo $`\gcd(p^{f/2}+1,p^i-1)`$. The proof must cover *all* stabilizers and the actual signed orbit relation, including nonsplit input groups. Earlier counts for only the preserved-space charts are not totals. The [reviewed two-prime constructions](../extraspecial-cores/README.md) do not rely on these necessary-direction arguments.

## Inside and outside exact factorizations

For faithful Nagy exact factorizations with an **abelian** $`p`$-core at order $`p^a q`$, a proposed integral classification uses cyclic necklaces. At top order $`p^k`$ put $`d_k=\mathrm{lcm}(p^k,f)`$. The necklace has $`(q-1)/d_k`$ entries in $`\{0,\dots,k\}`$ with maximum $`k`$, taken up to **rotation only**; only $`1\le k\le v_p(q-1)`$ occurs. The claimed exponent of $`p`$ in the order is $`k+d_k\sum_i e_i`$. The recognition of the actual factors, not just construction from a necklace, remains to be independently audited. This is not a parametrization of all two-prime Bol loops.

Conversely a proposed nested construction has order $`p^{1+\mathrm{lcm}(p,f)+rpf}q`$ at stage $`r\ge0`$ and whole right nucleus $`C_p`$. The candidate invariant at strictly positive stages is a common moved subspace for the two normal $`q`$-axes; it would distinguish these loops even up to isotopy from all faithful exact-factorization loops. This is distinct from the independently reviewed nonisotopy of the extraspecial constructions.

## Original loop, principal isotope, associated Bruck loop

- **Compatible Hall systems.** For a finite odd-order Bol loop an author argument seeks one principal isotope with a simultaneous family of Hall subloops for *all* sets of primes, compatible under meet and join. Existence at that selected basepoint does not mean existence at every basepoint. There is a different sufficient arithmetic condition for the original basepoint: draw $`p\to s`$ between distinct primes dividing the order $`n`$ when $`p\mid s^j-1`$ for some $`1\le j\le v_s(n)`$. The proposal obtains a compatible native Hall family for sets with no outgoing arrow. It would imply that 63 is the **least odd** Hall–Sylow failure; this lower bound is separate from the [reviewed example of order 63](../odd-bol-hall/README.md).
- **Subsquare geometry.** In the Heisenberg family, changing the distinguished identity may change the number of full-$`p`$ subloops even on a common Latin square. The proposed order-63 isotope census has counts 49, 7 and 0 in three isomorphism classes although the square has 343 order-nine subsquares. A separate proposed obstruction counts unpointed full-$`p`$ subsquares modulo $`p`$ directly from an ordinary incidence-graph deck. It is a recognition test, not a proof of a native Sylow theorem.
- **Bruck direct products.** A proposed native transfer says splitting across complementary prime sets holds for the odd-order loop exactly when it holds for its associated Bruck loop, on the same two characteristic subsets. It also compares the Fitting heights and noncentral chief-factor actions of their true left groups. It does *not* identify the two point stabilizers or assert that solvability of a translation group alone proves classical solvability of the loop.
- **A full Bruck fiber.** For a specified, labeled finite odd Bruck loop, a different construction seeks to describe every Bol multiplication with that very associate by subgroups of one bounded, explicitly constructed signed central cover. It does not solve the subgroup test for arbitrary nonabelian associates. The [abelian-associate normal form](../odd-degree/manuscripts/abelian-bruck-fibers-as-alternating-algebras.md) is a separately reviewed and more explicit result.

[Back to provisional research](README.md)
