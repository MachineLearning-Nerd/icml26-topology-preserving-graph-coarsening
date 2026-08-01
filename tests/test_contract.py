import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
def test_contract_has_six_live_claims(): assert len(json.loads((ROOT/'contract/live_claims.json').read_text()))==6
def test_source_manifest_entries_exist():
 for line in (ROOT/'evidence/source/SHA256SUMS').read_text().splitlines(): assert (ROOT/'evidence/source'/line.split()[-1]).exists()
