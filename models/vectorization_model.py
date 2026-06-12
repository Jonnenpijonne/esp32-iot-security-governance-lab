#!/usr/bin/env python3
"""Synthetic vectorization model for edge-device governance lab.

This module converts synthetic readiness and sensor values into a small numeric
feature vector. It does not train production models and does not use real data.
"""

from dataclasses import dataclass
from math import sqrt


@dataclass(frozen=True)
class FeatureInput:
    battery_percent: int
    temperature_c: float
    humidity_percent: float
    network_enabled: bool
    telemetry_enabled: bool
    ota_enabled: bool
    persistent_storage_enabled: bool


@dataclass(frozen=True)
class FeatureVector:
    values: tuple[float, ...]
    version: str


def bool_to_float(value: bool) -> float:
    return 1.0 if value else 0.0


def normalize(value: float, minimum: float, maximum: float) -> float:
    if maximum == minimum:
        return 0.0
    clipped = max(minimum, min(maximum, value))
    return (clipped - minimum) / (maximum - minimum)


def vectorize(input_data: FeatureInput) -> FeatureVector:
    values = (
        normalize(input_data.battery_percent, 0, 100),
        normalize(input_data.temperature_c, -20, 60),
        normalize(input_data.humidity_percent, 0, 100),
        bool_to_float(input_data.network_enabled),
        bool_to_float(input_data.telemetry_enabled),
        bool_to_float(input_data.ota_enabled),
        bool_to_float(input_data.persistent_storage_enabled),
    )
    return FeatureVector(values=values, version="feature-vector-v1")


def distance(a: FeatureVector, b: FeatureVector) -> float:
    if len(a.values) != len(b.values):
        raise ValueError("feature vector dimensions must match")
    return sqrt(sum((left - right) ** 2 for left, right in zip(a.values, b.values)))


def example() -> None:
    baseline = vectorize(
        FeatureInput(
            battery_percent=90,
            temperature_c=21.5,
            humidity_percent=45.0,
            network_enabled=False,
            telemetry_enabled=False,
            ota_enabled=False,
            persistent_storage_enabled=False,
        )
    )
    current = vectorize(
        FeatureInput(
            battery_percent=70,
            temperature_c=35.0,
            humidity_percent=55.0,
            network_enabled=False,
            telemetry_enabled=False,
            ota_enabled=False,
            persistent_storage_enabled=False,
        )
    )
    print(f"vector_version={current.version} drift_distance={distance(baseline, current):.4f}")


if __name__ == "__main__":
    example()
