import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Sequência Didática: Cosmologia, Big Bang e Expansão",
    page_icon="🌌",
    layout="wide",
)

# Estilização Visual (Tema Espacial com Painel da Raquel)
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
    .raquel-box {
        background-color: #1a0f35;
        border: 2px solid #ff00ff;
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
# BANCO DE QUESTÕES DIVIDIDO POR AULAS COM O SUPORTE DA RAQUEL (ASSISTENTE)
# =========================================================================

AULA_1_QUESTOES = [
    {
        "tipo": "hibrida",  # Marcação + Explicação obrigatória
        "pergunta": (
            "1. (Aula 1) Como o modelo do 'Átomo Primitivo' de Georges"
            " Lemaître revolucionou a visão de um universo estático?"
        ),
        "opcoes": [
            (
                "Propondo que o universo nem teve início nem terá fim,"
                " mantendo densidade constante."
            ),
            (
                "Sugerindo que toda a massa do cosmos esteve concentrada em um"
                " único ponto hiperdenso que iniciou sua expansão."
            ),
            (
                "Afirmando que a Via Láctea é o centro absoluto e imóvel de"
                " todas as galáxias."
            ),
            (
                "Defendendo que o espaço é preenchido por um fluido estático"
                " imutável chamado éter."
            ),
        ],
        "resposta_correta": (
            "Sugerindo que toda a massa do cosmos esteve concentrada em um"
            " único ponto hiperdenso que iniciou sua expansão."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Lembre-se da nossa Aula 1! Lemaître usou a"
            " física para mostrar que o universo teve um começo dinâmico.'"
        ),
        "indicacao": (
            "🎥 **Indicação da Raquel para Estudo:** Assista à videoaula sobre"
            " *A Origem do Universo e Georges Lemaître* no YouTube ou pesquise"
            " no portal da [NASA Science -"
            " Universe](https://science.nasa.gov/universe/)."
        ),
    },
    {
        "tipo": "hibrida",
        "pergunta": (
            "2. (Aula 1) O que o famoso 'Paradoxo de Olbers' questionava sobre"
            " o modelo de universo infinito e estático?"
        ),
        "opcoes": [
            (
                "Por que o céu noturno é escuro se o universo fosse infinito,"
                " estático e povoado por infinitas estrelas."
            ),
            (
                "Por que os planetas do Sistema Solar giram no mesmo sentido"
                " ao redor do Sol."
            ),
            (
                "Por que a luz das estrelas não sofre atrito ao atravessar o"
                " vácuo."
            ),
            (
                "Por que a massa do Sol é menor em comparação com as"
                " supergigantes."
            ),
        ],
        "resposta_correta": (
            "Por que o céu noturno é escuro se o universo fosse infinito,"
            " estático e povoado por infinitas estrelas."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Olhe para a noite! Se o universo fosse"
            " eterno e infinito, o céu brilharia como o sol!'"
        ),
        "indicacao": (
            "📖 **Indicação da Raquel:** Pesquise artigos sobre o *Paradoxo de"
            " Olbers* no portal do [Observatório"
            " Nacional](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/on)."
        ),
    },
    {
        "tipo": "dissertativa",
        "pergunta": (
            "3. (Aula 1 - Reflexão Descritiva) Com suas próprias palavras,"
            " descreva como a ciência mudou a forma de pensar a origem do"
            " universo desde a antiguidade até a proposta do Big Bang."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Escreva com suas palavras o que marcou você"
            " nesta aula! Pense na transição do céu eterno para o cosmo em"
            " expansão.'"
        ),
        "indicacao": (
            "🎥 **Indicação da Raquel:** Procure videoaulas de divulgação"
            " científica sobre *A História da Cosmologia* (como canais do Space"
            " Today ou Ciência Todo Dia)."
        ),
    },
]

AULA_2_QUESTOES = [
    {
        "tipo": "hibrida",
        "pergunta": (
            "1. (Aula 2) O que a Lei de Hubble demonstrou sobre o movimento das"
            " galáxias distantes?"
        ),
        "opcoes": [
            (
                "Que as galáxias mais distantes da Terra se afastam com"
                " velocidades maiores e proporcionais à sua distância."
            ),
            (
                "Que todas as galáxias orbitam o centro da Via Láctea em"
                " trajetórias circulares fixas."
            ),
            (
                "Que o universo está encolhendo gradualmente em direção a um"
                " ponto central."
            ),
            (
                "Que a luz das galáxias perde velocidade com o passar dos"
                " bilhões de anos."
            ),
        ],
        "resposta_correta": (
            "Que as galáxias mais distantes da Terra se afastam com velocidades"
            " maiores e proporcionais à sua distância."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Quanto mais longe a galáxia está, mais rápido"
            " o espaço entre nós e ela se estica!'"
        ),
        "indicacao": (
            "🎥 **Indicação da Raquel:** Assista a videoaulas sobre a *Lei de"
            " Hubble e o Redshift* ou visite a página de cosmologia da"
            " [ESA](https://www.esa.int/)."
        ),
    },
    {
        "tipo": "dissertativa",
        "pergunta": (
            "2. (Aula 2 - Experimento Mental) Explique como a analogia do balão"
            " com pontinhos desenhados ajuda a entender por que todas as"
            " galáxias se afastam umas das outras sem que exista um 'centro' no"
            " universo."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Pense no balão inflando: na borracha não há"
            " centro privilegiado! Todos os pontos se distanciam de todos.'"
        ),
        "indicacao": (
            "📖 **Indicação da Raquel:** Leia artigos de divulgação sobre a"
            " *Expansão do Tecido do Espaço-Tempo* no site do IAG-USP."
        ),
    },
]

AULA_3_QUESTOES = [
    {
        "tipo": "hibrida",
        "pergunta": (
            "1. (Aula 3) Por que as curvas de rotação galáctica exigiram a"
            " proposta da existência da Matéria Escura?"
        ),
        "opcoes": [
            (
                "Porque as estrelas nas bordas giram muito mais rápido do que a"
                " massa luminosa visível conseguiria sustentar."
            ),
            (
                "Porque o centro das galáxias emite mais luz do que a soma de"
                " todas as estrelas."
            ),
            (
                "Porque a expansão do universo empurra as bordas galácticas para"
                " fora."
            ),
            (
                "Porque o gás interestelar absorve toda a luz visível das"
                " estrelas centrais."
            ),
        ],
        "resposta_correta": (
            "Porque as estrelas nas bordas giram muito mais rápido do que a"
            " massa luminosa visível conseguiria sustentar."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Pela gravidade de Newton, as estrelas das"
            " bordas deveriam ir devagar. Se giram rápido, tem massa invisível"
            " lá!'"
        ),
        "indicacao": (
            "🎥 **Indicação da Raquel:** Assista a documentários sobre *O Mistério"
            " da Matéria Escura e Energia Escura*."
        ),
    },
    {
        "tipo": "hibrida",
        "pergunta": (
            "2. (Aula 3) Qual é a principal diferença de atuação entre a"
            " Matéria Escura e a Energia Escura na evolução do universo?"
        ),
        "opcoes": [
            (
                "A Matéria Escura atrai gravitacionalmente e une as estruturas;"
                " a Energia Escura atua repelindo e acelerando a expansão."
            ),
            (
                "A Matéria Escura brilha no escuro; a Energia Escura absorve"
                " luz."
            ),
            (
                "A Matéria Escura existe apenas no Sistema Solar; a Energia"
                " Escura fica nas galáxias distantes."
            ),
            (
                "Não há diferença prática entre as duas."
            ),
        ],
        "resposta_correta": (
            "A Matéria Escura atrai gravitacionalmente e une as estruturas; a"
            " Energia Escura atua repelindo e acelerando a expansão."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Uma puxa (atração) para formar galáxias, e a"
            " outra empurra (repulsão) para acelerar a expansão cósmica!'"
        ),
        "indicacao": (
            "📖 **Indicação da Raquel:** Explore o portal científico da [NASA"
            " Science - Dark Energy & Dark"
            " Matter](https://science.nasa.gov/universe/)."
        ),
    },
]

# =========================================================================
# GERENCIAMENTO DE ESTADO DA SESSÃO
# =========================================================================
if "modo" not in st.session_state:
  st.session_state.modo = "menu"
if "etapa_aluno" not in st.session_state:
  st.session_state.etapa_aluno = "escolha_aula"
if "aula_escolhida" not in st.session_state:
  st.session_state.aula_escolhida = ""
if "nome_usuario" not in st.session_state:
  st.session_state.nome_usuario = ""
if "questoes_sessao" not in st.session_state:
  st.session_state.questoes_sessao = []
if "indice_pergunta" not in st.session_state:
  st.session_state.indice_pergunta = 0
if "respostas_usuario" not in st.session_state:
  st.session_state.respostas_usuario = []
if "logado_gerente" not in st.session_state:
  st.session_state.logado_gerente = False
if "ranking" not in st.session_state:
  st.session_state.ranking = [
      {"nome": "Felipe Lima", "aula": "Aula 1", "pontos": 2},
      {"nome": "Raquel (Assistente)", "aula": "Aula 3", "pontos": 2},
  ]

# Título Principal
st.markdown(
    "<h1>🌌 Sequência Didática: Cosmologia & Big Bang</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Com o auxílio da assistente"
    " Raquel, estude a história, a expansão e os mistérios do cosmo.</p>",
    unsafe_allow_html=True,
)
st.divider()

# =========================================================================
# MENU INICIAL
# =========================================================================
if st.session_state.modo == "menu":
  col_m1, col_m2 = st.columns(2)
  with col_m1:
    st.markdown("### 👨‍🎓 Aluno / Participante")
    st.write(
        "Selecione sua aula, estude com as dicas da Raquel e responda às"
        " questões conceituais!"
    )
    if st.button("Entrar como Aluno"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_aluno = "escolha_aula"
      st.rerun()

  with col_m2:
    st.markdown("### ⚙️ Gerente de Rede (Organizador)")
    st.write(
        "Acesso restrito ao professor/organizador para gerenciar a turma."
    )
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

  # ETAPA 1: Identificação e Escolha da Aula
  if st.session_state.etapa_aluno == "escolha_aula":
    st.subheader("🎯 Passo 1: Identificação e Seleção da Aula")
    nome_input = st.text_input("Seu Nome Completo ou Apelido:")

    st.markdown("### Escolha a Aula da Sequência Didática:")
    aula_sel = st.selectbox(
        "Aula:",
        [
            "Aula 1: História da Cosmologia e o Big Bang",
            "Aula 2: A Expansão do Universo",
            "Aula 3: Matéria Escura, Energia Escura e Estrutura Cósmica",
        ],
    )

    if st.button("🚀 Iniciar Atividade com a Raquel"):
      if nome_input.strip() == "":
        st.warning("Por favor, digite um nome válido.")
      else:
        st.session_state.nome_usuario = nome_input.strip()
        st.session_state.aula_escolhida = aula_sel

        if "Aula 1" in aula_sel:
          st.session_state.questoes_sessao = list(AULA_1_QUESTOES)
        elif "Aula 2" in aula_sel:
          st.session_state.questoes_sessao = list(AULA_2_QUESTOES)
        else:
          st.session_state.questoes_sessao = list(AULA_3_QUESTOES)

        st.session_state.indice_pergunta = 0
        st.session_state.respostas_usuario = []
        st.session_state.etapa_aluno = "quiz"
        st.rerun()

  # ETAPA 2: Questões com Painel da Raquel ao Lado (Híbridas: Marcação + Explicação)
  elif st.session_state.etapa_aluno == "quiz":
    idx = st.session_state.indice_pergunta
    total_q = len(st.session_state.questoes_sessao)
    q_atual = st.session_state.questoes_sessao[idx]

    st.write(
        f"👤 **Participante:** {st.session_state.nome_usuario} | 📚"
        f" **Trilha:** {st.session_state.aula_escolhida} | **Questão"
        f" {idx + 1} de {total_q}**"
    )
    st.progress((idx) / total_q)

    # Layout de Duas Colunas: Esquerda (Questão), Direita (Painel da Raquel)
    col_q, col_r = st.columns([2, 1])

    with col_r:
      st.markdown(
          f"""
            <div class='raquel-box'>
                <h3 style='margin:0; color:#ff00ff;'>👧 Raquel, a Assistente</h3>
                <p style='margin-top:10px; font-size:15px;'>{q_atual['dica_raquel']}</p>
                <hr style='border-color: #444;'>
                <p style='font-size:13px; color:#ddd;'>{q_atual['indicacao']}</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

    with col_q:
      st.markdown(
          f"<div class='pergunta-box'><h3>{q_atual['pergunta']}</h3></div>",
          unsafe_allow_html=True,
      )

      if q_atual["tipo"] == "hibrida":
        resposta_escolhida = st.radio(
            "Selecione a alternativa correta:",
            q_atual["opcoes"],
            key=f"opt_{idx}",
        )
        st.markdown("<br>", unsafe_allow_html=True)
        explicacao_aluno = st.text_area(
            "✍️ Explique com suas palavras o porquê da sua escolha:",
            key=f"exp_{idx}",
            placeholder=(
                "Escreva aqui a sua justificativa detalhada para esta resposta..."
            ),
        )
      else:
        resposta_escolhida = "Questão Descritiva"
        explicacao_aluno = st.text_area(
            "✍️ Escreva sua resposta e reflexão detalhada:",
            key=f"text_{idx}",
            placeholder=(
                "Digite aqui sua descrição aprofundada sobre o tema..."
            ),
        )

    st.divider()
    c_btn1, c_btn2 = st.columns(2)
    with c_btn2:
      if st.button("Avançar para Próxima ➡️"):
        if (
            q_atual["tipo"] == "hibrida" and not explicacao_aluno.strip()
        ) or (q_atual["tipo"] == "dissertativa" and not explicacao_aluno.strip()):
          st.warning(
              "Por favor, preencha a explicação/descrição antes de avançar!"
          )
        else:
          correta = (
              q_atual["resposta_correta"]
              if q_atual["tipo"] == "hibrida"
              else "Resposta Descritiva"
          )
          is_acerto = (
              (resposta_escolhida == q_atual["resposta_correta"])
              if q_atual["tipo"] == "hibrida"
              else True
          )

          st.session_state.respostas_usuario.append({
              "pergunta": q_atual["pergunta"],
              "escolhida": resposta_escolhida,
              "explicacao": explicacao_aluno,
              "correta": correta,
              "acertou": is_acerto,
          })

          st.session_state.indice_pergunta += 1
          if st.session_state.indice_pergunta >= total_q:
            pontos = sum(
                1 for r in st.session_state.respostas_usuario if r["acertou"]
            )

            st.session_state.ranking.append({
                "nome": st.session_state.nome_usuario,
                "aula": st.session_state.aula_escolhida.split(":")[0],
                "pontos": pontos,
            })
            st.session_state.ranking = sorted(
                st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
            )
            st.session_state.etapa_aluno = "resultado"
          st.rerun()

  # ETAPA 3: Resultados Finais e Gabarito
  elif st.session_state.etapa_aluno == "resultado":
    st.success("🎉 Atividade da Aula Concluída com Sucesso!")

    pontos = sum(
        1 for r in st.session_state.respostas_usuario if r["acertou"]
    )
    total_q = len(st.session_state.questoes_sessao)
    st.markdown(
        f"### 🏆 Sua Pontuação de Desempenho: {pontos} de {total_q}"
    )

    if pontos <= 1:
      status_cosmico = (
          "🌍 **Cosmólogo(a) da Terra** (Raquel diz: Bom começo! Continue"
          " revisando as indicações de estudo.)"
      )
    elif pontos == 2:
      status_cosmico = (
          "🔭 **Cosmólogo(a) dos Céus** (Raquel diz: Ótimo trabalho! Excelente"
          " raciocínio conceitual.)"
      )
    else:
      status_cosmico = (
          "🌌 **Cosmólogo(a) do Universo** (Raquel diz: Perfeito! Domínio"
          " absoluto da matéria e expansão!)"
      )

    st.markdown(f"### Seu Título Cósmico: {status_cosmico}")
    st.divider()

    st.subheader("📋 Gabarito, Explicações Enviadas e Correção")
    for i, resp in enumerate(st.session_state.respostas_usuario, start=1):
      st.markdown(f"**Questão {i}:** {resp['pergunta']}")
      if resp["correta"] != "Resposta Descritiva":
        icon = "✅" if resp["escolhida"] == resp["correta"] else "❌"
        st.markdown(f"- Alternativa escolhida: {resp['escolhida']} {icon}")
        if resp["escolhida"] != resp["correta"]:
          st.markdown(f"- 💡 **Conceito Correto:** `{resp['correta']}`")
      st.markdown(f"- ✍️ *Sua explicação:* {resp['explicacao']}")
      st.markdown("---")

    st.subheader("📊 Ranking Geral de Participantes")
    for pos, c in enumerate(st.session_state.ranking[:10], start=1):
      medalha = (
          "🥇"
          if pos == 1
          else ("🥈" if pos == 2 else ("🥉" if pos == 3 else "🔸"))
      )
      st.markdown(
          f"**{medalha} {pos}º lugar:** {c['nome']} ({c['aula']}) —"
          f" **{c['pontos']} pts**"
      )

    st.divider()
    if st.button("🔄 Refazer / Escolher Outra Aula"):
      st.session_state.etapa_aluno = "escolha_aula"
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

    st.subheader("📊 Acompanhamento dos Alunos")
    if len(st.session_state.ranking) == 0:
      st.info("Nenhum registro na turma ainda.")
    else:
      for pos, c in enumerate(st.session_state.ranking, start=1):
        st.markdown(
            f"**{pos}º:** 👤 {c['nome']} | **Aula:** {c['aula']} |"
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
