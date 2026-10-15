import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Olimpíada de Cosmologia e Big Bang",
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

# Inicialização do Estado da Sessão
if "etapa" not in st.session_state:
  st.session_state.etapa = "cadastro"  # cadastro, quiz, resultado
if "nome_usuario" not in st.session_state:
  st.session_state.nome_usuario = ""
if "indice_pergunta" not in st.session_state:
  st.session_state.indice_pergunta = 0
if "pontuacao" not in st.session_state:
  st.session_state.pontuacao = 0
if "ranking" not in st.session_state:
  # Ranking simulado inicial para você ver os concorrentes
  st.session_state.ranking = [
      {"nome": "Kepler Silva", "pontos": 50},
      {"nome": "Hypatia Lima", "pontos": 40},
      {"nome": "Carl Sagan Jr.", "pontos": 30},
  ]

# Título Principal
st.markdown("<h1>🌌 Olimpíada Online de Cosmologia</h1>", unsafe_allow_html=True)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Teste seus conhecimentos"
    " sobre o Big Bang, História da Física e Teoria do Universo!</p>",
    unsafe_allow_html=True,
)
st.divider()

# ETAPA 1: Cadastro do Participante
if st.session_state.etapa == "cadastro":
  st.subheader("📝 Identificação do Concorrente")
  nome = st.text_input(
      "Digite seu Nome Completo ou Apelido para entrar na Competição:"
  )

  if st.button("🚀 Iniciar Olimpíada"):
    if nome.strip() == "":
      st.warning("Por favor, digite um nome válido para continuar.")
    else:
      st.session_state.nome_usuario = nome.strip()
      st.session_state.etapa = "quiz"
      st.session_state.indice_pergunta = 0
      st.session_state.pontuacao = 0
      st.rerun()

# ETAPA 2: O Quiz Interativo
elif st.session_state.etapa == "quiz":
  idx = st.session_state.indice_pergunta
  total_questoes = len(QUESTOES)

  st.write(
      f"**Concorrente:** 👤 {st.session_state.nome_usuario} | **Questão**"
      f" {idx + 1} de {total_questoes}"
  )
  st.progress((idx) / total_questoes)

  q = QUESTOES[idx]
  st.markdown(f"### {q['pergunta']}")

  # Opções de resposta em botões
  for op in q["opcoes"]:
    if st.button(op, key=f"opt_{op}"):
      # Avalia a resposta
      if op == q["resposta_correta"]:
        st.session_state.pontuacao += 10
        st.success("✨ Correto! Excelente raciocínio cosmológico.")
      else:
        st.error(
            f"❌ Incorreto. A resposta correta era: **{q['resposta_correta']}**"
        )

      # Exibe Curiosidade Científica da Questão
      st.markdown(
          f"<div class='curiosidade-box'><b>💡 Curiosidade da"
          f" Questão:</b><br>{q['curiosidade']}</div>",
          unsafe_allow_html=True,
      )

      # Botão para avançar
      if st.button("Próxima Questão ➡️"):
        st.session_state.indice_pergunta += 1
        if st.session_state.indice_pergunta >= total_questoes:
          # Fim do quiz: insere no ranking
          st.session_state.ranking.append({
              "nome": st.session_state.nome_usuario,
              "pontos": st.session_state.pontuacao,
          })
          # Ordena o ranking por pontuação (maior para menor)
          st.session_state.ranking = sorted(
              st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
          )
          st.session_state.etapa = "resultado"
        st.rerun()
      st.stop()

# ETAPA 3: Resultados Finais e Ranking dos Concorrentes
elif st.session_state.etapa == "resultado":
  st.success("🎉 Olimpíada Concluída com Sucesso!")
  st.markdown(f"### 🏆 Sua Pontuação Final: {st.session_state.pontuacao} / 50")

  if st.session_state.pontuacao >= 40:
    st.markdown(
        "🌟 **Classificação: Astrônomo(a) Sênior!** Você domina profundamente"
        " os mistérios do Big Bang."
    )
  elif st.session_state.pontuacao >= 20:
    st.markdown(
        "🔭 **Classificação: Explorador(a) do Cosmo!** Tem uma boa base, vale"
        " a pena aprofundar nas teorias."
    )
  else:
    st.markdown(
        "📚 **Classificação: Cadete Estelar!** Continue estudando as origens do"
        " universo."
    )

  st.divider()

  # Exibição do Ranking de Concorrentes
  st.subheader("📊 Ranking Geral de Concorrentes")
  st.write(
      "Veja abaixo a posição de todos os participantes que concluíram a"
      " olimpíada:"
  )

  for rank_pos, concorrente in enumerate(
      st.session_state.ranking[:10], start=1
  ):
    medalha = (
        "🥇"
        if rank_pos == 1
        else ("🥈" if rank_pos == 2 else ("🥉" if rank_pos == 3 else "🔸"))
    )
    st.markdown(
        f"**{medalha} {rank_pos}º lugar:** {concorrente['nome']} —"
        f" **{concorrente['pontos']} pontos**"
    )

  st.divider()

  # Sites recomendados para Pesquisa e Aprofundamento
  st.subheader("🔗 Sites Recomendados para Pesquisa em Cosmologia")
  st.markdown(
      "- [NASA Science - Big Bang & Universe"
      " (Inglês)](https://science.nasa.gov/universe/)"
  )
  st.markdown(
      "- [European Space Agency (ESA) - Cosmology"
      " (Inglês)](https://www.esa.int/Science_Exploration/Space_Science/Herschel/Cosmology)"
  )
  st.markdown(
      "- [Portal de Astronomia do Observatório Nacional"
      " (Brasil)](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/on)"
  )
  st.markdown(
      "- [Astronomia no USP (Divulgação Científica)]"
      "(https://www.astro.iag.usp.br/)"
  )

  st.divider()

  c1, c2 = st.columns(2)
  with c1:
    if st.button("🔄 Jogar Novamente"):
      st.session_state.etapa = "cadastro"
      st.session_state.nome_usuario = ""
      st.rerun()
  with c2:
    if st.button("🗑️ Limpar Ranking e Recomeçar"):
      st.session_state.ranking = []
      st.session_state.etapa = "cadastro"
      st.rerun()
