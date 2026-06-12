# Change Size Gates

This document defines lightweight gates for change size and acceptance.

## Purpose

The goal is to keep changes small enough to understand and easy enough to reverse.

## Change classes

| Class | Description | Expected control |
| --- | --- | --- |
| XS | Documentation-only or synthetic example | Validation required |
| S | Local firmware or model change without external behavior | Validation and rollback note required |
| M | Multiple files or wider local behavior change | Validation, rollback rehearsal and evidence required |
| L | Wider scope or external behavior | Stronger review required before proceeding |

## Gate questions

Before accepting a change, ask:

- Is the affected scope clear?
- Is the rollback path clear?
- Has validation passed?
- Is evidence recorded?
- Does the public/private boundary remain intact?
- Does the change add external behavior?

## Complexity rule

Prefer several small governed changes over one large unclear change.

## Current lab default

The public lab default target is XS, S or controlled M.

L-sized changes should remain out of the public baseline until the governance model is ready for them.
