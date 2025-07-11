# Coleção não ordenada de pares chave-valor

# Criando um dicionário de exemplo
pessoa = {
    "nome": "Matheus",
    "idade": 22,
    "cidade": "Formosa"
}

print("Meu dicionário:", pessoa)

# Acessando valores por chave
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])

pessoa["sobrenome"] = "Damacena"
print("Sobrenome:", pessoa["sobrenome"])

print("Meu dicionário:", pessoa)

pessoa["idade"] = 23
print("Idade:", pessoa["idade"])

# Removendo um par chave-valor
del pessoa["sobrenome"]

print("Meu dicionário:", pessoa)

# Metodos:: keys(), values(), items()
chaves = list(pessoa.keys())
print("chaves do dicionário:", chaves)
print("Primeira chave:", chaves[0])

# Metodo values()
valores = list(pessoa.values())
print("valores do dicionário:", valores)
print("Primeiro valor:", valores[0])

# Metodo items()
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro par chave-valor: %s = %s" % (itens[0][0], itens[0][1])) 
