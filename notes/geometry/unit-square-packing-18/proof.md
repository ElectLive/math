# Proof of the 18-square optimum

Put $`H=(7+\sqrt7)/2`$. The upper bound is an exact placement. The lower bound consists of geometric implications valid for continuous pose domains, and a finite certificate that these implications cover every pose below $`H`$.

## An exact placement at the proposed side

The [coordinate table](replay/six-tilt18.json) gives each center’s two coordinates as pairs $`(a,b)`$ representing $`a+b\sqrt7`$. Its orientation bit selects either the usual horizontal and vertical axes or the orthonormal frame with first vector

```math
u=\left(\frac{1+\sqrt7}{4},\frac{\sqrt7-1}{4}\right)
```

and second vector the quarter-turn of $`u`$. For a unit square of center $`p`$ and axes $`u,v`$, the projection interval onto direction $`d`$ has center $`d\cdot p`$ and radius $`(|d\cdot u|+|d\cdot v|)/2`$. With the two container-axis directions this gives four inequalities per tile. For two tiles, a separating axis can be one of their four axes; the center projections then differ by at least the sum of the two radii. Equality is allowed. The [exact checker](replay/six_tilt18.py) verifies 72 wall inequalities and a separating axis for each of the 153 pairs. Signs in the quadratic field are decided by rational comparisons, squaring when the two terms have opposite signs.

## Covering every possible assignment

Suppose a packing exists in a square of side $`L<H`$. Use the wall directions as coordinates and translate it inside a test box of side $`U=4.822876>H`$. The packing remains physically enclosed in its original smaller square. The test box bounds poses; it does not supply artificial contacts or substitute for the true walls in the lower-bound inequalities.

The [21-point rack](replay/stabs18-endpoint-window.json) is invariant under the eight symmetries of the test box. Every unit square inside it contains a rack point even after concentric contraction by the certified positive margin. To verify this over continuous orientations, use the rational half-angle parameter $`t=\tan(\theta/2)`$. On a parameter interval $`[a,b]`$, the angular difference from the midpoint frame is at most $`b-a`$ since the derivative of $`2\arctan t`$ is at most two. A rotated unit box has support inflation at most one plus this angular difference. Thus a midpoint-frame square of half-side $`(1-\varepsilon)/(2(1+b-a))`$ is contained in every contracted tile on the interval. A center box using the smaller endpoint wall half-width encloses all feasible centers, since $`\cos\theta+\sin\theta`$ has no interior minimum in the first quadrant. In the midpoint frame one checks that the union of the 21 smaller squares centered at the marks covers this outer center polygon: between consecutive rectangle or polygon events the active rectangles are fixed, and their vertical interval union must cover the polygon strip projection. Endpoints are checked as well. [The verifier](replay/check_stabs.py) makes those rational tests, bisecting unproved angle intervals rather than sampling orientations.

For each tile choose a rack point closest to its center in the tile’s own rotated maximum norm. The strict hit implies that every minimizing point is interior. No two tiles select the same point, because their interiors are disjoint. No tie is removed, and the set of permitted choices respects the actual box symmetries. Unselected points are not assumed to be outside the tiles. The case code explicitly covers all $`\binom{21}{18}=1330`$ occupied subsets by 187 orbits. Within each orbit every tile keeps its own continuous center and angle variables.

## Which changes to a pose domain are safe?

The [enclosure code](replay/lattice_kernel.cpp) keeps an outer center polygon for each tile and live angle interval. It starts from the wall inset and ownership inequalities. Nearest-point comparisons only remove a center region when another mark is *strictly* nearer throughout the angle interval. A signed linear inequality in the cosine and sine that is strict at both endpoints stays strict along their positive conic interpolation. Center and angle subdivisions use both closed sides, so a pose on a subdivision boundary survives in the cover.

At a live angle interval, a rational polygon strictly inside every rotated tile in that interval is an inner shape. For two inner shapes, their Minkowski sum specifies forbidden center differences: membership in its open interior forces overlap. Holding the other tile’s possible centers and angle intervals as a whole, one removes only centers forbidden for **every** such choice. This check uses support inequalities of the sum; one takes the union of the remaining closed exteriors and encloses it outward, never cutting away a feasible boundary. The kernel can also grow a common guaranteed-interior polygon for each tile. Two such polygons intersecting already contradict disjoint interiors, as does a tile losing its entire center domain in every angle interval.

Polygon intersections are rounded outward: the exact intersection is enclosed by its coordinate floor/ceiling box in integer lattice units, and the convex hull retains it. Lattice units represent bounds on real positions, not a restriction that a center be on a grid. Floating-point code may propose interior lattice points; they are included only after exact integer tests certify them for every live interval. A failed proposal cannot reject a case. The [driver](replay/verify_exact_18.py) regenerates the domains, checks cuts and coverage, and requires a valid terminal for every branch.

## How a branch can accommodate equality and still prove the bound

The six cases that may retain poses use three closely related terminal tests. They pick actual tiles inside the branch and bound projections with respect to the *true* walls of their side-$`L`$ container.

**Wall rows and a traversing segment.** A vertical probe crossing a tile’s opposing sides with near-horizontal axis $`(c,s)`$ contributes a chord of length $`1/c\ge 1`$. If it crosses a row of $`p`$ such tiles with terminal upper-right corner $`R`$, then in true wall coordinates $`R_y\ge p+(R_x-\xi)s/c`$, where $`\xi`$ is the probe abscissa. The wall also gives $`R_x\ge c+\max(0,-s)`$. The checked open probe interval places $`\xi`$ so that, for the positive unit direction $`(a,b)`$ used in the terminal test, these imply $`aR_x+bR_y\ge a+pb`$. Indeed $`a(c-1+\max(0,-s))+b(R_x-\xi)s/c\ge0`$ by the probe guard. Apply this bound at the terminal corner $`P`$ of a three-tile row and in the reflected frame at the corner $`Q`$ of a two-tile row. Translation offsets cancel and the resulting support is at most $`(L-3)a+(L-4)b`$. A segment from $`P`$ to $`Q`$ that crosses two distinct tiles from opposite face to opposite face has length at least two; disjoint interiors prevent its two chord lengths from overlapping. The [wall guard](replay/wall_chord_guard.py) verifies the probe and crossing inequalities over the whole pose enclosure, not just a chosen placement.

**Two native separating faces.** The [two-face guard](replay/genuine_facing_bridge.py) uses the same row support without requiring a common traversing segment. Let the selected middle tiles have centers $`f,g`$ and forward unit normals $`u,v`$. Write $`c=u\cdot v>0`$, $`s=u\cdot Jv`$ for the quarter-turn $`J`$. The guard requires $`u\cdot(f-P)\ge1/2`$, $`v\cdot(Q-g)\ge1/2`$, and certifies that a true separating axis directed from the first tile to the second is either $`u`$ or $`v`$. If it is $`u`$, the middle center gap along $`u`$ is at least $`(1+c+|s|)/2`$. The remaining transverse term is $`s\,Jv\cdot(Q-g)`$. The guard checks $`1/2+\mathrm{sign}(s)Jv\cdot(Q-g)\ge |s|/(1+c)`$ when $`s\ne0`$. Adding the three projections then gives at least $`1+c+s^2/(1+c)=2`$. With axis $`v`$ the analogous test is $`1/2-\mathrm{sign}(s)Ju\cdot(f-P)\ge |s|/(1+c)`$. Thus the two independently varying normals need not agree.

**Perpendicular probes at one corner.** The [perpendicular-probe guard](replay/double_probe_bridge.py) can use both a vertical and a horizontal row ending at the same physical corner $`(p,q)`$. For counts $`v_0,h_0`$ and probe coordinates $`\xi,\eta`$, the chord-length bounds give $`q\ge v_0+(p-\xi)s/c`$ and $`p\ge h_0-(q-\eta)s/c`$. Choose the probe offsets in ratio $`1:b/a`$ so the tilt errors cancel in $`ap+bq`$. This gives the corner support $`ah_0+bv_0`$. Applying it at opposite corners with total row counts 4 and 3 gives the same projection allowance as above, possibly with coordinates exchanged. A chord or two-face test again pays at least two. The rows do not need disjoint sets of tiles across the two probes; the proof combines support inequalities, not counts of tile areas.

In all three cases, Cauchy–Schwarz with coordinatewise positive parts gives

```math
2\le\sqrt{(L-3)_+^2+(L-4)_+^2}.
```

This is impossible for $`L\le4`$. For $`L>4`$, squaring gives $`2L^2-14L+21\ge0`$, and therefore $`L\ge H`$. A branch may contain a real packing at equality and still certify this implication.

## Completing the cover

The [case map](replay/README.md) records 235 empty terminal regions accounting for 181 full orbits. Six other orbits contribute 193 terminal regions with either exact emptiness or one of the three verified lower-bound tests. For case 82, the verifier uses a true reflection of the entire pose inside the same orbit: the base roots outside three specified regions are retained, and the other roots are intersections with reflected partner regions. Both sides of subsequent cuts are checked. Case 115 instead keeps all its base roots without this reflection. The full replay checks the cover and every terminal, a total of 428 regions. Thus an arbitrary hypothetical placement below $`H`$ falls into a terminal that is impossible or that forces $`L\ge H`$. Together with the exact placement this proves the theorem.
