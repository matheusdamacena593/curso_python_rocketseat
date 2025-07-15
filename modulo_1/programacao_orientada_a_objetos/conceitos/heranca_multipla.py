class Animal():
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando."
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando."
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Sou Bilionário."
    
morcego = Morcego(nome="Batman")

# Acessando métodos da classe base "Animal"
print("Nome do Morcego:", morcego.nome)
print("Som do morcego:", morcego.emitir_som())

# Acessando métodos das classe "Mamifero" e "Ave"
print("Morcego Amamentando:", morcego.amamentar())
print("Morcego Voando:", morcego.voar())
