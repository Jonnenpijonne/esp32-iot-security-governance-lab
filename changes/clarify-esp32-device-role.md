# Change: Clarify ESP32 device role

## Change type

Documentation change.

## Risk class

Risk Class 2 — controlled documentation or configuration-boundary change.

## Scope

Adds a public-safe documentation note explaining the role of ESP32 in this lab as a representative embedded / edge device.

The change affects only documentation and does not alter firmware, models, tests, workflows, configuration files or validation logic.

## Security impact

This change has no runtime security impact.

It clarifies the security-control interpretation of the lab by stating that ESP32 is used as a representative embedded / edge device, not as a production-ready device or real deployment scenario.

## Device / edge impact

This change has no device or edge runtime impact.

It does not change firmware behavior, serial output, local configuration, device identity, validation commands or edge-device assumptions.

## Public/private boundary

No real credentials are included.
No customer data is included.
No production deployment is included.

The change does not include real site names, real network identifiers, production IP addresses, restricted information, telemetry upload behavior, wireless scanning behavior or credential testing behavior.

## Test plan

- Documentation review
- Public/private boundary review
- GitHub Actions validation
- Gatehouse embedded quality gate

## Rollback plan

Rollback by reverting the device-role documentation note and this change record.

No production environment is affected.

## Evidence

- Added public-safe device-role documentation
- Added this Gatehouse change record
- PR validation checks

## Non-goals

- Does not add production deployment support
- Does not change firmware behavior
- Does not change Python model logic
- Does not change CI workflow logic
- Does not enable wireless scanning
- Does not add credential testing
- Does not upload telemetry to cloud services
- Does not include customer data
- Does not introduce real environment identifiers
- Does not replace human review
