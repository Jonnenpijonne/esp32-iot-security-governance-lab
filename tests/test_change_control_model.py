from models.change_control_model import ChangeControlRecord, calculate_blast_radius, evaluate_change_control


def test_low_blast_radius_change_can_proceed():
    record = ChangeControlRecord(
        change_id="SYNTH-CHANGE-001",
        affected_devices=1,
        affected_areas=1,
        network_enabled=False,
        telemetry_enabled=False,
        persistent_storage_enabled=False,
        rollback_steps_defined=True,
        rollback_tested=True,
        validation_passed=True,
        evidence_recorded=True,
    )
    result = evaluate_change_control(record)
    assert calculate_blast_radius(record) == "LOW"
    assert result.decision == "PROCEED"
    assert result.score == 100


def test_medium_blast_radius_requires_review():
    record = ChangeControlRecord(
        change_id="SYNTH-CHANGE-002",
        affected_devices=3,
        affected_areas=1,
        network_enabled=False,
        telemetry_enabled=False,
        persistent_storage_enabled=False,
        rollback_steps_defined=True,
        rollback_tested=True,
        validation_passed=True,
        evidence_recorded=True,
    )
    result = evaluate_change_control(record)
    assert calculate_blast_radius(record) == "MEDIUM"
    assert result.decision == "REVIEW"


def test_missing_rollback_test_stops_or_reviews_change():
    record = ChangeControlRecord(
        change_id="SYNTH-CHANGE-003",
        affected_devices=1,
        affected_areas=1,
        network_enabled=False,
        telemetry_enabled=False,
        persistent_storage_enabled=False,
        rollback_steps_defined=True,
        rollback_tested=False,
        validation_passed=True,
        evidence_recorded=True,
    )
    result = evaluate_change_control(record)
    assert result.decision == "REVIEW"
    assert "rollback" in result.reason


def test_high_blast_radius_cannot_auto_proceed():
    record = ChangeControlRecord(
        change_id="SYNTH-CHANGE-004",
        affected_devices=10,
        affected_areas=3,
        network_enabled=False,
        telemetry_enabled=False,
        persistent_storage_enabled=False,
        rollback_steps_defined=True,
        rollback_tested=True,
        validation_passed=True,
        evidence_recorded=True,
    )
    result = evaluate_change_control(record)
    assert calculate_blast_radius(record) == "HIGH"
    assert result.decision == "REVIEW"
