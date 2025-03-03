import tkinter as tk
from tkinter import messagebox
from cadastro_alunos import adicionar_aluno, listar_alunos, editar_aluno, excluir_aluno
from controle_pagamentos import registrar_pagamento, listar_pagamentos
from controle_estoque import adicionar_produto, listar_estoque
from relatorios import relatorio_pagamentos_grafico, relatorio_estoque_grafico

def exibir_alunos():
    alunos = listar_alunos()
    for aluno in alunos:
        print(aluno)

def exibir_estoque():
    produtos = listar_estoque()
    for produto in produtos:
        print(produto)

def gerar_relatorio_pagamentos():
    relatorio_pagamentos_grafico()

def gerar_relatorio_estoque():
    relatorio_estoque_grafico()

# Criação da interface
root = tk.Tk()
root.title("Hotlines Computer")

# Tela de Alunos
alunos_button = tk.Button(root, text="Exibir Alunos", command=exibir_alunos)
alunos_button.pack()

# Tela de Estoque
estoque_button = tk.Button(root, text="Exibir Estoque", command=exibir_estoque)
estoque_button.pack()

# Relatórios
relatorio_pagamentos_button = tk.Button(root, text="Relatório de Pagamentos", command=gerar_relatorio_pagamentos)
relatorio_pagamentos_button.pack()

relatorio_estoque_button = tk.Button(root, text="Relatório de Estoque", command=gerar_relatorio_estoque)
relatorio_estoque_button.pack()

root.mainloop()
