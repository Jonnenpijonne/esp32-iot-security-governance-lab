#!/usr/bin/env bash
set -euo pipefail

REQUIRED_FILES=(
  "README.md"
  ".gitignore"
  "docs/ARCHITECTURE.md"
  "docs/THREAT_MODEL.md"
  "docs/SECURITY_BASELINE.md"
  "docs/DEVICE_LIFECYCLE.md"
  "docs/OTA_AND_ROLLBACK.md"
  "docs/PRIVACY_AND_TELEMETRY.md"
  "docs/CHANGE_GOVERNANCE.md"
  "docs/EVIDENCE_MODEL.md"
  "examples/esp32-wifi-sensor-change.md"
  "examples/esp32-ota-update-change.md"
  "evidence/EXAMPLE_VALIDATION_REPORT.md"
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

if grep -RInE "WIFI_PASSWORD=|API_KEY=|PRIVATE_KEY=|BEGIN PRIVATE KEY" . \
  --exclude-dir=.git \
  --exclude-dir=.pio \
  --exclude-dir=build \
  --exclude="validate-docs.sh"; then
  echo "WARN: possible secret-like placeholder found. Review manually."
fi

if find . -type f \( -name "*.bin" -o -name "*.elf" -o -name "*.uf2" -o -name "*.pcap" -o -name "*.pcapng" \) | grep .; then
  echo "FAIL: generated firmware or capture artifact found"
  FAILED=1
fi

if [ "$FAILED" -ne 0 ]; then
  echo "ESP32 IoT Security Governance Lab validation: FAILED"
  exit 1
fi

echo "ESP32 IoT Security Governance Lab validation: PASSED"
