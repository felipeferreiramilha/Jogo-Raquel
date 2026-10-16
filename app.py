import streamlit as st
import requests
import re
import html
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from datetime import datetime


# ============================================================
# CONFIGURAÇÃO DA PÁGINA
# ============================================================

st.set_page_config(
    page_title="🌌 Explorador de Astronomia",
    page_icon="🌌",
    layout="wide"
)


# ============================================================
# ESTILO
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #0b132b;
    color: white;
}

.block-container {
    max-width: 1200px;
    padding-top: 2rem;
}

.stButton > button {
    width: 100%;
    border-radius: 10px;
    font-weight: bold;
    padding: 10px;
}

.titulo {
    text-align: center;
    color: #4cc9f0;
    font-size: 36px;
    font-weight: bold;
}

.subtitulo {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background-color: #1c2541;
    padding: 25px;
    border-radius: 15px;
    border: 1px solid #4361ee;
    margin-bottom: 20px;
}

.pergunta {
    background-color: #16213e;
    padding: 20px;
    border-radius: 12px;
    border-left: 5px solid #4cc9f0;
    margin-bottom: 20px;
}

.fonte {
    background-color: #111827;
    padding: 15px;
    border-radius: 10px;
    margin-top: 10px;
}

.fonte a {
    color: #4cc9f0;
    text-decoration: none;
}

.aviso {
    background-color: #332701;
    border: 1px solid #f59e0b;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# ESTADO DO SISTEMA
# ============================================================

if "historico_explicacoes" not in st.session_state:
    st.session_state.historico_explicacoes = []

if "pesquisas_realizadas" not in st.session_state:
    st.session_state.pesquisas_realizadas = 0

if "ultima_pergunta" not in st.session_state:
    st.session_state.ultima_pergunta = ""

if "ultima_resposta" not in st.session_state:
    st.session_state.ultima_resposta = ""

if "modo_sistema" not in st.session_state:
    st.session_state.modo_sistema = "🌌 Pesquisa de Astronomia"


# ============================================================
# FONTES PRIORITÁRIAS
# ============================================================

FONTES_PRIORITARIAS = [
    "nasa.gov",
    "science.nasa.gov",
    "esa.int",
    "gov.br",
    "inpe.br",
    "on.br",
    "iau.org",
    "noirlab.edu",
    "arxiv.org"
]


# ============================================================
# FUNÇÃO PARA PESQUISAR NA WEB
# ============================================================

def pesquisar_web(pergunta, quantidade=8):

    """
    Pesquisa a pergunta utilizando o mecanismo público
    DuckDuckGo.

    Retorna uma lista de resultados contendo:
    título
    link
    descrição
    """

    try:

        url = "https://html.duckduckgo.com/html/"

        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/155.0 Safari/537.36"
            )
        }

        resposta = requests.post(
            url,
            data={"q": pergunta},
            headers=headers,
            timeout=20
        )

        if resposta.status_code != 200:
            return []

        soup = BeautifulSoup(
            resposta.text,
            "html.parser"
        )

        resultados = []

        blocos = soup.select(".result")

        for bloco in blocos:

            titulo_elemento = bloco.select_one(".result__title")

            link_elemento = bloco.select_one(
                ".result__a"
            )

            descricao_elemento = bloco.select_one(
                ".result__snippet"
            )

            if not titulo_elemento or not link_elemento:
                continue

            titulo = titulo_elemento.get_text(
                " ",
                strip=True
            )

            link = link_elemento.get("href", "")

            descricao = ""

            if descricao_elemento:
                descricao = descricao_elemento.get_text(
                    " ",
                    strip=True
                )

            if not link:
                continue

            resultados.append({
                "titulo": titulo,
                "link": link,
                "descricao": descricao
            })

            if len(resultados) >= quantidade:
                break

        return resultados

    except Exception:
        return []


# ============================================================
# EXTRAIR DOMÍNIO
# ============================================================

def obter_dominio(url):

    try:

        dominio = re.findall(
            r"https?://([^/]+)",
            url
        )

        if dominio:
            return dominio[0]

    except Exception:
        pass

    return ""


# ============================================================
# ORGANIZAR RESULTADOS
# ============================================================

def organizar_resultados(resultados):

    """

    Coloca fontes institucionais e científicas
    primeiro.
    """

    def pontuacao(resultado):

        dominio = obter_dominio(
            resultado["link"]
        ).lower()

        pontos = 0

        for fonte in FONTES_PRIORITARIAS:

            if fonte in dominio:
                pontos += 10

        return pontos

    return sorted(
        resultados,
        key=pontuacao,
        reverse=True
    )


# ============================================================
# LIMPAR TEXTO
# ============================================================

def limpar_texto(texto):

    texto = html.unescape(texto)

    texto = re.sub(
        r"\s+",
        " ",
        texto
    )

    return texto.strip()


# ============================================================
# GERAR EXPLICAÇÃO DIDÁTICA
# ============================================================

def gerar_explicacao(pergunta, resultados):

    """
    Constrói uma explicação utilizando as informações
    encontradas na pesquisa.

    O objetivo é apresentar:
    1. resposta direta
    2. explicação
    3. aprofundamento
    4. exemplo
    5. conclusão
    """

    if not resultados:

        return (
            "Não consegui encontrar resultados confiáveis "
            "para essa pergunta neste momento."
        )

    pergunta_limpa = limpar_texto(pergunta)

    textos = []

    for resultado in resultados[:6]:

        titulo = limpar_texto(
            resultado["titulo"]
        )

        descricao = limpar_texto(
            resultado["descricao"]
        )

        if descricao:

            textos.append(
                f"{titulo}: {descricao}"
            )

    contexto = "\n".join(textos)

    # --------------------------------------------------------
    # Tenta utilizar uma API de IA configurada pelo usuário.
    # --------------------------------------------------------

    try:

        api_key = st.secrets["OPENAI_API_KEY"]

    except Exception:

        api_key = None


    if api_key:

        try:

            prompt = f"""
Você é um professor de Astronomia e Física especializado
em divulgação científica e ensino para estudantes.

O aluno fez a seguinte pergunta:

{pergunta_limpa}

A pesquisa na Web encontrou estas informações:

{contexto}

Escreva uma explicação científica correta, clara, fluida
e progressiva.

REGRAS:

1. Responda diretamente à pergunta logo no começo.
2. Depois explique o conceito passo a passo.
3. Não trate o aluno como se fosse incapaz.
4. Use linguagem simples, mas cientificamente correta.
5. Se houver uma analogia, deixe claro que é uma analogia.
6. Não invente dados.
7. Não invente cientistas.
8. Não invente fontes.
9. Diferencie fatos científicos de hipóteses.
10. Se houver alguma controvérsia científica, explique.
11. Se houver matemática importante, apresente a equação
    e explique o significado das grandezas.
12. Relacione o fenômeno com Astronomia sempre que possível.
13. Termine com uma pequena conclusão.
14. Não diga que pesquisou algo que não esteja no contexto.

Organize a resposta com:

## Resposta rápida

## Entendendo melhor

## Como isso acontece

## Um exemplo

## O que a ciência sabe atualmente

## Conclusão

Escreva de maneira natural, como um professor explicando
o assunto para um estudante.
"""

            resposta = requests.post(
                "https://api.openai.com/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "gpt-4o-mini",
                    "messages": [
                        {
                            "role": "system",
                            "content": (
                                "Você é um professor de "
                                "Astronomia e Física."
                            )
                        },
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    "temperature": 0.3
                },
                timeout=60
            )

            if resposta.status_code == 200:

                dados = resposta.json()

                return dados["choices"][0]["message"]["content"]

        except Exception:
            pass


    # --------------------------------------------------------
    # MODO SEM API DE IA
    # --------------------------------------------------------

    explicacao = f"""
## Resposta rápida

A pergunta pesquisada foi:

**{pergunta_limpa}**

A pesquisa encontrou informações em diferentes páginas
relacionadas ao tema.

## O que encontramos

"""

    for resultado in resultados[:5]:

        titulo = limpar_texto(
            resultado["titulo"]
        )

        descricao = limpar_texto(
            resultado["descricao"]
        )

        if descricao:

            explicacao += (
                f"### {titulo}\n\n"
                f"{descricao}\n\n"
            )

    explicacao += """
## Entendendo melhor

As informações acima foram obtidas a partir dos resultados
encontrados na pesquisa. Para uma explicação mais profunda,
o professor pode configurar uma API de Inteligência
Artificial no aplicativo.

## Conclusão

A resposta apresentada foi construída a partir das fontes
encontradas na pesquisa. Consulte as fontes abaixo para
aprofundar o estudo.
"""

    return explicacao


# ============================================================
# REALIZAR PESQUISA
# ============================================================

def realizar_pesquisa(pergunta):

    with st.spinner(
        "🔭 Pesquisando fontes científicas na Web..."
    ):

        resultados = pesquisar_web(
            pergunta,
            quantidade=10
        )

    if not resultados:

        st.error(
            "Não consegui encontrar resultados. "
            "Tente reformular a pergunta."
        )

        return

    resultados = organizar_resultados(
        resultados
    )

    with st.spinner(
        "🧠 Organizando as informações..."
    ):

        explicacao = gerar_explicacao(
            pergunta,
            resultados
        )

    st.session_state.ultima_pergunta = pergunta

    st.session_state.ultima_resposta = explicacao

    st.session_state.pesquisas_realizadas += 1

    st.session_state.historico_explicacoes.insert(
        0,
        {
            "pergunta": pergunta,
            "resposta": explicacao,
            "fontes": resultados,
            "data": datetime.now().strftime(
                "%d/%m/%Y %H:%M"
            )
        }
    )


# ============================================================
# CABEÇALHO
# ============================================================

st.markdown(
    '<div class="titulo">🌌 Explorador de Astronomia</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    'Faça uma pergunta sobre o Universo e investigue o assunto '
    'com ajuda de fontes científicas.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# MENU LATERAL
# ============================================================

st.sidebar.title("🔭 Painel")

st.sidebar.markdown(
    "### 🌌 Pesquisa de Astronomia"
)

st.sidebar.info(
    "O aluno pode escrever uma pergunta livremente. "
    "O sistema pesquisa a Web e organiza as informações "
    "de maneira didática."
)

st.sidebar.markdown("---")

st.sidebar.metric(
    "Pesquisas realizadas",
    st.session_state.pesquisas_realizadas
)

st.sidebar.markdown("---")


# ============================================================
# BOTÃO LIMPAR HISTÓRICO
# ============================================================

if st.sidebar.button(
    "🧹 Limpar histórico"
):

    st.session_state.historico_explicacoes = []

    st.session_state.ultima_pergunta = ""

    st.session_state.ultima_resposta = ""

    st.rerun()


# ============================================================
# ÁREA PRINCIPAL
# ============================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.markdown(
    "### 🔎 Faça sua pergunta"
)

st.write(
    "Você não precisa escolher um tema pronto. "
    "Escreva exatamente aquilo que deseja saber."
)

pergunta = st.text_area(
    "Pergunta do aluno",
    placeholder=(
        "Exemplo: Por que a Lua não cai na Terra?\n\n"
        "Ou: Como sabemos que existem buracos negros?\n\n"
        "Ou: Como nascem as estrelas?"
    ),
    height=130
)

pesquisar = st.button(
    "🔭 Pesquisar e explicar",
    type="primary"
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# EXECUTAR PESQUISA
# ============================================================

if pesquisar:

    if not pergunta.strip():

        st.warning(
            "Digite uma pergunta antes de pesquisar."
        )

    elif len(pergunta.strip()) < 5:

        st.warning(
            "Digite uma pergunta um pouco mais completa."
        )

    else:

        realizar_pesquisa(
            pergunta.strip()
        )


# ============================================================
# MOSTRAR ÚLTIMA RESPOSTA
# ============================================================

if st.session_state.ultima_resposta:

    st.markdown("---")

    st.markdown(
        '<div class="pergunta">',
        unsafe_allow_html=True
    )

    st.markdown(
        "### 👨‍🎓 Pergunta do aluno"
    )

    st.markdown(
        st.session_state.ultima_pergunta
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="card">',
        unsafe_allow_html=True
    )

    st.markdown(
        st.session_state.ultima_resposta
    )

    st.markdown(
        '</div>',
        unsafe_allow_html=True
    )


# ============================================================
# FONTES DA ÚLTIMA PESQUISA
# ============================================================

if st.session_state.historico_explicacoes:

    ultima = (
        st.session_state.historico_explicacoes[0]
    )

    st.markdown("---")

    st.subheader(
        "📚 Fontes utilizadas na pesquisa"
    )

    st.write(
        "As páginas abaixo são apresentadas para que "
        "o aluno e o professor possam consultar "
        "diretamente as informações."
    )

    for i, fonte in enumerate(
        ultima["fontes"][:8],
        1
    ):

        titulo = html.escape(
            fonte["titulo"]
        )

        link = html.escape(
            fonte["link"],
            quote=True
        )

        dominio = obter_dominio(
            fonte["link"]
        )

        st.markdown(
            f"""
            <div class="fonte">

            <strong>{i}. {titulo}</strong>

            <br>

            <small>
            🌐 {html.escape(dominio)}
            </small>

            <br><br>

            <a href="{link}" target="_blank">
            🔗 Abrir fonte original
            </a>

            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# HISTÓRICO
# ============================================================

if len(
    st.session_state.historico_explicacoes
) > 1:

    st.markdown("---")

    st.subheader(
        "🕘 Histórico de perguntas"
    )

    for i, item in enumerate(
        st.session_state.historico_explicacoes[1:],
        1
    ):

        with st.expander(
            f"🔭 {item['pergunta']}"
        ):

            st.markdown(
                item["resposta"]
            )

            st.caption(
                f"Pesquisa realizada em "
                f"{item['data']}"
            )


# ============================================================
# ÁREA PEDAGÓGICA
# ============================================================

st.markdown("---")

st.markdown(
    """
### 👨‍🏫 Como utilizar

O aluno pode começar com uma pergunta simples e,
depois, continuar investigando.

Por exemplo:

**Pergunta 1:**  
Por que o céu é azul?

**Pergunta 2:**  
O que acontece com a luz quando entra na atmosfera?

**Pergunta 3:**  
Por que o céu de Marte é diferente?

**Pergunta 4:**  
Como sabemos disso?

Dessa maneira, a ferramenta pode ser utilizada como
um ponto de partida para uma investigação de Astronomia,
em vez de simplesmente entregar uma resposta pronta.
"""
)


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("---")

st.caption(
    "🌌 Explorador de Astronomia — ferramenta educacional "
    "para pesquisa e aprendizagem."
)
