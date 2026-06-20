# Change: Public-safe edge-device configuration boundary clarification

## Change type

Documentation / configuration boundary.

## Risk class

Risk Class 2 — controlled documentation and configuration-boundary change.

## Scope

This example change clarifies the documented boundary between public-safe edge-device configuration examples and private or customer-specific configuration values.

It is intended to demonstrate how an embedded / edge-device governance change can be reviewed before entering the normal technical CI/CD validation path.

## Security impact

This change affects documentation only.

It does not add wireless scanning, placeholder-based authentication boundary validation, cloud upload, synthetic sample data handling, production network mapping or external communication behavior.

The security impact is limited to making the public/private evidence boundary clearer and easier to review.

## Device / edge impact

This change does not modify firmware behavior, serial output, device identity, local configuration parsing or build behavior.

No ESP32 runtime behavior is changed.

## Public/private boundary

No real credentials are included.
No live authentication material is included.
No customer data is included.
No production deployment is included.

This change does not include:

- real site names
- real network identifiers
- production IP addresses
- restricted or non-public information
- synthetic sample data streams
- cloud upload behavior
- wireless scanning behavior
- placeholder-based authentication boundary validation behavior

## Test plan

- Review this change document for required Gatehouse sections.
- Run the embedded Gatehouse validation workflow.
- Confirm that no existing firmware, build, test or documentation workflow is modified.
- Confirm that no private values or production claims are introduced.

## Rollback plan

Rollback by reverting this example change document and the related Gatehouse scaffold if the boundary model becomes unclear or too heavy for the repository.

No production environment is affected.

## Evidence

- New `.gatehouse/embedded-security-profile.yml`
- New `.gatehouse/change-template.md`
- New `tools/gatehouse_embedded_check.py`
- New `.github/workflows/gatehouse-embedded-quality-gate.yml`
- This example change document

## Non-goals

This change does not:

- add production deployment support
- enable wireless scanning
- add placeholder-based authentication boundary validation
- upload sample data to cloud services
- include customer data
- introduce real environment identifiers
- modify firmware source code
- modify existing CI/CD workflows
- replace human review
