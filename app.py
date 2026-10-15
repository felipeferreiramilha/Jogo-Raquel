import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Investigação Cósmica: Cadeia de Pistas & Death Tahim",
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
    .pista-box {
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
# BANCO DE AULAS COM CADEIA INVESTIGATIVA RAMIFICADA
# =========================================================================

CASOS_INVESTIGACAO = [
    {
        "id": 1,
        "titulo": (
            "Aula 1: A Investigação do Átomo Primitivo e a Queda do Dogma"
            " Estático"
        ),
        "contexto_inicial": (
            "🔍 **Pista Inicial da Investigação:** Os registros de Georges"
            " Lemaître foram corrompidos. Para avançar sem cair na armadilha de"
            " Death Tahim, você precisa seguir a cadeia exata de deduções"
            " lógicas baseadas no relatório a seguir."
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
            "🎥 **Vídeo Recomendado para Investigação:** Assista no YouTube a"
            " documentários sobre *"
            " https://www.youtube.com/results?search_query=Georges+Lemaitre+Big+Bang+Cosmologia"
            " * (Pesquise por: *Georges Lemaître e a Origem do Big Bang*)."
        ),
        # Cadeia de 7 perguntas encadeadas (a resposta anterior afeta a trilha de investigação)
        "cadeia_questoes": [
            {
                "fase": 1,
                "enunciado": (
                    "Fase 1 - Qual era a convicção generalizada que a"
                    " humanidade mantinha sobre a estrutura global do cosmo"
                    " antes do século XX?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Você desviou para"
                    " uma teoria paralela! Lembre-se: antes da física"
                    " moderna, as pessoas achavam que o céu nunca mudava."
                ),
            },
            {
                "fase": 2,
                "enunciado": (
                    "Fase 2 - Partindo dessa pista, qual arcabouço matemático"
                    " revolucionou a forma de calcular a gravidade e permitiu"
                    " modelar o cosmo?"
                ),
                "opcoes": [
                    (
                        "Forças eletromagnéticas geradas por núcleos densos de"
                        " ferro."
                    ),
                    (
                        "Teoria da Relatividade Geral de Einstein (curvatura do"
                        " espaço-tempo)."
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
                    "Teoria da Relatividade Geral de Einstein (curvatura do"
                    " espaço-tempo)."
                ),
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Volte ao início do"
                    " texto: qual é a famosa teoria de Einstein citada que"
                    " mexeu com a gravidade?"
                ),
            },
            {
                "enunciado": (
                    "Fase 3 - Analisando os cálculos de Lemaître baseados nessa"
                    " teoria, o que as equações de campo exigiam do sistema"
                    " cósmico?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Lemaître percebeu"
                    " que o cosmo não ficava parado nas equações. Ou ele"
                    " crescia, ou encolhia!"
                ),
            },
            {
                "fase": 4,
                "enunciado": (
                    "Fase 4 - Projetando o filme do tempo para trás, como"
                    " Lemaître batizou o ponto de densidade quase infinita?"
                ),
                "opcoes": [
                    ("Semente de Vácuo Quântico."),
                    ("Átomo Primitivo."),
                    ("Núcleo de Entropia Zero."),
                    ("Plasmocentro Primordial."),
                ],
                "correta": ("Átomo Primitivo."),
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Busque no relatório"
                    " o termo exato que ele usou para concentrar toda a massa"
                    " e energia."
                ),
            },
            {
                "fase": 5,
                "enunciado": (
                    "Fase 5 - Com a descompressão explosiva desse núcleo,"
                    " quais dimensões reais foram deflagradas na realidade?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Lembre-se que o"
                    " evento criou não só a matéria, mas a própria geometria da"
                    " realidade."
                ),
            },
            {
                "fase": 6,
                "enunciado": (
                    "Fase 6 - Qual era o propósito central das artimanhas"
                    " aplicadas por Death Tahim nesta fase?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** O vilão queria que"
                    " as pessoas continuassem acreditando em quê?"
                ),
            },
            {
                "enunciado": (
                    "Fase 7 - Concluindo a cadeia investigativa, qual foi o"
                    " impacto epistemológico final dessa descoberta?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** A grande guinada"
                    " foi entender que o universo teve um começo ativo e"
                    " dinâmico!"
                ),
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Agente, siga cada pista em cadeia!"
            " Uma resposta correta puxa a próxima evidência lógica do"
            " relatório.'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'Cada passo errado em minha cadeia de"
            " mentiras te afunda mais no escuro! Você precisa de pelo menos 4"
            " acertos para sair daqui vivo!'"
        ),
    },
    {
        "id": 2,
        "titulo": (
            "Aula 2: A Investigação do Espaço em Expansão e o Redshift"
        ),
        "contexto_inicial": (
            "🔍 **Pista Inicial da Investigação:** Os telescópios captaram"
            " sinais espectrais misteriosos. Siga a cadeia investigativa de"
            " Edwin Hubble para desvendar o desvio da luz."
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
            "🎥 **Vídeo Recomendado para Investigação:** Assista no YouTube a"
            " vídeos educacionais sobre *"
            " https://www.youtube.com/results?search_query=Edwin+Hubble+Redshift+Expansao+do+Universo"
            " * (Pesquise por: *Edwin Hubble, Redshift e a Expansão do Universo*)."
        ),
        "cadeia_questoes": [
            {
                "fase": 1,
                "enunciado": (
                    "Fase 1 - Qual foi a metodologia instrumental aplicada por"
                    " Edwin Hubble nas observações dos confins cósmicos?"
                ),
                "opcoes": [
                    ("Medições diretas de campo magnético em planetas."),
                    ("Investigações espectroscópicas de alta precisão."),
                    ("Cálculos estatísticos de densidade atmosférica."),
                    ("Análise de reflexão de radar em meteoroides."),
                ],
                "correta": ("Investigações espectroscópicas de alta precisão."),
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Releia o texto; ele"
                    " fala sobre o espectro da radiação luminosa."
                ),
            },
            {
                "fase": 2,
                "enunciado": (
                    "Fase 2 - Partindo dessa análise espectroscópica, como a"
                    " astrofísica batizou o deslocamento da luz para faixas"
                    " mais longas?"
                ),
                "opcoes": [
                    ("Compressão cromática azulada de feixes."),
                    ("Polarização quântica de vácuo interestelar."),
                    ("Redshift (desvio para o vermelho)."),
                    ("Refração direta em prisma estelar."),
                ],
                "correta": ("Redshift (desvio para o vermelho)."),
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** O termo em inglês"
                    " aponta para a cor vermelha do espectro visível."
                ),
            },
            {
                "fase": 3,
                "enunciado": (
                    "Fase 3 - Qual equívoco ingênuo observadores apressados"
                    " cometiam ao notar esse afastamento luminoso?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Eles achavam que as"
                    " galáxias corriam como carros em uma estrada parada."
                ),
            },
            {
                "fase": 4,
                "enunciado": (
                    "Fase 4 - Em contraste com esse erro, qual é a verdadeira"
                    " causa geométrica do afastamento galáctico segundo a"
                    " Relatividade?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** O que realmente se"
                    " estica ativamente é o próprio espaço entre os astros."
                ),
            },
            {
                "fase": 5,
                "enunciado": (
                    "Fase 5 - Que proporção métrica o relatório define entre a"
                    " velocidade de fuga e a localização espacial?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Quanto mais longe"
                    " está a galáxia, mais rápido ela parece se afastar."
                ),
            },
            {
                "fase": 6,
                "enunciado": (
                    "Fase 6 - Como Death Tahim tentou distorcer as"
                    " investigações de Hubble?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** O vilão tentou"
                    " inverter a expansão dizendo que o cosmo encolhia."
                ),
            },
            {
                "fase": 7,
                "enunciado": (
                    "Fase 7 - Concluindo a cadeia, por que a expansão métrica"
                    " supera a visão de movimento balístico simples?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** O recipiente do"
                    " universo (o espaço) cresce e se flexiona ativamente."
                ),
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Continue firme na cadeia de pistas da"
            " expansão! O tecido do espaço é a chave para vencer.'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'O tecido do espaço é frágil... Erre"
            " a cadeia lógica e afundarei suas deduções!'"
        ),
    },
    {
        "id": 3,
        "titulo": (
            "Aula 3: A Investigação Oculta da Matéria Escura e da Energia Escura"
        ),
        "contexto_inicial": (
            "🔍 **Pista Inicial da Investigação:** Forças invisíveis agem nas"
            " bordas galácticas e na expansão. Siga a cadeia lógica final para"
            " decodificar o mistério."
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
            "🎥 **Vídeo Recomendado para Investigação:** Assista no YouTube a"
            " vídeos científicos sobre *"
            " https://www.youtube.com/results?search_query=Materia+Escura+e+Energia+Escura+Cosmologia"
            " * (Pesquise por: *Matéria Escura e Energia Escura explicadas*)."
        ),
        "cadeia_questoes": [
            {
                "fase": 1,
                "enunciado": (
                    "Fase 1 - O que os astrofísicos detectaram nas curvas de"
                    " rotação estelar nas bordas das galáxias espirais?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** As estrelas da"
                    " periferia giravam rápido demais para a massa que"
                    " enxergamos."
                ),
            },
            {
                "fase": 2,
                "enunciado": (
                    "Fase 2 - Qual entidade teórica foi proposta para fornecer"
                    " a gravidade extra que impedia a fuga dessas estrelas?"
                ),
                "opcoes": [
                    ("Buraco negro supermassivo na borda externa."),
                    ("Fricção gerada por ventos de plasma interestelar."),
                    ("Vasto halo de Matéria Escura."),
                    ("Reflexo luminescente de galáxias vizinhas."),
                ],
                "correta": ("Vasto halo de Matéria Escura."),
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** A massa invisível"
                    " batizada para resolver isso foi a matéria escura."
                ),
            },
            {
                "fase": 3,
                "enunciado": (
                    "Fase 3 - Qual é a função primordial exercida pela Matéria"
                    " Escura na arquitetura cósmica?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Lembre-se que ela"
                    " funciona como uma cola gravitacional que une as"
                    " estruturas."
                ),
            },
            {
                "fase": 4,
                "enunciado": (
                    "Fase 4 - O que as supernovas distantes revelaram sobre o"
                    " ritmo da expansão cósmica em grande escala?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** A expansão não está"
                    " freando, ela está acelerando cada vez mais."
                ),
            },
            {
                "fase": 5,
                "enunciado": (
                    "Fase 5 - Qual componente teórico impulsiona essa"
                    " aceleração repulsiva no universo?"
                ),
                "opcoes": [
                    ("Pressão de radiação fóssil primária."),
                    ("Energia Escura."),
                    ("Campo magnético primordial de fundo."),
                    ("Entropia térmica absoluta."),
                ],
                "correta": ("Energia Escura."),
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** A pressão de vácuo"
                    " que empurra o cosmo chama-se energia escura."
                ),
            },
            {
                "fase": 6,
                "enunciado": (
                    "Fase 6 - Como Death Tahim explorou conceitualmente estes"
                    " dois grandes enigmas?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Ele fingiu ser o"
                    " senhor do caos para forçar testes rigorosos em nossa"
                    " mente."
                ),
            },
            {
                "fase": 7,
                "enunciado": (
                    "Fase 7 - Concluindo a cadeia investigativa final, qual é"
                    " o balanço dinâmico promovido por ambas no cosmos?"
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
                "dica_recuperacao": (
                    "💡 **Pista de Recuperação (Raquel):** Uma puxa para"
                    " formar estruturas (matéria) e a outra empurra o espaço"
                    " (energia)."
                ),
            },
        ],
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Esta é a última cadeia de pistas! Conecte"
            " a matéria e a energia escura para desvendar o segredo final.'"
        ),
        "comentario_makarius": (
            "😈 **Death Tahim sussurra:** 'Minhas sombras invisíveis são o"
            " teste supremo. Prove que sua cadeia lógica é impecável!'"
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
if "indice_fase_cadeia" not in st.session_state:
  st.session_state.indice_fase_cadeia = 0
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
    "<h1>🌌 Investigação Cósmica: Cadeia de Pistas & Death Tahim</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Siga a cadeia investigativa de"
    " pistas encadeadas. Obtenha ao menos 4 acertos por aula para avançar ou"
    " receba uma nova vida de Raquel Ferreira!</p>",
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
        "Inicie a jornada com perguntas em cadeia lógica, recuperação por"
        " pistas e o desfecho épico com Death Tahim!"
    )
    if st.button("Entrar como Agente"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.indice_fase_cadeia = 0
      st.session_state.acertos_caso_atual = 0
      st.session_state.acertos_totais = 0
      st.session_state.derrotado = False
      st.session_state.erros_cometidos = []
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
    if st.button("🚀 Iniciar Cadeia Investigativa"):
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
            <h2 style='color:#ff3333; margin-top:0;'>😈 Death Tahim Desestruturou Sua Cadeia de Pistas!</h2>
            <p style='font-size:16px;'><b>Death Tahim gargalha com sua voz profunda:</b><br>
            <i>"Você obteve apenas <b>{acertos} de 7 acertos</b> nesta aula! Sua linha de raciocínio falhou na cadeia investigativa. O conhecimento cósmico rejeita deduções defeituosas!"</i></p>
        </div>
        <div class='raquel-box'>
            <h3 style='color:#00ffff; margin-top:0;'>👧 Raquel Ferreira Concede uma Nova Vida!</h3>
            <p style='font-size:16px;'><b>Raquel segura sua mão e diz com firmeza:</b><br>
            <i>"Não desista, Agente <b>{nome}</b>! Eu estou lhe concedendo <b>MAIS UMA VIDA</b>. Revise a cadeia de pistas, preste atenção nas dicas de recuperação e enfrente Death Tahim novamente nesta aula. Você consegue atingir o mínimo de 4 acertos!"</i></p>
        </div>
        """.format(
            acertos=st.session_state.acertos_caso_atual,
            nome=st.session_state.nome_usuario,
        ),
        unsafe_allow_html=True,
    )

    if st.button("❤️ Usar Nova Vida e Reiniciar Esta Aula"):
      st.session_state.derrotado = False
      st.session_state.indice_fase_cadeia = 0
      st.session_state.acertos_caso_atual = 0
      st.rerun()

    st.stop()

  # -------------------------------------------------------------------------
  # ETAPA DE AULAS COM CADEIA DE PERGUNTAS
  # -------------------------------------------------------------------------
  if st.session_state.etapa_agente == "investigacao":
    idx = st.session_state.indice_caso
    total_casos = len(CASOS_INVESTIGACAO)

    if idx < total_casos:
      caso_atual = CASOS_INVESTIGACAO[idx]
      cadeia_fases = caso_atual["cadeia_questoes"]
      total_fases = len(cadeia_fases)
      fase_idx = st.session_state.indice_fase_cadeia

      if fase_idx < total_fases:
        fase_atual = cadeia_fases[fase_idx]

        st.markdown(
            f"<h2>📁 {caso_atual['titulo']} (Fase {fase_idx + 1} de"
            f" {total_fases})</h2>",
            unsafe_allow_html=True,
        )
        st.write(
            f"🕵️‍♂️ **Agente:** {st.session_state.nome_usuario} | **Aula Atual:**"
            f" {idx + 1} de {total_casos} | **Acertos nesta Aula:**"
            f" {st.session_state.acertos_caso_atual} (Mínimo para passar: 4)"
        )
        st.progress((fase_idx) / total_fases)

        # Contexto da Pista e Texto Base
        st.markdown(
            f"<div class='pista-box'>{caso_atual['contexto_inicial']}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div class='texto-base-box'>{caso_atual['texto_base']}</div>",
            unsafe_allow_html=True,
        )
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
              f"<div class='pergunta-box'><h4>{fase_atual['enunciado']}</h4></div>",
              unsafe_allow_html=True,
          )

          escolha_agente = st.radio(
              "Siga a cadeia investigativa correta:",
              fase_atual["opcoes"],
              key=f"radio_cadeia_{idx}_{fase_idx}",
          )

          st.markdown("<br>", unsafe_allow_html=True)
          if st.button("🔒 Validar Pista na Cadeia"):
            if escolha_agente == fase_atual["correta"]:
              st.session_state.acertos_caso_atual += 1
              st.session_state.acertos_totais += 1
              st.success(
                  "✨ Pista correta! Cadeia lógica avançada com sucesso."
              )
            else:
              st.error("❌ Pista incorreta! Sua cadeia lógica foi desviada.")
              st.info(f"{fase_atual['dica_recuperacao']}")
              erro_info = (
                  f"**{caso_atual['titulo']} (Fase {fase_idx + 1})**: Escolheu"
                  f" *'{escolha_agente[:35]}...'* em vez de"
                  f" *'{fase_atual['correta'][:35]}...'*."
              )
              if erro_info not in st.session_state.erros_cometidos:
                st.session_state.erros_cometidos.append(erro_info)

            st.session_state.indice_fase_cadeia += 1
            st.rerun()

      else:
        # Fim das fases da Aula Atual -> Verifica a Média de Acertos
        if st.session_state.acertos_caso_atual < 4:
          st.session_state.derrotado = True
          st.rerun()
        else:
          st.success(
              f"🎉 Excelente! Você obteve {st.session_state.acertos_caso_atual}"
              " de 7 acertos na cadeia e concluiu esta aula!"
          )
          st.session_state.indice_caso += 1
          st.session_state.indice_fase_cadeia = 0
          st.session_state.acertos_caso_atual = 0

          if st.session_state.indice_caso >= total_casos:
            st.session_state.etapa_agente = "avaliacao_final"
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

    if tot_acertos == 21:
      titulo_universo = "🌌 Conhecimento Absoluto e Supremo do Universo"
      desc_titulo = (
          "Você completou a cadeia lógica de todas as aulas com perfeição! Seu"
          " domínio é absoluto."
      )
    elif tot_acertos >= 18:
      titulo_universo = "🔮 Conhecimento das Forças Invisíveis Cósmicas"
      desc_titulo = (
          "Você obteve uma pontuação espetacular e dominou a cadeia de"
          " investigações invisíveis."
      )
    elif tot_acertos >= 15:
      titulo_universo = "📐 Conhecimento da Geometria do Espaço-Tempo"
      desc_titulo = (
          "Sua média prova que você compreende a curvatura e o encadeamento da"
          " expansão cósmica."
      )
    else:
      titulo_universo = "🔭 Conhecimento do Universo Observável"
      desc_titulo = (
          "Com a média garantida de acertos, você concluiu a jornada"
          " investigativa com honra."
      )

    st.markdown(
        """
        <div style='background-color: #0b1a2e; border: 2px solid #00ffff; padding: 22px; border-radius: 12px; margin-bottom: 20px;'>
            <h3 style='color: #00ffff; margin-top:0;'>🌌 O Desfecho: A Aparição de Death Tahim</h3>
            <p>Parabéns, Agente <b>{nome}</b>! Você concluiu a cadeia de pistas de todas as 3 Aulas Investigativas obtendo um total de <b>{tot_acertos} de 21 acertos possíveis</b>.</p>
            <p>As portas da câmara principal se abrem com um som metálico profundo. Das sombras surge <b>Death Tahim</b>, trajando seu imponente manto preto estilo <i>Darth Vader</i> de <i>Star Wars</i>, com sua respiração mecânica ecoando pelo ambiente. Ao lado dele, <b>Raquel Ferreira</b> sorri orgulhosa.</p>
            <p style='color: #ffcc00; font-style: italic; font-size: 16px;'>
            "Impressionante...", diz Death Tahim com sua voz profunda, retirando o capacete escuro e revelando um olhar de absoluto respeito. "Você navegou pela minha cadeia de armadilhas lógicas, recuperou-se dos desvios e provou seu valor intelectual."
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

    st.subheader("🧠 Relatório da Cadeia Investigativa e Erros Mapeados")
    if len(st.session_state.erros_cometidos) == 0:
      st.success(
          "🌟 Espantoso! Você seguiu a cadeia lógica sem errar nenhuma pista!"
      )
    else:
      st.warning(
          "⚠️ Durante a investigação em cadeia, as seguintes pistas exigiram"
          " recuperação:"
      )
      for err in st.session_state.erros_cometidos:
        st.markdown(f"- {err}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("✍️ Relatório Final de Síntese")
    st.write(
        "Para consolidar sua conquista, redija abaixo com suas próprias palavras"
        " o que você aprendeu sobre a evolução do universo ao longo desta cadeia"
        " investigativa:"
    )

    conclusao = st.text_area(
        "Escreva sua síntese investigativa final:",
        placeholder=(
            "Descreva como a cadeia de pistas revelou a expansão do cosmo..."
        ),
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
    if st.button("🔄 Realizar Nova Investigação em Cadeia"):
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.indice_fase_cadeia = 0
      st.session_state.acertos_caso_atual = 0
      st.session_state.acertos_totais = 0
      st.session_state.derrotado = False
      st.session_state.erros_cometidos = []
      st.session_state.nome_usuario = ""
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
      st.info("Nenhum agente concluiu a cadeia ainda.")
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
