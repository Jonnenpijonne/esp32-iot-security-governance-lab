# ESP32 Security Baseline

## Purpose

This document defines a lightweight security baseline for ESP32 IoT / edge-device work.

It is intended for early project governance, not as a complete embedded security standard.

---

## Baseline controls

| Control area | Baseline expectation |
| --- | --- |
| Secrets | No real Wi-Fi passwords, API keys or certificates in Git |
| Configuration | Use example files and placeholders for local configuration |
| Wireless | Disable unnecessary Wi-Fi/Bluetooth features |
| Debugging | Do not expose debug interfaces unnecessarily |
| Firmware | Document firmware source, version and update method |
| OTA | Treat OTA/update logic as high-risk unless proven otherwise |
| Logging | Avoid logging secrets or sensitive telemetry |
| Telemetry | Collect only what is needed and document purpose |
| Recovery | Define rollback or reflash path before update changes |
| Evidence | Store validation outputs as examples, not uncontrolled generated noise |

---

## Secrets handling

Do not commit:

```text
.env
wifi credentials
API keys
private certificates
private keys
real backend URLs
customer identifiers
raw telemetry dumps
packet captures with sensitive data
```

Use placeholders:

```text
WIFI_SSID=example-network
WIFI_PASSWORD=change-me-locally
API_ENDPOINT=https://example.invalid
DEVICE_ID=esp32-demo-device
```

---

## Wireless configuration principles

- Avoid default credentials.
- Avoid unnecessary access point mode.
- Avoid open debug services.
- Prefer explicit pairing or provisioning steps.
- Document whether Wi-Fi, Bluetooth or both are enabled.
- Document whether the device can operate offline.

---

## Firmware/update principles

- Keep firmware source traceable.
- Document build method before release artifacts are produced.
- Do not commit binary firmware artifacts unless intentionally released.
- Treat update paths as security-sensitive.
- Plan rollback before OTA/update changes.

---

## Evidence expectations

For meaningful changes, keep evidence of:

- what changed
- why it changed
- risk class
- test result
- rollback plan
- validation status
- reviewer / approver

Generated local evidence should usually stay out of Git unless it is a curated example.
