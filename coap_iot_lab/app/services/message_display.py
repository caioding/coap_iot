"""
Arquivo: app/services/message_display.py

Objetivo:
    Exibir uma mensagem localmente na tela do computador, quando possível.

Observação:
    Usa tkinter, se disponível. Caso falhe, apenas registra no log.
"""

import threading
from app.utils.logger import get_logger

logger = get_logger("message_display")

def _show_tk_message(title: str, message: str):
    try:
        import tkinter as tk

        def worker():
            root = tk.Tk()
            root.title(title)
            root.geometry("420x180")
            root.attributes("-topmost", True)

            label = tk.Label(
                root,
                text=message,
                wraplength=380,
                justify="center",
                font=("Arial", 12)
            )
            label.pack(expand=True, fill="both", padx=20, pady=20)

            button = tk.Button(root, text="Fechar", command=root.destroy)
            button.pack(pady=10)

            root.mainloop()

        threading.Thread(target=worker, daemon=True).start()
        return True, "Mensagem exibida em janela local."
    except Exception as exc:
        logger.exception("Falha ao exibir mensagem na tela.")
        return False, f"Não foi possível abrir janela local: {exc}"

def show_message(title: str, message: str) -> tuple[bool, str]:
    logger.info("Mensagem recebida para exibição | title=%s | message=%s", title, message)
    return _show_tk_message(title, message)