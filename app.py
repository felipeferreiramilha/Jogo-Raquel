streamlit
google-genai
import os
import streamlit as st
from google import genai
from google.genai import types

# ==========================================================
# 1. CONFIGURAÇÃO DA TELA
# ==========================================================
st.set_page_config(
    page_title="Astronomia para Crianças",
    page_icon="🚀",
    layout="centered"
)

st.title("🚀 Astronomia para Crianças 🌌")
st.markdown("### Digite qualquer dúvida sobre o espaço e receba explicações completas e mágicas!")

# ==========================================================
# 2. CONFIGURAÇÃO DA CHAVE DE API (SEGURANÇA DO STREAMLIT)
# ==========================================================
api_key = None
try:
    if "GEMINI_API_KEY" in st.secrets:
        api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

if not api_key:
    api_key = os.environ.get("GEMINI_API_KEY")

# ==========================================================
# 3. FUNÇÃO DA INTELIGÊNCIA ARTIFICIAL
# ==========================================================
def obter_resposta_espacial(pergunta):
    """
    Conecta ao Gemini e gera uma resposta rica e detalhada 
    com analogias simples para crianças.
    """
    try:
        # Inicializa o cliente com a chave encontrada
        client = genai.Client(api_key=api_key) if api_key else genai.Client()

        # Regras de comportamento para a IA
        instrucao_sistema = (
            "Você é o assistente 'Astronomia para Crianças', um guia espacial divertido. "
            "Regras obrigatórias:\n"
            "1. Responda a QUALQUER pergunta sobre espaço, planetas, física ou buracos negros.\n"
            "2. Cada resposta DEVE ter entre **3 e 5 parágrafos** bem desenvolvidos e ricos em detalhes.\n"
            "3. Use analogias mágicas e fáceis para crianças entenderem, sem perder o rigor científico."
        )

        configuracao = types.GenerateContentConfig(
            system_instruction=instrucao_sistema,
            temperature=0.7,
        )

        resposta = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=pergunta,
            config=configuracao,
        )
        return resposta.text

    except Exception as e:
        return (
            "⚠️ **Ops! O foguete perdeu o sinal com a base.**\n\n"
            "Isso geralmente acontece porque a chave `GEMINI_API_KEY` não foi configurada nos **Secrets** do Streamlit Cloud.\n\n"
            f"Detalhe do erro: `{e}`"
        )

# ==========================================================
# 4. INTERFACE VISUAL (STREAMLIT)
# ==========================================================
pergunta_usuario = st.text_input(
    "O que você quer descobrir no universo hoje?",
    placeholder="Ex: Como funciona um buraco negro? O que é matéria escura?"
)

if st.button("🌟 Decolar Pesquisa!", type="primary"):
    if pergunta_usuario.strip() != "":
        with st.spinner("✨ Viajando pelas galáxias para buscar a resposta..."):
            resposta_final = obter_resposta_espacial(pergunta_usuario)
        
        st.markdown("### 🔭 Resposta do Explorador Espacial:")
        st.write(resposta_final)
    else:
        st.warning("⚠️ Digite uma pergunta na caixa acima para poder pesquisar!")

st.markdown("---")
st.markdown("💡 **Dica:** Certifique-se de adicionar sua chave do Gemini em **Settings -> Secrets** no painel do Streamlit Cloud usando o formato: `GEMINI_API_KEY = \"sua_chave_aqui\"`")
GEMINI_API_KEY = "sua_chave_real_do_gemini_aqui"
