import time
import threading
import queue

class hours:
    # Construtor para iniciar a thread fechada
    def __init__(self, h):
        self.horas = h
        self.running = False
        self.fila = None

    # Metodo que verifica a hora atual
    def sendNotific(self, fila):
        a = 1
        while a != 0:
            time.sleep(1)
            hora = time.localtime()
            formated_hora = time.strftime("%H:%M", hora)
            for i in self.horas:
                if i == formated_hora:
                    mes = "MANDANDO MENSAGEM"
                    fila.put(mes)

    # Metodo que inicia a Thread
    def star(self):
        self.running = True
        self.fila = queue.Queue()
        startT = threading.Thread(target=self.setHours, )
        startT.start()







        

        
        