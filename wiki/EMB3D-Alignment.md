# EMB3D Alignment

This repository uses MITRE EMB3D as an external reference model for embedded-device threat-modeling alignment.

The repository does not copy or redistribute the EMB3D dataset.

## Local alignment pattern

The project uses this pattern:

```text
device property
→ exposure question
→ mitigation evidence
→ validation status
→ private annex if needed
```

## Local files

| Purpose | File |
| --- | --- |
| Alignment documentation | `docs/EMB3D_ALIGNMENT.md` |
| Mapping documentation | `docs/EMB3D_MAPPING_MODEL.md` |
| Exposure mapping model | `models/emb3d_mapping_model.py` |
| Evidence alignment model | `models/emb3d_alignment_model.py` |
| Tests | `tests/test_emb3d_mapping_model.py`, `tests/test_emb3d_alignment_model.py` |
| Evidence | `evidence/EXAMPLE_EMB3D_ALIGNMENT_REPORT.md` |

## Use

Use this layer to show how embedded-device properties can be turned into evidence-backed threat-modeling discussion.

## Boundary

Real EMB3D mappings for a customer or protected project belong in a controlled private annex.
