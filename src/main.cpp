#include <Arduino.h>
#include "lab_config.example.h"
#include "sensor_simulation.h"
#include "retention_policy.h"

#ifndef LAB_FIRMWARE_VERSION
#define LAB_FIRMWARE_VERSION "0.1.0"
#endif

#ifndef LAB_DEVICE_PROFILE
#define LAB_DEVICE_PROFILE "governance-demo"
#endif

static const uint32_t STATUS_INTERVAL_MS = 10000;
static uint32_t last_status_ms = 0;
static uint32_t sensor_sequence = 0;
static LocalRetentionState retention_state = create_empty_retention_state();

static void print_boot_banner() {
  Serial.println();
  Serial.println("ESP32 IoT Security Governance Lab");
  Serial.print("Firmware version: ");
  Serial.println(LAB_FIRMWARE_VERSION);
  Serial.print("Device profile: ");
  Serial.println(LAB_DEVICE_PROFILE);
  Serial.print("Example device id: ");
  Serial.println(LAB_EXAMPLE_DEVICE_ID);
  Serial.print("Example config profile: ");
  Serial.println(LAB_EXAMPLE_CONFIG_PROFILE);
  Serial.print("Example site label: ");
  Serial.println(LAB_EXAMPLE_SITE_LABEL);
  Serial.println("Mode: safe local skeleton, no network, no telemetry, no OTA");
  Serial.println("Retention: volatile last reading only, no persistent storage");
}

static void emit_local_status() {
  const SimulatedSensorReading reading = read_simulated_sensor(sensor_sequence++);
  update_local_retention(retention_state, reading);

  Serial.print("uptime_ms=");
  Serial.print(millis());
  Serial.print(" status=running");
  Serial.print(" network=");
  Serial.print(LAB_EXAMPLE_ENABLE_NETWORK ? "enabled" : "disabled");
  Serial.print(" telemetry=");
  Serial.print(LAB_EXAMPLE_ENABLE_TELEMETRY ? "enabled" : "disabled");
  Serial.print(" ota=");
  Serial.print(LAB_EXAMPLE_ENABLE_OTA ? "enabled" : "disabled");
  print_simulated_sensor_reading(reading);
  print_local_retention_state(retention_state);
  Serial.println();
}

void setup() {
  Serial.begin(115200);
  delay(500);
  print_boot_banner();
}

void loop() {
  const uint32_t now = millis();

  if (now - last_status_ms >= STATUS_INTERVAL_MS) {
    last_status_ms = now;
    emit_local_status();
  }
}
