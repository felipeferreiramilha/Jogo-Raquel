import streamlit as st

# Configuração da página
st.set_page_config(page_title="CDZ: Operação Horizonte de Equipes", page_icon="🌌", layout="centered")

# ==========================================
# INICIALIZAÇÃO DO ESTADO GLOBAL E BANCO DE DADOS LOCAL
# ==========================================
if "fase" not in st.session_state:
    st.session_state.fase = 1
if "pontos_alfa" not in st.session_state:
    st.session_state.pontos_alfa = 0
if "pontos_beta" not in st.session_state:
    st.session_state.pontos_beta = 0
if "pontos_gama" not in st.session_state:
    st.session_state.pontos_gama = 0
if "lista_equipes" not in st.session_state:
    st.session_state.lista_equipes = ["Equipe Alfa", "Equipe Beta", "Equipe Gama"]
if "indice_equipe" not in st.session_state:
    st.session_state.indice_equipe = 0
if "estabilidade" not in st.session_state:
    st.session_state.estabilidade = 100
if "historico_respostas" not in st.session_state:
    st.session_state.historico_respostas = []  # Armazena respostas dissertativas enviadas
if "banco_questoes" not in st.session_state:
    # Banco de questões customizáveis pelo Admin
    st.session_state.banco_questoes = {
        "dissertativa_1": {
            "enunciado": "Explique com suas palavras como o modelo do Big Bang descreve a evolução inicial do universo.",
            "palavras_chave": ["big bang", "singularidade", "expansão", "densidade", "quente", "espaço"]
        },
        "dissertativa_2": {
            "enunciado": "Qual é a função da Matéria Escura na estruturação das galáxias após a expansão cósmica?",
            "palavras_chave": ["matéria escura", "gravidade", "cola", "invisível", "massa", "atração", "galaxias"]
        }
    }

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

equipe_atual = st.session_state.lista_equipes[st.session_state.indice_equipe]

st.title("🌌 CDZ: Operação Horizonte de Eventos")
st.markdown(f"### ⚔️ Vez da **{equipe_atual}** jogar!")
st.markdown("---")

# ==========================================
# BARRA LATERAL: PLACAR E PAINEL ADMINISTRADOR
# ==========================================
st.sidebar.header("📊 Placar das 3 Equipes")
st.sidebar.metric(label="🛡️ Equipe Alfa", value=st.session_state.pontos_alfa)
st.sidebar.metric(label="🛡️ Equipe Beta", value=st.session_state.pontos_beta)
st.sidebar.metric(label="🛡️ Equipe Gama", value=st.session_state.pontos_gama)
st.sidebar.metric(label="⚡ Estabilidade do Cosmo", value=f"{st.session_state.estabilidade}%")
st.sidebar.markdown("---")

# PAINEL ADMINISTRADOR
with st.sidebar.expander("⚙️ Painel do Administrador"):
    st.markdown("### Histórico de Respostas Salvas")
    if st.session_state.historico_respostas:
        for idx, item in enumerate(st.session_state.historico_respostas):
            st.text(f"[{item['equipe']}] Fase {item['fase']}:\n\"{item['resposta']}\"")
        if st.button("🗑️ Apagar Todo o Histórico"):
            st.session_state.historico_respostas = []
            st.rerun()
    else:
        st.info("Nenhuma resposta dissertativa registrada ainda.")
    
    st.markdown("---")
    st.markdown("### Adicionar Nova Questão Dissertativa")
    nova_chave = st.text_input("Identificador (ex: dissertativa_3)")
    novo_enunciado = st.text_area("Enunciado da Questão")
    novas_palavras = st.text_input("Palavras-chave separadas por vírgula (ex: estrela, calor, luz)")
    
    if st.button("Adicionar Questão ao Banco"):
        if nova_chave and novo_enunciado and novas_palavras:
            lista_p = [p.strip().lower() for p in novas_palavras.split(",")]
            st.session_state.banco_questoes[nova_chave] = {
                "enunciado": novo_enunciado,
                "palavras_chave": lista_p
            }
            st.success(f"Questão '{nova_chave}' adicionada com sucesso!")
            st.rerun()
        else:
            st.warning("Preencha todos os campos para cadastrar a questão.")

def passar_turno():
    # Alterna entre Alfa (0) -> Beta (1) -> Gama (2) -> Alfa (0)
    st.session_state.indice_equipe = (st.session_state.indice_equipe + 1) % 3

def adicionar_pontos(qtd):
    eq = st.session_state.lista_equipes[st.session_state.indice_equipe]
    if eq == "Equipe Alfa":
        st.session_state.pontos_alfa += qtd
    elif eq == "Equipe Beta":
        st.session_state.pontos_beta += qtd
    elif eq == "Equipe Gama":
        st.session_state.pontos_gama += qtd

# ==========================================
# FASE 1: MÚLTIPLA ESCOLHA (A a E)
# ==========================================
if st.session_state.fase == 1:
    st.subheader("Fase 1: O Despertar da Singularidade (Múltipla Escolha)")
    st.markdown("""
    > *Raquel Ferreira* orienta as equipes a investigarem o relógio estelar. 
    > *Makarius* bloqueia a passagem, afirmando que a origem do universo é um mistério denso demais.
    
    **Missão:** A equipe atual deve debater e selecionar a alternativa correta (de A até E).
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
            adicionar_pontos(25)
            st.success(f"🎉 Resposta Correta! A **{equipe_atual}** pontuou e avança para a próxima etapa.")
            st.session_state.fase = 2
            passar_turno()
            st.rerun()
        else:
            st.error(f"❌ Resposta Incorreta! A **{equipe_atual}** errou. O turno passa automaticamente para a próxima equipe!")
            st.session_state.estabilidade -= 15
            passar_turno()
            st.rerun()

# ==========================================
# FASE 2: DISSERTATIVA COM AVALIAÇÃO POR PALAVRAS-CHAVE
# ==========================================
elif st.session_state.fase == 2:
    st.subheader("Fase 2: O Enigma Cosmológico (Questão Dissertativa)")
    
    # Pega a questão do banco dinâmico
    q_data = st.session_state.banco_questoes.get("dissertativa_1")
    
    st.markdown(f"""
    > *Makarius* desafia a **{equipe_atual}** com uma questão complexa:
    > **"{q_data['enunciado']}"**
    
    *Nota do Sistema:* Escreva livremente. O avaliador inteligente verificará se os conceitos fundamentais estão presentes na sua explicação.
    """)

    texto_dissertacao = st.text_area("✍️ Digite a resposta dissertativa da equipe:", key="dissertacao_f2")

    if st.button("Enviar Resposta Dissertativa"):
        texto_lower = texto_dissertacao.lower()
        
        # Salva no histórico administrativo
        st.session_state.historico_respostas.append({
            "equipe": equipe_atual,
            "fase": 2,
            "resposta": texto_dissertacao
        })
        
        # Verifica se pelo menos 2 palavras-chave do banco estão presentes no texto do aluno
        acertos = sum(1 for termo in q_data["palavras_chave"] if termo in texto_lower)
        
        if len(texto_dissertacao.strip()) > 10 and acertos >= 2:
            adicionar_pontos(40)
            st.success(f"🌟 Resposta Validada com Sucesso! A **{equipe_atual}** demonstrou total compreensão conceitual (Termos correlacionados identificados).")
            st.session_state.fase = 3
            passar_turno()
            st.rerun()
        else:
            st.error(f"❌ A resposta ficou incompleta ou faltaram termos essenciais (como *{', '.join(q_data['palavras_chave'])}*). A **{equipe_atual}** errou, e o turno passa para a próxima equipe!")
            st.session_state.estabilidade -= 20
            passar_turno()
            st.rerun()

# ==========================================
# FASE 3: SEGUNDA DISSERTATIVA (MATÉRIA ESCURA)
# ==========================================
elif st.session_state.fase == 3:
    st.subheader("Fase 3: A Câmara da Matéria Escura (Questão Dissertativa)")
    
    q_data_2 = st.session_state.banco_questoes.get("dissertativa_2", st.session_state.banco_questoes["dissertativa_1"])
    
    st.markdown(f"""
    > Chegando na câmara principal, *Makarius* testa o conhecimento final da **{equipe_atual}**:
    > **"{q_data_2['enunciado']}"**
    """)

    texto_dissertacao_2 = st.text_area("✍️ Escreva a explanação final da equipe:", key="dissertacao_f3")

    if st.button("Concluir e Validar com o Administrador"):
        texto_lower_2 = texto_dissertacao_2.lower()
        
        # Salva no histórico administrativo
        st.session_state.historico_respostas.append({
            "equipe": equipe_atual,
            "fase": 3,
            "resposta": texto_dissertacao_2
        })
        
        acertos_2 = sum(1 for termo in q_data_2["palavras_chave"] if termo in texto_lower_2)
        
        if len(texto_dissertacao_2.strip()) > 10 and acertos_2 >= 2:
            adicionar_pontos(50)
            st.success(f"✨ Perfeito! A **{equipe_atual}** gabaritou a fase final com conceitos precisos!")
            st.session_state.fase = 4
            st.rerun()
        else:
            st.error(f"❌ Conceitos fundamentais ausentes na dissertação. A **{equipe_atual}** passou a vez para a próxima equipe tentar o fechamento!")
            st.session_state.estabilidade -= 20
            passar_turno()
            st.rerun()

# ==========================================
# FASE 4: CONCLUSÃO E RESULTADOS
# ==========================================
elif st.session_state.fase == 4:
    st.balloons()
    st.subheader("Fase Final: A Revelação do Santuário 🏛️")
    st.markdown("""
    > *Makarius* sorri e revela a verdadeira intenção: 
    > *"Eu nunca quis destruir o cosmo! As anomalias e enigmas foram um teste planejado junto com Raquel Ferreira. Vocês provaram que dominam a ciência por trás das estrelas!"*
    """)
    
    st.markdown("---")
    st.markdown("### 🏆 **Placar Final da Batalha do Conhecimento**")
    st.markdown(f"* **🛡️ Equipe Alfa:** {st.session_state.pontos_alfa} pontos")
    st.markdown(f"* **🛡️ Equipe Beta:** {st.session_state.pontos_beta} pontos")
    st.markdown(f"* **🛡️ Equipe Gama:** {st.session_state.pontos_gama} pontos")
    st.markdown(f"* **🌌 Estabilidade Final do Cosmo:** {st.session_state.estabilidade}%")
    
    # Determina o vencedor
    pontuacoes = {
        "Equipe Alfa": st.session_state.pontos_alfa,
        "Equipe Beta": st.session_state.pontos_beta,
        "Equipe Gama": st.session_state.pontos_gama
    }
    vencedor = max(pontuacoes, key=pontuacoes.get)
    maior_pontuacao = pontuacoes[vencedor]
    
    # Verifica empate
    vencedores = [eq for eq, pts in pontuacoes.items() if pts == maior_pontuacao]
    
    if len(vencedores) > 1:
        st.success(f"🤝 **Empate Magnífico entre: {', '.join(vencedores)}! O universo foi salvo em conjunto!**")
    else:
        st.success(f"🥇 **{vencedor} Venceu a Jornada Cósmica com {maior_pontuacao} pontos!**")

    if st.button("🔄 Reiniciar Jogo Completo"):
        st.session_state.fase = 1
        st.session_state.pontos_alfa = 0
        st.session_state.pontos_beta = 0
        st.session_state.pontos_gama = 0
        st.session_state.indice_equipe = 0
        st.session_state.estabilidade = 100
        st.rerun()

