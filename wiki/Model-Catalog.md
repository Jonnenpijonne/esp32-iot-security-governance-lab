# Model Catalog

This page lists the Python models in the repository.

## Readiness and inventory

| Model | Purpose |
| --- | --- |
| `readiness_model.py` | Device readiness scoring |
| `network_inventory_model.py` | Network point documentation quality |
| `network_point_model.py` | Manual network point readiness review |

## Change and release gates

| Model | Purpose |
| --- | --- |
| `change_control_model.py` | Change control decision support |
| `vectorization_model.py` | Evidence vectorization readiness |
| `model_package_gate.py` | Model package release gate |

## Defensive validation

| Model | Purpose |
| --- | --- |
| `blue_team_protection_model.py` | Defensive protection scoring |
| `authorized_exercise_gate.py` | Validation exercise gate |
| `interference_observation_model.py` | Observation escalation model |

## EMB3D alignment

| Model | Purpose |
| --- | --- |
| `emb3d_mapping_model.py` | Embedded-device exposure mapping |
| `emb3d_alignment_model.py` | Property-to-evidence alignment maturity |

## Run all models

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
