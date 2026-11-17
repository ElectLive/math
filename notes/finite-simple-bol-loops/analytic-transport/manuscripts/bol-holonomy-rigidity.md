# Holonomy rigidity and the limits of the free-kernel architecture

**Mira Cult**

Construction and proof by model participant 2, with the linear
projector theorem proposed by model participant 5, for the separately owned PR #438
continuation, 2026-11-16. Labels HR1--HR6 are manuscript-local. The quadratic
control in HR6 was proposed by model participant 3 and model participant 5; their
checks and the author's proof below are participant contributions. This is an
additive result about the analytic architecture; it neither re-proves the
inherited class-two loop inputs nor changes their review qualifications.

## The question and its exact scope

The marked Bol construction supplies a finite Hermitian space, actual
translation operators, cocycle probes, and commuting holonomy pairs. The
[genus-one completion](bol-genus-one-kernel.md) attaches to these data a
standard residue-normalized flat-bundle kernel. Can that particular
attachment force a new relation between inequivalent holonomy sectors?

For linear identities with coefficients depending on the torus modulus but
not on the insertion coordinate, the answer below is precise: every such
identity comes from constant finite relations among joint spectral
projectors. For products and position derivatives evaluated at one common
spatial difference, a fixed pole bound gives a finite Laurent-jet normal
form. The latter is a reduction theorem, not a classification of all theta
identities or a no-go theorem for Bol moonshine.

The hypotheses matter. We keep one torus, fixed finite holonomies, and one
common insertion difference. We do not include isogenies, changes of
modulus, independently moving insertion points, punctured surfaces,
noncommuting boundary holonomies, interactions, or additional sewing
operators. Section HR5 explains what a commutator-defined Fourier sewing
operator adds to this architecture.

All fields of meromorphic functions below are on the open upper half-plane.
No growth, cusp, integrality, or modular condition on their elements is
implicitly asserted.

## HR1. Scalar kernels and finite translation projectors

Fix an integer N >= 2 and put


```math

 \mathcal X_N=\mu_N\times\mu_N,\qquad
 \mathbb M=\operatorname{Mer}(\mathbb H).

```


Write a character as chi=(u,v), with multiplication componentwise. It
assigns u to translation by 1 and v to translation by tau. For chi != 1
let k_chi(z;tau) be the unique scalar kernel with


```math

 k_\chi(z+1;\tau)=u k_\chi(z;\tau),\qquad
 k_\chi(z+\tau;\tau)=v k_\chi(z;\tau),\qquad
 k_\chi(z;\tau)=z^{-1}+O(1),                         \tag{HR1.1}

```


whose only poles are simple poles at the period lattice. This is precisely
the scalar kernel of [K1](bol-genus-one-kernel.md#k1-the-finite-holonomy-family-and-its-unique-kernel).
For u=exp(2 pi i alpha), v=exp(2 pi i beta), it is


```math

 k_\chi(z;\tau)=e^{2\pi i\alpha z}
 \frac{\theta_1'(0;\tau)\theta_1(z+\alpha\tau-\beta;\tau)}
 {\theta_1(z;\tau)\theta_1(\alpha\tau-\beta;\tau)}.     \tag{HR1.2}

```


The scalar functions are nonzero because their residue is one. They are
N-periodic in each lattice direction. On any such function define


```math

 (\mathscr P_\chi F)(z;\tau)=\frac1{N^2}
 \sum_{a,b=0}^{N-1}u^{-a}v^{-b}F(z+a+b\tau;\tau).
                                                               \tag{HR1.3}

```


These operators are linear over M: the scalar coefficient is evaluated at
the same tau throughout the sum. Character orthogonality gives


```math

 \mathscr P_\chi k_\psi=\delta_{\chi,\psi}k_\psi.
                                                               \tag{HR1.4}

```


**Theorem HR1 (linear independence over the modulus field).** The functions
k_chi, for distinct nontrivial chi in X_N, are linearly independent over M.

**Proof.** Apply P_chi to a proposed finite relation. Its chi term is
f_chi(tau) k_chi(z;tau)=0. Comparing the residue at zero gives f_chi=0 as a
meromorphic function. This works on the complement of the discrete set of
coefficient poles and hence identically. QED.

The restriction that coefficients are independent of z is essential.
Allowing meromorphic functions of both z and tau admits the tautological
relation k_psi k_chi - k_chi k_psi=0 and ratios between nonzero kernels;
HR1 makes no assertion over that larger field.

## HR2. Matrix relations and trace probes are finite spectral relations

Let B be a finite-dimensional complex Hermitian space. For j=1,...,s let
(U_j,V_j) be commuting unitary pairs with


```math

 U_j^N=V_j^N=I,\qquad
 \ker(U_j-I)\cap\ker(V_j-I)=0.

```


The pairs need not commute with one another. They are fixed matrices,
independent of z and tau. Their joint spectral projectors are the explicit
constant matrices


```math

 \Pi_{j,\chi}=\frac1{N^2}\sum_{a,b=0}^{N-1}
          u^{-a}v^{-b}U_j^aV_j^b.                    \tag{HR2.1}

```


The trivial projector is zero. The unique residue-normalized matrix kernel
is


```math

 K_j(z;\tau)=\sum_{\chi\ne1}\Pi_{j,\chi}k_\chi(z;\tau).
                                                               \tag{HR2.2}

```


**Theorem HR2 (constant origin of all linear relations).** For f_j in M,


```math

 \sum_j f_j(\tau)K_j(z;\tau)=0
 \quad\Longleftrightarrow\quad
 \sum_j f_j(\tau)\Pi_{j,\chi}=0
 \quad\hbox{for every }\chi.                         \tag{HR2.3}

```


Moreover, the M-vector space of these relations is the scalar extension of
the corresponding complex vector space of constant relations:


```math

 \operatorname{Rel}_{\mathbb M}(K_1,\ldots,K_s)
 =\mathbb M\otimes_{\mathbb C}
   \ker\!\left[
      \mathbb C^s\longrightarrow
       \bigoplus_{\chi\ne1}\operatorname{End}(B),\quad
      (c_j)\longmapsto(\textstyle\sum_j c_j\Pi_{j,\chi})_\chi
     \right].                                      \tag{HR2.4}

```


For a finite family of fixed probe matrices A_(r,j), put


```math

 C_{r,j}(z;\tau)=\operatorname{Tr}(A_{r,j}K_j(z;\tau)).

```


Then simultaneous identities sum_j f_j C_(r,j)=0 for every r are equivalent
to the finite constant-coefficient system


```math

 \sum_j f_j(\tau)\operatorname{Tr}(A_{r,j}\Pi_{j,\chi})=0
       \quad\hbox{for every }r,\chi,                 \tag{HR2.5}

```


and its relation space also arises by scalar extension from C.

**Proof.** Insert (HR2.2), apply (HR1.3), and compare the residue. This proves
(HR2.3) entrywise and (HR2.5) after taking the trace. Choose a complex basis
of the finite target of the displayed linear map. Its matrix has constant
complex entries. Row reduction over C gives pivot positions and a basis of
its nullspace. The same row reduction over M has exactly the same pivots;
the free variables may now lie in M. This proves (HR2.4) and the analogous
probe statement. QED.

The trace pairing on End(B) is nondegenerate. Consequently a basis of all
matrix probes detects exactly the matrix relation (HR2.3). A restricted
probe set detects only (HR2.5) and can lose information. In particular the
uninserted trace keeps only joint eigenvalue multiplicities; it need not
retain the marked embedding of the translation and cocycle operators.

**Corollary HR2a (the actual current probes suffice).** For the original
Bol seed X=G x_Z C, let


```math

 \mathscr A_X=\operatorname{span}\{M_aL_g:a\in\operatorname{Fun}(X),\ g\in G\}
       =\bigoplus_{\mathcal O\in G\backslash X}
              \operatorname{End}(\mathbb C^{\mathcal O}).       \tag{HR2.6}

```


The equality is the already proved
[CG1 operator-algebra identity](bol-correlation-geometry.md#a-finite-coefficient-algebra-for-the-current-system).
For holonomies in the original action of G x Z, with allowed scalar signs,
the probes from A_X detect exactly the full matrix relation (HR2.3).

**Proof.** The G-orbits of X correspond to the Z-orbits of C: the class of
[g,c] is determined by the Z-orbit of c. Left G and commuting right Z
therefore preserve each such orbit block. All holonomy matrices, their
joint projectors, and their kernels belong to the block algebra (HR2.6),
with scalar functions adjoined for the kernels. The trace pairing is
nondegenerate on this direct sum of full matrix algebras, as may also be
seen by testing each block against its matrix units. Hence a basis of A_X
in (HR2.5) detects every block entry. QED.

Simultaneous unitary transport carries every Pi_(j,chi) and every probe to
its conjugate. The theorem is therefore natural under the strict transport
interface used by the Bol construction. Comparing different loops still
requires that transport or a specified identification of the finite data;
the theorem does not choose one.

This result concerns **normalized bilocal kernels**. Multiplying each
sector by a nonzero meromorphic partition function changes the displayed
coefficients by those factors; it does not create an additional kernel
identity. Relations at different tau, different rescaled positions, or
involving derivatives in tau are outside (HR2.3).

## HR3. A nonlinear normal form at one spatial difference

Fix a pole bound D >= 1. Let S_(chi,D) be the M-vector space of jointly
meromorphic functions F(z;tau) having multipliers chi and, in the position
variable, no poles away from the lattice and poles of order at most D at
lattice points. Meromorphic coefficient poles in tau are allowed. Define,
for chi != 1,


```math

 b_{\chi,r}(z;\tau)=
   \frac{(-1)^{r-1}}{(r-1)!}\partial_z^{r-1}k_\chi(z;\tau),
                 \qquad 1\le r\le D.               \tag{HR3.1}

```


Each has Laurent principal part exactly z^(-r).

For the trivial multiplier use the Weierstrass function with periods
(1,tau), normalized by wp(z;tau)=z^(-2)+O(z^2). For r >= 2 put


```math

 p_r=\frac{(-1)^{r-2}}{(r-1)!}\partial_z^{r-2}\wp,
 \qquad \widetilde p_r=p_r-[z^0]p_r.                 \tag{HR3.2}

```


Subtracting the regular constant term is needed: higher derivatives of wp
can have a nonzero constant Laurent coefficient. The principal part of
p_r and p_tilde_r is z^(-r), and p_tilde_r has constant coefficient zero.

**Theorem HR3 (finite Laurent-jet normal form).**

1. If chi != 1, the functions b_(chi,1),...,b_(chi,D) are a basis of
   S_(chi,D), and


```math

    F=\sum_{r=1}^D [z^{-r}]F\;b_{\chi,r}.           \tag{HR3.3}

```


2. If chi = 1, the coefficient [z^(-1)]F is zero. The functions
   1,p_tilde_2,...,p_tilde_D are a basis, and


```math

    F=[z^0]F+\sum_{r=2}^D[z^{-r}]F\;\widetilde p_r.
                                                               \tag{HR3.4}

```


   For D=1 this means that the space consists only of constants in z.

In both cases the dimension over M is D.

**Proof.** In the nontrivial case subtract the right side of (HR3.3). All
negative Laurent coefficients vanish at zero. The multiplier laws then
remove poles at every lattice point. The difference is entire in z. Its
absolute value is periodic because the multipliers are unitary, hence
bounded on the plane. It is constant by Liouville's theorem. A constant
with nontrivial multipliers is zero. Distinct principal parts also prove
linear independence. The Laurent coefficients are meromorphic in tau, so
this argument is over M.

In the trivial case integrate around a fundamental parallelogram whose
boundary avoids the pole. Opposite edges cancel by ellipticity, proving
that the residue is zero. Subtract the right side of (HR3.4). The remaining
elliptic function is entire and therefore constant, and its constant
Laurent coefficient is zero. The displayed principal parts and the
constant function are linearly independent. QED.

**Corollary HR3a (bounded nonlinear reduction).** Consider a finite
expression made from products of k_chi(z;tau), their position derivatives,
constant finite matrix tensors and contractions, and coefficients in M.
All factors use the same spatial difference z. Suppose each monomial has
total pole order at most D. Then:

- the character projectors (HR1.3) split the expression into its total
  multiplier sectors;
- in every nontrivial total sector, vanishing is equivalent to vanishing
  of its D principal Laurent coefficients;
- in the trivial sector, vanishing is equivalent to vanishing of its
  coefficients of z^(-D),...,z^(-2) and its constant coefficient.

Thus every proposed identity in this architecture is exactly a finite
Laurent-jet system. Its coefficients are finite contractions of the input
tensors with Laurent coefficients of the same universal kernels.

**Proof.** A position derivative preserves the multiplier and increases
the pole bound by at most its order. Multiplication multiplies characters
and adds pole bounds. Expand the finite matrix contractions and apply HR3
to each character component. QED.

For example, write k_chi=z^(-1)+a_chi+b_chi z+O(z^2). When chi,psi and
chi psi are nontrivial, HR3 gives


```math

 k_\chi k_\psi
  =-\partial_z k_{\chi\psi}
     +(a_\chi+a_\psi)k_{\chi\psi}.                  \tag{HR3.5}

```


Both sides have principal part z^(-2)+(a_chi+a_psi)z^(-1), and their
difference is an entire section of a nontrivial flat line. Uniqueness also
gives k_(chi^(-1))(z)=-k_chi(-z), so


```math

 k_\chi k_{\chi^{-1}}
       =\wp+2b_\chi-a_\chi^2.                      \tag{HR3.6}

```


These are universal elliptic addition reductions. They are not new
identities forced by a Bol loop. The established Kronecker/Fay theory is
recorded in [Mat19, Section 2.1 and Proposition 2.3](../REFERENCES.md#mat19);
free-fermion determinant and Fay formulas are recorded in
[MTZ07, Proposition 6.4 and Corollary 6.8](../REFERENCES.md#mtz07).

Unlike HR2, the nonlinear reduction does **not** say that every relation is
generated by a constant finite nullspace: its normal-form coefficients
contain genuine universal functions of tau. Nor does it determine all
relations among those coefficient functions, all multivariable Fay
relations, or an ideal with a pole bound independent of degree. Finite Bol
data can still impose informative identities among the tensor coefficients.
They must be demonstrated rather than inferred from the existence of the
universal normal form.

## HR4. Spin products reach the zero-mode sector

The three nontrivial sign pairs in K1 are stable under the modular action,
but they are not a group under componentwise multiplication. Each sign
pair squares to the trivial pair. The full character family also contains
chi^(-1) whenever it contains chi, by reversing both cycles.

**Proposition HR4.** The residue-normalized simple-pole kernels of K1
cannot be closed under a sewing rule that requires such a kernel in every
product holonomy sector. In particular the product of inverse sectors
lands in a sector admitting no elliptic function with only a simple pole
at zero of residue one.

**Proof.** The product multiplier is trivial. Such a purported scalar
kernel would descend to an elliptic meromorphic function with one pole of
nonzero residue on the torus. The sum-of-residues theorem, or the
fundamental-parallelogram argument in HR3, rules it out. For a matrix
sector with a common fixed vector, projection to that vector gives the
same contradiction for residue I. QED.

There is no contradiction in the product itself: (HR3.6) is a valid
elliptic function with a double pole. The obstruction concerns interpreting
the resulting **fermion sector** with the same normalized simple-pole
propagator. A complete sewing interpretation must allow a zero-mode
prescription, such as unnormalized amplitudes with zero modes saturated by
insertions. This is an additional analytic sector, not a consequence of
Bol associators. [MTZ07, Proposition 6.6](../REFERENCES.md#mtz07) treats the
trivial flat line by a bordered determinant; Proposition 6.13 separately
proves its modular transformation law. Thus the necessary enlargement has
a standard precedent, while its compatibility with any proposed new Bol
sewing operations remains a task to prove.

## HR5. What commutator Fourier sewing changes

There is a concrete finite operation that is not part of HR2's input
alphabet. In the [translation-generated seed](bol-translation-class-fusion.md),
let C be the conjugacy classes of Q, A_C=Fun(C,C), and W=Q/Z. The zero-charge
space


```math

 V_0=A_C^Z

```


has one dimension for each w in W. Let O_w be the central orbit of classes
over w and use its canonical orthonormal basis


```math

 \eta_w=|O_w|^{-1/2}\mathbf1_{O_w}.

```


This normalization is relevant when the central orbits have unequal sizes.
Let alpha and beta be nondegenerate alternating F_p-valued forms on W
obtained by applying specified central charges to the actual commutator
bimap. Fix the same additive character psi(t)=exp(2 pi i t/p) as in the
charge construction, and let n_0=|W|. Define


```math

 F_\alpha\eta_y=n_0^{-1/2}
             \sum_{x\in W}\psi(\alpha(x,y))\eta_x.    \tag{HR5.1}

```


**Proposition HR5 (the finite Fourier sewing law).** The operators F_alpha
are unitary self-adjoint involutions. There is a unique invertible linear
map T:W -> W satisfying


```math

 \alpha(Tx,y)=\beta(x,y),

```


and, with P_T eta_y=eta_(Ty),


```math

                F_\alpha F_\beta^{-1}=P_T.           \tag{HR5.2}

```


These constructions are natural under simultaneous isomorphism of W and
the charged commutator forms. Extending F_alpha as the identity on the
orthogonal complement of V_0 gives a Z-intertwiner of A_C; induction to
B=Fun(G x_Z C,C) gives a G-intertwiner and hence commutes with every actual
Bol translation on B.

**Proof.** Alternation gives alpha(y,x)=-alpha(x,y), so the matrix in
(HR5.1) equals its adjoint. Its square has x,y entry


```math

 n_0^{-1}\sum_{z\in W}
        \psi(\alpha(x,z)+\alpha(z,y))
  = n_0^{-1}\sum_{z\in W}\psi(\alpha(x-y,z))
  =\mathbf1_{x=y},                                  \tag{HR5.3}

```


by nondegeneracy and character orthogonality. Nondegeneracy of alpha and
beta also gives the unique invertible T. The x,y entry of F_alpha F_beta
is


```math

 n_0^{-1}\sum_z\psi(\alpha(x,z)-\beta(y,z))
  =n_0^{-1}\sum_z\psi(\alpha(x-Ty,z))
  =\mathbf1_{x=Ty}.                                 \tag{HR5.4}

```


This proves (HR5.2). Relabeling W transports all basis vectors and phases
simultaneously. The zero-charge space is fixed pointwise by Z; its
orthogonal complement is Z-stable. Thus the extended operator commutes
with Z. Applying it fiberwise in an induced model is well-defined exactly
because of this equivariance, and commutes with the left G action. QED.

The operator is dictated by finite commutator data and lives on the
existing seed. It is not an unrelated module attached to every loop.
Nevertheless it is an **additional finite operation**: a Fourier matrix
is generally not pointwise-algebra multiplication, an algebra
automorphism, or an element of the original odd permutation action group.
The relative map T can retain information lost by separate ranks and
fusion dimensions, but that claim requires a worked comparison of the
chosen form pair. The sewing law itself is finite Fourier orthogonality.

**Corollary HR5a (strict enlargement of the original alphabet).** Suppose
|W|>1. The induced F_alpha does not belong to the original one-particle
algebra A_X of (HR2.6). If T != I, the induced relative operator P_T does
not belong to A_X either. Thus these operators cannot be generated by
finite sums and products of the original multiplication colors and
translation operators.

**Proof.** The central orbits of C are exactly the sets O_w, one for each
w in W. Therefore the G-orbits of X are


```math

                  X_w=G\times_Z O_w.                \tag{HR5.5}

```


The original algebra A_X preserves every C^(X_w). At any coset fiber
gZ, the vector eta_w lies in the w block, and every coefficient of its
Fourier image (HR5.1) is nonzero. The induced F_alpha therefore maps it
to a vector with components in every w' block, including w' != w. If
T != I, choose w with Tw != w; the induced P_T maps the same fiber vector
eta_w to eta_(Tw), crossing two distinct orbit blocks. This proves both
exclusions. QED.

This is a strict boundary at the level of the actual existing operator
algebra, not merely a statement that the new formulas look different.
Commuting with the left G action does not imply membership in A_X: the
new intertwiner mixes equivalent subrepresentations in distinct G-orbits,
while A_X preserves those orbits separately.

Consequently (HR5.2) does not contradict HR2. A kernel built with an
enlarged, compatible holonomy alphabet still satisfies HR2's spectral
criterion. What changes is the finite projector data to which the kernel
is applied. Moreover F_alpha has order two, and P_T can have even order;
the original argument that a negative sign excludes a fixed vector for
odd-order holonomies cannot be silently reused. Any new kernel sector
must separately satisfy the commuting and no-common-fixed-vector
hypotheses, or be supplied with an appropriate zero-mode treatment.

## HR6. A quadratic alternative that erases the graph parameter

Here is a separate finite-quadratic route whose first modular step can be
proved, but whose canonical output loses the desired parameter. Let p be
odd, let beta be a nondegenerate alternating form on W, and let R be
beta-selfadjoint, meaning beta(Rx,y)=beta(x,Ry). On


```math

 D=W\oplus W,\qquad q(x,y)=\beta(x,y)/p\pmod{\mathbb Z},

```


the notation t/p for t in F_p means its standard image in Q/Z. The
associated symmetric pairing is


```math

 B_D((x,y),(x',y'))=
       (\beta(x,y')+\beta(x',y))/p.

```


It is nondegenerate. Put L_R={(x,Rx):x in W} and
v_R=sum_(d in L_R)e_d in C[D].

**Proposition HR6 (graph erasure in the canonical Eisenstein packet).**
L_R is self-dual isotropic, and v_R is fixed by the standard finite Weil
operators S and T. The shear


```math

 g_R(x,y)=(x,y+Rx)

```


is an isometry of (D,q) and sends L_0 to L_R. Consequently every
O(D,q)-invariant vector-valued function E_D(tau) satisfies


```math

             \langle E_D(\tau),v_R\rangle
               =\langle E_D(\tau),v_0\rangle.       \tag{HR6.1}

```


In particular this holds for the canonical vector-valued Eisenstein series
formed from e_0 and the Weil representation rho_D in even weight k>2:


```math

 E_{D,k}(\tau)=
  \sum_{\gamma\in\Gamma_\infty\backslash SL_2(\mathbb Z)}
     (c\tau+d)^{-k}\rho_D(\gamma)^{-1}e_0,
 \quad \Gamma_\infty=\langle T,-I\rangle,\quad
 \gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}.         \tag{HR6.2}

```


The finite Weil operators are the diagonal phases psi(beta(x,y)) and
the normalized Fourier transform for B_D; see the
[finite-quadratic modular sources](../REFERENCES.md#modular-analytic-sources)
for the standard representation. These formulas fix the normalization in
(HR6.2).

**Proof.** Selfadjointness and alternation give
beta(x,Rx)=beta(Rx,x)=-beta(x,Rx), so beta(x,Rx)=0 because p is odd.
Thus q vanishes on L_R. Its order is |W|=sqrt(|D|), hence nondegeneracy
makes L_R its own orthogonal complement. The normalized Gauss sum is one:


```math

 |D|^{-1/2}\sum_{x,y\in W}\psi(\beta(x,y))=1.

```


There is therefore no additional phase in the Fourier formula for the
Weil generator S in this hyperbolic module. In either consistent sign
convention, character orthogonality gives


```math

 S v_R=\frac{|L_R|}{\sqrt{|D|}}v_{L_R^\perp}=v_R,
 \qquad T v_R=v_R.

```


The same identity beta(x,Rx)=0 shows q(g_R(x,y))=q(x,y). Every isometry
permutes the e_d basis, commutes with the finite Weil representation, and
fixes e_0. The absolutely convergent e_0-based Eisenstein sum in even
weight k>2 is therefore O(D,q)-invariant term by term. Its contraction
with v_R equals its contraction with v_0 because g_R v_0=v_R, proving
(HR6.1). More generally that last argument only uses the stated
O(D,q)-invariance of E_D. QED.

This is an exact negative control for this choice of quadratic module,
seed vector and graph contraction. Adding a noninvariant marking can
avoid the conclusion, but then that marking is additional data that must
be specified and transported. The proposition does not rule out other
quadratic or lattice constructions.

### A narrow equivariance obstruction to choosing the extra marking

The following control uses the strict local transport interface inherited
by [the canonical seed](bol-translation-class-fusion.md), rather than
claiming a new classification theorem. In that interface


```math

                  (L,M)=(-I_W,I_Z)

```


is an allowed automorphism of the full local data (b,R,T,f): bilinearity
gives b(-x,-y)=b(x,y), -I_W commutes with every R, and the maps on Z,
including T and f, are unchanged. The simultaneous W actions also commute
with the axis-swapping involution. Thus a functorially selected vector
v(b,R,T,f) in W must satisfy v=-v, and hence v=0 at odd p. A nonzero Weyl
displacement cannot be obtained by such a single-valued equivariant
selection alone. This observation was also derived by
model participant 4 in this continuation.

The same argument rules out a functorially assigned triadditive map
A:W^3 -> Z from these data, with the displayed action on its target:
naturality requires A(-x,-y,-z)=A(x,y,z), while triadditivity gives its
negative. Therefore A=0. This is only a sign obstruction to these specific
choices. It does not rule out non-multilinear group 3-cocycles, families
indexed by an additional marked vector or covector, a target carrying a
different involution, or a defect theory with separately proved coherence.

## Consequence for the next mathematical target

HR2 rules out a specific explanation: in the existing normalized bilocal
system, a relation between fixed holonomies with z-independent meromorphic
coefficients cannot contain more information than a finite constant
spectral relation. HR3 gives a finite test for same-position nonlinear
proposals without declaring all nonlinear proposals exhausted. Neither
result uses Wick's theorem or modular differentiation; their mechanism is
position monodromy and the elementary theory of meromorphic flat-line
sections.

A new Bol mechanism must therefore exhibit its extra finite or geometric
operation explicitly. Commutator Fourier sewing supplies one finite
candidate, with its law proved above. A relation on punctured surfaces,
an isogeny relation, or an interacting defect theory changes the hypotheses
more substantially and requires new coherence or sewing proofs. The
results here do not assert that these routes fail, and do not establish a
general obstruction to a Bol-loop moonshine phenomenon.
