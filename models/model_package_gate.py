#!/usr/bin/env python3
"""Synthetic model package gate.

This module evaluates whether a proposed model package has the basic governance
records required before it is accepted into the public lab baseline.
"""

from dataclasses import dataclass
from typing import Literal

PackageDecision = Literal["ACCEPT", "REVIEW", "REJECT"]


@dataclass(frozen=True)
class ModelPackageRecord:
    package_id: str
    synthetic_inputs_only: bool
    approval_recorded: bool
    validation_passed: bool
    fallback_defined: bool
    evidence_recorded: bool
    version_incremented: bool


@dataclass(frozen=True)
class ModelPackageResult:
    decision: PackageDecision
    score: int
    reason: str


def evaluate_model_package(record: ModelPackageRecord) -> ModelPackageResult:
    score = 0
    reasons: list[str] = []

    if record.package_id:
        score += 10
    else:
        reasons.append("missing package id")

    if record.synthetic_inputs_only:
        score += 15
    else:
        reasons.append("input boundary requires review")

    if record.approval_recorded:
        score += 20
    else:
        reasons.append("approval not recorded")

    if record.validation_passed:
        score += 20
    else:
        reasons.append("validation not passed")

    if record.fallback_defined:
        score += 15
    else:
        reasons.append("fallback not defined")

    if record.evidence_recorded:
        score += 10
    else:
        reasons.append("evidence not recorded")

    if record.version_incremented:
        score += 10
    else:
        reasons.append("version not incremented")

    if score >= 90:
        return ModelPackageResult("ACCEPT", score, "model package accepted")
    if score >= 60:
        return ModelPackageResult("REVIEW", score, "; ".join(reasons))
    return ModelPackageResult("REJECT", score, "; ".join(reasons))


def example() -> None:
    record = ModelPackageRecord(
        package_id="synthetic-vector-model-v1",
        synthetic_inputs_only=True,
        approval_recorded=True,
        validation_passed=True,
        fallback_defined=True,
        evidence_recorded=True,
        version_incremented=True,
    )
    result = evaluate_model_package(record)
    print(f"package_id={record.package_id} decision={result.decision} score={result.score} reason={result.reason}")


if __name__ == "__main__":
    example()
