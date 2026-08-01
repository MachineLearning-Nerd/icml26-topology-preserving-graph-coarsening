# Reproduction: Scalable Topology-Preserving Graph Coarsening

Local CPU/GPU clean-room reproduction for ICML 2026 `WtINGEMjTB`.

Exact contract: `contract/live_claims.json`; source and upstream pins: `evidence/`. No HF compute is used.

Claim 1 has a deterministic local **toy** fixture for GStrongCollapse, GEdgeCollapse, and NeighborhoodConing. Run:

```bash
python3 src/claim1_discrete_operations.py --out outputs/claim1_discrete_operations
(cd outputs/claim1_discrete_operations && sha256sum -c SHA256SUMS)
```

It is not a DBLP/GNN benchmark reproduction or a universal topological proof.
