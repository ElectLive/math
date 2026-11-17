# Charged Heisenberg fusion, torus degree, and the cocycle boundary

**Mira Cult**



This note tests a stronger charged object than the pointwise class algebra.
The retained two axes of the canonical class-two folder give genuine
Schrödinger modules and explicit tensor intertwiners. On a torus, their
projective commutator forces degree data and an integer extension of the
finite charge group. The extension gives actual holomorphic bundle maps
with coherent carry lines. It does not yet give a Bol-specific interacting
vertex algebra. Two exact limitations are essential: the forced neutral
zero algebra can be nonabelian, and central cocycle phases disappear in
unmarked neutral fusion networks.

The canonical group/folder, positive cocycle, and strict-isomorphism inputs
are those of [CF0--CF1](bol-translation-class-fusion.md). This note neither
changes nor reproves their classification. The torus exchange problem and
its remaining fusion obstruction are in
[the charged exchange manuscript](bol-charged-exchange.md). The different
attempt to put the actual loop product into matrix-current residues is
audited in [LC1--LC3](bol-local-current-obstruction.md).

## CH1. The marked axes give a genuine charged representation

Work at an odd prime $p$. Let $W,Z$ be finite-dimensional
$\mathbb F_p$-spaces and let $b:W\times W\to Z$ be the bilinear
map in the retained class-two normal form. The local group is


```math

 P=(W\oplus W)\oplus Z,

```



```math

 (x,y,z)(x',y',z')=
 \left(x+x',y+y',z+z'+\tfrac12[b(x,y')-b(x',y)]\right).
 \tag{CH1}

```


Its ordered axes are $S=\{(x,0,0)\}$ and
$\tau S=\{(0,y,0)\}$. They are part of the marked folder interface,
not a chosen polarization of an unmarked alternating space. Put
$\psi(t)=\exp(2\pi it/p)$. For $\ell\in Z^*$, define
$H_\ell=\operatorname{Fun}(W,\mathbb C)$, with counting inner product,
and


```math

 (\rho_\ell(x,y,z)\phi)(u)=
 \psi\!\left(\ell(z+b(u,y)+\tfrac12b(x,y))\right)\phi(u+x).
 \tag{CH2}

```


**Proposition CH1.** Equation (CH2) is a unitary representation of the
actual group $P$, with central character $\psi\circ\ell$. If
$b_\ell=\ell\circ b$ is nondegenerate, it is irreducible and has
dimension $|W|$. The construction is functorial under linear marked
data isomorphisms preserving the ordered axes and transporting $b,\ell$.

**Proof.** Composing (CH2) twice gives the phase


```math

 \ell\left(z+z'+b(u,y+y')+b(x,y')
          +\tfrac12b(x,y)+\tfrac12b(x',y')\right).

```


This is exactly the phase obtained by inserting (CH1) into (CH2).
Translations of $u$ and root-of-unity multipliers are unitary. Central
elements act by the stated scalar. If $b_\ell$ is nondegenerate, its
second-axis operators are all diagonal characters of $W$. An operator
commuting with them is diagonal; commuting also with all first-axis
translations makes that diagonal constant. Thus the commutant is scalar,
which proves irreducibility. Transport of the coordinate variable gives
the stated functoriality. QED.

No nondegeneracy is needed for the representation formula itself. When
$b_\ell$ is degenerate, $H_\ell$ need not be irreducible. We will
state explicitly where invertibility is used. Its left and right radicals
need not coincide. If $r=\operatorname{rank}b_\ell$, the radical of
the alternating form on $W\oplus W$ is the direct sum of those two
radicals; the quotient is a nondegenerate alternating space of dimension
$2r$. In the fixed central-character group algebra, Fourier
decomposition along this radical gives a packet of full matrix blocks of
size $p^r$: choose any complementary nondegenerate alternating space
and apply the orthogonal Weyl-basis argument below. Thus every irreducible
constituent has dimension $p^r$, but its radical character is additional
data. This does not canonically select one constituent or identify the two
radicals. The all-module bundle construction in CH4 requires no such choice.

In the source semidirect normal form, a torus element $a$ acts by
$(R(a),R(a)^{-1},T(a))$, with


```math

 b(R(a)x,R(a)^{-1}y)=T(a)b(x,y).

```


Consequently $a\cdot\ell=\ell\circ T(a)^{-1}$ and


```math

 (A_a\phi)(u)=\phi(R(a)^{-1}u):H_\ell\longrightarrow H_{a\cdot\ell}
 \tag{CH3}

```


intertwine the conjugated $P$-actions. They compose according to the
torus product. The direct sum of these spaces therefore has an actual
representation of the corresponding local semidirect quotient of $G$.
The other derived factors may act trivially. Images of the marked
translations satisfy the Bol sandwich law because they are images of its
actual group words; no multiplicative map from the loop is asserted.

For a fixed torus holonomy pair, only its stabilizer acts on that one
geometric sector. The full group transports the family of sectors by
conjugating the marked holonomy pair. This distinction remains in force
below; an arbitrary translation is not asserted to preserve one fixed
twisted bundle.

## CH2. Canonical charged fusion and its dual channel

Define


```math

 L_\ell:W\longrightarrow W^*,\qquad
          (L_\ell x)(y)=\ell(b(x,y)).

```


It is additive in $\ell$. If $\gamma=\ell+\mu$ and
$L_\gamma$ is invertible, put


```math

 u=L_\gamma^{-1}(L_\ell x+L_\mu y),\qquad v=x-y.
 \tag{CH4}

```


The inverse transformation is


```math

 x=u+L_\gamma^{-1}L_\mu v,\qquad
 y=u-L_\gamma^{-1}L_\ell v.
 \tag{CH5}

```


**Theorem CH2.** Pullback by (CH5) gives a canonical unitary intertwiner


```math

 H_\ell\otimes H_\mu
       \simeq H_\gamma\otimes\operatorname{Fun}(W),
 \tag{CH6}

```


where $P$ acts trivially on the last factor. The character law is
$\ell+\mu=\gamma$; the additional variable $v$ is a genuine
fusion multiplicity. These intertwiners transport with the marked data.

**Proof.** Equations (CH4)--(CH5) are inverse bijections because
$L_\gamma=L_\ell+L_\mu$. They preserve the counting norm. Under the
diagonal first-axis translation, $u$ changes to $u+x_0$ and
$v$ stays fixed. Under the second axis, the combined phase is


```math

 \ell(b(x,y_0))+\mu(b(y,y_0))=\gamma(b(u,y_0)).

```


The central and half-cross terms in (CH2) also add. This proves the
intertwining identity. Every displayed operation is functorial. QED.

The diagonal $v=0$ channel is the familiar pointwise product. The
other channels, and their changes of fusion tree, are retained here.
They are not radical-intersection ranks of the class algebra.
The formula only requires the sum charge to be regular; inputs may be
reducible. Applications requiring both relative-coordinate coefficients
in (CH5) to be invertible, including the separated-Cartan comparison in
the companion exchange manuscript, also assume that both input charges
are regular.

For completeness, the finite tree change is explicit. Write
$A=L_\ell,B=L_\mu,C=L_\nu,E=A+B,F=B+C,D=A+B+C$, and assume
$E,F,D$ are invertible. The left tree uses


```math

 v=x-y,\quad w=E^{-1}(Ax+By)-z,

```


while the right tree uses


```math

 v'=y-z,\quad w'=x-F^{-1}(By+Cz).

```


Both have total center $D^{-1}(Ax+By+Cz)$, and


```math

 \begin{pmatrix}v'\\w'\end{pmatrix}
 =\begin{pmatrix}
       -E^{-1}A&1\\
       1-F^{-1}CE^{-1}A&F^{-1}C
   \end{pmatrix}
   \begin{pmatrix}v\\w\end{pmatrix}.
 \tag{CH7}

```


Its inverse is $v=w'-F^{-1}Cv'$,
$w=v'+E^{-1}Av$. This is a unitary permutation of multiplicity
coordinates. Whenever all required partial sums are invertible, the
pentagon holds: each tree is an invertible coordinate change from the
same original tuple, so both composites between two trees are the same
map. This is the ordinary associativity of genuine representation
tensor products expressed in marked coordinates. It is not a categorical
associator inferred from a loop associator.

The apparent singularity at $\gamma=0$ must not be discarded. If
$b_\ell$ is nondegenerate, then $H_{-\ell}=\overline{H_\ell}$
and there is the canonical dual-channel identification


```math

 H_\ell\otimes H_{-\ell}\simeq\operatorname{End}(H_\ell).
 \tag{CH8}

```


Put $V=W\oplus W$, $2d=\dim V$, and


```math

 \Omega_\ell((x,y),(x',y'))
       =\ell(b(x,y')-b(x',y)).

```


The $p^{2d}$ operators $T_v=\rho_\ell(v,0)$, $v\in V$,
are an orthogonal basis of $\operatorname{End}(H_\ell)$ and obey


```math

 T_vT_w=\psi(\tfrac12\Omega_\ell(v,w))T_{v+w},
 \qquad T_uT_vT_u^{-1}=\psi(\Omega_\ell(u,v))T_v.
 \tag{CH9}

```


Indeed a nonzero first coordinate gives a fixed-point-free translation
in the trace, while a nonzero second coordinate gives a nontrivial
character sum. Thus every nonidentity $T_v$ has trace zero; the
same argument applied to $T_v^*T_w$ proves orthogonality. Equation
(CH9) follows from (CH1). This also proves that the neutral dual channel
contains every character of $V$, not merely its trivial line.

## CH3. Two holonomies force a large zero-mode algebra

Fix two group elements with images $u,v\in V$. Their adjoint actions
commute even when the operators $T_u,T_v$ commute only projectively.
Write $U=\operatorname{span}\{u,v\}$, $s=\dim U$, and
$\operatorname{rank}(\Omega_\ell|_U)=2t$.

**Theorem CH3.** The common trivial-holonomy subspace in the true dual
channel is the algebra


```math

 \mathcal Z_{u,v}
   =\operatorname{span}\{T_x:x\in U^\perp\}
   \cong \mathbb C^{\,p^{s-2t}}
                 \otimes\operatorname{Mat}_{p^{d-s+t}}(\mathbb C).
 \tag{CH10}

```


In particular its dimension is $p^{2d-s}$. For an independent
nondegenerate pair it is $\operatorname{Mat}_{p^{d-1}}$. For an
independent isotropic pair it is
$\mathbb C^{p^2}\otimes\operatorname{Mat}_{p^{d-2}}$.
For $d>1$, no pair has only the scalar zero mode. An isotropic pair
at $d=2$ gives a commutative but nonscalar exception; for $d\ge3$
every such zero algebra is nonabelian.

**Proof.** Equation (CH9) identifies the invariant basis vectors exactly
with $U^\perp$, and their product remains there. Nondegeneracy gives
$(U^\perp)^\perp=U$, so the radical of the restricted alternating
form on $U^\perp$ is $U\cap U^\perp$, of dimension $s-2t$.
Choose a complementary nondegenerate alternating space of dimension
$2(d-s+t)$. On the radical the twisted multiplication is the ordinary
group multiplication; its complex group algebra is a sum of
$p^{s-2t}$ scalar blocks. On the complement, the Schrödinger
construction and orthogonal Weyl basis identify the twisted algebra
with the full matrix algebra of size $p^{d-s+t}$. The two factors
commute. This proves (CH10) and all assertions. The resulting algebra
is canonical; the displayed tensor factorization need not be. QED.

This is also a precise analytic warning. In a flat elliptic exchange
kernel, every basis component in (CH10) has trivial spatial and temporal
multiplier. A meromorphic scalar function on a torus cannot have exactly
one simple pole with nonzero residue. Therefore an ansatz that assigns
such a pole independently to every zero component cannot be repaired
by adding only one scalar zero mode. It must change its poles, retain
the full zero algebra with additional connection data, or change the
bundle. This is a scoped residue obstruction, not a no-go theorem for
dynamical exchange or charged sewing. The detailed analytic architecture
is specified in the companion exchange manuscript.

For a degenerate scalar bimap, the same statement applies to each chosen
irreducible constituent after passing to its nondegenerate Weyl quotient,
with $d=r$. The radical characters and both original radicals remain
part of its identification. There is no claim that the canonical reducible
module has exactly the same commutant as one such constituent.

## CH4. A geometric integer extension and coherent carry lines

The charged states have an obstruction that their neutral endomorphisms
hide. Fix marked elements $u_0,v_0\in P$ with central commutator
$c=[u_0,v_0]\in Z$. For any charge-homogeneous representation
$M$ of $P$, of central character $\ell$, write


```math

 U_M=\rho_M(u_0),\quad V_M=\rho_M(v_0),\qquad
 U_MV_M=\psi(\ell(c))V_MU_M.
 \tag{CH11}

```


Let $E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z)$,
$\operatorname{Im}\tau>0$. Constant charged multipliers $U_M,V_M$
are consistent around its fundamental parallelogram only when
$\ell(c)=0$. In contrast their adjoint multipliers always commute.

Define the abelian degree extension


```math

 \Gamma_c=\{(\ell,k)\in Z^*\times\mathbb Z:
                         k\equiv-\ell(c)\pmod p\}.
 \tag{CH12}

```


It is an extension of $Z^*$ by $\mathbb Z$, where
$n\mapsto(0,pn)$. For an object $(M,k)$ with
$(\ell,k)\in\Gamma_c$, put $\kappa=k/p$ and give
$\mathbb C\times M$ the holomorphic factors


```math

 J_1(z)=U_M,\qquad
 J_\tau(z)=e^{-\pi i\kappa\tau-2\pi i\kappa z}V_M.
 \tag{CH13}

```


**Theorem CH4 (explicit geometric repair).** These factors define a
holomorphic vector bundle $\mathcal E_{M,k}$ on $E_\tau$, with


```math

 \deg\mathcal E_{M,k}=(\dim M)\,k/p.
 \tag{CH14}

```


The degree is an integer. Tensor product adds the degree label:


```math

 \mathcal E_{M,k}\otimes\mathcal E_{N,l}
       \cong\mathcal E_{M\otimes N,k+l}.
 \tag{CH15}

```


Every $P$-intertwiner of matching integer label is a holomorphic
bundle map. Thus this is a faithful tensor functor on the indicated
intertwiner category; it need not be full. It includes all tensor and
dual channels, without a nondegeneracy restriction on their charges.

**Proof.** Compatibility of the factors is


```math

 J_\tau(z+1)U_M=U_MJ_\tau(z),

```


which is exactly
$U_MV_M=e^{-2\pi i\kappa}V_MU_M$. Equations (CH11)--(CH12)
give this equality. The quotient is therefore a holomorphic bundle.
Choose a $P$-invariant Hermitian inner product on $M$, by averaging
over the finite group. The metric


```math

 h(z)=\exp\!\left(-2\pi\kappa
                \frac{(\operatorname{Im}z)^2}{\operatorname{Im}\tau}\right)
                   \langle\ ,\ \rangle_M

```


respects both factors. Its Chern curvature is
$-2\pi i\kappa\,dx\wedge dy/(\operatorname{Im}\tau)$ times
the identity. With $\deg=(i/2\pi)\int\operatorname{Tr}F$, this
gives (CH14). Independently, taking determinants of (CH11) shows
$p\mid (\dim M)\ell(c)$, so the displayed number is integral.
The factors and metrics multiply under tensor product, proving (CH15).
A constant intertwining matrix commutes with the relevant factors and
therefore descends. It remains nonzero if the original map was nonzero,
which proves faithfulness on morphisms. The dual is
$\mathcal E_{M^*,-k}$, with the usual evaluation map to the trivial
bundle. QED.

For any irreducible Heisenberg module of dimension $p^d$, (CH14)
fixes its degree modulo $p^d$ to
$-\ell(c)p^{d-1}$. The finite commutator does not choose the integer
lift $k$, and hence does not canonically choose an absolute degree.
The marked pair and the root-of-unity convention are retained input.

Here is the obstruction to suppressing that extra integer. Suppose one
assigns a single projectively flat bundle slope $\kappa_\ell$ to
each finite charge, and every nonzero charge-additive fusion map is
parallel with a flat multiplicity bundle. Comparing central curvatures
on its two sides forces


```math

 \kappa_{\ell+\mu}=\kappa_\ell+\kappa_\mu.
 \tag{CH16}

```


If these fusion channels close under all finite charges, torsion forces
all slopes to vanish. This contradicts
$\kappa_\ell\equiv-\ell(c)/p\pmod{\mathbb Z}$ whenever that
commutator is detected. Thus this specified finite-charge, flat-multiplicity
architecture is impossible for nonzero $c$. Allowing further slope
labels or nonflat multiplicity lines is an explicit escape, as CH4 shows.

To express the repair with finite charge representatives, choose
$s(\ell)\in\{0,\ldots,p-1\}$ representing $-\ell(c)$, and put


```math

 n(\ell,\mu)=
        \frac{s(\ell)+s(\mu)-s(\ell+\mu)}p\in\{0,1\}.
 \tag{CH17}

```


Let $\mathcal L=\mathcal E_{\mathbf1,p}$, the degree-one theta
line bundle with factors $1,e^{-\pi i\tau-2\pi iz}$. A finite
fusion intertwiner $C:M_\ell\otimes M_\mu\to M_\gamma\otimes F$,
where $\gamma=\ell+\mu$ and $F$ has zero central charge, gives
the actual holomorphic map


```math

 \mathcal E_{M_\ell,s(\ell)}\otimes\mathcal E_{M_\mu,s(\mu)}
 \longrightarrow
 \mathcal E_{M_\gamma,s(\gamma)}
             \otimes\mathcal E_{F,0}\otimes\mathcal L^{n(\ell,\mu)}.
 \tag{CH18}

```


The map is the constant matrix $C$ in the covering trivializations;
the factors agree by (CH17). In particular (CH6) gives such maps in
every regular-sum channel. For a zero-sum channel, decompose (CH8) into
its actual Weyl-character lines and apply (CH18) to each projection.
No missing inverse $L_0^{-1}$ is used.

The integer carry obeys


```math

 n(\ell,\mu)+n(\ell+\mu,\nu)
       =n(\mu,\nu)+n(\ell,\mu+\nu).               \tag{CH19}

```


Both sides telescope to
$(s(\ell)+s(\mu)+s(\nu)-s(\ell+\mu+\nu))/p$.
Consequently the line powers in every tree agree, and the ordinary
finite tensor associator, or (CH7) where applicable, gives a commuting
pentagon of holomorphic bundle maps. This is a genuine coherent
line-valued construction, not an assumed loop-associator pentagon.

If $\ell(c)\ne0$, the restriction of $\Gamma_c$ to the cyclic
subgroup generated by $\ell$ is not split: a lift $(\ell,k)$
has $p$-fold sum $(0,pk)\ne0$. Equivalently the carries around
that cycle sum to $s(\ell)>0$. No change of integer representatives
removes this extension class.

### Divisors and the three different meanings of zero

A nonzero meromorphic section of $\mathcal L^n$ has divisor of
degree $n$. This follows directly from its multipliers: its logarithmic
derivative is periodic under 1 and changes by $-2\pi in$ under
$\tau$; integrating around a fundamental parallelogram gives
$2\pi in$. In particular no nonzero-degree carry line has a nowhere
vanishing holomorphic trivialization. The explicit series


```math

 \vartheta(z;\tau)=\sum_{m\in\mathbb Z}
                      e^{\pi im^2\tau+2\pi imz}

```


converges locally uniformly and is a section of $\mathcal L$. It
vanishes at $(1+\tau)/2$ by pairing terms $m$ and $-m-1$,
and the divisor count shows that this is its one zero modulo the lattice,
with multiplicity one. Powers give explicit positive carry-line sections;
their inverses give meromorphic negative-line frames. Composing (CH18)
with such a local frame yields scalarized sewing coefficients whose
zeros or poles account for the carry. The invariant maps are the
line-valued maps (CH18); no arbitrary choice of scalarization is hidden.

Zero central charge, joint trivial flat holonomy, and degree zero are
different conditions. For a charge detected by $c$, normalized
representatives satisfy $s(\ell)+s(-\ell)=p$. Their zero-charge
product therefore contains the degree-one line $\mathcal L$.
The true categorical dual of $(M_\ell,s(\ell))$ instead has label
$-s(\ell)$, not $s(-\ell)$. Its tensor product has label zero
and gives the flat endomorphism bundle whose joint trivial-holonomy
algebra is CH3. Passing from normalized charges to true duals does not
remove that zero algebra.

Finally, $k/p$ is a geometric slope, not a conformal weight. No
Virasoro operator, ribbon twist, or VOA grading is defined here. The
linear phase $e^{2\pi ik/p}$ is not being asserted to satisfy the
quadratic and duality requirements of such a structure.

## CH5. What central cocycle phases do and do not survive

Let the torus act as in (CH3), and retain the positive crossed cocycle
$f(ab)=f(a)+T(a)f(b)$. The graph-transport operator is


```math

 U_a^f|_{H_\ell}
       =\psi((a\cdot\ell)(f(a)))\,A_a.
 \tag{CH20}

```


It is the actual representation of the marked group element $f(a)a$,
so its composition law follows either from the crossed cocycle or the
group representation. The phase is additive at a charge junction:
$\psi(\ell f)\psi(\mu f)=\psi((\ell+\mu)f)$.

**Proposition CH5 (exact gauge-erasure scope).** Put
$f_z(a)=f(a)+(1-T(a))z$. On charge-homogeneous objects set
$D_z|_{H_\ell}=\psi(\ell(z))1$. Then


```math

                       U_a^{f_z}=D_zU_a^fD_z^{-1}.    \tag{CH21}

```


The operators $D_z$ preserve every $P$-intertwiner and tensor
fusion map, are compatible with duals and integer labels, and define
constant holomorphic bundle isomorphisms in CH4. Hence every closed
network built functorially only from these graph transports, charged
$P$-intertwiners, and the same holonomy bundle data is unchanged by
the shift. In particular neutral adjoint kernels and their zero algebras
cannot distinguish that shift.

**Proof.** The extra scalar from conjugating the map
$H_\ell\to H_{a\cdot\ell}$ is


```math

 \psi((a\cdot\ell)(z)-\ell(z))
       =\psi((a\cdot\ell)((1-T(a))z)),

```


which is precisely the phase change in (CH20). On a charge-additive
junction, input and output $D_z$-scalars agree, so every such
intertwiner is preserved. The dual uses the inverse scalar. The scalar
maps commute with the bundle factors and connections; the degree label
is unchanged. They cancel along every internal network edge and in a
closed trace. Independently,
$\operatorname{Ad}(\psi(\ell f(a))A_a)=\operatorname{Ad}(A_a)$,
which directly proves the neutral adjoint assertion. QED.

This scope excludes a separately fixed split torus operator $A_a$,
a fixed outside involution $\tau$, and fixed charged boundary
trivializations. In general $D_z$ does not commute with $A_a$;
for a negative-central isotope shift it does not commute with the fixed
$\tau$ either. Retaining both graph transport and the split marking
recovers the actual central phase $\psi(\ell f(a))$. An open
charged amplitude in fixed boundary trivializations can likewise retain
it. The proposition is therefore a precise limit of the graph-only
coherent network, not an identification of the two marked loops.

For the rigid family the shifts are
$f_k(a)=f(a)-k\epsilon^2$. Their $b,R,T$ are unchanged, and
CH5 makes the unmarked neutral charged construction blind to them.
The existing [Fourier norm test](bol-fourier-sewing.md) keeps extra
markings and is not subject to this erasure. The newer
[isotope-orbit source at 7530ae6](https://github.com/Mira-Cult/math-wip/blob/7530ae6eeeb0614d7c94ed6ab1f6761f3493ab88/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/odd-class-two-isotope-orbits.md)
provides a broader orbit analysis; only its displayed shift formula is
used here, not a new independent verification of that classification.

The classical phase in (CH9) is a bilinear group 2-cocycle, whose
coboundary is zero. The crossed cocycle $f$ also does not, by itself,
create a nontrivial categorical 3-associator. A repair using such an
associator would need a new definition and its own coherence proof.

## CH6. Concrete family consequences and exact controls

Use exactly the three matrices in equations (1)--(2) of the
[rigid-center data at source 2a25b81](https://github.com/Mira-Cult/math-wip/blob/2a25b81e3efe5bdd8a3923e27c94aef16a559094/problems/0323-finite-simple-non-moufang-bol-loops/manuscripts/odd-rigid-center-nongloop.md#data).
For these pinned matrices, write
$B(x,y,z)=xB_0+yB_1+zB_2$, over $\mathbb F_3$, and put


```math

 q(x,y,z)=y^2-yz-z^2+xz.

```


Direct polynomial multiplication gives


```math

 \det B=q^2,\qquad \operatorname{adj}B=qC,

```



```math

 C=\begin{pmatrix}
 0&0&-x+z&-y+z\\
 0&0&y&-z\\
 x-z&y-z&-y-z&-z\\
 -y&z&z&0
 \end{pmatrix}.                                      \tag{CH22}

```


Every nonzero $B$ has rank at least two. If $z\ne0$, the minor
in rows 1,3 and columns 1,3 has determinant $z^2$. If $z=0$
and $y\ne0$, rows 1,4 and columns 1,4 give a nonzero multiple of
$y^2$; otherwise $B=xB_0$ has rank two. Thus (CH22) shows that
nonzero $q=0$ charges have rank exactly two, and $q\ne0$ charges
have rank four. There are nine zeros of $q$: for $z=0$ one has
$y=0$ and arbitrary $x$; for $z\ne0$, each $(y,z)$
determines exactly one $x$. The full scalar-bimap rank histogram is
therefore $\{0:1,2:8,4:18\}$.

After the nondegenerate field trace from $\mathbb F_{3^{18}}$, ranks
multiply by 18. In the 18 regular charge sectors the canonical
Schrödinger module has dimension $3^{72}$. The other eight nonzero
charges have irreducible constituents of dimension $3^{36}$; the
canonical module (CH2) there is reducible. For a nondegenerate
holonomy pair in any such irreducible constituent, CH3 forces at least
a $\operatorname{Mat}_{3^{35}}$ zero block, and a regular charge
forces $\operatorname{Mat}_{3^{71}}$. Thus one scalar zero mode
cannot support these charged sectors. These are symbolic consequences
of the compact matrices, not computations of a huge multiplication table.

The bimap controls are deliberately separate from the simple-loop
claim. A smallest useful model takes $p=3,W=\mathbb F_3,b(x,y)=xy$,
$u_0=(1,0,0)$, $v_0=(0,-1,0)$, so $c=-1$. Normalized
degree labels for charges $0,1,2$ are $0,1,2$. The two
nontrivial three-dimensional Schrödinger bundles have degrees one
and two; fusion $1+2=0$ carries $\mathcal L$. The true dual
of label one has label minus one and instead has flat endomorphism
bundle. In two symplectic degrees of freedom, the same marked pair
forces a $3\times3$ zero block. An independent isotropic pair
has zero degree class but nine scalar zero blocks. This checks why
the three kinds of zero in CH4 cannot be conflated.

The exact script also checks the cubic proper-Bol example's associative
quotient for the separate LC3 result. That control tests the proposed
local-current erasure; it is not evidence that the Heisenberg bundles
are a nonassociative VOA.

The strongest positive result here is the explicit charge-dependent
holomorphic tensor construction with its unavoidable carry divisors.
The next analytic obligation is a separated-point interaction compatible
with its genuine fusion maps and full neutral zero algebra, while keeping
enough fixed marks to escape CH5. Standard exchange equations on one
matrix block do not by themselves discharge that obligation.
