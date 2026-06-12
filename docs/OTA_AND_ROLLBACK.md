# OTA and Rollback Model

## Purpose

Firmware updates are one of the highest-risk areas in IoT and edge-device operations.

This document defines a lightweight governance model for OTA/update and rollback thinking in ESP32 projects.

---

## Why OTA is high risk

OTA or firmware update logic can affect:

- device availability
- device trust boundary
- remote code execution path
- credential handling
- recovery options
- field maintenance cost
- safety and physical-world behavior

For this reason, OTA/update changes should normally be treated as Risk Class 3 unless they are clearly documentation-only or non-production examples.

---

## Minimum OTA questions

Before adding or changing OTA behavior, answer:

1. Who can trigger an update?
2. Where does the update package come from?
3. How is the package verified?
4. What happens if power fails during update?
5. What happens if the new firmware does not boot?
6. How can the device be restored locally?
7. Are credentials preserved, rotated or wiped?
8. What evidence proves the update was tested?

---

## Rollback model

A rollback plan should include:

- previous known-good firmware version
- local reflash method
- configuration backup or reset method
- expected recovery time
- owner responsible for recovery
- validation after rollback

---

## Example rollback statement

```text
Rollback strategy: Reflash the previous known-good firmware image through USB serial, restore example-safe configuration and rerun local connectivity validation. No production credentials are stored in the repository.
```

---

## Evidence expectations

For OTA/update changes, store evidence of:

- firmware version before change
- firmware version after change
- test device used
- validation result
- rollback result or rollback rehearsal
- reviewer / approver

Generated firmware binaries should not be committed by default.
