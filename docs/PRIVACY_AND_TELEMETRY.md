# Privacy and Telemetry Model

## Purpose

ESP32 devices often interact with physical environments. Even simple signals can become privacy-relevant when collected, transmitted or correlated over time.

This document defines lightweight privacy and telemetry principles for ESP32 IoT / edge-device work.

---

## Privacy-relevant data examples

| Data type | Why it can matter |
| --- | --- |
| Motion or presence events | Can reveal occupancy or routines |
| Wi-Fi/Bluetooth connectivity events | Can reveal device proximity or behavior patterns |
| Sensor readings | Can reveal environmental or human activity |
| Timestamps | Can reveal routines and usage cycles |
| Device identifiers | Can link events to a device or location |
| Network metadata | Can reveal infrastructure details |

---

## Telemetry principles

1. Collect only what is needed.
2. Document why telemetry is collected.
3. Avoid raw dumps by default.
4. Avoid sending secrets or identifiers in logs.
5. Prefer aggregation or minimization where possible.
6. Define retention before collection.
7. Document whether telemetry leaves the local network.
8. Treat motion, presence and routine data as sensitive.

---

## Wi-Fi sensing note

Wireless environments can reveal physical-world activity even without cameras. Signal changes, connectivity patterns and device behavior can become privacy-relevant when processed or stored.

For this reason, ESP32 and smart-home style devices should be assessed not only as electronics, but as parts of a physical-environment sensing system.

---

## Privacy review questions

Before adding telemetry or sensing:

- What is being measured?
- Why is it needed?
- Is the data local or cloud-transmitted?
- Can the data reveal presence, motion or routine?
- How long is it retained?
- Who can access it?
- How is it deleted?
- Can the feature be disabled?

---

## Evidence expectations

For privacy-relevant changes, document:

- data category
- purpose
- retention expectation
- local/cloud boundary
- access path
- user-visible behavior
- disable/reset method
