import streamlit as st
import os

# Configuração da página
st.set_page_config(page_title="LB Simulador", layout="wide")

# --- FUNÇÃO DE FORMATAÇÃO BRASILEIRA ---
def formar_br(valor):
    # Transforma o número em 1.234,56
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# --- BARRA LATERAL (Entradas de dados) ---
with st.sidebar:
    nome_da_imagem = "tela inicial LB.png"
    
    if os.path.exists(nome_da_imagem):
        st.image(nome_da_imagem, use_container_width=True)
    else:
        st.sidebar.warning(f"⚠️ Arquivo '{nome_da_imagem}' não encontrado.")
    
    st.divider()
    
    st.header("1. BASE & ENGAJAMENTO")
    base_ativa = st.slider("Base Ativa (Clientes atuais)", 0, 5000, 800)
    taxa_recomendacao = st.slider("Taxa de Recomendação (%)", 0, 100, 60)
    recomenda_cliente = st.number_input("Recomendações por Cliente", value=5)
    
    st.header("2. CONVERSÃO")
    agendamento = st.slider("Agendamento (Reunião) %", 0, 100, 50)
    ticket_medio = st.number_input("Ticket Médio (R$)", value=1000)
    taxa_conversao = st.slider("Fechamento (Venda) %", 0, 100, 45)

# --- LÓGICA DO FUNIL ---
perc_rec = taxa_recomendacao / 100
perc_agend = agendamento / 100
perc_conv = taxa_conversao / 100

promotores = base_ativa * perc_rec
total_recomendacoes = promotores * recomenda_cliente
reunioes_geradas = total_recomendacoes * perc_agend
novos_clientes = reunioes_geradas * perc_conv

receita_mensal = novos_clientes * ticket_medio
receita_anual = receita_mensal * 12

# --- EXIBIÇÃO DOS RESULTADOS ---

st.title("📊 Labor Business")
st.subheader("Simulador de Funil de Vendas")
st.divider()

col1, col2 = st.columns(2)

with col1:
    st.info("RECEITA MENSAL")
    # Usando a função de formatação brasileira
    st.header(formar_br(receita_mensal))

with col2:
    st.success("RECEITA ANUAL")
    # Usando a função de formatação brasileira
    st.header(formar_br(receita_anual))

st.divider()

st.write("#### Detalhamento do Fluxo de Conversão")
c1, c2
