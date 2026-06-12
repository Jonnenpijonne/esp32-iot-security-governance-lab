# Architecture

The project architecture has three layers:

1. Firmware baseline.
2. Python validation models.
3. Governance and evidence documentation.

## Firmware layer

| Component | Purpose |
| --- | --- |
| `platformio.ini` | ESP32 build configuration |
| `src/main.cpp` | Local-only firmware skeleton |
| `include/lab_config.example.h` | Synthetic device identity and configuration |
| `include/sensor_simulation.h` | Synthetic sensor values |
| `include/retention_policy.h` | Volatile last-reading retention |
| `include/audit_events.h` | Local event visibility |

## Python model layer

The Python models provide defensive validation and governance scoring.

They do not interact with real networks or devices.

## Documentation layer

The documentation layer describes security posture, evidence, boundaries, mitigations and operating assumptions.

## Boundary

Public repository content stays synthetic.

Project-specific data belongs in private annexes.
