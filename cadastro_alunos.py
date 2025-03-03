import sqlite3
from db import connect_db

def adicionar_aluno(nome, cpf, curso, data_matricula):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO alunos (nome, cpf, curso, data_matricula) VALUES (?, ?, ?, ?)", 
                   (nome, cpf, curso, data_matricula))
    conn.commit()
    conn.close()

def editar_aluno(id, nome, cpf, curso, data_matricula):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE alunos SET nome=?, cpf=?, curso=?, data_matricula=? WHERE id=?", 
                   (nome, cpf, curso, data_matricula, id))
    conn.commit()
    conn.close()

def excluir_aluno(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id=?", (id,))
    conn.commit()
    conn.close()

def listar_alunos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos
