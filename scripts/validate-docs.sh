#!/usr/bin/env bash
set -euo pipefail

REQUIRED_FILES=(
  "README.md"
  ".gitignore"
  "platformio.ini"
  "src/main.cpp"
  "include/lab_config.example.h"
  "include/sensor_simulation.h"
  "include/retention_policy.h"
  "include/audit_events.h"
  "models/README.md"
  "models/FEATURES.md"
  "models/readiness_model.py"
  "models/network_inventory_model.py"
  "models/change_control_model.py"
  "models/vectorization_model.py"
  "models/model_package_gate.py"
  "tests/test_readiness_model.py"
  "tests/test_network_inventory_model.py"
  "tests/test_change_control_model.py"
  "tests/test_vectorization_model.py"
  "tests/test_model_package_gate.py"
  "docs/ROADMAP.md"
  "docs/DEVELOPER_HANDOFF.md"
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
  "docs/SENSOR_DATA_GOVERNANCE.md"
  "docs/DATA_RETENTION_BOUNDARY.md"
  "docs/EVENT_VISIBILITY_MODEL.md"
  "docs/NETWORK_POINT_INVENTORY_MODEL.md"
  "docs/AUTHORIZED_SITE_SURVEY_MODEL.md"
  "docs/NETWORK_POINT_RECORD_SCHEMA.md"
  "docs/BLAST_RADIUS_AND_ROLLBACK_MODEL.md"
  "docs/ROLLBACK_REHEARSAL.md"
  "docs/CHANGE_SIZE_GATES.md"
  "examples/esp32-wifi-sensor-change.md"
  "examples/esp32-ota-update-change.md"
  "examples/esp32-device-identity-change.md"
  "examples/esp32-sensor-simulation-change.md"
  "examples/esp32-data-retention-boundary-change.md"
  "examples/building-network-point-survey.md"
  "examples/shelter-readiness-assessment.md"
  "evidence/EXAMPLE_VALIDATION_REPORT.md"
  "evidence/EXAMPLE_FIRMWARE_BASELINE_REPORT.md"
  "evidence/EXAMPLE_DEVICE_IDENTITY_REPORT.md"
  "evidence/EXAMPLE_SENSOR_SIMULATION_REPORT.md"
  "evidence/EXAMPLE_DATA_RETENTION_REPORT.md"
  "evidence/EXAMPLE_SITE_SURVEY_REPORT.md"
  "evidence/EXAMPLE_BLAST_RADIUS_ROLLBACK_REPORT.md"
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
