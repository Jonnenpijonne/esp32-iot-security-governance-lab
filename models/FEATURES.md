# Feature Models

This directory includes small Python models for public lab validation.

## Files

- `vectorization_model.py` converts synthetic local values into a numeric feature vector.
- `model_package_gate.py` checks whether a model package record has version, validation, fallback and evidence fields.

## Run

```bash
python models/vectorization_model.py
python models/model_package_gate.py
python -m pytest tests/test_vectorization_model.py tests/test_model_package_gate.py
```

## Boundary

Use synthetic inputs in the public repository.

Real project inputs and project-specific package records belong in controlled private locations.
