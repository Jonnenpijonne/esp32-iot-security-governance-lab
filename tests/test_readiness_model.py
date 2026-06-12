from models.readiness_model import ReadinessInput, evaluate_readiness, evaluate_temperature


def test_temperature_preferred_band():
    score, reason = evaluate_temperature(21.5)
    assert score == 25
    assert "preferred" in reason


def test_temperature_limited_band():
    score, reason = evaluate_temperature(35.0)
    assert score == 10
    assert "limited" in reason


def test_temperature_outside_band():
    score, reason = evaluate_temperature(-10.0)
    assert score == 0
    assert "outside" in reason


def test_ready_baseline():
    data = ReadinessInput(
        device_id="ESP32-GOV-LAB-0001",
        battery_percent=92,
        temperature_c=21.5,
        humidity_percent=45.0,
        firmware_version="0.1.0",
        expected_firmware_version="0.1.0",
        network_enabled=False,
        telemetry_enabled=False,
        ota_enabled=False,
        persistent_storage_enabled=False,
    )
    result = evaluate_readiness(data)
    assert result.status == "READY"
    assert result.score == 100


def test_limited_when_temperature_is_not_preferred():
    data = ReadinessInput(
        device_id="ESP32-GOV-LAB-0001",
        battery_percent=90,
        temperature_c=35.0,
        humidity_percent=45.0,
        firmware_version="0.1.0",
        expected_firmware_version="0.1.0",
        network_enabled=False,
        telemetry_enabled=False,
        ota_enabled=False,
        persistent_storage_enabled=False,
    )
    result = evaluate_readiness(data)
    assert result.status == "LIMITED"
    assert result.score == 85


def test_not_ready_when_environment_is_outside_validation_band():
    data = ReadinessInput(
        device_id="ESP32-GOV-LAB-0001",
        battery_percent=20,
        temperature_c=-10.0,
        humidity_percent=95.0,
        firmware_version="0.1.0",
        expected_firmware_version="0.2.0",
        network_enabled=False,
        telemetry_enabled=False,
        ota_enabled=False,
        persistent_storage_enabled=False,
    )
    result = evaluate_readiness(data)
    assert result.status == "NOT_READY"
    assert result.score == 20
