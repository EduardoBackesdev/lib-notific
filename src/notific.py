from src.simple import simpleNotific
from src.constant import constant
from src.hours import hours

# Metodo principal
class notific(simpleNotific, constant, hours):
    # ---------------------METODOS AUXILIARES--------------------- #

    
    def addHours(self, horas):
        """ Metodo de classe principal para setar horas para notificação constante """
        self.h = horas
        print(self.h)
        hours.__init__(self, self.h)

    def startSendNotificConstant(self):
        """ Metodo de classe principal para iniciar as notificações """
        hours.starThreadHours(self)   

    # ---------------------METODOS NOTIFICAÇÕES--------------------- #

    def startSimpleNotific(self, nome_janela, titulo, descricao):
        """ Metodo de classe principal para iniciar norificacao simples """
        self.nj = nome_janela
        self.t = titulo
        self.d = descricao
        self.initSimple(self.nj, self.t, self.d)

    def persoConstantNotific(self, nome_janela, titulo, descricao):
        """ Metodo de classe principal para personalizar notificação constante """
        self.nj = nome_janela
        self.t = titulo
        self.d = descricao
        self.constantNotific(self.nj, self.t, self.d)

    def startConstantNotific(self):
        """ Metodo de classe principal para iniciar notificação constante """
        self.startThreadConstant()   


