# Branch and attribution audit

## Repository identity

- Current repository:
  <https://github.com/MachineLearning-Nerd/icml26-topology-preserving-graph-coarsening>
- Former repository:
  <code>icml26-repro-WtINGEMjTB-topology-preserving-graph-coarsening</code>
- Default branch: <code>main</code>
- Expected remote branches: exactly one
- Former prefix: <code>orx/</code>; no former-prefixed branch exists

The pre-dossier main checkpoint was
<code>a60b5167e8da65d0b0b2063a99e22195ee3cbf7c</code>. A recovery bundle made
before dossier edits has SHA-256
<code>2b64d66fa11acad930dc4edae96927e324c8146f8d6085621b2ce8b3a776267c</code>.
It contains the complete five-commit history.

## Branch contract

Only <code>main</code> is published. There are no experiment-lineage branches
to rename or interpret. Future claim work should add a descriptive branch only
when its source contract, command, raw output, checker, and negative control are
documented.

## Attribution contract

Every reachable commit must use:

<code>MachineLearning-Nerd &lt;MachineLearning-Nerd@users.noreply.github.com&gt;</code>

Commit messages must not contain a <code>Co-authored-by:</code> trailer. The
repository verifier checks author and committer identities across all reachable
refs.

## Verification contract

The publication verifier checks the canonical GitHub origin, main default
branch, exact one-branch topology, commit attribution, dossier hashes, source
and toy-output hashes, claim statuses, raw invariant results, and the destructive
control.

Run it with:

~~~bash
PYTHONDONTWRITEBYTECODE=1 python3 verify_final.py
~~~
