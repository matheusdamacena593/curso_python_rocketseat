print("Exemplo de captura de exceções")

try:
    numero = int(input("Digite um número inteiro: "))
    resultado = 10 / numero
    
except ValueError as ve:
    print(f"Erro de value error: {ve}")
    raise ValueError("Tipo de variaveis incompatíveis.")
except Exception as e:
    print("Erro:", e)
else:
    print("Resultado da divisão:", resultado)
finally:
    print("Operação Finalizada.")
