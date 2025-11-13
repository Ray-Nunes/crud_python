from config.db import criar_conexao
from config.crypt import checar_password, criptografar

def insert_user(email: str, password: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        password = criptografar(password)
        sql = "INSERT INTO usuarios(email, password) VALUES (%s, %s);"
        cursor.execute(sql, (email, password))
        con.commit()

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def login(email: str, password: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM usuarios WHERE email=%s"
        cursor.execute(sql, (email,))
        user = cursor.fetchone() #retorna somente um usuario
        if user and checar_password(password, bytes(user[2])):
            print("Conexão realizada com sucesso!")
            return user

        return None
    except Exception as e:
        print(e)