#!/usr/bin/env bash
set -euo pipefail

REQUIRED_FILES=(
  "README.md"
  ".gitignore"
  "platformio.ini"
  "src/main.cpp"
  "include/lab_config.example.h"
  "docs/ARCHITECTURE.md"
  "docs/THREAT_MODEL.md"
  "docs/SECURITY_BASELINE.md"
  "docs/DEVICE_LIFECYCLE.md"
  "docs/OTA_AND_ROLLBACK.md"
  "docs/PRIVACY_AND_TELEMETRY.md"
  "docs/CHANGE_GOVERNANCE.md"
  "docs/EVIDENCE_MODEL.md"
  "docs/PRODUCTIZATION_MODEL.md"
  "docs/ASSURANCE_CASE.md"
  "docs/SUPPLIER_AND_COMPONENT_GOVERNANCE.md"
  "docs/RELEASE_GOVERNANCE.md"
  "docs/OPERATIONS_RUNBOOK.md"
  "docs/PUBLIC_SCOPE.md"
  "docs/FIRMWARE_SECURITY_MODEL.md"
  "docs/KATAKRI_ALIGNMENT.md"
  "docs/DEVICE_IDENTITY_AND_CONFIGURATION.md"
  "examples/esp32-wifi-sensor-change.md"
  "examples/esp32-ota-update-change.md"
  "examples/esp32-device-identity-change.md"
  "evidence/EXAMPLE_VALIDATION_REPORT.md"
  "evidence/EXAMPLE_FIRMWARE_BASELINE_REPORT.md"
  "evidence/EXAMPLE_DEVICE_IDENTITY_REPORT.md"
)

FAILED=0

for file in "${REQUIRED_FILES[@]}"; do
  if [ ! -f "$file" ]; then
    echo "FAIL: missing $file"
    FAILED=1
  else
    echo "PASS: $file"
  fi
done

if [ "$FAILED" -ne 0 ]; then
  echo "ESP32 IoT Security Governance Lab validation: FAILED"
  exit 1
fi

echo "ESP32 IoT Security Governance Lab validation: PASSED"
