# Getting Started

This guide explains how to run the public ESP32 / embedded edge-device security governance lab locally.

## 1. Clone the repository

```bash
git clone https://github.com/Jonnenpijonne/esp32-iot-security-governance-lab.git
cd esp32-iot-security-governance-lab
```

## 2. Validate documentation baseline

```bash
bash scripts/validate-docs.sh
```

Expected result:

```text
ESP32 IoT Security Governance Lab validation: PASSED
```

## 3. Run Python model examples

```bash
python models/readiness_model.py
python models/network_inventory_model.py
python models/network_point_model.py
python models/change_control_model.py
python models/vectorization_model.py
python models/model_package_gate.py
python models/blue_team_protection_model.py
python models/authorized_exercise_gate.py
python models/interference_observation_model.py
python models/emb3d_mapping_model.py
python models/emb3d_alignment_model.py
```

## 4. Run Python tests

```bash
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
```

## 5. Build firmware skeleton

Install PlatformIO if needed:

```bash
python -m pip install --upgrade platformio
```

Build:

```bash
pio run
```

If `pio` is not available directly in Git Bash, run PlatformIO through Python:

```bash
python -m platformio --version
python -m platformio run
```

Expected local validation result:

```text
PlatformIO Core, version 6.1.19
Processing esp32dev (platform: espressif32; board: esp32dev; framework: arduino)
Linking .pio\build\esp32dev\firmware.elf
Building .pio\build\esp32dev\firmware.bin
RAM:   6.6%
Flash: 20.5%
[SUCCESS]
```

A successful build confirms that this repository has a locally runnable ESP32 firmware build path and is not documentation-only.

## 6. Interpret the project

This repository demonstrates:

- firmware baseline control
- local-only sensor simulation
- volatile data-retention boundary
- event visibility
- network point inventory readiness
- defensive validation gates
- protection scoring
- interference observation
- EMB3D-style property mapping
- KATAKRI-style public/private boundary

## 7. Public/private boundary

Keep this repository synthetic.

Do not add:

- real customer data
- real site names
- real room labels
- real device inventories
- real network addresses
- real evidence from protected environments
- credentials
- keys
- production secrets

Real project records belong in controlled private annexes.
