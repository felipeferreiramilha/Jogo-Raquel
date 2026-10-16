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
# 2. FUNÇÃO DA INTELIGÊNCIA ARTIFICIAL
# ==========================================================
def obter_resposta_espacial(pergunta):
    """
    Conecta ao Gemini e gera uma resposta rica e detalhada 
    com analogias simples para crianças.
    """
    try:
        # Inicializa o cliente oficial do Google GenAI
        client = genai.Client()

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
            "Verifique se você configurou a sua chave de API corretamente no terminal (`GEMINI_API_KEY`).\n\n"
            f"Erro técnico: `{e}`"
        )

# ==========================================================
# 3. INTERFACE VISUAL (STREAMLIT)
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
st.markdown("💡 **Dica para Live / OBS:** Abra o OBS Studio, adicione uma **Captura de Janela** selecionando esta aba do seu navegador para espelhar perfeitamente.")
