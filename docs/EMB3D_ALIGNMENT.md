# EMB3D Alignment Layer

This document defines how the public ESP32 IoT Security Governance Lab aligns with the MITRE EMB3D embedded-device threat-modeling workflow.

EMB3D is used here as a reference model, not copied into this repository.

## Purpose

The purpose is to connect this lab to a recognized embedded-device threat-modeling structure:

1. Identify device properties.
2. Map properties to relevant threat areas.
3. Evaluate whether each threat area is mitigated, partially mitigated or not applicable.
4. Record evidence.

## Public repository boundary

This repository does not include the full EMB3D dataset.

This repository contains a lightweight mapping layer that can be connected to EMB3D references in a private project or tooling pipeline.

## Current lab properties

| Lab property | Evidence |
| --- | --- |
| Firmware baseline | `src/main.cpp`, `platformio.ini` |
| Device identity | `include/lab_config.example.h` |
| Sensor data | `include/sensor_simulation.h` |
| Data retention | `include/retention_policy.h` |
| Event visibility | `include/audit_events.h` |
| Network point inventory | `models/network_inventory_model.py` |
| Readiness validation | `models/readiness_model.py` |
| Defensive exercise gate | `models/authorized_exercise_gate.py` |
| Protection readiness | `models/blue_team_protection_model.py` |
| Interference observation | `models/interference_observation_model.py` |

## Threat-modeling workflow

For each device property:

1. Describe the property.
2. Determine whether it creates exposure.
3. Identify expected mitigations.
4. Link to evidence.
5. Record residual risk.

## Example alignment

| Device property | Exposure question | Lab mitigation evidence |
| --- | --- | --- |
| Firmware | Is firmware version known and buildable? | PlatformIO build workflow, firmware baseline report |
| Device identity | Is the device identity controlled? | Device identity document and synthetic config header |
| Sensor data | Is sensor data classified? | Sensor data governance and synthetic sensor model |
| Retention | Is data stored? | Data retention boundary and volatile-only state |
| Events | Are events visible? | Event visibility model and serial-only event output |
| Network points | Are physical points documented? | Network inventory model and manual readiness examples |
| Exercise readiness | Is validation authorized and scoped? | Authorized exercise gate model |
| Protection readiness | Are defensive controls evidenced? | Blue team protection model |
| Interference observation | Are anomalies routed to review? | Interference observation model |

## Maturity levels

| Level | Meaning |
| --- | --- |
| 0 | Property not identified |
| 1 | Property identified |
| 2 | Property mapped to exposure question |
| 3 | Mitigation evidence exists |
| 4 | Evidence is validated by tests or CI |
| 5 | Private project annex links evidence to real deployment context |

## Principle

The lab uses EMB3D as an organizing layer for embedded-device assurance. Public content stays synthetic; real project mappings belong in controlled project annexes.
