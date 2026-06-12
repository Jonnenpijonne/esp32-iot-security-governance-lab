# Network Point Inventory Model

This document defines a synthetic network point inventory quality model for the public ESP32 IoT Security Governance Lab.

The model does not scan networks. It evaluates manually maintained or synthetic records for documentation completeness.

## Purpose

The purpose is to support authorized building readiness documentation by checking whether network point records contain enough basic information.

## Current implementation

The current implementation includes:

- `models/network_inventory_model.py`

The model evaluates:

- Point id.
- Room label.
- Equipment label.
- Owner.
- Power record.
- Cabling record.
- Documentation record.

## Output

The model returns:

- `DOCUMENTED`
- `NEEDS_REVIEW`
- `INCOMPLETE`

## Public repository boundary

This public repository uses synthetic examples only.

Real building records, diagrams, room names, customer labels and environment details should be stored in controlled project locations.

## Governance rule

Inventory work should be authorized, documented and limited to the project scope.

## Principle

The model is for documentation quality and readiness evidence, not for discovery against unknown networks.
