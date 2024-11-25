tarefas = [] 

def adicionar_tarefa(tarefas):
    nome = input("Digite o nome da tarefa: ")
    descricao = input("Digite a descrição da tarefa: ")
    prioridade = input("Digite a prioridade da tarefa (Alta, Média, Baixa): ")
    
    

    nova_tarefa = {
        "nome": nome,
        "descricao": descricao,
        "prioridade": prioridade
        
        
    }

    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!\n")

def exibir_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada. \n")
    else:
        for i, tarefa in enumerate(tarefas, 1):
            print(f'tarefa {i}: ')
            print(f' Nome: {tarefa["nome"]}')
            print(f' Descrição: {tarefa["descricao"]}') 
            print(f'  Prioridade: {tarefa["prioridade"]}\n')
           

def menu():
    while True:
        print("Menu de Interação")
        print("1. Adicionar uma nova tarefa")
        print("2. Exibir todas as tarefas")
        print("3. Sair")

        escolha = input("Escolha uma opção (1/2/3): ")
        if escolha == "1":
            adicionar_tarefa(tarefas)
        elif escolha == "2":
            exibir_tarefas(tarefas)
        elif escolha == "3":
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida, tente novamente. \n")
menu()
      