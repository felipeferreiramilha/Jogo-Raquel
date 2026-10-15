import streamlit as st

# Configuração da página
st.set_page_config(page_title="CDZ: Operação Horizonte de Eventos", page_icon="🌌", layout="centered")

# Inicialização do Estado da Sessão (para o jogo não reiniciar sozinho a cada clique)
if "etapa" not in st.session_state:
    st.session_state.etapa = 1
if "materia_escura" not in st.session_state:
    st.session_state.materia_escura = 0
if "estabilidade" not in st.session_state:
    st.session_state.estabilidade = 100
if "tentativas_erradas" not in st.session_state:
    st.session_state.tentativas_erradas = 0
if "mensagem_feedback" not in st.session_state:
    st.session_state.mensagem_feedback = ""

# Estilo visual customizado
st.markdown("""
    <style>
    .main {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        background-color: #1f4068;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        border: 1px solid #00b4d8;
    }
    .stButton>button:hover {
        background-color: #00b4d8;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🌌 CDZ: Operação Horizonte de Eventos")
st.markdown("### *Uma Jornada Cosmológica pelo Santuário*")
st.markdown("---")

# Barra Lateral (Status do Cosmo)
st.sidebar.header("📊 Status do Tabuleiro")
st.sidebar.metric(label="🌌 Matéria Escura Coletada", value=f"{st.session_state.materia_escura} Unidades")
st.sidebar.metric(label="⚡ Estabilidade do Cosmo", value=f"{st.session_state.estabilidade}%")
st.sidebar.markdown("---")
st.sidebar.info("👥 **Heróis:** Raquel Ferreira & Alunos\n😈 **Vilão:** Makarius (O Vilão Cósmico)")

# ---------------------------------------------------------
# ETAPA 1: O Despertar da Anomalia (Origem do Big Bang)
# ---------------------------------------------------------
if st.session_state.etapa == 1:
    st.subheader("Fase 1: O Eco do Big Bang")
    st.markdown("""
    > **Contexto:** *Raquel Ferreira* detecta uma distorção grave no relógio cósmico do Santuário. 
    > As leituras apontam que o **Big Bang** — a expansão inicial do espaço — está acelerando de forma descontrolada por causa de uma interferência. 
    > O misterioso **Makarius** aparece nas sombras, rindo e afirmando que vai espalhar o caos térmico por todo o universo!
    
    **Missão dos Alunos:** Para estabilizar a primeira casa do santuário, vocês precisam investigar a natureza da expansão cósmica inicial.
    """)
    
    st.markdown("---")
    st.markdown("❓ **Pergunta de Investigação:** O que o modelo do *Big Bang* descreve sobre a origem e evolução do Universo?")
    
    opcao = st.radio(
        "Selecione a pista correta recolhida no local:",
        [
            "A) O universo surgiu de um ponto extremamente denso e quente (singularidade) e continua se expandindo até hoje.",
            "B) O universo sempre existiu do mesmo tamanho, estático e imutável, sem nenhuma expansão.",
            "C) O universo foi criado instantaneamente em um formato plano e infinito, sem passado denso."
        ],
        key="q1"
    )

    if st.button("Investigar e Avançar"):
        if opcao.startswith("A"):
            st.session_state.materia_escura += 20
            st.session_state.estabilidade = min(100, st.session_state.estabilidade + 10)
            st.session_state.etapa = 2
            st.session_state.tentativas_erradas = 0
            st.success("Correto! A singularidade inicial começou a se expandir, formando o espaço e o tempo.")
            st.rerun()
        else:
            st.session_state.tentativas_erradas += 1
            st.session_state.estabilidade -= 15
            st.error("Resposta incorreta! A pista levou a uma distorção temporal. O Cosmo perdeu estabilidade. Tente outra linha de investigação!")

# ---------------------------------------------------------
# ETAPA 2: O Mistério da Matéria Escura
# ---------------------------------------------------------
elif st.session_state.etapa == 2:
    st.subheader("Fase 2: A Cola Invisível das Galáxias")
    st.markdown("""
    > **Contexto:** Com a expansão compreendida, o grupo avança para a Câmara dos Aglomerados Estelares. 
    > No entanto, as galáxias estão começando a se dispersar no espaço sideral. *Makarius* bloqueia o caminho, zombando: 
    > *"Sem massa suficiente para segurar as estrelas, o universo vai se esfacelar!"*
    
    **Missão dos Alunos:** Vocês precisam descobrir qual componente invisível do cosmos fornece a gravidade necessária para manter as estruturas unidas.
    """)
    
    st.markdown("---")
    st.markdown("❓ **Pergunta de Investigação:** Qual é a função da **Matéria Escura** na estrutura em grande escala do universo?")
    
    opcao = st.radio(
        "Selecione a propriedade correta:",
        [
            "A) Ela emite luz própria e forte radiação ultravioleta que aquece os planetas distantes.",
            "B) Ela interage predominantemente via gravidade, atuando como um arcabouço invisível que impede que as galáxias se dispersem.",
            "C) Ela absorve buracos negros e impede completamente qualquer tipo de expansão cósmica."
        ],
        key="q2"
    )

    if st.button("Analisar Pista de Matéria Escura"):
        if opcao.startswith("B"):
            st.session_state.materia_escura += 30
            st.session_state.estabilidade = min(100, st.session_state.estabilidade + 15)
            st.session_state.etapa = 3
            st.session_state.tentativas_erradas = 0
            st.success("Excelente! A Matéria Escura atua como a 'cola gravitacional' do cosmos.")
            st.rerun()
        else:
            st.session_state.tentativas_erradas += 1
            st.session_state.estabilidade -= 20
            st.error("Erro na análise! A rota escolhida levou a uma zona de radiação intensa. Cuidado com a estabilidade!")

# ---------------------------------------------------------
# ETAPA 3: A Revelação de Makarius e Conclusão
# ---------------------------------------------------------
elif st.session_state.etapa == 3:
    st.subheader("Fase Final: A Revelação no Horizonte de Eventos")
    st.markdown("""
    > **Contexto:** Chegando ao núcleo do Santuário, Raquel Ferreira e os alunos cercam *Makarius*. 
    > Preparados para o golpe final, Makarius abaixa a guarda, sorri e revela a verdade: 
    > *"Eu nunca quis destruir o universo... As anomalias eram um teste! O tecido do cosmos estava enfraquecendo porque os humanos esqueceram como o universo funciona. Eu criei a crise para forçá-los a despertar o verdadeiro cosmo através do conhecimento científico!"*
    
    **Missão Final:** Para consolidar o aprendizado e selar a estabilidade do universo, descreva em poucas palavras o que os alunos aprenderam sobre a expansão e a estrutura do universo nesta jornada.
    """)
    
    st.markdown("---")
    conclusao_aluno = st.text_area("✍️ Descreva a compreensão final dos alunos sobre o Big Bang e a Matéria Escura:")

    if st.button("Concluir Missão e Salvar o Santuário"):
        if len(conclusao_aluno.strip()) > 10:
            st.session_state.etapa = 4
            st.rerun()
        else:
            st.warning("Por favor, escreva uma breve descrição do que foi compreendido para encerrar o ciclo cósmico.")

# ---------------------------------------------------------
# TELA DE VITÓRIA / CONCLUSÃO
# ---------------------------------------------------------
elif st.session_state.etapa == 4:
    st.balloons()
    st.success("🎉 PARABÉNS! O UNIVERSO FOI SALVO!")
    st.markdown(f"""
    ### Relatório Final da Missão:
    * **Pontuação de Matéria Escura Coletada:** {st.session_state.materia_escura} Unidades
    * **Estabilidade Final do Cosmo:** {st.session_state.estabilidade}%
    
    > **Conclusão:** Guiados por *Raquel Ferreira*, os alunos desvendaram os mistérios do Big Bang, compreenderam o papel fundamental da Matéria Escura e descobriram as verdadeiras intenções de *Makarius*. O Santuário e o cosmos estão seguros em harmonia com as leis da física!
    """)
    
    if st.button("🔄 Jogar Novamente"):
        st.session_state.etapa = 1
        st.session_state.materia_escura = 0
        st.session_state.estabilidade = 100
        st.session_state.tentativas_erradas = 0
        st.rerun()
