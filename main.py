import getpass
import os
import time

from services.user_services import insert_user, login
from view.admin_view import panel

while True:

    print("\n========|APP GRUPO M2|========\n\nSelecione uma opção" )
    print("1 - Criar Novo Usuário \n2 - Entrar \n3 - Sair do Sistema")
    opcao = int(input("Digite a opção: "))
    os.system('cls')

    if(opcao == 1):
        print("========|TELA CADASTRO|=======")
        email = input("Digite o seu email: ")
        password = getpass.getpass("Digite sua senha: ")
        time.sleep(0.8)
        os.system('cls')

        insert_user(email, password)
    elif(opcao == 2):
        print("========|TELA LOGIN|=======")
        email = input("Digite o seu email: ")
        password = getpass.getpass("Digite sua senha: ")
        user_auth = login(email, password)
        time.sleep(0.8)
        os.system('cls')

        if(user_auth):
            panel(user_auth)
        else:
            print("Usuário ou senha invalidos")
    elif(opcao == 3):
        break
    else:
        print("Digite uma opção valida!")