import pandas as pd

def gerar_relatorio():

    dados = pd.read_csv("dados/vendas.csv")

    # criar coluna total
    dados["total"] = dados["quantidade"] * dados["preco"]

    # vendas por produto
    vendas_produto = dados.groupby("produto")["total"].sum()

    # vendas por região
    vendas_regiao = dados.groupby("regiao")["total"].sum()

    # vendas por vendedor
    vendas_vendedor = dados.groupby("vendedor")["total"].sum()

    print("\nVendas por produto")
    print(vendas_produto)

    print("\nVendas por região")
    print(vendas_regiao)

    print("\nVendas por vendedor")
    print(vendas_vendedor)

    dados.to_csv("relatorios/relatorio_vendas.csv", index=False)

    print("\nRelatório gerado com sucesso!")