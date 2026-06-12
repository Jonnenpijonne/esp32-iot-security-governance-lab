# Validation Guide

This guide describes how to validate the repository locally.

## Documentation validation

```bash
bash scripts/validate-docs.sh
```

Expected result:

```text
ESP32 IoT Security Governance Lab validation: PASSED
```

## Python model examples

```bash
python models/readiness_model.py
python models/network_inventory_model.py
python models/network_point_model.py
python models/change_control_model.py
python models/vectorization_model.py
python models/model_package_gate.py
python models/blue_team_protection_model.py
python models/authorized_exercise_gate.py
python models/interference_observation_model.py
python models/emb3d_mapping_model.py
python models/emb3d_alignment_model.py
```

## Python tests

```bash
python -m pytest
```

## Firmware build

```bash
pio run
```

## CI workflows

The repository includes:

- Documentation validation.
- Firmware build.
- Python model tests.
