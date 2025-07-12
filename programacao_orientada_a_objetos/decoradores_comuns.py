# @classmethod
# @staticmethod

class MinhaClasse:
    valor = 10 # Atributo de Classe

    def __init__(self, nome):
        self.nome = nome # Atributo de instância

    # Requer uma instância para ser chamado
    def metodo_instancia(self):
        return f"Método de instância chamado para {self.nome}"
    
    @classmethod
    def metodo_classe(cls):
        return f"Método da classe chamado para valor={cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Método estático sendo chamado"

    
obj = MinhaClasse(nome="Classe Exemplo")
print(obj.metodo_instancia())
# Metodo da classe
print(MinhaClasse.metodo_classe())
# Metodo estatico
print(MinhaClasse.metodo_estatico())

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, ano)
    
configuracao1 = "Toyota,Corolla,2022"
carro1 = Carro.criar_carro(configuracao1)
print(f"\nMarca: {carro1.marca}\nModelo: {carro1.modelo}\nAno: {carro1.ano}")

class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b

print(Matematica.somar(a=10, b=15))
