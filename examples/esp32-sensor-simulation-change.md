# Example Change: ESP32 Local Sensor Simulation

This is a synthetic example change record for the public governance lab.

It does not describe a customer system, protected environment or production device.

## Change summary

Add local simulated sensor readings to the ESP32 firmware skeleton.

## Purpose

The purpose is to demonstrate sensor-data governance without using real sensors, real measurements, network transmission or telemetry upload.

## Scope

Included:

- `include/sensor_simulation.h`
- `src/main.cpp`
- `docs/SENSOR_DATA_GOVERNANCE.md`

Excluded:

- Real sensor hardware integration.
- Real measurement data.
- Network transmission.
- Telemetry upload.
- Customer-specific data.
- Site-specific data.

## Risk class

Risk class: Low for public governance lab.

Reason:

The change uses deterministic synthetic values and prints them locally to the serial console. It does not enable network, telemetry or OTA behavior.

## Security impact

Positive:

- Sensor-data handling is now visible in the firmware baseline.
- Data classification is documented.
- Telemetry boundary is explicit.

Negative:

- Future real sensor work could accidentally reuse public example assumptions without proper classification.

Mitigation:

- Documentation states that real sensor data requires separate classification, retention and telemetry review.

## Rollback plan

Rollback by reverting:

- `include/sensor_simulation.h`
- Related `src/main.cpp` changes.
- `docs/SENSOR_DATA_GOVERNANCE.md`

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
- Sensor data governance document.
- Updated baseline report if needed.
