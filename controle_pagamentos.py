import sqlite3
from db import connect_db

def registrar_pagamento(aluno_id, valor, data_pagamento, pago):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO pagamentos (aluno_id, valor, data_pagamento, pago) VALUES (?, ?, ?, ?)",
                   (aluno_id, valor, data_pagamento, pago))
    conn.commit()
    conn.close()

def listar_pagamentos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pagamentos")
    pagamentos = cursor.fetchall()
    conn.close()
    return pagamentos

def relatorio_pagamentos():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT alunos.nome, COUNT(pagamentos.id), SUM(pagamentos.valor) FROM pagamentos "
                   "JOIN alunos ON alunos.id = pagamentos.aluno_id "
                   "GROUP BY alunos.id")
    relatorio = cursor.fetchall()
    conn.close()
    return relatorio
