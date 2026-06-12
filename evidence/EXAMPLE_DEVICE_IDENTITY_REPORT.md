# Example Device Identity Baseline Report

This is a synthetic evidence report for the public ESP32 IoT Security Governance Lab.

## Summary

| Field | Value |
| --- | --- |
| Device id | synthetic example only |
| Configuration profile | local-only-baseline |
| Site label | synthetic-lab |
| Network | disabled |
| Telemetry | disabled |
| OTA | disabled |

## Purpose

The purpose of this baseline is to show how a device identity and configuration profile can be made visible without using real project values.

## Evidence references

- `include/lab_config.example.h`
- `src/main.cpp`
- `docs/DEVICE_IDENTITY_AND_CONFIGURATION.md`
- `examples/esp32-device-identity-change.md`

## Expected firmware behavior

At boot, the firmware prints:

- Firmware version.
- Device profile.
- Synthetic device id.
- Synthetic configuration profile.
- Synthetic site label.
- Local-only mode statement.

During runtime, the firmware periodically prints local status showing that network, telemetry and OTA behavior remain disabled.

## Review conclusion

The identity baseline is suitable for a public governance lab because it uses only synthetic values and does not introduce external connectivity.
