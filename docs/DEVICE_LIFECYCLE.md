# ESP32 Device Lifecycle Model

## Purpose

This document defines a lightweight lifecycle model for ESP32-based IoT / edge devices.

The lifecycle model helps separate experimentation from maintainable operation.

---

## Lifecycle stages

| Stage | Description | Required control |
| --- | --- | --- |
| Concept | Device idea and intended use | scope, privacy purpose, risk notes |
| Prototype | Local test device or breadboard | no real secrets in Git, basic docs |
| Development | Repeatable firmware/config work | versioning, test notes, rollback path |
| Pilot | Limited real-world use | risk review, telemetry review, evidence |
| Active | Operational device | change governance, update records |
| Maintenance | Updates, repairs, reconfiguration | tested changes and recovery plan |
| Retirement | Device removed from use | wipe credentials and revoke access |

---

## Onboarding checklist

Before an ESP32 device is treated as part of an environment, document:

- device purpose
- board / module type
- enabled wireless interfaces
- firmware source
- configuration method
- credential handling
- telemetry purpose
- update method
- rollback method
- owner / maintainer

---

## Maintenance checklist

For each meaningful change:

- create or update a change note
- classify risk
- define rollback
- define test plan
- run validation
- store evidence if useful

---

## Retirement checklist

When a device is retired:

- remove Wi-Fi credentials
- revoke API keys or device tokens
- wipe local storage if used
- remove device from backend inventory
- document retirement date
- archive relevant evidence
