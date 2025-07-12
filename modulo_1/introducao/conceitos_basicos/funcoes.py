# Exemplo

# Função sem retorno
def saudacao(nome):
    print(f"Olá, {nome}!")

nome = input("Qual é o seu nome? ")
saudacao(nome)

# Função com retorno
def quadrado(numero):
    resultado = numero ** 2
    return resultado

numero = int(input("\nDigite um número: "))
resultado = quadrado(numero)
print(f"O quadrado de {numero} é {resultado}")

# Função com multiplos parâmetros
def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

numero1 = int(input("\nDigite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
resultado_soma = soma(numero1, numero2)
print(f"A soma de {numero1} + {numero2} é {resultado_soma}")
