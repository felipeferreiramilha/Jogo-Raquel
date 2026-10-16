import streamlit as st
import requests
import html
import re
import random
from urllib.parse import quote_plus


# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="🌌 Explorador do Universo",
    page_icon="🌌",
    layout="wide"
)


# ============================================================
# ESTILO
# ============================================================

st.markdown("""
<style>

body {
    background-color: #080d1c;
}

.main {
    background-color: #080d1c;
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
}

h1, h2, h3 {
    color: #5ee7ff;
}

.stButton > button {
    width: 100%;
    border-radius: 12px;
    min-height: 45px;
    font-weight: bold;
}

.caixa {
    background: linear-gradient(
        135deg,
        #101b35,
        #17264a
    );
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #31558c;
    margin-bottom: 20px;
}

.aspecto {
    background-color: #101a31;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #5ee7ff;
    margin-bottom: 18px;
}

.curiosidade {
    background-color: #201b42;
    padding: 20px;
    border-radius: 15px;
    border-left: 5px solid #f7c948;
    margin-bottom: 18px;
}

.fonte {
    background-color: #111827;
    padding: 15px;
    border-radius: 12px;
    margin-bottom: 12px;
}

.pergunta {
    background-color: #172554;
    padding: 18px;
    border-radius: 15px;
    border: 1px solid #2563eb;
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# ESTADOS
# ============================================================

if "modo" not in st.session_state:
    st.session_state.modo = "🌌 Explorador de Astronomia"

if "historico_astronomia" not in st.session_state:
    st.session_state.historico_astronomia = []

if "prof_logado" not in st.session_state:
    st.session_state.prof_logado = False

if "historico_professor" not in st.session_state:
    st.session_state.historico_professor = []

if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False

if "pergunta_jogo" not in st.session_state:
    st.session_state.pergunta_jogo = 0

if "alfa" not in st.session_state:
    st.session_state.alfa = 0

if "beta" not in st.session_state:
    st.session_state.beta = 0

if "gama" not in st.session_state:
    st.session_state.gama = 0


# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def limpar_texto(texto):

    if not texto:
        return ""

    texto = html.unescape(str(texto))

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


def normalizar(texto):

    texto = texto.lower()

    substituicoes = {
        "á": "a",
        "à": "a",
        "ã": "a",
        "â": "a",
        "é": "e",
        "ê": "e",
        "í": "i",
        "ó": "o",
        "ô": "o",
        "õ": "o",
        "ú": "u",
        "ç": "c"
    }

    for antigo, novo in substituicoes.items():
        texto = texto.replace(
            antigo,
            novo
        )

    return texto


# ============================================================
# BANCO DE CONHECIMENTO
# ============================================================

CONHECIMENTO = {

    # --------------------------------------------------------
    # MERCÚRIO
    # --------------------------------------------------------

    "mercurio": {
        "titulo": "☿ Mercúrio",
        "texto": (
            "Mercúrio é o planeta mais próximo do Sol e também "
            "o menor dos oito planetas do Sistema Solar. "
            "Ele é um planeta rochoso e possui uma superfície "
            "cheia de crateras."
        ),
        "curiosidades": [
            "Mercúrio não é o planeta mais quente do Sistema Solar; esse título pertence a Vênus.",
            "Um ano em Mercúrio dura apenas 88 dias terrestres.",
            "Mercúrio não possui uma atmosfera espessa como a da Terra."
        ]
    },

    # --------------------------------------------------------
    # VÊNUS
    # --------------------------------------------------------

    "venus": {
        "titulo": "♀️ Vênus",
        "texto": (
            "Vênus é o segundo planeta a partir do Sol. "
            "Ele possui uma atmosfera muito espessa, rica em "
            "dióxido de carbono, que produz um forte efeito estufa. "
            "Por isso, Vênus é o planeta mais quente do Sistema Solar."
        ),
        "curiosidades": [
            "Vênus é mais quente que Mercúrio mesmo estando mais longe do Sol.",
            "Vênus gira em sentido contrário ao da maioria dos planetas.",
            "Um dia em Vênus é muito longo."
        ]
    },

    # --------------------------------------------------------
    # TERRA
    # --------------------------------------------------------

    "terra": {
        "titulo": "🌍 Terra",
        "texto": (
            "A Terra é o terceiro planeta a partir do Sol e o único "
            "mundo onde sabemos que existe vida. Ela possui água "
            "líquida em sua superfície, uma atmosfera e condições "
            "que permitem a existência de muitos tipos de organismos."
        ),
        "curiosidades": [
            "A Terra possui um único satélite natural: a Lua.",
            "A maior parte da superfície terrestre é coberta por água.",
            "A Terra não é uma esfera perfeita: ela é ligeiramente achatada nos polos."
        ]
    },

    # --------------------------------------------------------
    # MARTE
    # --------------------------------------------------------

    "marte": {
        "titulo": "♂️ Marte",
        "texto": (
            "Marte é o quarto planeta a partir do Sol e é conhecido "
            "como o planeta vermelho por causa dos minerais ricos "
            "em ferro presentes em sua superfície. Marte possui "
            "montanhas, vales, crateras e sinais de que água líquida "
            "existiu em sua superfície no passado."
        ),
        "curiosidades": [
            "Marte possui o Olympus Mons, uma das maiores montanhas conhecidas do Sistema Solar.",
            "Marte possui duas pequenas luas: Fobos e Deimos.",
            "Robôs já exploraram a superfície de Marte."
        ]
    },

    # --------------------------------------------------------
    # JÚPITER
    # --------------------------------------------------------

    "jupiter": {
        "titulo": "♃ Júpiter",
        "texto": (
            "Júpiter é o maior planeta do Sistema Solar. "
            "Ele é um gigante gasoso composto principalmente "
            "por hidrogênio e hélio. Sua atmosfera possui enormes "
            "tempestades, incluindo a famosa Grande Mancha Vermelha."
        ),
        "curiosidades": [
            "Júpiter é tão grande que caberiam muitos planetas Terra dentro dele.",
            "Júpiter possui muitas luas.",
            "A Grande Mancha Vermelha é uma enorme tempestade observada há séculos."
        ]
    },

    # --------------------------------------------------------
    # SATURNO
    # --------------------------------------------------------

    "saturno": {
        "titulo": "♄ Saturno",
        "texto": (
            "Saturno é um gigante gasoso conhecido principalmente "
            "por seus impressionantes anéis. Esses anéis são formados "
            "principalmente por partículas de gelo e fragmentos rochosos."
        ),
        "curiosidades": [
            "Os anéis de Saturno são formados por bilhões de pequenos pedaços de material.",
            "Saturno possui muitas luas.",
            "Saturno tem densidade média menor que a da água."
        ]
    },

    # --------------------------------------------------------
    # URANO
    # --------------------------------------------------------

    "urano": {
        "titulo": "♅ Urano",
        "texto": (
            "Urano é um gigante de gelo localizado nas regiões "
            "externas do Sistema Solar. Sua atmosfera contém "
            "hidrogênio, hélio e metano. O metano ajuda a produzir "
            "sua aparência azul-esverdeada."
        ),
        "curiosidades": [
            "Urano possui uma inclinação extrema de seu eixo.",
            "Ele possui anéis.",
            "Urano é classificado como gigante de gelo."
        ]
    },

    # --------------------------------------------------------
    # NETUNO
    # --------------------------------------------------------

    "netuno": {
        "titulo": "♆ Netuno",
        "texto": (
            "Netuno é o planeta mais distante do Sol entre os oito "
            "planetas. Ele é um gigante de gelo e possui uma atmosfera "
            "com ventos extremamente rápidos."
        ),
        "curiosidades": [
            "Netuno foi descoberto por meio de cálculos matemáticos antes de ser observado diretamente.",
            "Netuno possui uma cor azulada.",
            "Tritão é sua maior lua."
        ]
    },

    # --------------------------------------------------------
    # PLUTÃO
    # --------------------------------------------------------

    "plutao": {
        "titulo": "🧊 Plutão",
        "texto": (
            "Plutão é classificado atualmente como planeta anão. "
            "Ele está localizado no Cinturão de Kuiper, uma região "
            "distante do Sistema Solar que contém muitos corpos gelados."
        ),
        "curiosidades": [
            "Plutão possui uma região em forma de coração muito famosa.",
            "Plutão possui cinco luas conhecidas.",
            "A sonda New Horizons passou por Plutão em 2015."
        ]
    },

    # --------------------------------------------------------
    # LUA
    # --------------------------------------------------------

    "lua": {
        "titulo": "🌙 A Lua",
        "texto": (
            "A Lua é o satélite natural da Terra. Ela não produz "
            "sua própria luz visível; o brilho que observamos vem "
            "da luz do Sol refletida em sua superfície."
        ),
        "curiosidades": [
            "A Lua possui fases.",
            "A Lua influencia as marés da Terra.",
            "Seres humanos já caminharam na superfície lunar."
        ]
    },

    # --------------------------------------------------------
    # SOL
    # --------------------------------------------------------

    "sol": {
        "titulo": "☀️ O Sol",
        "texto": (
            "O Sol é uma estrela localizada no centro do Sistema Solar. "
            "Sua gravidade mantém os planetas e muitos outros corpos "
            "em órbita. A energia produzida no interior do Sol é "
            "fundamental para a vida na Terra."
        ),
        "curiosidades": [
            "O Sol é uma estrela.",
            "A luz solar leva cerca de oito minutos para chegar à Terra.",
            "O Sol concentra praticamente toda a massa do Sistema Solar."
        ]
    },

    # --------------------------------------------------------
    # EXOPLANETAS
    # --------------------------------------------------------

    "exoplaneta": {
        "titulo": "🪐 Exoplanetas",
        "texto": (
            "Exoplanetas são planetas que orbitam estrelas diferentes "
            "do Sol. Os astrônomos já encontraram milhares deles. "
            "Alguns são gigantes gasosos, outros são mundos rochosos, "
            "e existem planetas que não possuem equivalente direto "
            "no nosso Sistema Solar."
        ),
        "curiosidades": [
            "Alguns exoplanetas orbitam suas estrelas em poucos dias.",
            "Existem exoplanetas que orbitam duas estrelas.",
            "Alguns planetas podem ser encontrados vagando pelo espaço sem uma estrela."
        ]
    },

    # --------------------------------------------------------
    # BURACO NEGRO
    # --------------------------------------------------------

    "buraco negro": {
        "titulo": "🕳️ Buracos negros",
        "texto": (
            "Um buraco negro é uma região do espaço onde a gravidade "
            "é extremamente intensa. Existe uma região chamada "
            "horizonte de eventos. Depois desse limite, a luz não "
            "consegue escapar para chegar até um observador distante."
        ),
        "curiosidades": [
            "Nem todos os buracos negros são formados da mesma maneira.",
            "Existem buracos negros supermassivos no centro de galáxias.",
            "Podemos estudar buracos negros observando seus efeitos sobre o ambiente ao redor."
        ]
    },

    # --------------------------------------------------------
    # BURACO DE MINHOCA
    # --------------------------------------------------------

    "buraco de minhoca": {
        "titulo": "🌀 Buracos de minhoca",
        "texto": (
            "Buracos de minhoca são estruturas hipotéticas que aparecem "
            "em algumas soluções matemáticas da relatividade. "
            "Eles são imaginados como possíveis conexões entre "
            "regiões diferentes do espaço-tempo."
        ),
        "curiosidades": [
            "Não temos evidência observacional de um buraco de minhoca atravessável.",
            "Buracos de minhoca aparecem em modelos teóricos.",
            "Eles são diferentes de buracos negros, embora os dois conceitos estejam relacionados à gravidade."
        ]
    },

    # --------------------------------------------------------
    # GALÁXIAS
    # --------------------------------------------------------

    "galaxia": {
        "titulo": "🌌 Galáxias",
        "texto": (
            "Galáxias são enormes sistemas formados por estrelas, "
            "gás, poeira, matéria escura e outros componentes. "
            "A Via Láctea é a galáxia onde está o Sistema Solar."
        ),
        "curiosidades": [
            "Existem bilhões de galáxias no universo observável.",
            "Galáxias podem ter diferentes formas.",
            "Muitas galáxias possuem buracos negros supermassivos em suas regiões centrais."
        ]
    },

    # --------------------------------------------------------
    # VIA LÁCTEA
    # --------------------------------------------------------

    "via lactea": {
        "titulo": "🌌 Via Láctea",
        "texto": (
            "A Via Láctea é a galáxia que contém o Sistema Solar. "
            "Ela é uma galáxia espiral barrada e possui uma enorme "
            "quantidade de estrelas."
        ),
        "curiosidades": [
            "O Sistema Solar fica em uma região chamada Braço de Órion ou Esporão de Órion.",
            "A Via Láctea possui um buraco negro supermassivo em sua região central.",
            "O Sistema Solar leva centenas de milhões de anos para completar uma volta ao redor do centro galáctico."
        ]
    },

    # --------------------------------------------------------
    # BIG BANG
    # --------------------------------------------------------

    "big bang": {
        "titulo": "💥 Big Bang",
        "texto": (
            "O Big Bang é o nome dado ao modelo científico que "
            "descreve a evolução inicial do universo a partir de "
            "um estado extremamente quente e denso. O universo "
            "passou por uma expansão e continua evoluindo."
        ),
        "curiosidades": [
            "A expansão do universo é uma das principais ideias da cosmologia moderna.",
            "A Radiação Cósmica de Fundo é uma evidência importante sobre o universo primordial.",
            "O Big Bang não deve ser imaginado simplesmente como uma explosão acontecendo dentro de um espaço vazio."
        ]
    },

    # --------------------------------------------------------
    # MATÉRIA ESCURA
    # --------------------------------------------------------

    "materia escura": {
        "titulo": "🌑 Matéria escura",
        "texto": (
            "Matéria escura é o nome dado a um componente que "
            "não observamos diretamente pela luz, mas que parece "
            "produzir efeitos gravitacionais importantes em "
            "galáxias e estruturas cósmicas."
        ),
        "curiosidades": [
            "A matéria escura não é observada diretamente pela luz.",
            "Seu efeito gravitacional aparece em diferentes observações astronômicas.",
            "Sua natureza ainda é uma das grandes perguntas da Física."
        ]
    },

    # --------------------------------------------------------
    # ENERGIA ESCURA
    # --------------------------------------------------------

    "energia escura": {
        "titulo": "✨ Energia escura",
        "texto": (
            "Energia escura é o nome dado ao componente hipotético "
            "associado à expansão acelerada do universo. "
            "Sua natureza ainda não é completamente conhecida."
        ),
        "curiosidades": [
            "Ela é estudada principalmente por meio do comportamento da expansão cósmica.",
            "Não devemos confundir energia escura com matéria escura.",
            "Sua natureza é uma das grandes questões da cosmologia."
        ]
    },

    # --------------------------------------------------------
    # TEORIA DAS CORDAS
    # --------------------------------------------------------

    "teoria das cordas": {
        "titulo": "🧵 Teoria das cordas",
        "texto": (
            "A teoria das cordas é uma proposta da Física teórica "
            "na qual as partículas fundamentais são descritas "
            "como objetos extremamente pequenos semelhantes a "
            "cordas vibrantes. Diferentes formas de vibração "
            "poderiam corresponder a diferentes partículas."
        ),
        "curiosidades": [
            "A teoria das cordas tenta estabelecer uma descrição unificada de diferentes interações fundamentais.",
            "Algumas versões da teoria utilizam dimensões espaciais adicionais.",
            "A teoria das cordas continua sendo uma área de pesquisa teórica e não possui confirmação experimental direta."
        ]
    },

    # --------------------------------------------------------
    # ESTRELA
    # --------------------------------------------------------

    "estrela": {
        "titulo": "⭐ Estrelas",
        "texto": (
            "Estrelas são enormes objetos celestes formados principalmente "
            "por gás muito quente. Em seus interiores acontecem processos "
            "nucleares que liberam energia."
        ),
        "curiosidades": [
            "O Sol é uma estrela.",
            "As estrelas podem possuir massas, tamanhos e temperaturas diferentes.",
            "Algumas estrelas terminam suas vidas como anãs brancas, estrelas de nêutrons ou buracos negros."
        ]
    },

    # --------------------------------------------------------
    # SUPERNOVA
    # --------------------------------------------------------

    "supernova": {
        "titulo": "💥 Supernovas",
        "texto": (
            "Supernova é o nome usado para explosões estelares extremamente "
            "energéticas. Algumas estão associadas ao fim da vida de "
            "estrelas muito massivas, enquanto outras acontecem em "
            "sistemas envolvendo anãs brancas."
        ),
        "curiosidades": [
            "Supernovas podem produzir e espalhar elementos químicos pelo espaço.",
            "Elas podem ficar extremamente brilhantes.",
            "Seus restos podem formar nebulosas e outros objetos."
        ]
    },

    # --------------------------------------------------------
    # ESTRELA DE NÊUTRONS
    # --------------------------------------------------------

    "estrela de neutrons": {
        "titulo": "🌟 Estrelas de nêutrons",
        "texto": (
            "Uma estrela de nêutrons é um objeto extremamente compacto "
            "que pode surgir depois do colapso de uma estrela massiva. "
            "Ela concentra uma enorme quantidade de massa em uma região "
            "muito pequena."
        ),
        "curiosidades": [
            "Algumas estrelas de nêutrons giram muitas vezes por segundo.",
            "Pulsares são estrelas de nêutrons que emitem sinais periódicos que podemos detectar.",
            "A matéria em seu interior está em condições extremas."
        ]
    },

    # --------------------------------------------------------
    # COMETAS
    # --------------------------------------------------------

    "cometa": {
        "titulo": "☄️ Cometas",
        "texto": (
            "Cometas são corpos formados por gelo, poeira e materiais "
            "rochosos. Quando se aproximam do Sol, o aquecimento pode "
            "produzir uma coma e uma cauda."
        ),
        "curiosidades": [
            "A cauda de um cometa não necessariamente aponta para trás da trajetória.",
            "O vento solar ajuda a influenciar a direção da cauda.",
            "Muitos cometas possuem órbitas muito alongadas."
        ]
    },

    # --------------------------------------------------------
    # ASTEROIDES
    # --------------------------------------------------------

    "asteroide": {
        "titulo": "☄️ Asteroides",
        "texto": (
            "Asteroides são corpos rochosos ou metálicos menores "
            "que planetas. Muitos estão localizados no cinturão "
            "de asteroides entre Marte e Júpiter."
        ),
        "curiosidades": [
            "Nem todos os asteroides ficam no cinturão principal.",
            "Alguns passam relativamente perto da órbita da Terra.",
            "Asteroides ajudam os cientistas a estudar a formação do Sistema Solar."
        ]
    },

    # --------------------------------------------------------
    # METEORO
    # --------------------------------------------------------

    "meteoro": {
        "titulo": "🌠 Meteoros",
        "texto": (
            "Um meteoro é o fenômeno luminoso produzido quando "
            "um pequeno objeto espacial entra na atmosfera e "
            "interage com o ar."
        ),
        "curiosidades": [
            "A expressão popular 'estrela cadente' normalmente se refere a um meteoro.",
            "Meteoros não são estrelas.",
            "Quando um fragmento chega ao solo, ele pode ser chamado de meteorito."
        ]
    },

    # --------------------------------------------------------
    # ECLIPSE
    # --------------------------------------------------------

    "eclipse": {
        "titulo": "🌑 Eclipses",
        "texto": (
            "Um eclipse acontece quando um corpo celeste passa "
            "de maneira que outro corpo fica parcialmente ou "
            "totalmente encoberto. Existem eclipses solares e lunares."
        ),
        "curiosidades": [
            "Eclipses solares acontecem quando a Lua fica entre a Terra e o Sol.",
            "Eclipses lunares acontecem quando a Terra fica entre o Sol e a Lua.",
            "Nem toda Lua nova produz um eclipse solar."
        ]
    },

    # --------------------------------------------------------
    # GRAVIDADE
    # --------------------------------------------------------

    "gravidade": {
        "titulo": "🌍 Gravidade",
        "texto": (
            "A gravidade é uma interação fundamental da natureza. "
            "Ela participa da formação e do movimento de estrelas, "
            "planetas, galáxias e outros objetos do universo."
        ),
        "curiosidades": [
            "A gravidade ajuda a manter os planetas em órbita.",
            "A gravidade também participa da formação das estrelas.",
            "A gravidade pode alterar a trajetória da luz."
        ]
    },

    # --------------------------------------------------------
    # COLISÃO DE PLANETAS
    # --------------------------------------------------------

    "colisao de planetas": {
        "titulo": "💫 Colisões entre planetas",
        "texto": (
            "Colisões entre corpos planetários podem acontecer "
            "durante a formação de sistemas planetários. "
            "Dependendo das massas, velocidades e ângulos envolvidos, "
            "uma colisão pode produzir fragmentos, crateras ou até "
            "juntar parte dos corpos envolvidos."
        ),
        "curiosidades": [
            "A formação dos planetas envolveu muitas colisões entre corpos menores.",
            "Acredita-se que a Lua tenha se formado a partir de um grande impacto envolvendo a Terra primitiva.",
            "Uma colisão planetária não precisa necessariamente destruir completamente os dois corpos."
        ]
    },

    # --------------------------------------------------------
    # TELESCÓPIO
    # --------------------------------------------------------

    "telescopio": {
        "titulo": "🔭 Telescópios",
        "texto": (
            "Telescópios são instrumentos usados para observar "
            "objetos distantes. Eles podem trabalhar com diferentes "
            "tipos de radiação, como luz visível, infravermelho, "
            "rádio, raios X e outras faixas do espectro."
        ),
        "curiosidades": [
            "Nem todo telescópio observa luz visível.",
            "Telescópios espaciais evitam parte dos efeitos da atmosfera terrestre.",
            "Quanto mais longe observamos, mais estamos olhando para o passado."
        ]
    },

    # --------------------------------------------------------
    # VIDA EXTRATERRESTRE
    # --------------------------------------------------------

    "vida extraterrestre": {
        "titulo": "👽 Vida fora da Terra",
        "texto": (
            "A busca por vida fora da Terra é uma área de pesquisa "
            "científica. Os pesquisadores procuram ambientes que "
            "possam possuir condições favoráveis à vida, como "
            "água líquida e moléculas importantes."
        ),
        "curiosidades": [
            "Até o momento, a Terra é o único lugar onde sabemos que existe vida.",
            "Marte é estudado por causa de evidências de água em seu passado.",
            "Algumas luas de Júpiter e Saturno possuem ambientes interessantes para pesquisa."
        ]
    },

    # --------------------------------------------------------
    # KEPLER
    # --------------------------------------------------------

    "kepler": {
        "titulo": "📐 Leis de Kepler",
        "texto": (
            "Johannes Kepler formulou três leis que descrevem "
            "o movimento dos planetas ao redor do Sol. "
            "Essas leis ajudaram a transformar a descrição "
            "dos movimentos planetários em uma estrutura matemática."
        ),
        "curiosidades": [
            "As órbitas planetárias são elípticas.",
            "Os planetas não se movem sempre com a mesma velocidade orbital.",
            "As leis de Kepler foram fundamentais para o desenvolvimento da Física de Newton."
        ]
    },

    # --------------------------------------------------------
    # NEWTON
    # --------------------------------------------------------

    "newton": {
        "titulo": "🍎 Newton e a gravidade",
        "texto": (
            "Isaac Newton desenvolveu uma teoria da gravitação "
            "que permitiu explicar matematicamente muitos movimentos "
            "observados no céu e na Terra."
        ),
        "curiosidades": [
            "A mesma ideia de gravidade pode ser aplicada à queda de objetos e às órbitas.",
            "A teoria de Newton foi extremamente importante para a Astronomia.",
            "As leis de Newton continuam sendo usadas em muitas situações práticas."
        ]
    }

}


# ============================================================
# BANCO DE SINÔNIMOS
# ============================================================

SINONIMOS = {

    "mercúrio": "mercurio",
    "venus": "venus",
    "vênus": "venus",

    "júpiter": "jupiter",
    "jupiter": "jupiter",

    "saturno": "saturno",

    "urano": "urano",

    "netuno": "netuno",

    "marte": "marte",

    "terra": "terra",

    "plutão": "plutao",
    "plutao": "plutao",

    "lua": "lua",

    "sol": "sol",

    "buracos negros": "buraco negro",
    "buraco negro": "buraco negro",

    "buracos de minhoca": "buraco de minhoca",
    "buraco de minhoca": "buraco de minhoca",

    "galáxias": "galaxia",
    "galaxias": "galaxia",
    "galáxia": "galaxia",
    "galaxia": "galaxia",

    "via láctea": "via lactea",
    "via lactea": "via lactea",

    "exoplanetas": "exoplaneta",
    "exoplaneta": "exoplaneta",

    "matéria escura": "materia escura",
    "materia escura": "materia escura",

    "energia escura": "energia escura",

    "teoria das cordas": "teoria das cordas",

    "estrelas": "estrela",
    "estrela": "estrela",

    "supernovas": "supernova",
    "supernova": "supernova",

    "estrelas de nêutrons": "estrela de neutrons",
    "estrela de nêutrons": "estrela de neutrons",

    "cometas": "cometa",
    "cometa": "cometa",

    "asteroides": "asteroide",
    "asteroide": "asteroide",

    "meteoros": "meteoro",
    "meteoro": "meteoro",

    "eclipses": "eclipse",
    "eclipse": "eclipse",

    "telescópios": "telescopio",
    "telescopio": "telescopio",

    "vida extraterrestre": "vida extraterrestre",

    "gravidade": "gravidade",

    "colisão de planetas": "colisao de planetas",
    "colisões de planetas": "colisao de planetas",
    "colisao de planetas": "colisao de planetas",

    "kepler": "kepler",

    "newton": "newton"
}


# ============================================================
# DETECTAR TEMA
# ============================================================

def detectar_temas(pergunta):

    p = normalizar(pergunta)

    encontrados = []

    # Primeiro verifica expressões maiores
    expressoes = sorted(
        SINONIMOS.keys(),
        key=len,
        reverse=True
    )

    for expressao in expressoes:

        exp_normalizada = normalizar(
            expressao
        )

        if exp_normalizada in p:

            tema = SINONIMOS[
                expressao
            ]

            if tema not in encontrados:

                encontrados.append(
                    tema
                )

    return encontrados


# ============================================================
# PESQUISA WEB
# ============================================================

FONTES = [

    (
        "NASA",
        "nasa.gov"
    ),

    (
        "NASA Space Place",
        "spaceplace.nasa.gov"
    ),

    (
        "ESA",
        "esa.int"
    ),

    (
        "INPE",
        "gov.br/inpe"
    ),

    (
        "Observatório Nacional",
        "gov.br/on"
    ),

    (
        "União Astronômica Internacional",
        "iau.org"
    ),

    (
        "NOIRLab",
        "noirlab.edu"
    )
]


def pesquisar_web(pergunta):

    resultados = []

    # --------------------------------------------------------
    # DUCKDUCKGO
    # --------------------------------------------------------

    try:

        resposta = requests.get(
            "https://api.duckduckgo.com/",
            params={
                "q": pergunta,
                "format": "json",
                "no_html": "1",
                "skip_disambig": "0"
            },
            headers={
                "User-Agent":
                    "Mozilla/5.0"
            },
            timeout=15
        )

        if resposta.status_code == 200:

            dados = resposta.json()

            texto = limpar_texto(
                dados.get(
                    "AbstractText",
                    ""
                )
            )

            titulo = limpar_texto(
                dados.get(
                    "Heading",
                    ""
                )
            )

            url = dados.get(
                "AbstractURL",
                ""
            )

            if texto:

                resultados.append({

                    "fonte":
                        "DuckDuckGo / Wikipedia",

                    "titulo":
                        titulo or pergunta,

                    "texto":
                        texto,

                    "url":
                        url or ""

                })


            relacionados = dados.get(
                "RelatedTopics",
                []
            )


            for item in relacionados:

                if not isinstance(
                    item,
                    dict
                ):
                    continue

                texto_item = limpar_texto(
                    item.get(
                        "Text",
                        ""
                    )
                )

                url_item = item.get(
                    "FirstURL",
                    ""
                )

                if texto_item:

                    resultados.append({

                        "fonte":
                            "DuckDuckGo",

                        "titulo":
                            pergunta,

                        "texto":
                            texto_item,

                        "url":
                            url_item or ""

                    })


    except Exception:
        pass


    # --------------------------------------------------------
    # WIKIPEDIA
    # --------------------------------------------------------

    try:

        url_wiki = (
            "https://pt.wikipedia.org/api/rest_v1/"
            "page/summary/"
            + quote_plus(pergunta)
        )

        resposta_wiki = requests.get(
            url_wiki,
            headers={
                "User-Agent":
                    "ExploradorUniverso/1.0"
            },
            timeout=15
        )

        if resposta_wiki.status_code == 200:

            dados_wiki = (
                resposta_wiki.json()
            )

            texto_wiki = limpar_texto(
                dados_wiki.get(
                    "extract",
                    ""
                )
            )

            titulo_wiki = limpar_texto(
                dados_wiki.get(
                    "title",
                    ""
                )
            )

            pagina = (
                dados_wiki
                .get(
                    "content_urls",
                    {}
                )
                .get(
                    "desktop",
                    {}
                )
                .get(
                    "page",
                    ""
                )
            )

            if texto_wiki:

                resultados.append({

                    "fonte":
                        "Wikipedia",

                    "titulo":
                        titulo_wiki or pergunta,

                    "texto":
                        texto_wiki,

                    "url":
                        pagina or ""

                })


    except Exception:
        pass


    # --------------------------------------------------------
    # PESQUISAS DIRECIONADAS
    # --------------------------------------------------------

    for nome, dominio in FONTES:

        busca = quote_plus(
            f"{pergunta} site:{dominio}"
        )

        url_google = (
            "https://www.google.com/search?q="
            + busca
        )

        resultados.append({

            "fonte":
                nome,

            "titulo":
                f"Pesquisa sobre {pergunta}",

            "texto":
                (
                    f"Pesquisa direcionada para "
                    f"encontrar informações sobre "
                    f"'{pergunta}' no site "
                    f"{dominio}."
                ),

            "url":
                url_google

        })


    # --------------------------------------------------------
    # EVITAR DUPLICAÇÃO
    # --------------------------------------------------------

    finais = []

    vistos = set()

    for resultado in resultados:

        if not isinstance(
            resultado,
            dict
        ):
            continue

        texto = resultado.get(
            "texto",
            ""
        )

        url = resultado.get(
            "url",
            ""
        )

        if not texto:
            continue

        chave = (
            url
            if url
            else
            texto[:150]
        )

        if chave in vistos:
            continue

        vistos.add(chave)

        finais.append(
            resultado
        )


    return finais[:20]


# ============================================================
# CURIOSIDADES GERAIS
# ============================================================

CURIOSIDADES_GERAIS = [

    "🌌 O universo observável contém uma quantidade gigantesca de galáxias.",

    "🪐 Existem milhares de planetas conhecidos fora do Sistema Solar.",

    "☀️ O Sol é apenas uma entre muitas estrelas da Via Láctea.",

    "🌍 Até hoje, a Terra é o único lugar onde sabemos com certeza que existe vida.",

    "🕳️ Buracos negros podem ser estudados mesmo sem serem observados diretamente pela luz.",

    "🔭 Observar objetos muito distantes também significa observar eventos que aconteceram no passado.",

    "☄️ Muitos pequenos corpos do Sistema Solar são restos da formação planetária.",

    "🌙 A Lua influencia as marés dos oceanos terrestres.",

    "🌌 A Via Láctea é apenas uma entre muitas galáxias.",

    "⭐ O Sol possui massa suficiente para dominar gravitacionalmente o Sistema Solar.",

    "💫 Colisões e encontros gravitacionais participam da evolução dos sistemas planetários.",

    "🧵 A teoria das cordas é uma proposta teórica e ainda não possui confirmação experimental direta.",

    "🌀 Buracos de minhoca são possibilidades teóricas, não objetos que já tenham sido observados.",

    "🌑 Matéria escura é estudada principalmente pelos seus efeitos gravitacionais.",

    "✨ As estrelas podem ter destinos muito diferentes dependendo principalmente de suas massas."
]


# ============================================================
# GERAR RESPOSTA
# ============================================================

def gerar_resposta(
    pergunta,
    resultados
):

    temas = detectar_temas(
        pergunta
    )

    resposta = []

    resposta.append(
        "## 🔭 Vamos explorar o universo!"
    )

    resposta.append(
        f"Você perguntou: **{pergunta}**"
    )


    # --------------------------------------------------------
    # TEMAS ENCONTRADOS
    # --------------------------------------------------------

    temas_usados = 0

    for tema in temas:

        if tema not in CONHECIMENTO:
            continue

        dados = CONHECIMENTO[
            tema
        ]

        resposta.append(
            f"### {dados['titulo']}"
        )

        resposta.append(
            dados["texto"]
        )


        # Curiosidades específicas

        resposta.append(
            "#### 💡 Curiosidades"
        )

        for curiosidade in dados[
            "curiosidades"
        ]:

            resposta.append(
                f"- {curiosidade}"
            )


        temas_usados += 1


        if temas_usados >= 5:
            break


    # --------------------------------------------------------
    # PERGUNTA SOBRE TODOS OS PLANETAS
    # --------------------------------------------------------

    p = normalizar(
        pergunta
    )


    palavras_planetas = [

        "planetas do sistema solar",
        "planetas do sistema",
        "todos os planetas",
        "sistema solar",
        "planetas"
    ]


    if any(
        palavra in p
        for palavra in palavras_planetas
    ):

        resposta.append(
            "### 🪐 Os oito planetas do Sistema Solar"
        )

        resposta.append(
            """
O Sistema Solar possui oito planetas. Eles podem ser
divididos de maneira simples em quatro planetas rochosos
mais próximos do Sol — Mercúrio, Vênus, Terra e Marte —
e quatro planetas gigantes nas regiões externas —
Júpiter, Saturno, Urano e Netuno.
"""
        )


        ordem = [

            ("mercurio", "☿ Mercúrio"),
            ("venus", "♀️ Vênus"),
            ("terra", "🌍 Terra"),
            ("marte", "♂️ Marte"),
            ("jupiter", "♃ Júpiter"),
            ("saturno", "♄ Saturno"),
            ("urano", "♅ Urano"),
            ("netuno", "♆ Netuno")

        ]


        for chave, nome in ordem:

            dados = CONHECIMENTO[
                chave
            ]

            resposta.append(
                f"#### {nome}"
            )

            resposta.append(
                dados["texto"]
            )


    # --------------------------------------------------------
    # COLISÃO
    # --------------------------------------------------------

    if (
        "colis" in p
        and (
            "planeta" in p
            or "terra" in p
            or "lua" in p
        )
    ):

        resposta.append(
            "### 💫 E se dois planetas colidissem?"
        )

        resposta.append(
            """
Uma colisão planetária seria um evento extremamente energético.
O resultado dependeria das massas, velocidades, composição e
ângulo do impacto. Os corpos poderiam se deformar, produzir
fragmentos, formar uma grande quantidade de detritos ou,
em algumas situações, parte do material poderia se juntar.
"""
        )


    # --------------------------------------------------------
    # CURIOSIDADE
    # --------------------------------------------------------

    if any(
        palavra in p
        for palavra in [
            "curiosidade",
            "curiosidades",
            "fato curioso",
            "coisa interessante",
            "interessante"
        ]
    ):

        resposta.append(
            "### 🌟 Curiosidades do universo"
        )

        selecionadas = random.sample(
            CURIOSIDADES_GERAIS,
            min(
                6,
                len(CURIOSIDADES_GERAIS)
            )
        )

        for item in selecionadas:

            resposta.append(
                f"- {item}"
            )


    # --------------------------------------------------------
    # VIDA
    # --------------------------------------------------------

    if any(
        palavra in p
        for palavra in [
            "vida",
            "alien",
            "extraterrestre",
            "habitavel",
            "habitável"
        ]
    ):

        dados = CONHECIMENTO[
            "vida extraterrestre"
        ]

        resposta.append(
            f"### {dados['titulo']}"
        )

        resposta.append(
            dados["texto"]
        )

        resposta.append(
            "#### 🔎 O que os cientistas procuram?"
        )

        resposta.append(
            """
Os pesquisadores procuram ambientes que possam apresentar
condições favoráveis à vida. Isso pode envolver água líquida,
moléculas importantes para a química da vida e fontes de energia.
Encontrar condições favoráveis, porém, não significa encontrar
vida.
"""
        )


    # --------------------------------------------------------
    # PERGUNTA GENÉRICA
    # --------------------------------------------------------

    if not temas and len(
        resposta
    ) <= 2:

        resposta.append(
            "### 🌌 Uma visão geral"
        )

        resposta.append(
            f"""
A sua pergunta é sobre **{pergunta}**. A Astronomia e a
Astrofísica estudam objetos e fenômenos que acontecem no
universo. Para investigar perguntas como essa, os cientistas
usam observações, telescópios, modelos matemáticos, simulações
e diferentes tipos de radiação.
"""
        )


        resposta.append(
            "### 🔬 Como pesquisar esse assunto?"
        )

        resposta.append(
            """
Uma boa investigação científica compara observações com
modelos e procura evidências. Por isso, quando uma pergunta
envolve um fenômeno ainda hipotético, é importante separar
aquilo que já foi observado daquilo que ainda é apenas uma
possibilidade teórica.
"""
        )


    # --------------------------------------------------------
    # PESQUISA
    # --------------------------------------------------------

    if resultados:

        resposta.append(
            "## 🌐 Pesquisa complementar"
        )

        resposta.append(
            """
Também procurei informações relacionadas à pergunta.
As fontes abaixo podem ser utilizadas para aprofundar
a pesquisa.
"""
        )


        quantidade = 0


        for fonte in resultados:

            if quantidade >= 6:
                break

            if not isinstance(
                fonte,
                dict
            ):
                continue


            nome = fonte.get(
                "fonte",
                "Fonte"
            )

            titulo = fonte.get(
                "titulo",
                "Pesquisa"
            )

            texto = fonte.get(
                "texto",
                ""
            )

            url = fonte.get(
                "url",
                ""
            )


            texto = limpar_texto(
                texto
            )


            if not texto:
                continue


            if len(texto) > 600:

                texto = (
                    texto[:600]
                    + "..."
                )


            resposta.append(
                f"### 🔬 {nome}"
            )

            resposta.append(
                f"**{titulo}**"
            )

            resposta.append(
                texto
            )


            if url:

                resposta.append(
                    f"[🔗 Abrir fonte]({url})"
                )


            quantidade += 1


    # --------------------------------------------------------
    # RESUMO
    # --------------------------------------------------------

    resposta.append(
        "## 🌟 Resumo"
    )

    resposta.append(
        """
A melhor maneira de aprender Astronomia é fazer perguntas,
comparar ideias e observar quais explicações possuem evidências.
O universo é enorme e muitas perguntas ainda estão sendo
investigadas pelos cientistas.
"""
    )


    return "\n\n".join(
        resposta
    )


# ============================================================
# MODO ASTRONOMIA
# ============================================================

def mostrar_astronomia():

    st.title(
        "🌌 Explorador do Universo"
    )

    st.markdown(
        """
### 🔭 Pergunte qualquer coisa sobre Astronomia!

Não precisa escolher um assunto em uma lista.

Você pode perguntar:

**🪐** "Explique todos os planetas do Sistema Solar"

**☄️** "O que aconteceria se dois planetas colidissem?"

**🕳️** "O que acontece dentro de um buraco negro?"

**🌀** "Buracos de minhoca existem?"

**🌌** "Como as galáxias se formam?"

**🧵** "O que é a teoria das cordas?"

**👽** "Existe possibilidade de vida em outros planetas?"

**✨** "Me conte curiosidades sobre o universo"

**🔭** "Como descobrimos exoplanetas?"

**💥** "O que foi o Big Bang?"
"""
    )


    st.markdown("---")


    pergunta = st.text_area(
        "🚀 Faça sua pergunta:",
        height=130,
        placeholder=(
            "Digite aqui qualquer pergunta sobre "
            "o universo..."
        )
    )


    col1, col2 = st.columns(2)


    with col1:

        pesquisar = st.button(
            "🔭 Pesquisar",
            use_container_width=True
        )


    with col2:

        limpar = st.button(
            "🧹 Limpar",
            use_container_width=True
        )


    if limpar:

        st.session_state.historico_astronomia = []

        st.rerun()


    if pesquisar:

        if not pergunta.strip():

            st.warning(
                "Digite uma pergunta."
            )

        else:

            with st.spinner(
                "🌌 Investigando o universo..."
            ):

                resultados = pesquisar_web(
                    pergunta
                )

                resposta = gerar_resposta(
                    pergunta,
                    resultados
                )


            registro = {

                "pergunta":
                    pergunta,

                "resposta":
                    resposta,

                "fontes":
                    resultados

            }


            st.session_state.historico_astronomia.insert(
                0,
                registro
            )


    st.markdown("---")


    # --------------------------------------------------------
    # HISTÓRICO
    # --------------------------------------------------------

    for registro in (
        st.session_state
        .historico_astronomia
    ):

        st.markdown(
            '<div class="caixa">',
            unsafe_allow_html=True
        )


        st.markdown(
            '<div class="pergunta">',
            unsafe_allow_html=True
        )

        st.markdown(
            f"### ❓ {registro['pergunta']}"
        )

        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


        st.markdown(
            registro["resposta"]
        )


        st.markdown(
            "</div>",
            unsafe_allow_html=True
        )


# ============================================================
# BANCO DO JOGO
# ============================================================

QUESTOES_JOGO = [

    {
        "pergunta":
            "Qual é o maior planeta do Sistema Solar?",

        "opcoes": [
            "Mercúrio",
            "Terra",
            "Júpiter",
            "Marte"
        ],

        "resposta":
            "Júpiter"
    },

    {
        "pergunta":
            "Qual planeta é conhecido como planeta vermelho?",

        "opcoes": [
            "Marte",
            "Vênus",
            "Saturno",
            "Netuno"
        ],

        "resposta":
            "Marte"
    },

    {
        "pergunta":
            "Qual é a estrela do Sistema Solar?",

        "opcoes": [
            "Sirius",
            "Sol",
            "Betelgeuse",
            "Vega"
        ],

        "resposta":
            "Sol"
    },

    {
        "pergunta":
            "Qual planeta possui os famosos anéis?",

        "opcoes": [
            "Terra",
            "Mercúrio",
            "Saturno",
            "Marte"
        ],

        "resposta":
            "Saturno"
    },

    {
        "pergunta":
            "Como se chama um planeta que orbita outra estrela?",

        "opcoes": [
            "Asteroide",
            "Exoplaneta",
            "Meteoro",
            "Cometa"
        ],

        "resposta":
            "Exoplaneta"
    },

    {
        "pergunta":
            "Qual é a galáxia do Sistema Solar?",

        "opcoes": [
            "Andrômeda",
            "Via Láctea",
            "Sombrero",
            "Triângulo"
        ],

        "resposta":
            "Via Láctea"
    },

    {
        "pergunta":
            "O que é um buraco negro?",

        "opcoes": [
            "Uma estrela comum",
            "Uma região de gravidade extremamente intensa",
            "Um planeta",
            "Uma galáxia"
        ],

        "resposta":
            "Uma região de gravidade extremamente intensa"
    },

    {
        "pergunta":
            "Qual é o planeta mais próximo do Sol?",

        "opcoes": [
            "Vênus",
            "Terra",
            "Mercúrio",
            "Marte"
        ],

        "resposta":
            "Mercúrio"
    }

]


# ============================================================
# MODO JOGO
# ============================================================

def mostrar_jogo():

    st.title(
        "⚔️ Cavaleiros do Zodíaco — Desafio Cósmico"
    )

    st.markdown(
        """
### 🏛️ Treine seu Cosmo!

Responda às perguntas de Astronomia
e avance pelo Santuário.
"""
    )


    # --------------------------------------------------------
    # PLACAR
    # --------------------------------------------------------

    col1, col2, col3 = st.columns(3)


    with col1:

        st.metric(
            "🛡️ Alfa",
            st.session_state.alfa
        )


    with col2:

        st.metric(
            "⚔️ Beta",
            st.session_state.beta
        )


    with col3:

        st.metric(
            "🌟 Gama",
            st.session_state.gama
        )


    st.markdown("---")


    if (
        st.session_state.pergunta_jogo
        >= len(QUESTOES_JOGO)
    ):

        st.success(
            "🏆 O desafio terminou!"
        )

        if st.button(
            "🔄 Novo jogo"
        ):

            st.session_state.pergunta_jogo = 0

            st.session_state.alfa = 0
            st.session_state.beta = 0
            st.session_state.gama = 0

            st.rerun()

        return


    q = QUESTOES_JOGO[
        st.session_state.pergunta_jogo
    ]


    equipes = [
        "Alfa",
        "Beta",
        "Gama"
    ]


    equipe = equipes[
        st.session_state.pergunta_jogo
        % 3
    ]


    st.info(
        f"⚔️ Vez da Equipe **{equipe}**"
    )


    resposta = st.radio(
        q["pergunta"],
        q["opcoes"],
        key=(
            f"jogo_"
            f"{st.session_state.pergunta_jogo}"
        )
    )


    if st.button(
        "🌟 Responder"
    ):

        if resposta == q["resposta"]:

            st.success(
                "🎉 Resposta correta!"
            )


            if equipe == "Alfa":

                st.session_state.alfa += 1

            elif equipe == "Beta":

                st.session_state.beta += 1

            else:

                st.session_state.gama += 1


        else:

            st.error(
                "❌ Resposta incorreta!"
            )

            st.info(
                f"A resposta correta é: "
                f"**{q['resposta']}**"
            )


        st.session_state.historico_professor.append({

            "equipe":
                equipe,

            "pergunta":
                q["pergunta"],

            "resposta":
                resposta,

            "correta":
                q["resposta"],

            "status":
                (
                    "CORRETA"
                    if resposta == q["resposta"]
                    else "INCORRETA"
                )

        })


        st.session_state.pergunta_jogo += 1

        st.rerun()


# ============================================================
# ÁREA DO PROFESSOR
# ============================================================

def mostrar_professor():

    st.title(
        "👨‍🏫 Área do Professor"
    )


    if not st.session_state.prof_logado:

        st.info(
            "Faça login para acessar a área do professor."
        )


        login = st.text_input(
            "Login"
        )

        senha = st.text_input(
            "Senha",
            type="password"
        )


        if st.button(
            "🔐 Entrar"
        ):

            if (
                login == "Felipe Ferreira"
                and
                senha == "Ff241198"
            ):

                st.session_state.prof_logado = True

                st.success(
                    "Login realizado."
                )

                st.rerun()

            else:

                st.error(
                    "Login ou senha incorretos."
                )


        return


    st.success(
        "👨‍🏫 Professor conectado."
    )


    if st.button(
        "🚪 Sair"
    ):

        st.session_state.prof_logado = False

        st.rerun()


    st.markdown("---")


    st.subheader(
        "📊 Histórico de respostas"
    )


    if not st.session_state.historico_professor:

        st.info(
            "Ainda não existem respostas registradas."
        )

    else:

        for i, item in enumerate(
            st.session_state.historico_professor,
            1
        ):

            with st.expander(
                f"Registro {i}"
            ):

                st.write(
                    item
                )


        texto = ""

        for i, item in enumerate(
            st.session_state.historico_professor,
            1
        ):

            texto += (
                f"REGISTRO {i}\n"
            )

            for chave, valor in item.items():

                texto += (
                    f"{chave}: {valor}\n"
                )

            texto += "\n"


        st.download_button(
            "📥 Baixar relatório",
            data=texto,
            file_name="relatorio_professor.txt",
            mime="text/plain"
        )


        if st.button(
            "🗑️ Limpar registros"
        ):

            st.session_state.historico_professor = []

            st.rerun()


# ============================================================
# MENU PRINCIPAL
# ============================================================

st.sidebar.title(
    "🌌 Explorador Cósmico"
)


st.session_state.modo = st.sidebar.radio(
    "Escolha:",
    [
        "🌌 Explorador de Astronomia",
        "⚔️ Jogo dos Cavaleiros",
        "👨‍🏫 Professor"
    ]
)


# ============================================================
# EXECUTAR
# ============================================================

if (
    st.session_state.modo
    == "🌌 Explorador de Astronomia"
):

    mostrar_astronomia()


elif (
    st.session_state.modo
    == "⚔️ Jogo dos Cavaleiros"
):

    mostrar_jogo()


elif (
    st.session_state.modo
    == "👨‍🏫 Professor"
):

    mostrar_professor()
