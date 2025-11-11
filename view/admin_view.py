from services.task_services import create_task, list_task, delete_task, update_task

def panel(user_auth):
    while True:
        print(f"Bem vindo: {user_auth[1]}")
        print("1 - Cadastrar Task \n2 - Listar Task \n3 - Remover Task \n4 - Atualizar Task \n5 - Deslogar") #buscar Task

        opcao = int(input("Digite a opção: "))

        if(opcao == 1):
            title = input("Digite o titulo da tarefa: ")
            create_task(user_auth[0], title)
        elif(opcao == 2):
            tasks = list_task(user_auth[0])
            for task in tasks:
                print(f"Tasks {task[0]} - {task[1]}")
        elif(opcao == 3):
            id_tasks = int(input("Qual o id da task que você quer deletar: "))
            delete_task(user_auth[0], id_tasks)
        elif(opcao == 4):
            id_tasks = int(input("Qual o id da task que você quer atualizar: "))
            novo_title = input("Digite o novo titulo da task: ")
            update_task(user_auth[0], id_tasks, novo_title)
        elif(opcao == 5):
            break
        else:
            print("Digite uma opção valida!")
