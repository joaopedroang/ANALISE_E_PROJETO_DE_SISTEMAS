import streamlit as st
from datetime import date

# --- CLASSES BASE (CONFORME DIAGRAMA) ---

class Endereco:
    def __init__(self, logradouro, cep, numero, bairro):
        self.logradouro = logradouro
        self.cep = cep
        self.numero = numero
        self.bairro = bairro

class Pessoa:
    def __init__(self, nome, dtnasc):
        self.nome = nome
        self.dtnasc = dtnasc
        self.enderecos = [] # Multiplicidade 1..*
        self.telefones = [] # Multiplicidade 1..*

class Cliente(Pessoa):
    def __init__(self, nome, dtnasc, codigo, limcredito, profissao):
        super().__init__(nome, dtnasc)
        self.codigo = codigo
        self.limcredito = limcredito
        self.profissao = profissao

class Funcionario(Pessoa):
    def __init__(self, nome, dtnasc, matricula, salario, dtadmi, cargo):
        super().__init__(nome, dtnasc)
        self.matricula = matricula
        self.salario = salario
        self.dtadmi = dtadmi
        self.cargo = cargo

# --- INTERFACE STREAMLIT ---

st.title("SISTEMA DE CADASTRO UNIFICADO")
st.subheader("Baseado no Diagrama de Herança do Professor")

tipo_cadastro = st.radio("Selecione o tipo de cadastro:", ["Cliente", "Funcionário"])

with st.form("cadastro_geral"):
    st.write("### Dados Básicos (Classe PESSOA)")
    nome = st.text_input("NOME")
    dtnasc = st.date_input("DATA DE NASCIMENTO (DTNASC)")
    
    if tipo_cadastro == "Cliente":
        st.write("### Dados do CLIENTE")
        codigo = st.text_input("CÓDIGO")
        limite = st.number_input("LIMITE DE CRÉDITO (LIMCREDITO)", min_value=0.0)
        profissao = st.text_input("NOME DA PROFISSÃO")
        
    else:
        st.write("### Dados do FUNCIONÁRIO")
        matricula = st.number_input("MATRÍCULA", step=1)
        salario = st.number_input("SALÁRIO", min_value=0.0)
        dtadmi = st.date_input("DATA DE ADMISSÃO (DTADMI)")
        cargo = st.text_input("NOME DO CARGO")

    if st.form_submit_button("CADASTRAR"):
        st.success(f"{tipo_cadastro} {nome} cadastrado com sucesso seguindo as regras de herança!")
