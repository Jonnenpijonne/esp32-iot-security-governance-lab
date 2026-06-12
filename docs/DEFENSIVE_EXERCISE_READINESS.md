# Defensive Exercise Readiness

This document defines a safe public-lab model for defensive validation exercises.

The model is about permission, scope, safety boundary, rollback ownership, evidence location and communication readiness.

## Current model

The current implementation includes:

- `models/authorized_exercise_gate.py`
- `tests/test_authorized_exercise_gate.py`

The model returns:

- `GO`
- `PREPARE`
- `NO_GO`

## Scope

Included:

- Written permission check.
- Scope check.
- Safety boundary check.
- Rollback owner check.
- Evidence location check.
- Communication channel check.
- Live impact expectation check.

Excluded:

- Offensive test logic.
- Exploit logic.
- Active disruption.
- Customer-specific procedure.
- Protected environment details.

## Principle

A validation exercise should not begin before permission, scope, rollback and evidence boundaries are clear.
