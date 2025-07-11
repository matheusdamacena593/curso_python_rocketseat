# Declaração
nome_completo = "Matheus Damacena"

nome_completo_aspas = """Matheus Damacena
Carvalho"""

nome_completo_quebra = "Matheus Damacena \
Carvalho"

nome = "Matheus"
sobrenome = "Damacena"

# Formatação
print("Nome completo (1° forma):", nome_completo)
print("Nome completo (2° forma):" + nome_completo)
print("Nome completo (3° forma):" + nome, sobrenome)
print("Nome completo (4° forma): %s" % nome_completo)
print(f"Nome completo (5° forma): {nome} {sobrenome}")
print("Nome completo (6° forma): {} {}".format(nome, sobrenome))

# Principais metodos para manipulação de strings
print(nome.upper())

print(nome.lower())

print(nome.count('a'))

print(nome.find('a'))

print(nome.encode())

print(nome.encode().decode())

print(nome.replace('a', 'b'))

print("-".join(nome))

print(nome_completo.split(" "))

nome_errado = "xMatheusx"
print(nome_errado.strip("x"))
print(nome_errado.rstrip("x"))

print(nome.startswith("Ma"))

print("the" in nome)

print("the" not in nome)