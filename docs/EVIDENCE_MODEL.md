# ESP32 Evidence Model

## Purpose

This document defines what useful evidence looks like for ESP32 IoT / edge-device governance.

Evidence should help prove that a change was planned, reviewed, tested and recoverable.

---

## Evidence types

| Evidence type | Example |
| --- | --- |
| Change request | Markdown file describing the change |
| Validation output | Output from `scripts/validate-docs.sh` |
| Test notes | Manual or scripted test result |
| Rollback notes | Recovery or reflash plan |
| Review record | Approver or reviewer entry |
| Version reference | Firmware/configuration version note |
| Privacy note | What data is collected and why |

---

## Evidence rules

- Keep curated examples in Git.
- Keep uncontrolled generated output out of Git.
- Do not commit secrets, real credentials or sensitive raw captures.
- Store generated evidence under ignored folders unless intentionally curated.
- Prefer Markdown evidence for readability.

---

## Example evidence summary

```text
Change: ESP32 Wi-Fi sensor telemetry example
Risk class: 2
Validation: PASSED
Rollback: Remove example change and restore previous documentation state
Privacy: No real telemetry or production data included
Evidence: EXAMPLE_VALIDATION_REPORT.md
```
