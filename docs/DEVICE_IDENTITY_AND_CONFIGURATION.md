# Device Identity and Configuration Governance

This document defines the public lab model for device identity and configuration governance.

The repository uses synthetic example values only. Real project identifiers, customer labels, network details, keys and environment-specific configuration must be stored outside this public repository.

## Purpose

Device identity and configuration must be controlled because they connect firmware behavior to lifecycle, inventory, ownership, evidence and incident response.

For this public lab, the goal is to demonstrate the governance structure without exposing real project details.

## Current implementation

The current firmware skeleton includes an example configuration header:

- `include/lab_config.example.h`

The example configuration defines:

- Synthetic device id.
- Synthetic configuration profile.
- Synthetic site label.
- Network disabled flag.
- Telemetry disabled flag.
- OTA disabled flag.

The firmware prints these values to the serial console during boot and status output.

## Public repository rule

The public repository may contain only synthetic configuration values.

Do not commit:

- Real device inventory.
- Real customer labels.
- Real site names.
- Real network details.
- Real credentials.
- Real keys or certificates.
- Real operational endpoints.
- Real deployment configuration.

## Private configuration model

A real project should maintain private configuration records separately.

Private records may include:

- Device inventory.
- Device owner.
- Device purpose.
- Approved firmware version.
- Approved configuration profile.
- Network zone.
- Telemetry policy.
- Update authority.
- Rollback owner.
- Evidence location.

## Configuration change control

Configuration changes should be treated as governed changes when they affect:

- Device identity.
- Network behavior.
- Telemetry behavior.
- Update behavior.
- Logging behavior.
- Access control.
- Data handling.
- Operational environment assumptions.

## Minimum change evidence

A configuration change record should include:

- Change purpose.
- Device or profile affected.
- Security impact.
- Telemetry impact.
- Rollback plan.
- Validation result.
- Approval record.

## Baseline status

Current public baseline:

| Item | Status |
| --- | --- |
| Device id | synthetic example only |
| Configuration profile | synthetic local-only baseline |
| Network | disabled |
| Telemetry | disabled |
| OTA | disabled |
| Customer-specific configuration | not present |

## Principle

Device identity and configuration are part of security governance. They should be explicit, reviewed and evidenced before real deployments.
