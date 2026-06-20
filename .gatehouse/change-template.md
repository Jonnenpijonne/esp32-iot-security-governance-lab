# Change: <short descriptive title>

## Change type

Documentation / configuration boundary / validation evidence / firmware-impacting change.

## Risk class

Risk Class 2 — controlled documentation or configuration-boundary change.

## Scope

Describe what this change does and which part of the repository it affects.

Keep this section specific. Avoid vague claims such as "security improved" unless the exact improvement is described.

## Security impact

Describe whether this change affects:

- device identity
- configuration boundaries
- network exposure
- logging or telemetry
- data retention
- evidence handling
- security-control interpretation

If there is no security impact, state that explicitly and explain why.

## Device / edge impact

Describe whether this change affects device behavior, firmware behavior, serial output, local configuration, edge-device assumptions or validation commands.

If there is no device or edge impact, state that explicitly.

## Public/private boundary

State the public-safe boundary clearly.

Required boundary statements for this repository:

```text
No real credentials are included.
No customer data is included.
No production deployment is included.
```

Also confirm whether the change avoids:

- real site names
- real network identifiers
- production IP addresses
- classified or restricted information
- real telemetry
- cloud upload behavior
- wireless scanning behavior
- credential testing behavior

## Test plan

List the validation steps.

Examples:

- Documentation review
- Public/private boundary review
- Python model tests
- PlatformIO firmware build
- GitHub Actions validation
- Link check, if applicable

## Rollback plan

Describe how to revert the change if it creates ambiguity, breaks validation or weakens the documented boundary.

Example:

```text
Rollback by reverting this change document and the related documentation update.
No production environment is affected.
```

## Evidence

List the evidence that supports the change.

Examples:

- Updated Markdown documentation
- CI validation output
- Python test output
- PlatformIO build output
- Reviewer confirmation
- Screenshot, only if it does not expose private data

## Non-goals

State what this change intentionally does not do.

Examples:

- Does not add production deployment support
- Does not enable wireless scanning
- Does not add credential testing
- Does not upload telemetry to cloud services
- Does not include customer data
- Does not introduce real environment identifiers
- Does not replace human review
