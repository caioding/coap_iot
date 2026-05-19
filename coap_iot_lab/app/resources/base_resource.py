"""
Arquivo: app/resources/base_resource.py

Objetivo:
    Classes base para recursos JSON simples e observáveis.
"""

import asyncio
from typing import Callable, Awaitable, Optional

import aiocoap
import aiocoap.resource as resource
from aiocoap.numbers.contentformat import ContentFormat

from app.utils.json_encoder import to_json_bytes

class JsonResource(resource.Resource):
    def __init__(self, title: str = "", rt: str = ""):
        super().__init__()
        self.title = title
        self.rt = rt

    def get_link_description(self):
        data = {}
        if self.title:
            data["title"] = self.title
        if self.rt:
            data["rt"] = self.rt
        return data

    def json_response(self, payload: dict) -> aiocoap.Message:
        return aiocoap.Message(
            payload=to_json_bytes(payload),
            content_format=ContentFormat.JSON
        )

class ObservableJsonResource(resource.ObservableResource):
    def __init__(
        self,
        producer: Callable[[], dict],
        interval_seconds: float,
        title: str = "",
        rt: str = ""
    ):
        super().__init__()
        self.producer = producer
        self.interval_seconds = interval_seconds
        self.title = title
        self.rt = rt
        self.current_payload = self.producer()
        self._task: Optional[asyncio.Task] = None

    def get_link_description(self):
        data = {}
        if self.title:
            data["title"] = self.title
        if self.rt:
            data["rt"] = self.rt
        return data

    async def start(self):
        if self._task is None:
            self._task = asyncio.create_task(self._observe_loop())

    async def _observe_loop(self):
        while True:
            await asyncio.sleep(self.interval_seconds)
            self.current_payload = self.producer()
            self.updated_state()

    async def render_get(self, request):
        return aiocoap.Message(
            payload=to_json_bytes(self.current_payload),
            content_format=ContentFormat.JSON
        )