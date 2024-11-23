from tkinter import *
from tkinter import ttk
from hours import hours
import threading

class constant(hours):
    @staticmethod
    # Metodo para definir a janela de notificacao
    # Importante, 
    def constant(self, nome_janela, titulo, descricao):
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

    @staticmethod
    def init():
        th = threading.Thread(target=constant.constant)
        th.start()


    