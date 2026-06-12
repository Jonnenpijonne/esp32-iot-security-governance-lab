from models.network_inventory_model import NetworkPointRecord, evaluate_network_point


def test_documented_inventory_record():
    record = NetworkPointRecord(
        point_id="SYNTH-NP-001",
        room_label="synthetic-room-a",
        equipment_label="synthetic-network-device",
        owner="facility-it",
        power_recorded=True,
        cabling_recorded=True,
        documentation_recorded=True,
    )
    result = evaluate_network_point(record)
    assert result.status == "DOCUMENTED"
    assert result.score == 100


def test_inventory_record_needs_review():
    record = NetworkPointRecord(
        point_id="SYNTH-NP-002",
        room_label="synthetic-room-b",
        equipment_label="synthetic-network-device",
        owner="facility-it",
        power_recorded=False,
        cabling_recorded=True,
        documentation_recorded=True,
    )
    result = evaluate_network_point(record)
    assert result.status == "NEEDS_REVIEW"
    assert result.score == 90
    assert "power record missing" in result.reason


def test_inventory_record_incomplete():
    record = NetworkPointRecord(
        point_id="",
        room_label="",
        equipment_label="",
        owner="",
        power_recorded=False,
        cabling_recorded=False,
        documentation_recorded=False,
    )
    result = evaluate_network_point(record)
    assert result.status == "INCOMPLETE"
    assert result.score == 0
