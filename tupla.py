# Criando uma tupla de exemplo (tuplas são imutáveis)
minha_tupla = (1, 2, 2, 3, 4)

print("Minha tupla:", minha_tupla)

print(minha_tupla[0])
print(minha_tupla[-1]) # Acessando o último elemento


# Método count
contagem = minha_tupla.count(2)
print("Quantidade de vezes que o elemento 2 aparece:", contagem)

indice = minha_tupla.index(3)
print("Indice da primeira ocorrência do elemento 3:", indice)