# Replaying the exact 18-square certificate

Use Python 3.10 or later (standard library only) and a C++17 compiler available as `g++` with `__int128` support. Keep Python assertions enabled. From this directory:

```sh
sha256sum -c SHA256SUMS
python3 -S verify_exact_18.py --workers 4
```

The driver checks the exact upper-bound construction, then runs seven lower-bound groups. It compiles its geometry programs in temporary directories and regenerates every geometry state from the supplied rack and case data. It does not read discovery snapshots or earlier success logs. A full replay took about twelve minutes with four workers on the original machine; time depends on hardware and load.

| Group | Finite input | Terminal regions |
|---|---|---:|
| 181 whole cases | [Base case cover](n18-482-base.json) | 235 |
| 53 | [Case subdivisions](full-endpoint-mask-cases.json) | 114 |
| 55 | [Case subdivisions](second-endpoint-mask-cases.json) | 15 |
| 137 | Base case cover; [perpendicular probes](verify_fork_mask.py) | 6 |
| 92 | [Case subdivisions](residual-92-cases.json) | 19 |
| 82 | [Case subdivisions](residual-82-cases.json) | 20 |
| 115 | [Case subdivisions](residual-115-cases.json) | 19 |

All groups share the [21-point rack](stabs18-endpoint-window.json). The common [rack verifier](check_stabs.py) checks the continuous interior-hit property, and the [case-cover code](verify_rack_angle.py) rebuilds the physical orbits and checks complementary cuts. The [geometry kernel](lattice_kernel.cpp) and Python generators implement outward enclosures; the [wall](wall_chord_guard.py), [two-face](genuine_facing_bridge.py) and [perpendicular-probe](double_probe_bridge.py) guards certify the lower bound on branches that retain poses. See the [proof](../proof.md) for how these checks combine.
