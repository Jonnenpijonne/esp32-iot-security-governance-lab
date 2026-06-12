# Example Review: Network Point Readiness

This is a synthetic example review for the public governance lab.

## Summary

Review a synthetic building network point using manual observations.

## Observation

| Field | Value |
| --- | --- |
| Point id | NP-SYN-001 |
| Location label | synthetic-shelter-room-a |
| Cable label present | yes |
| Link light observed | yes |
| Expected device present | yes |
| Unknown device observed | no |
| Physical damage observed | no |

## Result

Expected model result:

```text
status=READY score=100
```

## Scope boundary

This example does not include real building data, real port labels, real network addresses or real device inventory.

## Validation

Run:

```bash
python models/network_point_model.py
python -m pytest tests/test_network_point_model.py
```
