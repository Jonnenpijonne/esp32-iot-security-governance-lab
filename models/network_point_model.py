#!/usr/bin/env python3
"""Synthetic network point readiness model.

This model supports manual inventory and readiness scoring for building network
points using synthetic observations. It does not perform network scanning,
packet capture, credential discovery or active probing.
"""

from dataclasses import dataclass
from typing import Literal

PointStatus = Literal["READY", "REVIEW", "UNUSABLE"]


@dataclass(frozen=True)
class NetworkPointObservation:
    point_id: str
    location_label: str
    cable_label_present: bool
    link_light_observed: bool
    expected_device_present: bool
    unknown_device_observed: bool
    physical_damage_observed: bool
    notes: str = "synthetic example"


@dataclass(frozen=True)
class NetworkPointResult:
    point_id: str
    status: PointStatus
    score: int
    reason: str


def evaluate_network_point(observation: NetworkPointObservation) -> NetworkPointResult:
    score = 0
    reasons: list[str] = []

    if observation.cable_label_present:
        score += 20
    else:
        reasons.append("missing cable label")

    if observation.link_light_observed:
        score += 20
    else:
        reasons.append("no link indication")

    if observation.expected_device_present:
        score += 25
    else:
        reasons.append("expected device not observed")

    if not observation.unknown_device_observed:
        score += 20
    else:
        reasons.append("unknown device observed")

    if not observation.physical_damage_observed:
        score += 15
    else:
        reasons.append("physical damage observed")

    if score >= 85 and not reasons:
        status: PointStatus = "READY"
    elif score >= 50:
        status = "REVIEW"
    else:
        status = "UNUSABLE"

    return NetworkPointResult(
        point_id=observation.point_id,
        status=status,
        score=score,
        reason="; ".join(reasons) or "all manual checks passed",
    )


def example() -> None:
    observation = NetworkPointObservation(
        point_id="NP-SYN-001",
        location_label="synthetic-shelter-room-a",
        cable_label_present=True,
        link_light_observed=True,
        expected_device_present=True,
        unknown_device_observed=False,
        physical_damage_observed=False,
    )
    result = evaluate_network_point(observation)
    print(
        f"point_id={result.point_id} status={result.status} "
        f"score={result.score} reason={result.reason}"
    )


if __name__ == "__main__":
    example()
