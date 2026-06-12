# EMB3D Mapping Model

This document defines the public-lab EMB3D mapping layer.

The repository does not copy the MITRE EMB3D dataset. It uses a lightweight local model that maps public-lab device properties to broad exposure areas and mitigation evidence.

## Purpose

The purpose is to make embedded-device assurance traceable:

- identify device properties
- describe exposure areas
- link mitigation evidence
- validate the model with tests
- keep real project mappings in controlled private annexes

## Current implementation

The current implementation includes:

- `models/emb3d_mapping_model.py`
- `tests/test_emb3d_mapping_model.py`
- `docs/EMB3D_ALIGNMENT.md`
- `examples/emb3d-property-alignment-review.md`

## Public lab properties

The model currently evaluates whether the public lab profile includes:

- physical access risk
- network interface
- update mechanism
- persistent storage
- sensor inputs
- event visibility
- inventory record
- recovery owner

## Output

The model returns:

- `LOW`
- `MEDIUM`
- `HIGH`

These values describe synthetic exposure level for the lab profile. They are not a certification result.

## Boundary

This model is for defensive documentation, assurance and acquisition-readiness discussion.

It does not perform scanning, exploitation, active probing or device interaction.

## Validation

Run:

```bash
python models/emb3d_mapping_model.py
python -m pytest tests/test_emb3d_mapping_model.py
```

## Principle

EMB3D alignment should make embedded-device properties, exposure questions and evidence visible before a real project depends on the device.
