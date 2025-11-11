from config.db import criar_conexao


def insert_user(email: str, password: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = "INSERT INTO usuarios(email, password) VALUES (%s, %s);"
        cursor.execute(sql, (email, password))
        con.commit()
        print("Usuario cadastrado com sucesso")

    except Exception as e:
        print(e)
    finally:
        cursor.close()
        con.close()

def login(email: str, password: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM usuarios WHERE email=%s and password=%s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone() #retorna somente um usuario
        return user
    except Exception as e:
        print(e)