import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Investigação Cósmica: A Jornada das Aulas de Death Tahim",
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
    .derrota-box {
        background-color: #2b0000;
        border: 2px solid #ff0000;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

# =========================================================================
# BANCO DE AULAS/CASOS COM TEXTOS EXPANDIDOS E BANCO DE QUESTÕES
# =========================================================================

CASOS_INVESTIGACAO = [
    {
        "id": 1,
        "titulo": (
            "Aula 1: O Nascimento do Cosmos e a Queda do Dogma Estático"
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
            " humanidade algemada à illusions da estagnação perpétua."
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
                        " Via Láctea."
                    ),
                ],
                "correta": (
                    "Imutabilidade perpétua de um cenário cósmico visto como"
                    " perene e estagnado."
                ),
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
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Agente, leia cada linha com máxima"
            " atenção. O texto traz detalhes finos sobre a transição do"
            " pensamento estático para o dinâmico!'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'A eternidade estagnada é o meu"
            " domínio... Você precisará de pelo menos 4 acertos para sobreviver"
            " a esta aula!'"
        ),
    },
    {
        "id": 2,
        "titulo": "Aula 2: A Grande Expansão do Espaço-Tempo e o Redshift",
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
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Lembre-se da nossa dinâmica com o"
            " balão de borracha! O estiramento afeta todos os pontos de forma"
            " igualitária.'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'O tecido do espaço é maleável e"
            " frágil... Mantenha a média de 4 acertos ou caia perante minhas"
            " ilusões!'"
        ),
    },
    {
        "id": 3,
        "titulo": (
            "Aula 3: O Mistério Oculto da Matéria Escura e da Energia Escura"
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
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Entenda bem o papel de cada força"
            " invisível: uma puxa para formar galáxias e a outra empurra o"
            " espaço cósmico!'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'Minhas sombras invisíveis são o"
            " teste supremo. Esta é a última aula!'"
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
if "acertos_caso_atual" not in st.session_state:
  st.session_state.acertos_caso_atual = 0
if "acertos_totais" not in st.session_state:
  st.session_state.acertos_totais = 0
if "erros_cometidos" not in st.session_state:
  st.session_state.erros_cometidos = []
if "nome_usuario" not in st.session_state:
  st.session_state.nome_usuario = ""
if "derrotado" not in st.session_state:
  st.session_state.derrotado = False
if "ranking" not in st.session_state:
  st.session_state.ranking = [
      {
          "nome": "Agente Felipe",
          "status": "Conhecimento Absoluto e Supremo (21/21)",
          "pontos": 21,
      },
      {
          "nome": "Raquel Ferreira (Heroína)",
          "status": "Comandante Cognitiva (21/21)",
          "pontos": 21,
      },
  ]
if "logado_gerente" not in st.session_state:
  st.session_state.logado_gerente = False

# Título Principal
st.markdown(
    "<h1>🌌 Investigação Cósmica: As Aulas de Death Tahim</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Obtenha no mínimo 4 acertos por"
    " aula para avançar. Se falhar, Raquel lhe dará mais uma vida para enfrentar"
    " Death Tahim novamente!</p>",
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
        "Inicie as aulas investigativas com 7 questões por aula, sistema de"
        " vidas com a heroína Raquel Ferreira e conquiste o Conhecimento do"
        " Universo!"
    )
    if st.button("Entrar como Agente"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.indice_questao_caso = 0
      st.session_state.acertos_caso_atual = 0
      st.session_state.acertos_totais = 0
      st.session_state.derrotado = False
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
        " inspecionar o ranking e os relatórios."
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
    if st.button("🚀 Iniciar Aulas Investigativas"):
      if nome_input.strip() == "":
        st.warning("Por favor, digite um nome válido.")
      else:
        st.session_state.nome_usuario = nome_input.strip()
        st.rerun()
    st.stop()

  # -------------------------------------------------------------------------
  # TELA DE DERROTA E CONCESSÃO DE NOVA VIDA POR RAQUEL
  # -------------------------------------------------------------------------
  if st.session_state.derrotado:
    st.markdown(
        """
        <div class='derrota-box'>
            <h2 style='color:#ff3333; margin-top:0;'>😈 Death Tahim Derrotou Você!</h2>
            <p style='font-size:16px;'><b>Death Tahim gargalha com sua voz profunda:</b><br>
            <i>"Você fez apenas <b>{acertos} de 7 acertos</b> nesta aula! Suas estruturas conceituais são muito frágeis e incapazes de sustentar a verdade do cosmos. O conhecimento não pertence aos fracos!"</i></p>
        </div>
        <div class='raquel-box'>
            <h3 style='color:#00ffff; margin-top:0;'>👧 Raquel Ferreira Concede uma Nova Vida!</h3>
            <p style='font-size:16px;'><b>Raquel segura sua mão e diz com firmeza:</b><br>
            <i>"Não desista, Agente <b>{nome}</b>! Eu estou lhe concedendo <b>MAIS UMA VIDA</b>. Releia o texto base com atenção, pesquise o vídeo recomendado e enfrente Death Tahim novamente nesta aula. Eu sei que você consegue atingir o mínimo de 4 acertos!"</i></p>
        </div>
        """.format(
            acertos=st.session_state.acertos_caso_atual,
            nome=st.session_state.nome_usuario,
        ),
        unsafe_allow_html=True,
    )

    if st.button("❤️ Usar Nova Vida e Reiniciar Esta Aula"):
      st.session_state.derrotado = False
      st.session_state.indice_questao_caso = 0
      st.session_state.acertos_caso_atual = 0
      caso_atual = CASOS_INVESTIGACAO[st.session_state.indice_caso]
      st.session_state.questoes_sorteadas_caso = random.sample(
          caso_atual["banco_questoes"],
          min(7, len(caso_atual["banco_questoes"])),
      )
      st.rerun()

    st.stop()

  # -------------------------------------------------------------------------
  # ETAPA DE AULAS INVESTIGATIVAS
  # -------------------------------------------------------------------------
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
            f"🕵️‍♂️ **Agente:** {st.session_state.nome_usuario} | **Aula Atual:**"
            f" {idx + 1} de {total_casos} | **Acertos nesta Aula:**"
            f" {st.session_state.acertos_caso_atual} (Mínimo para passar: 4)"
        )
        st.progress((q_idx) / total_q)

        # 1. Ativação de Conhecimento Prévio
        st.markdown(
            f"<div class='subsunsor-box'>{caso_atual['subsunsor_previo']}</div>",
            unsafe_allow_html=True,
        )

        # 2. Texto Base
        st.markdown(
            f"<div class='texto-base-box'>{caso_atual['texto_base']}</div>",
            unsafe_allow_html=True,
        )

        # 3. Indicação de Vídeo
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
          st.markdown(
              f"<div class='pergunta-box'><h4>{q_atual['enunciado']}</h4></div>",
              unsafe_allow_html=True,
          )

          escolha_agente = st.radio(
              "Selecione a dedução investigativa correta:",
              q_atual["opcoes"],
              key=f"radio_aula_{idx}_{q_idx}",
          )

          st.markdown("<br>", unsafe_allow_html=True)
          if st.button("🔒 Validar Resposta e Avançar"):
            if escolha_agente == q_atual["correta"]:
              st.session_state.acertos_caso_atual += 1
              st.session_state.acertos_totais += 1
              st.success("✨ Resposta Correta! Ponto registrado.")
            else:
              st.error("❌ Resposta Incorreta!")
              erro_info = (
                  f"**{caso_atual['titulo']} (Questão {q_idx + 1})**: Escolheu"
                  f" *'{escolha_agente[:35]}...'* em vez de"
                  f" *'{q_atual['correta'][:35]}...'*."
              )
              if erro_info not in st.session_state.erros_cometidos:
                st.session_state.erros_cometidos.append(erro_info)

            st.session_state.indice_questao_caso += 1
            st.rerun()

      else:
        # Fim das 7 questões da Aula Atual -> Verifica a Média de Acertos
        if st.session_state.acertos_caso_atual < 4:
          # DERROTA: Menos de 4 acertos -> Aciona Death Tahim e concede nova vida com Raquel
          st.session_state.derrotado = True
          st.rerun()
        else:
          # APROVADO NA AULA -> Avança para a próxima aula
          st.success(
              f"🎉 Excelente! Você obteve {st.session_state.acertos_caso_atual}"
              " de 7 acertos e superou esta aula!"
          )
          st.session_state.indice_caso += 1
          st.session_state.indice_questao_caso = 0
          st.session_state.acertos_caso_atual = 0
          st.session_state.questoes_sorteadas_caso = []

          if st.session_state.indice_caso < total_casos:
            proximo_caso = CASOS_INVESTIGACAO[st.session_state.indice_caso]
            st.session_state.questoes_sorteadas_caso = random.sample(
                proximo_caso["banco_questoes"],
                min(7, len(proximo_caso["banco_questoes"])),
            )
          st.rerun()

    else:
      st.session_state.etapa_agente = "avaliacao_final"
      st.rerun()

  # -------------------------------------------------------------------------
  # ETAPA 3: AVALIAÇÃO FINAL & DESFECHO COM DEATH TAHIM (DARTH VADER)
  # -------------------------------------------------------------------------
  elif st.session_state.etapa_agente == "avaliacao_final":
    st.markdown(
        "<h2>📊 Avaliação Final & Concessão do Conhecimento do Universo</h2>",
        unsafe_allow_html=True,
    )

    tot_acertos = st.session_state.acertos_totais

    # Lógica de Concessão de Título por Média de Acertos
    if tot_acertos == 21:
      titulo_universo = "🌌 Conhecimento Absoluto e Supremo do Universo"
      desc_titulo = (
          "Você gabaritou todas as aulas! Seu domínio sobre o Big Bang,"
          " Redshift e Energia Escura é absoluto."
      )
    elif tot_acertos >= 18:
      titulo_universo = "🔮 Conhecimento das Forças Invisíveis Cósmicas"
      desc_titulo = (
          "Você obteve uma média espetacular (6 a 7 acertos por aula) e domina"
          " a física das forças invisíveis."
      )
    elif tot_acertos >= 15:
      titulo_universo = "📐 Conhecimento da Geometria do Espaço-Tempo"
      desc_titulo = (
          "Sua média de 5 acertos por aula prova que você compreende a"
          " curvatura e a expansão métrica do espaço."
      )
    else:
      titulo_universo = "🔭 Conhecimento do Universo Observável"
      desc_titulo = (
          "Com a média garantida de 4 acertos por aula, você conquistou o"
          " conhecimento fundamental sobre o cosmo."
      )

    st.markdown(
        """
        <div style='background-color: #0b1a2e; border: 2px solid #00ffff; padding: 22px; border-radius: 12px; margin-bottom: 20px;'>
            <h3 style='color: #00ffff; margin-top:0;'>🌌 O Desfecho: A Aparição de Death Tahim</h3>
            <p>Parabéns, Agente <b>{nome}</b>! Você concluiu todas as 3 Aulas Investigativas obtendo um total de <b>{tot_acertos} de 21 acertos possíveis</b>.</p>
            <p>As portas da câmara principal se abrem com um som metálico profundo. Das sombras surge <b>Death Tahim</b>, trajando seu imponente manto preto estilo <i>Darth Vader</i> de <i>Star Wars</i>, com sua respiração mecânica ecoando pelo ambiente. Ao lado dele, <b>Raquel Ferreira</b> sorri orgulhosa.</p>
            <p style='color: #ffcc00; font-style: italic; font-size: 16px;'>
            "Impressionante...", diz Death Tahim com sua voz profunda, retirando o capacete escuro e revelando um olhar de absoluto respeito. "Você superou as dificuldades, venceu as aulas e provou que possui determinação científica."
            </p>
            <p>Death Tahim ergue as mãos e lhe concede formalmente o título de:</p>
            <h2 style='color: #00ffff; text-align: center;'>🏆 {titulo_universo}</h2>
            <p style='text-align: center; font-style: italic;'>"{desc_titulo}"</p>
        </div>
        """.format(
            nome=st.session_state.nome_usuario,
            tot_acertos=tot_acertos,
            titulo_universo=titulo_universo,
            desc_titulo=desc_titulo,
        ),
        unsafe_allow_html=True,
    )

    st.subheader("🧠 Relatório de Desempenho e ErrosMapeados")
    if len(st.session_state.erros_cometidos) == 0:
      st.success(
          "🌟 Espantoso! Você não errou nenhuma questão ao longo das 3 aulas!"
      )
    else:
      st.warning(
          "⚠️ Durante as aulas, os seguintes pontos exigiram reanálise:"
      )
      for err in st.session_state.erros_cometidos:
        st.markdown(f"- {err}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("✍️ Relatório Final de Aprendizagem")
    st.write(
        "Para consolidar sua conquista, redija abaixo com suas próprias palavras"
        " o que você aprendeu sobre o universo ao longo destas 3 aulas:"
    )

    conclusao = st.text_area(
        "Escreva sua síntese investigativa final:",
        placeholder="Descreva o que aprendeu sobre a expansão do universo...",
    )

    if st.button("📤 Protocolar e Registrar no Ranking"):
      if not conclusao.strip():
        st.warning("Por favor, digite seu relatório para concluir.")
      else:
        st.session_state.ranking.append({
            "nome": st.session_state.nome_usuario,
            "status": f"{titulo_universo} ({tot_acertos}/21)",
            "pontos": tot_acertos,
        })
        st.session_state.ranking = sorted(
            st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
        )
        st.session_state.etapa_agente = "fim_sucesso"
        st.rerun()

  # -------------------------------------------------------------------------
  # ETAPA 4: TELA DE SUCESSO E RANKING
  # -------------------------------------------------------------------------
  elif st.session_state.etapa_agente == "fim_sucesso":
    st.success(
        "🎉 Jornada Concluída com Sucesso! Seu título foi registrado no"
        " Ranking Cósmico."
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
    if st.button("🔄 Realizar Nova Jornada (Questões Inéditas)"):
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.indice_questao_caso = 0
      st.session_state.acertos_caso_atual = 0
      st.session_state.acertos_totais = 0
      st.session_state.derrotado = False
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

    st.subheader("📊 Relatório de Agentes e Níveis Alcançados")
    if len(st.session_state.ranking) == 0:
      st.info("Nenhum agente concluiu as aulas ainda.")
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
        st.success("Ranking limpo com sucesso!")
        st.rerun()
    with col_g2:
      if st.button("🔒 Sair do Quartel-General"):
        st.session_state.logado_gerente = False
        st.session_state.modo = "menu"
        st.rerun()
