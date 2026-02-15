import streamlit as st
import os

# Configuração da página
st.set_page_config(page_title="LB Simulador", layout="wide")

# --- BARRA LATERAL (Entradas de dados) ---
with st.sidebar:
    # Inserindo a imagem no topo da barra lateral
    nome_da_imagem = "tela inicial LB.png"
    
    # Este bloco verifica se a imagem existe para não travar o app se você esquecer de subir o arquivo
    if os.path.exists(nome_da_imagem):
        st.image(nome_da_imagem, use_container_width=True)
    else:
        st.sidebar.warning(f"⚠️ Arquivo '{nome_da_imagem}' não encontrado no GitHub.")
    
    st.divider()
    
    st.header("1. BASE & ENGAJAMENTO")
    base_ativa = st.slider("Base Ativa (Clientes atuais)", 0, 5000, 800)
    taxa_recomendacao = st.slider("Taxa de Recomendação (%)", 0, 100, 60)
    recomenda_cliente = st.number_input("Recomendações por Cliente", value=5)
    
    st.header("2. CONVERSÃO")
    agendamento = st.slider("Agendamento (Reunião) %", 0, 100, 50)
    ticket_medio = st.number_input("Ticket Médio (R$)", value=1000)
    taxa_conversao = st.slider("Fechamento (Venda) %", 0, 100, 45)

# --- LÓGICA DO FUNIL (Cálculos Automáticos) ---
perc_rec = taxa_recomendacao / 100
perc_agend = agendamento / 100
perc_conv = taxa_conversao / 100

# Cálculo do fluxo
promotores = base_ativa * perc_rec
total_recomendacoes = promotores * recomenda_cliente
reunioes_geradas = total_recomendacoes * perc_agend
novos_clientes = reunioes_geradas * perc_conv

# Cálculo Financeiro (Apenas Receita agora)
receita_mensal = novos_clientes * ticket_medio
receita_anual = receita_mensal * 12

# --- EXIBIÇÃO DOS RESULTADOS ---

# Título e Identidade
st.title("📊 Labor Business")
st.subheader("Simulador de Funil de Vendas")
st.divider()

# Parte Superior: Os dois grandes números
col1, col2 = st.columns(2)

with col1:
    st.info("RECEITA MENSAL")
    st.header(f"R$ {receita_mensal:,.2f}")

with col2:
    st.success("RECEITA ANUAL")
    st.header(f"R$ {receita_anual:,.2f}")

st.divider()

# Parte Inferior: O caminho do cliente (Fluxo)
st.write("#### Detalhamento do Fluxo de Conversão")
c1, c2, c3, c4 = st.columns(4)

c1.metric("Base Ativa", base_ativa)
c2.metric("Indicações", int(total_recomendacoes))
c3.metric("Reuniões", int(reunioes_geradas))
c4.metric("Novas Vendas", int(novos_clientes))
