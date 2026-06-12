# Project Index

This index provides a project-level map for the ESP32 / embedded edge-device security governance lab.

## Firmware and device baseline

| Topic | File |
| --- | --- |
| Firmware source | `src/main.cpp` |
| Firmware build config | `platformio.ini` |
| Device configuration example | `include/lab_config.example.h` |
| Sensor simulation | `include/sensor_simulation.h` |
| Retention policy | `include/retention_policy.h` |
| Audit events | `include/audit_events.h` |

## Core governance documents

| Topic | File |
| --- | --- |
| Architecture | `docs/ARCHITECTURE.md` |
| Threat model | `docs/THREAT_MODEL.md` |
| Security baseline | `docs/SECURITY_BASELINE.md` |
| Device lifecycle | `docs/DEVICE_LIFECYCLE.md` |
| OTA and rollback | `docs/OTA_AND_ROLLBACK.md` |
| Privacy and telemetry | `docs/PRIVACY_AND_TELEMETRY.md` |
| Change governance | `docs/CHANGE_GOVERNANCE.md` |
| Evidence model | `docs/EVIDENCE_MODEL.md` |
| Productization model | `docs/PRODUCTIZATION_MODEL.md` |
| Assurance case | `docs/ASSURANCE_CASE.md` |

## Edge-device security layers

| Topic | File |
| --- | --- |
| Firmware security model | `docs/FIRMWARE_SECURITY_MODEL.md` |
| Device identity and configuration | `docs/DEVICE_IDENTITY_AND_CONFIGURATION.md` |
| Sensor data governance | `docs/SENSOR_DATA_GOVERNANCE.md` |
| Data retention boundary | `docs/DATA_RETENTION_BOUNDARY.md` |
| Event visibility | `docs/EVENT_VISIBILITY_MODEL.md` |
| Network point inventory | `docs/NETWORK_POINT_INVENTORY_MODEL.md` |
| Network point readiness | `docs/NETWORK_POINT_READINESS.md` |

## Defensive validation and readiness

| Topic | File |
| --- | --- |
| Defensive exercise readiness | `docs/DEFENSIVE_EXERCISE_READINESS.md` |
| Blue-team protection model | `docs/BLUE_TEAM_PROTECTION_MODEL.md` |
| Interference observation model | `docs/INTERFERENCE_OBSERVATION_MODEL.md` |
| KATAKRI alignment | `docs/KATAKRI_ALIGNMENT.md` |
| Public scope | `docs/PUBLIC_SCOPE.md` |

## EMB3D alignment

| Topic | File |
| --- | --- |
| EMB3D alignment | `docs/EMB3D_ALIGNMENT.md` |
| EMB3D mapping model | `docs/EMB3D_MAPPING_MODEL.md` |
| EMB3D evidence report | `evidence/EXAMPLE_EMB3D_ALIGNMENT_REPORT.md` |

## Python models

| Model | Purpose |
| --- | --- |
| `models/readiness_model.py` | Device readiness scoring |
| `models/network_inventory_model.py` | Network point inventory quality |
| `models/network_point_model.py` | Manual network point readiness review |
| `models/change_control_model.py` | Change control / rollback decision support |
| `models/vectorization_model.py` | Evidence vectorization readiness |
| `models/model_package_gate.py` | Model package release gate |
| `models/blue_team_protection_model.py` | Defensive protection scoring |
| `models/authorized_exercise_gate.py` | Authorized exercise gate |
| `models/interference_observation_model.py` | Interference observation escalation |
| `models/emb3d_mapping_model.py` | EMB3D-style exposure mapping |
| `models/emb3d_alignment_model.py` | EMB3D-style evidence alignment |

## CI workflows

| Workflow | Purpose |
| --- | --- |
| `.github/workflows/validation.yml` | Required file validation |
| `.github/workflows/firmware-build.yml` | PlatformIO firmware build |
| `.github/workflows/python-model-tests.yml` | Python model examples and pytest |

## Start here

Recommended reading order:

1. `README.md`
2. `docs/GETTING_STARTED.md`
3. `docs/PROJECT_INDEX.md`
4. `docs/PUBLIC_SCOPE.md`
5. `docs/EMB3D_ALIGNMENT.md`
6. `docs/KATAKRI_ALIGNMENT.md`
7. `evidence/EXAMPLE_EMB3D_ALIGNMENT_REPORT.md`
