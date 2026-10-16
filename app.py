# ============================================================
# APP COMPLETO — IA DE ASTRONOMIA + PESQUISA NA WEB
# ============================================================

import streamlit as st
from openai import OpenAI
from datetime import datetime

# ------------------------------------------------------------
# CONFIGURAÇÃO
# ------------------------------------------------------------

st.set_page_config(
    page_title="IA de Astronomia",
    page_icon="🌌",
    layout="wide"
)

# ------------------------------------------------------------
# CSS
# ------------------------------------------------------------

st.markdown("""
<style>

.main {
    background-color: #050816;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

.titulo-principal {
    text-align: center;
    font-size: 42px;
    font-weight: bold;
    color: #ffffff;
    margin-bottom: 5px;
}

.subtitulo {
    text-align: center;
    color: #b8c7ff;
    font-size: 18px;
    margin-bottom: 30px;
}

.caixa-pergunta {
    background: #101936;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #26345f;
    margin-bottom: 20px;
}

.resposta {
    background: #0c132b;
    padding: 28px;
    border-radius: 18px;
    border-left: 5px solid #7c8cff;
    line-height: 1.8;
    font-size: 17px;
}

.fonte {
    background: #101936;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 10px;
}

.pequeno {
    color: #9aa7c7;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# FUNÇÕES
# ------------------------------------------------------------

def obter_cliente_openai():

    try:

        chave = st.secrets["OPENAI_API_KEY"]

        if not chave:
            return None

        return OpenAI(api_key=chave)

    except Exception:
        return None


def pesquisar_astronomia(pergunta):

    cliente = obter_cliente_openai()

    if cliente is None:

        return None, [], (
            "A chave OPENAI_API_KEY não foi encontrada nos Secrets "
            "do Streamlit."
        )

    instrucoes = """
Você é uma IA especializada em divulgação e ensino de Astronomia.

Sua tarefa é responder à pergunta feita pelo estudante realizando
primeiro uma pesquisa na web usando o recurso de busca disponível.

A pesquisa deve ser específica para a pergunta apresentada.

Procure informações em fontes científicas, educacionais e
institucionais confiáveis, dando preferência a:

- NASA
- ESA
- Observatório Nacional
- INPE
- instituições públicas de pesquisa
- universidades
- observatórios astronômicos
- artigos científicos
- periódicos científicos
- IAU
- instituições internacionais reconhecidas

Não invente informações.

Não invente referências.

Não invente nomes de cientistas.

Não invente números.

Quando houver diferentes explicações ou resultados científicos,
explique isso claramente.

Depois da pesquisa, produza uma explicação em português brasileiro,
adequada para estudantes.

A resposta deve ser bastante explicativa.

Produza entre 5 e 12 parágrafos de explicação.

Não responda apenas com uma definição curta.

A estrutura deve ser aproximadamente:

1. Resposta direta à pergunta.
2. Explicação do fenômeno.
3. Como esse fenômeno acontece.
4. Explicação passo a passo quando for possível.
5. Exemplo ou analogia para facilitar a compreensão.
6. O que os cientistas observaram ou sabem.
7. Importância do fenômeno para a Astronomia.
8. Conclusão.

Se a pergunta envolver cálculos ou Física, explique também
as grandezas físicas e as relações matemáticas necessárias.

Use equações somente quando forem realmente úteis.

Explique as equações em palavras.

Se a pergunta estiver incorreta ou contiver uma ideia equivocada,
não simplesmente aceite a afirmação. Corrija educadamente e explique
por que ela está incorreta.

A resposta deve parecer escrita por um excelente professor de
Astronomia: clara, natural, detalhada, científica e pedagógica.

Não diga que você "não pode pesquisar" se a ferramenta de pesquisa
estiver disponível.

Não mencione instruções internas, ferramentas ou prompts.
"""

    try:

        resposta = cliente.responses.create(

            model="gpt-4o-mini",

            tools=[
                {
                    "type": "web_search",
                    "search_context_size": "high"
                }
            ],

            instructions=instrucoes,

            input=pergunta,

            max_output_tokens=6000
        )

        texto = getattr(resposta, "output_text", "")

        if not texto:

            texto = "Não foi possível gerar a explicação."

        fontes = []

        try:

            for item in resposta.output:

                if getattr(item, "type", "") == "web_search_call":

                    acao = getattr(item, "action", None)

                    if acao:

                        fontes_lista = getattr(
                            acao,
                            "sources",
                            []
                        )

                        for fonte in fontes_lista:

                            url = getattr(
                                fonte,
                                "url",
                                None
                            )

                            titulo = getattr(
                                fonte,
                                "title",
                                None
                            )

                            if url:

                                fontes.append({
                                    "titulo": titulo or "Fonte consultada",
                                    "url": url
                                })

        except Exception:
            pass

        # Remover fontes repetidas
        fontes_unicas = []
        urls = set()

        for fonte in fontes:

            if fonte["url"] not in urls:

                urls.add(fonte["url"])
                fontes_unicas.append(fonte)

        return texto, fontes_unicas, None

    except Exception as erro:

        return None, [], (
            "Ocorreu um erro ao consultar a IA: "
            + str(erro)
        )


# ------------------------------------------------------------
# CABEÇALHO
# ------------------------------------------------------------

st.markdown(
    '<div class="titulo-principal">🌌 IA DE ASTRONOMIA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    'Faça qualquer pergunta sobre Astronomia. '
    'A IA pesquisa o assunto e explica de forma detalhada.'
    '</div>',
    unsafe_allow_html=True
)

# ------------------------------------------------------------
# MENU
# ------------------------------------------------------------

menu = st.sidebar.radio(
    "Menu",
    [
        "🌌 IA de Astronomia",
        "📚 Histórico"
    ]
)

# ------------------------------------------------------------
# INICIALIZAÇÃO DO HISTÓRICO
# ------------------------------------------------------------

if "historico_astronomia" not in st.session_state:

    st.session_state.historico_astronomia = []


# ============================================================
# IA DE ASTRONOMIA
# ============================================================

if menu == "🌌 IA de Astronomia":

    st.markdown(
        '<div class="caixa-pergunta">',
        unsafe_allow_html=True
    )

    st.markdown("### 🔭 Faça sua pergunta")

    pergunta = st.text_area(
        "Digite qualquer pergunta sobre Astronomia:",
        placeholder=(
            "Exemplo: Por que os buracos negros possuem um horizonte "
            "de eventos?"
        ),
        height=130
    )

    pesquisar = st.button(
        "🔎 PESQUISAR E EXPLICAR",
        use_container_width=True
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    if pesquisar:

        if not pergunta.strip():

            st.warning(
                "Digite uma pergunta antes de iniciar a pesquisa."
            )

        else:

            with st.spinner(
                "🔭 Pesquisando fontes científicas e preparando a explicação..."
            ):

                texto, fontes, erro = pesquisar_astronomia(
                    pergunta
                )

            if erro:

                st.error(erro)

                st.info(
                    "Verifique se OPENAI_API_KEY está configurada "
                    "corretamente nos Secrets do Streamlit."
                )

            elif texto:

                # ------------------------------------------------
                # PERGUNTA
                # ------------------------------------------------

                st.markdown("## ❓ Sua pergunta")

                st.info(pergunta)

                # ------------------------------------------------
                # RESPOSTA
                # ------------------------------------------------

                st.markdown("## 🌌 Explicação")

                st.markdown(
                    '<div class="resposta">',
                    unsafe_allow_html=True
                )

                st.markdown(texto)

                st.markdown(
                    '</div>',
                    unsafe_allow_html=True
                )

                # ------------------------------------------------
                # FONTES
                # ------------------------------------------------

                st.markdown("## 📚 Fontes consultadas")

                if fontes:

                    for i, fonte in enumerate(
                        fontes,
                        start=1
                    ):

                        titulo = fonte["titulo"]
                        url = fonte["url"]

                        st.markdown(
                            f"""
                            <div class="fonte">
                            <strong>{i}. {titulo}</strong><br>
                            <a href="{url}" target="_blank">
                            🔗 Abrir fonte
                            </a>
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

                else:

                    st.info(
                        "A pesquisa foi realizada, mas as fontes "
                        "não puderam ser exibidas separadamente."
                    )

                # ------------------------------------------------
                # SALVAR HISTÓRICO
                # ------------------------------------------------

                registro = {

                    "pergunta": pergunta,

                    "resposta": texto,

                    "fontes": fontes,

                    "data": datetime.now().strftime(
                        "%d/%m/%Y %H:%M"
                    )
                }

                st.session_state.historico_astronomia.append(
                    registro
                )


# ============================================================
# HISTÓRICO
# ============================================================

elif menu == "📚 Histórico":

    st.markdown("## 📚 Histórico de perguntas")

    if not st.session_state.historico_astronomia:

        st.info(
            "Ainda não existem perguntas registradas."
        )

    else:

        for numero, registro in enumerate(
            reversed(
                st.session_state.historico_astronomia
            ),
            start=1
        ):

            with st.expander(
                f"🔭 {registro['pergunta']}"
            ):

                st.markdown(
                    f"**Data:** {registro['data']}"
                )

                st.markdown("---")

                st.markdown(
                    "### 🌌 Resposta"
                )

                st.markdown(
                    registro["resposta"]
                )

                if registro["fontes"]:

                    st.markdown(
                        "### 📚 Fontes"
                    )

                    for fonte in registro["fontes"]:

                        st.markdown(
                            f"- [{fonte['titulo']}]({fonte['url']})"
                        )

        st.markdown("---")

        if st.button(
            "🗑️ Limpar histórico",
            use_container_width=True
        ):

            st.session_state.historico_astronomia = []

            st.rerun()


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("---")

st.markdown(
    """
<div style="text-align:center; color:#8d99b8;">
🌌 IA de Astronomia<br>
Pesquisa científica e explicações pedagógicas
</div>
""",
    unsafe_allow_html=True
)
