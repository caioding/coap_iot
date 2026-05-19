"""
Arquivo: app/resources/environment_resources.py

Objetivo:
    Definir recursos CoAP de sensores simulados.
"""

from app.resources.base_resource import ObservableJsonResource
from app.services.environment_simulator import EnvironmentSimulator
from app.config import ENVIRONMENT_OBSERVE_INTERVAL_SECONDS

class RandomTemperatureResource(ObservableJsonResource):
    def __init__(self, simulator: EnvironmentSimulator):
        super().__init__(
            producer=simulator.get_temperature,
            interval_seconds=ENVIRONMENT_OBSERVE_INTERVAL_SECONDS,
            title="Temperatura simulada",
            rt="sensor-temperature"
        )

class RandomHumidityResource(ObservableJsonResource):
    def __init__(self, simulator: EnvironmentSimulator):
        super().__init__(
            producer=simulator.get_humidity,
            interval_seconds=ENVIRONMENT_OBSERVE_INTERVAL_SECONDS,
            title="Umidade simulada",
            rt="sensor-humidity"
        )

class RandomLightResource(ObservableJsonResource):
    def __init__(self, simulator: EnvironmentSimulator):
        super().__init__(
            producer=simulator.get_light,
            interval_seconds=ENVIRONMENT_OBSERVE_INTERVAL_SECONDS,
            title="Luminosidade simulada",
            rt="sensor-light"
        )