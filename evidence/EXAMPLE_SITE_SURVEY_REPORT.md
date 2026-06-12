# Example Site Survey Report

This is a synthetic evidence report for the public ESP32 IoT Security Governance Lab.

It does not describe a real building, customer environment or protected location.

## Summary

| Field | Value |
| --- | --- |
| Review id | SYNTH-SITE-001 |
| Site label | synthetic-building |
| Area label | synthetic-technical-area |
| Review owner | facility-it |
| Permission reference | synthetic-approved-review |
| Evidence location | controlled-private-annex |
| Overall status | NEEDS_REVIEW |

## Evidence references

- `docs/AUTHORIZED_SITE_SURVEY_MODEL.md`
- `docs/NETWORK_POINT_RECORD_SCHEMA.md`
- `examples/building-network-point-survey.md`
- `examples/shelter-readiness-assessment.md`
- `models/network_inventory_model.py`
- `models/readiness_model.py`

## Findings

| Item | Status | Notes |
| --- | --- | --- |
| Network point records | NEEDS_REVIEW | Synthetic point record missing cabling detail |
| Device readiness | READY | Synthetic local profile passed |
| Temperature validation | READY | Synthetic input inside validation band |
| Data retention boundary | READY | Volatile last reading only |
| Event visibility | READY | Local serial events only |
| Public/private boundary | READY | Real site details excluded |

## Limitations

- Synthetic report only.
- No real site details.
- No real device identifiers.
- No real network details.
- No automated discovery.
- No customer evidence.

## Review conclusion

The example demonstrates how a site readiness report can combine network point documentation, local device readiness, environmental validation, retention boundaries and event visibility into one evidence package.
