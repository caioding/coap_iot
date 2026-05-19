"""
Arquivo: app/config.py

Objetivo:
    Centralizar as configurações do servidor.
"""

# troque pelo IP que irá hospedar o servidor
HOST = "192.168.0.5"
PORT = 5683
NODE_NAME = "coap-iot-lab-node"

CPU_OBSERVE_INTERVAL_SECONDS = 2.0
ENVIRONMENT_OBSERVE_INTERVAL_SECONDS = 3.0

LOG_FILE = "logs/server.log"
ENABLE_TK_MESSAGE_WINDOW = True