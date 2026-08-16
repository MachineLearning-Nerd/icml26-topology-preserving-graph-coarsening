# Claim-to-evidence ledger

## Reading this ledger

The six live claims are defined by
<code>contract/live_claims.json</code>. The status **TOY_FINITE_OPERATION_FIXTURES**
means that a deterministic local fixture exercised the named discrete operations;
it is not a full paper reproduction, a general proof, or a DBLP/GNN result.
**UNVERIFIED_NOT_STARTED** means no independent evidence has been produced for
that claim in this repository.

## Claims and production paths

| Claim | Paper target | Evidence producer | Independent check or control | Status |
| --- | --- | --- | --- | --- |
| 1 | STPGC extends GStrongCollapse, GEdgeCollapse, and NeighborhoodConing | <code>src/claim1_discrete_operations.py</code> implements the three source-faithful operations on deterministic tiny fixtures and computes clique-complex Betti numbers | <code>tests/test_claim1_discrete_operations.py</code> checks all three fixtures; destructive non-dominance removal must change beta0 from 1 to 2; retained files are under <code>outputs/claim1_discrete_operations/</code> | TOY_FINITE_OPERATION_FIXTURES |
| 2 | Lemma 2.5: strong and edge collapse preserve homotopy equivalence | No producer has been implemented | No general proof, larger witness set, or independent checker exists | UNVERIFIED_NOT_STARTED |
| 3 | Shortest-path and receptive-field behavior of the three operations | No producer has been implemented | No distance audit or negative control exists | UNVERIFIED_NOT_STARTED |
| 4 | DBLP c=0.1 runtime and node-classification results | No producer has been implemented | No DBLP data, GNN training/evaluation, or benchmark checker exists | UNVERIFIED_NOT_STARTED |
| 5 | cit-Patent acceleration and near-linear scalability | No producer has been implemented | No large-graph timing study or scaling control exists | UNVERIFIED_NOT_STARTED |
| 6 | ExactCoarsening strictly preserves Betti_1 through coarsening | No producer has been implemented | No full ExactCoarsening trajectory or competing-method comparison exists | UNVERIFIED_NOT_STARTED |

## Claim 1 evidence

The deterministic result contains three rows, each preserving the reported
clique-complex invariants:

| Operation | Fixture | Betti numbers before | Betti numbers after |
| --- | --- | --- | --- |
| GStrongCollapse | pendant_into_dominator | (1, 0) | (1, 0) |
| GEdgeCollapse | triangle_edge | (1, 0) | (1, 0) |
| NeighborhoodConing | two_star_coning | (1, 0) | (1, 0) |

The destructive control removes the middle node from a three-node path without a
dominance certificate. It changes beta0 from 1 to 2 and sets
<code>expected_failure</code> to true. The source operation implementation is
pinned to upstream STPGC commit
<code>9f73ec9500b084e27be7a37f5007de5abe60d2c3</code>.

The exact retained outputs are:

- <code>outputs/claim1_discrete_operations/results.csv</code>
- <code>outputs/claim1_discrete_operations/result.json</code>
- <code>outputs/claim1_discrete_operations/run.log</code>
- <code>outputs/claim1_discrete_operations/SHA256SUMS</code>

## Evidence boundary

The toy uses three hand-sized deterministic fixtures and clique-complex
beta0/beta1 checks. It does not establish the universal homotopy statements,
shortest-path lemmas, DBLP/GNN metrics, cit-Patent speedups, near-linear
scaling, or ExactCoarsening trajectories. Claims 2–6 remain unverified until
their source-faithful protocols and raw evidence are added.
