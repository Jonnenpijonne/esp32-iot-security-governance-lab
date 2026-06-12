# EMB3D Alignment Model

This document defines the public lab alignment layer for the MITRE EMB3D threat model.

EMB3D is used here as a defensive embedded-device threat modeling reference. The public lab maps synthetic device properties to exposure areas and mitigation evidence.

## Purpose

The purpose is to connect the ESP32 / edge-device governance lab to a recognized embedded-device threat modeling structure.

The alignment layer helps answer:

- Which device properties are present?
- Which exposure areas become relevant?
- Which mitigation evidence exists in the repository?
- Which gaps require review before real deployment?

## Current implementation

The current implementation includes:

- `models/emb3d_mapping_model.py`
- `tests/test_emb3d_mapping_model.py`

## Synthetic property mapping

The current model uses public-lab properties:

| Property | Meaning in this lab |
| --- | --- |
| physical access risk | Device may exist in a physical environment where hands-on access is possible |
| network interface | Device has or may later have network capability |
| update mechanism | Device has or may later have update capability |
| persistent storage | Device stores data beyond runtime memory |
| sensor inputs | Device receives sensor-derived data |
| event visibility | Device emits local event information |
| inventory record | Device or network point has a maintained record |
| recovery owner | Responsible recovery owner is known |

## Public baseline interpretation

Current public lab baseline:

- Network disabled.
- OTA disabled.
- Persistent storage disabled.
- Synthetic sensor values only.
- Local event visibility present.
- Inventory/readiness models present.
- Defensive exercise gate present.
- Interference observation model present.

## Output

The model returns:

- `LOW`
- `MEDIUM`
- `HIGH`

These are lab-level exposure bands, not official EMB3D severity values.

## Evidence links inside this repository

Relevant mitigation evidence includes:

- `docs/FIRMWARE_SECURITY_MODEL.md`
- `docs/DEVICE_IDENTITY_AND_CONFIGURATION.md`
- `docs/SENSOR_DATA_GOVERNANCE.md`
- `docs/DATA_RETENTION_BOUNDARY.md`
- `docs/EVENT_VISIBILITY_MODEL.md`
- `docs/NETWORK_POINT_INVENTORY_MODEL.md`
- `docs/BLUE_TEAM_PROTECTION_MODEL.md`
- `docs/DEFENSIVE_EXERCISE_READINESS.md`
- `docs/INTERFERENCE_OBSERVATION_MODEL.md`

## Scope boundary

This alignment layer does not reproduce the full EMB3D dataset. It does not provide offensive testing, exploitation logic or active discovery.

For real projects, the official EMB3D model should be used as the source of truth and project-specific mappings should be maintained in controlled project documentation.

## Principle

Device properties should drive threat exposure review. Mitigation evidence should be explicit before real deployment.
