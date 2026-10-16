import streamlit as st
import random
import requests
import html
import re
from urllib.parse import quote_plus


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Cavaleiros do Zodíaco - Astronomia e Física",
    page_icon="🌟",
    layout="centered"
)


# ============================================================
# ESTILO
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #0b132b;
    color: #ffffff;
}

.stButton > button {
    width: 100%;
    background-color: #4361ee;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    border: 2px solid #4cc9f0;
    font-size: 16px;
    padding: 10px;
}

.stButton > button:hover {
    background-color: #4cc9f0;
    color: #0b132b;
}

.card-explicacao {
    background-color: #1c2541;
    padding: 22px;
    border-radius: 15px;
    border: 2px solid #4361ee;
    margin-bottom: 20px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.4);
}

.card-aspecto {
    background-color: #16213e;
    padding: 18px;
    border-radius: 12px;
    border-left: 5px solid #4cc9f0;
    margin-bottom: 15px;
}

.card-fonte {
    background-color: #202b4a;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 12px;
}

.titulo-crianca {
    color: #4cc9f0;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 10px;
}

h1, h2, h3 {
    color: #4cc9f0;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# 12 CASAS DO SANTUÁRIO
# ============================================================

CASAS_SANTUARIO = [
    "1ª Casa: Templo de Áries ♈",
    "2ª Casa: Templo de Touro ♉",
    "3ª Casa: Templo de Gêmeos ♊",
    "4ª Casa: Templo de Câncer ♋",
    "5ª Casa: Templo de Leão ♌",
    "6ª Casa: Templo de Virgem ♍",
    "7ª Casa: Templo de Libra ♎",
    "8ª Casa: Templo de Escorpião ♏",
    "9ª Casa: Templo de Sagitário ♐",
    "10ª Casa: Templo de Capricórnio ♑",
    "11ª Casa: Templo de Aquário ♒",
    "12ª Casa: Templo de Peixes ♓",
    "🏛️ Salão do Mestre / Templo de Athena 🏛️"
]


def obter_nome_casa(num_casa):
    indice = min(num_casa, len(CASAS_SANTUARIO) - 1)
    return CASAS_SANTUARIO[indice]


# ============================================================
# BANCO DE QUESTÕES
# ============================================================

guias = [
    "Seiya de Pégaso",
    "Shiryu de Dragão",
    "Hyoga de Cisne",
    "Shun de Andrômeda",
    "Ikki de Fênix",
    "Mu de Áries",
    "Shaka de Virgem",
    "Aioria de Leão",
    "Dohko de Libra",
    "Camus de Aquário"
]


dados_brutos = [

    (
        "Georges Lemaître estudou a expansão do universo.",
        "Georges Lemaître",
        "O que postula o modelo do Big Bang?",
        [
            "A expansão do universo a partir de um estado inicial muito quente e denso.",
            "O universo surgiu estático e eterno.",
            "As galáxias são todas paradas.",
            "O universo cria matéria continuamente.",
            "A origem do universo acontece a cada 100 anos."
        ],
        "A",
        "O modelo do Big Bang descreve um universo que esteve em um estado muito quente e denso e que passou a se expandir."
    ),

    (
        "Edwin Hubble estudou galáxias distantes.",
        "Edwin Hubble",
        "Qual é uma importante evidência da expansão do universo?",
        [
            "O desvio para o vermelho da luz de galáxias distantes.",
            "A colisão de planetas.",
            "O resfriamento do Sol.",
            "A ausência de estrelas.",
            "A rotação da Lua."
        ],
        "A",
        "O desvio para o vermelho mostra que muitas galáxias distantes estão se afastando de nós."
    ),

    (
        "Penzias e Wilson detectaram uma radiação que vinha de todas as direções.",
        "Arno Penzias e Robert Wilson",
        "O que é a Radiação Cósmica de Fundo?",
        [
            "Uma radiação remanescente do universo primordial.",
            "Luz produzida pelo Sol.",
            "Radiação produzida pela Lua.",
            "Ondas sonoras no espaço.",
            "Luz produzida pelos planetas."
        ],
        "A",
        "A Radiação Cósmica de Fundo é uma espécie de registro muito antigo do universo."
    ),

    (
        "A taxa de expansão do universo pode ser estudada pela constante de Hubble.",
        "Edwin Hubble",
        "O que representa a constante de Hubble?",
        [
            "Uma medida relacionada à taxa de expansão do universo.",
            "A velocidade da Terra.",
            "A massa do Sol.",
            "A distância entre a Terra e a Lua.",
            "A temperatura do espaço."
        ],
        "A",
        "A constante de Hubble está relacionada à velocidade com que o espaço se expande em diferentes distâncias."
    ),

    (
        "O princípio cosmológico descreve o universo em grandes escalas.",
        "Cosmologia",
        "O que significam os termos homogêneo e isotrópico?",
        [
            "Em grandes escalas, o universo apresenta propriedades semelhantes em diferentes regiões e direções.",
            "Todas as estrelas são iguais.",
            "Todos os planetas possuem o mesmo tamanho.",
            "A Terra está no centro do universo.",
            "O universo não possui galáxias."
        ],
        "A",
        "Em escalas muito grandes, o universo parece ser bastante semelhante quando observado em diferentes direções."
    ),

    (
        "A luz pode sofrer efeitos gravitacionais.",
        "Albert Einstein",
        "O que acontece com a luz quando passa perto de uma grande massa?",
        [
            "Sua trajetória pode ser desviada.",
            "Ela desaparece imediatamente.",
            "Ela vira som.",
            "Ela para completamente.",
            "Ela deixa de existir."
        ],
        "A",
        "Grandes concentrações de massa podem alterar a trajetória da luz."
    ),

    (
        "Ondas gravitacionais foram detectadas diretamente pelo LIGO.",
        "Colaboração LIGO",
        "O que são ondas gravitacionais?",
        [
            "Ondulações que se propagam pelo espaço-tempo.",
            "Ondas sonoras no espaço.",
            "Ondas produzidas pelos oceanos.",
            "Ondas de rádio comuns.",
            "Ondas produzidas apenas pelo Sol."
        ],
        "A",
        "Ondas gravitacionais são perturbações que se propagam pelo espaço-tempo."
    ),

    (
        "Vera Rubin estudou a rotação das galáxias.",
        "Vera Rubin",
        "Por que a matéria escura é importante nos modelos atuais?",
        [
            "Porque seus efeitos gravitacionais ajudam a explicar movimentos observados nas galáxias.",
            "Porque ela produz a maior parte da luz.",
            "Porque ela é formada por estrelas.",
            "Porque ela é visível diretamente.",
            "Porque ela produz o vento solar."
        ],
        "A",
        "A matéria escura não é observada diretamente pela luz, mas seus efeitos gravitacionais podem ser percebidos."
    ),

    (
        "Supernovas distantes ajudaram a descobrir que a expansão do universo está acelerando.",
        "Saul Perlmutter",
        "O que as observações de supernovas distantes ajudaram a mostrar?",
        [
            "Que a expansão do universo está acelerando.",
            "Que a Terra está aumentando de tamanho.",
            "Que o Sol está ficando maior.",
            "Que todas as galáxias estão paradas.",
            "Que a Lua produz energia."
        ],
        "A",
        "Observações de supernovas muito distantes ajudaram os cientistas a descobrir a expansão acelerada do universo."
    ),

    (
        "A inflação é uma hipótese sobre uma fase muito rápida do universo primordial.",
        "Alan Guth",
        "O que é a inflação cósmica?",
        [
            "Uma fase hipotética de expansão extremamente rápida do universo primordial.",
            "O crescimento das estrelas.",
            "O aumento do tamanho dos planetas.",
            "A expansão do Sol.",
            "O movimento da Lua."
        ],
        "A",
        "A inflação é uma hipótese segundo a qual o universo passou por uma expansão extremamente rápida em seus primeiros momentos."
    ),

    (
        "O universo possui estrelas, galáxias, planetas e muitas outras estruturas.",
        "Astronomia",
        "O que é uma galáxia?",
        [
            "Um grande sistema de estrelas, gás, poeira e outros componentes unidos pela gravidade.",
            "Uma única estrela.",
            "Um planeta gigante.",
            "Uma lua.",
            "Uma nuvem de chuva."
        ],
        "A",
        "Galáxias são enormes sistemas formados por estrelas, gás, poeira e outros componentes."
    ),

    (
        "Planetas podem existir ao redor de outras estrelas.",
        "Astronomia",
        "O que é um exoplaneta?",
        [
            "Um planeta que orbita uma estrela diferente do Sol.",
            "Uma estrela muito pequena.",
            "Uma galáxia pequena.",
            "Uma lua da Terra.",
            "Um cometa."
        ],
        "A",
        "Exoplanetas são planetas que orbitam outras estrelas que não o nosso Sol."
    ),

    (
        "As estrelas produzem energia em seus interiores.",
        "Astrofísica",
        "Por que as estrelas brilham?",
        [
            "Porque produzem energia em seus interiores, principalmente por processos de fusão nuclear.",
            "Porque refletem apenas a luz da Lua.",
            "Porque possuem fogo em sua superfície.",
            "Porque são feitas de eletricidade.",
            "Porque estão próximas da Terra."
        ],
        "A",
        "No interior das estrelas acontecem reações nucleares que liberam muita energia."
    ),

    (
        "A Lua é o satélite natural da Terra.",
        "Astronomia",
        "O que é a Lua?",
        [
            "O satélite natural da Terra.",
            "Uma estrela.",
            "Um planeta.",
            "Uma galáxia.",
            "Um cometa."
        ],
        "A",
        "A Lua gira ao redor da Terra e é o nosso satélite natural."
    ),

    (
        "O Sol é a estrela localizada no centro do Sistema Solar.",
        "Astronomia",
        "O que é o Sol?",
        [
            "Uma estrela.",
            "Um planeta.",
            "Uma galáxia.",
            "Um cometa.",
            "Um buraco negro."
        ],
        "A",
        "O Sol é uma estrela e fornece a maior parte da energia que chega à Terra."
    ),

    (
        "Buracos negros possuem regiões das quais a luz não consegue escapar.",
        "Astrofísica",
        "O que é um buraco negro?",
        [
            "Uma região do espaço com gravidade extremamente intensa.",
            "Um planeta sem luz.",
            "Uma estrela apagada comum.",
            "Uma galáxia pequena.",
            "Uma nuvem de poeira."
        ],
        "A",
        "Um buraco negro é uma região do espaço onde a gravidade é tão intensa que, depois de certo limite, nem a luz consegue escapar."
    ),

    (
        "A gravidade mantém planetas em órbita.",
        "Isaac Newton",
        "Qual é uma função importante da gravidade no Sistema Solar?",
        [
            "Manter os planetas em órbita ao redor do Sol.",
            "Produzir a luz do Sol.",
            "Criar estrelas.",
            "Parar o movimento dos planetas.",
            "Destruir todas as galáxias."
        ],
        "A",
        "A gravidade do Sol ajuda a manter os planetas em suas órbitas."
    ),

    (
        "Johannes Kepler estudou os movimentos dos planetas.",
        "Johannes Kepler",
        "O que as leis de Kepler descrevem?",
        [
            "O movimento dos planetas ao redor do Sol.",
            "A formação dos buracos negros.",
            "A temperatura das estrelas.",
            "A formação da Lua.",
            "A composição das galáxias."
        ],
        "A",
        "As leis de Kepler descrevem matematicamente como os planetas se movimentam ao redor do Sol."
    ),

    (
        "A Via Láctea é a galáxia onde está o Sistema Solar.",
        "Astronomia",
        "Em qual galáxia está o Sistema Solar?",
        [
            "Via Láctea.",
            "Andrômeda.",
            "Triângulo.",
            "Sombrero.",
            "Grande Nuvem de Magalhães."
        ],
        "A",
        "O Sistema Solar está localizado em uma região da galáxia chamada Via Láctea."
    )

]


# ============================================================
# CRIAÇÃO DO BANCO
# ============================================================

if "banco_50" not in st.session_state:

    lista_questoes = []

    for i, q in enumerate(dados_brutos):

        guia = guias[i % len(guias)]

        lista_questoes.append({
            "guia": guia,
            "texto_base": q[0],
            "cientista": q[1],
            "enunciado": q[2],
            "opcoes_originais": q[3],
            "correta_texto": q[3][ord(q[4]) - ord("A")],
            "por_que": q[5]
        })

    # Completa até 50 questões repetindo o banco com pequenas variações
    while len(lista_questoes) < 50:

        original = lista_questoes[len(lista_questoes) % len(dados_brutos)].copy()

        original["guia"] = guias[len(lista_questoes) % len(guias)]

        lista_questoes.append(original)

    st.session_state.banco_50 = lista_questoes[:50]


# ============================================================
# ESTADOS
# ============================================================

if "modo_sistema" not in st.session_state:
    st.session_state.modo_sistema = "⚔️ Jogo: Cavaleiros do Zodíaco"

if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False

if "indice_pergunta" not in st.session_state:
    st.session_state.indice_pergunta = 0

if "equipe_sub_idx" not in st.session_state:
    st.session_state.equipe_sub_idx = 0

if "casas_alfa" not in st.session_state:
    st.session_state.casas_alfa = 0

if "casas_beta" not in st.session_state:
    st.session_state.casas_beta = 0

if "casas_gama" not in st.session_state:
    st.session_state.casas_gama = 0

if "ultimo_feedback" not in st.session_state:
    st.session_state.ultimo_feedback = None

if "historico_professor" not in st.session_state:
    st.session_state.historico_professor = []

if "prof_logado" not in st.session_state:
    st.session_state.prof_logado = False

if "historico_explicacoes" not in st.session_state:
    st.session_state.historico_explicacoes = []


# ============================================================
# REINICIAR JOGO
# ============================================================

def reiniciar_jogo():

    st.session_state.jogo_iniciado = False
    st.session_state.indice_pergunta = 0
    st.session_state.equipe_sub_idx = 0

    st.session_state.casas_alfa = 0
    st.session_state.casas_beta = 0
    st.session_state.casas_gama = 0

    st.session_state.ultimo_feedback = None

    # Remove alternativas embaralhadas antigas
    chaves = [
        chave for chave in st.session_state.keys()
        if str(chave).startswith("opcoes_shuffled_")
    ]

    for chave in chaves:
        del st.session_state[chave]


# ============================================================
# PESQUISA DE ASTRONOMIA
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
        "dominio": "gov.br/on"
    },

    {
        "nome": "INPE",
        "dominio": "gov.br/inpe"
    },

    {
        "nome": "União Astronômica Internacional",
        "dominio": "iau.org"
    },

    {
        "nome": "NOIRLab",
        "dominio": "noirlab.edu"
    }
]


def limpar_texto(texto):

    if not texto:
        return ""

    texto = html.unescape(texto)

    texto = re.sub(r"<[^>]+>", " ", texto)

    texto = re.sub(r"\s+", " ", texto)

    return texto.strip()


def pesquisar_web_astronomia(pergunta):

    resultados = []

    pergunta = pergunta.strip()

    if not pergunta:
        return resultados

    # --------------------------------------------------------
    # PESQUISA DUCKDUCKGO
    # --------------------------------------------------------

    try:

        url_api = "https://api.duckduckgo.com/"

        parametros = {
            "q": pergunta,
            "format": "json",
            "no_html": "1",
            "skip_disambig": "0"
        }

        resposta = requests.get(
            url_api,
            params=parametros,
            timeout=15,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if resposta.status_code == 200:

            dados = resposta.json()

            titulo = limpar_texto(
                dados.get("Heading", "")
            )

            texto = limpar_texto(
                dados.get("AbstractText", "")
            )

            url = dados.get("AbstractURL", "")

            if texto:

                resultados.append({
                    "fonte": "DuckDuckGo / Wikipedia",
                    "titulo": titulo if titulo else pergunta,
                    "texto": texto,
                    "url": url if url else ""
                })

            # ------------------------------------------------
            # TÓPICOS RELACIONADOS
            # ------------------------------------------------

            topicos = dados.get("RelatedTopics", [])

            for topico in topicos:

                if not isinstance(topico, dict):
                    continue

                texto_topico = limpar_texto(
                    topico.get("Text", "")
                )

                url_topico = topico.get(
                    "FirstURL",
                    ""
                )

                if texto_topico:

                    resultados.append({
                        "fonte": "DuckDuckGo",
                        "titulo": pergunta,
                        "texto": texto_topico,
                        "url": url_topico if url_topico else ""
                    })

    except Exception:
        pass


    # --------------------------------------------------------
    # PESQUISAS DIRECIONADAS EM INSTITUIÇÕES CIENTÍFICAS
    # --------------------------------------------------------

    for fonte in FONTES_ASTRONOMIA:

        dominio = fonte.get("dominio", "")

        if not dominio:
            continue

        busca = quote_plus(
            f"{pergunta} site:{dominio}"
        )

        url_google = (
            "https://www.google.com/search?q="
            + busca
        )

        resultados.append({

            "fonte": fonte.get(
                "nome",
                "Fonte científica"
            ),

            "titulo": (
                f"Pesquisar '{pergunta}' em "
                f"{fonte.get('nome', 'fonte científica')}"
            ),

            "texto": (
                f"Pesquisa direcionada sobre "
                f"'{pergunta}' no site institucional "
                f"{dominio}."
            ),

            "url": url_google
        })


    # --------------------------------------------------------
    # REMOVE DUPLICADOS
    # --------------------------------------------------------

    resultados_finais = []

    urls_vistas = set()

    for resultado in resultados:

        if not isinstance(resultado, dict):
            continue

        url = resultado.get("url", "")

        texto = resultado.get("texto", "")

        if not texto:
            continue

        chave = url if url else texto[:150]

        if chave in urls_vistas:
            continue

        urls_vistas.add(chave)

        resultados_finais.append(resultado)


    return resultados_finais[:15]


# ============================================================
# IDENTIFICAR ASPECTOS DA PERGUNTA
# ============================================================

def identificar_aspectos(pergunta):

    p = pergunta.lower()

    aspectos = []


    if any(
        termo in p
        for termo in [
            "buraco negro",
            "buracos negros"
        ]
    ):

        aspectos.extend([
            (
                "🕳️ O que é um buraco negro?",
                "Um buraco negro é uma região do espaço onde a gravidade é extremamente intensa. Existe uma região chamada horizonte de eventos: depois de atravessá-la, não conseguimos receber luz ou informações daquele lugar."
            ),

            (
                "🌟 Como ele pode surgir?",
                "Alguns buracos negros podem se formar quando estrelas muito massivas chegam ao fim de suas vidas e sofrem um colapso gravitacional. Também existem buracos negros supermassivos no centro de muitas galáxias."
            ),

            (
                "💡 Por que não conseguimos vê-lo diretamente?",
                "Um buraco negro não brilha como uma estrela. Porém, podemos perceber seus efeitos observando estrelas próximas, gás muito quente ao redor dele e outros fenômenos produzidos pela sua gravidade."
            )
        ])


    elif any(
        termo in p
        for termo in [
            "estrela",
            "estrelas",
            "sol"
        ]
    ):

        aspectos.extend([
            (
                "⭐ O que é uma estrela?",
                "Uma estrela é uma enorme esfera de gás muito quente. Em seu interior acontecem processos nucleares que liberam energia. O Sol é a estrela mais próxima da Terra."
            ),

            (
                "🔥 Por que as estrelas brilham?",
                "As estrelas brilham porque produzem energia em seus interiores. Essa energia consegue chegar à superfície e ser emitida para o espaço na forma de luz e outras formas de radiação."
            ),

            (
                "🌌 Como elas nascem?",
                "Muitas estrelas nascem dentro de grandes nuvens de gás e poeira. A gravidade faz parte desse material se juntar, aumentando a temperatura e a pressão até que uma nova estrela possa se formar."
            )
        ])


    elif any(
        termo in p
        for termo in [
            "planeta",
            "planetas",
            "exoplaneta",
            "exoplanetas"
        ]
    ):

        aspectos.extend([
            (
                "🪐 O que é um planeta?",
                "Um planeta é um corpo celeste que orbita uma estrela e possui características próprias de tamanho, composição e movimento. No nosso Sistema Solar existem oito planetas."
            ),

            (
                "🔭 O que é um exoplaneta?",
                "Exoplaneta é o nome dado a um planeta que está fora do Sistema Solar. Esses mundos orbitam outras estrelas e podem ser muito diferentes dos planetas que conhecemos."
            ),

            (
                "🌍 Como descobrimos esses mundos?",
                "Muitos exoplanetas são descobertos observando pequenas mudanças na luz de suas estrelas. Por exemplo, quando um planeta passa na frente da estrela, a luz pode diminuir um pouquinho."
            )
        ])


    elif any(
        termo in p
        for termo in [
            "lua",
            "satélite"
        ]
    ):

        aspectos.extend([
            (
                "🌙 O que é a Lua?",
                "A Lua é o satélite natural da Terra. Ela não produz sua própria luz visível; nós conseguimos vê-la porque sua superfície reflete a luz do Sol."
            ),

            (
                "🔄 Por que a Lua muda de aparência?",
                "A Lua está sempre recebendo luz do Sol, mas conforme ela se movimenta ao redor da Terra, vemos partes diferentes de sua região iluminada. É isso que produz as fases da Lua."
            )
        ])


    elif any(
        termo in p
        for termo in [
            "galáxia",
            "galáxias",
            "via láctea"
        ]
    ):

        aspectos.extend([
            (
                "🌌 O que é uma galáxia?",
                "Uma galáxia é uma enorme estrutura formada por estrelas, gás, poeira e outros componentes. Tudo isso permanece reunido principalmente por causa da gravidade."
            ),

            (
                "🌍 Onde estamos?",
                "O Sistema Solar está dentro da Via Láctea. A Via Láctea é uma galáxia que possui uma quantidade gigantesca de estrelas."
            )
        ])


    elif any(
        termo in p
        for termo in [
            "big bang",
            "origem do universo",
            "universo começou",
            "universo surgiu"
        ]
    ):

        aspectos.extend([
            (
                "💥 O que é o Big Bang?",
                "O Big Bang é o modelo científico usado para descrever a evolução inicial do universo a partir de um estado extremamente quente e denso. O universo passou a se expandir e continua evoluindo."
            ),

            (
                "🌌 O universo está se expandindo?",
                "Sim. Observamos que muitas galáxias distantes apresentam um desvio para o vermelho em sua luz, o que está relacionado à expansão do universo."
            ),

            (
                "📡 Como sabemos disso?",
                "Uma das evidências importantes é a Radiação Cósmica de Fundo, uma radiação muito antiga que podemos observar atualmente. Ela funciona como uma espécie de registro do universo primordial."
            )
        ])


    elif any(
        termo in p
        for termo in [
            "matéria escura",
            "materia escura"
        ]
    ):

        aspectos.extend([
            (
                "🌑 O que é matéria escura?",
                "Matéria escura é o nome dado a um componente que não observamos diretamente pela luz, mas que apresenta efeitos gravitacionais importantes em galáxias e outras estruturas do universo."
            ),

            (
                "🔭 Como sabemos que ela pode existir?",
                "Os cientistas observam movimentos de estrelas e galáxias que não parecem ser explicados apenas pela matéria que conseguimos observar diretamente. A matéria escura é uma das explicações estudadas."
            )
        ])


    elif any(
        termo in p
        for termo in [
            "cometa",
            "cometas"
        ]
    ):

        aspectos.extend([
            (
                "☄️ O que é um cometa?",
                "Cometas são corpos formados principalmente por gelo, poeira e materiais rochosos. Quando chegam perto do Sol, parte do material pode formar uma região brilhante e uma cauda."
            ),

            (
                "☀️ Por que aparece uma cauda?",
                "Quando um cometa se aproxima do Sol, o aquecimento faz parte de seus materiais passar para o estado gasoso. A radiação e o vento solar ajudam a formar as estruturas que vemos como cauda."
            )
        ])


    elif any(
        termo in p
        for termo in [
            "gravidade",
            "gravitação"
        ]
    ):

        aspectos.extend([
            (
                "🌍 O que é gravidade?",
                "Gravidade é uma interação associada à massa e à energia. Ela é responsável por muitos movimentos que observamos no universo, como a órbita da Lua ao redor da Terra e dos planetas ao redor do Sol."
            ),

            (
                "🪐 Por que os planetas não saem voando?",
                "A gravidade do Sol atua sobre os planetas. Como eles também possuem movimento, eles seguem trajetórias ao redor do Sol em vez de simplesmente cair diretamente sobre ele."
            )
        ])


    if not aspectos:

        aspectos.extend([
            (
                "🔭 Sobre o tema da sua pergunta",
                f"A sua pergunta é sobre '{pergunta}'. A Astronomia estuda objetos e fenômenos que acontecem no universo, como estrelas, planetas, galáxias, buracos negros e muitos outros fenômenos."
            ),

            (
                "🌌 Como os cientistas estudam isso?",
                "Os astrônomos usam telescópios, satélites, observatórios e instrumentos científicos para coletar informações. A luz é especialmente importante porque carrega informações sobre objetos muito distantes."
            ),

            (
                "🧠 Por que isso é importante?",
                "Estudar o universo ajuda os cientistas a entender melhor como os astros nascem, evoluem e interagem. Muitas descobertas também ajudam a desenvolver novas tecnologias e conhecimentos."
            )
        ])


    return aspectos


# ============================================================
# MONTAR EXPLICAÇÃO
# ============================================================

def montar_explicacao_astronomia(
    pergunta,
    resultados
):

    aspectos = identificar_aspectos(
        pergunta
    )

    resposta = ""

    resposta += "## 🔭 Vamos descobrir!\n\n"

    resposta += (
        f"Você perguntou: **{pergunta}**\n\n"
    )

    resposta += (
        "Aqui está uma explicação simples, "
        "como uma pequena viagem pelo universo. 🚀\n\n"
    )


    for titulo, texto in aspectos:

        resposta += f"### {titulo}\n\n"

        resposta += f"{texto}\n\n"


    if resultados:

        resposta += "## 🌐 O que a pesquisa encontrou\n\n"

        resposta += (
            "Também fiz uma pesquisa para encontrar "
            "informações relacionadas ao tema. "
            "Algumas fontes são instituições científicas "
            "e outras servem como pontos de pesquisa.\n\n"
        )


        contador = 0

        for fonte in resultados:

            if contador >= 5:
                break

            if not isinstance(fonte, dict):
                continue

            texto = fonte.get(
                "texto",
                ""
            )

            titulo = fonte.get(
                "titulo",
                "Fonte"
            )

            nome = fonte.get(
                "fonte",
                "Fonte científica"
            )

            url = fonte.get(
                "url",
                ""
            )

            if not texto:
                continue

            texto = limpar_texto(
                texto
            )

            if len(texto) > 500:
                texto = texto[:500] + "..."

            resposta += (
                f"**{nome} — {titulo}**\n\n"
            )

            resposta += (
                f"{texto}\n\n"
            )

            if url:

                resposta += (
                    f"[🔗 Abrir fonte]({url})\n\n"
                )

            contador += 1


    resposta += "## 🌟 Resumindo\n\n"

    resposta += (
        "A Astronomia funciona como uma grande investigação. "
        "Os cientistas observam a luz, os movimentos e outras "
        "características dos objetos do espaço para descobrir "
        "como o universo funciona. 🌌🔭"
    )


    return resposta


# ============================================================
# MODO ASTRONOMIA
# ============================================================

def mostrar_ia_astronomia():

    st.title(
        "🌟 IA de Astronomia para Crianças"
    )

    st.markdown(
        """
        ### 🚀 Faça qualquer pergunta sobre o universo!

        Você pode perguntar, por exemplo:

        - Por que os buracos negros existem?
        - Como nasce uma estrela?
        - O que aconteceu no Big Bang?
        - Como descobrimos exoplanetas?
        - O que é matéria escura?
        - Por que a Lua muda de aparência?
        - Como funciona a gravidade?
        - O que são galáxias?
        """
    )

    st.markdown("---")


    pergunta = st.text_area(
        "🔭 Digite sua pergunta sobre Astronomia:",
        placeholder=(
            "Exemplo: "
            "Por que os planetas ficam girando ao redor do Sol?"
        ),
        height=120
    )


    col1, col2 = st.columns(2)


    with col1:

        botao_pesquisar = st.button(
            "🚀 Pesquisar e Explicar",
            use_container_width=True
        )


    with col2:

        botao_limpar = st.button(
            "🧹 Limpar Histórico",
            use_container_width=True
        )


    if botao_limpar:

        st.session_state.historico_explicacoes = []

        st.success(
            "Histórico apagado."
        )

        st.rerun()


    if botao_pesquisar:

        if not pergunta.strip():

            st.warning(
                "Digite uma pergunta primeiro."
            )

        else:

            with st.spinner(
                "🔭 Pesquisando informações sobre o universo..."
            ):

                resultados = pesquisar_web_astronomia(
                    pergunta
                )

                explicacao = montar_explicacao_astronomia(
                    pergunta,
                    resultados
                )


            registro = {

                "pergunta": pergunta,

                "explicacao": explicacao,

                "fontes": resultados
            }


            st.session_state.historico_explicacoes.insert(
                0,
                registro
            )


    st.markdown("---")


    if st.session_state.historico_explicacoes:

        for item in st.session_state.historico_explicacoes:

            st.markdown(
                '<div class="card-explicacao">',
                unsafe_allow_html=True
            )


            st.markdown(
                item.get(
                    "explicacao",
                    "Não foi possível gerar a explicação."
                )
            )


            st.markdown(
                "</div>",
                unsafe_allow_html=True
            )


            fontes = item.get(
                "fontes",
                []
            )


            if fontes:

                with st.expander(
                    "🌐 Ver fontes pesquisadas"
                ):

                    fontes_mostradas = 0


                    for fonte in fontes:

                        if fontes_mostradas >= 10:
                            break

                        if not isinstance(
                            fonte,
                            dict
                        ):
                            continue


                        nome = fonte.get(
                            "fonte",
                            "Fonte científica"
                        )


                        titulo = fonte.get(
                            "titulo",
                            "Pesquisa"
                        )


                        url = fonte.get(
                            "url",
                            ""
                        )


                        texto = fonte.get(
                            "texto",
                            ""
                        )


                        texto = limpar_texto(
                            texto
                        )


                        st.markdown(
                            '<div class="card-fonte">',
                            unsafe_allow_html=True
                        )


                        st.markdown(
                            f"**🔬 {nome}**"
                        )


                        st.markdown(
                            f"**{titulo}**"
                        )


                        if texto:

                            if len(texto) > 400:
                                texto = (
                                    texto[:400]
                                    + "..."
                                )

                            st.write(
                                texto
                            )


                        # IMPORTANTE:
                        # Nunca acessar fonte["url"] diretamente.
                        # Usamos .get() para evitar KeyError.

                        if url:

                            st.markdown(
                                f"[🔗 Abrir fonte da pesquisa]({url})"
                            )


                        st.markdown(
                            "</div>",
                            unsafe_allow_html=True
                        )


                        fontes_mostradas += 1


    else:

        st.info(
            "🌟 Faça uma pergunta e vamos explorar o universo juntos!"
        )


# ============================================================
# BARRA LATERAL
# ============================================================

st.sidebar.header(
    "🧭 Painel de Controle"
)


st.session_state.modo_sistema = st.sidebar.radio(
    "Escolha o Ambiente:",
    [
        "⚔️ Jogo: Cavaleiros do Zodíaco",
        "🌟 IA de Astronomia para Crianças"
    ]
)


# ============================================================
# ÁREA DO PROFESSOR
# ============================================================

st.sidebar.markdown("---")

st.sidebar.header(
    "👨‍🏫 Área do Professor / Admin"
)


with st.sidebar.expander(
    "🔑 Acesso Restrito"
):

    if not st.session_state.prof_logado:

        login_input = st.text_input(
            "Login"
        )

        senha_input = st.text_input(
            "Senha",
            type="password"
        )


        if st.button(
            "Entrar"
        ):

            if (
                login_input == "Felipe Ferreira"
                and
                senha_input == "Ff241198"
            ):

                st.session_state.prof_logado = True

                st.success(
                    "Login realizado com sucesso!"
                )

                st.rerun()

            else:

                st.error(
                    "Credenciais inválidas."
                )


    else:

        st.success(
            "Sessão ativa."
        )


        if st.button(
            "Sair"
        ):

            st.session_state.prof_logado = False

            st.rerun()


# ============================================================
# RELATÓRIO DO PROFESSOR
# ============================================================

if st.session_state.prof_logado:

    st.sidebar.markdown(
        "### 📄 Relatório do Professor"
    )


    relatorio_txt = ""

    relatorio_txt += (
        "====================================================\n"
    )

    relatorio_txt += (
        "RELATÓRIO DE DESEMPENHO\n"
    )

    relatorio_txt += (
        "====================================================\n\n"
    )


    if st.session_state.historico_professor:

        for idx, item in enumerate(
            st.session_state.historico_professor,
            1
        ):

            relatorio_txt += (
                f"Registro #{idx}\n"
            )

            relatorio_txt += (
                f"Equipe: {item.get('equipe', '')}\n"
            )

            relatorio_txt += (
                f"Casa: {item.get('casa_santuario', '')}\n"
            )

            relatorio_txt += (
                f"Guia: {item.get('guia', '')}\n"
            )

            relatorio_txt += (
                f"Cientista: {item.get('cientista', '')}\n"
            )

            relatorio_txt += (
                f"Pergunta: {item.get('enunciado', '')}\n"
            )

            relatorio_txt += (
                f"Resposta: {item.get('resposta', '')}\n"
            )

            relatorio_txt += (
                f"Status: {item.get('status', '')}\n"
            )

            relatorio_txt += (
                f"Justificativa: {item.get('por_que', '')}\n"
            )

            relatorio_txt += (
                "----------------------------------------------------\n"
            )


    else:

        relatorio_txt += (
            "Nenhum registro de respostas ainda.\n"
        )


    st.sidebar.download_button(
        "📥 Baixar Relatório",
        data=relatorio_txt,
        file_name="relatorio_desempenho.txt",
        mime="text/plain"
    )


    if st.sidebar.button(
        "🗑️ Limpar Relatório"
    ):

        st.session_state.historico_professor = []

        st.sidebar.success(
            "Relatório limpo."
        )

        st.rerun()


# ============================================================
# MODO 1 — JOGO
# ============================================================

if (
    st.session_state.modo_sistema
    == "⚔️ Jogo: Cavaleiros do Zodíaco"
):

    st.title(
        "🏛️ Cavaleiros do Zodíaco: O Despertar da Física"
    )

    st.markdown(
        "### *Treinamento das Equipes: Domine o Cosmo!*"
    )

    st.markdown("---")


    # --------------------------------------------------------
    # PLACAR
    # --------------------------------------------------------

    st.sidebar.markdown("---")

    st.sidebar.header(
        "📊 Posição no Santuário"
    )


    equipes = [

        (
            "Equipe Alfa",
            st.session_state.casas_alfa
        ),

        (
            "Equipe Beta",
            st.session_state.casas_beta
        ),

        (
            "Equipe Gama",
            st.session_state.casas_gama
        )

    ]


    for nome_eq, casas_eq in equipes:

        st.sidebar.markdown(
            f"🛡️ **{nome_eq}**"
        )

        st.sidebar.write(
            obter_nome_casa(
                casas_eq
            )
        )

        st.sidebar.progress(
            min(
                1.0,
                casas_eq / 12
            )
        )


    if st.sidebar.button(
        "🔄 Reiniciar Partida"
    ):

        reiniciar_jogo()

        st.rerun()


    # --------------------------------------------------------
    # INÍCIO
    # --------------------------------------------------------

    if not st.session_state.jogo_iniciado:

        st.subheader(
            "🔥 Cerimônia de Abertura"
        )


        st.markdown(
            """
            > Os aspirantes chegaram ao Santuário.
            >
            > Para alcançar o Templo de Athena, as equipes
            > precisam responder questões de Física,
            > Astronomia e Cosmologia.
            >
            > **Regras:**
            >
            > 🟢 Acertou: avança uma casa.
            >
            > 🔴 Errou: não perde casas e a vez passa.
            >
            > 🏆 Vence a primeira equipe a alcançar as 12 Casas.
            """
        )


        if st.button(
            "🌟 Iniciar Treinamento"
        ):

            st.session_state.jogo_iniciado = True

            st.rerun()


        st.stop()


    # --------------------------------------------------------
    # VERIFICAR VENCEDOR
    # --------------------------------------------------------

    vencedor = None


    if st.session_state.casas_alfa >= 12:

        vencedor = "Equipe Alfa"


    elif st.session_state.casas_beta >= 12:

        vencedor = "Equipe Beta"


    elif st.session_state.casas_gama >= 12:

        vencedor = "Equipe Gama"


    if (
        vencedor
        or
        st.session_state.indice_pergunta
        >= len(st.session_state.banco_50)
    ):

        st.balloons()


        st.subheader(
            "🏛️ Chegada ao Templo de Athena!"
        )


        if vencedor:

            st.success(
                f"🥇 A **{vencedor}** venceu o treinamento!"
            )

        else:

            st.success(
                "Todas as questões foram respondidas!"
            )


        if st.button(
            "🔄 Novo Treinamento"
        ):

            reiniciar_jogo()

            st.rerun()


        st.stop()


    # --------------------------------------------------------
    # QUESTÃO ATUAL
    # --------------------------------------------------------

    lista_equipes = [
        "Equipe Alfa",
        "Equipe Beta",
        "Equipe Gama"
    ]


    idx_p = (
        st.session_state.indice_pergunta
    )


    e_idx = (
        st.session_state.equipe_sub_idx
    )


    equipe_da_vez = (
        lista_equipes[e_idx]
    )


    if equipe_da_vez == "Equipe Alfa":

        casa_str = obter_nome_casa(
            st.session_state.casas_alfa
        )


    elif equipe_da_vez == "Equipe Beta":

        casa_str = obter_nome_casa(
            st.session_state.casas_beta
        )


    else:

        casa_str = obter_nome_casa(
            st.session_state.casas_gama
        )


    q_atual = (
        st.session_state.banco_50[idx_p]
    )


    # --------------------------------------------------------
    # EMBARALHAR ALTERNATIVAS
    # --------------------------------------------------------

    chave_opcoes = (
        f"opcoes_shuffled_{idx_p}"
    )


    if chave_opcoes not in st.session_state:

        opcoes_copia = list(
            q_atual["opcoes_originais"]
        )

        random.shuffle(
            opcoes_copia
        )


        rotulos = [
            "A",
            "B",
            "C",
            "D",
            "E"
        ]


        opcoes_rotuladas = [

            f"{rotulos[i]}) {texto}"

            for i, texto
            in enumerate(opcoes_copia)

        ]


        st.session_state[
            chave_opcoes
        ] = opcoes_rotuladas


    # --------------------------------------------------------
    # EXIBIÇÃO
    # --------------------------------------------------------

    st.warning(
        f"📍 **{equipe_da_vez}** está em: **{casa_str}**"
    )


    st.subheader(
        f"⚔️ Vez da {equipe_da_vez}"
    )


    st.markdown(
        f"**Guia:** *{q_atual['guia']}* ✨"
    )


    st.markdown("---")


    st.info(
        f"📜 **História da Ciência:**\n\n"
        f"{q_atual['texto_base']}\n\n"
        f"🔬 **Referência:** "
        f"*{q_atual['cientista']}*"
    )


    st.markdown(
        f"### 🧩 Pergunta\n\n"
        f"{q_atual['enunciado']}"
    )


    escolha_usuario = st.radio(
        "Selecione a alternativa:",
        st.session_state[
            chave_opcoes
        ],
        key=f"radio_{idx_p}_{e_idx}"
    )


    if st.button(
        "⚡ Enviar Resposta"
    ):

        texto_selecionado = (
            escolha_usuario
            .split(") ", 1)[1]
            .strip()
        )


        acertou = (
            texto_selecionado
            == q_atual["correta_texto"]
        )


        status = (
            "CORRETA"
            if acertou
            else
            "INCORRETA"
        )


        if acertou:

            if equipe_da_vez == "Equipe Alfa":

                st.session_state.casas_alfa += 1


            elif equipe_da_vez == "Equipe Beta":

                st.session_state.casas_beta += 1


            else:

                st.session_state.casas_gama += 1


        # --------------------------------------------
        # REGISTRO DO PROFESSOR
        # --------------------------------------------

        st.session_state.historico_professor.append({

            "equipe": equipe_da_vez,

            "casa_santuario": casa_str,

            "guia": q_atual["guia"],

            "cientista": q_atual["cientista"],

            "enunciado": q_atual["enunciado"],

            "resposta": escolha_usuario,

            "status": status,

            "por_que": q_atual["por_que"]

        })


        st.session_state.ultimo_feedback = {

            "status": status,

            "equipe": equipe_da_vez,

            "correta_texto":
                q_atual["correta_texto"],

            "por_que":
                q_atual["por_que"]

        }


        st.session_state.indice_pergunta += 1


        st.session_state.equipe_sub_idx = (
            e_idx + 1
        ) % 3


        st.rerun()


    # --------------------------------------------------------
    # FEEDBACK
    # --------------------------------------------------------

    if st.session_state.ultimo_feedback:

        st.markdown("---")


        feedback = (
            st.session_state.ultimo_feedback
        )


        if feedback["status"] == "CORRETA":

            st.success(
                f"🎉 Excelente! "
                f"A **{feedback['equipe']}** acertou!"
            )


        else:

            st.error(
                f"❌ A resposta da "
                f"**{feedback['equipe']}** estava incorreta."
            )


            st.info(
                f"A resposta correta era:\n\n"
                f"**{feedback['correta_texto']}**"
            )


        st.info(
            f"💡 **Por que?**\n\n"
            f"{feedback['por_que']}"
        )


# ============================================================
# MODO 2 — ASTRONOMIA
# ============================================================

elif (
    st.session_state.modo_sistema
    == "🌟 IA de Astronomia para Crianças"
):

    mostrar_ia_astronomia()
