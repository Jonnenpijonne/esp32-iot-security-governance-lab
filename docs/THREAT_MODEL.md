# ESP32 IoT Threat Model

## Purpose

This threat model identifies common risks for ESP32-based IoT and edge-device deployments.

The model is intentionally lightweight. It is meant to support early design, portfolio review and governance decisions before real firmware or cloud integrations are added.

---

## Assets

| Asset | Why it matters |
| --- | --- |
| Device firmware | Defines device behavior and security controls |
| Wi-Fi credentials | Can expose the local network if leaked |
| API credentials | Can expose backend services or telemetry endpoints |
| Device identity | Used to authorize device communication |
| Sensor data | May reveal physical activity or environmental state |
| OTA/update mechanism | Can become a remote compromise path |
| Logs / telemetry | Can contain sensitive operational or privacy data |
| Physical device | Can be stolen, reflashed or inspected |

---

## Threats

| Threat | Example | Mitigation direction |
| --- | --- | --- |
| Credential leakage | Wi-Fi password committed to Git | `.gitignore`, placeholders, secret scanning |
| Insecure firmware update | Unverified OTA package | signed update concept, rollback plan |
| Excessive telemetry | Device reports unnecessary activity data | telemetry minimization and purpose limitation |
| Wireless exposure | Open debug AP or weak Wi-Fi config | secure Wi-Fi config, no default passwords |
| Physical tampering | Device accessed through exposed pins | physical placement, debug interface awareness |
| Cloud dependency risk | Device unusable if API/backend fails | local fallback / fail-safe behavior |
| Privacy leakage | Sensor data reveals activity patterns | privacy review and retention limits |
| Uncontrolled changes | Firmware changed without review | change request, risk class, validation evidence |

---

## Risk classes

| Risk class | Meaning | Example |
| --- | --- | --- |
| Class 1 | Low-risk documentation or non-functional change | README wording update |
| Class 2 | Configuration, telemetry, non-production firmware or governance change | Wi-Fi sensor demo change |
| Class 3 | Production firmware, OTA, credential, authentication or safety-relevant change | OTA update logic or device identity handling |

---

## Privacy note

Wireless and sensor-enabled devices may reveal more than their direct function suggests. Motion, presence, signal changes, telemetry timing and device connectivity patterns can all become privacy-relevant.

---

## Required evidence for higher-risk changes

Class 2 and Class 3 changes should include:

- impact analysis
- rollback plan
- test plan
- privacy consideration
- evidence of validation
- approval record
