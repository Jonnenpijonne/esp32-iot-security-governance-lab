# Example Review: EMB3D Property Alignment

This is a synthetic example review for the public ESP32 IoT Security Governance Lab.

## Summary

Map a public-lab device property to an exposure question and evidence reference.

## Property

| Field | Value |
| --- | --- |
| Property | firmware baseline |
| Exposure question | is firmware version known and buildable |
| Evidence | `platformio.ini`, `src/main.cpp`, firmware workflow |
| Mitigation evidence | yes |
| CI validation | yes |

## Expected result

```text
status=VALIDATED score=100
```

## Scope boundary

This example does not copy the EMB3D dataset. It only demonstrates how a local lab property can be aligned to a threat-modeling workflow.

## Validation

Run:

```bash
python models/emb3d_alignment_model.py
python -m pytest tests/test_emb3d_alignment_model.py
```
