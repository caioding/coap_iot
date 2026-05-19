"""
Arquivo: app/services/notifier.py

Objetivo:
    Serviços auxiliares de atuação local.

Neste projeto, este módulo é usado para registrar mensagens
recebidas remotamente no log local do servidor.
"""

from app.utils.logger import get_logger

logger = get_logger("notifier")

def write_local_log(message: str) -> tuple[bool, str]:
    logger.info("LOG REMOTO | %s", message)
    return True, "Mensagem registrada no log local."