from models.model_package_gate import ModelPackageRecord, evaluate_model_package


def test_complete_model_package_is_accepted():
    record = ModelPackageRecord(
        package_id="synthetic-vector-model-v1",
        synthetic_inputs_only=True,
        approval_recorded=True,
        validation_passed=True,
        fallback_defined=True,
        evidence_recorded=True,
        version_incremented=True,
    )
    result = evaluate_model_package(record)
    assert result.decision == "ACCEPT"
    assert result.score == 100


def test_package_missing_fallback_needs_review():
    record = ModelPackageRecord(
        package_id="synthetic-vector-model-v1",
        synthetic_inputs_only=True,
        approval_recorded=True,
        validation_passed=True,
        fallback_defined=False,
        evidence_recorded=True,
        version_incremented=True,
    )
    result = evaluate_model_package(record)
    assert result.decision == "REVIEW"
    assert "fallback" in result.reason


def test_incomplete_package_is_rejected():
    record = ModelPackageRecord(
        package_id="",
        synthetic_inputs_only=False,
        approval_recorded=False,
        validation_passed=False,
        fallback_defined=False,
        evidence_recorded=False,
        version_incremented=False,
    )
    result = evaluate_model_package(record)
    assert result.decision == "REJECT"
