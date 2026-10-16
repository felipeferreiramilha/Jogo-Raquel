import streamlit as st
import random
import os
import html
from datetime import datetime

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Cavaleiros do Zodíaco - IA de Astronomia",
    page_icon="🌌",
    layout="centered"
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

.stButton>button {
    width: 100%;
    background-color: #4361ee;
    color: white;
    border-radius: 10px;
    font-weight: bold;
    border: 2px solid #4cc9f0;
    font-size: 16px;
    padding: 10px;
}

.stButton>button:hover {
    background-color: #4cc9f0;
    color: #0b132b;
}

.card-explicacao {
    background-color: #1c2541;
    padding: 25px;
    border-radius: 15px;
    border: 2px solid #4361ee;
    margin-bottom: 25px;
    box-shadow: 0 6px 12px rgba(0,0,0,0.4);
}

.titulo-crianca {
    color: #4cc9f0;
    font-size: 25px;
    font-weight: bold;
    margin-bottom: 15px;
}

.paragrafo-ia {
    color: #e2e8f0;
    font-size: 17px;
    line-height: 1.85;
    text-align: justify;
    margin-bottom: 18px;
}

.fonte-card {
    background-color: #151d36;
    padding: 12px;
    border-radius: 10px;
    margin-bottom: 10px;
    border-left: 4px solid #4cc9f0;
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
    idx = min(num_casa, len(CASAS_SANTUARIO) - 1)
    return CASAS_SANTUARIO[idx]


# ============================================================
# ESTADO DO SISTEMA
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
# BANCO DE 50 QUESTÕES
# ============================================================

if "banco_50" not in st.session_state:

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
            "O astrofísico e padre belga Georges Lemaître foi um dos pioneiros na formulação de ideias relacionadas à expansão cósmica.",
            "Georges Lemaître",
            "O que descreve o modelo do Big Bang?",
            [
                "A expansão do Universo a partir de um estado inicial extremamente quente e denso.",
                "O Universo surgiu estático e eterno.",
                "As galáxias permaneceram sempre paradas.",
                "O Universo expande-se criando matéria continuamente.",
                "A origem cósmica acontece a cada 100 anos."
            ],
            "A",
            "O modelo do Big Bang descreve a evolução do Universo a partir de um estado inicial extremamente quente e denso e sua expansão."
        ),

        (
            "Edwin Hubble analisou a luz de galáxias distantes e encontrou uma relação entre distância e velocidade de afastamento.",
            "Edwin Hubble",
            "Qual é uma das principais evidências observacionais da expansão do Universo?",
            [
                "O desvio para o vermelho observado nas galáxias distantes.",
                "A colisão de planetas.",
                "O resfriamento do Sol.",
                "A ausência completa de radiação.",
                "A rotação estática das estrelas."
            ],
            "A",
            "O redshift observado em muitas galáxias indica que elas estão se afastando e constitui uma importante evidência da expansão cósmica."
        ),

        (
            "Penzias e Wilson detectaram uma radiação de fundo proveniente de todas as direções do céu.",
            "Arno Penzias e Robert Wilson",
            "O que representa a Radiação Cósmica de Fundo?",
            [
                "Uma radiação remanescente do Universo primordial.",
                "Energia produzida por supernovas.",
                "Calor emitido apenas por buracos negros.",
                "Interferência de rádio alienígena.",
                "Luz refletida pela poeira terrestre."
            ],
            "A",
            "A Radiação Cósmica de Fundo é uma das principais evidências observacionais da história térmica do Universo."
        ),

        (
            "A relação entre distância e velocidade de afastamento das galáxias é fundamental para estudar a expansão.",
            "Edwin Hubble",
            "O que representa a constante de Hubble?",
            [
                "Uma medida relacionada à taxa atual de expansão do Universo.",
                "A velocidade de rotação da Terra.",
                "A distância até o centro da Via Láctea.",
                "A massa total do hidrogênio.",
                "A gravidade do Sol."
            ],
            "A",
            "A constante de Hubble caracteriza a taxa de expansão cósmica na época atual."
        ),

        (
            "O princípio cosmológico é utilizado para descrever o Universo em grandes escalas.",
            "Cosmologia",
            "O que significam homogeneidade e isotropia?",
            [
                "Em grandes escalas, o Universo apresenta propriedades estatisticamente semelhantes em diferentes regiões e direções.",
                "Todas as estrelas possuem exatamente a mesma massa.",
                "O Universo possui um centro fixo.",
                "Todas as galáxias têm a mesma forma.",
                "A temperatura do Universo é zero."
            ],
            "A",
            "Homogeneidade e isotropia são hipóteses fundamentais usadas nos modelos cosmológicos em grandes escalas."
        ),

        (
            "Durante o eclipse solar de 1919, observações foram utilizadas para estudar o desvio aparente da luz das estrelas próximas ao Sol.",
            "Arthur Eddington",
            "O que essas observações ajudaram a testar?",
            [
                "A previsão de que a gravidade pode desviar a trajetória da luz.",
                "A composição da Lua.",
                "A existência da matéria escura.",
                "A colisão do Sol com um buraco negro.",
                "A velocidade do som no espaço."
            ],
            "A",
            "As observações do eclipse ajudaram a testar previsões da Relatividade Geral sobre a deflexão da luz pela gravidade."
        ),

        (
            "Observatórios detectaram sinais produzidos por eventos extremamente energéticos envolvendo objetos compactos.",
            "Colaboração LIGO",
            "O que são ondas gravitacionais?",
            [
                "Perturbações que se propagam no espaço-tempo produzidas por movimentos acelerados de massas, como fusões de buracos negros.",
                "Ondas sonoras no vácuo.",
                "Ondas de rádio comuns.",
                "Raios cósmicos.",
                "Marés lunares."
            ],
            "A",
            "Ondas gravitacionais são perturbações que se propagam pelo espaço-tempo."
        ),

        (
            "Vera Rubin estudou curvas de rotação de galáxias espirais.",
            "Vera Rubin",
            "Por que as curvas de rotação são importantes para o estudo da matéria escura?",
            [
                "Porque indicam a presença de massa gravitacional que não é explicada apenas pela matéria luminosa observada.",
                "Porque mostram que as galáxias estão paradas.",
                "Porque provam que não existe gravidade.",
                "Porque medem diretamente a energia escura.",
                "Porque mostram que todas as estrelas possuem a mesma massa."
            ],
            "A",
            "As curvas de rotação fornecem evidências de uma quantidade adicional de massa gravitacional além da matéria visível."
        ),

        (
            "A cosmologia moderna distingue diferentes componentes do conteúdo energético do Universo.",
            "Cosmologia Moderna",
            "Qual é uma diferença geral entre matéria escura e energia escura?",
            [
                "A matéria escura está associada a efeitos gravitacionais atrativos, enquanto a energia escura está associada à aceleração da expansão cósmica.",
                "As duas são exatamente a mesma coisa.",
                "A energia escura é uma estrela.",
                "A matéria escura produz toda a luz do Universo.",
                "Nenhuma das duas possui relação com cosmologia."
            ],
            "A",
            "Matéria escura e energia escura são conceitos diferentes utilizados para explicar fenômenos cosmológicos distintos."
        ),

        (
            "Supernovas do tipo Ia foram utilizadas para estudar a expansão cósmica.",
            "Saul Perlmutter e outros pesquisadores",
            "O que as observações de supernovas distantes ajudaram a revelar?",
            [
                "Que a expansão do Universo está acelerando.",
                "Que a Terra está no centro do Universo.",
                "Que a Lua está se afastando do Sol.",
                "Que o Sol está esfriando rapidamente.",
                "Que todas as galáxias possuem a mesma massa."
            ],
            "A",
            "As observações de supernovas do tipo Ia contribuíram para a descoberta da expansão acelerada do Universo."
        ),

        (
            "A analogia de uma superfície elástica sendo expandida é usada em algumas explicações introdutórias.",
            "Didática da Cosmologia",
            "O que essa analogia pode representar?",
            [
                "O afastamento relativo entre pontos devido à expansão da própria superfície.",
                "A existência de um centro obrigatório do Universo.",
                "A criação de ar no espaço.",
                "A existência de paredes no Universo.",
                "A velocidade do som no espaço."
            ],
            "A",
            "A analogia ajuda a visualizar como distâncias entre pontos podem aumentar quando a própria superfície se expande."
        ),

        (
            "No Universo primordial, matéria e radiação estavam em condições muito diferentes das atuais.",
            "Cosmologia",
            "O que ocorreu durante a recombinação?",
            [
                "Elétrons e núcleos puderam formar átomos neutros, permitindo que a radiação viajasse mais livremente.",
                "Todas as galáxias desapareceram.",
                "A gravidade deixou de existir.",
                "O Universo tornou-se completamente vazio.",
                "Todas as estrelas atuais nasceram naquele momento."
            ],
            "A",
            "A formação de átomos neutros reduziu a interação entre matéria e radiação e permitiu que a luz se propagasse mais livremente."
        ),

        (
            "Buracos negros possuem uma região associada a um limite causal.",
            "Karl Schwarzschild",
            "O que é o horizonte de eventos?",
            [
                "Uma fronteira além da qual não é possível enviar sinais de volta para um observador distante.",
                "A superfície sólida de um planeta.",
                "A borda da Via Láctea.",
                "A região onde as estrelas nascem.",
                "O limite do Sistema Solar."
            ],
            "A",
            "O horizonte de eventos é uma fronteira característica de um buraco negro."
        ),

        (
            "Alan Guth desenvolveu uma importante proposta para a cosmologia primordial.",
            "Alan Guth",
            "O que é a inflação cósmica?",
            [
                "Uma fase hipotética de expansão extremamente rápida do Universo primordial.",
                "A expansão das estrelas individuais.",
                "O aumento da massa dos planetas.",
                "A explosão de todas as galáxias.",
                "O crescimento dos buracos negros atuais."
            ],
            "A",
            "A inflação é uma hipótese de expansão extremamente rápida do Universo em seus primeiros instantes."
        ),

        (
            "A luz proveniente de objetos distantes pode apresentar deslocamento para comprimentos de onda maiores.",
            "Christian Doppler / Cosmologia",
            "O que é redshift cosmológico?",
            [
                "O deslocamento da luz para comprimentos de onda maiores associado à expansão do Universo.",
                "O desaparecimento da luz.",
                "A transformação da luz em som.",
                "O aumento da massa da estrela.",
                "A mudança da cor causada apenas pela atmosfera terrestre."
            ],
            "A",
            "O redshift cosmológico está relacionado à expansão do espaço ao longo da viagem da luz."
        ),

        (
            "Albert Einstein desenvolveu a Relatividade Geral.",
            "Albert Einstein",
            "Como a Relatividade Geral descreve a gravidade?",
            [
                "Como um efeito associado à geometria do espaço-tempo determinada pela matéria e energia.",
                "Como uma força magnética.",
                "Como atrito entre planetas.",
                "Como uma onda sonora.",
                "Como uma propriedade exclusiva da Terra."
            ],
            "A",
            "Na Relatividade Geral, a gravidade está relacionada à geometria do espaço-tempo."
        ),

        (
            "A Relatividade prevê que relógios podem apresentar ritmos diferentes dependendo das condições gravitacionais e de movimento.",
            "Albert Einstein",
            "O que é dilatação gravitacional do tempo?",
            [
                "Uma diferença na passagem do tempo entre regiões submetidas a diferentes potenciais gravitacionais.",
                "O desaparecimento do tempo.",
                "O retorno do tempo ao passado.",
                "A paralisação completa do Universo.",
                "A criação de uma nova dimensão."
            ],
            "A",
            "A gravidade pode produzir diferenças mensuráveis na passagem do tempo."
        ),

        (
            "Sistemas de navegação por satélite precisam considerar efeitos relativísticos.",
            "Física Relativística",
            "Por que sistemas como o GPS precisam de correções relativísticas?",
            [
                "Porque movimento e diferenças gravitacionais afetam o funcionamento dos relógios dos satélites.",
                "Porque os satélites não possuem relógios.",
                "Porque a luz não viaja no espaço.",
                "Porque a Terra não possui gravidade.",
                "Porque os satélites estão parados."
            ],
            "A",
            "Efeitos relativísticos alteram a taxa dos relógios e precisam ser considerados para manter a precisão do sistema."
        ),

        (
            "A nucleossíntese primordial ocorreu no Universo muito jovem.",
            "Cosmologia",
            "Quais elementos leves foram produzidos em grande quantidade no Universo primordial?",
            [
                "Hidrogênio e hélio.",
                "Ouro e platina.",
                "Urânio e plutônio.",
                "Ferro e níquel.",
                "Silício e titânio."
            ],
            "A",
            "A nucleossíntese primordial produziu principalmente hidrogênio, hélio e pequenas quantidades de outros núcleos leves."
        ),

        (
            "Medições cosmológicas permitiram estimar a composição do Universo.",
            "Missões cosmológicas",
            "Qual é aproximadamente a fração de matéria ordinária no modelo cosmológico padrão?",
            [
                "Cerca de 5%.",
                "Cerca de 50%.",
                "Cerca de 70%.",
                "Cerca de 90%.",
                "100%."
            ],
            "A",
            "A matéria ordinária corresponde a uma pequena fração do conteúdo energético total do Universo."
        ),

        (
            "Observações da radiação cósmica de fundo ajudam a estimar parâmetros cosmológicos.",
            "Cosmologia Observacional",
            "Qual é a idade aproximada do Universo segundo o modelo cosmológico atualmente aceito?",
            [
                "Cerca de 13,8 bilhões de anos.",
                "4,5 bilhões de anos.",
                "6 mil anos.",
                "500 milhões de anos.",
                "100 bilhões de anos."
            ],
            "A",
            "As observações cosmológicas indicam uma idade de aproximadamente 13,8 bilhões de anos."
        ),

        (
            "Edwin Hubble observou relações entre distância e velocidade de afastamento de galáxias.",
            "Edwin Hubble",
            "O que essas observações ajudaram a estabelecer?",
            [
                "Que o Universo está em expansão.",
                "Que a Terra é o centro do Universo.",
                "Que as galáxias não possuem movimento.",
                "Que a Via Láctea é o Universo inteiro.",
                "Que a gravidade não existe."
            ],
            "A",
            "As observações contribuíram decisivamente para o estabelecimento observacional da expansão cósmica."
        ),

        (
            "Einstein formulou um princípio fundamental da Relatividade Geral.",
            "Albert Einstein",
            "O que afirma o princípio da equivalência?",
            [
                "Em determinadas condições locais, efeitos gravitacionais podem ser indistinguíveis de efeitos de uma aceleração.",
                "Toda matéria possui a mesma massa.",
                "A velocidade da luz muda livremente.",
                "A gravidade existe somente na Terra.",
                "Massa e energia são independentes."
            ],
            "A",
            "O princípio da equivalência relaciona localmente efeitos gravitacionais e aceleração."
        ),

        (
            "Hermann Minkowski desenvolveu uma formulação geométrica da Relatividade Especial.",
            "Hermann Minkowski",
            "O que é o espaço-tempo?",
            [
                "Uma estrutura matemática que combina três dimensões espaciais com uma dimensão temporal.",
                "Uma quarta dimensão espacial comum.",
                "Uma região dentro de um buraco negro.",
                "Uma galáxia.",
                "Um tipo de matéria."
            ],
            "A",
            "O espaço-tempo reúne matematicamente as dimensões espaciais e temporal."
        ),

        (
            "A famosa relação E=mc² conecta massa e energia.",
            "Albert Einstein",
            "O que essa relação expressa?",
            [
                "A equivalência entre massa e energia.",
                "A velocidade de uma galáxia.",
                "A massa da Terra.",
                "A energia da Lua.",
                "A distância entre estrelas."
            ],
            "A",
            "A relação mostra que massa e energia são grandezas relacionadas."
        ),

        (
            "Estrelas de nêutrons são objetos extremamente compactos.",
            "Astrofísica",
            "O que caracteriza uma estrela de nêutrons?",
            [
                "Um objeto extremamente denso formado principalmente por matéria nuclear.",
                "Um planeta gasoso.",
                "Uma galáxia pequena.",
                "Uma estrela comum de hidrogênio.",
                "Uma nuvem de poeira."
            ],
            "A",
            "Estrelas de nêutrons são remanescentes extremamente densos de determinadas estrelas massivas."
        ),

        (
            "A velocidade da luz possui papel central na Relatividade.",
            "Albert Einstein",
            "Qual é a velocidade aproximada da luz no vácuo?",
            [
                "3 × 10^8 m/s.",
                "3 × 10^4 m/s.",
                "3 × 10^2 m/s.",
                "300 m/s.",
                "3 × 10^10 km/s."
            ],
            "A",
            "A velocidade da luz no vácuo é aproximadamente 300 mil quilômetros por segundo."
        ),

        (
            "WIMPs foram propostos como possíveis candidatos à matéria escura.",
            "Física de Partículas",
            "O que significa WIMP?",
            [
                "Weakly Interacting Massive Particle.",
                "Wide Infrared Magnetic Photon.",
                "Weak Internal Matter Process.",
                "World Interstellar Matter Particle.",
                "Wave Interaction Mass Photon."
            ],
            "A",
            "WIMP significa partícula massiva de interação fraca e corresponde a uma classe histórica de candidatos à matéria escura."
        ),

        (
            "Massas muito grandes podem alterar a trajetória da luz.",
            "Relatividade Geral",
            "O que é lente gravitacional?",
            [
                "O desvio e, em alguns casos, a amplificação aparente da luz devido à gravidade de objetos massivos.",
                "Uma lente feita de vidro no espaço.",
                "Uma câmera de telescópio.",
                "Um fenômeno exclusivamente atmosférico.",
                "Uma estrela que emite lentes."
            ],
            "A",
            "A gravidade de estruturas massivas pode desviar a luz e produzir efeitos de lente gravitacional."
        ),

        (
            "Algumas soluções matemáticas da Relatividade Geral apresentam estruturas conhecidas como pontes de Einstein-Rosen.",
            "Relatividade Geral",
            "O que é um buraco de minhoca?",
            [
                "Uma estrutura hipotética que poderia conectar diferentes regiões do espaço-tempo.",
                "Um tipo de planeta.",
                "Uma estrela de nêutrons.",
                "Uma galáxia.",
                "Um cometa."
            ],
            "A",
            "Buracos de minhoca são estruturas hipotéticas estudadas matematicamente na gravitação."
        ),

        (
            "Pulsares são objetos compactos observados em Astronomia.",
            "Jocelyn Bell Burnell",
            "O que é um pulsar?",
            [
                "Uma estrela de nêutrons em rotação que produz sinais periódicos de radiação.",
                "Um planeta que pisca.",
                "Uma galáxia jovem.",
                "Um cometa.",
                "Uma nuvem molecular."
            ],
            "A",
            "Pulsares são estrelas de nêutrons magnetizadas em rotação que podem produzir sinais periódicos."
        ),

        (
            "A constante cosmológica aparece nas equações da Relatividade Geral.",
            "Albert Einstein",
            "Com o que a constante cosmológica está relacionada na cosmologia moderna?",
            [
                "Com um termo associado à dinâmica de expansão do Universo e frequentemente interpretado no modelo padrão como energia escura.",
                "Com a massa da Lua.",
                "Com a velocidade do som.",
                "Com o campo magnético terrestre.",
                "Com a idade do Sol."
            ],
            "A",
            "A constante cosmológica desempenha papel importante nos modelos atuais de expansão acelerada."
        ),

        (
            "A matéria do Universo forma estruturas em grandes escalas.",
            "Cosmologia",
            "O que são filamentos cósmicos?",
            [
                "Estruturas alongadas que fazem parte da grande teia cósmica.",
                "Ondas sonoras.",
                "Órbitas planetárias.",
                "Raios solares.",
                "Tipos de estrelas."
            ],
            "A",
            "Filamentos são estruturas de grande escala que conectam regiões densas da teia cósmica."
        ),

        (
            "Existem regiões gigantescas com poucas galáxias.",
            "Cosmologia Observacional",
            "O que são vazios cósmicos?",
            [
                "Grandes regiões do Universo com densidade de matéria relativamente baixa.",
                "Buracos negros gigantes.",
                "Regiões sem espaço.",
                "Partes do Sol.",
                "Regiões dentro da Terra."
            ],
            "A",
            "Vazios cósmicos são regiões de baixa densidade que fazem parte da estrutura em grande escala do Universo."
        ),

        (
            "Axions são partículas hipotéticas estudadas em Física de Partículas.",
            "Física de Partículas",
            "Por que axions são estudados em cosmologia?",
            [
                "Porque podem constituir candidatos à matéria escura.",
                "Porque são estrelas.",
                "Porque são galáxias.",
                "Porque são planetas.",
                "Porque produzem toda a luz do Universo."
            ],
            "A",
            "Axions estão entre as partículas hipotéticas estudadas como possíveis componentes da matéria escura."
        ),

        (
            "Simulações numéricas são utilizadas para investigar a formação de estruturas.",
            "Cosmologia Computacional",
            "Para que servem simulações de N-corpos?",
            [
                "Para estudar numericamente a evolução gravitacional de grandes conjuntos de partículas.",
                "Para calcular apenas a temperatura da Terra.",
                "Para observar diretamente buracos negros.",
                "Para produzir estrelas reais.",
                "Para criar galáxias no laboratório."
            ],
            "A",
            "Simulações de N-corpos permitem estudar numericamente sistemas gravitacionais com muitas partículas."
        ),

        (
            "A expansão acelerada possui consequências para o futuro cosmológico.",
            "Cosmologia",
            "Qual cenário é frequentemente associado ao futuro de um Universo dominado por energia escura?",
            [
                "Expansão continuada, com um Universo progressivamente mais frio e diluído.",
                "Colapso imediato.",
                "Explosão do Sol.",
                "Desaparecimento da gravidade.",
                "Paralisação do tempo."
            ],
            "A",
            "No cenário padrão com energia escura dominante, a expansão continua e o Universo tende a ficar mais frio e diluído."
        ),

        (
            "O satélite Planck realizou observações da radiação cósmica de fundo.",
            "ESA",
            "Qual foi uma das principais contribuições da missão Planck?",
            [
                "Medir com grande precisão as anisotropias da radiação cósmica de fundo.",
                "Levar astronautas a Marte.",
                "Estudar somente o Sol.",
                "Mapear apenas a Lua.",
                "Detectar diretamente matéria escura."
            ],
            "A",
            "Planck produziu medições extremamente precisas da radiação cósmica de fundo."
        ),

        (
            "A matéria escura é uma hipótese central para explicar diversos efeitos gravitacionais.",
            "Cosmologia",
            "Por que a matéria escura é chamada de escura?",
            [
                "Porque não observamos uma interação eletromagnética significativa que permita detectá-la diretamente pela luz.",
                "Porque possui cor preta.",
                "Porque está sempre à noite.",
                "Porque absorve toda a luz da Terra.",
                "Porque existe somente dentro de buracos negros."
            ],
            "A",
            "O termo escura está relacionado à ausência de uma detecção eletromagnética direta conhecida."
        ),

        (
            "A chamada tensão de Hubble envolve diferentes métodos de estimar a taxa de expansão atual.",
            "Cosmologia Moderna",
            "O que é a tensão de Hubble?",
            [
                "Uma diferença significativa entre determinadas estimativas da taxa atual de expansão obtidas por métodos diferentes.",
                "Uma força gravitacional.",
                "Uma onda gravitacional.",
                "Uma explosão de uma estrela.",
                "Um novo planeta."
            ],
            "A",
            "A tensão de Hubble refere-se à diferença entre algumas determinações independentes da expansão atual."
        ),

        (
            "As curvas de rotação das galáxias apresentam comportamento que não é explicado somente pela matéria visível.",
            "Vera Rubin e colaboradores",
            "O que essas observações sugerem?",
            [
                "A existência de uma quantidade adicional de massa gravitacional não luminosa.",
                "Que as galáxias não giram.",
                "Que a gravidade não existe.",
                "Que as estrelas não possuem massa.",
                "Que todas as galáxias são iguais."
            ],
            "A",
            "As curvas de rotação constituem uma das linhas de evidência para a matéria escura."
        ),

        (
            "A matéria escura participa da formação de estruturas em grande escala.",
            "Cosmologia",
            "Qual é uma função importante atribuída à matéria escura?",
            [
                "Fornecer uma contribuição gravitacional importante para a formação e evolução das estruturas cósmicas.",
                "Produzir a maior parte da luz das estrelas.",
                "Acelerar diretamente todos os planetas.",
                "Aquecer o Sol.",
                "Criar oxigênio na Terra."
            ],
            "A",
            "A gravidade associada à matéria escura é importante nos modelos de formação de estruturas."
        ),

        (
            "O espaço-tempo é uma parte essencial da descrição relativística do Universo.",
            "Albert Einstein",
            "O que significa dizer que o espaço-tempo é dinâmico?",
            [
                "Que sua geometria pode mudar de acordo com a distribuição de matéria e energia e pela evolução cosmológica.",
                "Que o espaço possui vento.",
                "Que as estrelas controlam o tempo.",
                "Que o espaço é uma substância comum.",
                "Que o tempo não existe."
            ],
            "A",
            "Na Relatividade Geral, a geometria do espaço-tempo participa dinamicamente da descrição gravitacional."
        ),

        (
            "O horizonte de eventos está relacionado à estrutura causal de um buraco negro.",
            "Karl Schwarzschild",
            "Por que não podemos receber luz emitida de dentro do horizonte de eventos?",
            [
                "Porque, dentro dessa região, as trajetórias futuras possíveis não permitem que um sinal alcance um observador externo.",
                "Porque a luz deixa de existir.",
                "Porque a luz fica pesada.",
                "Porque o espaço vira sólido.",
                "Porque o buraco negro apaga a luz."
            ],
            "A",
            "A estrutura causal do horizonte impede que sinais enviados de dentro alcancem o exterior."
        ),

        (
            "A inflação foi proposta para explicar algumas características do Universo primordial.",
            "Alan Guth",
            "Qual problema cosmológico a inflação ajuda a abordar?",
            [
                "O problema do horizonte e a elevada uniformidade observada em grandes escalas.",
                "A existência da Lua.",
                "A formação dos planetas.",
                "As marés terrestres.",
                "A temperatura do Sol."
            ],
            "A",
            "A inflação fornece uma explicação para a grande uniformidade observada em regiões que parecem ter estado causalmente separadas em modelos simples."
        ),

        (
            "A cosmologia procura estudar o Universo em suas maiores escalas.",
            "Georges Lemaître",
            "Qual é o objetivo geral da cosmologia?",
            [
                "Investigar a origem, evolução, estrutura e dinâmica do Universo.",
                "Estudar somente o clima da Terra.",
                "Estudar apenas os planetas.",
                "Estudar somente estrelas próximas.",
                "Estudar apenas buracos negros."
            ],
            "A",
            "A cosmologia estuda o Universo como um todo e procura compreender sua origem, evolução e estrutura."
        )

    ]

    lista_50 = []

    for i, q in enumerate(dados_brutos):

        guia = guias[i % len(guias)]

        lista_50.append({
            "guia": guia,
            "texto_base": q[0],
            "cientista": q[1],
            "enunciado": q[2],
            "opcoes_originais": q[3],
            "correta_texto": q[3][ord(q[4]) - ord("A")],
            "por_que": q[5]
        })

    st.session_state.banco_50 = lista_50


# ============================================================
# FUNÇÃO PARA REINICIAR JOGO
# ============================================================

def reiniciar_jogo():

    st.session_state.jogo_iniciado = False
    st.session_state.indice_pergunta = 0
    st.session_state.equipe_sub_idx = 0
    st.session_state.casas_alfa = 0
    st.session_state.casas_beta = 0
    st.session_state.casas_gama = 0
    st.session_state.ultimo_feedback = None


# ============================================================
# IA DE ASTRONOMIA
# ============================================================

def obter_api_key():

    try:

        if "OPENAI_API_KEY" in st.secrets:
            return st.secrets["OPENAI_API_KEY"]

    except Exception:
        pass

    return os.environ.get("OPENAI_API_KEY", "")


def pesquisar_e_explicar_com_ia(pergunta):

    """
    A IA pesquisa a pergunta diretamente na web usando
    a ferramenta de pesquisa da OpenAI e depois produz
    uma explicação entre 5 e 12 parágrafos.
    """

    api_key = obter_api_key()

    if not api_key:

        return {
            "sucesso": False,
            "erro": "A chave OPENAI_API_KEY não foi encontrada.",
            "resposta": None,
            "fontes": []
        }

    try:

        from openai import OpenAI

        cliente = OpenAI(api_key=api_key)

        instrucoes = """
Você é uma IA especializada em Astronomia, Astrofísica,
Cosmologia e Ensino de Física.

Sua função é responder perguntas de estudantes.

O estudante pode fazer QUALQUER pergunta relacionada
à Astronomia.

Você deve pesquisar a pergunta antes de responder.

A resposta final precisa ser uma explicação científica
verdadeira, clara, pedagógica e profunda.

REGRAS OBRIGATÓRIAS DA RESPOSTA:

1. Escreva ENTRE 5 E 12 PARÁGRAFOS.

2. Os parágrafos precisam ser desenvolvidos.
Não escreva frases isoladas.

3. Cada parágrafo deve acrescentar uma informação
nova ou aprofundar a explicação.

4. Não responda apenas com uma definição.

5. Não escreva uma resposta extremamente curta.

6. Não transforme toda a resposta em uma lista.

7. Explique primeiro a ideia principal.

8. Depois desenvolva o conceito científico.

9. Explique como o fenômeno acontece.

10. Apresente exemplos quando forem úteis.

11. Quando houver Física ou Matemática importante,
explique o significado físico das grandezas e das
equações utilizadas.

12. Relacione a explicação com observações astronômicas
reais quando isso for pertinente.

13. Diferencie fatos observacionais, modelos científicos,
hipóteses e especulações.

14. Não invente cientistas, instituições, descobertas,
experimentos ou dados.

15. Se houver controvérsia científica, explique que existe
uma controvérsia.

16. Use linguagem adequada para estudantes.

17. Não infantilize excessivamente a explicação.

18. Evite palavras desnecessariamente difíceis, mas
explique os termos técnicos importantes.

19. Não diga que você é uma inteligência artificial.

20. Não comece dizendo "Claro!" ou "Com certeza!".

21. Comece diretamente respondendo à pergunta.

22. Termine com uma conclusão que retome a pergunta.

ESTRUTURA SUGERIDA:

Parágrafo 1:
Resposta direta à pergunta e apresentação do fenômeno.

Parágrafo 2:
Explicação do conceito científico fundamental.

Parágrafo 3:
Aprofundamento físico ou astronômico.

Parágrafo 4:
Explicação de como o fenômeno ocorre.

Parágrafo 5:
Exemplo ou situação concreta.

Parágrafo 6:
Observações e evidências científicas.

Parágrafo 7:
O que os cientistas sabem atualmente.

Parágrafo 8:
Consequências ou relações com outros fenômenos.

Parágrafo 9:
Conclusão.

Você pode usar entre 5 e 12 parágrafos dependendo
da complexidade da pergunta.

NÃO coloque títulos como "Parágrafo 1".
NÃO numere os parágrafos.
Escreva como um texto contínuo e bem elaborado.
"""

        resposta = cliente.responses.create(

            model="gpt-6-luna",

            tools=[
                {
                    "type": "web_search"
                }
            ],

            instructions=instrucoes,

            input=pergunta,

            max_output_tokens=6000
        )

        texto = getattr(resposta, "output_text", None)

        if not texto:

            return {
                "sucesso": False,
                "erro": "A IA não retornou texto.",
                "resposta": None,
                "fontes": []
            }

        # ====================================================
        # O SDK pode devolver referências de pesquisa dentro
        # da resposta. Aqui tentamos extrair URLs quando elas
        # estiverem disponíveis.
        # ====================================================

        fontes = []

        try:

            for item in resposta.output:

                if hasattr(item, "content"):

                    for conteudo in item.content:

                        if hasattr(conteudo, "annotations"):

                            for anotacao in conteudo.annotations:

                                url = getattr(
                                    anotacao,
                                    "url",
                                    None
                                )

                                titulo = getattr(
                                    anotacao,
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

        # Remover duplicatas

        fontes_unicas = []

        urls_vistas = set()

        for fonte in fontes:

            if fonte["url"] not in urls_vistas:

                urls_vistas.add(fonte["url"])
                fontes_unicas.append(fonte)

        return {
            "sucesso": True,
            "erro": None,
            "resposta": texto,
            "fontes": fontes_unicas
        }

    except Exception as erro:

        return {
            "sucesso": False,
            "erro": str(erro),
            "resposta": None,
            "fontes": []
        }


# ============================================================
# FALLBACK
# ============================================================

def resposta_fallback(pergunta):

    return f"""
A pergunta apresentada foi: "{pergunta}".

Para responder essa questão com segurança científica, é
necessário consultar fontes astronômicas confiáveis e
analisar as informações encontradas antes de elaborar a
explicação. O sistema de pesquisa da aplicação não
conseguiu acessar a IA neste momento.

Quando a conexão com a API estiver funcionando, a resposta
será construída especificamente para essa pergunta, em vez
de utilizar um texto pronto baseado apenas em palavras-chave.

A explicação será organizada de maneira progressiva,
começando pelo conceito principal e depois desenvolvendo
os mecanismos físicos envolvidos. Também serão utilizados
exemplos para facilitar a compreensão do fenômeno.

Quando houver observações astronômicas relacionadas ao
assunto, elas serão apresentadas para mostrar como os
cientistas obtêm evidências sobre o fenômeno estudado.

A resposta também deverá diferenciar aquilo que é
observação científica, aquilo que é resultado de modelos
teóricos e aquilo que ainda permanece como hipótese ou
questão em investigação.

Assim, a proposta da ferramenta é transformar uma pergunta
do estudante em uma pequena explicação de Astronomia,
fundamentada em pesquisa e apresentada em linguagem
adequada para o aprendizado.
"""


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.header("🧭 Painel de Controle")

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
st.sidebar.header("👨‍🏫 Área do Professor / Admin")

with st.sidebar.expander("🔑 Acesso Restrito"):

    if not st.session_state.prof_logado:

        login_input = st.text_input(
            "Login",
            key="login_professor"
        )

        senha_input = st.text_input(
            "Senha",
            type="password",
            key="senha_professor"
        )

        if st.button("Entrar"):

            # Para maior segurança, você pode posteriormente
            # colocar essas credenciais nos Secrets.

            login_correto = st.secrets.get(
                "PROFESSOR_LOGIN",
                "Felipe Ferreira"
            )

            senha_correta = st.secrets.get(
                "PROFESSOR_SENHA",
                "Ff241198"
            )

            if (
                login_input == login_correto
                and senha_input == senha_correta
            ):

                st.session_state.prof_logado = True

                st.success(
                    "Logado com sucesso!"
                )

                st.rerun()

            else:

                st.error(
                    "Credenciais inválidas."
                )

    else:

        st.success(
            "Sessão ativa: Professor"
        )

        if st.button("Sair"):

            st.session_state.prof_logado = False

            st.rerun()


# ============================================================
# RELATÓRIO DO PROFESSOR
# ============================================================

if st.session_state.prof_logado:

    st.sidebar.markdown(
        "### 📄 Exportar Relatório"
    )

    relatorio_txt = ""

    relatorio_txt += (
        "====================================================\n"
    )

    relatorio_txt += (
        "RELATÓRIO - CAVALEIROS DO ZODÍACO / ASTRONOMIA\n"
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
                f"Equipe: {item['equipe']}\n"
            )

            relatorio_txt += (
                f"Casa: {item['casa_santuario']}\n"
            )

            relatorio_txt += (
                f"Guia: {item['guia']}\n"
            )

            relatorio_txt += (
                f"Cientista/Referência: "
                f"{item['cientista']}\n"
            )

            relatorio_txt += (
                f"Pergunta: {item['enunciado']}\n"
            )

            relatorio_txt += (
                f"Resposta: {item['resposta']}\n"
            )

            relatorio_txt += (
                f"Status: {item['status']}\n"
            )

            relatorio_txt += (
                f"Justificativa: {item['por_que']}\n"
            )

            relatorio_txt += (
                "----------------------------------------------------\n"
            )

    else:

        relatorio_txt += (
            "Nenhum registro do jogo até o momento.\n"
        )

    st.sidebar.download_button(
        "📥 Baixar Relatório (.txt)",
        data=relatorio_txt,
        file_name="relatorio_desempenho.txt",
        mime="text/plain"
    )

    if st.sidebar.button(
        "🗑️ Limpar Relatório"
    ):

        st.session_state.historico_professor = []

        st.sidebar.success(
            "Relatório limpo!"
        )

        st.rerun()


# ============================================================
# MODO 1 - JOGO
# ============================================================

if (
    st.session_state.modo_sistema
    == "⚔️ Jogo: Cavaleiros do Zodíaco"
):

    st.title(
        "🏛️ Cavaleiros do Zodíaco: O Despertar da Física"
    )

    st.markdown(
        "### *Treinamento das Equipes: "
        "Domine o Cosmo, a Física e a Astronomia!*"
    )

    st.markdown("---")

    # --------------------------------------------------------
    # PLACAR
    # --------------------------------------------------------

    st.sidebar.markdown("---")

    st.sidebar.header(
        "📊 Posição no Santuário"
    )

    for nome_eq, casas_eq in [

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

    ]:

        c_str = obter_nome_casa(
            casas_eq
        )

        st.sidebar.markdown(
            f"🛡️ **{nome_eq}**\n"
            f"*📍 {c_str}*"
        )

        st.sidebar.progress(
            min(1.0, casas_eq / 12)
        )

        st.sidebar.markdown("---")

    if st.sidebar.button(
        "🔄 Reiniciar Partida do Jogo"
    ):

        reiniciar_jogo()

        st.rerun()

    # --------------------------------------------------------
    # ABERTURA
    # --------------------------------------------------------

    if not st.session_state.jogo_iniciado:

        st.subheader(
            "🔥 Cerimônia de Abertura: "
            "O Despertar do Cosmo"
        )

        st.markdown("""
        > Aspirantes reúnem-se no sopé do Santuário.
        > Para se tornarem verdadeiros Cavaleiros de Athena,
        > vocês deverão atravessar as 12 Casas do Santuário
        > utilizando conhecimento científico.
        >
        > **Regras:**
        >
        > 🟢 Acerto: avança 1 Casa.
        >
        > 🔴 Erro: não perde Casa e a vez passa para a próxima equipe.
        >
        > 🏆 Vitória: a primeira equipe a atravessar as 12 Casas vence.
        """)

        if st.button(
            "🌟 Iniciar Treinamento do Santuário"
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
                f"🥇 **{vencedor} atravessou "
                f"as 12 Casas do Santuário!**"
            )

        else:

            st.success(
                "Fim das questões do Santuário!"
            )

        if st.button(
            "🔄 Iniciar Novo Treinamento"
        ):

            reiniciar_jogo()

            st.rerun()

        st.stop()

    # --------------------------------------------------------
    # QUESTÃO
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

    equipe_da_vez = lista_equipes[e_idx]

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

        letras = [
            "A",
            "B",
            "C",
            "D",
            "E"
        ]

        opcoes_rotuladas = [
            f"{letras[i]}) {texto}"
            for i, texto
            in enumerate(opcoes_copia)
        ]

        st.session_state[
            chave_opcoes
        ] = opcoes_rotuladas

    st.warning(
        f"📍 **{equipe_da_vez} encontra-se em:** "
        f"{casa_str}"
    )

    st.subheader(
        f"⚔️ Vez da: **{equipe_da_vez}**"
    )

    st.markdown(
        f"**Guia da Casa:** "
        f"*{q_atual['guia']}* ✨"
    )

    st.markdown("---")

    st.info(
        f"📜 **História da Ciência:**\n\n"
        f"{q_atual['texto_base']}\n\n"
        f"🔬 **Referência:** "
        f"*{q_atual['cientista']}*"
    )

    st.markdown(
        f"### **Enigma Cosmológico:**\n"
        f"{q_atual['enunciado']}"
    )

    escolha_usuario = st.radio(
        "Selecione a alternativa:",
        st.session_state[chave_opcoes],
        key=f"radio_{idx_p}_{e_idx}"
    )

    if st.button(
        "Enviar Resposta e Elevar o Cosmo"
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

        st.session_state.indice_pergunta += 1

        st.session_state.equipe_sub_idx = (
            e_idx + 1
        ) % 3

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

            "correta_texto": q_atual["correta_texto"],

            "por_que": q_atual["por_que"]

        }

        st.rerun()

    # --------------------------------------------------------
    # FEEDBACK
    # --------------------------------------------------------

    if st.session_state.ultimo_feedback:

        st.markdown("---")

        fb = (
            st.session_state.ultimo_feedback
        )

        if fb["status"] == "CORRETA":

            st.success(
                f"🎉 Excelente! "
                f"A **{fb['equipe']}** acertou!"
            )

        else:

            st.error(
                f"❌ A **{fb['equipe']}** errou."
                f" A correta era: "
                f"*{fb['correta_texto']}*"
            )

        st.info(
            f"💡 **Justificativa:**\n\n"
            f"{fb['por_que']}"
        )


# ============================================================
# MODO 2 - IA DE ASTRONOMIA
# ============================================================

elif (
    st.session_state.modo_sistema
    == "🌟 IA de Astronomia para Crianças"
):

    st.title(
        "🌟 IA de Astronomia"
    )

    st.markdown(
        "### *Faça qualquer pergunta sobre o Universo "
        "e receba uma explicação científica completa.*"
    )

    st.markdown("---")

    st.info(
        "🔭 A IA pesquisa a pergunta e depois "
        "elabora uma explicação desenvolvida. "
        "A resposta terá entre 5 e 12 parágrafos."
    )

    # --------------------------------------------------------
    # PERGUNTA
    # --------------------------------------------------------

    pergunta = st.text_area(

        "🌌 O que você quer descobrir sobre o Universo?",

        placeholder=(
            "Exemplo: "
            "Por que os buracos negros não deixam a luz escapar?"
        ),

        height=120
    )

    col1, col2 = st.columns(2)

    with col1:

        pesquisar = st.button(
            "🔭 Pesquisar e Explicar"
        )

    with col2:

        limpar = st.button(
            "🧹 Limpar Histórico"
        )

    if limpar:

        st.session_state.historico_explicacoes = []

        st.rerun()

    # --------------------------------------------------------
    # EXECUTAR PESQUISA
    # --------------------------------------------------------

    if pesquisar:

        if not pergunta.strip():

            st.warning(
                "Digite uma pergunta de Astronomia."
            )

        else:

            with st.spinner(
                "🔭 Pesquisando o Universo e preparando "
                "uma explicação completa..."
            ):

                resultado = (
                    pesquisar_e_explicar_com_ia(
                        pergunta.strip()
                    )
                )

            if resultado["sucesso"]:

                st.session_state.historico_explicacoes.insert(

                    0,

                    {
                        "pergunta": pergunta.strip(),

                        "resposta": resultado["resposta"],

                        "fontes": resultado["fontes"],

                        "data": datetime.now().strftime(
                            "%d/%m/%Y %H:%M"
                        )
                    }
                )

                st.success(
                    "✨ Explicação preparada!"
                )

            else:

                st.error(
                    "Não foi possível consultar a IA."
                )

                st.code(
                    resultado["erro"]
                )

                st.info(
                    "Verifique se OPENAI_API_KEY "
                    "está configurada nos Secrets."
                )

    # --------------------------------------------------------
    # HISTÓRICO
    # --------------------------------------------------------

    st.markdown("---")

    if (
        st.session_state.historico_explicacoes
    ):

        for item in (
            st.session_state.historico_explicacoes
        ):

            pergunta_html = html.escape(
                item["pergunta"]
            )

            st.markdown(
                f"""
                <div class="card-explicacao">

                    <div class="titulo-crianca">
                        🌌 {pergunta_html}
                    </div>

                    <div style="
                        color:#94a3b8;
                        font-size:13px;
                        margin-bottom:20px;
                    ">
                        Pesquisa realizada em:
                        {item["data"]}
                    </div>

                </div>
                """,
                unsafe_allow_html=True
            )

            # ------------------------------------------------
            # MOSTRAR PARÁGRAFOS SEPARADAMENTE
            # ------------------------------------------------

            resposta = item["resposta"]

            paragrafos = [

                p.strip()

                for p in resposta.split("\n\n")

                if p.strip()

            ]

            # Caso a IA tenha retornado quebras simples
            if len(paragrafos) < 5:

                paragrafos = [

                    p.strip()

                    for p in resposta.split("\n")

                    if p.strip()

                ]

            # ------------------------------------------------
            # GARANTIR VISUAL DE TEXTO LONGO
            # ------------------------------------------------

            for paragrafo in paragrafos:

                paragrafo_seguro = html.escape(
                    paragrafo
                )

                st.markdown(
                    f"""
                    <div class="paragrafo-ia">
                        {paragrafo_seguro}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            # ------------------------------------------------
            # FONTES
            # ------------------------------------------------

            st.markdown("---")

            st.markdown(
                "### 🔎 Fontes encontradas na pesquisa"
            )

            fontes = item.get(
                "fontes",
                []
            )

            if fontes:

                for fonte in fontes:

                    titulo_fonte = html.escape(
                        fonte.get(
                            "titulo",
                            "Fonte consultada"
                        )
                    )

                    url_fonte = fonte.get(
                        "url",
                        ""
                    )

                    if url_fonte:

                        st.markdown(
                            f"""
                            <div class="fonte-card">

                            📚 <strong>
                            {titulo_fonte}
                            </strong>

                            <br>

                            <a href="{url_fonte}"
                            target="_blank"
                            style="
                            color:#4cc9f0;
                            font-weight:bold;
                            ">

                            🌐 Abrir fonte

                            </a>

                            </div>
                            """,
                            unsafe_allow_html=True
                        )

            else:

                st.info(
                    "As referências da pesquisa "
                    "não puderam ser exibidas separadamente."
                )

            st.markdown(
                "---"
            )

    else:

        st.info(
            "🌠 Digite qualquer pergunta sobre "
            "Astronomia para começar."
        )

        st.markdown("""
        ### 💡 Exemplos de perguntas

        **🕳️ Buracos negros**

        Por que um buraco negro consegue impedir que a luz escape?

        **⭐ Estrelas**

        Como uma estrela nasce e por que ela começa a brilhar?

        **🌌 Universo**

        Como sabemos que o Universo está se expandindo?

        **🪐 Exoplanetas**

        Como os cientistas descobrem planetas que estão fora do Sistema Solar?

        **🌑 Matéria escura**

        Como os cientistas sabem que existe matéria escura se não conseguem vê-la?

        **💥 Big Bang**

        O que aconteceu nos primeiros momentos do Universo?

        **🌠 Galáxias**

        Por que as galáxias giram?

        **☀️ Sol**

        Como o Sol produz sua energia?
        """)
