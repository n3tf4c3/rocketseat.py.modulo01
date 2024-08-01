# if, elif e else

# Exemplo de "if"
idade = int(input("Quantos anos você tem? "))
print("Exemplo de comando if")
if idade >= 18:
    print("Você é maior de idade.")
elif idade >= 12:
    print("Você é um adolescente")
else:
    print("Você é menor de idade.")

mensagem = "Pode tirar a carteira" if idade >= 18 else "Não pode tirar a carteira"
print(mensagem)
