import random
import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Investigação Cósmica: O Segredo de Makarius Tahim",
    page_icon="🌌",
    layout="wide",
)

# Estilização Visual (Tema Sci-Fi Investigativo)
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
    .texto-base-box {
        background-color: #0b0b1c;
        border-left: 5px solid #00ffff;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        font-size: 16px;
        line-height: 1.5;
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
        background-color: #260a0a;
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
# BANCO DE CASOS INVESTIGATIVOS BASEADOS EM TEXTOS E BLOQUEIO POR ERRO
# =========================================================================

CASOS_INVESTIGACAO = [
    {
        "id": 1,
        "titulo": "Caso 1: O Texto do Átomo Primitivo e a Queda do Dogma Estático",
        "texto_base": (
            "📜 **Arquivo Histórico nº 01:** Durante séculos, a humanidade e"
            " grandes mentes aceitavam um universo estático, eterno e sem"
            " mudanças estruturais globais. No entanto, em 1927, o físico e"
            " padre Georges Lemaître analisou as equações de Einstein e"
            " propôs que o universo não era imutável. Ele deduziu que, voltando"
            " o tempo no passado, toda a matéria e energia estariam reunidas"
            " em um 'Átomo Primitivo' superdenso, cujo colapso e explosão"
            " inicial deram origem ao espaço e ao tempo — o que mais tarde"
            " seria chamado de Big Bang. Makarius Tahim, o enigma cósmico,"
            " tentou corromper este arquivo para manter o cosmo paralisado na"
            " ilusão estática."
        ),
        # Questão Inicial
        "pergunta_inicial": {
            "enunciado": (
                "Com base no Arquivo Histórico nº 01, qual foi a principal"
                " ruptura conceitual introduzida por Georges Lemaître contra"
                " o modelo estático?"
            ),
            "opcoes": [
                (
                    "Afirmar que a Via Láctea era o centro gravitacional"
                    " absoluto do universo."
                ),
                (
                    "Propor que o universo teve um início dinâmico a partir"
                    " de um ponto superdenso ('Átomo Primitivo') e está em"
                    " expansão."
                ),
                (
                    "Provar que o tempo é estático e que o passado e o futuro"
                    " coexistem simultaneamente sem alteração."
                ),
                (
                    "Demonstrar que o espaço é preenchido por um fluido fixo"
                    " chamado éter luminoso."
                ),
            ],
            "correta": (
                "Propor que o universo teve um início dinâmico a partir de um"
                " ponto superdenso ('Átomo Primitivo') e está em expansão."
            ),
        },
        # Pergunta de Resgate caso o aluno erre (Bloqueio)
        "pergunta_resgate": {
            "enunciado": (
                "⚠️ **Alerta de Segurança da Raquel:** Você errou a dedução"
                " principal! Releia o texto: o que Lemaître defendeu sobre a"
                " origem do cosmos para contrariar o universo estático?"
            ),
            "opcoes": [
                (
                    "Que o cosmos nasceu de um estado inicial hiperdenso e"
                    " iniciou sua expansão contínua."
                ),
                ("Que as estrelas nunca mudam de posição ao longo dos eras."),
                ("Que o universo foi criado sem espaço nem tempo fixos."),
                ("Que a matéria surge espontaneamente no vácuo estático."),
            ],
            "correta": (
                "Que o cosmos nasceu de um estado inicial hiperdenso e iniciou"
                " sua expansão contínua."
            ),
        },
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Agente, preste muita atenção nas"
            " evidências do texto. Makarius quer que a gente acredite que"
            " nada começou, mas Lemaître provou o contrário!'"
        ),
        "comentario_makarius": (
            "😈 **Makarius Tahim sussurra:** 'Vocês ousam desafiar a imutabilidade"
            " do Vazio? Tentem passar por esta pista se tiverem capacidade!'"
        ),
    },
    {
        "id": 2,
        "titulo": "Caso 2: O Texto da Expansão e o Desvio para o Vermelho",
        "texto_base": (
            "📜 **Arquivo Histórico nº 02:** Na década de 1920, o astrônomo"
            " Edwin Hubble fez uma descoberta que abalou a ciência: ao"
            " analisar a luz de galáxias distantes, ele percebeu que o"
            " comprimento de onda dessa luz estava esticado em direção ao"
            " espectro avermelhado (o chamado *redshift* ou desvio para o"
            " vermelho). Isso indicava que as galáxias estavam se afastando"
            " de nós. Mas a verdadeira sacada cosmológica não era que elas"
            " corriam pelo espaço, e sim que o próprio tecido do espaço-tempo"
            " estava se esticando, afastando todas as regiões entre si"
            " proporcionalmente à distância. Makarius Tahim tentou distorcer"
            " esses dados para fazer parecer que o universo estava encolhendo"
            " em direção a um colapso prematuro."
        ),
        "pergunta_inicial": {
            "enunciado": (
                "De acordo com o Arquivo Histórico nº 02, o que o desvio para"
                " o vermelho (*redshift*) das galáxias distantes realmente"
                " significa sobre o cosmos?"
            ),
            "opcoes": [
                (
                    "Que as galáxias estão correndo em alta velocidade dentro"
                    " de um espaço rígido e imóvel."
                ),
                (
                    "Que o próprio tecido do espaço-tempo está se esticando,"
                    " fazendo com que o universo se expanda."
                ),
                (
                    "Que as estrelas estão esfriando e emitindo apenas luz"
                    " vermelha por envelhecimento."
                ),
                (
                    "Que o universo está encolhendo em direção ao centro da"
                    " Via Láctea."
                ),
            ],
            "correta": (
                "Que o próprio tecido do espaço-tempo está se esticando, fazendo"
                " com que o universo se expanda."
            ),
        },
        "pergunta_resgate": {
            "enunciado": (
                "⚠️ **Alerta de Resgate da Raquel:** Atenção! O desvio para o"
                " vermelho não é sobre as galáxias 'correndo' no espaço. Qual"
                " é o fenômeno real descrito no texto?"
            ),
            "opcoes": [
                (
                    "O estiramento do próprio espaço entre as galáxias,"
                    " provando a expansão cósmica."
                ),
                ("O reflexo da luz do Sol nas lentes dos telescópios."),
                ("A absorção de luz por nuvens de poeira escura."),
                ("A rotação acelerada do núcleo de Andrômeda."),
            ],
            "correta": (
                "O estiramento do próprio espaço entre as galáxias, provando a"
                " expansão cósmica."
            ),
        },
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Lembre-se da nossa analogia do balão,"
            " agente! O espaço é que estica, e a luz estica junto com ele!'"
        ),
        "comentario_makarius": (
            "😈 **Makarius Tahim sussurra:** 'O tecido do espaço é frágil... Eu"
            " posso rasgá-lo a qualquer momento se vocês falharem na"
            " investigação!'"
        ),
    },
    {
        "id": 3,
        "titulo": "Caso 3: O Texto da Matéria Escura e da Energia Escura",
        "texto_base": (
            "📜 **Arquivo Histórico nº 03:** Ao mapear a velocidade de rotação"
            " das estrelas nas bordas das galáxias espirais, os cientistas"
            " descobriram um grande mistério: as estrelas giravam rápido demais"
            " para a quantidade de matéria luminosa visível. Se houvesse"
            " apenas gás e estrelas, a gravidade seria fraca e elas se"
            " dispersariam. Era necessária uma massa invisível — a Matéria"
            " Escura —, que atrai e une as estruturas cósmicas. Por outro"
            " lado, descobriu-se que a expansão do universo não está freando,"
            " mas sim acelerando devido a uma pressão de vácuo repulsiva chamada"
            " Energia Escura. Makarius Tahim se escondeu atrás dessas forças"
            " invisíveis para fingir ser o mestre absoluto do caos."
        ),
        "pergunta_inicial": {
            "enunciado": (
                "Com base no Arquivo Histórico nº 03, qual é a principal"
                " diferença funcional entre a Matéria Escura e a Energia Escura"
                " na evolução do universo?"
            ),
            "opcoes": [
                (
                    "A Matéria Escura atrai gravitacionalmente e ajuda a unir"
                    " as estruturas; a Energia Escura atua repelindo e"
                    " acelerando a expansão cósmica."
                ),
                (
                    "A Matéria Escura emite raios gama; a Energia Escura cria"
                    " estrelas azuis."
                ),
                (
                    "A Matéria Escura existe apenas na Terra; a Energia Escura"
                    " fica no centro do Sol."
                ),
                (
                    "Ambas exercem exatamente a mesma força de atração em todo"
                    " o cosmo."
                ),
            ],
            "correta": (
                "A Matéria Escura atrai gravitacionalmente e ajuda a unir as"
                " estruturas; a Energia Escura atua repelindo e acelerando a"
                " expansão cósmica."
            ),
        },
        "pergunta_resgate": {
            "enunciado": (
                "⚠️ **Alerta Crítico da Raquel:** Cuidado! Não confunda os"
                " papéis das duas forças invisíveis. O que cada uma faz de"
                " acordo com o texto?"
            ),
            "opcoes": [
                (
                    "Uma aglutina massa (Matéria Escura) e a outra acelera a"
                    " expansão (Energia Escura)."
                ),
                ("Uma congela o tempo e a outra derrete os buracos negros."),
                ("Uma ilumina as galáxias e a outra cria cometas."),
                ("Ambas destroem o espaço imediatamente."),
            ],
            "correta": (
                "Uma aglutina massa (Matéria Escura) e a outra acelera a expansão"
                " (Energia Escura)."
            ),
        },
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Esta é a última pista crítica,"
            " agente! Entenda bem o papel de cada força invisível para"
            " desmascarar o Makarius!'"
        ),
        "comentario_makarius": (
            "😈 **Makarius Tahim sussurra:** 'Vocês estão chegando perto do"
            " santuário final... Mas minhas sombras não cederão tão fácil!'"
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
if "em_resgate" not in st.session_state:
  st.session_state.em_resgate = False  # Controle se errou e está na pergunta de resgate bloqueante
if "nome_usuario" not in st.session_state:
  st.session_state.nome_usuario = ""
if "respostas_agente" not in st.session_state:
  st.session_state.respostas_agente = []
if "logado_gerente" not in st.session_state:
  st.session_state.logado_gerente = False
if "ranking" not in st.session_state:
  st.session_state.ranking = [
      {"nome": "Agente Felipe", "status": "Concluído", "pontos": 3},
      {
          "nome": "Raquel Ferreira (Heroína)",
          "status": "Comandante",
          "pontos": 3,
      },
  ]

# Título Principal
st.markdown(
    "<h1>🌌 Investigação Cósmica: O Segredo de Makarius Tahim</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: #aaa;'>Investigue os textos"
    " históricos, supere os bloqueios ao errar e descubra a verdadeira face"
    " de Makarius Tahim junto com Raquel Ferreira!</p>",
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
        "Inicie sua investigação baseada em textos, resolva os casos e desvende"
        " o mistério final!"
    )
    if st.button("Entrar como Agente"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.em_resgate = False
      st.session_state.respostas_agente = []
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

  # Se ainda não inseriu o nome
  if (
      st.session_state.nome_usuario == ""
      and st.session_state.etapa_agente == "investigacao"
  ):
    st.subheader("🎯 Credenciamento do Agente Investigativo")
    nome_input = st.text_input("Digite seu Nome de Agente ou Apelido:")
    if st.button("🚀 Entrar no Laboratório de Investigação"):
      if nome_input.strip() == "":
        st.warning("Por favor, digite um nome válido.")
      else:
        st.session_state.nome_usuario = nome_input.strip()
        st.rerun()
    st.stop()

  # ETAPA DE INVESTIGAÇÃO (CASOS 1, 2 e 3 COM BLOQUEIO POR ERRO)
  if st.session_state.etapa_agente == "investigacao":
    idx = st.session_state.indice_caso
    total_casos = len(CASOS_INVESTIGACAO)

    if idx < total_casos:
      caso_atual = CASOS_INVESTIGACAO[idx]

      st.markdown(f"<h2>📁 {caso_atual['titulo']}</h2>", unsafe_allow_html=True)
      st.write(
          f"🕵️‍♂️ **Agente:** {st.session_state.nome_usuario} | **Progresso da"
          f" Investigação:** Pista {idx + 1} de {total_casos}"
      )
      st.progress((idx) / total_casos)

      # Exibição do Texto Base de Investigação
      st.markdown(
          f"<div class='texto-base-box'>{caso_atual['texto_base']}</div>",
          unsafe_allow_html=True,
      )

      # Layout Lateral: Esquerda (Questão), Direita (Raquel e Vilão)
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
                    <h3 style='margin:0; color:#ff3333;'>😈 Makarius Tahim</h3>
                    <p style='margin-top:8px; font-size:13px; font-style:italic;'>{caso_atual['comentario_makarius']}</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with col_q:
        # Define se mostra a pergunta inicial ou a pergunta de resgate (caso tenha errado antes)
        if not st.session_state.em_resgate:
          q_ativa = caso_atual["pergunta_inicial"]
          modo_pergunta = "inicial"
        else:
          q_ativa = caso_atual["pergunta_resgate"]
          modo_pergunta = "resgate"

        st.markdown(
            f"<div class='pergunta-box'><h4>{q_ativa['enunciado']}</h4></div>",
            unsafe_allow_html=True,
        )

        escolha_agente = st.radio(
            "Selecione a dedução investigativa correta:",
            q_ativa["opcoes"],
            key=f"radio_caso_{idx}_{modo_pergunta}",
        )

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔒 Validar Evidência e Avançar"):
          if escolha_agente == q_ativa["correta"]:
            # ACERTOU!
            st.success(
                "✨ Evidência validada com sucesso! Pista desvendada com"
                " êxito."
            )
            st.session_state.respostas_agente.append({
                "caso": caso_atual["titulo"],
                "status": "Acertado",
            })
            st.session_state.em_resgate = (
                False  # Reseta o resgate para o próximo caso
            )
            st.session_state.indice_caso += 1
            st.rerun()
          else:
            # ERROU! BLOQUEIO ATIVO
            if not st.session_state.em_resgate:
              st.session_state.em_resgate = True
              st.error(
                  "❌ **Evidência Incorreta!** Makarius Tahim bloqueou sua"
                  " passagem. Você não pode avançar enquanto não decifrar a"
                  " pista correta. Leia atentamente o aviso da Raquel e tente"
                  " novamente!"
              )
              st.rerun()
            else:
              st.error(
                  "❌ Errado novamente! A pista continua bloqueada. Concentre-se"
                  " no texto e na dica da Raquel para superar o obstáculo de"
                  " Makarius."
              )

    else:
      # Passou de todos os 3 casos investigativos -> Vai para o Relatório Final e a Revelação (Plot Twist)
      st.session_state.etapa_agente = "relatorio_final"
      st.rerun()

  # ETAPA 3: RELATÓRIO FINAL E A GRANDE REVELAÇÃO (PLOT TWIST DE MAKARIUS THAIM)
  elif st.session_state.etapa_agente == "relatorio_final":
    st.markdown(
        "<h2>📝 Relatório Final de Investigação & A Revelação Cósmica</h2>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #0b1a2e; border: 2px solid #00ffff; padding: 20px; border-radius: 12px; margin-bottom: 20px;'>
            <h3 style='color: #00ffff; margin-top:0;'>📜 Transmissão Urgente do Quartel-General</h3>
            <p>Parabéns, Agente <b>{nome}</b>! Você investigou todos os arquivos base, superou os bloqueios impostos e chegou ao núcleo do mistério cósmico.</p>
            <p>De repente, as luzes da espaçonave mudam de cor. <b>Raquel Ferreira</b> e <b>Makarius Tahim</b> aparecem juntos no painel central de controle. O clima tenso se dissipa e uma grande verdade é revelada:</p>
            <p style='color: #ffcc00; font-style: italic; font-size: 17px;'>
            "Agente... Makarius Tahim nunca foi o vilão do mal", diz Raquel sorrindo. "Ele foi o criador de todo este sistema de segurança e testes rigorosos. Makarius assumiu o papel de antagonista cósmico para forçar a humanidade a estudar a fundo, pensar criticamente, questionar o universo e nunca aceitar respostas fáceis! O 'lado negro' dele era apenas o rigor científico necessário para que os verdadeiros investigadores despertassem!"
            </p>
            <p>Makarius Tahim assente e completa: <i>"Exatamente, agente. Sem o desafio, a mente humana estagna. Eu criei os obstáculos para garantir que apenas mentes brilhantes como a sua protegessem o conhecimento real do Big Bang."</i></p>
        </div>
        """.format(
            nome=st.session_state.nome_usuario
        ),
        unsafe_allow_html=True,
    )

    st.subheader("✍️ Sua Conclusão Descritiva Final")
    st.write(
        "Antes de oficializar sua patente no ranking, redija abaixo com suas"
        " próprias palavras o que você entendeu sobre toda esta jornada"
        " investigativa (Big Bang, Expansão e a verdadeira intenção por trás dos"
        " testes de Makarius):"
    )

    conclusao_final = st.text_area(
        "Escreva seu relatório descritivo final:",
        placeholder=(
            "Descreva aqui sua compreensão geral sobre a ciência e a reviravolta"
            " da história..."
        ),
    )

    if st.button("📤 Protocolar Relatório e Finalizar Missão"):
      if not conclusao_final.strip():
        st.warning(
            "Por favor, escreva sua conclusão descritiva para finalizar o"
            " protocolo."
        )
      else:
        # Insere no ranking oficial
        st.session_state.ranking.append({
            "nome": st.session_state.nome_usuario,
            "status": "Missão Concluída (Investigador Supremo)",
            "pontos": 3,
        })
        st.session_state.ranking = sorted(
            st.session_state.ranking, key=lambda x: x["pontos"], reverse=True
        )
        st.session_state.etapa_agente = "fim_sucesso"
        st.rerun()

  # ETAPA 4: TELA DE SUCESSO E RANKING
  elif st.session_state.etapa_agente == "fim_sucesso":
    st.success(
        "🎉 Missão Concluída com Honraria Máxima! Relatório protocolado no"
        " Quartel-General."
    )
    st.markdown("### 🏆 Patente Concedida: Investigador(a) do Multiverso")

    st.divider()
    st.subheader("📊 Ranking Oficial de Agentes Investigativos")
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
    if st.button("🔄 Realizar Nova Investigação"):
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.em_resgate = False
      st.session_state.respostas_agente = []
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
              "Acesso liberado! Bem-vindo ao Quartel-General do Gerente,"
              " Felipe."
          )
          st.rerun()
        else:
          st.error("❌ Credenciais de gerente incorretas.")
  else:
    st.success("✅ Sessão de Gerente Ativa (Felipe - Quartel-General)")

    st.subheader("📊 Relatório de Agentes Investigativos na Base")
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
