"""
Arquivo: app/resources/actuator_resources.py

Objetivo:
    Definir recursos CoAP que executam ações locais no computador.
"""

import json

from app.resources.base_resource import JsonResource
from app.services.message_display import show_message
from app.services.notifier import write_local_log
from app.utils.time_utils import iso_now

class MessageActuatorResource(JsonResource):
    def __init__(self):
        super().__init__(title="Exibir mensagem", rt="actuator-message")

    async def render_post(self, request):
        try:
            body = json.loads(request.payload.decode("utf-8"))
            title = body.get("title", "Mensagem CoAP")
            message = body.get("message", "")
            success, detail = show_message(title=title, message=message)

            response = {
                "resource": "message",
                "success": success,
                "detail": detail,
                "timestamp": iso_now(),
            }
            return self.json_response(response)
        except Exception as exc:
            response = {
                "resource": "message",
                "success": False,
                "detail": f"Payload inválido: {exc}",
                "timestamp": iso_now(),
            }
            return self.json_response(response)

class LogActuatorResource(JsonResource):
    def __init__(self):
        super().__init__(title="Registrar log", rt="actuator-log")

    async def render_post(self, request):
        try:
            body = json.loads(request.payload.decode("utf-8"))
            message = body.get("message", "")
            success, detail = write_local_log(message)

            response = {
                "resource": "log",
                "success": success,
                "detail": detail,
                "timestamp": iso_now(),
            }
            return self.json_response(response)
        except Exception as exc:
            response = {
                "resource": "log",
                "success": False,
                "detail": f"Payload inválido: {exc}",
                "timestamp": iso_now(),
            }
            return self.json_response(response)