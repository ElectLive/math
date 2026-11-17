// Finite support-graph controls for 0323:C0010; C++17, standard library only.
//
// Run from the repository root, writing the executable outside the checkout:
//   c++ -std=c++17 -O3 -Wall -Wextra -pedantic \
//     problems/0323-finite-simple-non-moufang-bol-loops/code/verify_stable_prime_support.cpp \
//     -o "$TMPDIR/verify_stable_prime_support"
//   "$TMPDIR/verify_stable_prime_support"
//
// Conditional geometry: in the pure stable p^2+p+p model with m=h=5,
// the preceding structural reduction has p cross strips (stable (x,0)
// to first paired x), p second-row singleton/residual vertices, and an
// U-equivariant perfect matching on the other stable factors. The order-5
// subgroup acts on their nonzero second coordinates in cosets B. Every
// paired orbit has the form
//   (x,b) <-> (x+s/b,d*b), b in B, x,s in F_p, d B = B' != B.
// The program enumerates every unordered pairing of these cosets, every
// multiplier d giving the partner, and every s. It tests the single actual
// pure reflection tau: (x,b)<->(b,x), first x<->second x.
//
// Coordinate-level graph: matching strip edges and tau edges alternate.
// Each (x,x) is a tau-fixed anchor; each second-row coordinate is a
// singleton or the unique residual leaf. Both kinds are terminal. All
// vertices have degree at most two. A collision-free completed support
// graph must have one anchor and one leaf in every component. During a
// partial matching we may therefore reject an added strip edge if it
// closes a cycle, joins two anchored paths, or joins two leaf paths.
// A closed leaf-to-leaf path is already an unanchored component. These
// conditions are necessary only; zero completions proves the finite
// graph obstruction under the stated geometric inputs. They do not prove
// those inputs, construct a folder, or establish the statement for other p.
// No randomness, network access, input data or output files are used.

#include <algorithm>
#include <array>
#include <cstdint>
#include <cstdlib>
#include <iostream>
#include <set>
#include <stdexcept>
#include <vector>

namespace {

int power_mod(int a, int n, int p) {
    int result = 1;
    while (n > 0) {
        if (n & 1) result = result * a % p;
        a = a * a % p;
        n >>= 1;
    }
    return result;
}

bool prime(int p) {
    if (p < 2) return false;
    for (int d = 2; d <= p / d; ++d)
        if (p % d == 0) return false;
    return true;
}

// A component has bit 1 for an anchor and bit 2 for a paired-output leaf.
// History stores only successful unions, so each search branch rolls back
// exactly to its previous graph without copying the whole state.
class RollbackGraph {
    struct Change { int child, parent, old_size, old_mask; };
    std::vector<int> parent_, size_, mask_;
    std::vector<Change> history_;

public:
    explicit RollbackGraph(int n) : parent_(n), size_(n, 1), mask_(n, 0) {
        for (int i = 0; i < n; ++i) parent_[i] = i;
    }
    int root(int x) const {
        while (parent_[x] != x) x = parent_[x];
        return x;
    }
    std::size_t checkpoint() const { return history_.size(); }
    void rollback(std::size_t checkpoint) {
        while (history_.size() > checkpoint) {
            const Change c = history_.back();
            history_.pop_back();
            parent_[c.child] = c.child;
            size_[c.parent] = c.old_size;
            mask_[c.parent] = c.old_mask;
        }
    }
    bool connect(int a, int b) {
        a = root(a); b = root(b);
        if (a == b || (mask_[a] & mask_[b])) return false;
        if (size_[a] < size_[b]) std::swap(a, b);
        history_.push_back({b, a, size_[a], mask_[a]});
        parent_[b] = a;
        size_[a] += size_[b];
        mask_[a] |= mask_[b];
        return true;
    }
    void terminal(int vertex, int flag) {
        int r = root(vertex);
        if (mask_[r] & flag) throw std::logic_error("invalid initial path");
        mask_[r] |= flag;
    }
};

class Search {
    int p_, rho_;
    std::vector<int> inverse_;
    std::vector<std::vector<int>> cosets_;
    RollbackGraph graph_;
    std::vector<std::uint64_t> nodes_, rejected_;
    std::vector<std::array<int, 4>> witness_;

    int stable(int x, int y) const { return x * p_ + y; }
    int first(int x) const { return p_ * p_ + x; }
    int second(int x) const { return p_ * p_ + p_ + x; }

    bool enumerate(std::uint64_t used, std::size_t depth) {
        ++nodes_[depth];
        if (depth == cosets_.size() / 2) return true;
        std::size_t i = 0;
        while (used & (std::uint64_t{1} << i)) ++i;
        for (std::size_t j = i + 1; j < cosets_.size(); ++j) {
            if (used & (std::uint64_t{1} << j)) continue;
            // Each target for one fixed representative determines a unique
            // multiplier d and hence the entire equivariant orbit bijection.
            for (int target : cosets_[j]) {
                int d = target * inverse_[cosets_[i][0]] % p_;
                for (int s = 0; s < p_; ++s) {
                    const std::size_t mark = graph_.checkpoint();
                    bool valid = true;
                    for (int b : cosets_[i]) {
                        int partner = d * b % p_;
                        int shift = s * inverse_[b] % p_;
                        for (int x = 0; x < p_; ++x) {
                            if (!graph_.connect(stable(x, b),
                                                stable((x + shift) % p_, partner))) {
                                valid = false;
                                break;
                            }
                        }
                        if (!valid) break;
                    }
                    if (valid) {
                        witness_.push_back({static_cast<int>(i), static_cast<int>(j), d, s});
                        if (enumerate(used | (std::uint64_t{1} << i) |
                                                (std::uint64_t{1} << j), depth + 1))
                            return true;
                        witness_.pop_back();
                    } else {
                        ++rejected_[depth];
                    }
                    graph_.rollback(mark);
                }
            }
        }
        return false;
    }

public:
    explicit Search(int p)
        : p_(p), rho_(0), inverse_(p, 0), graph_(p * p + 2 * p) {
        if (!prime(p_) || p_ % 5 != 1) throw std::logic_error("invalid prime");
        for (int x = 2; x < p_; ++x)
            if (power_mod(x, 5, p_) == 1) { rho_ = x; break; }
        if (!rho_ || power_mod(rho_, 5, p_) != 1)
            throw std::logic_error("missing element of order five");
        for (int x = 1; x < p_; ++x) inverse_[x] = power_mod(x, p_ - 2, p_);

        std::set<int> remaining;
        for (int x = 1; x < p_; ++x) remaining.insert(x);
        while (!remaining.empty()) {
            int x = *remaining.begin(), b = x;
            std::vector<int> orbit;
            do {
                if (!remaining.erase(b)) throw std::logic_error("coset overlap");
                orbit.push_back(b);
                b = b * rho_ % p_;
            } while (b != x);
            if (orbit.size() != 5) throw std::logic_error("incorrect coset size");
            cosets_.push_back(orbit);
        }
        if (cosets_.size() % 2 || cosets_.size() >= 64)
            throw std::logic_error("unsupported number of cosets");
        nodes_.assign(cosets_.size() / 2 + 1, 0);
        rejected_.assign(cosets_.size() / 2, 0);

        // Tau edges among stable coordinates, then its paired-row edges,
        // and the forced cross strips. Tau-fixed stable coordinates are
        // anchors; the second paired row consists of terminal leaves.
        for (int x = 0; x < p_; ++x)
            for (int y = x + 1; y < p_; ++y)
                if (!graph_.connect(stable(x, y), stable(y, x)))
                    throw std::logic_error("initial stable edge");
        for (int x = 0; x < p_; ++x) {
            if (!graph_.connect(first(x), second(x)) ||
                !graph_.connect(stable(x, 0), first(x)))
                throw std::logic_error("initial paired edge");
        }
        for (int x = 0; x < p_; ++x) {
            graph_.terminal(stable(x, x), 1);
            graph_.terminal(second(x), 2);
        }
    }

    bool run() {
        bool survivor = enumerate(0, 0);
        std::cout << "p=" << p_ << " rho=" << rho_
                  << " nonzero-orbits=" << cosets_.size()
                  << " collision-free completions=" << (survivor ? "at least one" : "0")
                  << " nodes-by-depth=";
        for (auto x : nodes_) std::cout << ' ' << x;
        std::cout << " rejected-by-depth=";
        for (auto x : rejected_) std::cout << ' ' << x;
        std::cout << '\n';
        if (survivor) {
            for (const auto& w : witness_)
                std::cerr << "pair " << w[0] << ',' << w[1]
                          << " d=" << w[2] << " s=" << w[3] << '\n';
        }
        return !survivor;
    }
};

} // namespace

int main() {
    try {
        bool ok31 = Search(31).run();
        bool ok41 = Search(41).run();
        if (!ok31 || !ok41) return EXIT_FAILURE;
        std::cout << "PASS: no collision-free matching for either finite control\n";
    } catch (const std::exception& e) {
        std::cerr << "FAIL: " << e.what() << '\n';
        return EXIT_FAILURE;
    }
    return EXIT_SUCCESS;
}
