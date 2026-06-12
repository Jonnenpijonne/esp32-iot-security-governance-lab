#pragma once

#include <Arduino.h>
#include "sensor_simulation.h"

struct LocalRetentionState {
  bool has_last_reading;
  SimulatedSensorReading last_reading;
  uint32_t last_update_ms;
};

inline LocalRetentionState create_empty_retention_state() {
  LocalRetentionState state;
  state.has_last_reading = false;
  state.last_reading = {0, 0, 0};
  state.last_update_ms = 0;
  return state;
}

inline void update_local_retention(LocalRetentionState &state, const SimulatedSensorReading &reading) {
  state.has_last_reading = true;
  state.last_reading = reading;
  state.last_update_ms = millis();
}

inline void print_local_retention_state(const LocalRetentionState &state) {
  Serial.print(" retention=volatile_last_reading_only");
  Serial.print(" retained_samples=");
  Serial.print(state.has_last_reading ? 1 : 0);
  Serial.print(" persistent_storage=disabled");
}
