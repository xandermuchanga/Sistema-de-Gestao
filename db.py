import sqlite3

def connect_db():
    conn = sqlite3.connect('hotlines_computer.db')
    return conn

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    # Tabela de alunos
    cursor.execute('''CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT NOT NULL,
                        cpf TEXT NOT NULL UNIQUE,
                        curso TEXT NOT NULL,
                        data_matricula TEXT NOT NULL
                    )''')

    # Tabela de pagamentos
    cursor.execute('''CREATE TABLE IF NOT EXISTS pagamentos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        aluno_id INTEGER,
                        valor REAL NOT NULL,
                        data_pagamento TEXT NOT NULL,
                        pago BOOLEAN NOT NULL,
                        FOREIGN KEY(aluno_id) REFERENCES alunos(id)
                    )''')

    # Tabela de estoque
    cursor.execute('''CREATE TABLE IF NOT EXISTS estoque (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome_produto TEXT NOT NULL,
                        quantidade INTEGER NOT NULL,
                        preco REAL NOT NULL
                    )''')

    conn.commit()
    conn.close()

create_tables()
