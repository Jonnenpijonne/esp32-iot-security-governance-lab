# Rollback Rehearsal

This document defines a lightweight rollback rehearsal model.

A rollback rehearsal is a controlled check that proves a change can be reversed before the change is treated as ready.

## Purpose

Rollback rehearsal reduces operational uncertainty.

The goal is not to create heavy process. The goal is to make sure the team knows how to return to the previous known-good state.

## Minimum rehearsal record

A rollback rehearsal should record:

- Change id.
- Previous known-good state.
- Rollback steps.
- Validation command.
- Expected result.
- Actual result.
- Evidence location.
- Owner.

## Rehearsal levels

| Level | Use case |
| --- | --- |
| Tabletop | Documentation-only review |
| Local dry run | Local validation without real deployment |
| Controlled restore | Restore to previous known-good state in a controlled environment |

## Current lab baseline

For this public lab, rollback rehearsal means:

- Revert the change or return to the previous commit.
- Run `bash scripts/validate-docs.sh`.
- Run `python -m pytest` where applicable.
- Run `pio run` for firmware changes.
- Record result in evidence.

## Principle

Rollback should be boring, repeatable and documented.
