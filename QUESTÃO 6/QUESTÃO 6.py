import streamlit as st

# --- MODELO DE DADOS (POO) ---

class Produto:
    """Classe que representa o catálogo de produtos."""
    def __init__(self, codigo, nome, valorUnitario):
        self.codigo = codigo
        self.nome = nome
        self.valorUnitario = valorUnitario

class ItemComanda:
    """Representa a associação entre um produto e sua quantidade na comanda."""
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto
        self.quantidade = quantidade
        self.subtotal = self.calcularSubtotal() # Atributo Derivado

    def calcularSubtotal(self):
        """RF06 - Cálculo automático de subtotal."""
        return self.quantidade * self.produto.valorUnitario

class Comanda:
    """Classe principal de controle da comanda."""
    def __init__(self, numero: int):
        self.numero = numero
        self.itens = [] # Atributo derivado (lista de objetos ItemComanda)
        self.total = 0.0
        self.finalizada = False # RF09 - Controle de estado

    def adicionarItem(self, produto: Produto, quantidade: int):
        """RF02 e RF03 - Registro de consumo."""
        if not self.finalizada:
            novo_item = ItemComanda(produto, quantidade)
            self.itens.append(novo_item)
            self.calcularTotal()
            return True
        return False

    def calcularTotal(self):
        """RF07 - Cálculo do valor total da compra."""
        self.total = sum(item.subtotal for item in self.itens)
        return self.total

# --- LOGICA DE INTERFACE (STREAMLIT) ---

def main():
    st.set_page_config(page_title="Padaria Doce Sabor", layout="wide")
    st.title("🥖 Padaria Doce Sabor - Sistema PDV")
    st.divider()

    # Inicialização do "Banco de Dados" em memória
    if 'produtos' not in st.session_state:
        st.session_state.produtos = {
            101: Produto(101, "Pão Francês (un)", 0.50),
            102: Produto(102, "Café Expresso", 4.50),
            103: Produto(103, "Pão de Queijo", 3.00),
            104: Produto(104, "Bolo de Milho (fatia)", 5.00)
        }
    if 'comandas' not in st.session_state:
        st.session_state.comandas = {}

    # --- ÁREA DO ATENDENTE (ABRIR COMANDA E REGISTRAR) ---
    st.sidebar.header("👨‍🍳 Área do Atendente")
    
    # RF01 - Criar Comanda
    num_comanda = st.sidebar.number_input("Número da Comanda", min_value=1, step=1)
    if st.sidebar.button("Abrir/Acessar Comanda"):
        if num_comanda not in st.session_state.comandas:
            st.session_state.comandas[num_comanda] = Comanda(num_comanda)
            st.sidebar.success(f"Comanda {num_comanda} aberta!")
        else:
            st.sidebar.info(f"Comanda {num_comanda} carregada.")

    # RF02/RF03/RF04 - Registrar Consumo
    if num_comanda in st.session_state.comandas:
        comanda_atual = st.session_state.comandas[num_comanda]
        
        if not comanda_atual.finalizada:
            st.subheader(f"📝 Lançamento - Comanda Nº {num_comanda}")
            prod_nome = st.selectbox("Selecionar Produto", 
                                    options=[p.nome for p in st.session_state.produtos.values()])
            
            # Busca objeto produto pelo nome
            produto_obj = next(p for p in st.session_state.produtos.values() if p.nome == prod_nome)
            
            qtd = st.number_input("Quantidade", min_value=1, value=1)
            
            if st.button("Registrar Produto"):
                comanda_atual.adicionarItem(produto_obj, qtd)
                st.toast(f"{prod_nome} adicionado!")
        else:
            st.error(f"A comanda {num_comanda} está FINALIZADA. Novos lançamentos impedidos (RNF05).")

    # --- ÁREA DO CAIXA (LEITURA E FINALIZAÇÃO) ---
    st.divider()
    st.header("🛒 Frente de Caixa")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # RF05/RF08 - Consultar e Ler Comanda
        num_caixa = st.number_input("Ler Comanda no Caixa", min_value=1, step=1, key="caixa")
        if num_caixa in st.session_state.comandas:
            c = st.session_state.comandas[num_caixa]
            st.write(f"### Detalhes da Comanda: {c.numero}")
            
            # Tabela de itens
            dados_tabela = []
            for item in c.itens:
                dados_tabela.append({
                    "Produto": item.produto.nome,
                    "Preço Un.": f"R$ {item.produto.valorUnitario:.2f}",
                    "Qtd": item.quantidade,
                    "Subtotal": f"R$ {item.subtotal:.2f}"
                })
            st.table(dados_tabela)
        else:
            st.warning("Comanda não encontrada ou não iniciada.")

    with col2:
        if num_caixa in st.session_state.comandas:
            c = st.session_state.comandas[num_caixa]
            # RF07/RF10 - Exibir Total
            st.metric("TOTAL DA COMPRA", f"R$ {c.total:.2f}")
            
            # RF09 - Finalizar Comanda
            if not c.finalizada:
                if st.button("FINALIZAR PAGAMENTO", use_container_width=True):
                    c.finalizada = True
                    st.balloons()
                    st.success("Compra finalizada com sucesso!")
            else:
                st.info("Status: PAGA / FINALIZADA")

if __name__ == "__main__":
    main()
