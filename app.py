import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Olimpíada de Cosmologia - Sequência Didática",
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
# BANCO DE QUESTÕES CONCEITUAIS PARA SEQUÊNCIA DIDÁTICA (COSMOLOGIA, NEWTON, BIG BANG, MATÉRIA ESCURA)
# =========================================================================

BANCO_BASICO = [
    {
        "pergunta": (
            "1. Na perspectiva histórica e conceitual da cosmologia, o que o"
            " modelo do 'Átomo Primitivo' de Georges Lemaître propôs inicialmente"
            " para a origem do universo?"
        ),
        "opcoes": [
            "Um estado estático eterno que sofreu uma expansão repentina devido a perturbações térmicas.",
            "A concentração de toda a matéria do universo em um único quantum superdenso que iniciou a expansão.",
            "Um universo cíclico que colapsa e renasce infinitamente sem ponto inicial.",
            "A criação contínua de matéria nos espaços vazios entre as galáxias.",
        ],
        "resposta_correta": (
            "A concentração de toda a matéria do universo em um único quantum"
            " superdenso que iniciou a expansão."
        ),
    },
    {
        "pergunta": (
            "2. Como a Lei de Hubble modificou a visão clássica de um universo"
            " estático predominante na época de Einstein?"
        ),
        "opcoes": [
            "Demonstrou que as estrelas da Via Láctea estão freando sua rotação.",
            "Comprovou que as galáxias distantes afastam-se umas das outras, indicando que o espaço está em expansão.",
            "Revelou que o universo possui um centro físico fixo de onde tudo se originou.",
            "Provou que a velocidade da luz diminui com a distância intergaláctica.",
        ],
        "resposta_correta": (
            "Comprovou que as galáxias distantes afastam-se umas das outras,"
            " indicando que o espaço está em expansão."
        ),
    },
    {
        "pergunta": (
            "3. O que representa a Radiação Cósmica de Fundo em Micro-ondas (CMB)"
            " no contexto do modelo do Big Bang?"
        ),
        "opcoes": [
            "O calor emitido por buracos negros supermassivos centrais.",
            "O eco térmico e eletromagnético remanescente do período em que o universo tornou-se transparente.",
            "A radiação ultravioleta gerada pelo atrito entre ventos estelares e o gás interestelar.",
            "O reflexo da luz das primeiras estrelas nas nuvens de poeira cósmica.",
        ],
        "resposta_correta": (
            "O eco térmico e eletromagnético remanescente do período em que o"
            " universo tornou-se transparente."
        ),
    },
    {
        "pergunta": (
            "4. Qual é o papel principal atribuído à Matéria Escura nas"
            " estruturas em grande escala do cosmos?"
        ),
        "opcoes": [
            "Acelerar a expansão do universo através de uma pressão negativarepulsiva.",
            "Fornecer a massa gravitacional adicional necessária para aglutinar e manter as galáxias coesas.",
            "Bloquear a radiação nociva emitida pelos núcleos galácticos ativos.",
            "Servir como combustível primário para a fusão nuclear nas anãs brancas.",
        ],
        "resposta_correta": (
            "Fornecer a massa gravitacional adicional necessária para aglutinar"
            " e manter as galáxias coesas."
        ),
    },
    {
        "pergunta": (
            "5. Por que a luz visível de estrelas e gás luminoso não é suficiente"
            " para explicar a rotação observada das galáxias espirais?"
        ),
        "opcoes": [
            "Porque a gravidade de Newton deixa de valer em distâncias galácticas.",
            "Porque a massa visível é muito menor do que a exigida gravitacionalmente para sustentar as altas velocidades periféricas.",
            "Porque o campo magnético intergaláctico desacelera as bordas das galáxias.",
            "Porque a expansão do universo empurra as estrelas para fora.",
        ],
        "resposta_correta": (
            "Porque a massa visível é muito menor do que a exigida"
            " gravitacionalmente para sustentar as altas velocidades"
            " periféricas."
        ),
    },
    {
        "pergunta": (
            "6. O que diferencia essencialmente a Matéria Escura da Energia"
            " Escura no modelo cosmológico padrão?"
        ),
        "opcoes": [
            "A Matéria Escura atrai gravitacionalmente aglutinando estruturas; a Energia Escura atua de forma repulsiva acelerando a expansão.",
            "A Matéria Escura emite raios X, enquanto a Energia Escura é totalmente invisível a qualquer espectro.",
            "A Matéria Escura localiza-se apenas no centro do Sistema Solar, enquanto a Energia Escura fica fora dele.",
            "Não há diferença física; são apenas nomenclaturas diferentes para o mesmo fenômeno quântico.",
        ],
        "resposta_correta": (
            "A Matéria Escura atrai gravitacionalmente aglutinando estruturas;"
            " a Energia Escura atua de forma repulsiva acelerando a expansão."
        ),
    },
    {
        "pergunta": (
            "7. No contexto de uma sequência didática sobre o Big Bang, qual é"
            " a importância de ensinar a Nucleossíntese Primordial?"
        ),
        "opcoes": [
            "Explicar como os planetas rochosos se condensaram a partir de poeira estelar.",
            "Demonstrar como a proporção cósmica de Hidrogênio e Hélio prevista teoricamente bate com as observações do universo.",
            "Comprovar que o universo teve origem em uma colisão entre galáxias ancestrais.",
            "Descrever a formação exclusiva de elementos pesados como o ouro e o urânio.",
        ],
        "resposta_correta": (
            "Demonstrar como a proporção cósmica de Hidrogênio e Hélio prevista"
            " teoricamente bate com as observações do universo."
        ),
    },
    {
        "pergunta": (
            "8. O que significa afirmar que o universo é homogêneo e isotrópico"
            " em grande escala?"
        ),
        "opcoes": [
            "Que ele possui exatamente a mesma temperatura em qualquer ponto microscópico.",
            "Que a distribuição de matéria é uniforme em grande escala (homogênea) e parece igual em todas as direções (isotrópica).",
            "Que todas as galáxias possuem o mesmo tamanho, formato e número exato de estrelas.",
            "Que o espaço não sofre alterações temporais nem gravitacionais.",
        ],
        "resposta_correta": (
            "Que a distribuição de matéria é uniforme em grande escala"
            " (homogênea) e parece igual em todas as direções (isotrópica)."
        ),
    },
]

BANCO_MEDIO = [
    {
        "pergunta": (
            "1. Como a Cosmologia Neo-Newtoniana (como os modelos de"
            " Milne-McCrea) consegue descrever a dinâmica da expansão cósmica"
            " sem recorrer de imediato à Relatividade Geral completa?"
        ),
        "opcoes": [
            "Aplicando a gravitação universal newtoniana em uma esfera de fluido homogêneo em expansão finita com condições de simetria.",
            "Assumindo que a velocidade da luz é infinita em sistemas estelares distantes.",
            "Desconsiderando totalmente a pressão do gás e focando apenas na força centrífuga.",
            "Substituindo a massa gravitacional por cargas elétricas estáticas distribuídas no espaço.",
        ],
        "resposta_correta": (
            "Aplicando a gravitação universal newtoniana em uma esfera de"
            " fluido homogêneo em expansão finita com condições de simetria."
        ),
    },
    {
        "pergunta": (
            "2. Qual é a principal limitação conceitual da Cosmologia"
            " Newtoniana quando aplicada a um universo infinitamente estendido e"
            " homogêneo?"
        ),
        "opcoes": [
            "A impossibilidade matemática de definir potenciais gravitacionais convergentes sem paradoxos como o de Olbers ou divergências nas forças.",
            "A incapacidade de prever órbitas elípticas para planetas fora do Sistema Solar.",
            "O conflito direto com as Leis de Kepler sobre o movimento dos cometas.",
            "A suposição incorreta de que o vácuo possui propriedades magnéticas.",
        ],
        "resposta_correta": (
            "A impossibilidade matemática de definir potenciais"
            " gravitacionais convergentes sem paradoxos como o de Olbers ou"
            " divergências nas forças."
        ),
    },
    {
        "pergunta": (
            "3. O que as Curvas de Rotação Plana das galáxias revelam sobre a"
            " distribuição de massa quando analisadas sob a ótica da física"
            " clássica e da gravitação?"
        ),
        "opcoes": [
            "Que a massa da galáxia concentra-se exclusivamente no buraco negro supermassivo central.",
            "Que a velocidade orbital das estrelas externas não cai conforme esperado por Kepler, exigindo um halo esférico extensivo de matéria não luminosa.",
            "Que a força gravitacional decresce proporcionalmente ao cubo da distância nas bordas.",
            "Que o atrito com o meio interestelar consome a energia cinética das estrelas periféricas.",
        ],
        "resposta_correta": (
            "Que a velocidade orbital das estrelas externas não cai conforme"
            " esperado por Kepler, exigindo um halo esférico extensivo de"
            " matéria não luminosa."
        ),
    },
    {
        "pergunta": (
            "4. Qual o significado físico do 'Parâmetro de Deceleração/Aceleração'"
            " no estudo da expansão do universo?"
        ),
        "opcoes": [
            "Mede a taxa na qual a rotação da Terra diminui devido à fricção das marés lunares.",
            "Indica se a taxa de expansão do cosmos está freando devido à gravidade da matéria ou acelerando devido à energia escura.",
            "Calcula o tempo exato que um fóton leva para cruzar o horizonte observável.",
            "Determina a perda de energia cinética de galáxias em colisão direta.",
        ],
        "resposta_correta": (
            "Indica se a taxa de expansão do cosmos está freando devido à"
            " gravidade da matéria ou acelerando devido à energia escura."
        ),
    },
    {
        "pergunta": (
            "5. No contexto do modelo cosmológico $\\Lambda$CDM, o que"
            " representa o termo $\\Lambda$ (Lambda)?"
        ),
        "opcoes": [
            "O coeficiente de atrito do espaço-tempo quântico.",
            "A Constante Cosmológica, associada à densidade de energia do vácuo que impulsiona a expansão acelerada.",
            "A taxa de decaimento radioativo dos elementos primordiais do Big Bang.",
            "O momento angular total acumulado por todas as galáxias espirais.",
        ],
        "resposta_correta": (
            "A Constante Cosmológica, associada à densidade de energia do vácuo"
            " que impulsiona a expansão acelerada."
        ),
    },
    {
        "pergunta": (
            "6. O que foi o problema resolvido pela introdução da Teoria da"
            " Inflação Cósmica na física do Big Bang?"
        ),
        "opcoes": [
            "A ausência de evidências sobre a existência de buracos negros estelares.",
            "Os problemas do horizonte e da planura, explicando por que o universo é isotrópico e geometricamente plano em grande escala.",
            "A divergência entre a massa do próton e a massa do nêutron no plasma primordial.",
            "A colisão iminente entre a Via Láctea e a galáxia de Andrômeda.",
        ],
        "resposta_correta": (
            "Os problemas do horizonte e da planura, explicando por que o"
            " universo é isotrópico e geometricamente plano em grande escala."
        ),
    },
    {
        "pergunta": (
            "7. Como as Supernovas do Tipo Ia atuam como 'velas padrão' na"
            " determinação da geometria e expansão do universo?"
        ),
        "opcoes": [
            "Por possuírem uma luminosidade de pico intrínseca extremamente uniforme e previsível devido ao limite de Chandrasekhar da anã branca.",
            "Por brilharem constantemente sem nunca diminuir de intensidade ao longo dos milênios.",
            "Por estarem fixas em pontos estelares de referência que não sofrem efeito Doppler.",
            "Por emitirem exclusivamente ondas de rádio de frequência fixa calibrada.",
        ],
        "resposta_correta": (
            "Por possuírem uma luminosidade de pico intrínseca extremamente"
            " uniforme e previsível devido ao limite de Chandrasekhar da anã"
            " branca."
        ),
    },
]

BANCO_AVANCADO = [
    {
        "pergunta": (
            "1. Analisando as Equações de Friedmann derivadas da Relatividade"
            " Geral (e em paralelo na Cosmologia Neo-Newtoniana), qual é a"
            " relação fundamental entre a curvatura espacial $k$, a densidade"
            " de energia e a taxa de expansão $H$?"
        ),
        "opcoes": [
            "A curvatura depende estritamente da temperatura absoluta da radiação de fundo, ignorando a massa.",
            "A equação de Friedmann relaciona o quadrado do parâmetro de Hubble com a densidade total de energia e a curvatura espacial normalizada.",
            "A taxa de expansão é independente da densidade de matéria, dependendo apenas da constante de Planck.",
            "A geometria do espaço é sempre hiperbólica, independentemente da densidade crítica do cosmos.",
        ],
        "resposta_correta": (
            "A equação de Friedmann relaciona o quadrado do parâmetro de"
            " Hubble com a densidade total de energia e a curvatura espacial"
            " normalizada."
        ),
    },
    {
        "pergunta": (
            "2. No estudo da instabilidade gravitacional de Jeans na"
            " cosmologia newtoniana, o que representa o 'Comprimento de Jeans'?"
        ),
        "opcoes": [
            "A distância máxima que a luz percorre em um segundo de tempo cosmológico.",
            "O limiar crítico de escala no qual as forças gravitacionais superam as forças de pressão térmica, permitindo o colapso e formação de estruturas.",
            "O raio exato do horizonte de eventos de um buraco negro primordial.",
            "A espessura da fronteira entre a matéria escura fria e a matéria bariônica.",
        ],
        "resposta_correta": (
            "O limiar crítico de escala no qual as forças gravitacionais"
            " superam as forças de pressão térmica, permitindo o colapso e"
            " formação de estruturas."
        ),
    },
    {
        "pergunta": (
            "3. O que caracteriza conceitualmente a Tensão de Hubble (Hubble"
            " Tension) na cosmologia contemporânea de precisão?"
        ),
        "opcoes": [
            "A falha mecânica dos espelhos do telescópio espacial James Webb ao focar galáxias distantes.",
            "A discrepância estatística irredutível entre a taxa de expansão medida localmente (supernovas/cefeidas) e a inferida via CMB (Planck).",
            "O atrito quântico sofrido pelos fótons ao atravessarem campos magnéticos intergalácticos fortes.",
            "A variação na constante gravitacional $G$ medida em diferentes estações do ano na Terra.",
        ],
        "resposta_correta": (
            "A discrepância estatística irredutível entre a taxa de expansão"
            " medida localmente (supernovas/cefeidas) e a inferida via CMB"
            " (Planck)."
        ),
    },
    {
        "pergunta": (
            "4. Qual é o papel epistemológico e metodológico de utilizar a"
            " abordagem da Cosmologia Neo-Newtoniana em sequências didáticas"
            " avançadas antes da Relatividade Geral?"
        ),
        "opcoes": [
            "Substituir definitivamente a relatividade por ser um modelo matematicamente mais correto.",
            "Permitir que estudantes compreendam a dinâmica da expansão, conservação de energia e equações de movimento usando cálculo e mecânica clássica familiar.",
            "Evitar qualquer uso de equações diferenciais no ensino de física moderna.",
            "Provar que o universo é estático e newtoniano em sua essência profunda.",
        ],
        "resposta_correta": (
            "Permitir que estudantes compreendam a dinâmica da expansão,"
            " conservação de energia e equações de movimento usando cálculo e"
            " mecânica clássica familiar."
        ),
    },
    {
        "pergunta": (
            "5. O que postula o Princípio Holográfico e sua relação com a"
            " entropia dos horizontes cosmológicos e de buracos negros?"
        ),
        "opcoes": [
            "Que a informação de um volume tridimensional de espaço pode ser inteiramente codificada em sua fronteira bidimensional, limitando graus de liberdade.",
            "Que as imagens de galáxias distantes são geradas por projeções holográficas de laser quântico no vácuo.",
            "Que o tempo cósmico flui em duasdireções simultâneas em dimensões compactificadas.",
            "Que a matéria escura é uma ilusão óptica gerada por interferência de ondas eletromagnéticas.",
        ],
        "resposta_correta": (
            "Que a informação de um volume tridimensional de espaço pode ser"
            " inteiramente codificada em sua fronteira bidimensional, limitando"
            " graus de liberdade."
        ),
    },
]

# Garantir robustez caso precise complementar
while len(BANCO_BASICO) < 25:
  BANCO_BASICO.append({
      "pergunta": (
          f"Questão Conceitual Básica Adicional {len(BANCO_BASICO)+1}: Qual a"
          " evidência primária da expansão cósmica?"
      ),
      "opcoes": [
          "O desvio para o vermelho (redshift) das galáxias distantes.",
          "O esfriamento do Sol ao longo dos anos.",
          "A aproximação contínua da Lua em relação à Terra.",
          "O aumento da luminosidade das estrelas cadentes.",
      ],
      "resposta_correta": (
          "O desvio para o vermelho (redshift) das galáxias distantes."
      ),
  })

while len(BANCO_MEDIO) < 25:
  BANCO_MEDIO.append({
      "pergunta": (
          f"Questão Conceitual Média Adicional {len(BANCO_MEDIO)+1}: No"
          " contexto newtoniano aplicado à cosmologia, como a energia total de"
          " uma casca esférica em expansão determina o destino do universo?"
      ),
      "opcoes": [
          "Energia total negativa indica universo fechado (recolapso); positiva indica aberto; nula indica plano (crítico).",
          "A energia total não tem relação com o destino dinâmico do cosmo.",
          "Apenas a pressão magnética define se haverá expansão infinita.",
          "A energia total determina exclusivamente a temperatura da radiação de fundo.",
      ],
      "resposta_correta": (
          "Energia total negativa indica universo fechado (recolapso);"
          " positiva indica aberto; nula indica plano (crítico)."
      ),
  })

while len(BANCO_AVANCADO) < 20:
  BANCO_AVANCADO.append({
      "pergunta": (
          f"Questão Conceitual Avançada Adicional"
          f" {len(BANCO_AVANCADO)+1}: Qual a implicação termodinâmica da"
          " predominância da Energia Escura na evolução tardia do universo?"
      ),
      "opcoes": [
          "O universo caminha para um cenário de expansão acelerada perpétua, levando ao 'Big Freeze' (Morte Térmica), onde estruturas isolam-se causalmente.",
          "O sistema sofrerá um colapso imediato revertendo para o estado de alta densidade.",
          "A entropia total do universo passará a decrescer exponencialmente.",
          "Haverá conversão total de energia escura em matéria bariônica luminosa.",
      ],
      "resposta_correta": (
          "O universo caminha para um cenário de expansão acelerada perpétua,"
          " levando ao 'Big Freeze' (Morte Térmica), onde estruturas"
          " isolam-se causalmente."
      ),
  })

# =========================================================================
# GERENCIAMENTO DE ESTADO DA SESSÃO
# =========================================================================
if "modo" not in st.session_state:
  st.session_state.modo = "menu"
if "etapa_aluno" not in st.session_state:
  st.session_state.etapa_aluno = "escolha_nivel"
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
      {"nome": "Prof. Francisco", "nivel": "Avançado", "pontos": 5},
      {"nome": "Estudante Pesquisador", "nivel": "Médio", "pontos": 4},
  ]

# Título Principal
st.markdown(
    "<h1>🌌 Sequência Didática: Cosmologia, Big Bang & Gravitação</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Ambiente conceitual de"
    " avaliação e estudo para Sequências Didáticas em Física e"
    " Astronomia.</p>",
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
    st.markdown("### 👨‍🎓 Aluno / Participante")
    st.write(
        "Realize a sequência de perguntas conceituais (Básico, Médio ou"
        " Avançado) e descubra seu status cósmico!"
    )
    if st.button("Entrar como Aluno"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_aluno = "escolha_nivel"
      st.rerun()

  with c2:
    st.markdown("### ⚙️ Gerente de Rede (Organizador)")
    st.write("Acesso restrito ao professor/gerente para gerenciar a turma.")
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
    st.subheader(
        "🎯 Passo 1: Identificação e Nível da Sequência Didática"
    )
    nome_input = st.text_input("Seu Nome Completo ou Apelido:")

    st.markdown("### Selecione o Nível de Profundidade Conceitual:")
    nivel_sel = st.selectbox(
        "Nível:",
        [
            "Básico (Fundamentos do Big Bang & Matéria Escura)",
            "Médio (Cosmologia Neo-Newtoniana & Dinâmica)",
            "Avançado (Equações de Friedmann, Tensão de Hubble & Termodinâmica)",
        ],
    )

    if st.button("🚀 Iniciar Sequência de Questões"):
      if nome_input.strip() == "":
        st.warning("Por favor, digite um nome válido.")
      else:
        st.session_state.nome_usuario = nome_input.strip()
        st.session_state.nivel_escolhido = nivel_sel

        if "Básico" in nivel_sel:
          banco = list(BANCO_BASICO)
        elif "Médio" in nivel_sel:
          banco = list(BANCO_MEDIO)
        else:
          banco = list(BANCO_AVANCADO)

        random.shuffle(banco)
        st.session_state.perguntas_sessao = banco[
            :5
        ]  # Bloco focado de 5 a 10 questões por teste pedagógico
        st.session_state.indice_pergunta = 0
        st.session_state.respostas_usuario = []
        st.session_state.etapa_aluno = "quiz"
        st.rerun()

  # ETAPA 2: O Quiz Conceitual (Pergunta por Pergunta)
  elif st.session_state.etapa_aluno == "quiz":
    idx = st.session_state.indice_pergunta
    total_q = len(st.session_state.perguntas_sessao)
    q_atual = st.session_state.perguntas_sessao[idx]

    st.write(
        f"👤 **Participante:** {st.session_state.nome_usuario} | 📚"
        f" **Trilha:** {st.session_state.nivel_escolhido} | **Questão"
        f" {idx + 1} de {total_q}**"
    )
    st.progress((idx) / total_q)

    st.markdown(
        f"<div class='pergunta-box'><h3>{q_atual['pergunta']}</h3></div>",
        unsafe_allow_html=True,
    )

    escolha = st.radio(
        "Selecione a interpretação conceitual correta:",
        q_atual["opcoes"],
        key=f"q_{idx}",
    )

    c_avanco1, c_avanco2 = st.columns(2)
    with c_avanco2:
      if st.button("Avançar para Próxima ➡️"):
        st.session_state.respostas_usuario.append({
            "pergunta": q_atual["pergunta"],
            "escolhida": escolha,
            "correta": q_atual["resposta_correta"],
        })

        st.session_state.indice_pergunta += 1
        if st.session_state.indice_pergunta >= total_q:
          acertos = sum(
              1
              for r in st.session_state.respostas_usuario
              if r["escolhida"] == r["correta"]
          )

          st.session_state.ranking.append({
              "nome": st.session_state.nome_usuario,
              "nivel": st.session_state.nivel_escolhido.split(" ")[0],
              "pontos": acertos,
          })
          st.session_state.ranking = sorted(
              st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
          )
          st.session_state.etapa_aluno = "resultado"
        st.rerun()

  # ETAPA 3: Resultados Finais, Gabarito e Ranks Temáticos
  elif st.session_state.etapa_aluno == "resultado":
    st.success("🎉 Sequência Didática Concluída com Sucesso!")

    acertos = sum(
        1
        for r in st.session_state.respostas_usuario
        if r["escolhida"] == r["correta"]
    )
    total_q = len(st.session_state.perguntas_sessao)
    st.markdown(
        f"### 🏆 Sua Pontuação Final: {acertos} de {total_q} acertos"
    )

    # Classificação Cósmica Temática
    if acertos <= 1:
      status_cosmico = (
          "🌍 **Cosmólogo(a) da Terra** (Você iniciou sua jornada compreendendo"
          " os alicerces observacionais clássicos!)"
      )
    elif acertos <= 3:
      status_cosmico = (
          "🔭 **Cosmólogo(a) dos Céus** (Você domina a dinâmica de rotação,"
          " gravitação e expansão galáctica!)"
      )
    elif acertos == 4:
      status_cosmico = (
          "🌌 **Cosmólogo(a) do Universo** (Excelente domínio conceitual sobre"
          " o Big Bang, matéria escura e modelos cosmológicos!)"
      )
    else:
      status_cosmico = (
          "🌀 **Cosmólogo(a) do Multiverso** (Domínio profundo e rigoroso da"
          " física teórica, termodinâmica e equações de campo!)"
      )

    st.markdown(f"### Seu Título na Sequência: {status_cosmico}")
    st.divider()

    # Gabarito Exibido Apenas ao Final
    st.subheader("📋 Gabarito e Análise Conceitual Detalhada")
    for i, resp in enumerate(st.session_state.respostas_usuario, start=1):
      acertou = resp["escolhida"] == resp["correta"]
      icon = "✅" if acertou else "❌"
      st.markdown(f"**Questão {i}:** {resp['pergunta']}")
      st.markdown(f"- Sua resposta: {resp['escolhida']} {icon}")
      if not acertou:
        st.markdown(f"- 💡 **Conceito Correto:** `{resp['correta']}`")
      st.markdown("---")

    # Ranking Geral da Turma/Participantes
    st.subheader("📊 Ranking Geral de Participantes")
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
    if st.button("🔄 Refazer a Sequência Didática"):
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

    st.subheader("📊 Desempenho dos Alunos na Sequência Didática")
    if len(st.session_state.ranking) == 0:
      st.info("Nenhum registro de aluno na turma ainda.")
    else:
      for pos, c in enumerate(st.session_state.ranking, start=1):
        st.markdown(
            f"**{pos}º:** 👤 {c['nome']} | **Trilha:** {c['nivel']} |"
            f" **Pontos:** {c['pontos']}"
        )

    st.divider()
    col_g1, col_g2 = st.columns(2)
    with col_g1:
      if st.button("🗑️ Limpar Registros da Turma"):
        st.session_state.ranking = []
        st.success("Registros limpos!")
        st.rerun()
    with col_g2:
      if st.button("🔒 Sair do Painel"):
        st.session_state.logado_gerente = False
        st.session_state.modo = "menu"
        st.rerun()
