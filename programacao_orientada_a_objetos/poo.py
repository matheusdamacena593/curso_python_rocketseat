# POO

# Classe exemplo
class Pessoa:
    # Construtor
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def saudacao(self):
        return f"Olá, meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos
pessoa1 = Pessoa("Matheus", 22)
mensagem1 = pessoa1.saudacao()
print(mensagem1)

pessoa2 = Pessoa("Lananda", 22)
mensagem2 = pessoa2.saudacao()
print(mensagem2)
