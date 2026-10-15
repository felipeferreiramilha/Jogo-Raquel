import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Investigação Cósmica: O Mistério do Big Bang",
    page_icon="🌌",
    layout="wide",
)

# Estilização Visual (Tema Espacial Sci-Fi Investigativo)
st.markdown(
    """
    <style>
    .stApp {
        background-color: #04040d;
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
        color: #04040d;
    }
    .pergunta-box {
        background-color: #09091d;
        border: 1px solid #ff00ff;
        padding: 20px;
        border-radius: 12px;
        margin-bottom: 20px;
    }
    .raquel-box {
        background-color: #150b2e;
        border: 2px solid #00ffff;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
    }
    .vilao-box {
        background-color: #2e0b0b;
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
# CASOS INVESTIGATIVOS (AULAS DA HISTÓRIA) COM RAQUEL E MAKARIUS THAIM
# =========================================================================

CASO_1 = [
    {
        "tipo": "hibrida",
        "pergunta": (
            "1. (Caso 1: O Início) Makarius Thaim tentou corromper os registros"
            " antigos afirmando que o cosmos sempre foi estático. Qual"
            " evidência histórica e matemática derruba a farsa de Makarius e"
            " prova o modelo do 'Átomo Primitivo' de Georges Lemaître?"
        ),
        "opcoes": [
            (
                "A prova de que a Via Láctea está parada no centro de um"
                " universo vazio."
            ),
            (
                "A dedução de que toda a matéria esteve concentrada em um"
                " quantum superdenso que deu início à expansão."
            ),
            (
                "A criação de um campo magnético eterno que impede qualquer"
                " mudança cósmica."
            ),
            (
                "A teoria de que o Sol é a única estrela real do universo"
                " conhecido."
            ),
        ],
        "resposta_correta": (
            "A dedução de que toda a matéria esteve concentrada em um quantum"
            " superdenso que deu início à expansão."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Agente, o Makarius quer nos enganar! Lemaître"
            " combinou física e astúcia para mostrar que o universo evolui a"
            " partir de um início denso.'"
        ),
        "ameaca_makarius": (
            "😈 **Makarius Thaim sussurra:** 'Tolhinhos... Um universo estático"
            " e sem começo é muito mais confortável para o meu Vazio!"
            " Vocês jamais provarão o contrário!'"
        ),
        "indicacao": (
            "🎥 **Relatório de Apoio da Raquel:** Estude a história do"
            " *Átomo Primitivo* no portal da [NASA Science -"
            " Universe](https://science.nasa.gov/universe/)."
        ),
    },
    {
        "tipo": "hibrida",
        "pergunta": (
            "2. (Caso 1: O Paradoxo) Makarius Thaim espalhou trevas nas"
            " anotações de Heinrich Olbers. O que o Paradoxo de Olbers"
            " realmente revela sobre a estrutura do cosmos?"
        ),
        "opcoes": [
            (
                "Que o céu noturno é escuro justamente porque o universo é"
                " dinâmico, finito em idade e teve um começo (o Big Bang)."
            ),
            ("Que as estrelas da noite emitem apenas luz invisível aos olhos."),
            ("Que a luz das galáxias é bloqueada por espelhos cósmicos secretos."),
            (
                "Que a Via Láctea bloqueia todas as estrelas do universo do"
                " lado norte."
            ),
        ],
        "resposta_correta": (
            "Que o céu noturno é escuro justamente porque o universo é dinâmico,"
            " finito em idade e teve um começo (o Big Bang)."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Se o universo fosse eterno e infinito, o céu"
            " brilharia como o Sol! O fato de ser escuro é a nossa maior pista"
            " contra o Makarius!'"
        ),
        "ameaca_makarius": (
            "😈 **Makarius Thaim sussurra:** 'A escuridão da noite é minha"
            " aliada, agentes! Vocês nunca decifrarão o enigma de Olbers!'"
        ),
        "indicacao": (
            "📖 **Relatório de Apoio da Raquel:** Pesquise artigos sobre o"
            " *Paradoxo de Olbers* no site do [Observatório"
            " Nacional](https://www.gov.br/mcti/pt-br/acompanhe-o-mcti/on)."
        ),
    },
    {
        "tipo": "dissertativa",
        "pergunta": (
            "3. (Caso 1 - Relatório Investigativo) Escreva em detalhes o seu"
            " relatório para a base, explicando com suas palavras como a"
            " ciência desmascarou o mito do universo estático e formulou a"
            " teoria do Big Bang."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Monte um relatório impecável, agente! Mostre"
            " como a humanidade superou a visão antiga de um céu imóvel.'"
        ),
        "ameaca_makarius": (
            "😈 **Makarius Thaim sussurra:** 'Escrevam o que quiserem nos seus"
            " relatórios de papel, o tempo apagará todas as provas!'"
        ),
        "indicacao": (
            "🎥 **Relatório de Apoio da Raquel:** Assista a documentários sobre"
            " *A Origem do Tempo*."
        ),
    },
]

CASO_2 = [
    {
        "tipo": "hibrida",
        "pergunta": (
            "1. (Caso 2: A Expansão) Makarius Thaim sabotou os instrumentos de"
            " Edwin Hubble para esconder a verdade. O que a Lei de Hubble"
            " prova sobre o tecido do cosmos?"
        ),
        "opcoes": [
            (
                "Que as galáxias distantes se afastam umas das outras porque o"
                " próprio espaço está se expandindo."
            ),
            ("Que a Terra está navegando em alta velocidade pelo espaço."),
            ("Que as galáxias estão caindo em direção a um buraco negro central."),
            ("Que o universo está girando como um pião em volta de Andrômeda."),
        ],
        "resposta_correta": (
            "Que as galáxias distantes se afastam umas das outras porque o"
            " próprio espaço está se expandindo."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Não caia na armadilha do Makarius! As"
            " galáxias não correm pelo espaço, é o espaço entre elas que estica!'"
        ),
        "ameaca_makarius": (
            "😈 **Makarius Thaim sussurra:** 'Acelerar a expansão é minha"
            " especialidade... Vou esticar tudo até virar pó frio e vazio!'"
        ),
        "indicacao": (
            "🎥 **Relatório de Apoio da Raquel:** Analise os dados da"
            " [ESA](https://www.esa.int/) sobre a expansão cósmica."
        ),
    },
    {
        "tipo": "dissertativa",
        "pergunta": (
            "2. (Caso 2 - Relatório Investigativo) Descreva a analogia do balão"
            " com pontinhos na superfície para explicar ao quartel-general por"
            " que a expansão cósmica não tem um centro fixo."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Use o exemplo do balão de aniversário que"
            " usamos na investigação anterior, agente! Nenhum ponto é o"
            " centro.'"
        ),
        "ameaca_makarius": (
            "😈 **Makarius Thaim sussurra:** 'Balões estouram, agentes... e o"
            " cosmo de vocês também vai estourar!'"
        ),
        "indicacao": (
            "📖 **Relatório de Apoio da Raquel:** Leia publicações de"
            " divulgação do IAG-USP sobre o *Redshift*."
        ),
    },
]

CASO_3 = [
    {
        "tipo": "hibrida",
        "pergunta": (
            "1. (Caso 3: Matéria e Energia Escura) Makarius Thaim tentou apagar"
            " as curvas de rotação galáctica para ocultar sua presença. O"
            " que prova a existência da Matéria Escura?"
        ),
        "opcoes": [
            (
                "As estrelas periféricas giram rápido demais, exigindo um halo"
                " gravitacional de massa invisível."
            ),
            ("O centro da galáxia brilha com luz verde fluorescente e tóxica."),
            ("A expansão do universo empurra as estrelas para fora das órbitas."),
            ("O gás estelar consome toda a gravidade das bordas galácticas."),
        ],
        "resposta_correta": (
            "As estrelas periféricas giram rápido demais, exigindo um halo"
            " gravitacional de massa invisível."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'O Makarius adora se esconder nas sombras, mas"
            " a gravidade extra nas bordas das galáxias entregou o esconderijo"
            " dele! É a Matéria Escura!'"
        ),
        "ameaca_makarius": (
            "😈 **Makarius Thaim sussurra:** 'Vocês ousam investigar minhas"
            " sombras? A Matéria Escura é o meu manto, e a Energia Escura é a"
            " minha espada!'"
        ),
        "indicacao": (
            "🎥 **Relatório de Apoio da Raquel:** Explore o portal [NASA"
            " Science - Dark Matter]"
            "(https://science.nasa.gov/universe/)."
        ),
    },
    {
        "tipo": "hibrida",
        "pergunta": (
            "2. (Caso 3: O Destino Final) Qual é a diferença fundamental"
            " entre a Matéria Escura e a Energia Escura na grande batalha do"
            " universo?"
        ),
        "opcoes": [
            (
                "A Matéria Escura atrai e une as estruturas; a Energia Escura"
                " repele e acelera a expansão cósmica."
            ),
            ("A Matéria Escura emite raios X; a Energia Escura congela o tempo."),
            ("A Matéria Escura é visível aos telescópios; a Energia Escura é um"
             " planeta rochoso."),
            ("Elas fazem exatamente a mesma coisa para o universo."),
        ],
        "resposta_correta": (
            "A Matéria Escura atrai e une as estruturas; a Energia Escura"
            " repele e acelera a expansão cósmica."
        ),
        "dica_raquel": (
            "👧 **Raquel diz:** 'Uma segura o tecido cósmico com atração"
            " gravitacional, enquanto a outra empurra tudo para longe. Uma"
            " verdadeira disputa cósmica!'"
        ),
        "ameaca_makarius": (
            "😈 **Makarius Thaim sussurra:** 'No fim, minha Energia Escura"
            " vencerá! O Big Freeze consumirá cada estrela, e eu reinarei"
            " sozinho!'"
        ),
        "indicacao": (
            "📖 **Relatório de Apoio da Raquel:** Estude os relatórios da"
            " expansão acelerada no site oficial da NASA."
        ),
    },
]

# =========================================================================
# GERENCIAMENTO DE ESTADO DA SESSÃO
# =========================================================================
if "modo" not in st.session_state:
  st.session_state.modo = "menu"
if "etapa_agente" not in st.session_state:
  st.session_state.etapa_agente = "escolha_caso"
if "caso_escolhido" not in st.session_state:
  st.session_state.caso_escolhido = ""
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
      {"nome": "Agente Felipe", "caso": "Caso 1", "pontos": 2},
      {"nome": "Raquel (Heroína Líder)", "caso": "Caso 3", "pontos": 2},
  ]

# Título Principal
st.markdown(
    "<h1>🌌 Investigação Cósmica: O Desafio contra Makarius Thaim</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Junto com a heroína Raquel,"
    " investigue os segredos do Big Bang e derrote o vilão Makarius"
    " Thaim!</p>",
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
        "Entre na espaçonave, escolha seu caso investigativo com a Raquel e"
        " derrote Makarius Thaim!"
    )
    if st.button("Entrar como Agente"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_agente = "escolha_caso"
      st.rerun()

  with col_m2:
    st.markdown("### ⚙️ Área do Gerente (Quartel-General)")
    st.write(
        "Acesso restrito ao organizador com credenciais para inspecionar os"
        " relatórios e o ranking."
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

  # ETAPA 1: Identificação e Escolha do Caso
  if st.session_state.etapa_agente == "escolha_caso":
    st.subheader("🎯 Passo 1: Credenciamento do Agente e Seleção do Caso")
    nome_input = st.text_input("Digite seu Nome de Agente ou Apelido:")

    st.markdown("### Selecione o Caso Cósmico para Investigar:")
    caso_sel = st.selectbox(
        "Caso:",
        [
            "Caso 1: O Início do Cosmos e o Átomo Primitivo",
            "Caso 2: A Grande Expansão do Espaço-Tempo",
            "Caso 3: O Mistério da Matéria e Energia Escura",
        ],
    )

    if st.button("🚀 Iniciar Missão com a Raquel"):
      if nome_input.strip() == "":
        st.warning("Por favor, digite um nome de agente válido.")
      else:
        st.session_state.nome_usuario = nome_input.strip()
        st.session_state.caso_escolhido = caso_sel

        if "Caso 1" in caso_sel:
          st.session_state.questoes_sessao = list(CASO_1)
        elif "Caso 2" in caso_sel:
          st.session_state.questoes_sessao = list(CASO_2)
        else:
          st.session_state.questoes_sessao = list(CASO_3)

        st.session_state.indice_pergunta = 0
        st.session_state.respostas_usuario = []
        st.session_state.etapa_agente = "missao"
        st.rerun()

  # ETAPA 2: Missão Investigativa (Painel da Raquel e Ameaças de Makarius)
  elif st.session_state.etapa_agente == "missao":
    idx = st.session_state.indice_pergunta
    total_q = len(st.session_state.questoes_sessao)
    q_atual = st.session_state.questoes_sessao[idx]

    st.write(
        f"🕵️‍♂️ **Agente:** {st.session_state.nome_usuario} | 📁 **Missão:**"
        f" {st.session_state.caso_escolhido} | **Pista {idx + 1} de"
        f" {total_q}**"
    )
    st.progress((idx) / total_q)

    # Layout de Duas Colunas: Esquerda (Pista e Investigação), Direita (Apoio da Raquel & Vilão)
    col_q, col_r = st.columns([2, 1])

    with col_r:
      st.markdown(
          f"""
            <div class='raquel-box'>
                <h3 style='margin:0; color:#00ffff;'>👧 Raquel, a Heroína</h3>
                <p style='margin-top:10px; font-size:14px;'>{q_atual['dica_raquel']}</p>
                <hr style='border-color: #333;'>
                <p style='font-size:12px; color:#ccc;'>{q_atual['indicacao']}</p>
            </div>
            """,
          unsafe_allow_html=True,
      )

      st.markdown(
          f"""
            <div class='vilao-box'>
                <h3 style='margin:0; color:#ff3333;'>😈 Makarius Thaim</h3>
                <p style='margin-top:10px; font-size:13px; font-style:italic;'>{q_atual['ameaca_makarius']}</p>
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
        escolha_agente = st.radio(
            "Selecione a evidência científica correta:",
            q_atual["opcoes"],
            key=f"opt_{idx}",
        )
        st.markdown("<br>", unsafe_allow_html=True)
        relatorio_agente = st.text_area(
            "✍️ Relatório de Investigação (Justifique sua escolha com suas"
            " palavras):",
            key=f"exp_{idx}",
            placeholder=(
                "Escreva os detalhes da sua dedução investigativa aqui..."
            ),
        )
      else:
        escolha_agente = "Relatório Descritivo de Missão"
        relatorio_agente = st.text_area(
            "✍️ Escreva seu relatório investigativo completo sobre o caso:",
            key=f"text_{idx}",
            placeholder="Descreva a conclusão da investigação...",
        )

    st.divider()
    c_btn1, c_btn2 = st.columns(2)
    with c_btn2:
      if st.button("Enviar Pista e Avançar ➡️"):
        if not relatorio_agente.strip():
          st.warning(
              "Agente, você precisa preencher o relatório investigativo antes"
              " de prosseguir!"
          )
        else:
          correta = (
              q_atual["resposta_correta"]
              if q_atual["tipo"] == "hibrida"
              else "Relatório Descritivo"
          )
          is_acerto = (
              (escolha_agente == q_atual["resposta_correta"])
              if q_atual["tipo"] == "hibrida"
              else True
          )

          st.session_state.respostas_usuario.append({
              "pergunta": q_atual["pergunta"],
              "escolhida": escolha_agente,
              "relatorio": relatorio_agente,
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
                "caso": st.session_state.caso_escolhido.split(":")[0],
                "pontos": pontos,
            })
            st.session_state.ranking = sorted(
                st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
            )
            st.session_state.etapa_agente = "resultado"
          st.rerun()

  # ETAPA 3: Fim da Missão, Relatório Final e Derrota de Makarius
  elif st.session_state.etapa_agente == "resultado":
    st.success(
        "🎉 Missão Concluída! Você e a Raquel derrotaram as trapaças de"
        " Makarius Thaim!"
    )

    pontos = sum(
        1 for r in st.session_state.respostas_usuario if r["acertou"]
    )
    total_q = len(st.session_state.questoes_sessao)
    st.markdown(
        f"### 🏆 Desempenho do Agente: {pontos} de {total_q} Pistas Solucionadas"
    )

    if pontos <= 1:
      patente = (
          "🎖️ **Investigador(a) Estelar Iniciante** (Raquel diz: Bom trabalho"
          " agente, mas Makarius quase nos pegou! Vamos revisar os arquivos.)"
      )
    elif pontos == 2:
      patente = (
          "🏅 **Detetive do Espaço-Tempo** (Raquel diz: Excelente dedução!"
          " Desmascaramos o plano de Makarius com sucesso.)"
      )
    else:
      patente = (
          "🌟 **Comandante Supremo do Cosmos** (Raquel diz: Perfeito!"
          " Salvamos o Big Bang e expulsamos Makarius para o Vazio Absoluto!)"
      )

    st.markdown(f"### Sua Patente Cósmica: {patente}")
    st.divider()

    st.subheader(
        "📁 Relatório Oficial de Investigação, Gabarito e Justificativas"
    )
    for i, resp in enumerate(st.session_state.respostas_usuario, start=1):
      st.markdown(f"**Pista {i}:** {resp['pergunta']}")
      if resp["correta"] != "Relatório Descritivo":
        icon = "✅" if resp["escolhida"] == resp["correta"] else "❌"
        st.markdown(f"- Evidência selecionada: {resp['escolhida']} {icon}")
        if resp["escolhida"] != resp["correta"]:
          st.markdown(
              f"- 💡 **Evidência Científica Correta:** `{resp['correta']}`"
          )
      st.markdown(f"- ✍️ *Seu relatório:* {resp['relatorio']}")
      st.markdown("---")

    st.subheader("📊 Ranking Geral de Agentes Investigativos")
    for pos, c in enumerate(st.session_state.ranking[:10], start=1):
      medalha = (
          "🥇"
          if pos == 1
          else ("🥈" if pos == 2 else ("🥉" if pos == 3 else "🔸"))
      )
      st.markdown(
          f"**{medalha} {pos}º lugar:** {c['nome']} ({c['caso']}) —"
          f" **{c['pontos']} pts**"
      )

    st.divider()
    if st.button("🔄 Nova Missão / Escolher Outro Caso"):
      st.session_state.etapa_agente = "escolha_caso"
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

    st.subheader("📊 Relatório de Agentes em Missão")
    if len(st.session_state.ranking) == 0:
      st.info("Nenhum agente registrou relatórios de missão ainda.")
    else:
      for pos, c in enumerate(st.session_state.ranking, start=1):
        st.markdown(
            f"**{pos}º:** 🕵️‍♂️ {c['nome']} | **Missão:** {c['caso']} |"
            f" **Pontos:** {c['pontos']}"
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
