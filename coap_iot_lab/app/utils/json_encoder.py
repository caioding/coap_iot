"""
Arquivo: app/utils/json_encoder.py

Objetivo:
    Converter objetos Python em bytes JSON UTF-8.
"""

import json

def to_json_bytes(data: dict) -> bytes:
    return json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")