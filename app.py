import streamlit as st

# Configuração da página
st.set_page_config(page_title="CDZ: Operação Horizonte de Equipes", page_icon="🌌", layout="centered")

# Inicialização do Estado da Sessão para Equipes
if "fase" not in st.session_state:
    st.session_state.fase = 1
if "modo_resgate" not in st.session_state:
    st.session_state.modo_resgate = False
if "pontos_equipe_a" not in st.session_state:
    st.session_state.pontos_equipe_a = 0
if "pontos_equipe_b" not in st.session_state:
    st.session_state.pontos_equipe_b = 0
if "turno_equipe" not in st.session_state:
    st.session_state.turno_equipe = "Equipe Alfa"
if "estabilidade_cosmos" not in st.session_state:
    st.session_state.estabilidade_cosmos = 100

# Estilo visual
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

st.title("🌌 CDZ: Operação Horizonte de Eventos - Modo Equipes")
st.markdown(f"### ⚔️ Vez da **{st.session_state.turno_equipe}** jogar!")
st.markdown("---")

# Barra Lateral de Placar e Status
st.sidebar.header("📊 Placar das Equipes & Cosmo")
st.sidebar.metric(label="🛡️ Equipe Alfa (Pontos)", value=st.session_state.pontos_equipe_a)
st.sidebar.metric(label="⚡ Equipe Beta (Pontos)", value=st.session_state.pontos_equipe_b)
st.sidebar.metric(label="🌌 Estabilidade do Universo", value=f"{st.session_state.estabilidade_cosmos}%")
st.sidebar.markdown("---")
st.sidebar.info("👥 **Heróis:** Raquel Ferreira & Alunos\n😈 **Vilão:** Makarius (O Vilão Cósmico)")

def alternar_turno():
    if st.session_state.turno_equipe == "Equipe Alfa":
        st.session_state.turno_equipe = "Equipe Beta"
    else:
        st.session_state.turno_equipe = "Equipe Alfa"

# =========================================================
# FASE 1: Múltipla Escolha (A a E) - Origem do Cosmo
# =========================================================
if st.session_state.fase == 1 and not st.session_state.modo_resgate:
    st.subheader("Fase 1: O Despertar da Singularidade (Múltipla Escolha)")
    st.markdown("""
    > *Raquel Ferreira* orienta as equipes a vasculharem as ruínas do relógio estelar. 
    > *Makarius* bloqueia a passagem, afirmando que a origem do universo é um mistério denso demais para mentes comuns.
    
    **Missão:** Em equipe, debatam e escolham a alternativa correta sobre a expansão inicial do universo.
    """)
    
    escolha = st.radio(
        "Selecione a pista correta:",
        (
            "A) O universo sempre existiu estático, eterno e do mesmo tamanho em todas as eras.",
            "B) O cosmos nasceu de um ponto infinitamente denso e quente (singularidade) que iniciou uma expansão contínua do espaço-tempo.",
            "C) As galáxias se formaram subitamente a partir de colisões de buracos negros estáticos.",
            "D) O universo expande-se porque as estrelas criam matéria do nada nos vazios espaciais.",
            "E) A origem do universo é cíclica, colapsando e reiniciando a cada 100 anos terrestres."
        ),
        key="f1_q"
    )

    if st.button("Submeter Resposta da Equipe"):
        if escolha.startswith("B"):
            if st.session_state.turno_equipe == "Equipe Alfa":
                st.session_state.pontos_equipe_a += 20
            else:
                st.session_state.pontos_equipe_b += 20
            st.success("🎉 Resposta correta! Vocês conectaram o conceito atual à ideia de expansão.")
            st.session_state.fase = 2
            alternar_turno()
            st.rerun()
        else:
            st.error("❌ Resposta incorreta! O universo sofreu uma oscilação de instabilidade. A equipe caiu na **Zona de Resgate Prévio**!")
            st.session_state.estabilidade_cosmos -= 15
            st.session_state.modo_resgate = True
            st.rerun()

# --- MODO RESGATE FASE 1 ---
elif st.session_state.fase == 1 and st.session_state.modo_resgate:
    st.warning("🛟 **PERGUNTA DE RESGATE EM EQUIPE!**")
    st.markdown("""
    > Para salvar a pontuação e estabilizar o cosmo, a equipe precisa resgatar um conceito básico que vocês já viram no cotidiano: 
    > *Pensem em como um balão de festa ganha volume e se estica quando sopramos por dentro.*
    """)
    
    resgate_escolha = st.radio(
        "Como o exemplo do balão de festa ajuda a compreender a expansão do universo?",
        (
            "A) Mostra que o balão cria ar novo do nada assim que é amarrado.",
            "B) Ilustra como os pontos na superfície do balão se afastam uns dos outros à medida que o espaço entre eles se expande.",
            "C) Comprova que o centro do balão é a única parte que se move, enquanto as bordas param.",
            "D) Indica que o universo tem paredes de borracha rígida que impedem o calor de sair."
        ),
        key="resgate_1"
    )

    if st.button("Tentar Resgate"):
        if resgate_escolha.startswith("B"):
            st.success("✨ Resgate bem-sucedido! Vocês usaram uma vivência anterior para ancorar o novo conhecimento.")
            st.session_state.modo_resgate = False
            st.session_state.fase = 2
            alternar_turno()
            st.rerun()
        else:
            st.error("Ainda não foi dessa vez. A estabilidade caiu mais um pouco, mas vamos avançar para aprender com o erro!")
            st.session_state.estabilidade_cosmos -= 10
            st.session_state.modo_resgate = False
            st.session_state.fase = 2
            alternar_turno()
            st.rerun()

# =========================================================
# FASE 2: Dissertativa com Análise Inteligente por Palavras-Chave
# =========================================================
elif st.session_state.fase == 2 and not st.session_state.modo_resgate:
    st.subheader("Fase 2: O Enigma da Matéria Escura (Dissertativa)")
    st.markdown("""
    > *Makarius* desafia as equipes na Câmara dos Aglomerados: 
    > *"As galáxias giram rápido demais! Pelas leis visíveis, elas deveriam se despedaçar. O que segura tudo unificado se vocês não conseguem enxergar essa massa?"*
    
    **Missão da Equipe:** Discutam entre vocês e redijam um breve texto explicativo sobre o papel da **Matéria Escura** e como ela atua no cosmos.
    """)

    texto_dissertacao = st.text_area("✍️ Escreva a explicação da equipe:", key="dissertacao_f2")

    if st.button("Enviar Explicação para Avaliação Cósmica"):
        # Sistema inteligente analisando termos fundamentais (subsunçores/conceitos-chave)
        texto_lower = texto_dissertacao.lower()
        
        # Palavras esperadas que indicam que a equipe compreendeu a essência
        termos_obrigatorios = ["gravidade", "invisível", "massa", "aglomerado", "conectar", "força", "estrelas", "unidas", "atração"]
        acertos = sum(1 for termo in termos_obrigatorios if termo in texto_lower)
        
        if len(texto_dissertacao.strip()) > 15 and acertos >= 2:
            if st.session_state.turno_equipe == "Equipe Alfa":
                st.session_state.pontos_equipe_a += 35
            else:
                st.session_state.pontos_equipe_b += 35
            st.success(f"🌟 Análise Excelente! O sistema detectou conceitos cruciais na resposta da equipe (Termos correlacionados identificados).")
            st.session_state.fase = 3
            alternar_turno()
            st.rerun()
        else:
            st.error("❌ A explicação ficou incompleta ou faltaram termos fundamentais sobre atração gravitacional e massa invisível. A equipe caiu na **Zona de Resgate**!")
            st.session_state.estabilidade_cosmos -= 20
            st.session_state.modo_resgate = True
            st.rerun()

# --- MODO RESGATE FASE 2 ---
elif st.session_state.fase == 2 and st.session_state.modo_resgate:
    st.warning("🛟 **PERGUNTA DE RESGATE: A COLA INVISÍVEL**")
    st.markdown("""
    > Pensem em quando vocês amarram um objeto pesado com uma corda invisível ou em como um ímã puxa metais sem encostar neles. 
    > Escolham a opção que melhor traduz essa ideia para o universo:
    """)
    
    resgate_escolha_2 = st.radio(
        "Selecione a analogia correta para a Matéria Escura:",
        (
            "A) É um escudo térmico que impede o sol de esfriar.",
            "B) É uma massa que não emite luz, mas exerce forte atração gravitacional, funcionando como uma 'cola' invisível para as galáxias.",
            "C) É uma energia que empurra todas as estrelas para fora do universo de forma acelerada.",
            "D) São cometas congelados que passam iluminando o céu noturno."
        ),
        key="resgate_2"
    )

    if st.button("Concluir Resgate da Fase 2"):
        if resgate_escolha_2.startswith("B"):
            st.success("✨ Excelente resgate! Conectaram bem a ideia de força de atração à estrutura galáctica.")
            st.session_state.modo_resgate = False
            st.session_state.fase = 3
            alternar_turno()
            st.rerun()
        else:
            st.error("O resgate não foi totalmente preciso, mas a jornada continua rumo ao confronto final!")
            st.session_state.estabilidade_cosmos -= 15
            st.session_state.modo_resgate = False
            st.session_state.fase = 3
            alternar_turno()
            st.rerun()

# =========================================================
# FASE 3: Conclusão e Revelação de Makarius
# =========================================================
elif st.session_state.fase == 3:
    st.balloons()
    st.subheader("Fase Final: A Revelação do Santuário 🏛️")
    st.markdown("""
    > Chegando ao núcleo do templo, *Makarius* sorri e revela a verdadeira intenção: 
    > *"Eu nunca quis destruir o cosmo! As anomalias e enigmas foram um teste planejado junto com Raquel Ferreira. Precisávamos que vocês conectassem o que já sabiam da vida com as leis da física para despertar o verdadeiro poder do conhecimento!"*
    """)
    
    st.markdown("---")
    st.markdown("### 🏆 **Resultado Final da Batalha do Conhecimento**")
    st.markdown(f"* **Pontos da Equipe Alfa:** {st.session_state.pontos_equipe_a}")
    st.markdown(f"* **Pontos da Equipe Beta:** {st.session_state.pontos_equipe_b}")
    st.markdown(f"* **Estabilidade Final do Cosmo:** {st.session_state.estabilidade_cosmos}%")
    
    if st.session_state.pontos_equipe_a > st.session_state.pontos_equipe_b:
        st.success("🥇 **Equipe Alfa Venceu a Jornada Cósmica!**")
    elif st.session_state.pontos_equipe_b > st.session_state.pontos_equipe_a:
        st.success("🥇 **Equipe Beta Venceu a Jornada Cósmica!**")
    else:
        st.info("🤝 **Empate Magnífico! Ambas as equipes salvaram o universo juntas!**")

    if st.button("🔄 Jogar Novamente"):
        st.session_state.fase = 1
        st.session_state.modo_resgate = False
        st.session_state.pontos_equipe_a = 0
        st.session_state.pontos_equipe_b = 0
        st.session_state.estabilidade_cosmos = 100
        st.session_state.turno_equipe = "Equipe Alfa"
        st.rerun()
