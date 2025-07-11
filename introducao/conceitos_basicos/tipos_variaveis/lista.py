# Declaracao

minha_lista = [1, 2, 3, 4, 5, 3.14]

# Exibindo a lista
print("Minha lista de exemplo", minha_lista)

# Exibindo valores individuais
print("Elemento", minha_lista[5])

# Mudando valores
# minha_lista[0] = "python"
print("Minha lista alterada", minha_lista)

# Fatiar a lista
print("Fatiando a lista", minha_lista[1:7]) # sempre adicionar 1 elemento a mais
print("Fatiando até o alvo:", minha_lista[:6])
print("Começando do alvo:", minha_lista[3:])

# Adicionar elementos append()
minha_lista.append(6)
print("Utilizando append:", minha_lista)

# Metodo index()
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Metodo insert(): insere um elemento em um indice específico
minha_lista.insert(2, 10)
print("Utilizando insert:", minha_lista)

# Medoto pop()
elemento_removido = minha_lista.pop(3)
print("Elemento removido:", elemento_removido)
print("Lista após pop:", minha_lista)

# metodo remove()
minha_lista.remove(True)
print("Lista após remove:", minha_lista)

# Metodo sort():: ordena lista em ordem crescente
minha_lista.sort()
print("Lista ordenada:", minha_lista)
