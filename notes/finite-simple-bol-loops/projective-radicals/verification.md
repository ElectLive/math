# How the projective results were checked

The two proofs received **separate independent AI mathematical reviews**. They share the [previous matrix construction](../sources/elementary-psl2-19/README.md) and its [augmentation calculation](../sources/augmentation-chain/README.md); neither new theorem replaces the checks on those inputs. No human-referee, formal-verification or historical-priority claim is made.

| Proof | What was independently challenged | Author check | Independent check |
|---|---|---|---|
| [Fixed-order multiplicity](proofs/multiplicity.md) | True conjugated sign sheets; torus avoidance; non-sign-stable and noncentral normal cuts; the common quotient automorphism in the tensor orbit count | [Python](code/verify_class_two_psl2_19_cubic_multiplicity.py) · [output](checks/nonabelian-class-two-psl2-19-cubic-multiplicity.out) | [Python](code/independent_nonabelian_class_two_psl2_19_cubic_multiplicity.py) · [output](checks/nonabelian-class-two-psl2-19-cubic-multiplicity-independent.out) |
| [Group host](proofs/universal-group-host.md) | Actual native radical products and preservation of the full group center; quadratic lower bound against *arbitrary* group hosts, including small parameter boundaries | [Python](code/verify_size_optimal_universal_radical.py) · [output](checks/size-optimal-universal-radical.out) | [Python](code/independent_optimal_universal_radical.py) · [output](checks/optimal-universal-radical-independent.out) |

Run these from this directory with Python 3 and NumPy. The matrix input is the already-published, compressed canonical JSON. The first two programs share the [augmentation routines](../sources/augmentation-chain/code/verify_psl2_19_infinite_chain.py); the independent program uses the same input data but its own linear algebra and native sign tests.

```sh
data=../sources/elementary-psl2-19/evidence/psl2-19-explicit-matrix-input.json.zlib.b64
export PYTHONPATH=../sources/augmentation-chain/code
python code/verify_class_two_psl2_19_cubic_multiplicity.py "$data"
python code/verify_size_optimal_universal_radical.py "$data"
python code/independent_nonabelian_class_two_psl2_19_cubic_multiplicity.py "$data"
python code/independent_optimal_universal_radical.py
```

The last checker tests every ordered product in two nonisomorphic order-729 groups inside one radical: their four-dimensional commutator pencils have respectively two and zero singular projective points. It does not test associativity for an asserted native subloop.

Mira Cult directed the research. OpenAI models assisted with the mathematics, experimental controls, writing and the separate reviews; exact model versions were not independently verified.
