import streamlit as st

# Configuração da página para o layout ficar profissional
st.set_page_config(page_title="LB Simulador", layout="wide")

# Título e Branding
st.title("📊 Labor Business: Operating System")
st.markdown("### Simulador de Impacto Financeiro")
st.divider()

# --- SIDEBAR (Barra Lateral para os Sliders) ---
with st.sidebar:
    st.header("1. BASE & ENGAJAMENTO")
    base_ativa = st.slider("Base Ativa (Clientes na carteira)", 0, 5000, 800)
    taxa_recomendacao = st.slider("Taxa de Recomendação (%)", 0, 100, 60)
    recomenda_cliente = st.number_input("Recomendações por Cliente", value=5)
    
    st.header("2. CONVERSÃO")
    agendamento = st.slider("Agendamento (Reunião) %", 0, 100, 50)
    ticket_medio = st.number_input("Ticket Médio (R$)", value=1000)
    taxa_conversao = st.slider("Conversão de Vendas %", 0, 100, 45)

# --- LÓGICA DE CÁLCULO ---
# 1. Transformando as porcentagens em números decimais para o cálculo
perc_rec = taxa_recomendacao / 100
perc_agend = agendamento / 100
perc_conv = taxa_conversao / 100

# 2. O Funil
total_recomendacoes = base_ativa * perc_rec * recomenda_cliente
reunioes_geradas = total_recomendacoes * perc_agend
novos_clientes = reunioes_geradas * perc_conv

# 3. Financeiro
receita_mensal = novos_clientes * ticket_medio
cmi_mensal = receita_mensal * 0.70  # Considerando 70% de margem real como na sua foto
cmi_anual = cmi_mensal * 12

# --- EXIBIÇÃO DOS RESULTADOS (DASHBOARD) ---
col1, col2, col3 = st.columns(3)

with col1:
    st.info("RECEITA MENSAL")
    st.subheader(f"R$ {receita_mensal:,.2f}")

with col2:
    st.success("CMI MENSAL (70%)")
    st.subheader(f"R$ {cmi_mensal:,.2f}")

with col3:
    st.warning("CMI ANUAL (12 MESES)")
    st.subheader(f"R$ {cmi_anual:,.2f}")

st.divider()

# Fluxo de Conversão visual
st.write("#### Fluxo de Conversão")
c1, c2, c3 = st.columns(3)
c1.metric("Base Ativa", base_ativa)
c2.metric("Total Recomendações", int(total_recomendacoes))
c3.metric("Novos Clientes", int(novos_clientes))
