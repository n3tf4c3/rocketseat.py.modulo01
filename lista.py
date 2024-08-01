# Declaracao
minha_lista = [1, 2, 3, 4, 5, "rocketseat", True, False]
minha_lista2 = [5, 2, 4, 3, 1]
# Exibindo a lista
print("Minha lista de exemplo:", minha_lista)

# Exibindo os elementos
minha_lista[0] = "python"
print("Minha lista de exemplo[5]:", minha_lista[5])
print("Minha lista de exemplo[1:7]:", minha_lista[1:7])
print("Minha lista de exemplo[:6]:", minha_lista[:6])
print("Minha lista de exemplo[2:]:", minha_lista[2:])


# Método append(): Adiciona um elemento ao final da lista
minha_lista.append(6)
print("Após append(6):", minha_lista)

# Método index
indice = minha_lista.index(6)
print("Indice do elemento 6:", indice)

# Método insert: Insere um elemento em um índice específico
minha_lista.insert(2, 10)
print("Após o insert(2,10):", minha_lista)


# Método pop
elemento_removido = minha_lista.pop(2)
print("Elemento removido:", elemento_removido)

#Método remove
minha_lista.remove(True)
print("Após remove(True):", minha_lista)

#Método sort
minha_lista2.sort()
print("Após sort()", minha_lista2)