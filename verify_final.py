#!/usr/bin/env python3
"""Verify the published STPGC dossier without launching large experiments."""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
EXPECTED_ORIGIN = (
    "https://github.com/MachineLearning-Nerd/"
    "icml26-topology-preserving-graph-coarsening"
)
EXPECTED_BRANCHES = {"main"}
EXPECTED_IDENTITY = (
    "MachineLearning-Nerd",
    "MachineLearning-Nerd@users.noreply.github.com",
)
EXPECTED_REPOSITORY = "MachineLearning-Nerd/icml26-topology-preserving-graph-coarsening"
EXPECTED_OVERALL_VERDICT = "PARTIAL_CLAIM_1_TOY_CLAIMS_2_TO_6_UNVERIFIED"
EXPECTED_PUBLICATION_BOUNDARY = "PARTIAL_TOY_ONLY_NO_FULL_REPRODUCTION"
ERRORS: list[str] = []


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        ERRORS.append(message)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(relative: str) -> dict:
    path = ROOT / relative
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        ERRORS.append(f"{relative}: cannot parse JSON: {exc}")
        return {}


def main() -> int:
    origin_result = run("git", "remote", "get-url", "origin")
    origin = origin_result.stdout.strip().removesuffix(".git").rstrip("/")
    require(origin == EXPECTED_ORIGIN, f"unexpected origin: {origin!r}")

    symref = run("git", "ls-remote", "--symref", "origin", "HEAD")
    require(
        "ref: refs/heads/main\tHEAD" in symref.stdout,
        "origin HEAD does not point to main",
    )

    heads = run("git", "ls-remote", "--heads", "origin")
    remote_branches = set()
    for line in heads.stdout.splitlines():
        fields = line.split("\t", 1)
        if len(fields) == 2 and fields[1].startswith("refs/heads/"):
            remote_branches.add(fields[1].removeprefix("refs/heads/"))
    require(remote_branches == EXPECTED_BRANCHES, f"remote branches: {sorted(remote_branches)}")
    require(
        not any(branch.startswith("orx/") for branch in remote_branches),
        "old orx branch remains on the remote",
    )

    local_heads = run(
        "git",
        "for-each-ref",
        "--format=%(refname:strip=2)",
        "refs/heads",
    )
    local_branches = set(filter(None, local_heads.stdout.splitlines()))
    require(
        local_branches <= EXPECTED_BRANCHES,
        f"unexpected local branches: {sorted(local_branches - EXPECTED_BRANCHES)}",
    )
    old_refs = run("git", "for-each-ref", "refs/original")
    require(not old_refs.stdout.strip(), "refs/original exists")

    count_result = run("git", "rev-list", "--count", "--all")
    try:
        commit_count = int(count_result.stdout.strip())
    except ValueError:
        commit_count = 0
    require(commit_count >= 5, f"reachable commit count is only {commit_count}")

    identity_output = run(
        "git",
        "log",
        "--all",
        "--format=%an%x09%ae%x09%cn%x09%ce",
    ).stdout
    for line in filter(None, identity_output.splitlines()):
        fields = line.split("\t")
        require(len(fields) == 4, f"malformed identity row: {line}")
        if len(fields) == 4:
            author_name, author_email, committer_name, committer_email = fields
            require(
                (author_name, author_email) == EXPECTED_IDENTITY,
                f"non-canonical author identity: {line}",
            )
            require(
                (committer_name, committer_email) == EXPECTED_IDENTITY,
                f"non-canonical committer identity: {line}",
            )
    messages = run("git", "log", "--all", "--format=%B").stdout
    require(
        "Co-authored-by:" not in messages and "Co-Authored-By:" not in messages,
        "co-author trailer found in commit messages",
    )

    required_files = [
        "README.md",
        "STATUS.md",
        "BRANCH_AUDIT.md",
        "AUTHOR_THANK_YOU.md",
        "CITATION.cff",
        "CLAIM_EVIDENCE.md",
        "ENVIRONMENT.md",
        "REPORT.md",
        "SOURCE_AUDIT.md",
        "claims.json",
        "reproduction_verdicts.json",
        "AUTONOMOUS_STATE.json",
        "EVIDENCE_MANIFEST.json",
        "verify_final.py",
        "contract/live_claims.json",
        "evidence/source/SHA256SUMS",
        "evidence/upstream/UPSTREAM_PIN.txt",
        "outputs/claim1_discrete_operations/SHA256SUMS",
        "outputs/claim1_discrete_operations/result.json",
        "outputs/claim1_discrete_operations/results.csv",
        "outputs/claim1_discrete_operations/run.log",
    ]
    for relative in required_files:
        require((ROOT / relative).is_file(), f"missing required file: {relative}")

    manifest = load_json("EVIDENCE_MANIFEST.json")
    require(manifest.get("branch_contract") == {
        "default": "main",
        "total": 1,
        "descriptive": 0,
        "old_prefix_absent": "orx/",
    }, "branch contract mismatch")
    require(
        manifest.get("repository") == EXPECTED_REPOSITORY,
        "manifest repository mismatch",
    )
    require(
        manifest.get("overall_verdict") == EXPECTED_OVERALL_VERDICT
        and manifest.get("publication_allowed") is False
        and manifest.get("publication_boundary") == EXPECTED_PUBLICATION_BOUNDARY
        and manifest.get("score_claim") is False
        and manifest.get("official_author_endorsement") is False,
        "manifest publication boundary mismatch",
    )
    require(
        manifest.get("attribution", {}).get("email") == EXPECTED_IDENTITY[1],
        "manifest attribution mismatch",
    )
    for relative, expected in manifest.get("aggregates", {}).items():
        path = ROOT / relative
        require(path.is_file(), f"missing aggregate input: {relative}")
        if path.is_file():
            require(sha256(path) == expected, f"aggregate hash mismatch: {relative}")
    for row in manifest.get("files", []):
        relative = row.get("path", "")
        path = ROOT / relative
        expected = row.get("sha256")
        require(path.is_file(), f"manifest file missing: {relative}")
        require(expected not in (None, "", "PENDING"), f"manifest hash pending: {relative}")
        if path.is_file() and expected not in (None, "", "PENDING"):
            require(sha256(path) == expected, f"manifest hash mismatch: {relative}")

    claims = load_json("claims.json")
    expected_statuses = {
        1: "TOY_FINITE_OPERATION_FIXTURES",
        2: "UNVERIFIED_NOT_STARTED",
        3: "UNVERIFIED_NOT_STARTED",
        4: "UNVERIFIED_NOT_STARTED",
        5: "UNVERIFIED_NOT_STARTED",
        6: "UNVERIFIED_NOT_STARTED",
    }
    actual_claims = {item.get("id"): item for item in claims.get("claims", [])}
    require(set(actual_claims) == set(expected_statuses), "claims.json IDs mismatch")
    for claim_id, status in expected_statuses.items():
        require(
            actual_claims.get(claim_id, {}).get("status") == status,
            f"claims.json status mismatch for Claim {claim_id}",
        )
    reproduction = load_json("reproduction_verdicts.json")
    state = load_json("AUTONOMOUS_STATE.json")
    require(
        claims.get("repository") == EXPECTED_REPOSITORY
        and claims.get("overall_verdict") == EXPECTED_OVERALL_VERDICT
        and claims.get("publication_allowed") is False
        and claims.get("publication_boundary") == EXPECTED_PUBLICATION_BOUNDARY
        and claims.get("score_claim") is False
        and claims.get("official_author_endorsement") is False,
        "claims publication boundary mismatch",
    )
    require(
        reproduction.get("repository") == EXPECTED_REPOSITORY
        and reproduction.get("overall_verdict") == EXPECTED_OVERALL_VERDICT
        and reproduction.get("publication_allowed") is False
        and reproduction.get("publication_boundary") == EXPECTED_PUBLICATION_BOUNDARY
        and reproduction.get("score_claim") is False
        and reproduction.get("official_author_endorsement") is False
        and {
            str(row.get("id")).removeprefix("C"): row.get("status")
            for row in reproduction.get("claims", [])
        }
        == {
            "1": "TOY_FINITE_OPERATION_FIXTURES",
            "2": "UNVERIFIED_NOT_STARTED",
            "3": "UNVERIFIED_NOT_STARTED",
            "4": "UNVERIFIED_NOT_STARTED",
            "5": "UNVERIFIED_NOT_STARTED",
            "6": "UNVERIFIED_NOT_STARTED",
        },
        "reproduction verdict boundary mismatch",
    )
    require(
        state.get("github_repository") == "https://github.com/" + EXPECTED_REPOSITORY
        and state.get("phase") == "published_scoped_partial_audit"
        and state.get("publication_allowed") is False
        and state.get("overall_verdict") == EXPECTED_OVERALL_VERDICT
        and state.get("publication_boundary") == EXPECTED_PUBLICATION_BOUNDARY
        and state.get("score_claim") is False
        and state.get("official_author_endorsement") is False
        and state.get("live_verification", {}).get("branch_count") == 1
        and state.get("live_verification", {}).get("default_branch") == "main"
        and state.get("verified_reachable_commits") == 7,
        "state publication boundary mismatch",
    )
    require(
        state.get("attribution", {}).get("email") == EXPECTED_IDENTITY[1],
        "state attribution mismatch",
    )

    source_manifest = (ROOT / "evidence/source/SHA256SUMS").read_text().splitlines()
    for line in source_manifest:
        fields = line.split()
        require(len(fields) == 2, f"malformed source hash row: {line}")
        if len(fields) == 2:
            digest, relative = fields
            path = ROOT / "evidence/source" / relative
            require(path.is_file(), f"source file missing: {relative}")
            if path.is_file():
                require(sha256(path) == digest, f"source hash mismatch: {relative}")

    output_manifest = (ROOT / "outputs/claim1_discrete_operations/SHA256SUMS").read_text().splitlines()
    for line in output_manifest:
        fields = line.split()
        require(len(fields) == 2, f"malformed output hash row: {line}")
        if len(fields) == 2:
            digest, relative = fields
            path = ROOT / "outputs/claim1_discrete_operations" / relative
            require(path.is_file(), f"output file missing: {relative}")
            if path.is_file():
                require(sha256(path) == digest, f"output hash mismatch: {relative}")

    result = load_json("outputs/claim1_discrete_operations/result.json")
    require(
        result.get("source_upstream_commit")
        == "9f73ec9500b084e27be7a37f5007de5abe60d2c3",
        "upstream commit mismatch",
    )
    rows = result.get("rows", [])
    require([row.get("operation") for row in rows] == [
        "GStrongCollapse",
        "GEdgeCollapse",
        "NeighborhoodConing",
    ], "Claim 1 operation set mismatch")
    require(
        all(
            row.get("beta0_before") == row.get("beta0_after")
            and row.get("beta1_before") == row.get("beta1_after")
            for row in rows
        ),
        "Claim 1 invariant result mismatch",
    )
    negative = result.get("negative_control", {})
    require(negative.get("expected_failure") is True, "negative control did not fail")
    require(
        negative.get("before", {}).get("beta0") == 1
        and negative.get("after", {}).get("beta0") == 2,
        "negative control beta0 mismatch",
    )

    try:
        sys.path.insert(0, str(ROOT))
        from src.claim1_discrete_operations import run as run_claim1

        recomputed_rows, recomputed_control = run_claim1()
        require(len(recomputed_rows) == 3, "recomputed Claim 1 row count mismatch")
        require(
            all(before == after for _, _, before, after, _ in recomputed_rows),
            "recomputed Claim 1 invariant mismatch",
        )
        require(
            recomputed_control.get("expected_failure") is True,
            "recomputed negative control did not fail",
        )
    except Exception as exc:
        ERRORS.append(f"Claim 1 recomputation failed: {exc}")

    document_markers = {
        "README.md": (
            "PARTIAL_CLAIM_1_TOY_CLAIMS_2_TO_6_UNVERIFIED",
            "reproduction_verdicts.json",
            "AUTONOMOUS_STATE.json",
            "publication_allowed=false",
            "score_claim=false",
            "official_author_endorsement=false",
        ),
        "STATUS.md": (
            "published_scoped_partial_audit",
            "PARTIAL_CLAIM_1_TOY_CLAIMS_2_TO_6_UNVERIFIED",
            "reproduction_verdicts.json",
        ),
        "REPORT.md": (
            "PARTIAL_CLAIM_1_TOY_CLAIMS_2_TO_6_UNVERIFIED",
            "publication_allowed=false",
            "official_author_endorsement=false",
        ),
    }
    for relative, markers in document_markers.items():
        document = (ROOT / relative).read_text()
        for marker in markers:
            require(marker in document, f"{relative} missing marker: {marker}")

    if ERRORS:
        print("FINAL_AUDIT=FAILED")
        for error in ERRORS:
            print(f"- {error}")
        return 1
    print(
        f"FINAL_AUDIT=VERIFIED branches={len(remote_branches)} "
        f"commits={commit_count} claim1=toy claims2-6=unverified"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
