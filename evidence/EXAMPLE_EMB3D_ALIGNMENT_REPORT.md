# Example EMB3D Alignment Evidence Report

This is a synthetic evidence report for the public ESP32 IoT Security Governance Lab.

## Summary

| Field | Value |
| --- | --- |
| Framework reference | MITRE EMB3D |
| Local mapping model | `models/emb3d_mapping_model.py` |
| Local property alignment model | `models/emb3d_alignment_model.py` |
| Data source | synthetic public-lab properties |
| Output | exposure band and evidence alignment |
| Customer data | none |
| Full EMB3D dataset | not included |

## Purpose

The purpose is to show how public-lab device properties can be mapped to exposure areas and mitigation evidence.

## Evidence references

- `docs/EMB3D_ALIGNMENT.md`
- `docs/EMB3D_MAPPING_MODEL.md`
- `models/emb3d_mapping_model.py`
- `models/emb3d_alignment_model.py`
- `tests/test_emb3d_mapping_model.py`
- `tests/test_emb3d_alignment_model.py`
- `examples/emb3d-property-alignment-review.md`

## Validation commands

```bash
python models/emb3d_mapping_model.py
python models/emb3d_alignment_model.py
python -m pytest tests/test_emb3d_mapping_model.py tests/test_emb3d_alignment_model.py
```

## Expected result

The example models print synthetic EMB3D-style property exposure and evidence alignment results.

The tests validate exposure bands and evidence-alignment maturity states using synthetic device profiles.

## Review conclusion

The EMB3D alignment layer is suitable for the public lab because it connects device properties, exposure review and mitigation evidence without including real project data or offensive logic.

Real project mappings should be maintained in controlled private annexes.
