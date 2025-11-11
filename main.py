import getpass

from services.user_services import insert_user, login
from view.admin_view import panel

while True:
    print("1 - Criar Novo Usuário \n2 - Entrar \n3 - Sair do Sistema")
    opcao = int(input("Digite a opção: "))

    if(opcao == 1):
        email = input("Digite o seu email: ")
        password = getpass.getpass("Digite sua senha: ")

        insert_user(email, password)
    elif(opcao == 2):
        email = input("Digite o seu email: ")
        password = getpass.getpass("Digite sua senha: ")
        user_auth = login(email, password)

        if(user_auth):
            panel(user_auth)
        else:
            print("Usuário ou senha invalidos")
    elif(opcao == 3):
        break
    else:
        print("Digite uma opção valida!")