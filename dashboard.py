import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Dashboard de Vendas",
    layout="wide"
)

st.title("📊 Dashboard Empresarial de Vendas")

# carregar dados
dados = pd.read_csv("dados/vendas.csv")

dados["total"] = dados["quantidade"] * dados["preco"]

# =====================
# FILTROS
# =====================

st.sidebar.header("Filtros")

regiao = st.sidebar.multiselect(
    "Selecione a região",
    dados["regiao"].unique(),
    default=dados["regiao"].unique()
)

vendedor = st.sidebar.multiselect(
    "Selecione o vendedor",
    dados["vendedor"].unique(),
    default=dados["vendedor"].unique()
)

dados_filtrados = dados[
    (dados["regiao"].isin(regiao)) &
    (dados["vendedor"].isin(vendedor))
]

# =====================
# KPIs
# =====================

faturamento = dados_filtrados["total"].sum()
total_produtos = dados_filtrados["quantidade"].sum()
total_vendas = dados_filtrados.shape[0]
ticket_medio = faturamento / total_vendas

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Faturamento", f"R$ {faturamento:,.2f}")
col2.metric("📦 Produtos Vendidos", total_produtos)
col3.metric("🧾 Total de Vendas", total_vendas)
col4.metric("📊 Ticket Médio", f"R$ {ticket_medio:,.2f}")

st.divider()

# =====================
# GRÁFICOS
# =====================

col1, col2 = st.columns(2)

vendas_produto = dados_filtrados.groupby("produto")["total"].sum().reset_index()

fig_produto = px.bar(
    vendas_produto,
    x="produto",
    y="total",
    title="Vendas por Produto"
)

col1.plotly_chart(fig_produto, use_container_width=True)

vendas_regiao = dados_filtrados.groupby("regiao")["total"].sum().reset_index()

fig_regiao = px.pie(
    vendas_regiao,
    names="regiao",
    values="total",
    title="Distribuição por Região"
)

col2.plotly_chart(fig_regiao, use_container_width=True)

st.divider()

# gráfico vendedor

vendas_vendedor = dados_filtrados.groupby("vendedor")["total"].sum().reset_index()

fig_vendedor = px.bar(
    vendas_vendedor,
    x="vendedor",
    y="total",
    title="Vendas por Vendedor"
)

st.plotly_chart(fig_vendedor, use_container_width=True)

# =====================
# TABELA
# =====================

st.subheader("Dados detalhados")

st.dataframe(dados_filtrados)