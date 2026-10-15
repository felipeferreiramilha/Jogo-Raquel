import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Olimpíada Online de Cosmologia",
    page_icon="🌌",
    layout="centered",
)

# Estilização Visual (Tema Espacial)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #070714;
        color: #ffffff;
    }
    h1, h2, h3 {
        color: #00ffff !important;
        text-align: center;
    }
    .stButton>button {
        background-color: #16213e;
        color: #00ffff;
        border: 2px solid #00ffff;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
        height: 45px;
    }
    .stButton>button:hover {
        background-color: #00ffff;
        color: #070714;
    }
    .curiosidade-box {
        background-color: #12122c;
        border-left: 5px solid #ffcc00;
        padding: 15px;
        border-radius: 5px;
        margin-top: 15px;
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

# Banco de Perguntas sobre Cosmologia e Big Bang
QUESTOES = [
    {
        "pergunta": (
            "1. Quem foi o físico e padre belga que propôs pela primeira vez a"
            " teoria do 'Átomo Primitivo', que mais tarde ficou conhecida como"
            " o Big Bang?"
        ),
        "opcoes": [
            "Albert Einstein",
            "Georges Lemaître",
            "Stephen Hawking",
            "Edwin Hubble",
        ],
        "resposta_correta": "Georges Lemaître",
        "curiosidade": (
            "Georges Lemaître propôs a teoria em 1927. No início, Einstein"
            " rejeitou a ideia dizendo que 'sua física era abominável', mas"
            " depois comprovou-se correta com a expansão do universo."
        ),
    },
    {
        "pergunta": (
            "2. O que comprova de forma mais direta a teoria do Big Bang através"
            " de um 'eco' remanescente do início do universo?"
        ),
        "opcoes": [
            "A Radiação Cósmica de Fundo em Micro-ondas (CMB)",
            "A gravidade dos buracos negros",
            "O vento solar",
            "A luz das estrelas binárias",
        ],
        "resposta_correta": (
            "A Radiação Cósmica de Fundo em Micro-ondas (CMB)"
        ),
        "curiosidade": (
            "Descoberta acidentalmente em 1965 por Arno Penzias e Robert"
            " Wilson, a CMB é o calor remanescente dos primeiros momentos do"
            " universo (cerca de 380 mil anos após o Big Bang)."
        ),
    },
    {
        "pergunta": (
            "3. O que a célebre 'Lei de Hubble' demonstrou sobre o nosso"
            " universo?"
        ),
        "opcoes": [
            "Que o universo é estático e eterno",
            "Que as galáxias distantes estão se afastando umas das outras"
            " (expansão)",
            "Que o centro do universo é a Via Láctea",
            "Que o Sol vai virar um buraco negro",
        ],
        "resposta_correta": (
            "Que as galáxias distantes estão se afastando umas das outras"
            " (expansão)"
        ),
        "curiosidade": (
            "Edwin Hubble descobriu em 1929 que o desvio para o vermelho"
            " (redshift) da luz das galáxias prova que o cosmos está em"
            " expansão contínua."
        ),
    },
    {
        "pergunta": (
            "4. Qual é o nome dado à misteriosa força responsável por"
            " acelerar a expansão do universo nos tempos atuais?"
        ),
        "opcoes": [
            "Matéria Escura",
            "Energia Escura",
            "Força Centrífuga Cósmica",
            "Antigravidade Quântica",
        ],
        "resposta_correta": "Energia Escura",
        "curiosidade": (
            "Cerca de 68% do universo é composto por Energia Escura, 27% por"
            " Matéria Escura e apenas 5% por matéria normal (tudo o que"
            " conhecemos e tocamos!)."
        ),
    },
    {
        "pergunta": (
            "5. Qual foi o principal telescópio espacial lançado em dezembro de"
            " 2021 para observar as galáxias mais antigas e o início do"
            " universo?"
        ),
        "opcoes": [
            "Telescópio Espacial Hubble",
            "Telescópio James Webb (JWST)",
            "Observatório Chandra",
            "Telescópio Kepler",
        ],
        "resposta_correta": "Telescópio James Webb (JWST)",
        "curiosidade": (
            "O James Webb consegue capturar luz infravermelha de galáxias que"
            " se formaram há mais de 13,5 bilhões de anos, quase alcançando a"
            " 'Aurora Cósmica'."
        ),
    },
]

# Inicialização do Estado da Sessão (Persistência)
if "modo" not in st.session_state:
  st.session_state.modo = "menu"  # 'menu', 'aluno', 'gerente'
if "etapa_aluno" not in st.session_state:
  st.session_state.etapa_aluno = "cadastro"  # 'cadastro', 'quiz', 'resultado'
if "nome_usuario" not in st.session_state:
  st.session_state.nome_usuario = ""
if "indice_pergunta" not in st.session_state:
  st.session_state.indice_pergunta = 0
if "pontuacao" not in st.session_state:
  st.session_state.pontuacao = 0
if "logado_gerente" not in st.session_state:
  st.session_state.logado_gerente = False
if "ranking" not in st.session_state:
  st.session_state.ranking = [
      {"nome": "Kepler Silva", "pontos": 50},
      {"nome": "Hypatia Lima", "pontos": 40},
  ]

# Título Principal
st.markdown("<h1>🌌 Olimpíada Online de Cosmologia</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Plataforma oficial de"
    " avaliação e estudos sobre o Big Bang e o Universo.</p>",
    unsafe_allow_html=True,
)
st.divider()

# ==========================================
# MENU INICIAL (Escolha de Perfil)
# ==========================================
if st.session_state.modo == "menu":
  st.subheader("📌 Selecione o seu Perfil de Acesso:")

  col1, col2 = st.columns(2)

  with col1:
    st.markdown("### 👨‍🎓 Aluno / Concorrente")
    st.write(
        "Inscreva-se com seu nome, participe da olimpíada de perguntas e veja"
        " sua posição no ranking."
    )
    if st.button("Entrar como Aluno"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_aluno = "cadastro"
      st.rerun()

  with col2:
    st.markdown("### ⚙️ Gerente de Rede")
    st.write(
        "Área restrita ao organizador para gerenciar a plataforma, ver o"
        " ranking e resetar dados."
    )
    if st.button("Entrar como Gerente"):
      st.session_state.modo = "gerente"
      st.rerun()


# ==========================================
# FLUXO DO ALUNO
# ==========================================
elif st.session_state.modo == "aluno":

  if st.button("⬅️ Voltar ao Menu Principal"):
    st.session_state.modo = "menu"
    st.rerun()

  st.divider()

  # ETAPA: Cadastro do Aluno
  if st.session_state.etapa_aluno == "cadastro":
    st.subheader("📝 Inscrição do Aluno")
    nome_aluno = st.text_input("Digite seu Nome Completo para começar:")

    if st.button("🚀 Começar a Olimpíada"):
      if nome_aluno.strip() == "":
        st.warning("Por favor, digite um nome válido.")
      else:
        st.session_state.nome_usuario = nome_aluno.strip()
        st.session_state.etapa_aluno = "quiz"
        st.session_state.indice_pergunta = 0
        st.session_state.pontuacao = 0
        st.rerun()

  # ETAPA: Quiz
  elif st.session_state.etapa_aluno == "quiz":
    idx = st.session_state.indice_pergunta
    total_questoes = len(QUESTOES)

    st.write(
        f"**Concorrente:** 👤 {st.session_state.nome_usuario} | **Questão**"
        f" {idx + 1} de {total_questoes}"
    )
    st.progress((idx) / total_questoes)

    q = QUESTOES[idx]
    st.markdown(f"### {q['pergunta']}")

    for op in q["opcoes"]:
      if st.button(op, key=f"aluno_opt_{op}"):
        if op == q["resposta_correta"]:
          st.session_state.pontuacao += 10
          st.success("✨ Correto! Excelente raciocínio.")
        else:
          st.error(
              f"❌ Incorreto. A resposta correta era: **{q['resposta_correta']}**"
          )

        st.markdown(
            f"<div class='curiosidade-box'><b>💡 Curiosidade da"
            f" Questão:</b><br>{q['curiosidade']}</div>",
            unsafe_allow_html=True,
        )

        if st.button("Próxima Questão ➡️", key="btn_prox"):
          st.session_state.indice_pergunta += 1
          if st.session_state.indice_pergunta >= total_questoes:
            # Salva no ranking geral
            st.session_state.ranking.append({
                "nome": st.session_state.nome_usuario,
                "pontos": st.session_state.pontuacao,
            })
            st.session_state.ranking = sorted(
                st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
            )
            st.session_state.etapa_aluno = "resultado"
          st.rerun()
        st.stop()

  # ETAPA: Resultado e Ranking Parcial do Aluno
  elif st.session_state.etapa_aluno == "resultado":
    st.success("🎉 Parabéns por concluir a Olimpíada!")
    st.markdown(f"### 🏆 Sua Pontuação Final: {st.session_state.pontuacao} / 50")

    st.divider()
    st.subheader("📊 Ranking Geral Atualizado")
    for pos, c in enumerate(st.session_state.ranking[:10], start=1):
      medalha = (
          "🥇"
          if pos == 1
          else ("🥈" if pos == 2 else ("🥉" if pos == 3 else "🔸"))
      )
      st.markdown(
          f"**{medalha} {pos}º lugar:** {c['nome']} — **{c['pontos']} pts**"
      )

    st.divider()
    if st.button("🔄 Refazer / Novo Aluno"):
      st.session_state.etapa_aluno = "cadastro"
      st.session_state.nome_usuario = ""
      st.rerun()


# ==========================================
# FLUXO DO GERENTE (Painel Administrativo)
# ==========================================
elif st.session_state.modo == "gerente":

  if st.button("⬅️ Voltar ao Menu Principal"):
    st.session_state.modo = "menu"
    st.rerun()

  st.divider()
  st.markdown("<h2>⚙️ Painel de Controle do Gerente</h2>", unsafe_allow_html=True)

  # Sistema de Login do Gerente
  if not st.session_state.logado_gerente:
    with st.container():
      st.markdown(
          "<div class='admin-box'>🔒 <b>Área Restrita:</b> Digite as"
          " credenciais de organizador.</div>",
          unsafe_allow_html=True,
      )
      user_input = st.text_input("Usuário do Gerente:")
      pass_input = st.text_input("Senha:", type="password")

      if st.button("🔑 Entrar no Sistema"):
        if (
            user_input.strip() == "Felipe241198"
            and pass_input.strip() == "123456789"
        ):
          st.session_state.logado_gerente = True
          st.success("Login efetuado com sucesso! Carregando painel...")
          st.rerun()
        else:
          st.error("❌ Usuário ou senha incorretos.")
  else:
    st.success("✅ Sessão de Gerente Ativa (Felipe)")

    # Ferramentas do Gerente
    st.markdown("### 📊 Gerenciamento de Concorrentes e Alunos")
    st.write(
        "Aqui você acompanha todos os alunos que enviaram respostas e a"
        " classificação geral:"
    )

    if len(st.session_state.ranking) == 0:
      st.info("Nenhum aluno cadastrado no ranking até o momento.")
    else:
      for pos, c in enumerate(st.session_state.ranking, start=1):
        st.markdown(
            f"**{pos}º Colocado:** 👤 {c['nome']} — **{c['pontos']} pontos**"
        )

    st.divider()

    col_m1, col_m2 = st.columns(2)
    with col_m1:
      if st.button("🗑️ Limpar Todo o Ranking"):
        st.session_state.ranking = []
        st.success("Ranking limpo com sucesso!")
        st.rerun()

    with col_m2:
      if st.button("🔒 Sair (Logout do Gerente)"):
        st.session_state.logado_gerente = False
        st.session_state.modo = "menu"
        st.rerun()
