# Event Visibility Model

This document defines the local event visibility model for the public ESP32 IoT Security Governance Lab.

The firmware prints event-style lines to the serial console only.

## Current firmware events

| Event | Purpose |
| --- | --- |
| BOOT | Boot banner was printed |
| SENSOR_READING_UPDATED | Synthetic local reading was updated |
| RETENTION_STATE_REPORTED | Runtime retention state was reported |
| STATUS_EMITTED | Local status line was printed |

## Scope

Included:

- Local serial event output.
- Synthetic firmware lifecycle events.
- Runtime-only visibility.

Excluded:

- Stored event history.
- Forwarded event streams.
- Customer-specific event records.
- Environment-specific event records.

## Governance rule

Any change that stores or forwards event data should be treated as a governed change.

## Principle

Event visibility should be explicit before events become stored, forwarded or project-specific.
