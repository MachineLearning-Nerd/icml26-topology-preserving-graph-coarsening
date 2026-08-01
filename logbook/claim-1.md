# Claim 1 — graph-coarsening operations

**Exact live claim:** STPGC extends graph strong collapse and graph edge collapse from algebraic topology into scalable graph coarsening algorithms, including GStrongCollapse, GEdgeCollapse, and NeighborhoodConing (Section 3.1, Section 3.2, Section 3.3).

**Outcome: toy (local discrete-operation fixture; not a DBLP/GNN reproduction).**

## Source-faithful local protocol

The pinned paper source (`evidence/source/arxiv_source.tar.gz`, `STPGC_ICML_CR.tex` Algorithms 1--3) and pinned upstream implementation (`evidence/upstream/UPSTREAM_PIN.txt`, `GNN/graph_coarsening.py`) define closed-neighborhood node dominance, open-neighborhood edge dominance, and neighborhood coning. `src/claim1_discrete_operations.py` independently implements those discrete operations on three deterministic graph fixtures and measures clique-complex `(Betti_0, Betti_1)` before/after each operation. Source locations are retained in `evidence/claim1_attempt1/source_locations.md`.

## Execution and retained evidence

```bash
python3 src/claim1_discrete_operations.py --out outputs/claim1_discrete_operations
(cd outputs/claim1_discrete_operations && sha256sum -c SHA256SUMS)
```

`outputs/claim1_discrete_operations/results.csv` retains three fixtures:

| Operation | Fixture | Result |
|---|---|---|
| GStrongCollapse | pendant node into triangle dominator | `(1,0) -> (1,0)` |
| GEdgeCollapse | dominated edge of a triangle | `(1,0) -> (1,0)` |
| NeighborhoodConing | two-edge star, insert a dominated edge then remove apex | `(1,0) -> (1,0)` |

A destructive non-dominance middle-node deletion on a three-node path changes `Betti_0: 1 -> 2`, so the invariant check is capable of failing.

## Limits

These exact small graph operations support only a reduced local toy outcome. They do not reproduce the DBLP-scale GNN experiments, scalability claims, or a general homotopy proof.
