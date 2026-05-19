"""
Arquivo: run_server.py

Objetivo:
    Ponto de entrada do servidor CoAP da prática.

Responsabilidades:
    - carregar a configuração principal
    - iniciar o servidor CoAP
    - manter o loop assíncrono em execução
"""

import asyncio
from app.server import start_server

if __name__ == "__main__":
    asyncio.run(start_server())