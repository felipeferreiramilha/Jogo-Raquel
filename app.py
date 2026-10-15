import streamlit as st

# Configuração da Página
st.set_page_config(
    page_title="Investigação Cósmica & Ausubel: O Segredo de Makarius Tahim",
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
# CASOS INVESTIGATIVOS COM ANCORAGEM DE SUBSUNÇORES (DAVID AUSUBEL)
# =========================================================================

CASOS_INVESTIGACAO = [
    {
        "id": 1,
        "titulo": (
            "Caso 1: O Átomo Primitivo e a Superação do Universo Estático"
        ),
        "subsunsor_previo": (
            "🧠 **Ativação de Conhecimento Prévio (Subsunçor):** Antes de"
            " investigarmos, pense no que você já sabe sobre o espaço. Quando"
            " olhamos para o céu à noite, temos a impressão de que ele é"
            " eterno e imutável. Na teoria de David Ausubel, esse conceito"
            " antigo que você já traz na mente é o seu *subsunçor de ancoragem*"
            " sobre a imensidão celeste."
        ),
        "texto_base": (
            "📜 **Arquivo Histórico nº 01:** O físico e padre Georges Lemaître"
            " rompeu com o subsunçor tradicional ao propor em 1927 que o"
            " universo não era estático. Usando as equações de Einstein, ele"
            " deduziu que, retrocedendo no tempo, toda a matéria e energia"
            " estariam concentradas em um único 'Átomo Primitivo' superdenso,"
            " cujo início dinâmico deu origem ao espaço e ao tempo — o Big"
            " Bang. Makarius Tahim tentou corromper este registro para que"
            " as pessoas mantivessem a ideia errônea de um cosmo eterno e"
            " parado."
        ),
        "pergunta_inicial": {
            "enunciado": (
                "Qual foi a principal ruptura conceitual introduzida por Lemaître"
                " para ancorar um novo conhecimento contra o modelo"
                " estático?"
            ),
            "opcoes": [
                (
                    "Afirmar que a Via Láctea era o centro gravitacional"
                    " absoluto."
                ),
                (
                    "Propor que o universo teve um início dinâmico a partir"
                    " de um ponto superdenso ('Átomo Primitivo') e está em"
                    " expansão."
                ),
                ("Provar que o passado e o futuro coexistem sem alteração."),
                ("Demonstrar que o espaço é preenchido por um fluido chamado éter."),
            ],
            "correta": (
                "Propor que o universo teve um início dinâmico a partir de um"
                " ponto superdenso ('Átomo Primitivo') e está em expansão."
            ),
        },
        "pergunta_resgate": {
            "enunciado": (
                "⚠️ **Aviso de Falha no Subsunçor (Raquel):** Você ancorou o"
                " conceito de forma incorreta! Releia: o que Lemaître defendeu"
                " sobre a origem do cosmos para substituir a ideia estática?"
            ),
            "opcoes": [
                (
                    "Que o cosmos nasceu de um estado inicial hiperdenso e"
                    " iniciou sua expansão contínua."
                ),
                ("Que as estrelas nunca mudam de posição ao longo dos eras."),
                ("Que o universo foi criado sem espaço nem tempo."),
                ("Que a matéria surge espontaneamente no vácuo estático."),
            ],
            "correta": (
                "Que o cosmos nasceu de um estado inicial hiperdenso e iniciou"
                " sua expansão contínua."
            ),
        },
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Agente, vamos ancorar esse novo"
            " conhecimento conectando-o com o que você já sabe sobre o tempo e"
            " a origem das coisas!'"
        ),
        "comentario_makarius": (
            "😈 **Makarius Tahim sussurra:** 'Seu conceito antigo é frágil... Se"
            " seus subsunçores falharem, você ficará preso no meu Vazio"
            " estático!'"
        ),
    },
    {
        "id": 2,
        "titulo": "Caso 2: A Expansão do Espaço e o Redshift",
        "subsunsor_previo": (
            "🧠 **Ativação de Conhecimento Prévio (Subsunçor):** Pense em um"
            " objeto se afastando de você na estrada: o som ou a luz parecem"
            " mudar. Na cosmologia, usamos essa ideia prévia para entender o"
            " movimento das galáxias."
        ),
        "texto_base": (
            "📜 **Arquivo Histórico nº 02:** Edwin Hubble descobriu que a luz"
            " de galáxias distantes sofre um desvio para o vermelho"
            " (*redshift*), indicando que os comprimentos de onda estão sendo"
            " esticados. A interpretação correta segundo a aprendizagem"
            " significativa é que o próprio tecido do espaço-tempo está se"
            " esticando, afastando as galáxias proporcionalmente à distância."
            " Makarius Tahim tentou distorcer essa evidência para fazer o"
            " público acreditar que o universo estava encolhendo."
        ),
        "pergunta_inicial": {
            "enunciado": (
                "De acordo com o texto, o que o desvio para o vermelho"
                " (*redshift*) revela sobre o universo?"
            ),
            "opcoes": [
                (
                    "Que as galáxias correm rapidamente dentro de um espaço"
                    " rígido."
                ),
                (
                    "Que o próprio tecido do espaço-tempo está se esticando,"
                    " promovendo a expansão cósmica."
                ),
                ("Que as estrelas estão esfriando e emitindo luz vermelha."),
                ("Que o universo está encolhendo em direção ao centro."),
            ],
            "correta": (
                "Que o próprio tecido do espaço-tempo está se esticando,"
                " promovendo a expansão cósmica."
            ),
        },
        "pergunta_resgate": {
            "enunciado": (
                "⚠️ **Aviso de Falha no Subsunçor (Raquel):** Atenção! O"
                " desvio para o vermelho não significa que as galáxias correm"
                " como carros. Qual é a ancoragem conceitual correta?"
            ),
            "opcoes": [
                (
                    "O estiramento do próprio espaço entre as galáxias,"
                    " provando a expansão cósmica."
                ),
                ("O reflexo da luz solar nas lentes dos telescópios."),
                ("A absorção de luz por nuvens de poeira cósmica."),
                ("A rotação acelerada do núcleo estelar."),
            ],
            "correta": (
                "O estiramento do próprio espaço entre as galáxias, provando a"
                " expansão cósmica."
            ),
        },
        "comentario_raquel": (
            "👧 **Raquel Ferreira diz:** 'Conecte isso com a nossa analogia do"
            " balão! O espaço cresce por igual em todas as direções.'"
        ),
        "comentario_makarius": (
            "😈 **Makarius Tahim sussurra:** 'Vocês confundem movimento com"
            " expansão do espaço... Sua cognição vai colapsar!'"
        ),
    },
    {
        "id": 3,
        "titulo": "Caso 3: Matéria Escura e Energia Escura",
        "subsunsor_previo": (
            "🧠 **Ativação de Conhecimento Prévio (Subsunçor):** Pense na"
            " gravidade que você experimenta na Terra ao segurar um objeto."
            " Agora, imagine forças invisíveis que unem ou empurram galáxias"
            " inteiras pelo universo."
        ),
        "texto_base": (
            "📜 **Arquivo Histórico nº 03:** As curvas de rotação galáctica"
            " mostraram que as estrelas periféricas giram rápido demais para"
            " a massa visível, exigindo a presença de Matéria Escura"
            " (atração/estruturação). Simultaneamente, descobriu-se que a"
            " expansão está acelerando devido à Energia Escura"
            " (repulsão/pressão de vácuo). Makarius Tahim usou esses mistérios"
            " para assustar os pesquisadores com o medo do desconhecido."
        ),
        "pergunta_inicial": {
            "enunciado": (
                "Qual é a diferença funcional entre a Matéria Escura e a"
                " Energia Escura na evolução do universo?"
            ),
            "opcoes": [
                (
                    "A Matéria Escura atrai gravitacionalmente e une as"
                    " estruturas; a Energia Escura repele e acelera a"
                    " expansão."
                ),
                ("A Matéria Escura emite raios gama; a Energia Escura congela o tempo."),
                ("A Matéria Escura existe só na Terra; a Energia Escura fica no Sol."),
                ("Ambas exercem exatamente a mesma força de atração."),
            ],
            "correta": (
                "A Matéria Escura atrai gravitacionalmente e une as estruturas;"
                " a Energia Escura repele e acelera a expansão."
            ),
        },
        "pergunta_resgate": {
            "enunciado": (
                "⚠️ **Aviso de Falha no Subsunçor (Raquel):** Cuidado para não"
                " inverter os conceitos! O que cada uma dessas forças faz?"
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
            "👧 **Raquel Ferreira diz:** 'Lembre-se: uma puxa para formar"
            " galáxias (matéria) e a outra empurra para acelerar o cosmo"
            " (energia)!'"
        ),
        "comentario_makarius": (
            "😈 **Makarius Tahim sussurra:** 'Minhas forças invisíveis são"
            " complexas demais para sua mente ancorar!'"
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
  st.session_state.em_resgate = False
if "erros_cometidos" not in st.session_state:
  st.session_state.erros_cometidos = []
if "nome_usuario" not in st.session_state:
  st.session_state.nome_usuario = ""
if "ranking" not in st.session_state:
  st.session_state.ranking = [
      {"nome": "Agente Felipe", "status": "Concluído (Darth Makarius)", "pontos": 3},
      {
          "nome": "Raquel Ferreira (Heroína)",
          "status": "Comandante Cognitiva",
          "pontos": 3,
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
    "<p style='text-align: center; color: #aaa;'>Ative seus subsunçores,"
    " supere os bloqueios e enfrente Makarius Tahim em seu traje épico de"
    " Darth Vader!</p>",
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
        "Inicie a investigação com ancoragem de subsunçores, análise de erros"
        " e o desfecho com Darth Makarius!"
    )
    if st.button("Entrar como Agente"):
      st.session_state.modo = "aluno"
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.em_resgate = False
      st.session_state.erros_cometidos = []
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
    if st.button("🚀 Iniciar Ancoragem e Investigação"):
      if nome_input.strip() == "":
        st.warning("Por favor, digite um nome válido.")
      else:
        st.session_state.nome_usuario = nome_input.strip()
        st.rerun()
    st.stop()

  # ETAPA DE INVESTIGAÇÃO COM SUBSUNÇORES E BLOQUEIO
  if st.session_state.etapa_agente == "investigacao":
    idx = st.session_state.indice_caso
    total_casos = len(CASOS_INVESTIGACAO)

    if idx < total_casos:
      caso_atual = CASOS_INVESTIGACAO[idx]

      st.markdown(f"<h2>📁 {caso_atual['titulo']}</h2>", unsafe_allow_html=True)
      st.write(
          f"🕵️‍♂️ **Agente:** {st.session_state.nome_usuario} | **Progresso:**"
          f" Caso {idx + 1} de {total_casos}"
      )
      st.progress((idx) / total_casos)

      # 1. Ativação de Conhecimento Prévio (Ausubel)
      st.markdown(
          f"<div class='subsunsor-box'>{caso_atual['subsunsor_previo']}</div>",
          unsafe_allow_html=True,
      )

      # 2. Texto Base de Investigação
      st.markdown(
          f"<div class='texto-base-box'>{caso_atual['texto_base']}</div>",
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
                    <h3 style='margin:0; color:#ff3333;'>😈 Makarius Tahim (Darth Tahim)</h3>
                    <p style='margin-top:8px; font-size:13px; font-style:italic;'>{caso_atual['comentario_makarius']}</p>
                </div>
                """,
            unsafe_allow_html=True,
        )

      with col_q:
        if not st.session_state.em_resgate:
          q_ativa = caso_atual["pergunta_inicial"]
          modo_p = "inicial"
        else:
          q_ativa = caso_atual["pergunta_resgate"]
          modo_p = "resgate"

        st.markdown(
            f"<div class='pergunta-box'><h4>{q_ativa['enunciado']}</h4></div>",
            unsafe_allow_html=True,
        )

        escolha_agente = st.radio(
            "Selecione a dedução investigativa correta:",
            q_ativa["opcoes"],
            key=f"radio_ausubel_{idx}_{modo_p}",
        )

        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("🔒 Validar Subsunçor e Avançar"):
          if escolha_agente == q_ativa["correta"]:
            st.success(
                "✨ Conceito ancorado com sucesso! Subsunçor integrado à"
                " estrutura cognitiva."
            )
            st.session_state.em_resgate = False
            st.session_state.indice_caso += 1
            st.rerun()
          else:
            erro_info = (
                f"**{caso_atual['titulo']}**: Você selecionou uma ancoragem"
                f" equivocada (*'{escolha_agente[:40]}...'*), gerando conflito"
                " com o subsunçor científico correto"
                f" (*'{q_ativa['correta'][:40]}...'*)."
            )
            if erro_info not in st.session_state.erros_cometidos:
              st.session_state.erros_cometidos.append(erro_info)

            if not st.session_state.em_resgate:
              st.session_state.em_resgate = True
              st.error(
                  "❌ **Conflito Cognitivo (Erro Detectado)!** Makarius Tahim"
                  " (Darth Tahim) bloqueou seu acesso. Seus subsunçores antigos"
                  " colidiram com a evidência correta. Leia a dica da Raquel e"
                  " tente novamente!"
              )
              st.rerun()
            else:
              st.error(
                  "❌ Errado novamente! O bloqueio continua ativo. Releia o"
                  " texto base e ajuste sua estrutura conceitual."
              )

    else:
      st.session_state.etapa_agente = "avaliacao_ausubel"
      st.rerun()

  # ETAPA 3: AVALIAÇÃO DIAGNÓSTICA DE ERROS & DESFECHO ÉPICO (DARTH MAKARIUS)
  elif st.session_state.etapa_agente == "avaliacao_ausubel":
    st.markdown(
        "<h2>📊 Avaliação Diagnóstica de Erros & Conhecimento do Universo</h2>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style='background-color: #0b1a2e; border: 2px solid #00ffff; padding: 20px; border-radius: 12px; margin-bottom: 20px;'>
            <h3 style='color: #00ffff; margin-top:0;'>🌌 O Desfecho: A Aparição de Darth Makarius</h3>
            <p>Parabéns, Agente <b>{nome}</b>! Você concluiu todos os casos de investigação cósmica.</p>
            <p>As portas da câmara principal se abrem com um som metálico profundo. Das sombras surge <b>Makarius Tahim (Darth Tahim)</b>, vestindo seu imponente traje preto estilo <i>Darth Vader</i> de <i>Star Wars</i>, com sua respiração mecânica ecoando pelo ambiente. Ao lado dele, <b>Raquel Ferreira</b> sorri orgulhosa.</p>
            <p style='color: #ffcc00; font-style: italic; font-size: 16px;'>
            "Impressionante...", diz Darth Makarius com sua voz profunda, retirando o capacete escuro e revelando um olhar de absoluto respeito. "Você enfrentou os conflitos cognitivos, superou seus erros e reestruturou seus subsunçores como um verdadeiro mestre. Na Teoria de David Ausubel, o erro não é o fim, mas o degrau necessário para a aprendizagem significativa."
            </p>
            <p>Makarius ergue as mãos e lhe transfere o sagrado <b>Conhecimento do Universo</b>, dizendo: <i>"Eu assumi o manto e o visual do lado negro para forçar a sua mente a evoluir. Meus parabéns, agente. O cosmos agora está em boas mãos."</i></p>
        </div>
        """.format(
            nome=st.session_state.nome_usuario
        ),
        unsafe_allow_html=True,
    )

    # Exibição Detalhada dos Erros Cometidos (Análise Ausubel)
    st.subheader(
        "🧠 Relatório Pedagógico: Análise dos Erros e Perdas de Roteiro"
    )
    if len(st.session_state.erros_cometidos) == 0:
      st.success(
          "🌟 Espantoso! Você não cometeu erros conceituais significativos"
          " durante a ancoragem. Seus subsunçores estavam perfeitamente"
          " alinhados desde o início!"
      )
    else:
      st.warning(
          "⚠️ Durante a jornada investigativa, foram mapeados os seguintes"
          " desvios conceituais e conflitos de subsunçores que fizeram você"
          " se perder momentaneamente:"
      )
      for err in st.session_state.erros_cometidos:
        st.markdown(f"- {err}")

    st.markdown("<br>", unsafe_allow_html=True)
    st.subheader("✍️ Relatório Final de Reancoragem Cognitiva")
    st.write(
        "Para consolidar sua aprendizagem significativa, redija abaixo com suas"
        " próprias palavras o que você entendeu sobre a evolução do universo"
        " (Big Bang, Expansão e Matéria/Energia Escura) e como os erros"
        " ajudaram na sua compreensão:"
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
        "🎉 Jornada Concluída com Honraria Máxima! Relatório de aprendizagem"
        " significativa protocolado com bênção de Darth Makarius."
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
    if st.button("🔄 Realizar Nova Investigação Cognitiva"):
      st.session_state.etapa_agente = "investigacao"
      st.session_state.indice_caso = 0
      st.session_state.em_resgate = False
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

    st.subheader("📊 Relatório de Agentes e Análise de Subsuncionários")
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
