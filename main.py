from src.notific import notific

a = notific("nome janela", "titulo da janela", "descricao da janela")
a.addHours(["21:30","21:31"])
a.startSendNotificConstant()
a.persoConstantNotific()
a.startConstantNotific()

