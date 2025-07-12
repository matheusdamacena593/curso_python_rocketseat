# Herança
print("\nExeplo de herença: ")
class Animal:
    def __init__(self, nome):
        self.nome = nome # Atributo Público

    def andar(self):
        print(f"O animal {self.nome} andou")
        return
    
    def emitir_som(self):
        pass

#Herança - Uma classe filha herda atributos e métodos da classe mãe
class Cachorro(Animal):
    # Polimorfismo - Reimplementar métodos de uma classe mãe na classe filha
    def emitir_som(self):
        return "Au, au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau!"
    
dog = Cachorro("Rex")
cat = Gato("Gamora")

print("\nExemplo de Polimorfismo:")
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")

print("\nExemplo de Encapsulamento:")
class ContaBancaria:
    def __init__(self, saldo) -> None:
        self.__saldo = saldo # Atributo Privado

    # Para privar atributos e metodos comece com __
    
    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor

    def consultar_saldo(self):
        return self.__saldo
    

conta = ContaBancaria(saldo=1000)

print(f"Saldo na conta: {conta.consultar_saldo()}")
conta.depositar(valor=1000)
print(f"Saldo na conta: {conta.consultar_saldo()}")
conta.sacar(valor=200)
print(f"Saldo na conta: {conta.consultar_saldo()}")

conta_do_zezinho = ContaBancaria(saldo=50)

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):

    @abstractmethod # Decorador
    def ligar(self):
        pass

    @abstractmethod # Decorador
    def desligar(self):
        pass

class Carro(Veiculo):
    def __init__(self) -> None:
        pass

    def ligar(self):
        return "Carro ligado usando a chave"
    
    def desligar(self):
        return "Carro desligado usando a chave"

volvo = Carro()

print(volvo.ligar())
print(volvo.desligar())
