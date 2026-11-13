
class Leitor:
    def __init__(self, nome):
        self.nome = nome
        self.perfil = "comum"

    def pode_emprestar(self):
        return True

class LeitorPremium(Leitor):
    def __init__(self, nome):
        super().__init__(nome)
        self.perfil = "premium"

    def pode_emprestar(self):
        return True

def leitor_do_tipo(tipo, nome):
    classes = {"comum": Leitor, "premium": LeitorPremium}
    return classes[tipo](nome)
