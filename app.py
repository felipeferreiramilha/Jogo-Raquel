import streamlit as st
import requests
import re
import html
from urllib.parse import quote_plus
from datetime import datetime


# ============================================================
# CONFIGURAÇÃO
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
# ESTADO
# ============================================================

if "historico_explicacoes" not in st.session_state:
    st.session_state.historico_explicacoes = []

if "pesquisas_realizadas" not in st.session_state:
    st.session_state.pesquisas_realizadas = 0

if "ultima_pergunta" not in st.session_state:
    st.session_state.ultima_pergunta = ""

if "ultima_resposta" not in st.session_state:
    st.session_state.ultima_resposta = ""

if "fontes_atuais" not in st.session_state:
    st.session_state.fontes_atuais = []


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
# FUNÇÃO DE LIMPEZA
# ============================================================

def limpar_texto(texto):

    if not texto:
        return ""

    texto = html.unescape(texto)

    texto = re.sub(
        r"<[^>]+>",
        " ",
        texto
    )

    texto = re.sub(
        r"\s+",
        " ",
        texto
    )

    return texto.strip()


# ============================================================
# PESQUISA NA WEB
# ============================================================

def pesquisar_web(pergunta):

    resultados = []

    try:

        consulta = quote_plus(
            pergunta
        )

        # API pública do DuckDuckGo
        url = (
            "https://api.duckduckgo.com/"
            f"?q={consulta}"
            "&format=json"
            "&no_html=1"
            "&skip_disambig=0"
        )

        resposta = requests.get(
            url,
            timeout=20,
            headers={
                "User-Agent":
                "Mozilla/5.0"
            }
        )

        if resposta.status_code == 200:

            dados = resposta.json()

            # ------------------------------------------------
            # RESPOSTA PRINCIPAL
            # ------------------------------------------------

            if dados.get("AbstractText"):

                resultados.append({
                    "titulo": (
                        dados.get("Heading")
                        or "Informação encontrada"
                    ),
                    "descricao": dados.get(
                        "AbstractText",
                        ""
                    ),
                    "link": dados.get(
                        "AbstractURL",
                        ""
                    )
                })

            # ------------------------------------------------
            # TÓPICOS RELACIONADOS
            # ------------------------------------------------

            def adicionar_topicos(lista):

                for item in lista:

                    if len(resultados) >= 10:
                        return

                    if isinstance(item, dict):

                        texto = item.get(
                            "Text",
                            ""
                        )

                        primeiro_url = item.get(
                            "FirstURL",
                            ""
                        )

                        if texto:

                            resultados.append({
                                "titulo": texto.split(
                                    " - "
                                )[0],
                                "descricao": texto,
                                "link": primeiro_url
                            })

                        if item.get(
                            "Topics"
                        ):

                            adicionar_topicos(
                                item["Topics"]
                            )

            adicionar_topicos(
                dados.get(
                    "RelatedTopics",
                    []
                )
            )

    except Exception:
        pass


    # ========================================================
    # PESQUISA DIRETA EM FONTES CIENTÍFICAS
    # ========================================================

    fontes_busca = [
        (
            "NASA",
            "https://www.google.com/search?q="
            + quote_plus(
                "site:nasa.gov "
                + pergunta
            )
        ),
        (
            "ESA",
            "https://www.google.com/search?q="
            + quote_plus(
                "site:esa.int "
                + pergunta
            )
        ),
        (
            "INPE",
            "https://www.google.com/search?q="
            + quote_plus(
                "site:inpe.br "
                + pergunta
            )
        ),
        (
            "Observatório Nacional",
            "https://www.google.com/search?q="
            + quote_plus(
                "site:gov.br/on "
                + pergunta
            )
        )
    ]


    # Adiciona páginas de pesquisa como fontes
    # para consulta direta do aluno.

    for nome, link in fontes_busca:

        resultados.append({
            "titulo": (
                f"Pesquisar sobre '{pergunta}' "
                f"em {nome}"
            ),
            "descricao": (
                f"Pesquisa direcionada para encontrar "
                f"informações sobre {pergunta} "
                f"em fontes relacionadas a {nome}."
            ),
            "link": link
        })


    return organizar_resultados(
        resultados
    )


# ============================================================
# ORGANIZAR RESULTADOS
# ============================================================

def obter_dominio(url):

    try:

        resultado = re.search(
            r"https?://([^/]+)",
            url
        )

        if resultado:
            return resultado.group(1)

    except Exception:
        pass

    return ""


def pontuar_fonte(resultado):

    dominio = obter_dominio(
        resultado.get("link", "")
    ).lower()

    pontos = 0

    for fonte in FONTES_PRIORITARIAS:

        if fonte in dominio:
            pontos += 10

    return pontos


def organizar_resultados(resultados):

    resultados = sorted(
        resultados,
        key=pontuar_fonte,
        reverse=True
    )

    # Remove resultados duplicados

    finais = []

    links_vistos = set()

    for resultado in resultados:

        link = resultado.get(
            "link",
            ""
        )

        if link in links_vistos:
            continue

        links_vistos.add(link)

        finais.append(
            resultado
        )

    return finais[:10]


# ============================================================
# GERADOR DE RESPOSTA
# ============================================================

def gerar_resposta_sem_IA(
    pergunta,
    resultados
):

    pergunta = limpar_texto(
        pergunta
    )

    resposta = f"""
## 🔭 Resposta à pergunta

**{pergunta}**

A pesquisa encontrou informações relacionadas ao tema.
Abaixo estão os principais resultados encontrados.

## 🌌 O que encontramos

"""

    resultados_reais = 0

    for resultado in resultados:

        titulo = limpar_texto(
            resultado.get(
                "titulo",
                ""
            )
        )

        descricao = limpar_texto(
            resultado.get(
                "descricao",
                ""
            )
        )

        if not titulo:
            continue

        if not descricao:
            continue

        resultados_reais += 1

        resposta += f"""
### {titulo}

{descricao}

"""

        if resultados_reais >= 5:
            break


    if resultados_reais == 0:

        resposta += """
Não foi possível obter uma explicação detalhada
diretamente dos resultados da pesquisa.

Use as fontes indicadas abaixo para continuar
a investigação.
"""


    resposta += """

## 🧠 Como interpretar a pesquisa

É importante lembrar que uma pesquisa científica
não deve depender de uma única página.

Quando estudamos Astronomia, devemos comparar
informações, observar quem produziu o conteúdo e,
sempre que possível, dar preferência a instituições
científicas, universidades, observatórios e agências
espaciais.

## 📚 Conclusão

A pergunta foi pesquisada utilizando resultados
disponíveis na Web. As fontes apresentadas abaixo
podem ser abertas pelo aluno para aprofundar
o estudo.
"""

    return resposta


# ============================================================
# GERADOR COM INTELIGÊNCIA ARTIFICIAL
# ============================================================

def gerar_resposta_com_ia(
    pergunta,
    resultados
):

    try:

        api_key = st.secrets[
            "OPENAI_API_KEY"
        ]

    except Exception:

        return None


    contexto = ""

    for resultado in resultados[:8]:

        titulo = limpar_texto(
            resultado.get(
                "titulo",
                ""
            )
        )

        descricao = limpar_texto(
            resultado.get(
                "descricao",
                ""
            )
        )

        if descricao:

            contexto += (
                f"\nFonte: {titulo}\n"
                f"Informação: {descricao}\n"
            )


    prompt = f"""
Você é um professor de Astronomia e Física.

Um estudante fez esta pergunta:

{pergunta}

A pesquisa encontrou as seguintes informações:

{contexto}

Produza uma explicação científica, detalhada,
fluida e didática.

A resposta deve:

1. Responder diretamente à pergunta.
2. Começar pelo conceito mais simples.
3. Desenvolver a explicação passo a passo.
4. Explicar os termos científicos importantes.
5. Utilizar analogias somente quando ajudarem.
6. Não inventar informações.
7. Não inventar cientistas.
8. Não inventar resultados científicos.
9. Não apresentar hipótese como fato.
10. Informar quando algo ainda é objeto de pesquisa.
11. Usar equações quando forem importantes.
12. Explicar cada variável de uma equação.
13. Relacionar o fenômeno com Astronomia.
14. Ser adequada para estudantes.
15. Não infantilizar excessivamente a explicação.

Organize assim:

## Resposta rápida

## Entendendo o fenômeno

## Explicação passo a passo

## Exemplo

## O que os cientistas sabem

## Conclusão
"""

    try:

        resposta = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={
                "Authorization":
                    f"Bearer {api_key}",
                "Content-Type":
                    "application/json"
            },
            json={
                "model": "gpt-4o-mini",
                "messages": [
                    {
                        "role": "system",
                        "content":
                        "Você é um professor de Astronomia."
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

            return (
                dados[
                    "choices"
                ][0][
                    "message"
                ][
                    "content"
                ]
            )

    except Exception:

        return None

    return None


# ============================================================
# REALIZAR PESQUISA
# ============================================================

def realizar_pesquisa(pergunta):

    with st.spinner(
        "🔭 Pesquisando na Web..."
    ):

        resultados = pesquisar_web(
            pergunta
        )

    if not resultados:

        st.error(
            "Não consegui encontrar resultados "
            "para essa pergunta."
        )

        return


    with st.spinner(
        "🧠 Organizando a explicação..."
    ):

        resposta = gerar_resposta_com_ia(
            pergunta,
            resultados
        )

    # Se não existir API, utiliza modo básico.

    if not resposta:

        resposta = gerar_resposta_sem_IA(
            pergunta,
            resultados
        )


    st.session_state.ultima_pergunta = pergunta

    st.session_state.ultima_resposta = resposta

    st.session_state.fontes_atuais = resultados

    st.session_state.pesquisas_realizadas += 1

    st.session_state.historico_explicacoes.insert(
        0,
        {
            "pergunta": pergunta,
            "resposta": resposta,
            "fontes": resultados,
            "data": datetime.now().strftime(
                "%d/%m/%Y %H:%M"
            )
        }
    )


# ============================================================
# TÍTULO
# ============================================================

st.markdown(
    '<div class="titulo">'
    '🌌 Explorador de Astronomia'
    '</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">'
    'Pergunte sobre o Universo, pesquise e aprenda.'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title(
    "🔭 Painel do Explorador"
)

st.sidebar.info(
    "O aluno pode escrever livremente "
    "qualquer pergunta relacionada à Astronomia."
)

st.sidebar.metric(
    "Pesquisas realizadas",
    st.session_state.pesquisas_realizadas
)

st.sidebar.markdown("---")

if st.sidebar.button(
    "🧹 Limpar histórico"
):

    st.session_state.historico_explicacoes = []

    st.session_state.ultima_pergunta = ""

    st.session_state.ultima_resposta = ""

    st.session_state.fontes_atuais = []

    st.rerun()


# ============================================================
# PERGUNTA
# ============================================================

st.markdown(
    '<div class="card">',
    unsafe_allow_html=True
)

st.subheader(
    "🔎 O que você quer saber?"
)

st.write(
    "Escreva a pergunta exatamente como você faria "
    "para um professor."
)

pergunta = st.text_area(
    "Pergunta do aluno",
    placeholder=(
        "Exemplo:\n\n"
        "Por que a Lua não cai na Terra?\n\n"
        "Como nasce uma estrela?\n\n"
        "Como sabemos que existem buracos negros?\n\n"
        "Por que Plutão não é mais considerado planeta?"
    ),
    height=160
)

botao = st.button(
    "🔭 Pesquisar e explicar",
    type="primary"
)

st.markdown(
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PESQUISAR
# ============================================================

if botao:

    if not pergunta.strip():

        st.warning(
            "Digite uma pergunta primeiro."
        )

    elif len(pergunta.strip()) < 5:

        st.warning(
            "Faça uma pergunta um pouco mais completa."
        )

    else:

        realizar_pesquisa(
            pergunta.strip()
        )


# ============================================================
# RESPOSTA
# ============================================================

if st.session_state.ultima_resposta:

    st.markdown("---")

    st.markdown(
        '<div class="pergunta">',
        unsafe_allow_html=True
    )

    st.subheader(
        "👨‍🎓 Pergunta do aluno"
    )

    st.write(
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
# FONTES
# ============================================================

if st.session_state.fontes_atuais:

    st.markdown("---")

    st.subheader(
        "📚 Fontes da pesquisa"
    )

    st.write(
        "Estas são as páginas encontradas durante "
        "a pesquisa. O aluno pode abrir as fontes "
        "para verificar e aprofundar as informações."
    )


    for numero, fonte in enumerate(
        st.session_state.fontes_atuais,
        1
    ):

        titulo = limpar_texto(
            fonte.get(
                "titulo",
                "Fonte"
            )
        )

        descricao = limpar_texto(
            fonte.get(
                "descricao",
                ""
            )
        )

        link = fonte.get(
            "link",
            ""
        )

        dominio = obter_dominio(
            link
        )


        st.markdown(
            f"""
            <div class="fonte">

            <strong>
            {numero}. {html.escape(titulo)}
            </strong>

            <br><br>

            <small>
            🌐 {html.escape(dominio)}
            </small>

            <br><br>

            {html.escape(descricao)}

            <br><br>

            <a href="{html.escape(link, quote=True)}"
               target="_blank">
            🔗 Abrir fonte
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
        "🕘 Histórico de pesquisas"
    )

    for item in (
        st.session_state.historico_explicacoes[1:]
    ):

        with st.expander(
            "🔭 " + item["pergunta"]
        ):

            st.markdown(
                item["resposta"]
            )

            st.caption(
                "Pesquisado em "
                + item["data"]
            )


# ============================================================
# ORIENTAÇÃO PEDAGÓGICA
# ============================================================

st.markdown("---")

st.markdown(
    """
### 👨‍🏫 Sugestão para investigação

O aluno pode fazer uma sequência de perguntas.

Por exemplo:

**1.** Como nasce uma estrela?

**2.** O que acontece dentro dela?

**3.** Por que ela começa a produzir energia?

**4.** O que acontece quando o combustível acaba?

**5.** Todas as estrelas terminam da mesma maneira?

Assim, a ferramenta pode ser utilizada para construir
uma investigação de Astronomia, e não apenas para
receber uma resposta isolada.
"""
)


# ============================================================
# RODAPÉ
# ============================================================

st.markdown("---")

st.caption(
    "🌌 Explorador de Astronomia — ferramenta educacional"
)
