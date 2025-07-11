
print("For utilizando lista")
lista = [1, 2, 3, 4, 5]
for i in lista:
    print(i)

print("\nFor utilizando tupla")
tupla = (1, 2, 3, 4, 5)
for i in tupla:
    print(i)

pessoa = {
    "nome": "Matheus",
    "idade": 22,
    "cidade": "Formosa"
}

print("\nFor utilizando dicionário pegando chaves")
for chave in pessoa.keys():
    print(chave)

print("\nFor utilizando dicionário pegando valores")
for valor in pessoa.values():
    print(valor)

print("\nFor utilizando dicionário pegando chaves e valores")
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# renge(): intervalo numero em forma de lista
print("\nFor utilizando range()")
for numero in range(5):
    print("Numero:", numero)

print("\nFor utilizando range() com len()")
lista = [1, 2, 3, 4, 5]
print(lista)
for indice in range(0, len(lista)):
    if indice == 3:
        lista[indice] = "Python"
    else:
        lista[indice] = "Java"
print(lista)

# Enumerate()
print("\nFor utilizando enumerate()")
lista_enumerate = ["a", "b", "c"]
for indice, valor in enumerate(lista_enumerate):
    print(f"{indice}: {valor}")
