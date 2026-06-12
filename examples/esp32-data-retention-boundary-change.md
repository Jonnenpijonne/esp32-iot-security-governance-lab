# Example Change: ESP32 Data Retention Boundary

This is a synthetic example change record for the public governance lab.

It does not describe a customer system, protected environment or production device.

## Change summary

Add an explicit local data retention boundary to the firmware skeleton.

## Purpose

The purpose is to show that sensor readings are handled as runtime-only values unless a reviewed change introduces storage or transmission.

## Scope

Included:

- `include/retention_policy.h`
- `src/main.cpp`
- `docs/DATA_RETENTION_BOUNDARY.md`

Excluded:

- Persistent storage.
- File logging.
- SD card logging.
- Network transmission.
- Telemetry upload.
- Real sensor data.
- Customer-specific data.

## Risk class

Risk class: Low for public governance lab.

Reason:

The change stores only the latest synthetic reading in volatile runtime memory. It does not write to persistent storage or transmit data.

## Security impact

Positive:

- Data retention boundary is explicit.
- Runtime state is visible in serial output.
- Persistent storage remains disabled.

Negative:

- Future real persistence work could be underestimated if not reviewed separately.

Mitigation:

- Documentation states that any storage, aggregation or transmission must be handled as a governed change.

## Rollback plan

Rollback by reverting:

- `include/retention_policy.h`
- Related `src/main.cpp` changes.
- `docs/DATA_RETENTION_BOUNDARY.md`

## Validation

Run:

```bash
bash scripts/validate-docs.sh
pio run
```

## Approval expectation

For a real project, this type of change should be reviewed by the firmware owner, data owner and security documentation owner.

## Evidence

Expected evidence:

- Change record.
- Validation output.
- Firmware build result.
- Data retention boundary document.
- Updated baseline report if needed.
