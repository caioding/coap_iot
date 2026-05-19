"""
Arquivo: app/server.py

Objetivo:
    Montar o servidor CoAP e registrar todos os recursos expostos.
"""

import asyncio
import aiocoap.resource as resource
import aiocoap

from app.config import HOST, PORT, NODE_NAME
from app.utils.logger import get_logger
from app.resources.discovery import add_discovery_resource
from app.resources.system_resources import (
    CpuResource,
    MemoryResource,
    DiskResource,
    UptimeResource,
    TimeResource,
    HostnameResource,
)
from app.resources.environment_resources import (
    RandomTemperatureResource,
    RandomHumidityResource,
    RandomLightResource,
)
from app.resources.actuator_resources import (
    MessageActuatorResource,
    LogActuatorResource,
)
from app.services.environment_simulator import EnvironmentSimulator

logger = get_logger("server")

async def start_server():
    logger.info("Inicializando servidor CoAP '%s'...", NODE_NAME)

    root = resource.Site()
    simulator = EnvironmentSimulator()

    cpu_resource = CpuResource()
    temp_resource = RandomTemperatureResource(simulator)
    humidity_resource = RandomHumidityResource(simulator)
    light_resource = RandomLightResource(simulator)

    memory_resource = MemoryResource()
    disk_resource = DiskResource()
    uptime_resource = UptimeResource()
    time_resource = TimeResource()
    hostname_resource = HostnameResource()

    message_actuator = MessageActuatorResource()
    log_actuator = LogActuatorResource()

    root.add_resource(["system", "cpu"], cpu_resource)
    root.add_resource(["system", "memory"], memory_resource)
    root.add_resource(["system", "disk"], disk_resource)
    root.add_resource(["system", "uptime"], uptime_resource)
    root.add_resource(["system", "time"], time_resource)
    root.add_resource(["system", "hostname"], hostname_resource)

    root.add_resource(["environment", "random-temperature"], temp_resource)
    root.add_resource(["environment", "random-humidity"], humidity_resource)
    root.add_resource(["environment", "random-light"], light_resource)

    root.add_resource(["actuators", "message"], message_actuator)
    root.add_resource(["actuators", "log"], log_actuator)

    add_discovery_resource(root)

    await cpu_resource.start()
    await temp_resource.start()
    await humidity_resource.start()
    await light_resource.start()

    await aiocoap.Context.create_server_context(root, bind=(HOST, PORT))

    logger.info("Servidor CoAP ativo em coap://%s:%s", HOST, PORT)
    logger.info("Recursos principais registrados.")
    logger.info("Use Ctrl+C para encerrar.")

    await asyncio.get_running_loop().create_future()