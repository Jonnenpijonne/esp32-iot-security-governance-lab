# Blue Team Protection Model

This document defines a defensive protection readiness model for the public ESP32 IoT Security Governance Lab.

## Current model

The current implementation includes:

- `models/blue_team_protection_model.py`
- `tests/test_blue_team_protection_model.py`

The model evaluates whether a device or environment has enough defensive evidence available.

## Evaluation areas

The model checks:

- Firmware baseline known.
- Configuration baseline known.
- Event visibility enabled.
- Retention boundary known.
- Manual inventory available.
- Recovery owner known.
- Interference review needed.
- Unexpected device review needed.

## Output

The model returns:

- `STRONG`
- `PARTIAL`
- `WEAK`

## Scope boundary

This model does not perform scanning, exploitation or disruption. It evaluates defensive evidence completeness from synthetic or manually maintained inputs.

## Principle

Protection readiness should be measurable before incidents, anomalies or operational pressure appear.
