import sqlite3
from db import connect_db

def adicionar_produto(nome_produto, quantidade, preco):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO estoque (nome_produto, quantidade, preco) VALUES (?, ?, ?)", 
                   (nome_produto, quantidade, preco))
    conn.commit()
    conn.close()

def atualizar_estoque(id, quantidade):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE estoque SET quantidade = quantidade + ? WHERE id = ?", (quantidade, id))
    conn.commit()
    conn.close()

def listar_estoque():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM estoque")
    produtos = cursor.fetchall()
    conn.close()
    return produtos
