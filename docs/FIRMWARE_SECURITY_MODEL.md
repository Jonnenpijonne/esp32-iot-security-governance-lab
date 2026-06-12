# Firmware Security Model

This document defines the security model for the firmware skeleton in this repository.

The firmware included in this public repository is intentionally minimal. It is a governance demonstration, not a production firmware package.

## Firmware scope

The current firmware skeleton:

- Boots on a generic ESP32 development board.
- Prints firmware version and device profile to serial output.
- Emits a local status line at a fixed interval.
- Does not connect to Wi-Fi.
- Does not enable Bluetooth.
- Does not send telemetry.
- Does not perform OTA updates.
- Does not store credentials.
- Does not include customer-specific logic.

## Security principle

The default firmware posture is safe and local.

Networking, telemetry, OTA updates, device identity, certificates and remote configuration must be added only through reviewed changes with documented risk, rollback and evidence.

## Controlled expansion model

Firmware features should be added in controlled increments:

1. Local boot and status only.
2. Device identity placeholder.
3. Local sensor simulation.
4. Controlled configuration loading.
5. Network enablement in a separate reviewed change.
6. Telemetry enablement in a separate reviewed change.
7. OTA enablement in a separate reviewed change.
8. Release signing and release evidence in a separate controlled process.

## Prohibited public-repository content

The public firmware tree must not include:

- Real credentials.
- Customer-specific device logic.
- Customer-specific network details.
- Real certificates or private keys.
- Real operational telemetry endpoints.
- Classified or sensitive project details.

## Evidence expectations

Each firmware-related change should define:

- Purpose of change.
- Security impact.
- Configuration impact.
- Telemetry impact.
- Rollback plan.
- Validation evidence.
- Known limitations.

## Initial firmware baseline

The initial firmware baseline is intentionally simple:

- Version: 0.1.0
- Network: disabled
- Telemetry: disabled
- OTA: disabled
- Configuration: compile-time demo values only
- Output: serial console only

This makes the first firmware version suitable for governance review without introducing unnecessary attack surface.
