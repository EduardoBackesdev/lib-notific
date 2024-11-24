from tkinter import *
from tkinter import ttk
from src.hours import hours
import queue
import threading

# Classe para uma notificação de forma constante
# Implementa classe hours para definir as horas de notificação
# E iniciar a thread de comunicaçao com classe constant
class constant:
    def __init__(self):
          self.running = False
          self.fila = None

    # Metodo para definir a janela de notificacao
    def constantNotific(self, nome_janela, titulo, descricao):
            if self.running and self.fila.get():
                root = Tk()
                root.title(nome_janela)
                altura = 500
                largura = 500
                w = root.winfo_screenmmwidth()
                h = root.winfo_screenheight()
                x = (w // 2) - (largura // 2)
                y = (h // 2) - (altura // 2)
                root.geometry(f"{altura}x{largura}+{x}+{y}")
                mainframe = ttk.Frame(root, padding="3 3 12 12")
                mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
                root.columnconfigure(0, weight=1)
                root.rowconfigure(0, weight=1)
                ttk.Label(mainframe, text=titulo, font=50).grid(column=0, row=1, sticky="nsew")
                ttk.Label(mainframe, text=descricao).grid(column=0, row=2, sticky="")
                root.mainloop()

    # Metodo que inicia a Thread
    def startThreadConstant(self):
          self.running = True
          self.fila = queue.Queue()
          thread = threading.Thread(target=self.constantNotific, args=(self.fila,))
          thread.start()
        


    