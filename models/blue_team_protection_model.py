#!/usr/bin/env python3
"""Blue-team protection readiness model.

This model evaluates defensive readiness using synthetic control evidence.
It does not perform offensive testing, exploitation, scanning or disruption.
"""

from dataclasses import dataclass
from typing import Literal

ProtectionStatus = Literal["STRONG", "PARTIAL", "WEAK"]


@dataclass(frozen=True)
class ProtectionInput:
    device_id: str
    firmware_known: bool
    config_baseline_known: bool
    event_visibility_enabled: bool
    retention_boundary_known: bool
    manual_inventory_available: bool
    recovery_owner_known: bool
    interference_reported: bool
    unexpected_device_reported: bool


@dataclass(frozen=True)
class ProtectionResult:
    status: ProtectionStatus
    score: int
    reason: str


def evaluate_protection(data: ProtectionInput) -> ProtectionResult:
    score = 0
    reasons: list[str] = []

    if data.firmware_known:
        score += 15
    else:
        reasons.append("firmware baseline missing")

    if data.config_baseline_known:
        score += 15
    else:
        reasons.append("configuration baseline missing")

    if data.event_visibility_enabled:
        score += 15
    else:
        reasons.append("event visibility missing")

    if data.retention_boundary_known:
        score += 15
    else:
        reasons.append("retention boundary missing")

    if data.manual_inventory_available:
        score += 15
    else:
        reasons.append("manual inventory missing")

    if data.recovery_owner_known:
        score += 15
    else:
        reasons.append("recovery owner missing")

    if not data.interference_reported:
        score += 5
    else:
        reasons.append("interference review needed")

    if not data.unexpected_device_reported:
        score += 5
    else:
        reasons.append("unexpected device review needed")

    if score >= 90 and not reasons:
        return ProtectionResult("STRONG", score, "defensive readiness evidence complete")
    if score >= 60:
        return ProtectionResult("PARTIAL", score, "; ".join(reasons))
    return ProtectionResult("WEAK", score, "; ".join(reasons))


def example() -> None:
    sample = ProtectionInput(
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
    result = evaluate_protection(sample)
    print(f"device_id={sample.device_id} status={result.status} score={result.score} reason={result.reason}")


if __name__ == "__main__":
    example()
