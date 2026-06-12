from models.network_point_model import NetworkPointObservation, evaluate_network_point


def test_ready_network_point():
    observation = NetworkPointObservation(
        point_id="NP-SYN-001",
        location_label="synthetic-room-a",
        cable_label_present=True,
        link_light_observed=True,
        expected_device_present=True,
        unknown_device_observed=False,
        physical_damage_observed=False,
    )
    result = evaluate_network_point(observation)
    assert result.status == "READY"
    assert result.score == 100


def test_review_network_point_with_missing_label():
    observation = NetworkPointObservation(
        point_id="NP-SYN-002",
        location_label="synthetic-room-b",
        cable_label_present=False,
        link_light_observed=True,
        expected_device_present=True,
        unknown_device_observed=False,
        physical_damage_observed=False,
    )
    result = evaluate_network_point(observation)
    assert result.status == "REVIEW"
    assert result.score == 80
    assert "missing cable label" in result.reason


def test_unusable_network_point_with_multiple_issues():
    observation = NetworkPointObservation(
        point_id="NP-SYN-003",
        location_label="synthetic-room-c",
        cable_label_present=False,
        link_light_observed=False,
        expected_device_present=False,
        unknown_device_observed=True,
        physical_damage_observed=True,
    )
    result = evaluate_network_point(observation)
    assert result.status == "UNUSABLE"
    assert result.score == 0
