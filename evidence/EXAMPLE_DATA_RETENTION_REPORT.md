# Example Data Retention Evidence Report

This is a synthetic evidence report for the public ESP32 IoT Security Governance Lab.

## Summary

| Field | Value |
| --- | --- |
| Data source | synthetic sensor simulation |
| Retention mode | volatile last reading only |
| Retained samples | maximum 1 runtime sample |
| Persistent storage | disabled |
| Network | disabled |
| Telemetry | disabled |
| Customer data | none |

## Purpose

The purpose of this report is to show how data retention can be documented before real storage or telemetry is introduced.

## Evidence references

- `include/retention_policy.h`
- `include/sensor_simulation.h`
- `src/main.cpp`
- `docs/DATA_RETENTION_BOUNDARY.md`
- `examples/esp32-data-retention-boundary-change.md`

## Expected firmware behavior

At runtime, the firmware periodically prints a local status line containing:

- Device status.
- Synthetic sensor values.
- Retention mode.
- Retained sample count.
- Persistent storage status.

Expected retention status:

```text
retention=volatile_last_reading_only retained_samples=1 persistent_storage=disabled
```

## Security posture

The data retention baseline does not introduce persistent storage, file logging, network transmission or telemetry upload.

## Known limitations

This baseline does not include:

- Storage lifecycle management.
- Deletion process.
- Data integrity checks.
- Access control for stored data.
- Real log review.
- Customer-specific retention policy.

## Review conclusion

The retention baseline is suitable for a public governance lab because it keeps data handling explicit while avoiding real data storage.

Further storage or telemetry work should be handled through governed changes with classification, retention, deletion, access control and rollback review.
