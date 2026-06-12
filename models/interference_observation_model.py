#!/usr/bin/env python3
"""Interference observation model.

This model evaluates manually recorded signs of degraded device environment.
It is defensive and evidence-oriented. It does not generate or simulate interference.
"""

from dataclasses import dataclass
from typing import Literal

InterferenceStatus = Literal["NORMAL", "WATCH", "ESCALATE"]


@dataclass(frozen=True)
class InterferenceObservation:
    observation_id: str
    repeated_disconnects: bool
    unstable_power_observed: bool
    unexpected_device_seen: bool
    enclosure_opened: bool
    temperature_outside_band: bool
    manual_note_present: bool


@dataclass(frozen=True)
class InterferenceResult:
    status: InterferenceStatus
    score: int
    reason: str


def evaluate_interference(observation: InterferenceObservation) -> InterferenceResult:
    risk = 0
    reasons: list[str] = []

    if observation.repeated_disconnects:
        risk += 20
        reasons.append("repeated disconnects observed")

    if observation.unstable_power_observed:
        risk += 20
        reasons.append("unstable power observed")

    if observation.unexpected_device_seen:
        risk += 20
        reasons.append("unexpected device observed")

    if observation.enclosure_opened:
        risk += 20
        reasons.append("enclosure state changed")

    if observation.temperature_outside_band:
        risk += 15
        reasons.append("temperature outside band")

    if not observation.manual_note_present:
        risk += 5
        reasons.append("manual note missing")

    if risk >= 50:
        return InterferenceResult("ESCALATE", risk, "; ".join(reasons))
    if risk >= 20:
        return InterferenceResult("WATCH", risk, "; ".join(reasons))
    return InterferenceResult("NORMAL", risk, "no elevated observation")


def example() -> None:
    sample = InterferenceObservation(
        observation_id="SYNTH-OBS-001",
        repeated_disconnects=False,
        unstable_power_observed=False,
        unexpected_device_seen=False,
        enclosure_opened=False,
        temperature_outside_band=False,
        manual_note_present=True,
    )
    result = evaluate_interference(sample)
    print(f"observation_id={sample.observation_id} status={result.status} risk={result.score} reason={result.reason}")


if __name__ == "__main__":
    example()
