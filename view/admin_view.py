import time, os

from services.agendamento_services import agendar_gravacao, listar_agendamentos, atualizar_agendamento, deletar_agendamento

def panel(user_auth):
    while True:
        print("========|TELA INICIAL|=======")
        print(f"Bem vindo: {user_auth[1]} \n\n >Escolha uma opção<\n")
        print("1 - Agendar gravação \n2 - Meus agendamentos \n3 - Atualizar agendamento \n4 - Remover agendamento \n5 - Deslogar") #buscar Task

        opcao = int(input("Digite a opção: "))
        os.system('cls')

        if(opcao == 1):
            data_gravacao = input("\nDigite a data de gravação: ")
            horario_gravacao = input("Qual o horario da gravação: ")
            qtd_videos = input("Qual a quantidade de videos: ")
            local_gravacao = input("Qual o local da gravação: ")
            video_aereo = input("Quantidade de videos aéreos: ")
            agendar_gravacao(user_auth[0], data_gravacao, horario_gravacao, qtd_videos, local_gravacao, video_aereo)

        elif(opcao == 2):
            os.system('cls')
            agendamentos = listar_agendamentos(user_auth[0])
            for agendamento in agendamentos:
                print(f"\nAgendamento - {agendamento[0]} \nData_gravacao: {agendamento[1]} \nHorario_gravacao: {agendamento[2]} \nQtd_videos: {agendamento[3]} \nLocal_gravacao: {agendamento[4]} \nQtd de aéreos: {agendamento[5]} \n----------------------")
            time.sleep(2.5)

        elif(opcao == 3):
            print("========|SEUS AGENDAMENTOS|=======\n")
            agendamentos = listar_agendamentos(user_auth[0])
            for agendamento in agendamentos:
                print(f"Agendamento - {agendamento[0]}")

            agendamento_id = int(input("Qual o id do agendamento que você quer atualizar: "))
            
            campos = ['data_gravacao', 'horario_gravacao', 'qtd_videos', 'local_gravacao', 'video_aereo']
            
            print("\n Escolha uma opção para atualizar:")
            for i, campo in enumerate(campos, 1):
                print(f"{i} - {campo}")

            opcao_atualizar = int(input("\nDigite o número da opção: "))

            if(opcao_atualizar >= 1 and opcao_atualizar <= len(campos)):
                campo = campos[opcao_atualizar - 1]
                novo_valor = input(f"Digite um novo valor para {campo}: ")

            atualizar_agendamento(user_auth[0], agendamento_id, campo, novo_valor)  

        elif(opcao == 4):
            print("========|SEUS AGENDAMENTOS|=======\n")
            agendamentos = listar_agendamentos(user_auth[0])
            for agendamento in agendamentos:
                print(f"Agendamento - {agendamento[0]}")

            agendamento_id = int(input("Qual o id do agendamento que você quer deletar: "))
            deletar_agendamento(user_auth[0], agendamento_id)
        
        elif(opcao == 5):
            break

        else:
            print("Digite uma opção valida!")
