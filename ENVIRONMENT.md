# Environment and reproduction record

## Fixed local entrypoint

The committed Claim 1 command is:

~~~bash
python3 src/claim1_discrete_operations.py --out outputs/claim1_discrete_operations
(cd outputs/claim1_discrete_operations && sha256sum -c SHA256SUMS)
~~~

The retained artifact was generated with Python 3.14.5 on a Linux x86_64
machine. The code uses only the Python standard library. No Hugging Face Job,
paid compute, remote service, or external dataset was used.

## What ran

| Workload | Scale | Result |
| --- | --- | --- |
| GStrongCollapse fixture | one tiny graph | (beta0, beta1) preserved: (1,0) to (1,0) |
| GEdgeCollapse fixture | one triangle | (beta0, beta1) preserved: (1,0) to (1,0) |
| NeighborhoodConing fixture | one two-edge star | (beta0, beta1) preserved: (1,0) to (1,0) |
| Destructive control | one three-node path | beta0 changes from 1 to 2 as intended |

The command writes the raw CSV, JSON, log, and checksum manifest already
committed under <code>outputs/claim1_discrete_operations/</code>. This dossier
does not rerun or rewrite those outputs.

## Source and implementation pins

- Paper PDF SHA-256:
  <code>215d2b0491b2cab3225c351570e9986f9984cfa228b4ce4e5722d1084ac491cf</code>
- Paper source archive SHA-256:
  <code>dcb4be3149eb266c308a502e1d41fe75677a320c09b21fa63572afdfeb5234f0</code>
- Upstream STPGC commit:
  <code>9f73ec9500b084e27be7a37f5007de5abe60d2c3</code>

## Scope policy

Claims 2–6 have no produced evidence in this repository. A future run must
record its exact source contract, data, command, machine allocation, raw output,
independent checker, and negative control before changing those statuses. The
final verifier is intentionally lightweight and never launches DBLP/GNN,
large-graph, or remote workloads.
