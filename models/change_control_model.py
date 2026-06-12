#!/usr/bin/env python3
"""Lightweight change control model for public governance lab.

The model evaluates change size, blast radius, rollback repeatability and
acceptance gate readiness using synthetic or manually maintained records.
"""

from dataclasses import dataclass
from typing import Literal

ChangeDecision = Literal["PROCEED", "REVIEW", "STOP"]
BlastRadius = Literal["LOW", "MEDIUM", "HIGH"]


@dataclass(frozen=True)
class ChangeControlRecord:
    change_id: str
    affected_devices: int
    affected_areas: int
    network_enabled: bool
    telemetry_enabled: bool
    persistent_storage_enabled: bool
    rollback_steps_defined: bool
    rollback_tested: bool
    validation_passed: bool
    evidence_recorded: bool


@dataclass(frozen=True)
class ChangeControlResult:
    decision: ChangeDecision
    blast_radius: BlastRadius
    score: int
    reason: str


def calculate_blast_radius(record: ChangeControlRecord) -> BlastRadius:
    if record.affected_devices <= 1 and record.affected_areas <= 1:
        if not record.network_enabled and not record.telemetry_enabled and not record.persistent_storage_enabled:
            return "LOW"
    if record.affected_devices <= 5 and record.affected_areas <= 2:
        return "MEDIUM"
    return "HIGH"


def evaluate_change_control(record: ChangeControlRecord) -> ChangeControlResult:
    score = 0
    reasons: list[str] = []
    blast_radius = calculate_blast_radius(record)

    if record.change_id:
        score += 10
    else:
        reasons.append("missing change id")

    if blast_radius == "LOW":
        score += 25
    elif blast_radius == "MEDIUM":
        score += 10
        reasons.append("medium blast radius")
    else:
        reasons.append("high blast radius")

    if record.rollback_steps_defined:
        score += 15
    else:
        reasons.append("rollback steps not defined")

    if record.rollback_tested:
        score += 20
    else:
        reasons.append("rollback not tested")

    if record.validation_passed:
        score += 20
    else:
        reasons.append("validation not passed")

    if record.evidence_recorded:
        score += 10
    else:
        reasons.append("evidence not recorded")

    if score >= 90 and blast_radius == "LOW":
        return ChangeControlResult("PROCEED", blast_radius, score, "change ready for controlled execution")
    if score >= 60:
        return ChangeControlResult("REVIEW", blast_radius, score, "; ".join(reasons))
    return ChangeControlResult("STOP", blast_radius, score, "; ".join(reasons))


def example() -> None:
    sample = ChangeControlRecord(
        change_id="SYNTH-CHANGE-001",
        affected_devices=1,
        affected_areas=1,
        network_enabled=False,
        telemetry_enabled=False,
        persistent_storage_enabled=False,
        rollback_steps_defined=True,
        rollback_tested=True,
        validation_passed=True,
        evidence_recorded=True,
    )
    result = evaluate_change_control(sample)
    print(
        f"change_id={sample.change_id} decision={result.decision} "
        f"blast_radius={result.blast_radius} score={result.score} reason={result.reason}"
    )


if __name__ == "__main__":
    example()
