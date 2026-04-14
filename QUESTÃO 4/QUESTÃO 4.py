import streamlit as st
from datetime import datetime, timedelta

# --- MODELO DE DADOS (POO) ---

class Prescricao:
    def __init__(self, paciente, remedio, dosagem, data_inicio, dias, vezes_dia, hora_inicial):
        self.paciente = paciente
        self.remedio = remedio
        self.dosagem = dosagem
        self.data_inicio = data_inicio
        self.dias = dias
        self.vezes_dia = vezes_dia
        self.hora_inicial = hora_inicial
        
        # Atributo Derivado: Data de Término (RF04)
        self.data_termino = data_inicio + timedelta(days=dias)
        
        # Planilha do Dia (Lista de horários)
        self.planilha_dia = self._gerar_horarios_dia(hora_inicial)

    def _gerar_horarios_dia(self, hora_referencia):
        """Gera a grade de horários baseada na frequência (24h / vezes_dia)"""
        intervalo = 24 // self.vezes_dia
        lista_horarios = []
        
        # Cria o objeto datetime completo para o cálculo
        base_dt = datetime.combine(datetime.today(), hora_referencia)
        
        for i in range(self.vezes_dia):
            horario_dose = base_dt + timedelta(hours=i * intervalo)
            lista_horarios.append(horario_dose.time())
        return lista_horarios

    def reorganizar_por_atraso(self, hora_atrasada):
        """RF07 - Reorganiza os horários do dia a partir de um atraso"""
        self.planilha_dia = self._gerar_horarios_dia(hora_atrasada)

# --- INTERFACE WEB (STREAMLIT) ---

st.set_page_config(page_title="Controle de Medicação", page_icon="💊")

st.title("💊 Sistema de Controle de Remédios")
st.markdown("---")

# Verificação de Estado da Sessão (Persistência em memória)
if 'prescricao' not in st.session_state:
    st.subheader("📝 Novo Cadastro de Prescrição (RF01)")
    
    with st.form("form_cadastro"):
        col1, col2 = st.columns(2)
        paciente = col1.text_input("Nome do Paciente", placeholder="Ex: Maurício")
        remedio = col2.text_input("Nome do Remédio", placeholder="Ex: Amoxicilina")
        
        col3, col4, col5 = st.columns(3)
        dosagem = col3.text_input("Dosagem", placeholder="Ex: 500mg")
        data_ini = col4.date_input("Data de Início")
        dias = col5.number_input("Duração (Dias)", min_value=1, value=7)
        
        col6, col7 = st.columns(2)
        vezes_dia = col6.selectbox("Vezes ao dia", [1, 2, 3, 4, 6, 8, 12], index=2)
        hora_ini = col7.time_input("Horário da Primeira Dose (RF03)")
        
        enviar = st.form_submit_button("Cadastrar e Gerar Horários")
        
        if enviar:
            if paciente and remedio:
                st.session_state.prescricao = Prescricao(
                    paciente, remedio, dosagem, data_ini, dias, vezes_dia, hora_ini
                )
                st.rerun()
            else:
                st.error("Preencha o nome do paciente e do remédio.")

else:
    # RECUPERAÇÃO DO OBJETO
    p = st.session_state.prescricao
    
    # EXIBIÇÃO DE INFORMAÇÕES GERAIS (RF04 e RF07 do boneco adaptado)
    st.success(f"✅ Medicação ativa: **{p.remedio}** ({p.dosagem})")
    st.info(f"👤 **Paciente:** {p.paciente}  |  🏁 **Término do tratamento:** {p.data_termino.strftime('%d/%m/%Y')}")
    
    col_lista, col_atraso = st.columns([2, 1])
    
    with col_lista:
        st.subheader("📅 Planilha de Horários do Dia (RF06)")
        for i, hora in enumerate(p.planilha_dia):
            st.write(f"🔔 **{i+1}ª Dose:** {hora.strftime('%H:%M')}")
            
    with col_atraso:
        st.subheader("⌛ Notificar Atraso (RF07)")
        st.write("Se atrasou a dose, informe o novo horário abaixo:")
        nova_hora = st.time_input("Novo horário da dose atual", value=datetime.now().time())
        
        if st.button("Reorganizar Horários"):
            p.reorganizar_por_atraso(nova_hora)
            st.toast("Horários do dia atualizados com sucesso!", icon="⏰")
            st.rerun()

    if st.button("🗑️ Excluir Prescrição (Reset)"):
        del st.session_state.prescricao
        st.rerun()