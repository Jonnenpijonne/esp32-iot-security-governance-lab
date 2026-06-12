# Change Request — ESP32 Wi-Fi Sensor Governance Example

## Basic information

- **Change name:** ESP32 Wi-Fi sensor governance example
- **Requester:** Jonne Silvennoinen
- **Date:** 2026-06-12
- **Risk class:** 2
- **Target environment:** documentation

## Risk justification

Risk Class 2 is selected because this is a documentation and governance example for an ESP32 Wi-Fi sensor scenario. It does not include production firmware, real device credentials, real telemetry or production deployment.

## Description

This change documents how an ESP32-based Wi-Fi sensor should be evaluated from a governance, privacy and security perspective before implementation.

## Impact analysis

The impact is limited to documentation. No firmware, hardware, network configuration or real telemetry pipeline is changed.

## Rollback plan

- **Rollback strategy:** Revert this example file or remove it from the repository.
- **Expected recovery time:** 5 minutes
- **Owner:** Repository owner

## Test plan

- Run `bash scripts/validate-docs.sh`.
- Verify that required documentation files exist.
- Verify that no generated firmware or local secrets are committed.

## Privacy consideration

No real sensor data is included. The example highlights that Wi-Fi and sensor-based events can become privacy-relevant if they reveal presence, movement, routines or environment state.

## Approval

- **Reviewer:** Repository owner
