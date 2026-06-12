# ESP32 Change Governance Model

## Purpose

This document defines a lightweight change governance model for ESP32 IoT and edge-device work.

The goal is to keep device, firmware, connectivity and telemetry changes documented, reviewable and recoverable.

---

## Change categories

| Category | Example | Typical risk |
| --- | --- | --- |
| Documentation | Update architecture note | Class 1 |
| Configuration | Change local example settings | Class 2 |
| Telemetry | Add new event output | Class 2 or 3 |
| Firmware behavior | Change device logic | Class 2 or 3 |
| Update method | Change update or recovery path | Class 3 |
| Privacy-related feature | Add sensing or activity-related behavior | Class 3 |

---

## Required change-request sections

A meaningful change should document:

- change name
- requester
- date
- risk class
- risk justification
- target environment
- impact analysis
- rollback plan
- test plan
- privacy consideration
- approval record

---

## Risk class guide

| Risk class | Meaning |
| --- | --- |
| Class 1 | Documentation-only or non-functional change |
| Class 2 | Non-production configuration, telemetry or governance change |
| Class 3 | Production firmware, update, recovery, safety or privacy-impacting change |

---

## Approval expectations

| Risk class | Approval expectation |
| --- | --- |
| Class 1 | Self-review acceptable |
| Class 2 | Technical review recommended |
| Class 3 | Explicit owner/security review required |

---

## Evidence expectations

For Class 2 and Class 3 changes, keep evidence of:

- validation result
- rollback plan
- test plan
- reviewer
- known limitations
- decision outcome
