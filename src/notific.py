from src.simple import simpleNotific
from src.constant import constant
from src.hours import hours

# Metodo principal
class notific(simpleNotific, constant, hours):

    # Metododo construtor para classe notific, seta nome da janela, titulo e descricao da notificação
    def __init__(self, nome_janela, titulo, descricao):
        self.nj = nome_janela
        self.t = titulo
        self.d = descricao

    # ---------------------METODOS AUXILIARES--------------------- #
    def addHours(self, horas):
        """ Metodo de classe principal para setar horas para notificação constante """
        self.h = horas
        hours.__init__(self, self.h)

    def startSendNotificConstant(self):
        """ Metodo de classe principal para iniciar as notificações """
        hours.starThreadHours(self)   

    # ---------------------METODOS NOTIFICAÇÕES--------------------- #
    def startSimpleNotific(self):
        """ Metodo de classe principal para iniciar norificacao simples """
        self.initSimple(self.nj, self.t, self.d)

    def persoConstantNotific(self):
        """ Metodo de classe principal para personalizar notificação constante """
        self.constantNotific(self.nj, self.t, self.d)

    def startConstantNotific(self):
        """ Metodo de classe principal para iniciar notificação constante """
        self.startThreadConstant()   


