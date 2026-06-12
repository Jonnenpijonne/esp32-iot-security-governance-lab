#!/usr/bin/env python3
"""Authorized exercise gate model.

This model checks whether a defensive validation exercise has the required
boundaries before it begins. It does not include active test logic.
"""

from dataclasses import dataclass
from typing import Literal

GateStatus = Literal["GO", "PREPARE", "NO_GO"]


@dataclass(frozen=True)
class ExerciseGateInput:
    exercise_id: str
    written_permission: bool
    scope_defined: bool
    safety_boundary_defined: bool
    rollback_owner_defined: bool
    evidence_location_defined: bool
    communication_channel_defined: bool
    live_impact_expected: bool


@dataclass(frozen=True)
class ExerciseGateResult:
    status: GateStatus
    score: int
    reason: str


def evaluate_exercise_gate(data: ExerciseGateInput) -> ExerciseGateResult:
    score = 0
    reasons: list[str] = []

    if data.written_permission:
        score += 20
    else:
        reasons.append("written permission missing")

    if data.scope_defined:
        score += 20
    else:
        reasons.append("scope missing")

    if data.safety_boundary_defined:
        score += 15
    else:
        reasons.append("safety boundary missing")

    if data.rollback_owner_defined:
        score += 15
    else:
        reasons.append("rollback owner missing")

    if data.evidence_location_defined:
        score += 10
    else:
        reasons.append("evidence location missing")

    if data.communication_channel_defined:
        score += 10
    else:
        reasons.append("communication channel missing")

    if not data.live_impact_expected:
        score += 10
    else:
        reasons.append("live impact expected")

    if score >= 90 and not reasons:
        return ExerciseGateResult("GO", score, "exercise gate complete")
    if score >= 60:
        return ExerciseGateResult("PREPARE", score, "; ".join(reasons))
    return ExerciseGateResult("NO_GO", score, "; ".join(reasons))


def example() -> None:
    sample = ExerciseGateInput(
        exercise_id="SYNTH-EX-001",
        written_permission=True,
        scope_defined=True,
        safety_boundary_defined=True,
        rollback_owner_defined=True,
        evidence_location_defined=True,
        communication_channel_defined=True,
        live_impact_expected=False,
    )
    result = evaluate_exercise_gate(sample)
    print(f"exercise_id={sample.exercise_id} status={result.status} score={result.score} reason={result.reason}")


if __name__ == "__main__":
    example()
