# Data Retention Boundary

This document defines the data retention boundary for the public ESP32 IoT Security Governance Lab.

The current firmware uses synthetic local sensor values only. It keeps only the latest reading in volatile runtime memory and does not write readings to persistent storage.

## Purpose

Data retention must be explicit because stored sensor data can become operationally sensitive in real projects.

This public lab demonstrates a minimal retention model before any real data storage, telemetry or customer-specific processing is introduced.

## Current retention model

Current baseline:

| Item | Status |
| --- | --- |
| Sensor data source | synthetic simulation |
| Retention mode | volatile last reading only |
| Persistent storage | disabled |
| File logging | disabled |
| Network transmission | disabled |
| Telemetry upload | disabled |
| Customer data | none |

## Firmware implementation

The current firmware includes:

- `include/retention_policy.h`
- `include/sensor_simulation.h`
- `src/main.cpp`

The firmware updates a local runtime state with the latest synthetic reading. The state is not written to flash, filesystem, SD card or network destination.

## Governance rule

Any change that stores, transmits or aggregates sensor data must be treated as a governed change.

This includes:

- Writing to flash.
- Writing to filesystem.
- Writing to SD card.
- Increasing retained sample count.
- Adding event history.
- Adding telemetry upload.
- Adding network transport.
- Adding customer-specific labels.
- Adding real sensor data.

## Minimum evidence for persistence

Before persistent storage is added, document:

- Purpose of storage.
- Data classification.
- Retention period.
- Deletion behavior.
- Storage location.
- Access control model.
- Integrity expectations.
- Confidentiality expectations.
- Rollback plan.
- Validation evidence.

## Public repository boundary

This public repository may include synthetic retention examples only.

Real logs, real device data, customer measurements and environment-specific data must be stored outside this public repository.

## Principle

No persistence by default.

Retention must be intentional, documented, reviewed and evidenced.
