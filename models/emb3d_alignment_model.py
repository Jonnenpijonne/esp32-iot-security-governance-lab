#!/usr/bin/env python3
"""Lightweight EMB3D alignment model.

This model does not copy the EMB3D dataset. It provides a small public-lab
mapping structure for device properties, exposure questions and evidence.
"""

from dataclasses import dataclass
from typing import Literal

AlignmentStatus = Literal["VALIDATED", "EVIDENCED", "IDENTIFIED", "GAP"]


@dataclass(frozen=True)
class PropertyAlignment:
    property_name: str
    exposure_question: str
    evidence_reference: str
    ci_validated: bool
    mitigation_evidenced: bool
    property_identified: bool


@dataclass(frozen=True)
class AlignmentResult:
    property_name: str
    status: AlignmentStatus
    score: int
    reason: str


def evaluate_alignment(item: PropertyAlignment) -> AlignmentResult:
    score = 0
    reasons: list[str] = []

    if item.property_identified:
        score += 25
    else:
        reasons.append("property not identified")

    if item.exposure_question:
        score += 20
    else:
        reasons.append("exposure question missing")

    if item.evidence_reference:
        score += 20
    else:
        reasons.append("evidence reference missing")

    if item.mitigation_evidenced:
        score += 20
    else:
        reasons.append("mitigation evidence missing")

    if item.ci_validated:
        score += 15
    else:
        reasons.append("ci validation missing")

    if score >= 90 and not reasons:
        return AlignmentResult(item.property_name, "VALIDATED", score, "property alignment validated")
    if score >= 65:
        return AlignmentResult(item.property_name, "EVIDENCED", score, "; ".join(reasons))
    if score >= 25:
        return AlignmentResult(item.property_name, "IDENTIFIED", score, "; ".join(reasons))
    return AlignmentResult(item.property_name, "GAP", score, "; ".join(reasons))


def example() -> None:
    sample = PropertyAlignment(
        property_name="firmware baseline",
        exposure_question="is firmware version known and buildable",
        evidence_reference="platformio.ini, src/main.cpp, firmware workflow",
        ci_validated=True,
        mitigation_evidenced=True,
        property_identified=True,
    )
    result = evaluate_alignment(sample)
    print(f"property={result.property_name} status={result.status} score={result.score} reason={result.reason}")


if __name__ == "__main__":
    example()
