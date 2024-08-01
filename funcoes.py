# Exemplo
def saudacao(nome):
  print(f"Olá, {nome}!")

print("\n Chamando a função saudação")
saudacao("Alice")
saudacao("Bob")

# Funcao com retorno
def quadrado(numero):
  resultado = numero ** 2
  return resultado

print("\nChamando função quadrado")
resultado_quadrado = quadrado(7)
print("Resultado da funcao quadrado:", resultado_quadrado)

# Funcao om multiplos parametros
def soma(numero1, numero2):
  resultado = numero1 + numero2
  return resultado

numero1 = 20
numero2 = 50
print("\Chamando a função soma:")
resultado_soma = soma(numero1, numero2)
print("A soma do numero %s e o numero %s é %s" % (numero1, numero2, resultado_soma))