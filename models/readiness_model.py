#!/usr/bin/env python3
"""Generic readiness and temperature validation model.

This model is intentionally domain-neutral. It can be used to demonstrate
edge-device readiness logic for regulated logistics, hospital support,
field devices or other sensitive non-public environments without including
customer-specific or operational details.
"""

from dataclasses import dataclass
from typing import Literal

ReadinessStatus = Literal["READY", "LIMITED", "NOT_READY"]


@dataclass(frozen=True)
class ReadinessInput:
    device_id: str
    battery_percent: int
    temperature_c: float
    humidity_percent: float
    firmware_version: str
    expected_firmware_version: str
    network_enabled: bool
    telemetry_enabled: bool
    ota_enabled: bool
    persistent_storage_enabled: bool


@dataclass(frozen=True)
class ReadinessResult:
    status: ReadinessStatus
    score: int
    reason: str


def evaluate_temperature(temperature_c: float) -> tuple[int, str]:
    if 15.0 <= temperature_c <= 30.0:
        return 25, "temperature within preferred validation band"
    if 5.0 <= temperature_c < 15.0 or 30.0 < temperature_c <= 40.0:
        return 10, "temperature within limited validation band"
    return 0, "temperature outside validation band"


def evaluate_readiness(data: ReadinessInput) -> ReadinessResult:
    score = 0
    reasons: list[str] = []

    if data.battery_percent >= 80:
        score += 20
    elif data.battery_percent >= 50:
        score += 10
        reasons.append("battery below preferred threshold")
    else:
        reasons.append("battery below minimum threshold")

    temperature_score, temperature_reason = evaluate_temperature(data.temperature_c)
    score += temperature_score
    if temperature_score < 25:
        reasons.append(temperature_reason)

    if 20.0 <= data.humidity_percent <= 70.0:
        score += 15
    else:
        reasons.append("humidity outside validation band")

    if data.firmware_version == data.expected_firmware_version:
        score += 20
    else:
        reasons.append("firmware version mismatch")

    if not data.network_enabled:
        score += 5
    else:
        reasons.append("network enabled")

    if not data.telemetry_enabled:
        score += 5
    else:
        reasons.append("telemetry enabled")

    if not data.ota_enabled:
        score += 5
    else:
        reasons.append("ota enabled")

    if not data.persistent_storage_enabled:
        score += 5
    else:
        reasons.append("persistent storage enabled")

    if score >= 85 and not reasons:
        return ReadinessResult("READY", score, "all validation checks passed")
    if score >= 60:
        return ReadinessResult("LIMITED", score, "; ".join(reasons) or "limited readiness")
    return ReadinessResult("NOT_READY", score, "; ".join(reasons) or "readiness checks failed")


def example() -> None:
    sample = ReadinessInput(
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
    result = evaluate_readiness(sample)
    print(f"device_id={sample.device_id} status={result.status} score={result.score} reason={result.reason}")


if __name__ == "__main__":
    example()
