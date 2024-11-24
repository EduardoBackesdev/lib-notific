from src.notific import notific

a = notific()
a.addHours(["04:11"])
a.startSendNotificConstant()
a.persoConstantNotific("Nome janela", "titulo aqui", "descricao aqui")
a.startConstantNotific()

