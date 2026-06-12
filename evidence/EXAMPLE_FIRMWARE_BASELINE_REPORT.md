# Example Firmware Baseline Report

This is a synthetic example evidence report for the public ESP32 IoT Security Governance Lab.

It does not describe a customer system, protected environment or production device.

## Baseline summary

| Field | Value |
| --- | --- |
| Firmware profile | governance-demo |
| Firmware version | 0.1.0 |
| Board profile | esp32dev |
| Framework | Arduino via PlatformIO |
| Network | disabled |
| Bluetooth | disabled |
| Telemetry | disabled |
| OTA | disabled |
| Secrets | none in repository |
| Customer logic | none |

## Purpose

The purpose of the first firmware baseline is to prove that the repository can contain a minimal ESP32 firmware skeleton without turning into an uncontrolled firmware product.

The baseline is intentionally local-only. It prints a boot banner and local status messages to the serial console.

## Evidence references

- `platformio.ini`
- `src/main.cpp`
- `docs/FIRMWARE_SECURITY_MODEL.md`
- `docs/KATAKRI_ALIGNMENT.md`
- `docs/RELEASE_GOVERNANCE.md`
- `scripts/validate-docs.sh`

## Validation commands

Documentation and baseline validation:

```bash
bash scripts/validate-docs.sh
```

Optional firmware build validation when PlatformIO is available:

```bash
pio run
```

## Expected result

The documentation validation should pass.

The firmware build should compile the local-only skeleton for the configured ESP32 development board.

## Security posture

The initial firmware baseline has intentionally low external exposure:

- No Wi-Fi connection is initiated.
- No Bluetooth functionality is enabled.
- No telemetry endpoint is configured.
- No OTA update mechanism is enabled.
- No credentials are stored.
- No customer-specific behavior is included.

## Known limitations

This is not production firmware.

Missing production controls include:

- Device identity.
- Secure configuration loading.
- Release signing.
- Hardware-backed key handling.
- Secure OTA implementation.
- Sensor integration.
- Operational monitoring.
- Project-specific approval evidence.

## Review conclusion

The firmware baseline is suitable as a first governance-controlled skeleton.

Further features should be added only through reviewed changes with updated threat model, security baseline, rollback plan and evidence records.
