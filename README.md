# Scalable Topology-Preserving Graph Coarsening

Independent reproduction workspace for:

> Xiang Wu, Rong-Hua Li, Xunkai Li, Kangfei Zhao, Hongchao Qin, and Guoren Wang, “Scalable Topology-Preserving Graph Coarsening: Concepts and Algorithms.”

Paper: [arXiv:2601.22943v2](https://arxiv.org/abs/2601.22943v2) · [HTML paper](https://arxiv.org/html/2601.22943) · [OpenReview submission WtINGEMjTB](https://openreview.net/forum?id=WtINGEMjTB) · [ICML 2026 poster](https://icml.cc/virtual/2026/poster/63471).

This is an independent audit, not an author-maintained implementation. The
current repository has one local deterministic Claim 1 toy and has not started
the DBLP/GNN or large-scale experiments required by Claims 2–6. The status is
deliberately conservative so that a passing toy is not mistaken for a full paper
reproduction.

## Current status

| Claim | Paper target | Repository evidence | Verdict |
| --- | --- | --- | --- |
| 1 | STPGC extends graph strong collapse, graph edge collapse, and NeighborhoodConing | Three source-faithful tiny fixtures preserve clique-complex `Betti_0`/`Betti_1`; a destructive non-dominance control changes `Betti_0` | **TOY ONLY** |
| 2 | Lemma 2.5: strong/edge collapse preserve homotopy equivalence | No independent general proof or larger fixture yet | **UNVERIFIED** |
| 3 | Strong collapse and NeighborhoodConing do not increase shortest paths; edge collapse increases them by at most one | No distance/receptive-field audit yet | **UNVERIFIED** |
| 4 | DBLP runtime and node-classification results at coarsening ratio `c=0.1` | No DBLP or GNN benchmark run | **UNVERIFIED** |
| 5 | Up to 37× cit-Patent acceleration and near-linear scalability | No large-graph runtime study | **UNVERIFIED** |
| 6 | ExactCoarsening strictly preserves `Betti_1` through the coarsening phase | No full ExactCoarsening trajectory | **UNVERIFIED** |

The Claim 1 toy runs locally with no remote or paid compute:

```bash
python3 src/claim1_discrete_operations.py --out outputs/claim1_discrete_operations
(cd outputs/claim1_discrete_operations && sha256sum -c SHA256SUMS)
```

It reports `(Betti_0, Betti_1) = (1, 0)` before and after each of
`GStrongCollapse`, `GEdgeCollapse`, and `NeighborhoodConing`. Removing the
middle node of a three-node path without a dominance certificate changes
`Betti_0` from 1 to 2, demonstrating that the control can fail.

## Audit dossier

The repository-level audit record is split into small, reviewable documents:

- [CLAIM_EVIDENCE.md](CLAIM_EVIDENCE.md) maps all six claims to their current
  evidence producers, controls, and explicit unverified boundaries.
- [SOURCE_AUDIT.md](SOURCE_AUDIT.md) records the paper, challenge contract,
  source hashes, upstream pin, and former/current repository names.
- [ENVIRONMENT.md](ENVIRONMENT.md) records the local command, artifact runtime,
  resource policy, and no-large-workload boundary.
- [REPORT.md](REPORT.md) gives the concise scoped result and limitations.
- [BRANCH_AUDIT.md](BRANCH_AUDIT.md) records the main-only branch topology,
  attribution contract, and final verifier.
- [claims.json](claims.json) is the machine-readable status ledger.
- [CITATION.cff](CITATION.cff) and [AUTHOR_THANK_YOU.md](AUTHOR_THANK_YOU.md)
  provide citation metadata and the thank-you note to the paper authors.
- [EVIDENCE_MANIFEST.json](EVIDENCE_MANIFEST.json) hashes the dossier and
  immutable source/toy evidence.

The current result is intentionally conservative: Claim 1 is
<code>TOY_FINITE_OPERATION_FIXTURES</code>; Claims 2–6 are
<code>UNVERIFIED_NOT_STARTED</code>. Run the lightweight final check with:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_final.py
~~~

## How the current claim evidence is produced

| Claim | Evidence path | What is and is not established |
| --- | --- | --- |
| 1 | `contract/live_claims.json` defines the target; `CLAIM_1_PROTOCOL.md` records the protocol; `src/claim1_discrete_operations.py` implements three deterministic fixtures; `outputs/claim1_discrete_operations/{results.csv,result.json,run.log,SHA256SUMS}` stores the result | The local operations mirror the pinned Algorithms 1–3 on tiny graphs and preserve two Betti numbers. This is not a DBLP/GNN reproduction or a universal homotopy proof. |
| 2 | Planned independent homotopy/equivalence audit | No evidence has been produced. |
| 3 | Planned shortest-path and receptive-field audit | No evidence has been produced. |
| 4 | Planned reproduction of the DBLP node-classification and runtime tables | No dataset, baseline, or GNN result is currently included. |
| 5 | Planned scalability audit on cit-Patent, LiveJournal, YouTube, and Flixster | No large-graph timing evidence is currently included. |
| 6 | Planned ExactCoarsening Betti trajectory audit | No full trajectory or competing-method comparison is currently included. |

The source boundary is pinned in
[`evidence/claim1_attempt1/source_locations.md`](evidence/claim1_attempt1/source_locations.md).
The paper source is stored under `evidence/source/`, and the public upstream
implementation is pinned in
[`evidence/upstream/UPSTREAM_PIN.txt`](evidence/upstream/UPSTREAM_PIN.txt) at
`BITNEO/STPGC` commit `9f73ec9500b084e27be7a37f5007de5abe60d2c3`.

## Repository map

- `contract/` — the six live claim texts and immutable contract manifests.
- `evidence/source/` — source archive and checksums for the paper record.
- `evidence/upstream/` — upstream repository commit pin.
- `src/claim1_discrete_operations.py` — clean-room local operation fixtures.
- `outputs/claim1_discrete_operations/` — raw CSV/JSON, run log, and hashes.
- `logbook/claim-1.md` — detailed Claim 1 protocol, outcome, and limitations.
- `tests/` — contract and Claim 1 checks.

## Branch state

Only `main` exists in the current repository. There are no hidden experiment
branches or `orx/*` branches to interpret. If later claims are implemented, each
experiment branch should document its exact claim, source assumptions, command,
raw output, independent checker, negative control, and reproduction status before
it is published.

## Citation

```bibtex
@inproceedings{wu2026scalable,
  title     = {Scalable Topology-Preserving Graph Coarsening: Concepts and Algorithms},
  author    = {Wu, Xiang and Li, Rong-Hua and Li, Xunkai and Zhao, Kangfei and Qin, Hongchao and Wang, Guoren},
  booktitle = {Proceedings of the 43rd International Conference on Machine Learning},
  year      = {2026},
  eprint    = {2601.22943},
  archivePrefix = {arXiv},
  primaryClass = {cs.LG},
  doi       = {10.48550/arXiv.2601.22943}
}
```

## Thank you

Thank you to Xiang Wu, Rong-Hua Li, Xunkai Li, Kangfei Zhao, Hongchao Qin, and
Guoren Wang for making the STPGC concepts, algorithms, source record, and claims
available for inspection. The explicit definitions of graph strong collapse,
graph edge collapse, and NeighborhoodConing make a careful local audit possible.

This repository is intended as a transparent companion audit: it records what has
actually been reproduced, what remains untouched, and where future evidence must
come from.

## Attribution

Approved repository commits are attributed to:

```text
MachineLearning-Nerd <37579156+MachineLearning-Nerd@users.noreply.github.com>
```
