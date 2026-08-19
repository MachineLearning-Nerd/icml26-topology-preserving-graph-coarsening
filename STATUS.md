OpenReview ID: WtINGEMjTB
Submission number: 9789
Live claim count / maximum points: 6 / 12
Selection timestamp: 2026-08-01T14:30:38Z
Contract manifest: contract/contract_manifest.json
Source paper/version: arXiv:2601.22943 (SHA-256 in evidence/source/SHA256SUMS)
Official code/data/model pins: https://github.com/BITNEO/STPGC.git @ 9f73ec9500b084e27be7a37f5007de5abe60d2c3
Compute policy: local CPU/local GPU only; no HF cpu-upgrade, Jobs, paid, or remote compute
GitHub repository: https://github.com/MachineLearning-Nerd/icml26-topology-preserving-graph-coarsening
Current phase: published_scoped_partial_audit
Per-claim state: C1 toy — local source-faithful discrete fixtures execute GStrongCollapse, GEdgeCollapse and NeighborhoodConing with a destructive invariant control; C2-C6 not started
Overall verdict: PARTIAL_CLAIM_1_TOY_CLAIMS_2_TO_6_UNVERIFIED.
Publication boundary: publication_allowed=false for a complete reproduction or score; this is a scoped toy-level dossier. score_claim=false and official_author_endorsement=false.
Publication status: renamed, attribution-normalized, dossier-published, pushed, and verified; full scientific claim release remains incomplete
Selection rationale: refreshed live duplicate gate passed; source audit found public upstream code and discrete graph operations suitable for local tests. DBLP-scale claims require separate resource audit.
Initial public commit: 76715f7b27eb4621f86d4e43b63acb90413f1a2f
Evidence: outputs/claim1_discrete_operations/{results.csv,result.json,run.log,SHA256SUMS}; evidence/claim1_attempt1/source_locations.md
Dossier: CLAIM_EVIDENCE.md, SOURCE_AUDIT.md, ENVIRONMENT.md, REPORT.md, claims.json, reproduction_verdicts.json, AUTONOMOUS_STATE.json, EVIDENCE_MANIFEST.json, and verify_final.py
Verification command: PYTHONDONTWRITEBYTECODE=1 python3 verify_final.py
