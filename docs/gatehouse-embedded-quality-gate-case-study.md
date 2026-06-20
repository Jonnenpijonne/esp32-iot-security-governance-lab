# Gatehouse Embedded Quality Gate — Case Study

## Summary

This document records the rationale, implementation and validation outcome of the embedded Gatehouse quality gate added to the ESP32 IoT Security Governance Lab.

The change introduced a lightweight pre-CI governance layer for embedded and edge-device change documentation. The purpose was not to replace firmware builds, Python tests or existing repository validation. The purpose was to make security-boundary assumptions visible before technical CI/CD is treated as the next validation layer.

## Why this was added

The repository already had technical validation. The existing checks could verify that firmware builds, Python model tests pass and documentation validation succeeds.

However, technical checks alone do not fully answer governance questions such as:

```text
Is the change clearly scoped?
Is the risk class visible?
Is the public/private boundary documented?
Is the device or edge impact stated?
Is rollback documented?
Is evidence listed?
Does the change stay inside portfolio-safe example boundaries?
```

The embedded Gatehouse quality gate was added to make those questions explicit before merge.

## Design idea

The gate is intentionally lightweight.

It validates change documentation. It does not build firmware, deploy anything, operate devices, inspect live environments or replace human review.

The intended validation flow is:

```text
Change document
  -> Embedded Gatehouse quality gate
  -> Technical CI/CD validation
  -> Human review
  -> Merge
```

This keeps the governance layer understandable and prevents it from becoming a heavy compliance platform.

## What was implemented

The merged change added an embedded Gatehouse scaffold:

```text
.gatehouse/embedded-security-profile.yml
.gatehouse/change-template.md
changes/example-embedded-security-boundary-change.md
tools/gatehouse_embedded_check.py
.github/workflows/gatehouse-embedded-quality-gate.yml
```

The change was additive. It did not modify firmware source code, build configuration, PlatformIO setup, existing tests or runtime behavior.

## Required change document structure

The validator requires change documents under `changes/*.md` to include these sections:

```text
## Change type
## Risk class
## Scope
## Security impact
## Device / edge impact
## Public/private boundary
## Test plan
## Rollback plan
## Evidence
## Non-goals
```

The point is simple: a change should not be mergeable only because it is technically harmless. It should also be understandable, scoped, reversible and reviewable.

## Validator behavior

The validator is implemented in:

```text
tools/gatehouse_embedded_check.py
```

It checks that change documents include:

```text
required sections
allowed risk class
required public/private boundary statements
no blocked boundary wording outside approved protocol statements
```

The validator is deliberately conservative. It does not try to understand every sentence semantically. It checks for required structure and known boundary wording.

That makes the result predictable.

## GitHub Actions integration

The workflow is implemented in:

```text
.github/workflows/gatehouse-embedded-quality-gate.yml
```

It runs:

```bash
python tools/gatehouse_embedded_check.py
```

The workflow is now part of the protected validation path.

## Validation failures and corrections

During validation, the first failures came from wording inside the example change document. Some boundary terms were written in a way that was understandable to a human reviewer, but still matched the validator’s blocked wording list.

The correction was to rewrite those phrases using public-safe wording while preserving the same governance meaning.

Examples of safer wording:

```text
placeholder-based authentication boundary validation
synthetic sample data
live authentication material
restricted or non-public information
```

This was a documentation wording fix, not a protocol bypass.

## Validator rule conflict

A second failure revealed an internal rule conflict in the validator.

The validator required a specific public/private boundary statement, but also blocked part of the same wording when it appeared in the document.

That meant the document could not satisfy both rules at the same time:

```text
If the required statement was missing:
  the validator failed because the boundary statement was missing.
If the required statement was present:
  the validator failed because blocked wording appeared.
```

This was a validator design issue, not a documentation issue.

## Correct fix

The correct fix was not to remove the required boundary statement.

The correct fix was also not to weaken the whole validator.

The correct fix was to allow required protocol statements while keeping the blocked wording active everywhere else.

The validator was updated so that required boundary statements are allowed as protocol text, while the same wording remains blocked outside those statements.

This keeps the gate strict without making the rule set contradictory.

## Why this was not a bypass

This correction did not bypass the Gatehouse protocol.

The protocol was preserved:

```text
required sections still required
risk class still required
public/private boundary still required
test plan still required
rollback plan still required
evidence still required
```

The validator was corrected only because its previous rule set was internally contradictory.

A good quality gate must be strict, but it must also be logically consistent.

## Governance lesson

A quality gate failure can mean different things:

```text
1. The document is incomplete.
2. The validator has a rule bug.
3. The process requires missing evidence or approval.
```

Those should not be treated the same way.

If the document is incomplete, fix the document.

If the validator contradicts itself, fix the validator.

If the process requires evidence or approval, add the evidence or approval note.

Do not silently bypass the protocol.

## Approval and protocol principle

If a change requires documentation, it must be documented.

If a change requires approval, the approval requirement must be recorded.

If an approval is not applicable because the change is a portfolio example rather than a production change, that must be documented as the approval model.

The principle is:

```text
Do not bypass the protocol.
If the protocol is not applicable, document why.
If the validator is contradictory, fix the validator.
If the documentation is incomplete, fix the documentation.
```

## Relationship to technical CI/CD

The embedded Gatehouse quality gate does not replace the normal technical pipeline.

It complements it.

Technical validation answers questions such as:

```text
Does the firmware build?
Do Python tests pass?
Do documentation checks pass?
Does the repository still validate?
```

The Gatehouse check answers questions such as:

```text
Is the change scoped?
Is the risk class visible?
Is the security impact described?
Is device / edge impact described?
Is the public/private boundary clear?
Is rollback documented?
Is evidence listed?
```

Together, these create a stronger validation story.

## Ruleset alignment

After the PR checks passed, the main-branch ruleset was aligned so that the required checks matched the actual workflow job names.

The required checks are:

```text
Build ESP32 firmware skeleton
Gatehouse embedded quality gate
Run Python model tests
Validate documentation baseline
```

The important point is that rulesets should not contain stale or ghost check names. A strict ruleset is useful only when it points to real checks that the repository actually reports.

## Final outcome

The final outcome is a lightweight embedded Gatehouse profile that:

```text
adds governance structure for change documents
validates public/private boundary wording
requires risk, scope, impact, test, rollback and evidence sections
runs through GitHub Actions
keeps firmware and runtime behavior unchanged
preserves human review
avoids protocol bypass
```

The most valuable part of the work was not just adding the validator.

The valuable part was discovering a rule conflict, preserving the required boundary statement, and correcting the validator so that it enforces the protocol consistently.

## One-sentence summary

The embedded Gatehouse quality gate adds a small pre-CI governance layer that validates security-boundary change documentation before technical CI/CD, while keeping the repository lightweight and reviewable.
