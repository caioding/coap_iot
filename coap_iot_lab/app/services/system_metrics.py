"""
Arquivo: app/services/system_metrics.py

Objetivo:
    Coletar métricas locais do sistema operacional.
"""

import os
import platform
import socket
import time
import psutil

from app.utils.time_utils import iso_now

BOOT_TIME = psutil.boot_time()

def get_cpu_data() -> dict:
    return {
        "resource": "cpu",
        "value": psutil.cpu_percent(interval=0.2),
        "unit": "%",
        "cores_logical": psutil.cpu_count(logical=True),
        "cores_physical": psutil.cpu_count(logical=False),
        "timestamp": iso_now(),
    }

def get_memory_data() -> dict:
    mem = psutil.virtual_memory()
    return {
        "resource": "memory",
        "total_mb": round(mem.total / (1024 * 1024), 2),
        "used_mb": round(mem.used / (1024 * 1024), 2),
        "available_mb": round(mem.available / (1024 * 1024), 2),
        "percent": mem.percent,
        "timestamp": iso_now(),
    }

def get_disk_data() -> dict:
    disk = psutil.disk_usage(os.path.abspath(os.sep))
    return {
        "resource": "disk",
        "total_gb": round(disk.total / (1024**3), 2),
        "used_gb": round(disk.used / (1024**3), 2),
        "free_gb": round(disk.free / (1024**3), 2),
        "percent": disk.percent,
        "timestamp": iso_now(),
    }

def get_uptime_data() -> dict:
    uptime_seconds = time.time() - BOOT_TIME
    return {
        "resource": "uptime",
        "uptime_seconds": int(uptime_seconds),
        "uptime_minutes": round(uptime_seconds / 60, 2),
        "timestamp": iso_now(),
    }

def get_time_data() -> dict:
    return {
        "resource": "time",
        "local_time": iso_now(),
        "timestamp": iso_now(),
    }

def get_hostname_data() -> dict:
    return {
        "resource": "hostname",
        "hostname": socket.gethostname(),
        "platform": platform.platform(),
        "timestamp": iso_now(),
    }