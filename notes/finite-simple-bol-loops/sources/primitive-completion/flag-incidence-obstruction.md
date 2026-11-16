# An obstruction for incidence-flag actions

Mira Cult
**Status:** Independently reviewed under the exact scope recorded below. This is a bounded continuation of `0323-finite-simple-non-moufang-bol-loops:C0010` and no CFSG assumption. The loop consequence uses C0008 Lemma 2.1. The theorem concerns the specified action on graph edges; the occurrence, primitivity, and full almost-simple stabilizer of a particular classical flag action are separate questions.

## Theorem

Let $`B`$ be a finite connected simple bipartite $`d`$-regular graph, $`d\ge3`$, with distinct neighborhoods for distinct vertices on the same side. Put $`\Omega=E(B)`$. No automorphism of $`B`$ maps **every** edge to a distinct edge sharing an endpoint with it. Consequently, no loop on $`\Omega`$ has multiplication group contained in the induced action of $`\mathop{\mathrm{Aut}}\nolimits(B)`$ on its edges.

*Proof.* Write the two sides as $`X,Y`$. Connectedness makes each automorphism either preserve or swap the sides. Regularity implies $`|X|=|Y|=N`$ and $`|E(B)|=Nd`$.

Suppose first that $`g`$ preserves the sides, acting as $`f:X\to X`$ and $`h:Y\to Y`$. If every edge $`(x,y)`$ moves to a distinct edge sharing an endpoint, then exactly one of $`f(x)=x`$ and $`h(y)=y`$ holds on every edge. The fixed-status indicators at adjacent vertices are therefore opposite. Connectedness forces one entire side to be fixed pointwise, and the other side to be moved pointwise. But fixing all vertices of one side fixes the other side as well: each vertex on the other side has its neighborhood preserved, and distinct vertices have distinct neighborhoods. This contradiction rules out type-preserving $`g`$.

Now suppose $`g`$ swaps the sides. Write $`g(x,y)=(f(y),h(x))`$, where $`f:Y\to X`$ and $`h:X\to Y`$ are bijections. An edge can share an endpoint with its image only if $`x=f(y)`$ or $`y=h(x)`$. The first condition holds for at most one edge per $`y\in Y`$, and the second for at most one edge per $`x\in X`$. At most $`2N`$ edges can meet either condition, fewer than $`Nd`$ when $`d\ge3`$. This rules out type-swapping $`g`$.

For the loop consequence, choose distinct adjacent edges $`e,a`$, where $`e`$ is the loop identity; such an $`a`$ exists since $`d\ge3`$. For every $`z\in\Omega`$, the right translation $`R_z`$ maps $`(e,a)`$ to $`(z,L_a(z))`$. If the multiplication group lies in the induced graph automorphism group, $`L_a`$ sends each edge to a distinct adjacent edge, contradicting the first part. This is also the UOD principle of C0008 Lemma 2.1. $`\square`$

## Classical example and limits

Let $`B`$ be the incidence graph of projective points and totally isotropic lines of a nondegenerate four-dimensional symplectic space over $`\mathbb F_q`$, $`q\ge2`$. Each point is incident with $`q+1`$ isotropic lines and each line with $`q+1`$ points. The graph is connected: collinear points are connected through their line, while for noncollinear points $`x,y`$, any point in $`x^\perp\cap y^\perp`$ is collinear with both. Distinct points lie on at most one common line, and distinct lines meet in at most one point; as $`q+1\ge3`$, the two sides are twin-free. Thus the theorem excludes loop multiplication groups contained in the **full incidence graph automorphism action** on incident point–line flags, including automorphisms that interchange the two types. This application does not assert that a particular almost-simple extension acts primitively on these flags or identify its full group; those are separate action-interface checks.

The bound $`d\ge3`$ is sharp. The 6-cycle is connected, simple, bipartite, 2-regular, and twin-free. Rotation acts regularly on its six edges; the cyclic group of order six gives a loop whose multiplication group is contained in that edge action. Each rotation by one edge sends every edge to a distinct adjacent edge.

## Faithful quotient observation

More generally, let $`P`$ act on a set $`\Omega`$ preserving an equivalence relation with at least two classes and at least one class containing distinct points. If the induced action on $`\Omega/{\sim}`$ is faithful, no loop on $`\Omega`$ has multiplication group contained in $`P`$. Indeed, choose $`a\ne e`$ with $`a\sim e`$. C0008 UOD implies $`y\sim L_a(y)`$ for all $`y`$, so $`L_a`$ acts trivially on the quotient and hence on $`\Omega`$, impossible. This covers type-preserving flag actions with a faithful constituent projection. The graph theorem is stronger in its stated setting because it also covers automorphisms exchanging the two vertex types.

Independent review should check the edge-action conventions, the symplectic incidence example and small fields, and any use of the result in a specific primitive almost-simple classification.


automated reviewers a separate automated checker accepted the argument at its recorded source revision, checking both type-preserving and type-swapping automorphisms, the twin-free condition, the symplectic q≥2 example, the six-cycle boundary and faithful-quotient deduction. The loop consequence uses C0008 Lemma 2.1. The review does not identify the full group or primitivity of any other almost-simple flag action.
