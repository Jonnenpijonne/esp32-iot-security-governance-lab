# Audit Event Model

This document defines the public lab audit event model.

The current firmware emits audit-style events to the serial console only. Events are not stored persistently and are not transmitted over a network.

## Current events

| Event | Meaning |
| --- | --- |
| BOOT | Firmware boot sequence reached the local banner stage |
| SENSOR_READING_UPDATED | Synthetic local sensor reading was updated |
| RETENTION_STATE_REPORTED | Volatile retention state was reported |
| STATUS_EMITTED | Local status line was emitted |

## Scope

The audit event model is intended for public governance demonstration only.

It does not include:

- Persistent event storage.
- Remote log shipping.
- Network transmission.
- Customer-specific event data.
- Protected environment details.

## Governance rule

Any future change that stores or transmits audit events must be treated as a governed change.

## Principle

Audit events should be explicit before they are stored or transmitted.
