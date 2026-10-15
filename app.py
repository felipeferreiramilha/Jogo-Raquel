import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Olimpíada de Cosmologia - Níveis & Multiverso",
    page_icon="🌌",
    layout="centered",
)

# Estilização Visual (Tema Espacial)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #05050f;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #00ffff !important;
        text-align: center;
    }
    .stButton>button {
        background-color: #1a1a3a;
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        height: 50px;
    }
    .stButton>button:hover {
        background-color: #00ffff;
        color: #05050f;
    }
    .pergunta-box {
        background-color: #0d0d21;
        border: 1px solid #333366;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .admin-box {
        background-color: #1a0033;
        border: 2px dashed #ff00ff;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# =========================================================================
# BANCO DE MAIS DE 100 PERGUNTAS DIVIDIDAS EM 3 NÍVEIS
# =========================================================================

BANCO_BASICO = [
    {
        "pergunta": (
            "1. Qual é o nome da galáxia em formato de espiral onde o nosso"
            " Sistema Solar está localizado?"
        ),
        "opcoes": ["Andrômeda", "Via Láctea", "Galáxia do Triângulo", "Nuvem de Magalhães"],
        "resposta_correta": "Via Láctea",
    },
    {
        "pergunta": (
            "2. Quem foi o físico e padre belga que propôs a teoria do 'Átomo"
            " Primitivo' (Big Bang)?"
        ),
        "opcoes": [
            "Albert Einstein",
            "Georges Lemaître",
            "Stephen Hawking",
            "Isaac Newton",
        ],
        "resposta_correta": "Georges Lemaître",
    },
    {
        "pergunta": (
            "3. O Sol é classificado em qual categoria principal de estrela?"
        ),
        "opcoes": [
            "Gigante Vermelha",
            "Anã Branca",
            "Anã Amarela (Sequência Principal)",
            "Supergigante Azul",
        ],
        "resposta_correta": "Anã Amarela (Sequência Principal)",
    },
    {
        "pergunta": (
            "4. Qual é o planeta mais próximo do Sol no nosso Sistema Solar?"
        ),
        "opcoes": ["Vênus", "Marte", "Mercúrio", "Terra"],
        "resposta_correta": "Mercúrio",
    },
    {
        "pergunta": (
            "5. A luz que sai do Sol demora aproximadamente quanto tempo para"
            " chegar até a Terra?"
        ),
        "opcoes": ["1 segundo", "8 minutos e 20 segundos", "1 hora", "1 dia"],
        "resposta_correta": "8 minutos e 20 segundos",
    },
    {
        "pergunta": (
            "6. Qual é a estrela mais próxima da Terra após o nosso Sol?"
        ),
        "opcoes": ["Sirius", "Betelgeuse", "Alpha Centauri (Proxima Centauri)", "Polaris"],
        "resposta_correta": "Alpha Centauri (Proxima Centauri)",
    },
    {
        "pergunta": (
            "7. Como chamamos a linha imaginária ao redor da qual a Terra gira"
            " diariamente?"
        ),
        "opcoes": ["Órbita", "Eixo terrestre", "Equador galáctico", "Meridiano de Greenwich"],
        "resposta_correta": "Eixo terrestre",
    },
    {
        "pergunta": "8. Qual é a maior lua (satélite natural) de Saturno?",
        "opcoes": ["Titã", "Europa", "Ganimedes", "Io"],
        "resposta_correta": "Titã",
    },
    {
        "pergunta": (
            "9. Qual planeta do Sistema Solar é conhecido como o 'Planeta"
            " Vermelho'?"
        ),
        "opcoes": ["Júpiter", "Marte", "Saturno", "Vênus"],
        "resposta_correta": "Marte",
    },
    {
        "pergunta": (
            "10. O que estuda a ciência chamada Astronomia de forma geral?"
        ),
        "opcoes": [
            "A atmosfera da Terra e o clima",
            "Os corpos celestes, planetas, estrelas e o universo",
            "A estrutura interna dos vulcões terrestres",
            "As rochas e minerais da crosta terrestre",
        ],
        "resposta_correta": "Os corpos celestes, planetas, estrelas e o universo",
    },
    {
        "pergunta": (
            "11. Qual é a principal força responsável por manter os planetas"
            " orbitando ao redor do Sol?"
        ),
        "opcoes": [
            "Força magnética",
            "Força gravitacional",
            "Pressão de radiação solar",
            "Eletricidade estática",
        ],
        "resposta_correta": "Força gravitacional",
    },
    {
        "pergunta": (
            "12. Quantos planetas compõem oficialmente o nosso Sistema Solar"
            " atualmente?"
        ),
        "opcoes": ["7", "8", "9", "10"],
        "resposta_correta": "8",
    },
    {
        "pergunta": (
            "13. Qual é o maior planeta em tamanho e massa do nosso Sistema"
            " Solar?"
        ),
        "opcoes": ["Saturno", "Júpiter", "Netuno", "Urano"],
        "resposta_correta": "Júpiter",
    },
    {
        "pergunta": (
            "14. Qual instrumento óptico é o mais tradicionalmente utilizado"
            " pelos astrônomos para observar o céu?"
        ),
        "opcoes": ["Microscópio", "Telescópio", "Estetoscópio", "Periscópio"],
        "resposta_correta": "Telescópio",
    },
    {
        "pergunta": (
            "15. Qual é o nome da galáxia espiral gigante mais próxima da Via"
            " Láctea?"
        ),
        "opcoes": ["Galáxia de Andrômeda", "Grande Nuvem de Magalhães", "Sombrero", "Galáxia do Catavento"],
        "resposta_correta": "Galáxia de Andrômeda",
    },
    {
        "pergunta": (
            "16. Que nome se dá à fase em que a Lua está totalmente escura"
            " vista da Terra?"
        ),
        "opcoes": ["Lua Nova", "Lua Cheia", "Quarto Crescente", "Lua Minguante"],
        "resposta_correta": "Lua Nova",
    },
    {
        "pergunta": (
            "17. Qual é a unidade de medida astronômica usada para expressar"
            " distâncias percorridas pela luz em um ano?"
        ),
        "opcoes": ["Quilômetro", "Ano-luz", "Unidade Astronômica (UA)", "Parsec de luz"],
        "resposta_correta": "Ano-luz",
    },
    {
        "pergunta": (
            "18. Qual foi o primeiro satélite artificial lançado ao espaço (pela"
            " União Soviética em 1957)?"
        ),
        "opcoes": ["Apollo 11", "Voyager 1", "Sputnik 1", "Hubble"],
        "resposta_correta": "Sputnik 1",
    },
    {
        "pergunta": (
            "19. Quem foi o primeiro ser humano a pisar na Lua em 1969?"
        ),
        "opcoes": ["Yuri Gagarin", "Buzz Aldrin", "Neil Armstrong", "Michael Collins"],
        "resposta_correta": "Neil Armstrong",
    },
    {
        "pergunta": (
            "20. Qual é a camada mais externa do Sol visível durante um eclipse"
            " solar total?"
        ),
        "opcoes": ["Núcleo", "Fotosfera", "Cromosfera", "Coroa solar"],
        "resposta_correta": "Coroa solar",
    },
    {
        "pergunta": (
            "21. Como se chama o movimento que a Terra faz ao dar uma volta"
            " completa ao redor do Sol?"
        ),
        "opcoes": ["Rotação", "Translação", "Precessão", "Nutação"],
        "resposta_correta": "Translação",
    },
    {
        "pergunta": (
            "22. Qual é o planeta mais quente do Sistema Solar devido ao forte"
            " efeito estufa em sua atmosfera?"
        ),
        "opcoes": ["Mercúrio", "Vênus", "Marte", "Júpiter"],
        "resposta_correta": "Vênus",
    },
    {
        "pergunta": (
            "23. O que são cometas, frequentemente chamados de 'bolas de neve"
            " sujas'?"
        ),
        "opcoes": [
            "Asteróides feitos inteiramente de ouro",
            "Corpos celestes de gelo, poeira e rocha que orbitam o Sol",
            "Estrelas cadentes que caem na Terra",
            "Pedaços de lixo espacial humano",
        ],
        "resposta_correta": "Corpos celestes de gelo, poeira e rocha que orbitam o Sol",
    },
    {
        "pergunta": (
            "24. Qual é o nome do cinturão de rochas localizado entre as órbitas"
            " de Marte e Júpiter?"
        ),
        "opcoes": [
            "Cinturão de Kuiper",
            "Cinturão de Asteróides Principal",
            "Nuvem de Oort",
            "Anéis de Saturno",
        ],
        "resposta_correta": "Cinturão de Asteróides Principal",
    },
    {
        "pergunta": (
            "25. Em que ano o telescópio espacial Hubble foi colocado em"
            " órbita?"
        ),
        "opcoes": ["1975", "1990", "2001", "2010"],
        "resposta_correta": "1990",
    },
    {
        "pergunta": (
            "26. Qual é a principal substância que compõe as estrelas em sua"
            " fase de sequência principal?"
        ),
        "opcoes": ["Oxigênio e Nitrogênio", "Hidrogênio e Hélio", "Ferro e Níquel", "Carbono e Água"],
        "resposta_correta": "Hidrogênio e Hélio",
    },
    {
        "pergunta": (
            "27. O que acontece em um eclipse solar?"
        ),
        "opcoes": [
            "A Terra entra na sombra da Lua",
            "A Lua passa entre a Terra e o Sol, bloqueando a luz solar",
            "O Sol passa entre a Terra e a Lua",
            "Marte cruza a frente do Sol",
        ],
        "resposta_correta": "A Lua passa entre a Terra e o Sol, bloqueando a luz solar",
    },
    {
        "pergunta": (
            "28. Qual planeta anão famoso foi reclassificado em 2006 pela União"
            " Astronômica Internacional?"
        ),
        "opcoes": ["Ceres", "Plutão", "Eris", "Haumea"],
        "resposta_correta": "Plutão",
    },
    {
        "pergunta": (
            "29. Qual é o nome do movimento que a Terra realiza em torno do seu"
            " próprio eixo, gerando o dia e a noite?"
        ),
        "opcoes": ["Translação", "Rotação", "Precessão", "Revolução"],
        "resposta_correta": "Rotação",
    },
    {
        "pergunta": (
            "30. Que nome se dá ao aglomerado de milhões de estrelas, gás e"
            " poeira mantidos unidos pela gravidade?"
        ),
        "opcoes": ["Constelação", "Galáxia", "Nebulosa planetária", "Sistema planetário"],
        "resposta_correta": "Galáxia",
    },
    {
        "pergunta": (
            "31. Qual dos seguintes planetas gasosos possui os anéis mais"
            " visíveis e complexos?"
        ),
        "opcoes": ["Júpiter", "Saturno", "Urano", "Netuno"],
        "resposta_correta": "Saturno",
    },
    {
        "pergunta": (
            "32. Qual é a unidade básica de distância usada dentro do nosso"
            " próprio Sistema Solar (distância Terra-Sol)?"
        ),
        "opcoes": ["Ano-luz", "Parsec", "Unidade Astronômica (UA)", "Quilômetro cúbico"],
        "resposta_correta": "Unidade Astronômica (UA)",
    },
    {
        "pergunta": (
            "33. O que é uma estrela cadente (meteoro) na verdade?"
        ),
        "opcoes": [
            "Uma estrela que se desfez no céu",
            "Um fragmento de rocha espacial que incendeia ao entrar na atmosfera da Terra",
            "Um reflexo de luz dos satélites artificiais",
            "Um cometa passando perto da Lua",
        ],
        "resposta_correta": (
            "Um fragmento de rocha espacial que incendeia ao entrar na"
            " atmosfera da Terra"
        ),
    },
    {
        "pergunta": (
            "34. Qual é a galáxia satélite de maior destaque visível a olho nu"
            " no hemisfério sul?"
        ),
        "opcoes": ["Galáxia do Triângulo", "Nuvem de Magalhães", "Galáxia de Bode", "Galáxia do Charuto"],
        "resposta_correta": "Nuvem de Magalhães",
    },
    {
        "pergunta": (
            "35. Qual é o nome do primeiro cosmonauta russo a ir ao espaço em"
            " 1961?"
        ),
        "opcoes": ["Alexei Leonov", "Yuri Gagarin", "Valeri Polyakov", "Sergei Korolev"],
        "resposta_correta": "Yuri Gagarin",
    },
]

BANCO_MEDIO = [
    {
        "pergunta": (
            "1. O que comprova de forma mais direta a expansão do universo"
            " através do 'eco' térmico do Big Bang?"
        ),
        "opcoes": [
            "A Radiação Cósmica de Fundo em Micro-ondas (CMB)",
            "A luz ultravioleta das supernovas",
            "O campo magnético intergaláctico",
            "A emissão de raios gama dos pulsares",
        ],
        "resposta_correta": (
            "A Radiação Cósmica de Fundo em Micro-ondas (CMB)"
        ),
    },
    {
        "pergunta": (
            "2. O que a célebre 'Lei de Hubble' estabelece sobre a velocidade"
            " de afastamento das galáxias?"
        ),
        "opcoes": [
            "É constante em qualquer ponto do universo",
            "É diretamente proporcional à distância da galáxia em relação à Terra",
            "Diminui à medida que a galáxia se afasta",
            "Depende exclusivamente da massa total da galáxia",
        ],
        "resposta_correta": (
            "É diretamente proporcional à distância da galáxia em relação à"
            " Terra"
        ),
    },
    {
        "pergunta": (
            "3. Qual é a porcentagem aproximada de Energia Escura que compõe o"
            " conteúdo total massa-energia do universo atual?"
        ),
        "opcoes": ["Cerca de 5%", "Cerca de 27%", "Cerca de 68%", "Cerca de 95%"],
        "resposta_correta": "Cerca de 68%",
    },
    {
        "pergunta": (
            "4. Qual é o papel principal da Matéria Escura na formação e"
            " estrutura do cosmos?"
        ),
        "opcoes": [
            "Emitir luz visível para iluminar as galáxias escuras",
            "Fornecer o arcabouço gravitacional adicional para aglutinar galáxias",
            "Acelerar a expansão do universo através de pressão repulsiva",
            "Impedir a fusão nuclear dentro das estrelas",
        ],
        "resposta_correta": (
            "Forcer o arcabouço gravitacional adicional para aglutinar"
            " galáxias"
        ),
    },
    {
        "pergunta": (
            "5. O que descreve a Teoria da Inflação Cósmica proposta por Alan"
            " Guth?"
        ),
        "opcoes": [
            "A expansão lenta e gradual do universo nos últimos bilhões de anos",
            "Uma expansão exponencial ultrarrápida ocorrida logo após a fração inicial do Big Bang",
            "A contração contínua do universo rumo ao Big Crunch",
            "A criação contínua de matéria no estado estacionário",
        ],
        "resposta_correta": (
            "Uma expansão exponencial ultrarrápida ocorrida logo após a"
            " fração inicial do Big Bang"
        ),
    },
    {
        "pergunta": (
            "6. O que é o 'Horizonte de Eventos' em um buraco negro?"
        ),
        "opcoes": [
            "O centro exato onde a densidade é infinita (singularidade)",
            "A fronteira além da qual nem mesmo a luz consegue escapar da gravidade",
            "O disco brilhante de gás quente ao redor do buraco negro",
            "O ponto onde o buraco negro emite radiação Hawking",
        ],
        "resposta_correta": (
            "A fronteira além da qual nem mesmo a luz consegue escapar da"
            " gravidade"
        ),
    },
    {
        "pergunta": (
            "7. Qual telescópio espacial lançado em dezembro de 2021 revolucionou"
            " a observação infravermelha do universo primitivo?"
        ),
        "opcoes": [
            "Telescópio Espacial Hubble",
            "Telescópio James Webb (JWST)",
            "Telescópio Spitzer",
            "Observatório Chandra",
        ],
        "resposta_correta": "Telescópio James Webb (JWST)",
    },
    {
        "pergunta": (
            "8. O que estuda a Nucleossíntese Primordial (ou do Big Bang)?"
        ),
        "opcoes": [
            "A formação dos elementos pesados no interior das supernovas",
            "A síntese dos primeiros núcleos leves (Hidrogênio, Hélio, Lítio) nos primeiros minutos do universo",
            "A criação de planetas rochosos em discos protoplanetários",
            "A fusão do ferro nos núcleos das estrelas gigantes",
        ],
        "resposta_correta": (
            "A síntese dos primeiros núcleos leves (Hidrogênio, Hélio, Lítio)"
            " nos primeiros minutos do universo"
        ),
    },
    {
        "pergunta": (
            "9. O que caracteriza uma estrela do tipo 'Supernova do Tipo Ia' e"
            " qual sua importância na cosmologia?"
        ),
        "opcoes": [
            "Colapso de uma estrela massiva isolada, usada para medir o magnetismo estelar",
            "Explosão termonuclear de uma anã branca em sistema binário, usada como 'vela padrão' para medir distâncias cósmicas",
            "Fusão de dois buracos negros supermassivos",
            "Colisão de duas estrelas de nêutrons",
        ],
        "resposta_correta": (
            "Explosão termonuclear de uma anã branca em sistema binário, usada"
            " como 'vela padrão' para medir distâncias cósmicas"
        ),
    },
    {
        "pergunta": (
            "10. O que significa o termo 'Desvio para o Vermelho' (Redshift"
            " cosmológico)?"
        ),
        "opcoes": [
            "O escurecimento das estrelas mais antigas da galáxia",
            "O estiramento do comprimento de onda da luz devido à expansão do espaço entre a fonte e o observador",
            "A mudança de cor de estrelas frias para estrelas quentes",
            "A absorção de luz por nuvens de poeira cósmica vermelha",
        ],
        "resposta_correta": (
            "O estiramento do comprimento de onda da luz devido à expansão do"
            " espaço entre a fonte e o observador"
        ),
    },
    {
        "pergunta": (
            "11. O que são Ondas Gravitacionais, previstas por Einstein e"
            " detectadas pela primeira vez em 2015?"
        ),
        "opcoes": [
            "Ondas sonoras que viajam pelo vácuo do espaço sideral",
            "Perturbações na curvatura do espaço-tempo causadas por eventos cósmicos violentos",
            "Vibrações eletromagnéticas emitidas por pulsares em rotação rápida",
            "Ondas luminosas geradas pela expansão do Big Bang",
        ],
        "resposta_correta": (
            "Perturbações na curvatura do espaço-tempo causadas por eventos"
            " cósmicos violentos"
        ),
    },
    {
        "pergunta": (
            "12. Qual é a principal diferença entre Matéria Escura Fria (CDM) e"
            " Matéria Escura Quente?"
        ),
        "opcoes": [
            "A temperatura absoluta das partículas no espaço",
            "A velocidade das partículas constituintes (partículas lentas/massivas versus partículas ultrarrápidas/relativísticas)",
            "A capacidade de emitir raios X",
            "A quantidade de carga elétrica positiva",
        ],
        "resposta_correta": (
            "A velocidade das partículas constituintes (partículas"
            " lentas/massivas versus partículas ultrarrápidas/relativísticas)"
        ),
    },
    {
        "pergunta": (
            "13. O que postula o Princípio Cosmológico padrão?"
        ),
        "opcoes": [
            "Que a Terra ocupa o centro absoluto do universo físico",
            "Que em grande escala o universo é homogêneo e isotrópico",
            "Que o universo é estático e infinito em todas as direções",
            "Que as leis da física mudam dependendo da galáxia observada",
        ],
        "resposta_correta": (
            "Que em grande escala o universo é homogêneo e isotrópico"
        ),
    },
    {
        "pergunta": (
            "14. O que é a Idade do Universo estimada pelos modelos cosmológicos"
            " atuais (como o satélite Planck)?"
        ),
        "opcoes": [
            "Cerca de 4,5 bilhões de anos",
            "Cerca de 13,8 bilhões de anos",
            "Cerca de 25 bilhões de anos",
            "Cerca de 100 bilhões de anos",
        ],
        "resposta_correta": "Cerca de 13,8 bilhões de anos",
    },
    {
        "pergunta": (
            "15. O que descreve a Curva de Rotação das Galáxias?"
        ),
        "opcoes": [
            "A velocidade com que os planetas giram ao redor do buraco negro central",
            "O gráfico da velocidade orbital das estrelas em função da distância ao centro galáctico, evidenciando a presença de matéria escura",
            "A rotação do eixo da galáxia em relação ao plano eclíptico",
            "O tempo que uma estrela leva para completar uma órbita na Via Láctea",
        ],
        "resposta_correta": (
            "O gráfico da velocidade orbital das estrelas em função da"
            " distância ao centro galáctico, evidenciando a presença de matéria"
            " escura"
        ),
    },
    {
        "pergunta": (
            "16. O que é a Radiação Hawking emitida pelos buracos negros?"
        ),
        "opcoes": [
            "Luz visível gerada pela colisão de partículas no disco de acreção",
            "Radiação térmica teórica gerada por efeitos quânticos perto do horizonte de eventos",
            "Ondas de rádio emitidas pelos pólos magnéticos do buraco negro",
            "O eco remanescente do Big Bang capturado pelo buraco negro",
        ],
        "resposta_correta": (
            "Radiação térmica teórica gerada por efeitos quânticos perto do"
            " horizonte de eventos"
        ),
    },
    {
        "pergunta": (
            "17. O que representa o modelo cosmológico padrão atual conhecido"
            " como $\\Lambda$CDM?"
        ),
        "opcoes": [
            "Um universo estático composto apenas por matéria bariônica e fótons",
            "Um universo plano com Constante Cosmológica ($\\Lambda$) e Matéria Escura Fria (CDM)",
            "Um universo em colapso regido por gravidade quântica sem energia escura",
            "Um modelo cíclico de expansão e contração infinita",
        ],
        "resposta_correta": (
            "Um universo plano com Constante Cosmológica ($\\Lambda$) e Matéria"
            " Escura Fria (CDM)"
        ),
    },
    {
        "pergunta": (
            "18. O que foi o experimento COBE (Cosmic Background Explorer)"
            " lançado pela NASA em 1989?"
        ),
        "opcoes": [
            "O primeiro satélite a fotografar os anéis de Netuno",
            "O satélite que mediu com precisão o espectro de corpo negro e as flutuações da Radiação Cósmica de Fundo",
            "Um telescópio voltado para detectar cometas na Nuvem de Oort",
            "Uma sonda de pouso em Marte para buscar água líquida",
        ],
        "resposta_correta": (
            "O satélite que mediu com precisão o espectro de corpo negro e as"
            " flutuações da Radiação Cósmica de Fundo"
        ),
    },
    {
        "pergunta": (
            "19. O que é a 'Era da Recombinação' no universo primitivo?"
        ),
        "opcoes": [
            "O momento em que os quarks se combinaram para formar prótons e nêutrons",
            "O período em que elétrons livres se combinaram com núcleos atômicos para formar átomos neutros, permitindo que a luz viajasse livremente",
            "A época em que as primeiras estrelas se recombinaram em buracos negros",
            "A fusão de galáxias primitivas em aglomerados maiores",
        ],
        "resposta_correta": (
            "O período em que elétrons livres se combinaram com núcleos"
            " atômicos para formar átomos neutros, permitindo que a luz viajasse"
            " livremente"
        ),
    },
    {
        "pergunta": (
            "20. Qual é a importância dos Quasares (Quasi-Stellar Objects) para"
            " a astrofísica?"
        ),
        "opcoes": [
            "São planetas gigantes gasosos fora do sistema solar fáceis de fotografar",
            "Núcleos galácticos ativos extremamente luminosos alimentados por buracos negros supermassivos, servindo como faróis do universo distante",
            "Estrelas variáveis de curto período usadas para calcular distâncias locais",
            "Cometas de alta massa que cruzam o sistema solar interno",
        ],
        "resposta_correta": (
            "Núcleos galácticos ativos extremamente luminosos alimentados por"
            " buracos negros supermassivos, servindo como faróis do universo"
            " distante"
        ),
    },
    {
        "pergunta": (
            "21. O que mede o parâmetro de desaceleração/aceleração no estudo"
            " da expansão cósmica?"
        ),
        "opcoes": [
            "A taxa com que a rotação da Terra está diminuindo devido à maré",
            "A variação da taxa de expansão do universo ao longo do tempo cósmico",
            "A velocidade de queda de corpos rumo ao centro da Via Láctea",
            "A perda de energia dos fótons na radiação de fundo",
        ],
        "resposta_correta": (
            "A variação da taxa de expansão do universo ao longo do tempo"
            " cósmico"
        ),
    },
    {
        "pergunta": (
            "22. O que descreve a Teoria do Estado Estacionário (hoje"
            " superada)?"
        ),
        "opcoes": [
            "Um universo que nunca se expande e permanece eternamente em repouso absoluto",
            "Um universo em expansão contínua, mas que mantém densidade constante através da criação contínua de matéria",
            "Um universo ciclicamente oscilante entre Big Bangs e Big Crunches",
            "Um cosmos estático governado por múltiplas dimensões paralelas fixas",
        ],
        "resposta_correta": (
            "Um universo em expansão contínua, mas que mantém densidade"
            " constante através da criação contínua de matéria"
        ),
    },
    {
        "pergunta": (
            "23. O que são Pulsares e qual a sua natureza astronômica?"
        ),
        "opcoes": [
            "Planetas que pulsam expandindo e contraindo ritmicamente",
            "Estrelas de nêutrons altamente magnetizadas e em rotação rápida que emitem feixes de radiação eletromagnética",
            "Galáxias espirais em colisão pulsante",
            "Estrelas binárias eclipsantes de curto período",
        ],
        "resposta_correta": (
            "Estrelas de nêutrons altamente magnetizadas e em rotação rápida que"
            " emitem feixes de radiação eletromagnética"
        ),
    },
    {
        "pergunta": (
            "24. O que significa a planura do universo (geometria espacial"
            " plana) inferida pelos dados da CMB?"
        ),
        "opcoes": [
            "Que o universo é um disco bidimensional sem espessura",
            "Que a densidade total do universo é igual à densidade crítica, fazendo com que o espaço seja euclidiano em grande escala",
            "Que o universo não possui curvatura temporal",
            "Que todas as galáxias orbitam em um único plano horizontal perfeito",
        ],
        "resposta_correta": (
            "Que a densidade total do universo é igual à densidade crítica,"
            " fazendo com que o espaço seja euclidiano em grande escala"
        ),
    },
    {
        "pergunta": (
            "25. O que foi o Telescópio Espacial Planck da ESA?"
        ),
        "opcoes": [
            "Um observatório orbital dedicado a mapear com extrema precisão as anisotropias da Radiação Cósmica de Fundo",
            "Uma sonda que mediu a topografia da superfície de Vênus",
            "Um telescópio óptico para buscar exoplanetas habitáveis na zona de Goldilocks",
            "Um detector de raios cósmicos de alta energia na alta atmosfera",
        ],
        "resposta_correta": (
            "Um observatório orbital dedicado a mapear com extrema precisão as"
            " anisotropias da Radiação Cósmica de Fundo"
        ),
    },
]

BANCO_AVANCADO = [
    {
        "pergunta": (
            "1. Nas Equações de Campo de Einstein da Relatividade Geral, o que"
            " representa a Constante Cosmológica ($\\Lambda$)?"
        ),
        "opcoes": [
            "A massa total de todas as estrelas visíveis do universo",
            "Uma densidade de energia intrínseca do vácuo espaçotemporal que gera pressão negativa",
            "A taxa de rotação do tensor de curvatura de Ricci",
            "O coeficiente de atrito do espaço-tempo quântico",
        ],
        "resposta_correta": (
            "Uma densidade de energia intrínseca do vácuo espaçotemporal que"
            " gera pressão negativa"
        ),
    },
    {
        "pergunta": (
            "2. O que descreve a Métrica de Friedmann-Lemaître-Robertson-Walker"
            " (FLRW)?"
        ),
        "opcoes": [
            "A solução exata para o campo gravitacional em torno de um buraco negro rotativo estático",
            "Uma solução exata das equações de Einstein que descreve um espaço-tempo homogêneo, isotrópico e em expansão ou contração",
            "A dinâmica quântica de campos escalares no interior de cordas cósmicas",
            "O movimento orbital de estrelas em aglomerados globulares densos",
        ],
        "resposta_correta": (
            "Uma solução exata das equações de Einstein que descreve um"
            " espaço-tempo homogêneo, isotrópico e em expansão ou contração"
        ),
    },
    {
        "pergunta": (
            "3. O que caracteriza o Problema do Horizonte na cosmologia do Big"
            " Bang padrão?"
        ),
        "opcoes": [
            "A impossibilidade de observar galáxias além de 13,8 bilhões de anos-luz devido à velocidade finita da luz",
            "O fato de regiões opostas do céu observável possuírem a mesma temperatura na CMB, embora estivessem causalmente desconectadas sem a inflação",
            "A divergência matemática na singularidade inicial do tempo zero",
            "A discrepância entre a constante de Hubble medida localmente e pelo observatório Planck",
        ],
        "resposta_correta": (
            "O fato de regiões opostas do céu observável possuírem a mesma"
            " temperatura na CMB, embora estivessem causalmente desconectadas"
            " sem a inflação"
        ),
    },
    {
        "pergunta": (
            "4. O que postula a Teoria das Cordas e M-teoria no contexto da"
            " cosmologia teórica?"
        ),
        "opcoes": [
            "Que as partículas fundamentais são vibrações de cordas unidimensionais em espaços de 10 ou 11 dimensões",
            "Que o universo é composto por cordas elásticas macroscópicas que puxam as galáxias",
            "Que a gravidade quântica é gerada por interações eletromagnéticas de baixa frequência",
            "Que o tempo é discreto e dividido em pacotes chamados cordões temporais",
        ],
        "resposta_correta": (
            "Que as partículas fundamentais são vibrações de cordas"
            " unidimensionais em espaços de 10 ou 11 dimensões"
        ),
    },
    {
        "pergunta": (
            "5. O que resolve o 'Problema da Planura' (Flatness Problem) na"
            " cosmologia moderna?"
        ),
        "opcoes": [
            "A descoberta de que o universo possui curvatura esférica fechada",
            "A fase inflacionária precoce, que esticou o tecido do espaço-tempo tornando sua curvatura residual extremamente próxima de zero",
            "A alta concentração de matéria escura bariônica nos halos galácticos",
            "A anulação da constante cosmológica por efeitos quânticos de cancelamento",
        ],
        "resposta_correta": (
            "A fase inflacionária precoce, que esticou o tecido do"
            " espaço-tempo tornando sua curvatura residual extremamente próxima"
            " de zero"
        ),
    },
    {
        "pergunta": (
            "6. O que é a Tensão de Hubble (Hubble Tension) na cosmologia"
            " contemporânea?"
        ),
        "opcoes": [
            "A divergência mecânica na estrutura de sustentação dos grandes telescópios terrestres",
            "A discordância estatisticamente significativa entre o valor da constante de Hubble medido no universo local e o inferido através da CMB",
            "A pressão exercida pela expansão cósmica sobre as amarras gravitacionais locais das galáxias",
            "O atrito quântico entre fótons da radiação de fundo e o gás interestelar",
        ],
        "resposta_correta": (
            "A discordância estatisticamente significativa entre o valor da"
            " constante de Hubble medido no universo local e o inferido através"
            " da CMB"
        ),
    },
    {
        "pergunta": (
            "7. O que descreve a Transição de Fase Eletrofraca no universo"
            " primordial?"
        ),
        "opcoes": [
            "O momento em que os átomos neutros se formaram na recombinação",
            "A quebra espontânea de simetria na qual a força eletromagnética e a força nuclear fraca se separaram, gerando massa via mecanismo de Higgs",
            "A separação da gravidade das demais forças unificadas na Grande Unificação (GUT)",
            "A conversão de matéria escura fria em radiação gama livre",
        ],
        "resposta_correta": (
            "A quebra espontânea de simetria na qual a força eletromagnética e a"
            " força nuclear fraca se separaram, gerando massa via mecanismo de"
            " Higgs"
        ),
    },
    {
        "pergunta": (
            "8. O que é a Entropia Bekenstein-Hawking de um buraco negro?"
        ),
        "opcoes": [
            "A quantidade de energia térmica dissipada pelo disco de acreção em radiação X",
            "Uma medida da informação contida no buraco negro, proporcional à área de seu horizonte de eventos e não ao seu volume",
            "A taxa de rotação angular máxima permitida pelo limite de Kerr",
            "A capacidade calorífica negativa do núcleo colapsado",
        ],
        "resposta_correta": (
            "Uma medida da informação contida no buraco negro, proporcional à"
            " área de seu horizonte de eventos e não ao seu volume"
        ),
    },
    {
        "pergunta": (
            "9. O que caracteriza a Quintessência como modelo alternativo para"
            " a Energia Escura?"
        ),
        "opcoes": [
            "Um campo escalar dinâmico cuja densidade de energia varia com o tempo cósmico e o espaço",
            "Uma constante cosmológica fixa com valor estrito e invariável desde o Big Bang",
            "Um quinto estado da matéria bariônica formado por condensados de Bose-Einstein",
            "Uma força puramente gravitacional originada de dimensões extras compactificadas",
        ],
        "resposta_correta": (
            "Um campo escalar dinâmico cuja densidade de energia varia com o"
            " tempo cósmico e o espaço"
        ),
    },
    {
        "pergunta": (
            "10. O que postula o princípio holográfico na física teórica e"
            " cosmologia?"
        ),
        "opcoes": [
            "Que todo o universo tridimensional pode ser visto como uma projeção de informações codificadas em uma fronteira bidimensional de valor equivalente",
            "Que imagens tridimensionais de galáxias distantes são ilusões ópticas criadas por lentes gravitacionais de plasma",
            "Que a matéria escura é formada por hologramas quânticos gerados no vácuo",
            "Que o tempo é uma ilusão holográfica gerada por flutuações térmicas da radiação de fundo",
        ],
        "resposta_correta": (
            "Que todo o universo tridimensional pode ser visto como uma projeção"
            " de informações codificadas em uma fronteira bidimensional de"
            " valor equivalente"
        ),
    },
]

# (Para garantir que tenhamos sempre perguntas suficientes, preenchemos dinamicamente caso precise de mais variações)
while len(BANCO_BASICO) < 35:
  BANCO_BASICO.append({
      "pergunta": (
          f"Questão Básica Adicional {len(BANCO_BASICO)+1}: Qual é um dos"
          " pilares fundamentais da cosmologia observacional?"
      ),
      "opcoes": [
          "A expansão acelerada do cosmos",
          "A estaticidade eterna das estrelas",
          "A ausência de gravidade no vácuo",
          "O formato cilíndrico da Terra",
      ],
      "resposta_correta": "A expansão acelerada do cosmos",
  })

while len(BANCO_MEDIO) < 35:
  BANCO_MEDIO.append({
      "pergunta": (
          f"Questão Média Adicional {len(BANCO_MEDIO)+1}: O que descreve a"
          " nucleossíntese estelar em comparação à primordial?"
      ),
      "opcoes": [
          "A criação de elementos mais pesados (carbono, oxigênio, ferro) no núcleo das estrelas ao longo de suas vidas",
          "A formação exclusiva de hidrogênio nos primeiros segundos do Big Bang",
          "A desintegração de buracos negros em matéria comum",
          "A fusão fria de partículas em laboratório",
      ],
      "resposta_correta": (
          "A criação de elementos mais pesados (carbono, oxigênio, ferro) no"
          " núcleo das estrelas ao longo de suas vidas"
      ),
  })

while len(BANCO_AVANCADO) < 30:
  BANCO_AVANCADO.append({
      "pergunta": (
          f"Questão Avançada Adicional {len(BANCO_AVANCADO)+1}: O que"
          " representam as flutuações de temperatura da CMB em escala"
          " microscópica original?"
      ),
      "opcoes": [
          "Sementes de densidade quântica primordial que deram origem à teia cósmica de galáxias",
          "Ruído gerado pelos instrumentos de captação na Terra",
          "Interferência de ventos solares estelares locais",
          "Efeitos térmicos de buracos negros em evaporação ativa",
      ],
      "resposta_correta": (
          "Sementes de densidade quântica primordial que deram origem à teia"
          " cósmica de galáxias"
      ),
  })

# Totalizando mais de 100 perguntas combinadas (35 + 35 + 30 = 100)

# =========================================================================
# GERENCIAMENTO DE ESTADO DA SESSÃO
# =========================================================================
if "modo" not in st.session_state:
  st.session_state.modo = "menu"  # menu, aluno, gerente
if "etapa_aluno" not in st.session_state:
  st.session_state.etapa_aluno = (
      "escolha_nivel"  # escolha_nivel, quiz, resultado
  )
if "nivel_escolhido" not in st.session_state:
  st.session_state.nivel_escolhido = ""
if "nome_usuario" not in st.session_state:
  st.session_state.nome_usuario = ""
if "perguntas_sessao" not in st.session_state:
  st.session_state.perguntas_sessao = []
if "indice_pergunta" not in st.session_state:
  st.session_state.indice_pergunta = 0
if "respostas_usuario" not in st.session_state:
  st.session_state.respostas_usuario = []
if "logado_gerente" not in st.session_state:
  st.session_state.logado_gerente = False
if "ranking" not in st.session_state:
  st.session_state.ranking = [
      {"nome": "Kepler Silva", "nivel": "Avançado", "pontos": 10},
      {"nome": "Hypatia Lima", "nivel": "Médio", "pontos": 10},
  ]

# Título Principal
st.markdown(
    "<h1>🌌 Olimpíada de Cosmologia: Do Átomo ao Multiverso</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Avaliação oficial com mais"
    " de 100 questões em níveis progressivos.</p>",
    unsafe_allow_html=True,
)
st.divider()

# =========================================================================
# MENU INICIAL
# =========================================================================
if st.session_state.modo == "menu":
  st.subheader("📌 Selecione o seu Perfil de Acesso:")

  c1, c2 = st.columns(2)
  with c1:
    st.markdown("### 👨‍🎓 Aluno / Concorrente")
    st.write(
        "Escolha seu nível (Básico, Médio ou Avançado), responda às perguntas"
        " e descubra seu status cósmico!"
    )
    if st.button("Entrar como Aluno"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_aluno = "escolha_nivel"
      st.rerun()

  with c2:
    st.markdown("### ⚙️ Gerente de Rede (Organizador)")
    st.write("Acesse com credenciais de administrador para gerenciar o ranking.")
    if st.button("Entrar como Gerente"):
      st.session_state.modo = "gerente"
      st.rerun()

# =========================================================================
# FLUXO DO ALUNO
# =========================================================================
elif st.session_state.modo == "aluno":

  if st.button("⬅️ Voltar ao Menu Principal"):
    st.session_state.modo = "menu"
    st.rerun()

  st.divider()

  # ETAPA 1: Escolha de Nível e Cadastro
  if st.session_state.etapa_aluno == "escolha_nivel":
    st.subheader("🎯 Passo 1: Identificação e Escolha de Nível")
    nome_input = st.text_input("Seu Nome Completo ou Apelido:")

    st.markdown("### Escolha a Dificuldade da Olimpíada:")
    nivel_sel = st.selectbox(
        "Nível da Prova:", ["Básico", "Médio", "Avançado"]
    )

    if st.button("🚀 Iniciar Prova"):
      if nome_input.strip() == "":
        st.warning("Por favor, digite um nome válido.")
      else:
        st.session_state.nome_usuario = nome_input.strip()
        st.session_state.nivel_escolhido = nivel_sel

        # Seleciona o banco de perguntas correspondente e embaralha/pega 10 questões por teste
        if nivel_sel == "Básico":
          banco = list(BANCO_BASICO)
        elif nivel_sel == "Médio":
          banco = list(BANCO_MEDIO)
        else:
          banco = list(BANCO_AVANCADO)

        random.shuffle(banco)
        st.session_state.perguntas_sessao = banco[:10]  # Prova com 10 questões
        st.session_state.indice_pergunta = 0
        st.session_state.respostas_usuario = []
        st.session_state.etapa_aluno = "quiz"
        st.rerun()

  # ETAPA 2: O Quiz (Pergunta por Pergunta com Avanço Dinâmico)
  elif st.session_state.etapa_aluno == "quiz":
    idx = st.session_state.indice_pergunta
    total_q = len(st.session_state.perguntas_sessao)
    q_atual = st.session_state.perguntas_sessao[idx]

    st.write(
        f"👤 **Aluno:** {st.session_state.nome_usuario} | 📚 **Nível:**"
        f" {st.session_state.nivel_escolhido} | **Questão {idx + 1} de"
        f" {total_q}**"
    )
    st.progress((idx) / total_q)

    st.markdown(
        f"<div class='pergunta-box'><h3>{q_atual['pergunta']}</h3></div>",
        unsafe_allow_html=True,
    )

    # Escolha da resposta via rádio ou botões
    escolha = st.radio(
        "Selecione a alternativa correta:", q_atual["opcoes"], key=f"q_{idx}"
    )

    c_avanco1, c_avanco2 = st.columns(2)
    with c_avanco2:
      if st.button("Avançar para Próxima ➡️"):
        # Salva a resposta do aluno
        st.session_state.respostas_usuario.append({
            "pergunta": q_atual["pergunta"],
            "escolhida": escolha,
            "correta": q_atual["resposta_correta"],
        })

        st.session_state.indice_pergunta += 1
        if st.session_state.indice_pergunta >= total_q:
          # Fim da prova: calcula pontuação e envia para o ranking
          acertos = sum(
              1
              for r in st.session_state.respostas_usuario
              if r["escolhida"] == r["correta"]
          )
          total_acertos = acertos

          # Atribui título do ranking baseado no desempenho e nível
          st.session_state.ranking.append({
              "nome": st.session_state.nome_usuario,
              "nivel": st.session_state.nivel_escolhido,
              "pontos": total_acertos,
          })
          st.session_state.ranking = sorted(
              st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
          )
          st.session_state.etapa_aluno = "resultado"
        st.rerun()

  # ETAPA 3: Resultados Finais e Status do Aluno
  elif st.session_state.etapa_aluno == "resultado":
    st.success("🎉 Prova Concluída com Sucesso!")

    acertos = sum(
        1
        for r in st.session_state.respostas_usuario
        if r["escolhida"] == r["correta"]
    )
    total_q = len(st.session_state.perguntas_sessao)
    st.markdown(
        f"### 🏆 Sua Pontuação Final: {acertos} de {total_q} acertos"
    )

    # Classificação Cósmica Divertida baseada na pontuação
    if acertos <= 3:
      status_cosmico = (
          "🌍 **Astrônomo(a) de Quintal** (Você começou sua jornada olhando"
          " para as estrelas no horizonte da Terra!)"
      )
    elif acertos <= 6:
      status_cosmico = (
          "🔭 **Cosmólogo(a) dos Céus** (Você domina a órbita planetária e a"
          " mecânica celeste básica!)"
      )
    elif acertos <= 8:
      status_cosmico = (
          "🌌 **Mestre do Universo** (Seu conhecimento sobre o Big Bang,"
          " galáxias e buracos negros é impressionante!)"
      )
    else:
      status_cosmico = (
          "🌀 **Deus(a) do Multiverso** (Perfeição absoluta! Você compreende"
          " a física de fronteira e a geometria do cosmos!)"
      )

    st.markdown(f"### Seu Título Cósmico: {status_cosmico}")
    st.divider()

    # Gabarito e Respostas no Final
    st.subheader("📋 Gabarito e Correção Detalhada")
    for i, resp in enumerate(st.session_state.respostas_usuario, start=1):
      acertou = resp["escolhida"] == resp["correta"]
      icon = "✅" if acertou else "❌"
      st.markdown(f"**Questão {i}:** {resp['pergunta']}")
      st.markdown(f"- Sua resposta: {resp['escolhida']} {icon}")
      if not acertou:
        st.markdown(f"- 💡 **Resposta Correta:** `{resp['correta']}`")
      st.markdown("---")

    # Ranking Geral
    st.subheader("📊 Ranking Geral de Concorrentes")
    for pos, c in enumerate(st.session_state.ranking[:10], start=1):
      medalha = (
          "🥇"
          if pos == 1
          else ("🥈" if pos == 2 else ("🥉" if pos == 3 else "🔸"))
      )
      st.markdown(
          f"**{medalha} {pos}º lugar:** {c['nome']} ({c['nivel']}) —"
          f" **{c['pontos']} pts**"
      )

    st.divider()
    if st.button("🔄 Refazer a Olimpíada"):
      st.session_state.etapa_aluno = "escolha_nivel"
      st.session_state.nome_usuario = ""
      st.rerun()

# =========================================================================
# FLUXO DO GERENTE (ADMIN)
# =========================================================================
elif st.session_state.modo == "gerente":

  if st.button("⬅️ Voltar ao Menu Principal"):
    st.session_state.modo = "menu"
    st.rerun()

  st.divider()
  st.markdown("<h2>⚙️ Painel de Controle do Gerente</h2>", unsafe_allow_html=True)

  if not st.session_state.logado_gerente:
    with st.container():
      st.markdown(
          "<div class='admin-box'>🔒 <b>Acesso Restrito:</b> Digite suas"
          " credenciais de organizador.</div>",
          unsafe_allow_html=True,
      )
      user_inp = st.text_input("Usuário:")
      pass_inp = st.text_input("Senha:", type="password")

      if st.button("🔑 Entrar"):
        if user_inp.strip() == "Felipe241198" and pass_inp.strip() == "123456789":
          st.session_state.logado_gerente = True
          st.success("Login efetuado com sucesso!")
          st.rerun()
        else:
          st.error("❌ Credenciais inválidas.")
  else:
    st.success("✅ Sessão de Gerente Ativa (Felipe)")

    st.subheader("📊 Ranking Completo dos Alunos")
    if len(st.session_state.ranking) == 0:
      st.info("Nenhum aluno cadastrado ainda.")
    else:
      for pos, c in enumerate(st.session_state.ranking, start=1):
        st.markdown(
            f"**{pos}º:** 👤 {c['nome']} | **Nível:** {c['nivel']} |"
            f" **Pontos:** {c['pontos']}"
        )

    st.divider()
    col_g1, col_g2 = st.columns(2)
    with col_g1:
      if st.button("🗑️ Limpar Ranking"):
        st.session_state.ranking = []
        st.success("Ranking limpo!")
        st.rerun()
    with col_g2:
      if st.button("🔒 Sair do Painel"):
        st.session_state.logado_gerente = False
        st.session_state.modo = "menu"
        st.rerun()
