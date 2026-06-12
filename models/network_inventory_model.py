#!/usr/bin/env python3
"""Synthetic network point inventory quality model.

The model does not scan networks. It evaluates manually maintained or synthetic
network point records for documentation completeness.
"""

from dataclasses import dataclass
from typing import Literal

InventoryStatus = Literal["DOCUMENTED", "NEEDS_REVIEW", "INCOMPLETE"]


@dataclass(frozen=True)
class NetworkPointRecord:
    point_id: str
    room_label: str
    equipment_label: str
    owner: str
    power_recorded: bool
    cabling_recorded: bool
    documentation_recorded: bool


@dataclass(frozen=True)
class InventoryResult:
    status: InventoryStatus
    score: int
    reason: str


def evaluate_network_point(record: NetworkPointRecord) -> InventoryResult:
    score = 0
    reasons: list[str] = []

    if record.point_id:
        score += 20
    else:
        reasons.append("missing point id")

    if record.room_label:
        score += 20
    else:
        reasons.append("missing room label")

    if record.equipment_label:
        score += 15
    else:
        reasons.append("missing equipment label")

    if record.owner:
        score += 15
    else:
        reasons.append("missing owner")

    if record.power_recorded:
        score += 10
    else:
        reasons.append("power record missing")

    if record.cabling_recorded:
        score += 10
    else:
        reasons.append("cabling record missing")

    if record.documentation_recorded:
        score += 10
    else:
        reasons.append("documentation record missing")

    if score >= 90:
        return InventoryResult("DOCUMENTED", score, "network point record complete")
    if score >= 60:
        return InventoryResult("NEEDS_REVIEW", score, "; ".join(reasons))
    return InventoryResult("INCOMPLETE", score, "; ".join(reasons))


def example() -> None:
    sample = NetworkPointRecord(
        point_id="SYNTH-NP-001",
        room_label="synthetic-room-a",
        equipment_label="synthetic-network-device",
        owner="facility-it",
        power_recorded=True,
        cabling_recorded=True,
        documentation_recorded=True,
    )
    result = evaluate_network_point(sample)
    print(f"point_id={sample.point_id} status={result.status} score={result.score} reason={result.reason}")


if __name__ == "__main__":
    example()
