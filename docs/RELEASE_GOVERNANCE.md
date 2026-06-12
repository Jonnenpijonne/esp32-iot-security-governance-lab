# Release Governance

This document defines a documentation-first release governance model for ESP32 / edge-device projects.

The current repository does not build real firmware. This document describes the controls that should exist before a real implementation creates release artifacts.

## Purpose

The purpose is to make releases controlled, traceable, reviewable and reversible.

## Release flow

A controlled release should follow this flow:

1. Source change is proposed.
2. Change is reviewed.
3. Required documentation is updated.
4. Validation is executed.
5. Build output is created in a controlled environment.
6. Release evidence is collected.
7. Release is approved.
8. Deployment window is defined.
9. Rollback target is confirmed.
10. Post-release validation is recorded.

## Required release metadata

A release record should include release name, release version, source commit, build environment, tool version, validation result, approver, rollback target and known limitations.

## Build evidence

Build evidence should include build command, build environment, tool version, validation command, validation output and artifact hash when applicable.

## Approval expectations

Before release, the project should confirm that architecture impact, baseline impact, telemetry impact, rollback plan and evidence ownership have been considered.

## Rollback expectations

Each release should define previous known-good version, rollback decision owner, rollback trigger, rollback evidence and post-rollback validation.

## Public repository boundary

This public repository may contain release governance templates and examples. Real delivery artifacts, real customer release records and environment-specific details should be stored in controlled project locations.

## Minimum readiness checklist

A release process is not ready until build process, validation process, approval model, rollback target, evidence package and public/private information boundary are documented.
