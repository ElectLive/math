# Optimal quadratic logarithmic cost of universal group hosts inside simple Bol left groups

**Mira Cult**

The loop realization uses the preceding [nonabelian projective construction](multiplicity.md). The abstract group embedding and lower bound below are independent of its computational base matrices. A subgroup of the *left multiplication group* is not being identified with a subloop of the native loop.

**Theorem.** For every $`k\ge1`$ put $`s=\max(k,\binom{k}{2})`$. There is a **single** finite simple proper left Bol loop $`Q_k`$ of order $`20\cdot3^{119+38s}`$ and exponent six whose canonical group of left translations has solvable radical $`P_k`$ of order $`3^{236+76s}`$, class exactly two and exponent three. Every finite group $`F`$ of nilpotency class at most two and exponent dividing three with $`|F|\le3^k`$ embeds in $`P_k`$. One can choose the embedding so that $`F\cap Z(P_k)=Z(F)`$ after identification. The ambient loop, its marked native structure and its radical are **fixed independently of $`F`$**. The signed quotient is the same native projective construction with $`G/P_k\cong\operatorname{PSL}_2(19)`$.

The dependence $`\log_3|P_k|=O(k^2)`$ is optimal in order of growth **even if arbitrary finite group hosts are permitted**. In fact, if a finite group $`D`$ contains isomorphic copies of all such $`F`$, then for $`t=\lfloor k/3\rfloor\ge2`$,

```math
\log_3 |D|\ \ge\ t^2-4t+\frac1{2t}.
```

This is a cost bound on the hosting **group**, not a lower bound of exponential-quadratic order on the size of every conceivable Bol loop that realizes these embeddings. It does not classify all groups arising as *the whole* radical, nor claim a family of subloops of the indicated types.

## 1. A fixed universal mixed bracket

Write $`\mathbb F=\mathbb F_3`$ and use the 19-dimensional projective augmentation module $`M`$ for $`T=\operatorname{PSL}_2(19)`$. Its symmetric product is $`\beta(a,b)=(a_i b_i)_i-\frac1{20}(\sum a_ib_i)\mathbf{1}`$ on 20 actual coordinate sites. Fix $`e=e_0-e_\infty`$ once and put $`w=\beta(e,e)\ne0`$ (the two nonzero sites of $`e`$ show this). Use the preceding source with $`s`$ passive and $`s`$ active pairs, and any of its admissible detector-preserving shears. In the true radical $`P`$ the underlying vector space has coordinates including active plus/minus vectors $`(x_\alpha,y_\alpha)\in M^2`$ per slot, and passive minus vectors $`z_h\in M`$, all central in $`P`$. Its group product is $`u*v=u+v+\tfrac12[u,v]`$ where the only nonzero commutator coordinates are

```math
[u,v]_h=\sum_{\alpha,\gamma}(C_h)_{\alpha\gamma}
   \bigl(\beta(x_\alpha,y'_\gamma)-\beta(x'_\alpha,y_\gamma)\bigr).
                                                               \tag{1}
```

All symmetric coefficient matrices $`C_h`$ are permitted, arbitrary unused slots and dependent outputs included; the earlier proof checks *the native* left Bol operation, all normal cuts, true torus avoidance and exact generation rather than just the additive quotient.

Name distinct active slots $`(i,j)`$ for $`i,j\ge1,\ i+j\le k`$; there are $`\binom k2`$. Name $`k`$ distinct passive outputs. Define $`(C_1)_{(i,1),(i,1)}=1`$ for the existing such slots. For $`j>1`$ put $`(C_j)_{(i,1),(i,j)}=(C_j)_{(i,j),(i,1)}=1`$ whenever $`(i,j)`$ exists. Set every other entry to zero. If $`k=1`$ there are no triangular slots; put one 1 on the first diagonal of $`C_1`$ instead. For $`k\ge2`$ the slot $`(1,1)`$ is present, so in all cases the radical has class exactly two. No input group has entered the choice of these arrays.

Recall directly the coordinates for any $`F`$ in the class. Write $`Z=Z(F)`$ and $`V=F/Z`$, with $`c=\dim Z`$, $`d=\dim V`$ so $`c+d\le k`$. The commutator descends to the alternating bilinear map $`\omega:V^2\to Z`$ since commutators are central. The underlying elements of $`F`$ form an additive $`\mathbb F`$-space under $`a+b=ab[a,b]^{-1/2}`$ (commutator convention $`[a,b]=a^{-1}b^{-1}ab`$). Indeed centrality gives additivity of the commutator separately, so the two expansions of $`(a+b)+c=a+(b+c)`$ have the same three correction factors. Swapping $`a,b`$ leaves this sum unchanged, and repeated sums of one element are its ordinary powers. Split off the additive subspace $`Z`$. In these coordinates the group law is $`(v,z)*(v',z')=(v+v',z+z'+\omega(v,v')/2)`$, also for abelian $`F`$ with $`d=0`$.

Choose ordered bases $`v_i`$ of $`V`$ and $`z_j`$ of $`Z`$, and write $`\omega_j`$ for the components. Send $`z_j`$ to $`w`$ in passive central slot $`j`$. For each $`v_n`$, put $`e`$ in active **plus** slot $`(n,1)`$, and in active **minus** slot $`(i,j)`$ put $`\omega_j(v_i,v_n)e`$ for every $`i<n`$ and $`1\le j\le c`$. All other coordinates vanish. For $`d>0`$ we have $`c\ge1`$, so $`(n,1)`$ exists, and $`i+j\le d+c\le k`$ throughout. Extend additively to $`V\oplus Z`$. This is injective by the separate plus and passive coordinate readings. For $`i<n`$, the image bracket computed from (1) has precisely $`\omega_j(v_i,v_n)w`$ in output $`j`$. The negative summand is zero because the earlier vector's minus support has only row indices below $`i`$. The symmetric transposed entry for $`j>1`$ contributes no other term, since all plus inputs have column index 1. Hence all brackets and the actual group law are preserved. True central elements go to passive vectors, and a noncentral element of $`F`$ already has a nontrivial commutator within its own copy, proving the center assertion.

The arrays do **not** encode one target bracket chosen after $`F`$ is known: changing $`F`$ changes just its subgroup in this particular native radical. For an abelian $`F`$ all generators land in passive coordinates. We make no claim that all these embeddings are characteristic, normal, pairwise disjoint or retracts.

## 2. Every arbitrary host pays quadratically

Fix $`t\ge2`$, $`3t\le k`$, and let $`V=\mathbb F^{2t}`$, $`Z=\mathbb F^t`$, $`h=\binom{2t}{2}`$. Fix one nonsingular alternating form $`B_1`$ on $`V`$. Choose successively $`B_j`$ for $`2\le j\le t`$ linearly independent of the preceding ones in the $`h`$-space of alternating forms. There are precisely $`\prod_{j=1}^{t-1}(3^h-3^j)`$ ordered choices. Use $`(B_j)`$ as the central-valued bracket in the class-two product above. The resulting group has order $`3^{3t}`$ and exponent three. Its center is exactly $`Z`$ because $`B_1`$ is nondegenerate, and its derived subgroup is $`Z`$ since independent coordinate forms make $`\bigwedge^2V\to Z`$ surjective.

An abstract group isomorphism induces linear isomorphisms on its true center/derived subgroup and quotient preserving the bracket. Thus each isomorphism type accounts for at most $`|\operatorname{GL}_{2t}(3)|\,|\operatorname{GL}_t(3)|<3^{5t^2}`$ of the displayed tuples. Possible central changes of section do not change this pair of induced linear maps or its action on the tuple. Each factor $`3^h-3^j`$ is at least $`3^{h-1}`$, so we obtain at least $`3^{(t-1)(h-1)-5t^2}=3^{2t^3-8t^2+1}`$ isotypes. Lifts of a basis of $`V`$ generate each group: their commutators already span $`Z`$. The total number of possible subgroups of an arbitrary finite group $`D`$ generated by an ordered $`2t`$-tuple is at most $`|D|^{2t}`$, counting more than just isotypes. Combining bounds proves the displayed inequality. In particular the logarithmic cost order is sharp. No historical assertion of novelty of universal class-two groups as an abstract group-theoretic object is intended; the host here is the actual canonical radical at a controlled native simple loop order.

[Review and reproduction](../verification.md) · [Overview](../README.md)
