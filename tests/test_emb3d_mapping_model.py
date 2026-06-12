from models.emb3d_mapping_model import EmbeddedDeviceProperties, evaluate_emb3d_alignment


def test_low_exposure_alignment():
    properties = EmbeddedDeviceProperties(
        device_id="ESP32-GOV-LAB-0001",
        has_physical_access_risk=False,
        has_network_interface=False,
        has_update_mechanism=False,
        has_persistent_storage=False,
        has_sensor_inputs=False,
        has_event_visibility=True,
        has_inventory_record=True,
        has_recovery_owner=True,
    )
    result = evaluate_emb3d_alignment(properties)
    assert result.exposure_level == "LOW"
    assert result.exposure_score == 0


def test_medium_exposure_alignment():
    properties = EmbeddedDeviceProperties(
        device_id="ESP32-GOV-LAB-0002",
        has_physical_access_risk=True,
        has_network_interface=False,
        has_update_mechanism=False,
        has_persistent_storage=False,
        has_sensor_inputs=True,
        has_event_visibility=True,
        has_inventory_record=True,
        has_recovery_owner=True,
    )
    result = evaluate_emb3d_alignment(properties)
    assert result.exposure_level == "MEDIUM"
    assert result.exposure_score == 30


def test_high_exposure_alignment():
    properties = EmbeddedDeviceProperties(
        device_id="ESP32-GOV-LAB-0003",
        has_physical_access_risk=True,
        has_network_interface=True,
        has_update_mechanism=True,
        has_persistent_storage=True,
        has_sensor_inputs=True,
        has_event_visibility=False,
        has_inventory_record=False,
        has_recovery_owner=False,
    )
    result = evaluate_emb3d_alignment(properties)
    assert result.exposure_level == "HIGH"
    assert result.exposure_score == 105
