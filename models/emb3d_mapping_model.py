#!/usr/bin/env python3
"""Synthetic EMB3D alignment model.

This model maps public lab device properties to broad embedded-device threat
exposure areas and mitigation evidence. It is a defensive documentation model,
not a vulnerability scanner.
"""

from dataclasses import dataclass
from typing import Literal

ExposureLevel = Literal["LOW", "MEDIUM", "HIGH"]


@dataclass(frozen=True)
class EmbeddedDeviceProperties:
    device_id: str
    has_physical_access_risk: bool
    has_network_interface: bool
    has_update_mechanism: bool
    has_persistent_storage: bool
    has_sensor_inputs: bool
    has_event_visibility: bool
    has_inventory_record: bool
    has_recovery_owner: bool


@dataclass(frozen=True)
class Emb3dAlignmentResult:
    device_id: str
    exposure_level: ExposureLevel
    exposure_score: int
    property_summary: str
    mitigation_summary: str


def evaluate_emb3d_alignment(properties: EmbeddedDeviceProperties) -> Emb3dAlignmentResult:
    exposure_score = 0
    exposures: list[str] = []
    mitigations: list[str] = []

    if properties.has_physical_access_risk:
        exposure_score += 20
        exposures.append("physical access")
    else:
        mitigations.append("physical access risk not selected")

    if properties.has_network_interface:
        exposure_score += 25
        exposures.append("network interface")
    else:
        mitigations.append("network disabled in baseline")

    if properties.has_update_mechanism:
        exposure_score += 20
        exposures.append("update mechanism")
    else:
        mitigations.append("update mechanism disabled in baseline")

    if properties.has_persistent_storage:
        exposure_score += 15
        exposures.append("persistent storage")
    else:
        mitigations.append("persistent storage disabled in baseline")

    if properties.has_sensor_inputs:
        exposure_score += 10
        exposures.append("sensor input")
    else:
        mitigations.append("real sensor input not enabled")

    if properties.has_event_visibility:
        mitigations.append("local event visibility present")
    else:
        exposure_score += 5
        exposures.append("missing event visibility")

    if properties.has_inventory_record:
        mitigations.append("inventory record present")
    else:
        exposure_score += 5
        exposures.append("inventory record missing")

    if properties.has_recovery_owner:
        mitigations.append("recovery owner known")
    else:
        exposure_score += 5
        exposures.append("recovery owner missing")

    if exposure_score >= 60:
        level: ExposureLevel = "HIGH"
    elif exposure_score >= 25:
        level = "MEDIUM"
    else:
        level = "LOW"

    return Emb3dAlignmentResult(
        device_id=properties.device_id,
        exposure_level=level,
        exposure_score=exposure_score,
        property_summary=", ".join(exposures) or "minimal selected exposure properties",
        mitigation_summary="; ".join(mitigations) or "no mitigation evidence selected",
    )


def example() -> None:
    sample = EmbeddedDeviceProperties(
        device_id="ESP32-GOV-LAB-0001",
        has_physical_access_risk=True,
        has_network_interface=False,
        has_update_mechanism=False,
        has_persistent_storage=False,
        has_sensor_inputs=True,
        has_event_visibility=True,
        has_inventory_record=True,
        has_recovery_owner=True,
    )
    result = evaluate_emb3d_alignment(sample)
    print(
        f"device_id={result.device_id} level={result.exposure_level} "
        f"score={result.exposure_score} properties={result.property_summary} "
        f"mitigations={result.mitigation_summary}"
    )


if __name__ == "__main__":
    example()
