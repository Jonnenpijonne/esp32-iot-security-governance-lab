# Interference Observation Model

This document defines a defensive observation model for the public ESP32 IoT Security Governance Lab.

The model evaluates manually recorded signs of degraded device environment.

## Current model

The current implementation includes:

- `models/interference_observation_model.py`
- `tests/test_interference_observation_model.py`

## Observation areas

The model evaluates:

- Repeated disconnects.
- Unstable power observation.
- Unexpected device observation.
- Enclosure state change.
- Temperature outside validation band.
- Manual note availability.

## Output

The model returns:

- `NORMAL`
- `WATCH`
- `ESCALATE`

## Scope boundary

This model does not generate interference, simulate attacks or interact with external systems. It is for defensive observation and escalation readiness.

## Principle

Interference-related observations should be captured as evidence and routed to review before they become operational surprises.
