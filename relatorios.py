import matplotlib.pyplot as plt
from controle_pagamentos import relatorio_pagamentos
from controle_estoque import listar_estoque

def relatorio_pagamentos_grafico():
    dados = relatorio_pagamentos()
    nomes = [dado[0] for dado in dados]
    pagamentos = [dado[1] for dado in dados]
    valores = [dado[2] for dado in dados]

    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    
    # Gráfico de barras: Pagamentos por aluno
    ax[0].bar(nomes, pagamentos)
    ax[0].set_title("Pagamentos por Aluno")
    ax[0].set_ylabel("Número de Pagamentos")
    ax[0].set_xlabel("Nome do Aluno")

    # Gráfico de pizza: Valor total pago por aluno
    ax[1].pie(valores, labels=nomes, autopct='%1.1f%%')
    ax[1].set_title("Distribuição de Pagamentos por Aluno")

    plt.tight_layout()
    plt.show()

def relatorio_estoque_grafico():
    produtos = listar_estoque()
    nomes_produtos = [produto[1] for produto in produtos]
    quantidades = [produto[2] for produto in produtos]

    plt.bar(nomes_produtos, quantidades)
    plt.title("Estoque de Produtos")
    plt.xlabel("Produto")
    plt.ylabel("Quantidade")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()
