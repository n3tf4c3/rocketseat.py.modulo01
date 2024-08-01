def adicionar_contato(contatos, nome_contato, telefones, telefone_contato, emails, email_contato):
  contato = {"contato": nome_contato, "favorita": False}
  contatos.append(contato)
  print(f"Contato {nome_contato} foi adicionado com sucesso!")
  telefone = {"telefone": telefone_contato, "favorita": False}
  telefones.append(telefone)
  print(f"Telefone {telefone_contato} foi adicionado com sucesso!")
  email = {"email": email_contato, "favorita": False}
  emails.append(email)
  print(f"Email {email_contato} foi adicionado com sucesso!")
  return

def ver_contatos(contatos, telefones, emails):
  print("\nLista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    status = "✓" if contato["favorita"] else " "
    nome_contato = contato["contato"]
    nome_telefone = telefones[indice - 1]["telefone"]
    nome_email = emails[indice - 1]["email"]
    print(f"{indice}. [{status}] {nome_contato} {nome_telefone} {nome_email}")
  return

def editar_contato(contatos, indice_contato, novo_nome_contato):
  indice_contato_editado = int(indice_contato) - 1
  if indice_contato_editado >= 0 and indice_contato_editado < len(contatos):
    contatos[indice_contatos_editado]["contato"] = novo_nome_contato
    print(f"Contato {indice_contato} atualizada para {novo_nome_contato}")
  else:
    print("Índice de contato inválido")
  return

contatos = []
telefones = []
emails = []
while True:
  print("\n==@==Gerenciador de contatos==@==")
  print("1. Adicionar contato")
  print("2. Ver contato")
  print("3. Editar contato")
  print("4. Deletar contato")
  print("5. Marcar contato favorito")
  print("6. Sair")

  escolha = input("Digite a sua escolha: ")

  if escolha == "1":
    nome_contato = input("Digite o nome do contato que deseja adicionar: ")
    telefone_contato = input("Digite o telefone do contato que deseja adicionar: ")
    email_contato = input("Digite o email do contato que deseja adicionar: ")
    adicionar_contato(contatos, nome_contato, telefones, telefone_contato, emails, email_contato)
  elif escolha == "2":
    ver_contatos(contatos, telefones, emails)
  elif escolha == "3":
    editar_contato(contatos)
  """elif escolha == "3":
    deletar_contato(contatos)
    indice_contatos = input("Digite deletar o contato: ")
    novo_nome = input("Digite o novo nome da tarefa: ")
    atualizar_nome_contato(contatos, indice_contatos, novo_contato)
  elif escolha == "4":
    ver_tarefas(contatos)
    indice_tarefa = input("Digite o número do contato que deseja no favoritos: ")
    completar_contato(contatos, indice_contatos)
  elif escolha =="5":
    deletar_contato_completados(contatos)
    ver_tarefas(contatos)
  elif escolha == "6":
    break"""
