"""
Arquivo: app/utils/time_utils.py

Objetivo:
    Utilitários de data e hora.
"""

from datetime import datetime, timezone

def iso_now() -> str:
    return datetime.now(timezone.utc).astimezone().isoformat()