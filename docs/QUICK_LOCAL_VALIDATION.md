# Quick Local Validation

This guide is for a reader who wants to validate the repository from a clean local checkout.

## Prerequisites

- Git
- Git Bash on Windows, or another Bash-compatible shell
- Python 3.x
- Internet connection for dependency installation

No physical ESP32 board is required for build validation. The firmware build targets `esp32dev`, but this guide does not flash a device.

---

## Option A — normal local checkout

Copy and run this in Git Bash:

```bash
git clone https://github.com/Jonnenpijonne/esp32-iot-security-governance-lab.git
cd esp32-iot-security-governance-lab

bash scripts/validate-docs.sh

python -m pytest \
  tests/test_readiness_model.py \
  tests/test_network_inventory_model.py \
  tests/test_network_point_model.py \
  tests/test_change_control_model.py \
  tests/test_vectorization_model.py \
  tests/test_model_package_gate.py \
  tests/test_blue_team_protection_model.py \
  tests/test_authorized_exercise_gate.py \
  tests/test_interference_observation_model.py \
  tests/test_emb3d_mapping_model.py \
  tests/test_emb3d_alignment_model.py

python -m pip install --upgrade platformio
python -m platformio --version
python -m platformio run
```

---

## Option B — temporary sandbox checkout

Use this if you want to validate the repository without keeping a permanent local copy.

```bash
cd /tmp
rm -rf esp32-iot-security-governance-lab

git clone https://github.com/Jonnenpijonne/esp32-iot-security-governance-lab.git
cd esp32-iot-security-governance-lab

bash scripts/validate-docs.sh

python -m pytest \
  tests/test_readiness_model.py \
  tests/test_network_inventory_model.py \
  tests/test_network_point_model.py \
  tests/test_change_control_model.py \
  tests/test_vectorization_model.py \
  tests/test_model_package_gate.py \
  tests/test_blue_team_protection_model.py \
  tests/test_authorized_exercise_gate.py \
  tests/test_interference_observation_model.py \
  tests/test_emb3d_mapping_model.py \
  tests/test_emb3d_alignment_model.py

python -m pip install --upgrade platformio
python -m platformio --version
python -m platformio run
```

Optional cleanup after validation:

```bash
cd /tmp
rm -rf esp32-iot-security-governance-lab
```

---

## PlatformIO command note

This guide intentionally uses:

```bash
python -m platformio run
```

instead of relying only on:

```bash
pio run
```

On some Windows / Git Bash environments, PlatformIO may be installed for the current Python user but the direct `pio` command may not be available in the shell `PATH`. In that case, `pio run` can return `command not found` even though PlatformIO itself is installed and working.

The validated fallback command is:

```bash
python -m platformio run
```

---

## Expected result

```text
Documentation validation: PASSED
Python tests: passed
PlatformIO firmware build: SUCCESS
Build artifacts: firmware.elf, firmware.bin
```

## Purpose

```text
repo -> documentation validation -> Python tests -> PlatformIO firmware build -> artifacts -> SUCCESS
```

This validates that the repository has a runnable local verification path and is not documentation-only.
