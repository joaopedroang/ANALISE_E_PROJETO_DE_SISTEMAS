import streamlit as st
import pandas as pd
from datetime import datetime

# --- MODELO DE DADOS (POO) ---

class Gasto:
    def __init__(self, tipo, data, valor, forma_pagamento):
        self.tipo = tipo
        self.data = data
        self.valor = valor
        self.forma_pagamento = forma_pagamento

class ControleFinanceiro:
    def __init__(self):
        self.gastos = []

    def adicionar_gasto(self, gasto):
        self.gastos.append(gasto)

    def obter_dataframe(self):
        """Converte a lista de objetos para um DataFrame para facilitar relatórios"""
        if not self.gastos:
            return pd.DataFrame()
        
        dados = [
            {
                "Tipo": g.tipo,
                "Data": g.data,
                "Valor": g.valor,
                "Forma de Pagamento": g.forma_pagamento,
                "Mês": g.data.strftime("%m/%Y")
            }
            for g in self.gastos
        ]
        return pd.DataFrame(dados)

# --- INTERFACE STREAMLIT ---

st.set_page_config(page_title="Gastos Diários - Vera", layout="wide")

st.title("📊 Gestão de Gastos Diários")
st.markdown("---")

# Inicialização do controle no estado da sessão
if 'controle' not in st.session_state:
    st.session_state.controle = ControleFinanceiro()

controle = st.session_state.controle

# --- COLUNAS: CADASTRO E RELATÓRIO ---
col_cad, col_rel = st.columns([1, 2])

with col_cad:
    st.subheader("📝 Novo Lançamento")
    with st.form("form_gasto", clear_on_submit=True):
        tipo = st.selectbox("Tipo do Gasto", ["Refeição", "Remédio", "Roupa", "Transporte", "Lazer", "Outros"])
        data = st.date_input("Data do Gasto", value=datetime.now())
        valor = st.number_input("Valor (R$)", min_value=0.01, step=0.01)
        forma = st.selectbox("Forma de Pagamento", 
                             ["Dinheiro", "Cartão de Crédito", "Cartão de Débito", "Ticket Alimentação", "Refeição"])
        
        if st.form_submit_button("Adicionar à Planilha"):
            novo_gasto = Gasto(tipo, data, valor, forma)
            controle.adicionar_gasto(novo_gasto)
            st.success("Gasto registrado!")
            st.rerun()

with col_rel:
    st.subheader("📈 Relatório Mensal")
    df = controle.obter_dataframe()

    if df.empty:
        st.info("Nenhum gasto cadastrado ainda.")
    else:
        # Filtro de Mês para o Relatório
        meses_disponiveis = df["Mês"].unique()
        mes_selecionado = st.selectbox("Selecione o Mês para Análise", meses_disponiveis)
        
        df_mes = df[df["Mês"] == mes_selecionado]

        # --- EXIBIÇÃO DOS TOTAIS DERIVADOS ---
        total_geral = df_mes["Valor"].sum()
        st.metric("Gasto Total no Mês", f"R$ {total_geral:,.2f}")

        tab1, tab2 = st.tabs(["Agrupado por Tipo", "Agrupado por Pagamento"])

        with tab1:
            # Agrupamento conforme RF05
            resumo_tipo = df_mes.groupby("Tipo")["Valor"].sum().reset_index()
            st.table(resumo_tipo.style.format({"Valor": "R$ {:.2f}"}))
            st.bar_chart(resumo_tipo.set_index("Tipo"))

        with tab2:
            # Agrupamento conforme RF06
            resumo_pag = df_mes.groupby(["Tipo", "Forma de Pagamento"])["Valor"].sum().reset_index()
            st.dataframe(resumo_pag.style.format({"Valor": "R$ {:.2f}"}), use_container_width=True)

# --- VISUALIZAÇÃO DA PLANILHA (ESTILO EXCEL) ---
if not df.empty:
    st.divider()
    st.subheader("📋 Lista Geral de Gastos")
    st.dataframe(df.drop(columns=["Mês"]), use_container_width=True)
    
    if st.button("🗑️ Limpar Planilha"):
        st.session_state.controle = ControleFinanceiro()
        st.rerun()