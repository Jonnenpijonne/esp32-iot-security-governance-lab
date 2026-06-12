from models.blue_team_protection_model import ProtectionInput, evaluate_protection


def test_strong_protection_baseline():
    data = ProtectionInput(
        device_id="ESP32-GOV-LAB-0001",
        firmware_known=True,
        config_baseline_known=True,
        event_visibility_enabled=True,
        retention_boundary_known=True,
        manual_inventory_available=True,
        recovery_owner_known=True,
        interference_reported=False,
        unexpected_device_reported=False,
    )
    result = evaluate_protection(data)
    assert result.status == "STRONG"
    assert result.score == 100


def test_partial_protection_baseline():
    data = ProtectionInput(
        device_id="ESP32-GOV-LAB-0002",
        firmware_known=True,
        config_baseline_known=True,
        event_visibility_enabled=False,
        retention_boundary_known=True,
        manual_inventory_available=False,
        recovery_owner_known=True,
        interference_reported=False,
        unexpected_device_reported=False,
    )
    result = evaluate_protection(data)
    assert result.status == "PARTIAL"
    assert result.score == 70


def test_weak_protection_baseline():
    data = ProtectionInput(
        device_id="ESP32-GOV-LAB-0003",
        firmware_known=False,
        config_baseline_known=False,
        event_visibility_enabled=False,
        retention_boundary_known=False,
        manual_inventory_available=False,
        recovery_owner_known=False,
        interference_reported=True,
        unexpected_device_reported=True,
    )
    result = evaluate_protection(data)
    assert result.status == "WEAK"
    assert result.score == 0
