tarefas = []

# adicionar uma tarefa à lista
def adicionar_tarefa():
    tarefa = input("Digite a tarefa que você deseja adicionar: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

# listar as tarefas
def listar_tarefas():
    print("Lista de tarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa}")

# remover uma tarefa 
def remover_tarefa():
    listar_tarefas()
    indice = int(input("Digite o número da tarefa que você deseja remover: "))
    if indice < 1 or indice > len(tarefas):
        print("Número de tarefa inválido.")
    else:
        tarefa_removida = tarefas.pop(indice - 1)
        print(f"Tarefa '{tarefa_removida}' removida com sucesso!")

# Menu
while True:
    print("\nO que você deseja fazer?")
    print("1. Adicionar uma tarefa")
    print("2. Listar as tarefas")
    print("3. Remover uma tarefa")
    print("4. Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        adicionar_tarefa()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        remover_tarefa()
    elif opcao == 4:
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
