import time, os

from config.db import criar_conexao

def agendar_gravacao(user_id, data_gravacao, horario_gravacao, qtd_videos, local_gravacao, video_aereo):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "INSERT INTO agendar_gravacao (user_id, data_gravacao, horario_gravacao, qtd_videos, local_gravacao, video_aereo) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, [user_id, data_gravacao, horario_gravacao, qtd_videos, local_gravacao, video_aereo])
    conn.commit()
    os.system('cls')
    print(f"AGENDAMENTO CONCLUÍDO")
    time.sleep(2.5)
    os.system('cls')

def listar_agendamentos(user_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM agendar_gravacao WHERE user_id = %s"
    cursor.execute(sql, [user_id])
    agendamentos = cursor.fetchall()
    return agendamentos

def atualizar_agendamento(user_id, agendamento_id, campo, novo_valor):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = f"UPDATE agendar_gravacao SET {campo} = %s WHERE user_id = %s AND id = %s"
    cursor.execute(sql, [novo_valor, user_id, agendamento_id])
    conn.commit()
    print(f"Agendamento atualizado com sucesso!")
    time.sleep(1.5)
    os.system('cls')

def deletar_agendamento(user_id, agendamento_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "DELETE FROM agendar_gravacao WHERE user_id = %s AND id = %s"
    cursor.execute(sql, [user_id, agendamento_id])
    conn.commit()
    print("Agendamento deletado")
    time.sleep(2.5)
    os.system('cls')