# Example Blast Radius and Rollback Report

This is a synthetic evidence report for the public ESP32 IoT Security Governance Lab.

## Summary

| Field | Value |
| --- | --- |
| Change id | SYNTH-CHANGE-001 |
| Blast radius | LOW |
| Decision | PROCEED |
| Rollback steps | defined |
| Rollback rehearsal | completed in model |
| Validation | expected to pass |
| Evidence | recorded |

## Evidence references

- `models/change_control_model.py`
- `tests/test_change_control_model.py`
- `docs/BLAST_RADIUS_AND_ROLLBACK_MODEL.md`
- `docs/ROLLBACK_REHEARSAL.md`
- `docs/CHANGE_SIZE_GATES.md`

## Validation commands

```bash
python models/change_control_model.py
python -m pytest tests/test_change_control_model.py
```

## Review conclusion

The model adds a lightweight control layer for change size, affected scope, rollback repeatability and evidence readiness.

The model is intentionally small so that it improves governance without adding heavy process complexity.
