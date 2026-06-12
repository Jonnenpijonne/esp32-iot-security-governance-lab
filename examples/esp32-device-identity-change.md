# Example Change: ESP32 Device Identity Baseline

This is a synthetic example change record for the public governance lab.

It does not describe a customer system, protected environment or production device.

## Change summary

Add a synthetic device identity and configuration profile to the local-only firmware skeleton.

## Purpose

The purpose is to demonstrate how device identity and configuration can be made explicit without adding network, telemetry or OTA behavior.

## Scope

Included:

- `include/lab_config.example.h`
- `src/main.cpp`
- `docs/DEVICE_IDENTITY_AND_CONFIGURATION.md`

Excluded:

- Real device inventory.
- Real customer identifiers.
- Real network configuration.
- Real keys or certificates.
- Telemetry endpoints.
- OTA behavior.

## Risk class

Risk class: Low for public governance lab.

Reason:

The change adds only synthetic example values and serial output. It does not enable network behavior, telemetry, OTA updates or customer-specific configuration.

## Security impact

Positive:

- Device identity is made explicit.
- Configuration posture is visible in firmware output.
- Public/private configuration boundary is documented.

Negative:

- If copied incorrectly into real projects, synthetic patterns could be mistaken for sufficient production identity management.

Mitigation:

- Documentation states that real device inventory and project configuration must be maintained separately.

## Rollback plan

Rollback by reverting:

- `include/lab_config.example.h`
- Related `src/main.cpp` changes.
- `docs/DEVICE_IDENTITY_AND_CONFIGURATION.md`

## Validation

Run:

```bash
bash scripts/validate-docs.sh
pio run
```

## Approval expectation

For a real project, this type of change should be reviewed by the firmware owner and security documentation owner.

## Evidence

Expected evidence:

- Change record.
- Validation output.
- Firmware build result.
- Updated firmware baseline report if needed.
