# ============================================================
# IA DE ASTRONOMIA — VERSÃO SIMPLES PARA CRIANÇAS
# ============================================================
#
# NÃO USA:
# openai
# bs4
#
# USA APENAS:
# streamlit
# requests
#
# A criança pode perguntar QUALQUER coisa sobre Astronomia.
#
# O programa:
# 1. Pesquisa a pergunta.
# 2. Procura informações em diferentes fontes.
# 3. Organiza os resultados.
# 4. Cria explicações simples.
# 5. Mostra um parágrafo para cada aspecto encontrado.
# 6. Mostra as fontes.
#
# ============================================================

import requests
import html
import re
from urllib.parse import quote_plus


# ============================================================
# FONTES PRIORITÁRIAS
# ============================================================

FONTES_ASTRONOMIA = [

    {
        "nome": "NASA",
        "dominio": "nasa.gov"
    },

    {
        "nome": "ESA",
        "dominio": "esa.int"
    },

    {
        "nome": "Observatório Nacional",
        "dominio": "on.br"
    },

    {
        "nome": "INPE",
        "dominio": "inpe.br"
    },

    {
        "nome": "IAU",
        "dominio": "iau.org"
    },

    {
        "nome": "NOIRLab",
        "dominio": "noirlab.edu"
    },

    {
        "nome": "Scientific American",
        "dominio": "scientificamerican.com"
    }

]


# ============================================================
# PESQUISA NA WEB
# ============================================================

def pesquisar_web_astronomia(pergunta):

    resultados = []

    pergunta_limpa = pergunta.strip()

    if not pergunta_limpa:

        return []


    # --------------------------------------------------------
    # 1. DUCKDUCKGO
    # --------------------------------------------------------

    try:

        url = (
            "https://api.duckduckgo.com/"
            "?q="
            + quote_plus(pergunta_limpa)
            + "&format=json"
            + "&no_html=1"
            + "&skip_disambig=0"
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


            # -----------------------------------------------
            # RESPOSTA PRINCIPAL
            # -----------------------------------------------

            abstract = dados.get(
                "AbstractText",
                ""
            )


            abstract_url = dados.get(
                "AbstractURL",
                ""
            )


            heading = dados.get(
                "Heading",
                ""
            )


            if abstract:

                resultados.append({

                    "fonte":
                    "DuckDuckGo",

                    "titulo":
                    heading
                    if heading
                    else
                    pergunta_limpa,

                    "texto":
                    abstract,

                    "url":
                    abstract_url

                })


            # -----------------------------------------------
            # RESULTADOS RELACIONADOS
            # -----------------------------------------------

            related = dados.get(
                "RelatedTopics",
                []
            )


            for item in related:

                if not isinstance(
                    item,
                    dict
                ):

                    continue


                texto = item.get(
                    "Text",
                    ""
                )


                url_item = item.get(
                    "FirstURL",
                    ""
                )


                if texto:

                    resultados.append({

                        "fonte":
                        "DuckDuckGo",

                        "titulo":
                        texto[:120],

                        "texto":
                        texto,

                        "url":
                        url_item

                    })


    except Exception:

        pass


    # ========================================================
    # 2. PESQUISAS DIRECIONADAS
    # ========================================================

    for fonte in FONTES_ASTRONOMIA:

        try:

            consulta = (
                pergunta_limpa
                + " "
                + fonte["dominio"]
            )


            url_busca = (
                "https://www.google.com/search?q="
                + quote_plus(
                    consulta
                )
            )


            resultados.append({

                "fonte":
                fonte["nome"],

                "titulo":
                (
                    "Pesquisar "
                    + pergunta_limpa
                    + " em "
                    + fonte["nome"]
                ),

                "texto":
                (
                    "Pesquisa direcionada "
                    "para encontrar informações "
                    "sobre "
                    + pergunta_limpa
                    + " em fontes relacionadas "
                    "a "
                    + fonte["nome"]
                    + "."
                ),

                "url":
                url_busca

            })


        except Exception:

            continue


    return resultados


# ============================================================
# LIMPAR TEXTO
# ============================================================

def limpar_texto(texto):

    if not texto:

        return ""


    texto = html.unescape(
        texto
    )


    texto = re.sub(
        r"\s+",
        " ",
        texto
    )


    return texto.strip()


# ============================================================
# IDENTIFICAR ASSUNTOS
# ============================================================

def identificar_aspectos(pergunta):

    pergunta = pergunta.lower()


    aspectos = []


    # --------------------------------------------------------
    # BURACO NEGRO
    # --------------------------------------------------------

    if (
        "buraco negro" in pergunta
        or
        "buracos negros" in pergunta
    ):

        aspectos = [

            (
                "🌌 O que são",
                "Buracos negros são regiões do espaço onde a gravidade é extremamente forte. Existe uma região chamada horizonte de eventos e, depois de atravessá-la, não é possível enviar sinais para um observador que esteja fora do buraco negro."
            ),

            (
                "⭐ Como podem se formar",
                "Alguns buracos negros podem surgir quando estrelas muito massivas chegam ao fim de suas vidas. Depois que o combustível da estrela acaba, seu núcleo pode sofrer um forte colapso gravitacional."
            ),

            (
                "🌀 A gravidade",
                "A grande quantidade de matéria concentrada em uma região muito pequena produz um campo gravitacional extremamente intenso. Por isso, a luz também pode ficar presa depois de atravessar o horizonte de eventos."
            ),

            (
                "🚪 Horizonte de eventos",
                "O horizonte de eventos pode ser imaginado como uma fronteira ao redor do buraco negro. Depois de ultrapassar essa fronteira, não existe um caminho conhecido para que a informação volte para um observador distante."
            ),

            (
                "🔭 Como sabemos que existem",
                "Os astrônomos não observam um buraco negro diretamente como observam uma estrela brilhante. Em vez disso, eles estudam os efeitos que ele produz sobre estrelas, gás, luz e outros objetos próximos."
            ),

            (
                "🌌 Buracos negros supermassivos",
                "Existem buracos negros muito maiores chamados buracos negros supermassivos. Muitos deles estão localizados no centro de galáxias. No centro da Via Láctea existe um deles chamado Sagittarius A*."
            ),

            (
                "💡 Eles são como aspiradores?",
                "Não. Um buraco negro não funciona como um aspirador espacial que suga tudo ao redor. Se uma estrela estivesse longe de um buraco negro e a massa fosse a mesma de outro objeto, sua órbita poderia ser semelhante à que teria ao redor desse outro objeto."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # ESTRELA
    # --------------------------------------------------------

    if "estrela" in pergunta:

        aspectos = [

            (
                "⭐ O que é uma estrela",
                "Uma estrela é uma enorme esfera de gás muito quente. Em seu interior acontecem processos que liberam uma enorme quantidade de energia, fazendo com que ela brilhe."
            ),

            (
                "🔥 Como uma estrela produz energia",
                "No interior de muitas estrelas acontece fusão nuclear. Nesse processo, núcleos atômicos leves podem se unir e liberar energia."
            ),

            (
                "🌌 Onde elas nascem",
                "As estrelas podem nascer dentro de grandes nuvens de gás e poeira chamadas nebulosas. A gravidade faz parte do processo que reúne o material até formar uma nova estrela."
            ),

            (
                "💥 Como elas morrem",
                "O destino de uma estrela depende principalmente de sua massa. Algumas terminam como anãs brancas, enquanto estrelas muito massivas podem terminar em eventos extremamente energéticos e deixar estrelas de nêutrons ou buracos negros."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # PLANETA
    # --------------------------------------------------------

    if "planeta" in pergunta:

        aspectos = [

            (
                "🪐 O que é um planeta",
                "Um planeta é um corpo celeste que orbita uma estrela ou outro objeto astronômico. No Sistema Solar, os planetas também possuem massa suficiente para assumir uma forma aproximadamente arredondada."
            ),

            (
                "☀️ Como eles orbitam",
                "Os planetas permanecem em órbita porque possuem movimento e ao mesmo tempo sofrem a atração gravitacional da estrela."
            ),

            (
                "🌍 Existem outros planetas?",
                "Sim. Os astrônomos já descobriram milhares de exoplanetas, que são planetas localizados fora do Sistema Solar."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # LUA
    # --------------------------------------------------------

    if (
        "lua" in pergunta
        or
        "satélite natural" in pergunta
    ):

        aspectos = [

            (
                "🌙 O que é a Lua",
                "A Lua é o satélite natural da Terra. Ela não produz luz própria como uma estrela; o brilho que vemos é principalmente luz do Sol refletida por sua superfície."
            ),

            (
                "🌍 Por que ela orbita a Terra",
                "A gravidade da Terra mantém a Lua em órbita. Ao mesmo tempo, a Lua possui movimento, fazendo com que ela não simplesmente caia diretamente sobre nosso planeta."
            ),

            (
                "🌊 Lua e marés",
                "A atração gravitacional da Lua participa da produção das marés oceânicas. O Sol também exerce influência nesse fenômeno."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # SOL
    # --------------------------------------------------------

    if "sol" in pergunta:

        aspectos = [

            (
                "☀️ O que é o Sol",
                "O Sol é uma estrela localizada no centro do Sistema Solar. Ele é muito maior que a Terra e contém a maior parte da massa do Sistema Solar."
            ),

            (
                "🔥 Como o Sol produz energia",
                "No interior do Sol acontece fusão nuclear. O processo transforma núcleos de hidrogênio em hélio e libera energia."
            ),

            (
                "🌍 Por que o Sol é importante",
                "A energia do Sol é fundamental para a vida na Terra. Ela participa do clima, da fotossíntese e de muitos processos que acontecem em nosso planeta."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # GALÁXIA
    # --------------------------------------------------------

    if "galáxia" in pergunta:

        aspectos = [

            (
                "🌌 O que é uma galáxia",
                "Uma galáxia é uma enorme estrutura formada por estrelas, gás, poeira, matéria escura e outros componentes ligados principalmente pela gravidade."
            ),

            (
                "🌠 A Via Láctea",
                "A Via Láctea é a galáxia onde está localizado o Sistema Solar. Ela contém uma quantidade enorme de estrelas."
            ),

            (
                "🌀 Tipos de galáxias",
                "Existem diferentes tipos de galáxias. Algumas possuem braços espirais, outras apresentam formas elípticas e também existem galáxias com formatos irregulares."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # BIG BANG
    # --------------------------------------------------------

    if (
        "big bang" in pergunta
        or
        "origem do universo" in pergunta
    ):

        aspectos = [

            (
                "🌌 O que é o Big Bang",
                "O Big Bang é o nome dado ao modelo científico que descreve a evolução do universo a partir de um estado inicial extremamente quente e denso."
            ),

            (
                "📈 O universo está se expandindo",
                "As observações mostram que, em grandes escalas, as galáxias estão se afastando umas das outras. Isso é descrito como expansão do universo."
            ),

            (
                "📻 Radiação cósmica de fundo",
                "Existe uma radiação muito antiga observável em todas as direções do céu. Ela é chamada de radiação cósmica de fundo e é uma importante evidência do universo primordial."
            ),

            (
                "⭐ Formação das primeiras estrelas",
                "Depois das primeiras etapas da evolução cósmica, a matéria começou a se organizar pela gravidade, formando as primeiras estrelas e posteriormente estruturas maiores."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # MATÉRIA ESCURA
    # --------------------------------------------------------

    if "matéria escura" in pergunta:

        aspectos = [

            (
                "🌑 O que é matéria escura",
                "Matéria escura é o nome dado a um componente que não vemos diretamente pela luz, mas cuja existência é estudada por causa de seus efeitos gravitacionais."
            ),

            (
                "🌀 Galáxias",
                "Uma das evidências estudadas envolve a maneira como as estrelas se movimentam dentro das galáxias. Esses movimentos sugerem que existe mais massa gravitacional do que conseguimos observar diretamente."
            ),

            (
                "🔭 Como os cientistas estudam",
                "Os pesquisadores procuram efeitos gravitacionais associados à matéria escura, incluindo movimentos de estrelas e galáxias e fenômenos de lentes gravitacionais."
            ),

            (
                "❓ Ainda sabemos tudo?",
                "Não. A natureza exata da matéria escura continua sendo uma das grandes perguntas da Física e da Astronomia."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # EXOPLANETAS
    # --------------------------------------------------------

    if "exoplaneta" in pergunta:

        aspectos = [

            (
                "🪐 O que é um exoplaneta",
                "Um exoplaneta é um planeta que está fora do nosso Sistema Solar. Ele pode orbitar uma estrela diferente do Sol."
            ),

            (
                "🔭 Como são descobertos",
                "Uma das maneiras de descobrir exoplanetas é observar pequenas quedas no brilho de uma estrela quando um planeta passa na frente dela."
            ),

            (
                "🌍 Eles podem ter vida?",
                "Alguns exoplanetas estão em regiões onde as condições podem ser interessantes para a busca por ambientes habitáveis. Porém, encontrar um planeta potencialmente habitável não significa ter encontrado vida."
            )

        ]


        return aspectos


    # --------------------------------------------------------
    # RESPOSTA GENÉRICA
    # --------------------------------------------------------

    return [

        (
            "🌌 O que é",
            "A Astronomia estuda os objetos, fenômenos e estruturas existentes no Universo, como planetas, estrelas, galáxias, nebulosas e outros corpos celestes."
        ),

        (
            "🔭 Como os cientistas estudam",
            "Os astrônomos utilizam telescópios e outros instrumentos para observar a luz e diferentes tipos de radiação que chegam até nós. Essas observações ajudam a descobrir como os objetos do Universo funcionam."
        ),

        (
            "🧪 Como a ciência investiga",
            "Os pesquisadores comparam observações com modelos científicos. Quando novas evidências aparecem, os modelos podem ser testados, aperfeiçoados ou modificados."
        )

    ]


# ============================================================
# COMPLETAR EXPLICAÇÃO COM A PESQUISA
# ============================================================

def montar_explicacao_astronomia(
    pergunta,
    resultados
):

    aspectos = identificar_aspectos(
        pergunta
    )


    texto = ""


    texto += "## 🔭 Resposta à pergunta\n\n"


    texto += (
        "**"
        + html.escape(
            pergunta
        )
        + "**\n\n"
    )


    # --------------------------------------------------------
    # PARÁGRAFOS DOS ASPECTOS
    # --------------------------------------------------------

    for titulo, explicacao in aspectos:

        texto += (
            "### "
            + titulo
            + "\n\n"
        )


        texto += (
            explicacao
            + "\n\n"
        )


    # --------------------------------------------------------
    # O QUE A PESQUISA ENCONTROU
    # --------------------------------------------------------

    if resultados:

        texto += (
            "## 🌐 O que a pesquisa encontrou\n\n"
        )


        # Mostrar apenas resultados que realmente
        # possuem conteúdo útil.

        resultados_com_texto = [

            r

            for r in resultados

            if r.get(
                "texto",
                ""
            )

        ]


        for resultado in resultados_com_texto[:5]:

            nome_fonte = resultado.get(
                "fonte",
                "Fonte científica"
            )


            conteudo = limpar_texto(
                resultado.get(
                    "texto",
                    ""
                )
            )


            if not conteudo:

                continue


            # Não despejar textos enormes.

            if len(conteudo) > 600:

                conteudo = (
                    conteudo[:600]
                    + "..."
                )


            texto += (
                "### 📚 "
                + html.escape(
                    nome_fonte
                )
                + "\n\n"
            )


            texto += (
                conteudo
                + "\n\n"
            )


    # --------------------------------------------------------
    # CONCLUSÃO
    # --------------------------------------------------------

    texto += (
        "## 🌟 Em resumo\n\n"
    )


    texto += (
        "A Astronomia procura entender o Universo "
        "usando observações, experimentos, modelos "
        "científicos e muita investigação. "
        "Quando uma pergunta ainda não possui uma "
        "resposta definitiva, os cientistas continuam "
        "pesquisando para descobrir novas evidências."
        "\n\n"
    )


    return texto


# ============================================================
# INTERFACE DA IA
# ============================================================

def mostrar_ia_astronomia():

    st.markdown(
        """
        <div class="titulo-ia">
        🌌 IA DE ASTRONOMIA
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown(
        """
        ### 🔭 Pergunte qualquer coisa sobre Astronomia

        Você pode perguntar sobre:

        🪐 planetas  
        ⭐ estrelas  
        🌌 galáxias  
        🕳️ buracos negros  
        🌑 matéria escura  
        ☀️ Sol  
        🌙 Lua  
        🚀 exploração espacial  
        🌠 Big Bang  
        🔭 telescópios  
        👽 vida no Universo  
        🌀 cosmologia  
        """

    )


    pergunta = st.text_area(

        "Digite sua pergunta:",

        placeholder=
        "Exemplo: O que são buracos negros?",

        height=120,

        key="pergunta_astronomia"

    )


    if st.button(
        "🔎 Pesquisar no Universo",
        use_container_width=True
    ):


        if not pergunta.strip():

            st.warning(
                "Digite uma pergunta primeiro."
            )

            return


        with st.spinner(
            "🔭 Pesquisando informações de Astronomia..."
        ):


            resultados = (
                pesquisar_web_astronomia(
                    pergunta
                )
            )


            explicacao = (
                montar_explicacao_astronomia(
                    pergunta,
                    resultados
                )
            )


        # ----------------------------------------------------
        # MOSTRAR RESPOSTA
        # ----------------------------------------------------

        st.markdown(
            """
            <div class="card-resposta">
            """,
            unsafe_allow_html=True
        )


        st.markdown(
            explicacao
        )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        # ----------------------------------------------------
        # FONTES
        # ----------------------------------------------------

        st.markdown(
            "## 📚 Fontes consultadas"
        )


        fontes_mostradas = set()


        for fonte in resultados:

            nome = fonte.get(
                "fonte",
                "Fonte"
            )


            url = fonte.get(
                "url",
                ""
            )


            titulo = fonte.get(
                "titulo",
                "Pesquisa"
            )


            # -----------------------------------------------
            # CORREÇÃO DO KEYERROR
            # -----------------------------------------------

            if not url:

                continue


            if url in fontes_mostradas:

                continue


            fontes_mostradas.add(
                url
            )


            st.markdown(

                f"""
                <div class="card-fonte">

                <strong>
                📚 {html.escape(nome)}
                </strong>

                <br>

                {html.escape(titulo[:200])}

                <br><br>

                <a
                href="{url}"
                target="_blank"
                style="
                color:#4cc9f0;
                font-weight:bold;
                "
                >
                🔗 Abrir fonte
                </a>

                </div>
                """,

                unsafe_allow_html=True

            )


# ============================================================
# CHAMAR A IA
# ============================================================

mostrar_ia_astronomia()
