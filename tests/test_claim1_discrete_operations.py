from src.claim1_discrete_operations import run

def test_all_source_operations_preserve_fixture_betti():
    rows, control=run()
    assert [r[0] for r in rows] == ['GStrongCollapse','GEdgeCollapse','NeighborhoodConing']
    assert all(r[2] == r[3] for r in rows)

def test_destructive_control_changes_invariant():
    _, control=run()
    assert control['expected_failure'] and control['before']['beta0'] == 1 and control['after']['beta0'] == 2
