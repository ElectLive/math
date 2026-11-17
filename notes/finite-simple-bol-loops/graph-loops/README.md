# Graph-native Bruck and Moufang loops

Mira Cult

This construction turns graph edges into actual associators of a loop, rather than adding a fixed nonassociative factor to a graph encoding. The resulting algebra also classifies maximal associative subloops through dominating vertex sets. The underlying integration mechanisms are established work of Kepka and cubic/code-loop theory; the precise specializations, intrinsic recovery and subloop results are proved in the linked manuscripts.

## A multiplication determined by edges

Let Γ be a finite simple graph, K a commutative unital ring, W the free vertex module, and Z the quotient of the exterior square of W by the generators corresponding to nonedges. Put B(u,v)=[u∧v]. On K⊕W⊕Z define

```math
(a,u,s)*(b,v,t)=(a+b,u+v,s+t+(a+2b)B(u,v)).
```

This is a left Bruck loop. Its central associator is

```math
D((a,u),(b,v),(c,w))=aB(v,w)-bB(u,w)-2cB(u,v).
```

Thus the associator on the marker and two vertex vectors is their edge generator, or zero for a nonedge. Edgeless inputs are groups. The law is Moufang exactly when 3B=0; nonzero edge data over a prime field of characteristic other than three give proper Bol loops. Over F_p the order is p^(1+|V|+|E|).

At each fixed prime, this Bruck family determines the ordinary graph up to **unmarked loop isomorphism**. The proof extracts the relevant alternating-map data intrinsically, handles star exceptions, then uses He–Qiao's established all-field graphical alternating-map theorem. A separate binary cubic construction gives graph-native Moufang loops, also with unmarked graph recovery.

## Structural payoff

Over a prime field F_p with p≠3 and a graph having an edge, all maximal associative subloops are classified. Besides the marker-zero group, they correspond to a dominating vertex set S and a full-support line on each connected component of the induced graph Γ[S]. If c(S) is its number of components, S contributes

```math
(p-1)^{|S|-c(S)}
```

groups, each of order p^(|E|+1+c(S)). These groups are elementary abelian. The repeated-argument proper-Bol associator eliminates affine placements; binary and ternary Moufang suspensions retain a precisely counted affine factor. A six-vertex example shows that these counts do not determine the graph, although the full loop does.

## Complete manuscripts

- [All-ring Bruck law, unmarked recovery and Eisenstein coefficients](manuscripts/graph-eisenstein-loops.md).
- [Binary cubic Moufang law and unmarked recovery](manuscripts/graph-cubic-loops.md).
- [Associative subloops, domination and comparisons with established constructions](manuscripts/graph-associative-subloops.md).

Directed and colored versions retain specified markings. Arbitrary unmarked recovery of colors or directions is not claimed. Eisenstein coefficients distinguish negation, conjugation and color rotation; finite quotients and zero divisors are treated explicitly. Graph morphisms are isomorphisms and the stated induced embeddings, not all graph homomorphisms.

## Evidence and boundary

[Publication record](PUBLICATION.md) · [Independent research review](evidence/graph-loops-review.md) · [Executable checks](code/README.md) · [References](REFERENCES.md) · [Public claim 0092](../claims/0092.md).

The complete proofs have scoped independent model reviews and explicit established dependencies. This is not human refereeing, formal verification or an exhaustive novelty certification. Graph deletion is a specified algebraic quotient/retraction, not deletion of one loop element. Neither graph reconstruction nor finite-simple Bol classification is solved. These central extensions are not a new family of nonassociative simple loops.
