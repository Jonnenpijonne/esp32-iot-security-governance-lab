from models.emb3d_alignment_model import PropertyAlignment, evaluate_alignment


def test_validated_alignment():
    item = PropertyAlignment(
        property_name="firmware baseline",
        exposure_question="is firmware version known and buildable",
        evidence_reference="platformio.ini, src/main.cpp, firmware workflow",
        ci_validated=True,
        mitigation_evidenced=True,
        property_identified=True,
    )
    result = evaluate_alignment(item)
    assert result.status == "VALIDATED"
    assert result.score == 100


def test_evidenced_alignment_without_ci():
    item = PropertyAlignment(
        property_name="device identity",
        exposure_question="is identity controlled",
        evidence_reference="include/lab_config.example.h",
        ci_validated=False,
        mitigation_evidenced=True,
        property_identified=True,
    )
    result = evaluate_alignment(item)
    assert result.status == "EVIDENCED"
    assert result.score == 85


def test_identified_alignment_with_missing_evidence():
    item = PropertyAlignment(
        property_name="future property",
        exposure_question="is property reviewed",
        evidence_reference="",
        ci_validated=False,
        mitigation_evidenced=False,
        property_identified=True,
    )
    result = evaluate_alignment(item)
    assert result.status == "IDENTIFIED"
    assert result.score == 45


def test_gap_alignment():
    item = PropertyAlignment(
        property_name="unknown",
        exposure_question="",
        evidence_reference="",
        ci_validated=False,
        mitigation_evidenced=False,
        property_identified=False,
    )
    result = evaluate_alignment(item)
    assert result.status == "GAP"
    assert result.score == 0
