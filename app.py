import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Investigação Cósmica: O Segredo de Death Tahim",
    page_icon="🌌",
    layout="wide",
)

# Estilização Visual (Tema Sci-Fi Pedagógico & Star Wars)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #03030a;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #00ffff !important;
        text-align: center;
    }
    .stButton>button {
        background-color: #11112b;
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        height: 50px;
    }
    .stButton>button:hover {
        background-color: #00ffff;
        color: #03030a;
    }
    .subsunsor-box {
        background-color: #1a120b;
        border-left: 5px solid #ffaa00;
        padding: 18px;
        border-radius: 8px;
        margin-bottom: 20px;
        font-size: 15px;
        line-height: 1.5;
    }
    .texto-base-box {
        background-color: #0b0b1c;
        border-left: 5px solid #00ffff;
        padding: 24px;
        border-radius: 8px;
        margin-bottom: 20px;
        font-size: 16px;
        line-height: 1.7;
    }
    .pergunta-box {
        background-color: #0a0a1a;
        border: 1px solid #ff00ff;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .raquel-box {
        background-color: #120a26;
        border: 2px solid #00ffff;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    .vilao-box {
        background-color: #1c0505;
        border: 2px solid #ff3333;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
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
# BANCO DE CASOS COM TEXTOS EXPANDIDOS E RESPOSTAS VARIADAS (SEM PADRÃO 'A')
# =========================================================================

CASOS_INVESTIGACAO = [
    {
        "id": 1,
        "titulo": (
            "Caso 1: O Nascimento do Cosmos e a Queda do Dogma Estático"
        ),
        "subsunsor_previo": (
            "🧠 **Ativação de Conhecimento Prévio:** Pense na sua vivência"
            " cotidiana e na herança cultural de que o céu noturno e o mundo"
            " físico representam um cenário eterno, imutável e estruturalmente"
            " fixo. Essa ideia arraigada na mente será desafiada pelas"
            " evidências da astrofísica moderna."
        ),
        "texto_base": (
            "📜 **Arquivo Histórico Extendido nº 01 (Relatório Científico):**"
            " Durante milênios, a totalidade da civilização humana sustentou"
            " dogmaticamente a premissa filosófica e intuitiva de que o"
            " universo possuía uma natureza estática, imutável, infinita no"
            " espaço e eterna no tempo. As estrelas eram encaradas como"
            " marcadores perenes em um relógio cósmico inalterável. No entanto,"
            " os alvores do século XX testemunharam uma reviravolta sem"
            " precedentes com a publicação da Teoria da Relatividade Geral por"
            " Albert Einstein, que remodelou a compreensão geométrica da"
            " gravidade, associando-a à curvatura do próprio espaço-tempo. Em"
            " 1927, o físico teórico e sacerdote católico Georges Lemaître"
            " mergulhou profundamente nas equações de campo einsteinianas e"
            " deduziu algo matematicamente inevitável e conceitualmente"
            " herético para a época: o cosmo não podia estar em repouso estável;"
            " ele exigia uma dinâmica de expansão ou de colapso. Ousando"
            " projetar o fluxo temporal para trás, Lemaître formulou que a"
            " totalidade da massa e da energia atualmente dispersas no universo"
            " esteve outrora concentrada em um ponto de densidade quase"
            " infinita, ao qual denominou 'Átomo Primitivo'. A posterior"
            " descompressão explosiva desse núcleo gerou o espaço, o tempo e a"
            " expansão métrica universal — o evento fundamental que a"
            " comunidade científica posteriormente consagrou como o Big Bang."
            " Death Tahim, agindo como o guardião severo das antigas certezas,"
            " tentou suprimir e corromper esses arquivos para manter a"
            " humanidade algemada à ilusão da estagnação perpétua."
        ),
        "video_recomendado": (
            "🎥 **Vídeo Recomendado para Pesquisa:** Assista no YouTube a"
            " documentários sobre *"
            " https://www.youtube.com/results?search_query=Georges+Lemaitre+Big+Bang+Cosmologia"
            " * (Pesquise por: *Georges Lemaître e a Origem do Big Bang*)."
        ),
        "banco_questoes": [
            {
                "enunciado": (
                    "Qual pilar filosófico e intuitivo sustentou a visão de"
                    " mundo da humanidade a respeito do cosmo durante"
                    " milênios?"
                ),
                "opcoes": [
                    (
                        "Imutabilidade perpétua de um cenário cósmico visto"
                        " como perene e estagnado."
                    ),
                    (
                        "Colisões cíclicas e regulares entre galáxias distantes"
                        " a cada século."
                    ),
                    (
                        "Fluxo temporal invertido nas regiões de vácuo absoluto."
                    ),
                    (
                        "Posicionamento do Sol na margem externa e isolada da"
                        " via Láctea."
                    ),
                ],
                "correta": (
                    "Imutabilidade perpétua de um cenário cósmico visto como"
                    " perene e estagnado."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Pense no conceito tradicional"
                        " que as civilizações antigas mantinham sobre o céu."
                        " Como o cosmo era visto antes da física moderna?"
                    ),
                    "opcoes": [
                        ("Estrutura permanente, perene e estagnada."),
                        ("Laboratório dinâmico em expansão acelerada."),
                        ("Oceano de fluidos magnéticos flutuantes no vácuo."),
                        ("Sistema estelar em processo de colapso cíclico."),
                    ],
                    "correta": ("Estrutura permanente, perene e estagnada."),
                },
            },
            {
                "enunciado": (
                    "De que maneira a Relatividade Geral de Einstein alterou"
                    " a compreensão clássica sobre a gravidade em escala"
                    " macroscópica?"
                ),
                "opcoes": [
                    (
                        "Forças eletromagnéticas geradas por núcleos densos de"
                        " ferro."
                    ),
                    (
                        "Vinculando o fenômeno gravitacional à deformação e"
                        " curvatura geométrica do espaço-tempo."
                    ),
                    (
                        "Atração mecânica mediada por fios invisíveis de"
                        " matéria escura."
                    ),
                    (
                        "Redução progressiva da massa corporal conforme o corpo"
                        " se desloca."
                    ),
                ],
                "correta": (
                    "Vinculando o fenômeno gravitacional à deformação e"
                    " curvatura geométrica do espaço-tempo."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Releia o texto. O que a teoria"
                        " de Einstein estabeleceu sobre a gravidade e o"
                        " universo?"
                    ),
                    "opcoes": [
                        ("Que a força gravitacional repele galáxias distantes."),
                        ("Que o espaço é plano, rígido e imune a massas."),
                        (
                            "Que a gravidade modela a geometria e a curvatura"
                            " do espaço-tempo."
                        ),
                        ("Que o tempo flui independentemente da massa estelar."),
                    ],
                    "correta": (
                        "Que a gravidade modela a geometria e a curvatura do"
                        " espaço-tempo."
                    ),
                },
            },
            {
                "enunciado": (
                    "Ao examinar as equações de campo einsteinianas, qual"
                    " contradição matemática inevitável Lemaître identificou em"
                    " relação ao modelo vigente?"
                ),
                "opcoes": [
                    (
                        "Centro universal ocupado inteiramente por antimatéria"
                        " pura."
                    ),
                    (
                        "Cálculos indicando massa infinita para fótons no vácuo"
                        " interestelar."
                    ),
                    (
                        "Invalidação total da existência de corpos celestes com"
                        " massa."
                    ),
                    (
                        "Instabilidade do sistema físico, exigindo expansão"
                        " ininterrupta ou contração."
                    ),
                ],
                "correta": (
                    "Instabilidade do sistema físico, exigindo expansão"
                    " ininterrupta ou contração."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Lemaître percebeu que as"
                        " equações matemáticas rejeitavam qual estado"
                        " tradicional?"
                    ),
                    "opcoes": [
                        ("A estagnação e o repouso estático global."),
                        ("A aceleração infinita dos fótons de luz."),
                        ("A rotação síncrona dos planetas rochosos."),
                        ("A densidade nula do espaço interestelar."),
                    ],
                    "correta": ("A estagnação e o repouso estático global."),
                },
            },
            {
                "enunciado": (
                    "Qual foi o conceito conceitual batizado por Georges"
                    " Lemaître para representar o ponto inicial de concentração"
                    " máxima da realidade física?"
                ),
                "opcoes": [
                    ("Semente de Vácuo Quântico."),
                    ("Átomo Primitivo."),
                    ("Núcleo de Entropia Zero."),
                    ("Plasmocentro Primordial."),
                ],
                "correta": ("Átomo Primitivo."),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Busque nos registros históricos"
                        " do caso o nome dado à singularidade hiperdensa."
                    ),
                    "opcoes": [
                        ("Coração de Quantum."),
                        ("Ponto Omega Absoluto."),
                        ("Átomo Primitivo."),
                        ("Esfera de Neutrônicos."),
                    ],
                    "correta": ("Átomo Primitivo."),
                },
            },
            {
                "enunciado": (
                    "Quais dimensões estruturais e fundamentais foram"
                    " deflagradas a partir da descompressão explosiva desse"
                    " núcleo primordial?"
                ),
                "opcoes": [
                    (
                        "Campos magnéticos isolados e partículas dispersas de"
                        " éter."
                    ),
                    ("Buracos negros estelares e cometas de gelo cósmico."),
                    (
                        "O espaço tridimensional, o fluxo do tempo e a"
                        " expansão métrica universal."
                    ),
                    ("A atmosfera gasosa dos planetas do sistema solar."),
                ],
                "correta": (
                    "O espaço tridimensional, o fluxo do tempo e a expansão"
                    " métrica universal."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** A explosão primordial não criou"
                        " apenas matéria, mas estruturou a própria realidade de"
                        " quê?"
                    ),
                    "opcoes": [
                        ("Apenas da luz visível e do calor estelar."),
                        ("Somente das órbitas planetárias e luas."),
                        ("Do espaço, do tempo e da expansão cósmica."),
                        ("Unicamente dos campos gravitacionais locais."),
                    ],
                    "correta": (
                        "Do espaço, do tempo e da expansão cósmica."
                    ),
                },
            },
            {
                "enunciado": (
                    "Qual papel estratégico a narrativa atribui à"
                    " intervenção de Death Tahim perante estas descobertas?"
                ),
                "opcoes": [
                    (
                        "Financiar a construção de sondas para exploração"
                        " exoplanetária."
                    ),
                    (
                        "Abafar e corromper os arquivos para manter o"
                        " intelecto humano preso ao dogma estático."
                    ),
                    (
                        "Auxiliar Lemaître diretamente nos cálculos de"
                        " expansão diferencial."
                    ),
                    (
                        "Medir com precisão milimétrica a temperatura da"
                        " radiação fóssil."
                    ),
                ],
                "correta": (
                    "Abafar e corromper os arquivos para manter o intelecto"
                    " humano preso ao dogma estático."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Lembre-se do antagonista do"
                        " laboratório. Qual era a intenção de Death Tahim"
                        " frente ao conhecimento?"
                    ),
                    "opcoes": [
                        (
                            "Corromper os registros para preservar a ilusão da"
                            " imutabilidade."
                        ),
                        ("Acelerar artificialmente a rotação da Via Láctea."),
                        ("Destruir todos os telescópios ópticos do planeta."),
                        ("Impedir o funcionamento de reatores nucleares."),
                    ],
                    "correta": (
                        "Corromper os registros para preservar a ilusão da"
                        " imutabilidade."
                    ),
                },
            },
            {
                "enunciado": (
                    "Analisando o impacto epistemológico da proposta de"
                    " Lemaître, por que ela representou uma revolução no"
                    " pensamento científico?"
                ),
                "opcoes": [
                    (
                        "Comprovação de massa infinita distribuída em qualquer"
                        " ponto espacial."
                    ),
                    (
                        "Banimento total da matemática nas investigações da"
                        " astrofísica."
                    ),
                    (
                        "Demonstração de que cometas superam a velocidade limite"
                        " da luz."
                    ),
                    (
                        "Substituição de um cosmo eterno por uma linha"
                        " temporal finita com um marco inicial dinâmico."
                    ),
                ],
                "correta": (
                    "Substituição de um cosmo eterno por uma linha temporal"
                    " finita com um marco inicial dinâmico."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel (Questão Crítica):** Pense na"
                        " grande virada conceitual: qual foi a ruptura de"
                        " aceitar que o universo teve um começo?"
                    ),
                    "opcoes": [
                        (
                            "O reconhecimento de que a história do cosmo teve um"
                            " início ativo e evolutivo."
                        ),
                        ("A certeza de que o universo tem tamanho zero hoje."),
                        ("A prova de que o tempo flui de trás para frente."),
                        ("A eliminação total da gravidade em escalas globais."),
                    ],
                    "correta": (
                        "O reconhecimento de que a história do cosmo teve um"
                        " início ativo e evolutivo."
                    ),
                },
            },
            {
                "enunciado": (
                    "Que qualificações fundamentais caracterizam a formação"
                    " acadêmica e profissional de Georges Lemaître conforme o"
                    " texto?"
                ),
                "opcoes": [
                    ("Atuação exclusiva como engenheiro naval militar."),
                    (
                        "Acúmulo de saberes como físico teórico e sacerdote"
                        " católico."
                    ),
                    (
                        "Dedicação integral a astronomia amadora focada em"
                        " cometas."
                    ),
                    (
                        "Funções diplomáticas exercidas em conjunto com"
                        " finanças."
                    ),
                ],
                "correta": (
                    "Acúmulo de saberes como físico teórico e sacerdote"
                    " católico."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** O texto menciona duas"
                        " ocupações importantes de Lemaître. Quais são elas?"
                    ),
                    "opcoes": [
                        ("Físico e padre católico."),
                        ("Filósofo e poeta clássico."),
                        ("Matemático e navegador."),
                        ("Químico e geólogo."),
                    ],
                    "correta": ("Físico e padre católico."),
                },
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Agente, leia cada linha com máxima"
            " atenção. O texto traz detalhes finos sobre a transição do"
            " pensamento estático para o dinâmico!'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'A eternidade estagnada é o meu"
            " domínio... Ouse desafiar minhas barreiras conceituais se puder!'"
        ),
    },
    {
        "id": 2,
        "titulo": "Caso 2: A Grande Expansão do Espaço-Tempo e o Redshift",
        "subsunsor_previo": (
            "🧠 **Ativação de Conhecimento Prévio:** Pense em um trem que apita"
            " ao se afastar: o som fica mais grave porque as ondas sonoras se"
            " esticam. Na astronomia, utilizamos essa analogia intuitiva para"
            " compreender como a luz de galáxias distantes se altera ao viajar"
            " pelo espaço."
        ),
        "texto_base": (
            "📜 **Arquivo Histórico Extendido nº 02 (Relatório Científico):**"
            " Nas vibrantes décadas de observação astronômica dos anos 1920,"
            " o eminente astrônomo Edwin Hubble liderou investigações"
            " espectroscópicas revolucionárias que alteraram nossa escala de"
            " percepção da realidade. Ao examinar minuciosamente o espectro"
            " eletromagnético da radiação emitida por galáxias distantes,"
            " Hubble identificou um padrão inequívoco: as linhas espectrais"
            " apresentavam um deslocamento sistemático em direção a"
            " comprimentos de onda mais longos, correspondendo à porção"
            " vermelha do espectro visível (um fenômeno universalmente"
            " conhecido como *redshift* ou desvio para o vermelho). Para"
            " observadores desprovidos de rigor crítico, a dedução imediata"
            " podia parecer que os aglomerados galácticos estavam em uma"
            " frenética corrida mecânica, disparando *através* de um vácuo"
            " estático e imutável. No entanto, a rigorosa interpretação"
            " cosmológica fundamentada na Relatividade Geral revelou uma"
            " realidade geométrica muito mais grandiosa: as galáxias não estão"
            " apenas navegando no espaço; é o próprio tecido métrico do"
            " espaço-tempo que se estica ativamente, afastando os corpos"
            " celestes uns dos outros em proporção direta à distância que os"
            " separa. Death Tahim tentou manipular esses dados espectrais para"
            " induzir a comunidade a acreditar que o universo estaria em"
            " colapso retrógrado."
        ),
        "video_recomendado": (
            "🎥 **Vídeo Recomendado para Pesquisa:** Assista no YouTube a"
            " vídeos educacionais sobre *"
            " https://www.youtube.com/results?search_query=Edwin+Hubble+Redshift+Expansao+do+Universo"
            " * (Pesquise por: *Edwin Hubble, Redshift e a Expansão do Universo*)."
        ),
        "banco_questoes": [
            {
                "enunciado": (
                    "Qual metodologia instrumental foi adotada por Edwin"
                    " Hubble para examinar a radiação luminosa dos confins"
                    " cósmicos?"
                ),
                "opcoes": [
                    ("Medições diretas de campo magnético em planetas."),
                    ("Investigações espectroscópicas de alta precisão."),
                    ("Cálculos estatísticos de densidade atmosférica."),
                    ("Análise de reflexão de radar em meteoroides."),
                ],
                "correta": ("Investigações espectroscópicas de alta precisão."),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** O texto aponta que Hubble"
                        " utilizou análises de qual tipo na radiação luminosa?"
                    ),
                    "opcoes": [
                        ("Espectroscópicas."),
                        ("Termodinâmicas."),
                        ("Mecânicas fluidas."),
                        ("Magneto-ópticas."),
                    ],
                    "correta": ("Espectroscópicas."),
                },
            },
            {
                "enunciado": (
                    "Como a astrofísica define o fenômeno de deslocamento das"
                    " linhas espectrais luminosas em direção a faixas mais"
                    " longas?"
                ),
                "opcoes": [
                    ("Compressão cromática azulada de feixes."),
                    ("Polarização quântica de vácuo interestelar."),
                    ("Redshift (desvio para o vermelho)."),
                    ("Refração direta em prisma estelar."),
                ],
                "correta": ("Redshift (desvio para o vermelho)."),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Releia o texto para encontrar o"
                        " termo em inglês usado para o desvio na direção da"
                        " cor vermelha."
                    ),
                    "opcoes": [
                        ("Redshift."),
                        ("Blueshift."),
                        ("Frequência zero."),
                        ("Efeito Doppler acústico."),
                    ],
                    "correta": ("Redshift."),
                },
            },
            {
                "enunciado": (
                    "Qual era a armadilha conceitual em que observadores"
                    " desatentos costumavam cair ao analisar o afastamento"
                    " galáctico?"
                ),
                "opcoes": [
                    (
                        "Supor que as galáxias corriam como projéteis velozes"
                        " dentro de um palco estático."
                    ),
                    (
                        "Acreditar que aglomerados estelares evaporavam em"
                        " calor puro."
                    ),
                    (
                        "Imaginar a Terra posicionada imóvel no centro exato"
                        " do cosmo."
                    ),
                    (
                        "Considerar perda de velocidade natural da luz no"
                        " vácuo."
                    ),
                ],
                "correta": (
                    "Supor que as galáxias corriam como projéteis velozes"
                    " dentro de um palco estático."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** O texto alerta sobre o erro de"
                        " achar que as galáxias apenas...?"
                    ),
                    "opcoes": [
                        (
                            "Disparavam correndo através de um espaço rígido e"
                            " imóvel."
                        ),
                        ("Giravam em órbitas circulares fixas ao redor do Sol."),
                        ("Caíam juntas em direção a buracos negros locais."),
                        ("Emitiam feixes de raios gama destrutivos."),
                    ],
                    "correta": (
                        "Disparavam correndo através de um espaço rígido e"
                        " imóvel."
                    ),
                },
            },
            {
                "enunciado": (
                    "De acordo com a Relatividade Geral, qual é a causa"
                    " geométrica real do afastamento mútuo das galáxias?"
                ),
                "opcoes": [
                    ("Ação de jatos de plasma soprados por supernovas."),
                    ("Colisão cruzada de linhas magnéticas intergalácticas."),
                    (
                        "O estiramento métrico contínuo do próprio tecido do"
                        " espaço-tempo."
                    ),
                    ("Rotação global universal em torno de um eixo fixo."),
                ],
                "correta": (
                    "O estiramento métrico contínuo do próprio tecido do"
                    " espaço-tempo."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** O que é que realmente se"
                        " estica para afastar os corpos celestes?"
                    ),
                    "opcoes": [
                        ("O tecido geométrico do espaço-tempo."),
                        ("A atmosfera invisível das galáxias."),
                        ("As órbitas elípticas dos cometas."),
                        ("O campo gravitacional dos núcleos."),
                    ],
                    "correta": ("O tecido geométrico do espaço-tempo."),
                },
            },
            {
                "enunciado": (
                    "Que proporção métrica o texto estabelece entre a"
                    " velocidade de afastamento e a posição espacial dos"
                    " aglomerados?"
                ),
                "opcoes": [
                    (
                        "A velocidade de afastamento é diretamente proporcional"
                        " à distância que os separa."
                    ),
                    (
                        "Galáxias próximas afastam-se mais rápido que as"
                        " distantes."
                    ),
                    (
                        "Ausência total de relação matemática entre distância e"
                        " fuga."
                    ),
                    (
                        "Inversão proporcional relacionada ao brilho visível do"
                        " núcleo."
                    ),
                ],
                "correta": (
                    "A velocidade de afastamento é diretamente proporcional à"
                    " distância que os separa."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Releia o trecho final do"
                        " parágrafo: o afastamento é proporcional a quê?"
                    ),
                    "opcoes": [
                        ("À distância física entre os corpos."),
                        ("À idade média de cada estrela."),
                        ("Ao peso atômico do hidrogênio."),
                        ("À temperatura do gás interestelar."),
                    ],
                    "correta": ("À distância física entre os corpos."),
                },
            },
            {
                "enunciado": (
                    "Qual artifício distorcido Death Tahim tentou aplicar"
                    " sobre os relatórios de Hubble?"
                ),
                "opcoes": [
                    (
                        "Afirmar que o desvio vermelho derivava de poluição"
                        " gasosa."
                    ),
                    (
                        "Argumentar que o universo sofria um processo de"
                        " colapso retrógrado interno."
                    ),
                    ("Ocultar a existência de vizinhanças galácticas."),
                    (
                        "Provar que o tempo desacelerava unicamente no planeta"
                        " Terra."
                    ),
                ],
                "correta": (
                    "Argumentar que o universo sofria um processo de colapso"
                    " retrógrado interno."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** O vilão quis inverter a"
                        " lógica da expansão. O que ele alegou?"
                    ),
                    "opcoes": [
                        ("Que o cosmo estava encolhendo em colapso."),
                        ("Que o universo havia parado de girar."),
                        ("Que as estrelas estavam se apagando."),
                        ("Que o vácuo absorvia toda a matéria."),
                    ],
                    "correta": ("Que o cosmo estava encolhendo em colapso."),
                },
            },
            {
                "enunciado": (
                    "Analisando profundamente a física envolvida, por que a"
                    " expansão métrica do espaço supera a visão de movimento"
                    " mecânico simples?"
                ),
                "opcoes": [
                    (
                        "Ganho de massa mensurável em fótons ao cruzarem o"
                        " vácuo."
                    ),
                    ("Eliminação completa da gravidade intergaláctica."),
                    (
                        "Validação de coordenadas espaciais absolutas e"
                        " estáticas."
                    ),
                    (
                        "Evidência de que o palco da matéria é flexível e"
                        " dinâmico, e não rígido."
                    ),
                ],
                "correta": (
                    "Evidência de que o palco da matéria é flexível e"
                    " dinâmico, e não rígido."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel (Questão Crítica):** Pense no"
                        " espaço como um tecido elástico. Qual é a revolução de"
                        " entender que ele estica?"
                    ),
                    "opcoes": [
                        (
                            "O próprio recipiente geométrico do cosmos se"
                            " expande ativamente."
                        ),
                        ("Os planetas aumentam de tamanho físico."),
                        ("O Sol duplica sua massa a cada ano."),
                        ("As leis físicas deixam de valer nas bordas."),
                    ],
                    "correta": (
                        "O próprio recipiente geométrico do cosmos se expande"
                        " ativamente."
                    ),
                },
            },
            {
                "enunciado": (
                    "Em qual período temporal específico as investigações"
                    " espectroscópicas de Edwin Hubble ganharam notoriedade"
                    " mundial?"
                ),
                "opcoes": [
                    ("Nos anos de 1850 durante a industrialização."),
                    ("Na década de 1920."),
                    ("No início do século XXI digital."),
                    ("Durante a transição histórica renascentista."),
                ],
                "correta": ("Na década de 1920."),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Releia a primeira frase do"
                        " arquivo histórico nº 02."
                    ),
                    "opcoes": [
                        ("Na década de 1920."),
                        ("Nos anos 1980."),
                        ("Na década de 1950."),
                        ("No ano de 2010."),
                    ],
                    "correta": ("Na década de 1920."),
                },
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Lembre-se da nossa dinâmica com o"
            " balão de borracha! O estiramento afeta todos os pontos de forma"
            " igualitária.'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'O tecido do espaço é maleável e"
            " frágil... Eu posso distorcê-lo se sua cognição fraquejar!'"
        ),
    },
    {
        "id": 3,
        "titulo": (
            "Caso 3: O Mistério Oculto da Matéria Escura e da Energia Escura"
        ),
        "subsunsor_previo": (
            "🧠 **Ativação de Conhecimento Prévio:** Pense na gravidade que"
            " mantém você preso ao solo e como uma mola reage ao ser esticada"
            " ou comprimida. Na cosmologia avançada, lidamos com componentes"
            " invisíveis que atuam como forças de coesão ou como motores de"
            " aceleração cósmica."
        ),
        "texto_base": (
            "📜 **Arquivo Histórico Extendido nº 03 (Relatório Científico):**"
            " Conforme a astrofísica contemporânea aprofundou o mapeamento da"
            " arquitetura em larga escala do universo, um enigma monumental"
            " desafiou os teóricos mais brilhantes: ao calcularem a velocidade"
            " de rotação das estrelas localizadas nas regiões periféricas das"
            " galáxias espirais, constatou-se que elas giravam com uma rapidez"
            " espantosa, muito além do que a massa de matéria luminosa visível"
            " (estrelas, nebulosas e gás brilhante) conseguiria sustentar"
            " gravitacionalmente. Se houvesse apenas o material que conseguimos"
            " enxergar, a atração gravitacional seria demasiadamente fraca e"
            " essas estrelas periféricas escaparíam em disparada para o vazio"
            " intergaláctico. A conclusão inevitável exigiu a presença de um"
            " vasto halo de massa invisível e não luminosa — a Matéria Escura"
            " —, que atua coesivamente atraindo e unindo estruturalmente as"
            " galáxias. Em contraponto dinâmico, investigações recentes com"
            " supernovas distantes revelaram algo ainda mais impressionante:"
            " a expansão do universo não está freando por causa da gravidade,"
            " mas sim acelerando, impulsionada por uma misteriosa pressão"
            " repulsiva de vácuo batizada de Energia Escura. Death Tahim"
            " utilizou esses dois grandes véus de mistério para encenar o papel"
            " de senhor absoluto do caos, testando rigorosamente os limites da"
            " mente humana."
        ),
        "video_recomendado": (
            "🎥 **Vídeo Recomendado para Pesquisa:** Assista no YouTube a"
            " vídeos científicos sobre *"
            " https://www.youtube.com/results?search_query=Materia+Escura+e+Energia+Escura+Cosmologia"
            " * (Pesquise por: *Matéria Escura e Energia Escura explicadas*)."
        ),
        "banco_questoes": [
            {
                "enunciado": (
                    "Que anomalia dinâmica os astrofísicos detectaram ao"
                    " examinar as curvas de rotação das estrelas nas bordas"
                    " galácticas?"
                ),
                "opcoes": [
                    ("Bordas galácticas em estado de repouso absoluto."),
                    (
                        "Velocidade estelar periférica muito acima da"
                        " sustentável pela massa visível."
                    ),
                    ("Movimento oposto ao sentido do núcleo galáctico."),
                    ("Emissão restrita a raios gama de alta intensidade."),
                ],
                "correta": (
                    "Velocidade estelar periférica muito acima da sustentável"
                    " pela massa visível."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** O texto aponta que as estrelas"
                        " das bordas giravam de que maneira em relação à luz"
                        " visível?"
                    ),
                    "opcoes": [
                        ("Muito mais rápido do que a massa visível suportaria."),
                        ("Muito mais devagar do que o normal previsto."),
                        ("Em linha reta em direção ao vazio exterior."),
                        ("De forma estática sem nenhuma órbita."),
                    ],
                    "correta": (
                        "Muito mais rápido do que a massa visível suportaria."
                    ),
                },
            },
            {
                "enunciado": (
                    "Qual entidade teórica foi proposta para explicar a"
                    " existência da gravidade extra que impede a dispersão das"
                    " estrelas periféricas?"
                ),
                "opcoes": [
                    ("Buraco negro supermassivo na borda externa."),
                    ("Fricção gerada por ventos de plasma interestelar."),
                    ("Vasto halo de Matéria Escura."),
                    ("Reflexo luminescente de galáxias vizinhas."),
                ],
                "correta": ("Vasto halo de Matéria Escura."),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Como foi batizada a massa"
                        " invisível responsável por gerar essa gravidade"
                        " adicional?"
                    ),
                    "opcoes": [
                        ("Matéria Escura."),
                        ("Antimatéria estelar densa."),
                        ("Plasma primordial oculto."),
                        ("Gás de hidrogênio congelado."),
                    ],
                    "correta": ("Matéria Escura."),
                },
            },
            {
                "enunciado": (
                    "Qual é o papel funcional primordial exercido pela"
                    " Matéria Escura na arquitetura cósmica?"
                ),
                "opcoes": [
                    (
                        "Atracão gravitacional coesiva que une e estrutura as"
                        " galáxias."
                    ),
                    (
                        "Repulsão violenta de estrelas para acelerar o"
                        " afastamento."
                    ),
                    ("Absorção total de fótons emitidos por núcleos estelares."),
                    ("Criação de campos magnéticos protetores contra choques."),
                ],
                "correta": (
                    "Atracão gravitacional coesiva que une e estrutura as"
                    " galáxias."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Lembre-se: a matéria escura"
                        " atrai ou repele as estruturas galácticas?"
                    ),
                    "opcoes": [
                        ("Ela atrai e ajuda a unir as estruturas cósmicas."),
                        ("Ela repele as estrelas para longe do centro."),
                        ("Ela congela o tempo ao seu redor."),
                        ("Ela consome energia para criar buracos negros."),
                    ],
                    "correta": (
                        "Ela atrai e ajuda a unir as estruturas cósmicas."
                    ),
                },
            },
            {
                "enunciado": (
                    "O que as observações recentes de supernovas distantes"
                    " revelaram a respeito do ritmo da expansão cósmica?"
                ),
                "opcoes": [
                    ("Colapso gravitacional total em andamento."),
                    ("Velocidade de expansão completamente estagnada."),
                    (
                        "Aceleração contínua, desmentindo a hipótese de"
                        " frenagem gravitacional."
                    ),
                    ("Oscilação cíclica anual de expansão e contração."),
                ],
                "correta": (
                    "Aceleração contínua, desmentindo a hipótese de frenagem"
                    " gravitacional."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** O texto menciona que o ritmo da"
                        " expansão está fazendo o quê?"
                    ),
                    "opcoes": [
                        ("Acelerando cada vez mais."),
                        ("Desacelerando até parar."),
                        ("Mantendo-se estático e constante."),
                        ("Oscilando aleatoriamente."),
                    ],
                    "correta": ("Acelerando cada vez mais."),
                },
            },
            {
                "enunciado": (
                    "Qual componente teórico é apontado como responsável"
                    " por impulsionar essa aceleração repulsiva na expansão do"
                    " universo?"
                ),
                "opcoes": [
                    ("Pressão de radiação fóssil primária."),
                    ("Energia Escura."),
                    ("Campo magnético primordial de fundo."),
                    ("Entropia térmica absoluta."),
                ],
                "correta": ("Energia Escura."),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Busque no texto o nome da"
                        " pressão repulsiva de vácuo que acelera o cosmo."
                    ),
                    "opcoes": [
                        ("Energia Escura."),
                        ("Força de repulsão quântica."),
                        ("Vácuo magnético estelar."),
                        ("Pressão de plasma escuro."),
                    ],
                    "correta": ("Energia Escura."),
                },
            },
            {
                "enunciado": (
                    "De que maneira Death Tahim se valeu conceitualmente"
                    " desses dois grandes enigmas da astrofísica?"
                ),
                "opcoes": [
                    (
                        "Uso dos véus do desconhecido para encenar o mestre do"
                        " caos e testar o intelecto humano."
                    ),
                    (
                        "Tentativa de converter matéria escura em combustível"
                        " para frotas."
                    ),
                    ("Refúgio físico no interior de halos de energia escura."),
                    ("Eliminação de telescópios detectores de supernovas."),
                ],
                "correta": (
                    "Uso dos véus do desconhecido para encenar o mestre do"
                    " caos e testar o intelecto humano."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Qual foi a estratégia do"
                        " antagonista ao se esconder atrás dessas forças"
                        " invisíveis?"
                    ),
                    "opcoes": [
                        (
                            "Simular ser o senhor do caos para forçar testes"
                            " rigorosos na ciência."
                        ),
                        ("Destruir fisicamente todas as galáxias espirais."),
                        ("Roubar a luz visível de todas as estrelas."),
                        ("Impedir a formação de novos planetas."),
                    ],
                    "correta": (
                        "Simular ser o senhor do caos para forçar testes"
                        " rigorosos na ciência."
                    ),
                },
            },
            {
                "enunciado": (
                    "Sintetizando a atuação conjunta desses dois fenômenos,"
                    " qual é o balanço dinâmico que eles promovem na rota"
                    " evolutiva do cosmos?"
                ),
                "opcoes": [
                    (
                        "Matéria Escura aglutina e estrutura via gravidade,"
                        " enquanto Energia Escura acelera o afastamento"
                        " espacial."
                    ),
                    (
                        "Esforço conjunto direcionado estritamente ao colapso"
                        " em singularidade final."
                    ),
                    (
                        "Energia Escura gera galáxias e Matéria Escura expele"
                        " o espaço exterior."
                    ),
                    ("Ausência de interferência na gravidade macroscópica."),
                ],
                "correta": (
                    "Matéria Escura aglutina e estrutura via gravidade,"
                    " enquanto Energia Escura acelera o afastamento espacial."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel (Questão Crítica):** Lembre-se"
                        " do papel duplo: uma segura a estrutura (atração)"
                        " e a outra acelera a expansão (repulsão)."
                    ),
                    "opcoes": [
                        (
                            "Uma faz o papel de cola gravitacional e a outra de"
                            " motor de expansão acelerada."
                        ),
                        ("Uma congela as estrelas e a outra aquece o vácuo."),
                        ("Ambas funcionam como buracos negros idênticos."),
                        ("Uma cria luz e a outra consome o tempo."),
                    ],
                    "correta": (
                        "Uma faz o papel de cola gravitacional e a outra de"
                        " motor de expansão acelerada."
                    ),
                },
            },
            {
                "enunciado": (
                    "Que consequência direta a ausência de matéria escura"
                    " traria para as estrelas periféricas nas galáxias espirais?"
                ),
                "opcoes": [
                    (
                        "Desprendimento orbital e fuga rumo ao espaço"
                        " intergaláctico."
                    ),
                    ("Colisão instantânea contra o núcleo central estelar."),
                    ("Duplicação rápida de brilho e temperatura térmica."),
                    ("Transformação espontânea em estrelas de nêutrons."),
                ],
                "correta": (
                    "Desprendimento orbital e fuga rumo ao espaço"
                    " intergaláctico."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** O texto menciona que sem a"
                        " gravidade extra da matéria escura, a força de"
                        " atração seria fraca e as estrelas...?"
                    ),
                    "opcoes": [
                        ("Escaparíam para o espaço intergaláctico."),
                        ("Ficaríam paradas no mesmo lugar."),
                        ("Desceríam em direção ao centro do Sol."),
                        ("Congelaríam em gelo estelar."),
                    ],
                    "correta": ("Escaparíam para o espaço intergaláctico."),
                },
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Entenda bem o papel de cada força"
            " invisível: uma puxa para formar galáxias e a outra empurra o"
            " espaço cósmico!'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'Minhas sombras invisíveis são o"
            " teste supremo para a sua cognição. Prove seu valor!'"
        ),
    },
]

# =========================================================================
# GERENCIAMENTO DE ESTADO DA SESSÃO
# =========================================================================
if "modo" not in st.session_state:
  st.session_state.modo = "menu"
if "etapa_agente" not in st.session_state:
  st.session_state.etapa_agente = "investigacao"
if "indice_caso" not in st.session_state:
  st.session_state.indice_caso = 0
if "indice_questao_caso" not in st.session_state:
  st.session_state.indice_questao_caso = 0
if "questoes_sorteadas_caso" not in st.session_state:
  st.session_state.questoes_sorteadas_caso = []
if "em_resgate" not in st.session_state:
  st.session_state.em_resgate = False
if "erros_cometidos" not in st.session_state:
  st.session_state.erros_cometidos = []
if "nome_usuario" not in st.session_state:
  st.session_state.nome_usuario = ""
if "ranking" not in st.session_state:
  st.session_state.ranking = [
      {"nome": "Agente Felipe", "status": "Mestre (Death Tahim)", "pontos": 21},
      {
          "nome": "Raquel Ferreira (Heroína)",
          "status": "Comandante Cognitiva",
          "pontos": 21,
      },
  ]
if "logado_gerente" not in st.session_state:
  st.session_state.logado_gerente = False

# Título Principal
st.markdown(
    "<h1>🌌 Investigação Cósmica & Aprendizagem Significativa</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Ative seus conhecimentos,"
    " investigue textos detalhados com 7 questões sorteadas por caso e"
    " enfrente Death Tahim!</p>",
    unsafe_allow_html=True,
)
st.divider()

# =========================================================================
# MENU INICIAL
# =========================================================================
if st.session_state.modo == "menu":
  col_m1, col_m2 = st.columns(2)
  with col_m1:
    st.markdown("### 🕵️‍♂️ Área do Aluno (Agente Investigativo)")
    st.write(
        "Inicie a investigação com banco de questões dinâmico, análise e o"
        " desfecho épico com Death Tahim!"
    )
    if st.button("Entrar como Agente"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.indice_questao_caso = 0
      st.session_state.em_resgate = False
      st.session_state.erros_cometidos = []
      caso_inicial = CASOS_INVESTIGACAO[0]
      st.session_state.questoes_sorteadas_caso = random.sample(
          caso_inicial["banco_questoes"],
          min(7, len(caso_inicial["banco_questoes"])),
      )
      st.rerun()

  with col_m2:
    st.markdown("### ⚙️ Área do Gerente (Quartel-General)")
    st.write(
        "Acesso restrito ao organizador com credenciais (Felipe) para"
        " inspecionar os relatórios."
    )
    if st.button("Entrar como Gerente"):
      st.session_state.modo = "gerente"
      st.rerun()

# =========================================================================
# FLUXO DO ALUNO (AGENTE INVESTIGATIVO)
# =========================================================================
elif st.session_state.modo == "aluno":

  if st.button("⬅️ Voltar ao Menu Principal"):
    st.session_state.modo = "menu"
    st.rerun()

  st.divider()

  if (
      st.session_state.nome_usuario == ""
      and st.session_state.etapa_agente == "investigacao"
  ):
    st.subheader("🎯 Credenciamento do Agente Cognitivo")
    nome_input = st.text_input("Digite seu Nome de Agente ou Apelido:")
    if st.button("🚀 Iniciar Investigação"):
      if nome_input.strip() == "":
        st.warning("Por favor, digite um nome válido.")
      else:
        st.session_state.nome_usuario = nome_input.strip()
        st.rerun()
    st.stop()

  # ETAPA DE INVESTIGAÇÃO COM BANCO DINÂMICO
  if st.session_state.etapa_agente == "investigacao":
    idx = st.session_state.indice_caso
    total_casos = len(CASOS_INVESTIGACAO)

    if idx < total_casos:
      caso_atual = CASOS_INVESTIGACAO[idx]

      if not st.session_state.questoes_sorteadas_caso:
        st.session_state.questoes_sorteadas_caso = random.sample(
            caso_atual["banco_questoes"],
            min(7, len(caso_atual["banco_questoes"])),
        )

      questoes_ativas = st.session_state.questoes_sorteadas_caso
      total_q = len(questoes_ativas)
      q_idx = st.session_state.indice_questao_caso

      if q_idx < total_q:
        q_atual = questoes_ativas[q_idx]

        st.markdown(
            f"<h2>📁 {caso_atual['titulo']} (Questão {q_idx + 1} de"
            f" {total_q})</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            f"🕵️‍♂️ **Agente:** {st.session_state.nome_usuario} | **Progresso do"
            f" Caso:** {idx + 1} de {total_casos}"
        )
        st.progress((q_idx) / total_q)

        # 1. Ativação de Conhecimento Prévio
        st.markdown(
            f"<div class='subsunsor-box'>{caso_atual['subsunsor_previo']}</div>",
            unsafe_allow_html=True,
        )

        # 2. Texto Base de Investigação Longo e Detalhado
        st.markdown(
            f"<div class='texto-base-box'>{caso_atual['texto_base']}</div>",
            unsafe_allow_html=True,
        )

        # 3. Indicação de Vídeo Relacionado
        st.markdown(
            f"<div"
            f" style='background-color:#071a2e;border:1px solid"
            f" #00ffff;padding:12px;border-radius:8px;margin-bottom:20px;font-size:14px;'>{caso_atual['video_recomendado']}</div>",
            unsafe_allow_html=True,
        )

        col_q, col_r = st.columns([2, 1])

        with col_r:
          st.markdown(
              f"""
                    <div class='raquel-box'>
                        <h3 style='margin:0; color:#00ffff;'>👧 Raquel Ferreira</h3>
                        <p style='margin-top:8px; font-size:13px;'>{caso_atual['comentario_raquel']}</p>
                    </div>
                    """,
              unsafe_allow_html=True,
          )
          st.markdown(
              f"""
                    <div class='vilao-box'>
                        <h3 style='margin:0; color:#ff3333;'>😈 Death Tahim (Darth Tahim)</h3>
                        <p style='margin-top:8px; font-size:13px; font-style:italic;'>{caso_atual['comentario_makarius']}</p>
                    </div>
                    """,
              unsafe_allow_html=True,
          )

        with col_q:
          if not st.session_state.em_resgate:
            q_ativa = q_atual
            modo_p = "inicial"
          else:
            q_ativa = q_atual["resgate"]
            modo_p = "resgate"

          st.markdown(
              f"<div class='pergunta-box'><h4>{q_ativa['enunciado']}</h4></div>",
              unsafe_allow_html=True,
          )

          escolha_agente = st.radio(
              "Selecione a dedução investigativa correta:",
              q_ativa["opcoes"],
              key=f"radio_ausubel_{idx}_{q_idx}_{modo_p}",
          )

          st.markdown("<br>", unsafe_allow_html=True)
          if st.button("🔒 Validar Resposta e Avançar"):
            if escolha_agente == q_ativa["correta"]:
              st.success(
                  "✨ Conceito validado com sucesso! Integrado à sua estrutura"
                  " de raciocínio."
              )
              st.session_state.em_resgate = False
              st.session_state.indice_questao_caso += 1
              st.rerun()
            else:
              erro_info = (
                  f"**{caso_atual['titulo']} (Questão {q_idx + 1})**: Você"
                  f" selecionou uma dedução equivocada"
                  f" (*'{escolha_agente[:40]}...'*), gerando conflito com o"
                  f" conceito científico correto (*'{q_ativa['correta'][:40]}...'*)."
              )
              if erro_info not in st.session_state.erros_cometidos:
                st.session_state.erros_cometidos.append(erro_info)

              if not st.session_state.em_resgate:
                st.session_state.em_resgate = True
                st.error(
                    "❌ **Conflito Cognitivo (Erro Detectado)!** Death Tahim"
                    " bloqueou seu acesso. Suas ideias antigas colidiram com a"
                    " evidência correta. Leia a dica da Raquel e tente"
                    " novamente com a pista de resgate!"
                )
                st.rerun()
              else:
                st.error(
                    "❌ Errado novamente! O bloqueio continua ativo. Releia o"
                    " texto base e ajuste sua lógica conceitual."
                )
      else:
        st.session_state.indice_caso += 1
        st.session_state.indice_questao_caso = 0
        st.session_state.questoes_sorteadas_caso = []
        if st.session_state.indice_caso < total_casos:
          proximo_caso = CASOS_INVESTIGACAO[st.session_state.indice_caso]
          st.session_state.questoes_sorteadas_caso = random.sample(
              proximo_caso["banco_questoes"],
              min(7, len(proximo_caso["banco_questoes"])),
          )
        st.rerun()

    else:
      st.session_state.etapa_agente = "avaliacao_ausubel"
      st.rerun()

  # ETAPA 3: AVALIAÇÃO DIAGNÓSTICA DE ERROS & DESFECHO ÉPICO (DEATH TAHIM)
  elif st.session_state.etapa_agente == "avaliacao_ausubel":
    st.markdown(
        "<h2>📊 Avaliação Diagnóstica & Conhecimento do Universo</h2>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #0b1a2e; border: 2px solid #00ffff; padding: 20px; border-radius: 12px; margin-bottom: 20px;'>
            <h3 style='color: #00ffff; margin-top:0;'>🌌 O Desfecho: A Aparição de Death Tahim</h3>
            <p>Parabéns, Agente <b>{nome}</b>! Você investigou todos os 3 casos e venceu as questões dinâmicas sorteadas.</p>
            <p>As portas da câmara principal se abrem com um som metálico profundo. Das sombras surge <b>Death Tahim</b>, vestindo seu imponente traje preto estilo <i>Darth Vader</i> de <i>Star Wars</i>, com sua respiração mecânica ecoando pelo ambiente. Ao lado dele, <b>Raquel Ferreira</b> sorri orgulhosa.</p>
            <p style='color: #ffcc00; font-style: italic; font-size: 16px;'>
            "Impressionante...", diz Death Tahim com sua voz profunda, retirando o capacete escuro e revelando um olhar de absoluto respeito. "Você enfrentou os conflitos cognitivos, superou seus erros por meio da leitura atenta e reestruturou seu entendimento como um verdadeiro mestre. O erro nunca foi o fim, mas o degrau necessário para a evolução intelectual."
            </p>
            <p>Death Tahim ergue as mãos e lhe transfere formalmente o sagrado <b>Conhecimento do Universo</b>, dizendo: <i>"Eu assumi o manto e o visual do lado negro para forçar a sua mente a evoluir através da pesquisa crítica. Meus parabéns, agente. O cosmos agora está em boas mãos."</i></p>
        </div>
        """.format(
            nome=st.session_state.nome_usuario
        ),
        unsafe_allow_html=True,
    )

    st.subheader(
        "🧠 Relatório Pedagógico: Análise dos Erros e Desvios Conceituais"
    )
    if len(st.session_state.erros_cometidos) == 0:
      st.success(
          "🌟 Espantoso! Você não cometeu erros conceituais significativos"
          " durante a investigação de nenhum caso. Sua lógica estava"
          " perfeitamente alinhada desde o início!"
      )
    else:
      st.warning(
          "⚠️ Durante a jornada investigativa, foram mapeados os seguintes"
          " desvios conceituais que fizeram você se perder momentaneamente:"
      )
      for err in st.session_state.erros_cometidos:
        st.markdown(f"- {err}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("✍️ Relatório Final de Compreensão Cognitiva")
    st.write(
        "Para consolidar sua experiência, redija abaixo com suas próprias"
        " palavras o que você entendeu sobre a evolução do universo (Big Bang,"
        " Expansão e Matéria/Energia Escura) e como a leitura atenta e os erros"
        " superados ajudaram na sua compreensão:"
    )

    conclusao_ausubel = st.text_area(
        "Escreva sua compreensão final (Relatório Descritivo):",
        placeholder=(
            "Descreva detalhadamente o que aprendeu e como superou os erros..."
        ),
    )

    if st.button("📤 Protocolar Relatório Final e Receber o Título"):
      if not conclusao_ausubel.strip():
        st.warning(
            "Por favor, escreva seu relatório descritivo para registrar sua"
            " aprendizagem."
        )
      else:
        st.session_state.ranking.append({
            "nome": st.session_state.nome_usuario,
            "status": "Mestre Cósmico (Conhecimento do Universo)",
            "pontos": 21,
        })
        st.session_state.ranking = sorted(
            st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
        )
        st.session_state.etapa_agente = "fim_sucesso"
        st.rerun()

  # ETAPA 4: TELA DE SUCESSO E RANKING
  elif st.session_state.etapa_agente == "fim_sucesso":
    st.success(
        "🎉 Jornada Concluída com Honraria Máxima! Relatório protocolado com"
        " bênção de Death Tahim."
    )
    st.markdown(
        "### 🏆 Patente Concedida: Guardião(ã) do Conhecimento do Universo"
    )

    st.divider()
    st.subheader("📊 Ranking Oficial de Agentes Cognitivos")
    for pos, c in enumerate(st.session_state.ranking[:10], start=1):
      medalha = (
          "🥇"
          if pos == 1
          else ("🥈" if pos == 2 else ("🥉" if pos == 3 else "🔸"))
      )
      st.markdown(
          f"**{medalha} {pos}º lugar:** {c['nome']} — **Status:**"
          f" {c['status']}"
      )

    st.divider()
    if st.button("🔄 Realizar Nova Investigação (Questões Inéditas)"):
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.indice_questao_caso = 0
      st.session_state.em_resgate = False
      st.session_state.erros_cometidos = []
      st.session_state.nome_usuario = ""
      caso_inicial = CASOS_INVESTIGACAO[0]
      st.session_state.questoes_sorteadas_caso = random.sample(
          caso_inicial["banco_questoes"],
          min(7, len(caso_inicial["banco_questoes"])),
      )
      st.rerun()

# =========================================================================
# FLUXO DO GERENTE (QUARTEL-GENERAL / ADMIN)
# =========================================================================
elif st.session_state.modo == "gerente":

  if st.button("⬅️ Voltar ao Menu Principal"):
    st.session_state.modo = "menu"
    st.rerun()

  st.divider()
  st.markdown(
      "<h2>⚙️ Quartel-General: Painel de Controle do Gerente</h2>",
      unsafe_allow_html=True,
  )

  if not st.session_state.logado_gerente:
    with st.container():
      st.markdown(
          "<div class='admin-box'>🔒 <b>Acesso Restrito ao Gerente:</b> Digite"
          " suas credenciais de organizador (Felipe).</div>",
          unsafe_allow_html=True,
      )
      user_inp = st.text_input("Usuário do Gerente:")
      pass_inp = st.text_input("Senha de Acesso:", type="password")

      if st.button("🔑 Acessar Quartel-General"):
        if user_inp.strip() == "Felipe241198" and pass_inp.strip() == "123456789":
          st.session_state.logado_gerente = True
          st.success(
              "Acesso liberado! Bem-vindo de volta ao Quartel-General,"
              " Felipe."
          )
          st.rerun()
        else:
          st.error("❌ Credenciais de gerente incorretas.")
  else:
    st.success("✅ Sessão de Gerente Ativa (Felipe - Quartel-General)")

    st.subheader("📊 Relatório de Agentes e Análise de Desvios")
    if len(st.session_state.ranking) == 0:
      st.info("Nenhum agente concluiu as investigações ainda.")
    else:
      for pos, c in enumerate(st.session_state.ranking, start=1):
        st.markdown(
            f"**{pos}º:** 🕵️‍♂️ {c['nome']} — **Status:** {c['status']}"
        )

    st.divider()
    col_g1, col_g2 = st.columns(2)
    with col_g1:
      if st.button("🗑️ Limpar Arquivos do Ranking"):
        st.session_state.ranking = []
        st.success("Arquivos limpos com sucesso!")
        st.rerun()
    with col_g2:
      if st.button("🔒 Sair do Quartel-General"):
        st.session_state.logado_gerente = False
        st.session_state.modo = "menu"
        st.rerun()
