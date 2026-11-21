# The even first-degree residue is extraspecial

**Supporting proof draft; no separate end-to-end review asserted.** [Verification and provenance](../VERIFICATION.md).

Retain the odd distinct prime pair $`p,q`$, $`p\mid q-1`$, $`f=\operatorname{ord}_q(p)`$, $`p\nmid f`$, $`d=pf`$, at the first degree $`p^{d+1}q`$. Write $`N`$ for the nonaxial core, $`\Phi=[N,N]\cong C_p`$, $`U=N/\Phi`$, and $`\bar W`$ for the image of $`W=H\cap N`$. The preceding theorem gives $`\dim U=2d`$, $`N`$ of exponent $`p`$, $`C_N(B)=\Phi`$, and the commutator rank $`d`$ or $`2d`$.

**Lemma.** The rank $`d`$ possibility cannot occur. In particular any first-degree nonaxial example still open (necessarily $`f`$ even) has an extraspecial exponent-$`p`$ core of order $`p^{2d+1}`$ and its actual $`\bar W`$ is a Lagrangian subspace (totally isotropic of dimension $`d`$).

**Proof.** The projected stabilizer $`J=HN/N`$ normalizes the $`q`$-axis $`B_2`$ and acts on it through a scalar of order $`p`$. The $`B_2`$-fixed part of $`U`$ is zero by absence of axial weights and by $`C_U(B)=0`$. Over a splitting field each nontrivial $`B_2`$-character has a joint orbit under Frobenius and this scalar of size $`\operatorname{lcm}(p,f)=d`$. Consequently every nonzero rational $`J`$-submodule of $`U`$, including one of $`\bar W`$, has dimension a positive multiple of $`d`$. As $`\dim\bar W=d`$, it is irreducible. Let $`R`$ be the radical of the alternating commutator form. If the rank is $`d`$, any nonzero projection $`\bar W\to U/R`$ is injective and hence onto, contradicting total isotropy of its image. Therefore $`\bar W=R`$. The actual intersection $`W\cap Z(N)`$ has order $`p^d`$ because $`W\cap\Phi=1`$ and $`R=\bar W`$. The original center orbit $`[Z(N):H\cap Z(N)]`$ has order $`p`$, but the signed packet lower bound gives at least $`p^{(d-f)/2}>p`$ inverted elements in $`Z(N)`$ (here $`f\ge3`$). They are actual marks and must hit distinct points of this orbit, a contradiction. At rank $`2d`$, $`Z(N)=\Phi`$, giving the stated extraspecial conclusion.

## An exact ambient group split and a test on the survivor

The odd exponent-$`p`$, class-two group $`N`$ has a canonical additive structure on its underlying set: write $`[x,y]=xyx^{-1}y^{-1}`$ and define $`x\oplus y=xy[x,y]^{-1/2}`$, where the half power is taken in the center. The class-two commutator identity directly gives symmetry and associativity of this addition; ordinary powers give scalar multiplication in $`\mathbb F_p`$. All group automorphisms preserve this structure. Coprime averaging for $`B`$ splits the additive $`N`$ as its fixed line $`\Phi`$ and its sum of difference images for $`B`$, the latter identifying with $`U`$ and stable under $`N_D(B)`$ and $`t`$. Thus $`N`$ is in Heisenberg coordinates, with product in these coordinates
```math
(u,z)(v,w)=(u+v,z+w+\tfrac12\omega(u,v)).
```
Here $`\omega`$ is the actual nondegenerate commutator form, with values in a chosen copy of $`\mathbb F_p`$.

In the proof of the predecessor, $`S`$ is a $`t`$-stable Sylow $`p`$-subgroup of $`N_D(B)`$, abelian with fixed subgroup precisely $`\Phi`$, and $`S/\Phi\cong C_p`$. The negative part $`P_0`$ of its plus/minus decomposition has order $`p`$. It normalizes $`B`$ and is inverted by $`t`$. Since $`N\cap N_D(B)=C_N(B)=\Phi`$ and $`N_D(B)=BS`$, the group $`X_0=B P_0`$ complements $`N`$ in $`D`$ and is $`t`$-stable. In the canonical additive split of $`N`$ above, the $`X_0,t`$ actions fix the center and act linearly and symplectically on $`U`$; no nonsplit ambient extension remains.

The projected stabilizer also obeys a stronger condition than isotropy:
```math
\bar W^g\cap U^- = \{0\}\qquad(g\in D),
```
where the conjugation action on $`U`$ factors through $`X_0`$ and $`U^-`$ is the negative eigenspace of $`t`$. Indeed a nonzero vector $`u`$ in the intersection has an inverted lift $`(u,0)`$ in the physical mark set. It also has some lift in $`W^g`$. In a Heisenberg group, conjugation by an element with vector $`v`$ changes the central coordinate of the latter lift by the linear functional $`\pm\omega(v,u)`$; nondegeneracy and $`u\ne0`$ make all central coordinates attainable. Since $`N`$ acts trivially on $`U`$, this puts the inverted lift in a conjugate point stabilizer, impossible for a nonidentity mark in a sharply transitive set. Thus the problem left at even $`f`$ has a genuine symplectic complement test on the original stabilizer, not just a dimension count. This is a necessary condition; it does not verify avoidance for marks above the nontrivial $`q`$-axis or $`p`$-top.

No new computational premise is used. These deductions depend on the exact inherited prime-pair hypotheses and do not establish first-degree uniqueness when $`f`$ is even.
