#pragma once

#include <Arduino.h>

enum class AuditEventType {
  BOOT,
  STATUS_EMITTED,
  SENSOR_READING_UPDATED,
  RETENTION_STATE_REPORTED
};

inline const char *audit_event_name(AuditEventType event_type) {
  switch (event_type) {
    case AuditEventType::BOOT:
      return "BOOT";
    case AuditEventType::STATUS_EMITTED:
      return "STATUS_EMITTED";
    case AuditEventType::SENSOR_READING_UPDATED:
      return "SENSOR_READING_UPDATED";
    case AuditEventType::RETENTION_STATE_REPORTED:
      return "RETENTION_STATE_REPORTED";
    default:
      return "UNKNOWN";
  }
}

inline void emit_audit_event(AuditEventType event_type, const char *detail) {
  Serial.print("audit_event=");
  Serial.print(audit_event_name(event_type));
  Serial.print(" uptime_ms=");
  Serial.print(millis());
  Serial.print(" detail=");
  Serial.println(detail);
}
