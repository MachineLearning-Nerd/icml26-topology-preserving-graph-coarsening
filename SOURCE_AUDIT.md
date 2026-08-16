# Source and provenance audit

## Paper identity

- Title: **Scalable Topology-Preserving Graph Coarsening: Concepts and Algorithms**
- Authors: Xiang Wu, Rong-Hua Li, Xunkai Li, Kangfei Zhao, Hongchao Qin, and
  Guoren Wang
- Stable source: [arXiv:2601.22943v2](https://arxiv.org/abs/2601.22943v2)
- HTML source: [arXiv HTML](https://arxiv.org/html/2601.22943)
- OpenReview: [WtINGEMjTB](https://openreview.net/forum?id=WtINGEMjTB)
- ICML poster: [poster 63471](https://icml.cc/virtual/2026/poster/63471)

The challenge contract was retrieved at 2026-08-01T14:30:38Z. The paper PDF
and source archive are retained under <code>evidence/source/</code> with
<code>evidence/source/SHA256SUMS</code>.

## Immutable source hashes

- <code>evidence/source/arxiv.pdf</code>:
  <code>215d2b0491b2cab3225c351570e9986f9984cfa228b4ce4e5722d1084ac491cf</code>
- <code>evidence/source/arxiv_source.tar.gz</code>:
  <code>dcb4be3149eb266c308a502e1d41fe75677a320c09b21fa63572afdfeb5234f0</code>
- <code>evidence/source/SHA256SUMS</code>:
  <code>c8e2158ab51377c332da5522403cc7119e5a1ad10bdfff46e15f3c7afd0a6e87</code>
- <code>evidence/upstream/UPSTREAM_PIN.txt</code>:
  <code>9797ca1e6f2efb95fec33d046047e9d7709de7173ac00797a0cad513b88b5fc7</code>

## Source locations

The source archive's <code>STPGC_ICML_CR.tex</code> contains the three
discrete algorithms near source lines 306, 369, and 454. The method text is near
lines 289–353 and 470–512. The pinned public implementation
<code>BITNEO/STPGC</code> at commit
<code>9f73ec9500b084e27be7a37f5007de5abe60d2c3</code> contains
<code>strong_collapse</code> near line 317,
<code>edge_collapse</code> near line 404, and
<code>insert_dominated_edges_2</code> near line 470.

## Repository identity

- Former name:
  <code>icml26-repro-WtINGEMjTB-topology-preserving-graph-coarsening</code>
- Current name:
  <code>icml26-topology-preserving-graph-coarsening</code>
- Current URL:
  https://github.com/MachineLearning-Nerd/icml26-topology-preserving-graph-coarsening
- Upstream implementation:
  https://github.com/BITNEO/STPGC/tree/9f73ec9500b084e27be7a37f5007de5abe60d2c3

The upstream pin is provenance for source-faithful behavior; this repository's
Claim 1 implementation is an independent clean-room fixture. No author review
or endorsement is inferred.
