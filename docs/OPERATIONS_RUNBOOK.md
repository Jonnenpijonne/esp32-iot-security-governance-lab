# Operations Runbook

This document defines a high-level operations runbook for ESP32 / edge-device projects using this governance model.

The runbook is intentionally generic. Customer-specific operating procedures should be maintained outside this public repository.

## Purpose

The purpose of the runbook is to describe what operators, maintainers or project owners should know before devices are used in a real environment.

## Operating assumptions

Before use, the project should define:

- Device owner.
- Environment owner.
- Configuration owner.
- Update owner.
- Evidence owner.
- Incident contact.
- Decommissioning owner.

## Device onboarding

Before a device is accepted into use, confirm:

- Device identity is recorded.
- Expected firmware or configuration version is recorded.
- Network assumptions are documented.
- Telemetry expectations are documented.
- Security baseline has been reviewed.
- Evidence location is known.

## Configuration review

Configuration review should confirm:

- No default credentials are used.
- Required interfaces are documented.
- Unused features are disabled where possible.
- Telemetry is minimized.
- Logging expectations are defined.
- Update behavior is documented.

## Update window

Before an update, confirm:

- Change record exists.
- Approver is known.
- Validation has passed.
- Rollback target exists.
- Operator understands expected behavior.
- Evidence will be collected.

## Abnormal behavior

When abnormal behavior is observed, record:

- Device identifier.
- Time of observation.
- Observed behavior.
- Recent changes.
- Network or power conditions, if relevant.
- Logs or screenshots, if available.
- Immediate containment decision.
- Escalation owner.

## Rollback

Rollback should be considered when:

- Update causes unexpected behavior.
- Device loses required functionality.
- Security baseline cannot be confirmed.
- Telemetry behavior differs from expectation.
- Operator cannot verify the current state.

Rollback evidence should include:

- Reason for rollback.
- Previous known-good version.
- Person approving rollback.
- Time of rollback.
- Post-rollback validation result.

## Lost or removed device

If a device is lost, removed or retired, record:

- Device identifier.
- Last known state.
- Last known configuration.
- Data exposure assessment.
- Decommissioning decision.
- Evidence location.

## Evidence collection

Operational evidence may include:

- Validation reports.
- Change records.
- Release records.
- Configuration review notes.
- Rollback records.
- Incident notes.
- Decommissioning records.

## Public repository boundary

This runbook is generic. Real operational logs, customer names, locations, network information, screenshots and incident details should not be stored in this public repository.
