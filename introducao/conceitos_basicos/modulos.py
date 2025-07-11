print("Exemplos de importação de um módulo padrão:")
# import math
from math import sqrt

numero = int(input("Digite um número para calcular a raiz quadrada: "))
raiz_quadrada = sqrt(numero)
print(f"A raiz quadrada de {numero} é: {raiz_quadrada}")

print("\nExemplo de criação e utilização de um módulo personalizado:")
from meu_modulo import saudacao, dobro

mensagem = saudacao("Pythonista")
resultado_dobro = dobro(5)

print(mensagem)
print(f"O dobro de 5 é: {resultado_dobro}")
