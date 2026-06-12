# Example: EMB3D Device Property Mapping

This is a synthetic example for the public ESP32 IoT Security Governance Lab.

## Purpose

Map public-lab device properties to broad embedded-device exposure areas and mitigation evidence.

## Synthetic device profile

| Property | Value |
| --- | --- |
| Device id | ESP32-GOV-LAB-0001 |
| Physical access risk | selected |
| Network interface | not selected in baseline |
| Update mechanism | not selected in baseline |
| Persistent storage | not selected in baseline |
| Sensor inputs | selected as synthetic simulation |
| Event visibility | present |
| Inventory record | present |
| Recovery owner | present |

## Expected model result

```text
level=MEDIUM score=30
```

## Interpretation

The synthetic profile has physical access and sensor-input exposure, but the public baseline keeps network, OTA and persistent storage disabled.

## Evidence references

- `docs/EMB3D_ALIGNMENT_MODEL.md`
- `models/emb3d_mapping_model.py`
- `tests/test_emb3d_mapping_model.py`
- `docs/BLUE_TEAM_PROTECTION_MODEL.md`
- `docs/INTERFERENCE_OBSERVATION_MODEL.md`

## Scope boundary

This example is not a complete EMB3D assessment. It is a public-lab mapping pattern.

Real project mappings should use the official EMB3D model and project-specific controlled evidence.
