from config.db import criar_conexao

def create_task(user_id, title):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = 'INSERT INTO TASKS (title, user_id) VALUES (%s, %s)'
    cursor.execute(sql, (title, user_id))
    conn.commit()
    print("Tesk cadastrada")

def list_task(user_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "SELECT * FROM TASKS WHERE user_id = %s"
    cursor.execute(sql, [user_id])
    tasks = cursor.fetchall() #-> Uma lista de tasks
    return tasks

def delete_task(user_id, task_id):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "DELETE FROM tasks WHERE user_id=%s AND id=%s"
    cursor.execute(sql, [user_id, task_id])
    conn.commit()
    print("Task deletada")

def update_task(user_id, task_id, title):
    conn = criar_conexao()
    cursor = conn.cursor()
    sql = "UPDATE tasks SET title = %s WHERE user_id = %s AND id = %s"
    cursor.execute(sql, [title, user_id, task_id])
    conn.commit()
    print("Tesk atualizada!")