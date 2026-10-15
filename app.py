import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="CDZ: Rumo a Athena - Cosmologia", page_icon="🌌", layout="centered")

# ==========================================
# INICIALIZAÇÃO DO ESTADO GLOBAL
# ==========================================
if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False
if "equipe_atual_idx" not in st.session_state:
    st.session_state.indice_equipe = 0
if "pontos_alfa" not in st.session_state:
    st.session_state.pontos_alfa = 0
if "pontos_beta" not in st.session_state:
    st.session_state.pontos_beta = 0
if "pontos_gama" not in st.session_state:
    st.session_state.pontos_gama = 0
if "lista_equipes" not in st.session_state:
    st.session_state.lista_equipes = ["Equipe Alfa", "Equipe Beta", "Equipe Gama"]
if "pergunta_atual_idx" not in st.session_state:
    st.session_state.pergunta_atual_idx = 0
if "estabilidade" not in st.session_state:
    st.session_state.estabilidade = 100
if "historico_respostas" not in st.session_state:
    st.session_state.historico_respostas = []

# Banco robusto de questões conceituais (Múltipla Escolha A-E e Dissertativas)
if "banco_questoes" not in st.session_state:
    st.session_state.banco_questoes = [
        # Fase 1: Big Bang e Expansão
        {
            "tipo": "multipla",
            "guia": "Mu de Áries",
            "enunciado": "O que o modelo cosmológico do Big Bang postula sobre a origem do Universo?",
            "opcoes": [
                "A) O universo sempre existiu estático, eterno e do mesmo tamanho.",
                "B) O cosmos originou-se de uma singularidade extremamente densa e quente, expandindo-se continuamente desde então.",
                "C) As galáxias formaram-se a partir de colisões repentinas de buracos negros parados.",
                "D) O universo expande-se porque as estrelas criam matéria do nada nos vazios.",
                "E) A origem é cíclica, colapsando exatamente a cada 100 anos."
            ],
            "correta": "B",
            "explicacao": "O Big Bang descreve a expansão métrica do espaço a partir de um estado inicial de alta densidade e temperatura."
        },
        {
            "tipo": "dissertativa",
            "guia": "Aldebaran de Touro",
            "enunciado": "Explique brevemente como a analogia do balão de festa preenchendo ar ajuda a entender a expansão do universo.",
            "palavras_chave": ["balão", "superfície", "afastam", "espaço", "expansão", "pontos"],
            "explicacao": "À medida que o balão infla, os pontos desenhados na sua superfície se afastam uns dos outros porque o próprio espaço da borracha se expande, assim como as galáxias."
        },
        {
            "tipo": "multipla",
            "guia": "Saga de Gêmeos",
            "enunciado": "Qual é a principal evidência observacional que corrobora a expansão do Universo?",
            "opcoes": [
                "A) O desvio para o vermelho (redshift) das galáxias distantes, formulado na Lei de Hubble.",
                "B) A colisão frequente de planetas no sistema solar.",
                "C) O resfriamento rápido do Sol observado por telescópios modernos.",
                "D) A ausência completa de radiação no espaço interestelar.",
                "E) A rotação estática das estrelas fixas na esfera celeste."
            ],
            "correta": "A",
            "explicacao": "O redshift demonstra que as galáxias estão se afastando umas das outras, comprovando a expansão cósmica."
        },
        # Fase 2: Relatividade Geral
        {
            "tipo": "multipla",
            "guia": "Aioria de Leão",
            "enunciado": "Segundo a Teoria da Relatividade Geral de Einstein, como a gravidade é entendida no cosmos?",
            "opcoes": [
                "A) Uma força magnética invisível emitida pelos planetas.",
                "B) Uma atração mecânica instantânea entre corpos rígidos.",
                "C) A curvatura do espaço-tempo provocada pela presença de massa e energia.",
                "D) O atrito gerado pelo vento solar nas galáxias.",
                "E) Uma ilusão óptica causada pela atmosfera terrestre."
            ],
            "correta": "C",
            "explicacao": "A massa curva o tecido quadridimensional do espaço-tempo, determinando como os corpos se movimentam."
        },
        {
            "tipo": "dissertativa",
            "guia": "Shaka de Virgem",
            "enunciado": "O que indica a curvatura do espaço-tempo em regiões com grande concentração de massa, como buracos negros?",
            "palavras_chave": ["curvatura", "massa", "gravidade", "luz", "espaço-tempo", "intensa"],
            "explicacao": "Altas densidades geram curvaturas extremas capazes de reter até mesmo a luz, formando o horizonte de eventos."
        },
        # Fase 3: Matéria Escura e Energia Escura
        {
            "tipo": "multipla",
            "guia": "Dohko de Libra",
            "enunciado": "Qual é a principal função da Matéria Escura na estrutura em grande escala do universo?",
            "opcoes": [
                "A) Emitir radiação intensa para aquecer planetas distantes.",
                "B) Atuar como uma 'cola gravitacional' invisível que impede as galáxias de se dispersarem.",
                "C) Acelerar infinitamente a expansão do cosmos.",
                "D) Absorver buracos negros para criar novos sistemas solares.",
                "E) Bloquear a luz das estrelas jovens."
            ],
            "correta": "B",
            "explicacao": "A matéria escura fornece a massa gravitacional adicional necessária para manter as galáxias coesas."
        },
        {
            "tipo": "dissertativa",
            "guia": "Milo de Escorpião",
            "enunciado": "Qual é a diferença conceitual básica entre Matéria Escura e Energia Escura no cosmos?",
            "palavras_chave": ["atração", "expansão", "aceleração", "massa", "energia", "gravidade"],
            "explicacao": "Enquanto a matéria escura exerce atração gravitacional (unindo estruturas), a energia escura atua como uma pressão repulsiva que acelera a expansão do universo."
        },
        {
            "tipo": "multipla",
            "guia": "Shura de Capricórnio",
            "enunciado": "O que a Radiação Cósmica de Fundo em Micro-ondas (CMB) representa para a cosmologia moderna?",
            "opcoes": [
                "A) O eco térmico remanescente dos primeiros momentos após o Big Bang.",
                "B) A energia gerada pelas supernovas na Via Láctea.",
                "C) O calor emitido pelo núcleo de buracos negros supermassivos.",
                "D) Interferência de rádio gerada por civilizações alienígenas.",
                "E) Luz refletida pela poeira interestelar."
            ],
            "correta": "A",
            "explicacao": "A CMB é a radiação fóssil do universo primordial, quando este se tornou transparente após o resfriamento inicial."
        }
    ]

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

st.title("🏛️ CDZ: A Ascensão ao Santuário de Athena")
st.markdown("### *Jornada Cosmológica: Big Bang, Relatividade e Matéria Escura*")
st.markdown("---")

# ==========================================
# PAINEL DO ADMINISTRADOR & GABARITO
# ==========================================
st.sidebar.header("⚙️ Painel do Administrador")
with st.sidebar.expander("📚 Baixar Gabarito Oficial"):
    st.markdown("Gabarito completo com todas as respostas corretas e explicações conceituais:")
    texto_gabarito = "# GABARITO OFICIAL - CDZ COSMOLOGIA\n\n"
    for i, q in enumerate(st.session_state.banco_questoes, 1):
        texto_gabarito += f"Questão {i} ({q['guia']}):\n"
        texto_gabarito += f"Enunciado: {q['enunciado']}\n"
        if q['tipo'] == 'multipla':
            texto_gabarito += f"Resposta Correta: {q['correta']}\n"
        else:
            texto_gabarito += f"Palavras-chave esperadas: {', '.join(q['palavras_chave'])}\n"
        texto_gabarito += f"Explicação: {q['explicacao']}\n\n"
    
    st.download_button(
        label="📥 Baixar Gabarito (TXT/PDF)",
        data=texto_gabarito,
        file_name="gabarito_cdz_cosmologia.txt",
        mime="text/plain"
    )

with st.sidebar.expander("🛠️ Gerenciar Questões e Histórico"):
    if st.session_state.historico_respostas:
        st.markdown("### Respostas Registradas:")
        for h in st.session_state.historico_respostas:
            st.text(f"[{h['equipe']}] Q{h['questao']}: {h['resposta'][:30]}...")
        if st.button("🗑️ Limpar Histórico"):
            st.session_state.historico_respostas = []
            st.rerun()
    else:
        st.info("Nenhuma resposta enviada ainda.")

# ==========================================
# SORTEIO INICIAL DA EQUIPE
# ==========================================
if not st.session_state.jogo_iniciado:
    st.subheader("🎲 Sorteio Inicial do Santuário")
    st.markdown("Clique no botão abaixo para realizar o sorteio e definir qual equipe dará o primeiro passo rumo a Athena!")
    
    if st.button("Realizar Sorteio da Equipe Inicial"):
        st.session_state.indice_equipe = random.randint(0, 2)
        st.session_state.jogo_iniciado = True
        st.rerun()
    st.stop()

equipe_atual = st.session_state.lista_equipes[st.session_state.indice_equipe]
st.sidebar.header("📊 Placar das Equipes")
st.sidebar.metric(label="🛡️ Equipe Alfa", value=st.session_state.pontos_alfa)
st.sidebar.metric(label="🛡️ Equipe Beta", value=st.session_state.pontos_beta)
st.sidebar.metric(label="🛡️ Equipe Gama", value=st.session_state.pontos_gama)
st.sidebar.metric(label="⚡ Estabilidade do Cosmo", value=f"{st.session_state.estabilidade}%")
st.sidebar.markdown(f"**Turno Atual:** ⚔️ {equipe_atual}")

# ==========================================
# PROGRESSO DO JOGO (QUESTÕES)
# ==========================================
idx_q = st.session_state.pergunta_atual_idx

if idx_q < len(st.session_state.banco_questoes):
    questao = st.session_state.banco_questoes[idx_q]
    
    st.subheader(f"🏛️ Estação Guiada por: **{questao['guia']}** (Questão {idx_q + 1} de {len(st.session_state.banco_questoes)})")
    st.markdown(f"> *{questao['guia']} aparece no templo e desafia a **{equipe_atual}** com um enigma cósmico:*")
    st.markdown(f"### **{questao['enunciado']}**")
    
    # Se for múltipla escolha (A a E)
    if questao['tipo'] == 'multipla':
        escolha = st.radio("Selecione a alternativa correta:", questao['opcoes'], key=f"q_{idx_q}")
        
        if st.button("Submeter Resposta"):
            letra_escolhida = escolha.split(")")[0].strip()
            
            # Salva histórico
            st.session_state.historico_respostas.append({
                "equipe": equipe_atual,
                "questao": idx_q + 1,
                "resposta": escolha
            })
            
            if letra_escolhida == questao['correta']:
                st.success(f"🎉 Correto! A **{equipe_atual}** elevou seu cosmo e marcou pontos!")
                if equipe_atual == "Equipe Alfa": st.session_state.pontos_alfa += 20
                elif equipe_atual == "Equipe Beta": st.session_state.pontos_beta += 20
                else: st.session_state.pontos_gama += 20
                
                st.session_state.pergunta_atual_idx += 1
                st.session_state.indice_equipe = (st.session_state.indice_equipe + 1) % 3
                st.rerun()
            else:
                st.error(f"❌ Resposta Incorreta! A **{equipe_atual}** errou. O turno passa para a próxima equipe!")
                st.session_state.estabilidade -= 10
                st.session_state.indice_equipe = (st.session_state.indice_equipe + 1) % 3
                st.rerun()

    # Se for questão dissertativa curta (Avaliação por palavras-chave)
    elif questao['tipo'] == 'dissertativa':
        resposta_usuario = st.text_area("✍️ Escreva a resposta conceitual da equipe:", key=f"diss_{idx_q}")
        
        if st.button("Validar Resposta com o Guardião"):
            texto_lower = resposta_usuario.lower()
            
            st.session_state.historico_respostas.append({
                "equipe": equipe_atual,
                "questao": idx_q + 1,
                "resposta": resposta_usuario
            })
            
            # Verifica se pelo menos 2 palavras-chave aparecem no texto do aluno
            acertos = sum(1 for p in questao['palavras_chave'] if p in texto_lower)
            
            if len(resposta_usuario.strip()) > 5 and acertos >= 2:
                st.success(f"🌟 Excelente! O guardião validou os conceitos fundamentais na resposta da **{equipe_atual}**!")
                if equipe_atual == "Equipe Alfa": st.session_state.pontos_alfa += 30
                elif equipe_atual == "Equipe Beta": st.session_state.pontos_beta += 30
                else: st.session_state.pontos_gama += 30
                
                st.session_state.pergunta_atual_idx += 1
                st.session_state.indice_equipe = (st.session_state.indice_equipe + 1) % 3
                st.rerun()
            else:
                st.error(f"❌ Resposta incompleta ou faltaram termos essenciais. A **{equipe_atual}** passou a vez!")
                st.session_state.estabilidade -= 15
                st.session_state.indice_equipe = (st.session_state.indice_equipe + 1) % 3
                st.rerun()

else:
    # FASE FINAL: CHEGADA AO TETO DE ATHENA
    st.balloons()
    st.subheader("🏛️ Chegada ao Templo de Athena!")
    st.markdown("""
    > As equipes superaram todas as doze casas, decifrando os mistérios do Big Bang, da Relatividade e da Matéria Escura. 
    > Athena surge no topo do santuário, abençoando o cosmo de todos os participantes!
    """)
    
    st.markdown("---")
    st.markdown("### 🏆 **Placar Final das Equipes**")
    st.markdown(f"* **🛡️ Equipe Alfa:** {st.session_state.pontos_alfa} pontos")
    st.markdown(f"* **🛡️ Equipe Beta:** {st.session_state.pontos_beta} pontos")
    st.markdown(f"* **🛡️ Equipe Gama:** {st.session_state.pontos_gama} pontos")
    st.markdown(f"* **⚡ Estabilidade Final do Cosmo:** {st.session_state.estabilidade}%")
    
    pontuacoes = {
        "Equipe Alfa": st.session_state.pontos_alfa,
        "Equipe Beta": st.session_state.pontos_beta,
        "Equipe Gama": st.session_state.pontos_gama
    }
    vencedor = max(pontuacoes, key=pontuacoes.get)
    st.success(f"🥇 **A {vencedor} conquistou a vitória e salvou o Santuário junto a Athena!**")
    
    if st.button("🔄 Reiniciar Nova Jornada"):
        st.session_state.jogo_iniciado = False
        st.session_state.pergunta_atual_idx = 0
        st.session_state.pontos_alfa = 0
        st.session_state.pontos_beta = 0
        st.session_state.pontos_gama = 0
        st.session_state.estabilidade = 100
        st.rerun()

