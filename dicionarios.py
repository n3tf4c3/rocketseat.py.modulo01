# Criando um dicionário de exemplo
pessoa = {"nome": "Joao", "idade": 30, "cidade": "São Paulo"}

# Exibindo  o dicionário
print("Meu dicionário de exemplo:", pessoa)

# Acessando valores por chaves
print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
pessoa["sobrenome"] = "Silva"
print("Sobrenome:", pessoa["sobrenome"])
print("Cidade:", pessoa["cidade"])


pessoa["idade"] = 31
print("Idade:", pessoa["idade"])

pessoa["idade"] = 31
print("Idade:", pessoa["idade"])


# Removendo um par chave-valor

del pessoa["sobrenome"]
print("Meu dicionário de exemplo:", pessoa)

# Métodos: keys(), values(), items()

chaves = list(pessoa.keys())
print("Chaves do dicionário:", chaves)
print()

valores = list(pessoa.values())
print("Valores do dicionário:", valores)
print("Valores do dicionário:", valores[0])

# Métodos items
itens = list(pessoa.items())
print("Pares chave-valor do dicionário:", itens)
print("Primeiro chave-valor: %s = %s" % (itens [0][0], itens[0][1]))