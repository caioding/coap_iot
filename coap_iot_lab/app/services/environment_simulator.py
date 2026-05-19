"""
Arquivo: app/services/environment_simulator.py

Objetivo:
    Gerar leituras simuladas de sensores ambientais.
"""

import random
from app.utils.time_utils import iso_now

class EnvironmentSimulator:
    def __init__(self):
        self.temperature = 24.0
        self.humidity = 55.0
        self.light = 420.0

    def _walk(self, value: float, step: float, min_value: float, max_value: float) -> float:
        value += random.uniform(-step, step)
        return max(min_value, min(max_value, value))

    def get_temperature(self) -> dict:
        self.temperature = self._walk(self.temperature, 0.7, 18.0, 35.0)
        return {
            "resource": "random-temperature",
            "value": round(self.temperature, 2),
            "unit": "°C",
            "timestamp": iso_now(),
        }

    def get_humidity(self) -> dict:
        self.humidity = self._walk(self.humidity, 2.5, 30.0, 90.0)
        return {
            "resource": "random-humidity",
            "value": round(self.humidity, 2),
            "unit": "%",
            "timestamp": iso_now(),
        }

    def get_light(self) -> dict:
        self.light = self._walk(self.light, 35.0, 100.0, 900.0)
        return {
            "resource": "random-light",
            "value": round(self.light, 2),
            "unit": "lux",
            "timestamp": iso_now(),
        }