# Change Request — ESP32 OTA Update Governance Example

## Basic information

- **Change name:** ESP32 OTA update governance example
- **Requester:** Jonne Silvennoinen
- **Date:** 2026-06-12
- **Risk class:** 3
- **Target environment:** documentation

## Risk justification

Risk Class 3 is selected because OTA and firmware update mechanisms are high-impact areas for IoT devices. Even though this repository contains only documentation, the example models a change type that would be high-risk in a real device environment.

## Description

This change documents the governance expectations for an ESP32 OTA/update scenario: update source, verification, rollback, local recovery and evidence.

## Impact analysis

The current repository impact is documentation-only. In a real environment, an OTA/update change could affect device availability, recovery, firmware integrity and operational trust.

## Rollback plan

- **Rollback strategy:** Revert this documentation example. In a real device context, reflash previous known-good firmware locally and verify boot/connectivity.
- **Expected recovery time:** 5 minutes for documentation, environment-specific for real devices
- **Owner:** Repository owner

## Test plan

- Run `bash scripts/validate-docs.sh`.
- Verify OTA and rollback documentation exists.
- Verify the example does not include real firmware binaries or local secrets.

## Privacy consideration

No real device data is included. OTA/update evidence should avoid exposing sensitive device identifiers or environment details.

## Approval

- **Reviewer:** Repository owner
