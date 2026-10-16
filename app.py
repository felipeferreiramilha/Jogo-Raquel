import os
import streamlit as st
from google import genai
from google.genai import types

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA E VISUAL
# ==========================================================
st.set_page_config(
    page_title="Astronomia para Crianças",
    page_icon="🚀",
    layout="centered"
)

# Estilização visual futurista e amigável para lives
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
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# 2. CONFIGURAÇÃO DA INTELIGÊNCIA ARTIFICIAL (GEMINI)
# ==========================================================
def obter_resposta_detalhada(pergunta):
    """
    Conecta à API do Gemini e força a IA a entregar respostas
    profundas, divididas em 3 a 5 parágrafos ricos em detalhes.
    """
    try:
        # Inicializa o cliente do Gemini
        # Nota: Certifique-se de configurar sua chave no terminal com: 
        # set GEMINI_API_KEY="sua_chave" (Windows) ou export GEMINI_API_KEY="sua_chave" (Mac/Linux)
        client = genai.Client()

        # Instrução de Sistema rígida para garantir explicações elaboradas e infantis
        instrucao_sistema = (
            "Você é o assistente virtual 'Astronomia para Crianças', um guia espacial divertido, "
            "cientista e mágico que explica os maiores mistérios do universo. "
            "Regras OBRIGATÓRIAS que você deve seguir:\n"
            "1. Responda a QUALQUER pergunta sobre astronomia, física, buracos negros, matéria escura, "
            "teoria das cordas, relatividade ou exoplanetas.\n"
            "2. Cada resposta DEVE ser altamente elaborada, rica em detalhes e ter obrigatoriamente "
            "entre **3 e 5 parágrafos** bem desenvolvidos.\n"
            "3. Use uma linguagem mágica, acolhedora, com analogias fantásticas fáceis para crianças entenderem, "
            "mas sem perder o rigor científico real.\n"
            "4. Nunca dê respostas curtas ou superficiais. Explique o 'porquê' das coisas de forma fascinante."
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
            "🚀 **Houston, tivemos um pequeno problema técnico!**\n\n"
            "Parece que a chave da API do Gemini (`GEMINI_API_KEY`) não foi configurada corretamente no seu computador, "
            "ou o foguete perdeu o sinal com a base. Verifique se a sua chave está ativa no terminal e tente novamente!\n\n"
            f"*Detalhe técnico do erro:* `{e}`"
        )

# ==========================================================
# 3. INTERFACE GRÁFICA (STREAMLIT)
# ==========================================================
st.title("🚀 Astronomia para Crianças 🌌")
st.markdown("### O super computador cósmico que responde **tudo** sobre o espaço com explicações completas e detalhadas!")

# Campo de entrada da pergunta
pergunta_usuario = st.text_input(
    "O que você quer explorar no universo hoje?",
    placeholder="Ex: Como funciona um buraco negro? O que é matéria escura? Me explique a relatividade de Einstein..."
)

# Botão de envio
if st.button("🌟 Decolar Pesquisa Cósmica!", type="primary"):
    if pergunta_usuario.strip() != "":
        # Mostra um aviso visual de carregamento enquanto a IA elabora a resposta rica
        with st.spinner("✨ O foguete está viajando pelas galáxias e elaborando uma resposta completa para você..."):
            resposta_gerada = obter_resposta_detalhada(pergunta_usuario)
        
        # Exibe a resposta estruturada em um bloco visual elegante
        st.markdown("### 🔭 Resposta do Explorador Espacial:")
        st.markdown(f'<div class="resposta-box">{resposta_gerada}</div>', unsafe_allow_html=True)
    else:
        st.warning("⚠️ Digite uma pergunta na caixa acima para o foguete poder decolar!")

# Rodapé informativo para a Live / OBS
st.markdown("---")
st.markdown("💡 **Dica para sua Live / Stream (OBS Studio):** Abra o OBS, adicione uma fonte de **Captura de Janela** e selecione esta aba do seu navegador. Ela vai espelhar perfeitamente em tela cheia, sem telas pretas e com alta qualidade!")
