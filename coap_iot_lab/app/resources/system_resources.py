"""
Arquivo: app/resources/system_resources.py

Objetivo:
    Definir os recursos CoAP relacionados a métricas reais do sistema.
"""

from app.resources.base_resource import JsonResource, ObservableJsonResource
from app.services.system_metrics import (
    get_cpu_data,
    get_memory_data,
    get_disk_data,
    get_uptime_data,
    get_time_data,
    get_hostname_data,
)
from app.config import CPU_OBSERVE_INTERVAL_SECONDS

class CpuResource(ObservableJsonResource):
    def __init__(self):
        super().__init__(
            producer=get_cpu_data,
            interval_seconds=CPU_OBSERVE_INTERVAL_SECONDS,
            title="Uso de CPU",
            rt="sensor-cpu"
        )

class MemoryResource(JsonResource):
    def __init__(self):
        super().__init__(title="Uso de memória", rt="sensor-memory")

    async def render_get(self, request):
        return self.json_response(get_memory_data())

class DiskResource(JsonResource):
    def __init__(self):
        super().__init__(title="Uso de disco", rt="sensor-disk")

    async def render_get(self, request):
        return self.json_response(get_disk_data())

class UptimeResource(JsonResource):
    def __init__(self):
        super().__init__(title="Tempo ligado", rt="sensor-uptime")

    async def render_get(self, request):
        return self.json_response(get_uptime_data())

class TimeResource(JsonResource):
    def __init__(self):
        super().__init__(title="Hora local", rt="sensor-time")

    async def render_get(self, request):
        return self.json_response(get_time_data())

class HostnameResource(JsonResource):
    def __init__(self):
        super().__init__(title="Hostname", rt="sensor-hostname")

    async def render_get(self, request):
        return self.json_response(get_hostname_data())