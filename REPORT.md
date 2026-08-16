# STPGC reproduction audit report

## Result

This repository has one **TOY_FINITE_OPERATION_FIXTURES** result and five
**UNVERIFIED_NOT_STARTED** claims.

Claim 1's local fixture executes clean-room versions of GStrongCollapse,
GEdgeCollapse, and NeighborhoodConing on three deterministic tiny graphs. All
three preserve clique-complex beta0 and beta1. A destructive non-dominance
control changes beta0, demonstrating that the check can reject an invalid
operation.

## Claim status

| Claim | Status | Evidence |
| --- | --- | --- |
| 1 | TOY_FINITE_OPERATION_FIXTURES | Three tiny source-faithful fixtures plus a destructive control |
| 2 | UNVERIFIED_NOT_STARTED | No homotopy-equivalence proof or larger audit |
| 3 | UNVERIFIED_NOT_STARTED | No shortest-path or receptive-field audit |
| 4 | UNVERIFIED_NOT_STARTED | No DBLP data or GNN benchmark |
| 5 | UNVERIFIED_NOT_STARTED | No cit-Patent or multi-dataset timing study |
| 6 | UNVERIFIED_NOT_STARTED | No ExactCoarsening Betti trajectory |

## What this does not claim

The toy does not reproduce the paper's DBLP runtime or node-classification
numbers, the cit-Patent acceleration, near-linear scaling, universal
homotopy/shortest-path statements, or ExactCoarsening comparison. No external
judge score or author endorsement is claimed.

The paper's six-claim maximum-point contract remains untouched. A toy fixture
is recorded as a scoped mechanism audit rather than promoted to a paper-scale
verdict.
