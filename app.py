import streamlit as st

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Astronomia para Crianças",
    page_icon="🚀",
    layout="centered"
)

# Estilização visual amigável e limpa
st.markdown(
    """
    <style>
    .main {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #161b22;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        border: 1px solid #30363d;
    }
    .resposta-box {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-top: 20px;
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 Astronomia para Crianças 🌌")
st.markdown("### Digite qualquer tema sobre o espaço para ver explicações claras e divertidas!")

# ==========================================================
# 2. BANCO DE CONHECIMENTO (RESPOSTAS PRONTAS E REVISADAS)
# ==========================================================
BASE_CONHECIMENTO = {
    "mercúrio": (
        "Mercúrio é o planeta mais próximo do Sol e também o menorzinho de todos os oito planetas do Sistema Solar. "
        "Como ele fica bem colado ao Sol, a parte dele que fica virada para a luz é tããão quente que poderia derreter metais, "
        "enquanto o outro lado é super congelante!\n\n"
        "Ele é um planeta rochoso, cheio de buraquinhos na superfície chamados crateras
