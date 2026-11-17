# Candidate raw-F3 inequality for five exceptional families

**Mira Cult**

Conditional on the primitive-folder and raw-F3 inputs in the repository manuscript [raw-F₃ criterion](sd-raw-involution-count.md), the following excludes SD_k with k≥3 and socle T^k for T=F4(q), E6(q), ²E6(q), E7(q), or E8(q), each q=p^f≥2. This manuscript-local candidate for [C0010](../../claims/0010.md) has the scoped independent review recorded below and makes no global classification claim.

Let n=|T|, t=|Out T|, a=tn and b=#{x∈Aut(T):x²=1}. Put (r,D)=(4,52),(6,78),(6,78),(7,133),(8,248) in the order of the families above. Fulman–Guralnick, Trans. AMS 364 (2012), Lemma 2.1(1)–(2), p3027, and Table 1, p3049, https://dornsife.usc.edu/jason-fulman/wp-content/uploads/sites/224/2023/06/bounded.pdf, give k(Aut T)≤t k(T)≤8tq^r. The stated simple-group bound follows by passing to the simple central quotient of the simply connected form. The explicit twisted ²E6 entry uses q, without an almost-simple twisted-rank interpretation. Frobenius–Schur and Cauchy–Schwarz give b²≤a k(Aut T), so b<3tq^(r/2) sqrt(n).

Lucchini–Marion–Tracey, *Generating maximal subgroups of finite almost simple groups*, Forum Math. Sigma 8 (2020), Prop. 3.11 and Table 2 pp20–21, https://pure-oai.bham.ac.uk/ws/portalfiles/portal/147250970/LUCCHINI_et_al_2020_Forum_of_Mathematics_Sigma.pdf, give t≤6f≤6q. Their table includes the extra F4 graph factor in characteristic two, t=2f; E6 has t=2f gcd(3,q−1), ²E6 has t=2f gcd(3,q+1), E7 has t=f gcd(2,q−1), and E8 has t=f.

Craven–Oliver–Semeraro, *Reduced fusion systems over p-groups with abelian subgroup of index p: II*, Advances Math. 322 (2017), Table 9.2 p45 of author PDF, https://pure-oai.bham.ac.uk/ws/files/44753700/indp2_AIM_final.pdf, gives the exceptional universal group orders via q-prime cyclotomic factors and the center divisor for the simple quotient. In standard product form the five orders have ≤8 factors q^i±1 with i≥2, denominator ≤3, and leading degree D; positive-root powers are 24,36,36,63,120. In particular ²E6(q) has order q^36(q^12−1)(q^9+1)(q^8−1)(q^6−1)(q^5+1)(q²−1)/gcd(3,q+1). All normalized factors are at least 3/4, so n≥(3/4)^8 q^D/3>q^D/30. All these groups meet n≥2²⁰, since 2^52/30>2²⁰.

Thus

 (b³+3ab)/n² < 34992 q^(3+3r/2−D/2) +1944 q^(2+r/2−D/2).

The largest exponents across these five pairs occur at F4: −17 and −22. Hence for every q≥2 the expression is at most 34992/2^17+1944/2^22<1. This is the required raw-F3 inequality. The external group data and upstream reduction remain explicit dependencies; this argument does not depend on an involution-class square condition or a numerical extrapolation.

## Tits group

For T=²F₄(2)' put n=17,971,200 and a=|Aut(T)|=35,942,400. The GAP 4.15.1 release archive https://github.com/gap-system/gap/releases/download/v4.15.1/gap-4.15.1.tar.gz has SHA-256 `6049d53e99b12e25c2d848db21ac4a06380a46fe4c4157243d556fe06930042c`; its bundled CTblLib 1.3.11 file `pkg/ctbllib/data/ctotwis1.tbl` has SHA-256 `c98913edec288dfcc671ea20a1beb48099ed63595fd1cc5e871b447db96fc8c2`. Its `MOT("2F4(2)'.2",...)` record states origin ATLAS and construction Aut(²F₄(2)'). Its centralizer list and square power map show positions mapping to the identity are 1, 2, 3 with centralizers respectively a, 20480, 3072. Independent GAP read-only query:

```
t:=CharacterTable("2F4(2)'.2");;
Positions(PowerMap(t,2),1);
SizesCentralizers(t){Positions(PowerMap(t,2),1)};
```

The results are `[1,2,3]` and `[35942400,20480,3072]`. Assuming the published character-table data and group identification, the number of elements squaring to one in the full automorphism group is b=1+a/20480+a/3072=13,456. Exact integer arithmetic gives

    b³+3ab = 3,887,319,126,016 < 322,964,029,440,000 = n²,
    n ≥ 2²⁰.

Therefore the raw-F₃ criterion applies subject to that criterion, its upstream hypotheses, and the source data. This arithmetic neither proves the published character table nor establishes a global simple-group census. The scoped independent review is recorded below.

Run `python3 problems/0323-finite-simple-non-moufang-bol-loops/code/verify_sd_exceptional_remaining.py` for exact endpoint and Tits arithmetic. It does not verify the group data or the upstream criterion.

## Independent review

contributor 1 accepted this argument at exact source [the source revision](https://github.com/Mira-Cult/math-wip/commit/f6c7e01a4337b51c703b4d9ffc94d3b84a732fe5), conditional on the raw-F₃ criterion, folder/inversion machinery and cited group data. The review checked the Fulman–Guralnick class bounds and central quotients, Gallagher and Frobenius–Schur steps, Craven–Oliver–Semeraro orders, Lucchini–Marion–Tracey outer orders, normalized-factor bound, exponents and uniform rational endpoint. The Python 3.12.14 certificate passed independently. A separate GAP 4.15.1 / CTblLib 1.3.11 query reproduced the Tits table order, square-map positions and centralizers and checked the `ctotwis1.tbl` hash. Published table correctness and identification remain external inputs; this review does not certify the all-socle assembly.
