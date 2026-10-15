import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Investigação Cósmica & Ausubel: Death Tahim",
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
# BANCO GIGANTE DE MAIS DE 50 QUESTÕES E TEXTOS EXPANDIDOS (AUSUBEL)
# =========================================================================

CASOS_INVESTIGACAO = [
    {
        "id": 1,
        "titulo": (
            "Caso 1: O Nascimento do Cosmos e a Queda do Dogma Estático"
        ),
        "subsunsor_previo": (
            "🧠 **Ativação de Conhecimento Prévio (Subsunçor):** Pense na sua"
            " vivência cotidiana e na herança cultural e filosófica de que o"
            " céu noturno e o mundo físico representam um cenário eterno,"
            " imutável e estruturalmente fixo. Na teoria de David Ausubel, esse"
            " conceito arraigado na sua mente funciona como o subsunçor de"
            " ancoragem que será confrontado pelas evidências da astrofísica"
            " moderna."
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
            " documentários como *"
            " https://www.youtube.com/results?search_query=Georges+Lemaitre+Big+Bang+Cosmologia"
            " * (Pesquise por: *Georges Lemaître e a Origem do Big Bang*)."
        ),
        # Banco com 18 questões complexas (parte do total de 50+ do sistema) para sorteio aleatório
        "banco_questoes": [
            {
                "enunciado": (
                    "1. Qual pilar filosófico e intuitivo sustentou a visão de"
                    " mundo da humanidade a respeito do cosmo durante"
                    " milênios?"
                ),
                "opcoes": [
                    (
                        "A crença firmada em um cenário universal estático,"
                        " eterno e estruturalmente inalterável."
                    ),
                    (
                        "A certeza de que as galáxias se chocavam periodicamente"
                        " a cada século."
                    ),
                    (
                        "A hipótese de que o tempo fluía de trás para frente no"
                        " vácuo."
                    ),
                    (
                        "A tese de que o Sol ocupava a borda externa e isolada"
                        " da galáxia."
                    ),
                ],
                "correta": (
                    "A crença firmada em um cenário universal estático,"
                    " eterno e estruturalmente inalterável."
                ),
                "resgate": {
                    "enunciado": (
                        "⚠️ **Dica da Raquel:** Pense no conceito tradicional"
                        " que as civilizações antigas mantinham sobre o céu."
                        " Como o cosmo era visto antes da física moderna?"
                    ),
                    "opcoes": [
                        ("Como uma estrutura permanente, perene e estagnada."),
                        ("Como um laboratório dinâmico em expansão rápida."),
                        ("Como um oceano de fluidos magnéticos flutuantes."),
                        ("Como um sistema estelar em colapso cíclico."),
                    ],
                    "correta": (
                        "Como uma estrutura permanente, perene e estagnada."
                    ),
                },
            },
            {
                "enunciado": (
                    "2. De que maneira a Relatividade Geral de Einstein alterou"
                    " a compreensão clássica sobre a gravidade em escala"
                    " macroscópica?"
                ),
                "opcoes": [
                    (
                        "Vinculando o fenômeno gravitacional à deformação e"
                        " curvatura geométrica do espaço-tempo."
                    ),
                    (
                        "Tratando a gravidade como uma força eletromagnética"
                        " gerada por núcleos de ferro."
                    ),
                    (
                        "Comprovando que a atração ocorre por meio de fios"
                        " invisíveis de matéria escura."
                    ),
                    (
                        "Estabelecendo que a massa de um corpo diminui à medida"
                        " que ele se desloca."
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
                        (
                            "Que a gravidade modela a geometria e a curvatura"
                            " do espaço-tempo."
                        ),
                        ("Que a força gravitacional repele galáxias distantes."),
                        ("Que o espaço é plano, rígido e imune a massas."),
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
                    "3. Ao examinar as equações de campo einsteinianas, qual"
                    " contradição matemática inevitável Lemaître identificou em"
                    " relação ao modelo vigente?"
                ),
                "opcoes": [
                    (
                        "As equações demonstravam que o sistema físico era"
                        " instável e exigia expansão ou contração."
                    ),
                    (
                        "A matemática provava que o centro do universo era"
                        " ocupado por antimatéria pura."
                    ),
                    (
                        "Os cálculos indicavam que a luz possuía massa infinita"
                        " no vácuo interestelar."
                    ),
                    (
                        "A teoria anulava totalmente a existência de corpos"
                        " celestes com massa."
                    ),
                ],
                "correta": (
                    "As equações demonstravam que o sistema físico era"
                    " instável e exigia expansão ou contração."
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
                    "4. Qual foi o conceito conceitual batizado por Georges"
                    " Lemaître para representar o ponto inicial de concentração"
                    " máxima da realidade física?"
                ),
                "opcoes": [
                    ("Átomo Primitivo."),
                    ("Semente de Vácuo Quântico."),
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
                        ("Átomo Primitivo."),
                        ("Coração de Quantum."),
                        ("Ponto Omega Absoluto."),
                        ("Esfera de Neutrônicos."),
                    ],
                    "correta": ("Átomo Primitivo."),
                },
            },
            {
                "enunciado": (
                    "5. Quais dimensões estruturais e fundamentais foram"
                    " deflagradas a partir da descompressão explosiva desse"
                    " núcleo primordial?"
                ),
                "opcoes": [
                    (
                        "O espaço tridimensional, o fluxo do tempo e a"
                        " expansão métrica universal."
                    ),
                    ("Apenas os campos magnéticos e as partículas de éter."),
                    ("Somente os buracos negros estelares e cometas."),
                    ("A atmosfera gasosa dos planetas rochosos."),
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
                        ("Do espaço, do tempo e da expansão cósmica."),
                        ("Apenas da luz visível e do calor estelar."),
                        ("Somente das órbitas planetárias e luas."),
                        ("Unicamente dos campos gravitacionais locais."),
                    ],
                    "correta": (
                        "Do espaço, do tempo e da expansão cósmica."
                    ),
                },
            },
            {
                "enunciado": (
                    "6. Qual papel estratégico a narrativa atribui à"
                    " intervenção de Death Tahim perante estas descobertas?"
                ),
                "opcoes": [
                    (
                        "Tentar abafar e corromper os arquivos para manter o"
                        " intelecto humano preso ao dogma estático."
                    ),
                    (
                        "Financiar a construção de espaçonaves para explorar"
                        " exoplanetas distantes."
                    ),
                    (
                        "Auxiliar diretamente Lemaître nos cálculos"
                        " diferenciais de expansão."
                    ),
                    (
                        "Medir com precisão a temperatura da radiação de fundo"
                        " em micro-ondas."
                    ),
                ],
                "correta": (
                    "Tentar abafar e corromper os arquivos para manter o"
                    " intelecto humano preso ao dogma estático."
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
                    "7. Analisando o impacto epistemológico da proposta de"
                    " Lemaître, por que ela representou uma revolução no"
                    " pensamento científico?"
                ),
                "opcoes": [
                    (
                        "Porque substituiu a visão de um cosmo estagnado e"
                        " eterno por uma linha temporal finita com um marco"
                        " inicial dinâmico."
                    ),
                    (
                        "Porque comprovou que a matéria possui massa"
                        " inesgotável em qualquer ponto espacial."
                    ),
                    (
                        "Porque baniu definitivamente o uso da matemática nas"
                        " investigações de astrofísica."
                    ),
                    (
                        "Porque demonstrou que a velocidade da luz pode ser"
                        " superada por cometas."
                    ),
                ],
                "correta": (
                    "Porque substituiu a visão de um cosmo estagnado e eterno"
                    " por uma linha temporal finita com um marco inicial"
                    " dinâmico."
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
                    "8. Que qualificações fundamentais caracterizam a formação"
                    " acadêmica e profissional de Georges Lemaître conforme o"
                    " texto?"
                ),
                "opcoes": [
                    (
                        "Ele acumulava conhecimentos como físico teórico e"
                        " sacerdote católico."
                    ),
                    ("Ele atuava exclusivamente como engenheiro naval militar."),
                    (
                        "Ele era um astrônomo amador focado em cometas do"
                        " sistema solar."
                    ),
                    (
                        "Ele exercia funções de diplomata e matemático financeiro."
                    ),
                ],
                "correta": (
                    "Ele acumulava conhecimentos como físico teórico e"
                    " sacerdote católico."
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
            "🧠 **Ativação de Conhecimento Prévio (Subsunçor):** Pense em um"
            " trem que apita ao se afastar: o som fica mais grave porque as"
            " ondas sonoras se esticam. Na astronomia, utilizamos essa analogia"
            " intuitiva para compreender como a luz de galáxias distantes se"
            " altera ao viajar pelo espaço."
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
                    "1. Qual metodologia instrumental foi adotada por Edwin"
                    " Hubble para examinar a radiação luminosa dos confins"
                    " cósmicos?"
                ),
                "opcoes": [
                    ("Investigações espectroscópicas de alta precisão."),
                    ("Medições diretas de campo magnético planetário."),
                    ("Cálculos de densidade atmosférica estelar."),
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
                    "2. Como a astrofísica define o fenômeno de deslocamento"
                    " das linhas espectrais luminosas em direção a faixas mais"
                    " longas?"
                ),
                "opcoes": [
                    ("Redshift (desvio para o vermelho)."),
                    ("Compressão cromática azulada."),
                    ("Polarização de vácuo quântico."),
                    ("Refração de prisma estelar."),
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
                    "3. Qual era a armadilha conceitual em que observadores"
                    " desatentos costumavam cair ao analisar o afastamento"
                    " galáctico?"
                ),
                "opcoes": [
                    (
                        "Supor que as galáxias corriam como projéteis velozes"
                        " dentro de um palco estático."
                    ),
                    (
                        "Acreditar que os aglomerados estelares estavam"
                        " evaporando em calor."
                    ),
                    (
                        "Imaginar que a Terra encontrava-se imóvel no centro"
                        " exato de tudo."
                    ),
                    (
                        "Considerar que a luz perdia sua velocidade natural ao"
                        " cruzar o vácuo."
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
                    "4. De acordo com a Relatividade Geral, qual é a causa"
                    " geométrica real do afastamento mútuo das galáxias?"
                ),
                "opcoes": [
                    (
                        "O estiramento métrico contínuo do próprio tecido do"
                        " espaço-tempo."
                    ),
                    ("A ação de jatos de plasma soprados por supernovas."),
                    ("A colisão de linhas magnéticas intergalácticas."),
                    ("A rotação global do cosmo em torno de um eixo fixo."),
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
                    "5. Que proporção métrica o texto estabelece entre a"
                    " velocidade de afastamento e a posição espacial dos"
                    " aglomerados?"
                ),
                "opcoes": [
                    (
                        "A velocidade de afastamento é diretamente proporcional"
                        " à distância que os separa."
                    ),
                    (
                        "As galáxias mais próximas se afastam muito mais rápido"
                        " que as distantes."
                    ),
                    (
                        "Não existe nenhuma relação matemática entre distância"
                        " e velocidade."
                    ),
                    (
                        "A velocidade é inversamente proporcional ao brilho"
                        " visível do núcleo."
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
                    "6. Qual artifício distorcido Death Tahim tentou aplicar"
                    " sobre os relatórios de Hubble?"
                ),
                "opcoes": [
                    (
                        "Argumentar que o universo sofria um processo de"
                        " colapso retrógrado interno."
                    ),
                    (
                        "Afirmar que o desvio para o vermelho era causado por"
                        " poluição gasosa."
                    ),
                    (
                        "Ocultar a existência de qualquer aglomerado além da"
                        " Via Láctea."
                    ),
                    (
                        "Provar que o tempo passava mais devagar unicamente na"
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
                    "7. Analisando profundamente a física envolvida, por que a"
                    " expansão métrica do espaço supera a visão de movimento"
                    " mecânico simples?"
                ),
                "opcoes": [
                    (
                        "Porque evidencia que o palco onde a matéria habita é"
                        " flexível e dinâmico, e não um cenário rígido."
                    ),
                    (
                        "Porque prova que os fótons de luz ganham peso ao"
                        " viajarem pelo vácuo."
                    ),
                    (
                        "Porque elimina a necessidade de considerar a gravidade"
                        " cósmica."
                    ),
                    (
                        "Porque valida a existência de pontos de coordenadas"
                        " absolutas fixas."
                    ),
                ],
                "correta": (
                    "Porque evidencia que o palco onde a matéria habita é"
                    " flexível e dinâmico, e não um cenário rígido."
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
                    "8. Em qual período temporal específico as investigações"
                    " espectroscópicas de Edwin Hubble ganharam notoriedade"
                    " mundial?"
                ),
                "opcoes": [
                    ("Na década de 1920."),
                    ("Nos anos de 1850 durante a revolução industrial."),
                    ("No início do século XXI."),
                    ("Na transição para o Renascimento."),
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
            "🧠 **Ativação de Conhecimento Prévio (Subsunçor):** Pense na"
            " gravidade que mantém você preso ao solo e como uma mola reage"
            " ao ser esticada ou comprimida. Na cosmologia avançada, lidamos"
            " com componentes invisíveis que atuam como forças de coesão ou"
            " como motores de aceleração cósmica."
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
                    "1. Que anomalia dinâmica os astrofísicos detectaram ao"
                    " examinar as curvas de rotação das estrelas nas bordas"
                    " galácticas?"
                ),
                "opcoes": [
                    (
                        "As estrelas periféricas giravam com velocidade muito"
                        " acima da sustentável pela massa visível."
                    ),
                    ("As bordas galácticas encontravam-se totalmente paradas."),
                    ("O movimento estelar girava no sentido opuesto ao núcleo."),
                    (
                        "As estrelas das bordas emitiam unicamente raios gama"
                        " intensos."
                    ),
                ],
                "correta": (
                    "As estrelas periféricas giravam com velocidade muito acima"
                    " da sustentável pela massa visível."
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
                    "2. Qual entidade teórica foi proposta para explicar a"
                    " existência da gravidade extra que impede a dispersão das"
                    " estrelas periféricas?"
                ),
                "opcoes": [
                    ("A presença de um vasto halo de Matéria Escura."),
                    ("A existência de um buraco negro maciço na borda externa."),
                    ("A fricção gerada por ventos de plasma interestelar."),
                    ("O reflexo da luz de galáxias vizinhas distantes."),
                ],
                "correta": ("A presença de um vasto halo de Matéria Escura."),
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
                    "3. Qual é o papel funcional primordial exercido pela"
                    " Matéria Escura na arquitetura cósmica?"
                ),
                "opcoes": [
                    (
                        "Atuar coesivamente através da atração gravitacional,"
                        " unindo e estruturando as galáxias."
                    ),
                    (
                        "Repelir violentamente as estrelas para acelerar a"
                        " expansão."
                    ),
                    ("Absorver toda a luz emitida pelos núcleos estelares."),
                    (
                        "Gerar campos magnéticos que impedem colisões entre"
                        " astros."
                    ),
                ],
                "correta": (
                    "Atuar coesivamente através da atração gravitacional,"
                    " unindo e estruturando as galáxias."
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
                    "4. O que as observações recentes de supernovas distantes"
                    " revelaram a respeito do ritmo da expansão cósmica?"
                ),
                "opcoes": [
                    (
                        "Que a expansão não está freando, mas sim em contínuo"
                        " processo de aceleração."
                    ),
                    ("Que o universo entrou em colapso gravitacional total."),
                    ("Que a velocidade de expansão zerou completamente."),
                    ("Que o cosmo oscila expand
       
