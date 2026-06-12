# Blast Radius and Rollback Model

This document defines a lightweight blast radius and rollback repeatability model for the public ESP32 IoT Security Governance Lab.

The goal is to add operational control without creating unnecessary process complexity.

## Purpose

Every change should answer four questions:

1. What can this affect?
2. How large is the affected scope?
3. Can the change be reversed repeatably?
4. What evidence proves the change was validated?

## Blast radius levels

| Level | Meaning |
| --- | --- |
| LOW | One device, one area, local-only behavior |
| MEDIUM | Small group of devices or areas, still controlled |
| HIGH | Wider scope or behavior that needs stronger review |

## Repeatable rollback

Rollback is repeatable when:

- Steps are written down.
- Expected previous state is known.
- Validation command is known.
- Evidence location is known.
- The rollback has been tested or rehearsed.

## Acceptance gates

A change should not proceed unless:

- Change id exists.
- Blast radius is understood.
- Rollback steps are defined.
- Rollback has been tested for non-trivial changes.
- Validation has passed.
- Evidence has been recorded.

## Current implementation

The current implementation includes:

- `models/change_control_model.py`
- `tests/test_change_control_model.py`

The model returns:

- `PROCEED`
- `REVIEW`
- `STOP`

## Principle

Keep the model small. The goal is not bureaucracy. The goal is to prevent uncontrolled changes from becoming operational surprises.
