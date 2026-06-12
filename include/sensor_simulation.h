#pragma once

#include <Arduino.h>

struct SimulatedSensorReading {
  uint32_t sequence;
  int temperature_c_x100;
  int humidity_percent_x100;
};

inline SimulatedSensorReading read_simulated_sensor(uint32_t sequence) {
  const int temperature_wave = static_cast<int>((sequence % 20) - 10);
  const int humidity_wave = static_cast<int>((sequence % 10) - 5);

  SimulatedSensorReading reading;
  reading.sequence = sequence;
  reading.temperature_c_x100 = 2150 + (temperature_wave * 5);
  reading.humidity_percent_x100 = 4500 + (humidity_wave * 10);
  return reading;
}

inline void print_simulated_sensor_reading(const SimulatedSensorReading &reading) {
  Serial.print(" sensor_sequence=");
  Serial.print(reading.sequence);
  Serial.print(" simulated_temperature_c=");
  Serial.print(reading.temperature_c_x100 / 100);
  Serial.print(".");
  Serial.print(abs(reading.temperature_c_x100 % 100));
  Serial.print(" simulated_humidity_percent=");
  Serial.print(reading.humidity_percent_x100 / 100);
  Serial.print(".");
  Serial.print(abs(reading.humidity_percent_x100 % 100));
}
