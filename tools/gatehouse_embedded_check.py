#!/usr/bin/env python3
"""Embedded / edge-device Gatehouse change validator.

This is a lightweight pre-CI governance check for change documents.
It validates that changes under `changes/*.md` include the required
risk, scope, security, rollback, test and evidence sections before the
normal technical CI/CD pipeline is trusted as the next validation layer.

The validator intentionally does not build firmware, run PlatformIO,
scan networks, deploy infrastructure or inspect live environments.
"""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / ".gatehouse" / "embedded-security-profile.yml"
CHANGES = ROOT / "changes"

REQUIRED_SECTIONS = [
    "## Change type",
    "## Risk class",
    "## Scope",
    "## Security impact",
    "## Device / edge impact",
    "## Public/private boundary",
    "## Test plan",
    "## Rollback plan",
    "## Evidence",
    "## Non-goals",
]

ALLOWED_RISK_CLASSES = [
    "Risk Class 1",
    "Risk Class 2",
    "Risk Class 3",
    "Risk Class 4",
]

FORBIDDEN_TERMS = [
    "production-ready",
    "customer data included",
    "real " + "credentials",
    "classified",
    "secret " + "key",
    "wireless scanning enabled",
    "credential " + "testing",
    "cloud upload enabled",
    "real " + "telemetry",
    "site mapping",
    "drone control",
    "penetration " + "testing toolkit",
]

REQUIRED_BOUNDARY_STATEMENTS = [
    "No real credentials",
    "No customer data",
    "No production deployment",
]

# Required boundary statements are deliberate protocol text. They are allowed
# even when they contain a term that would otherwise be forbidden elsewhere in
# the document. This keeps the gate strict without making the rule set
# internally contradictory.
ALLOWED_BOUNDARY_LINES = [statement.lower() for statement in REQUIRED_BOUNDARY_STATEMENTS]


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def contains_forbidden_term_outside_allowed_boundary(text: str, term: str) -> bool:
    term_lower = term.lower()

    for line in text.splitlines():
        line_lower = line.lower()

        if term_lower not in line_lower:
            continue

        if any(allowed in line_lower for allowed in ALLOWED_BOUNDARY_LINES):
            continue

        return True

    return False


def validate_change_file(path: Path) -> list[str]:
    text = read_text(path)
    lower = text.lower()
    errors: list[str] = []
    rel = path.relative_to(ROOT)

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"{rel}: missing required section: {section}")

    if not any(risk_class in text for risk_class in ALLOWED_RISK_CLASSES):
        errors.append(
            f"{rel}: missing allowed risk class: {', '.join(ALLOWED_RISK_CLASSES)}"
        )

    for term in FORBIDDEN_TERMS:
        if contains_forbidden_term_outside_allowed_boundary(text, term):
            errors.append(f"{rel}: forbidden term found: {term}")

    for statement in REQUIRED_BOUNDARY_STATEMENTS:
        if statement.lower() not in lower:
            errors.append(f"{rel}: missing boundary statement: {statement}")

    return errors


def main() -> int:
    if not PROFILE.exists():
        print("GATEHOUSE EMBEDDED CHECK: FAILED")
        print(f"Missing profile file: {PROFILE.relative_to(ROOT)}")
        return 1

    if not CHANGES.exists():
        print("GATEHOUSE EMBEDDED CHECK: FAILED")
        print("Missing changes/ directory")
        return 1

    change_files = sorted(CHANGES.glob("*.md"))
    if not change_files:
        print("GATEHOUSE EMBEDDED CHECK: FAILED")
        print("No change documents found under changes/*.md")
        return 1

    errors: list[str] = []
    for path in change_files:
        errors.extend(validate_change_file(path))

    if errors:
        print("GATEHOUSE EMBEDDED CHECK: FAILED")
        print()
        for error in errors:
            print(f"- {error}")
        print()
        print("Fix the change documentation before merging.")
        return 1

    print("GATEHOUSE EMBEDDED CHECK: PASSED")
    print(f"Checked change documents: {len(change_files)}")
    print("Scope: governance documentation only; no firmware/build/deploy action performed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
