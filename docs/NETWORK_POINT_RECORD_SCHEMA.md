# Network Point Record Schema

This document defines a generic schema for documenting network points during authorized readiness work.

The schema is manual and documentation-focused. It does not require automated discovery.

## Required fields

| Field | Purpose |
| --- | --- |
| point_id | Synthetic or project-controlled point identifier |
| area_label | Generic area label |
| room_label | Project-controlled room label |
| equipment_label | Generic equipment label |
| owner | Responsible owner or team |
| power_recorded | Whether power information is documented |
| cabling_recorded | Whether cabling information is documented |
| documentation_recorded | Whether the record is complete enough for review |
| limitations | Known limitations |
| evidence_reference | Controlled evidence location |

## Public example rule

Public examples must use synthetic labels only.

Do not place real building diagrams, room names, network details, device identifiers or customer evidence in this public repository.

## Review statuses

A network point record can be:

- `DOCUMENTED`
- `NEEDS_REVIEW`
- `INCOMPLETE`

## Principle

The goal is documentation quality, not uncontrolled discovery.
