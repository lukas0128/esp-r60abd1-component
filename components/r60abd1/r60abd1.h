#pragma once
#include "esphome.h"

namespace esphome {
namespace r60abd1 {

class R60ABD1Component : public PollingComponent, public UARTDevice {
 public:
  R60ABD1Component(UARTComponent *parent) : PollingComponent(1000), UARTDevice(parent) {}

  Sensor *heart_rate_sensor = new Sensor();
  Sensor *breath_rate_sensor = new Sensor();
  Sensor *sleep_state_sensor = new Sensor();

  void setup() override;
  void update() override;

 protected:
  void parse_data();
};

}  // namespace r60abd1
}  // namespace esphome