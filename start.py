# ESTE CRUD DEVE SER SIMPLES, ENTAO NAO HA NECESSIDADE DE USAR UM BANCO DE DADOS.
# VOU CONSTRUIR USANDO UM ARQUIVO CSV.
# COMO MODELO DE TRABALHO, VOU USAR O CONCEITO DE ESTACOES DE TRABALHO, WORKSTATIONS(WS).
# CABECALHO: (WS_ID, WS_NAME,         CITY, WORKERS) 
# EXEMPLO  : (    1, MOINHOS, PORTO ALEGRE,      33)

def adicionar():
  print("Chama método ADICIONAR")

def editar():
  print("Chama método EDITAR")

def visualizar():
  print("Chama método VISUALIZAR")

def visualizarUmRegistro():
  print("Chama método VISUALIZAR UM SOMENTE")

def deletar():
  print("Chama método DELETAR")

loopAtivo = True

while loopAtivo:
  print("\n\nDigite a opção desejada: \n",
        "A - Adicionar\n",
        "E - Editar\n",
        "V - Visualizar tudo\n",
        "U - Visualizar Um\n",
        "D - Deletar\n",
        "S - Sair")
  opcao = input()

  # DESCOBRIR COMO FAZER A LEITURA DE UM CSV

  if opcao == "A" or opcao == "a":
    adicionar()

  elif opcao == "E" or opcao == "e":
    editar()

  elif opcao == "V" or opcao == "v":
    visualizar()

  elif opcao == "U" or opcao == "u":
    visualizarUmRegistro()

  elif opcao == "D" or opcao == "d":
    deletar()

  elif opcao == "S" or opcao == "s":
    print("Saindo. . . ")
    loopAtivo = False

  else:
    print("Opção incorreta, digite novamente.\n\n")
