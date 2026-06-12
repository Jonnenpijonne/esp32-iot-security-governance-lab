from models.authorized_exercise_gate import ExerciseGateInput, evaluate_exercise_gate


def test_gate_go_baseline():
    data = ExerciseGateInput(
        exercise_id="SYNTH-EX-001",
        written_permission=True,
        scope_defined=True,
        safety_boundary_defined=True,
        rollback_owner_defined=True,
        evidence_location_defined=True,
        communication_channel_defined=True,
        live_impact_expected=False,
    )
    result = evaluate_exercise_gate(data)
    assert result.status == "GO"
    assert result.score == 100


def test_gate_prepare_baseline():
    data = ExerciseGateInput(
        exercise_id="SYNTH-EX-002",
        written_permission=True,
        scope_defined=True,
        safety_boundary_defined=False,
        rollback_owner_defined=True,
        evidence_location_defined=False,
        communication_channel_defined=True,
        live_impact_expected=False,
    )
    result = evaluate_exercise_gate(data)
    assert result.status == "PREPARE"
    assert result.score == 75


def test_gate_no_go_baseline():
    data = ExerciseGateInput(
        exercise_id="SYNTH-EX-003",
        written_permission=False,
        scope_defined=False,
        safety_boundary_defined=False,
        rollback_owner_defined=False,
        evidence_location_defined=False,
        communication_channel_defined=False,
        live_impact_expected=True,
    )
    result = evaluate_exercise_gate(data)
    assert result.status == "NO_GO"
    assert result.score == 0
