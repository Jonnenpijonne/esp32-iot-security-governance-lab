# Quick Local Validation

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

Expected result:

```text
Documentation validation: PASSED
Python tests: passed
PlatformIO firmware build: SUCCESS
Build artifacts: firmware.elf, firmware.bin
```

Purpose:

```text
repo -> documentation validation -> Python tests -> PlatformIO firmware build -> artifacts -> SUCCESS
```

This validates that the repository has a runnable local verification path and is not documentation-only.
