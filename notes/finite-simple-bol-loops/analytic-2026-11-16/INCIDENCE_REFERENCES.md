# References for the trace–exponential counting theorem

The [application manuscript](manuscripts/bol-collective-incidence.md) also draws on the [collective cancellation bibliography](REFERENCES.md) for the trace-form construction, frame operators and code duality.

### INCIDENCE-LHL

Boaz Barak, Yevgeniy Dodis, Hugo Krawczyk, Olivier Pereira, Krzysztof
Pietrzak, Francois-Xavier Standaert and Yu Yu,
*Leftover Hash Lemma, Revisited*, author version dated 3 September 2011.
[Primary author PDF](https://cs.nyu.edu/~dodis/ps/lhl.pdf).
Definition 2.2 and Lemma 2.1, printed page 6, discuss almost-universal
hashing. Lemma 3.1, printed pages 7–8, applies to **any finite output
alphabet** and bounds test-function deviation by its variance times the
conditional collision excess. With output alphabet of size seven,
side information equal to the seed, and test function the output-set
indicator, it supplies the conversion used in SMALL. Theorem 3.1,
page 8, gives the related generalized leftover hash lemma for bit outputs;
we use the preceding arbitrary-alphabet lemma directly. The exact
collision profile and radical extremizers are calculated in COL, not
attributed to this source.

### INCIDENCE-BILINEAR

Le Anh Vinh, *On the solvability of systems of bilinear equations in finite
fields*, arXiv:0903.1156v1, 6 March 2009.
[Primary version](https://arxiv.org/pdf/0903.1156v1).
Section 2, Lemma 2.1 and Theorem 2.2, printed pages 3–4, bound the
second moment and incidences for a nondegenerate bilinear form on
F_q^d at a nonzero target. The error is
q^((d-1)/2) sqrt(|U||V|).
The application manuscript states the rank-quotient comparator and pays
the dimension and multiplicity costs of an explicit F7 feature encoding.
The source does not directly apply to the compound trace–exponential
readout. Exact theorem and hypotheses were inspected.

### INCIDENCE-FLATS

Nguyen Duy Phuong, Pham Van Thang and Le Anh Vinh,
*Incidences between planes over finite fields*,
arXiv:1510.03481v1, 12 October 2015.
[Primary PDF displaying v1](https://arxiv.org/pdf/1510.03481).
Theorem 1.5, printed page 2, states the earlier point/flat result
attributed there to Bennett–Iosevich–Pakianathan; Theorem 1.6, page 3,
is the authors' flat/flat generalization. Section 2, Lemma 2.1,
pages 4–5, gives the biregular mixing framework.
The paper's asymptotic parameter is q. Our manuscript instead calculates
the exact full point/flat Gram at q=3 with growing dimension and retains
flat multiplicities. This avoids transplanting a q-asymptotic factor.


### INCIDENCE-UNIVERSAL-HASHING

J. Lawrence Carter and Mark N. Wegman, *Universal classes of hash functions*,
Journal of Computer and System Sciences 18 (1979), 143–154,
DOI [10.1016/0022-0000(79)90044-8](https://doi.org/10.1016/0022-0000(79)90044-8).
[Primary IBM record](https://research.ibm.com/publications/universal-classes-of-hash-functions--1).
This is the historical universal-hashing reference. The manuscript proves
its particular affine seven-symbol control directly by pair counting;
no unverified theorem number is attributed to the paper.
The stronger directly applicable modern finite-alphabet source is
INCIDENCE-LHL above.

This bounded search distinguishes established methods from the specified
family's exact degree/collision statistics, new applications and controlled
comparisons. It does not establish a literature-wide priority claim.
