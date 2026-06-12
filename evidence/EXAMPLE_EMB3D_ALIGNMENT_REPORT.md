# Example EMB3D Alignment Evidence Report

This is a synthetic evidence report for the public ESP32 IoT Security Governance Lab.

## Summary

| Field | Value |
| --- | --- |
| Model | EMB3D alignment pattern |
| Device id | ESP32-GOV-LAB-0001 |
| Mapping type | synthetic device properties |
| Output | LOW, MEDIUM or HIGH lab exposure band |
| Customer data | none |
| Full EMB3D dataset | not included |

## Evidence references

- `docs/EMB3D_ALIGNMENT_MODEL.md`
- `models/emb3d_mapping_model.py`
- `tests/test_emb3d_mapping_model.py`
- `examples/emb3d-device-property-mapping.md`

## Validation commands

```bash
python models/emb3d_mapping_model.py
python -m pytest tests/test_emb3d_mapping_model.py
```

## Expected result

The example model prints a synthetic EMB3D-style property exposure result.

The tests validate low, medium and high exposure bands using synthetic device profiles.

## Review conclusion

The EMB3D alignment layer is suitable for the public lab because it connects device properties, exposure review and mitigation evidence without including real project data or offensive logic.
