import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID, CONF_UART_ID, CONF_UPDATE_INTERVAL

# 定义命名空间
r60abd1_ns = cg.esphome_ns.namespace('r60abd1')
R60ABD1Component = r60abd1_ns.class_('R60ABD1Component', cg.PollingComponent, uart.UARTDevice)

# 配置选项
CONFIG_SCHEMA = cv.Schema({
    cv.GenerateID(): cv.declare_id(R60ABD1Component),
    cv.Required(CONF_UART_ID): cv.use_id(uart.UARTComponent),
    cv.Optional(CONF_UPDATE_INTERVAL, default='1s'): cv.update_interval,
}).extend(uart.UART_DEVICE_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    cg.add(var.set_update_interval(config[CONF_UPDATE_INTERVAL]))

