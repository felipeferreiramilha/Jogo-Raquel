import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="CDZ: Rumo a Athena - Rodadas por Equipe", page_icon="🌌", layout="centered")

# ==========================================
# INICIALIZAÇÃO DO ESTADO GLOBAL
# ==========================================
if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False
if "rodada_atual" not in st.session_state:
    st.session_state.rodada_atual = 1
if "pontos_alfa" not in st.session_state:
    st.session_state.pontos_alfa = 0
if "pontos_beta" not in st.session_state:
    st.session_state.pontos_beta = 0
if "pontos_gama" not in st.session_state:
    st.session_state.pontos_gama = 0
if "estabilidade" not in st.session_state:
    st.session_state.estabilidade = 100
if "historico_respostas" not in st.session_state:
    st.session_state.historico_respostas = []

# Banco robusto de questões divididas por rodadas (3 equipes por rodada)
if "banco_rodadas" not in st.session_state:
    st.session_state.banco_rodadas = [
        # --- RODADA 1 ---
        {
            "rodada": 1,
            "questoes": {
                "Equipe Alfa": {
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
                    "explicacao": "O Big Bang descreve a expansão métrica do espaço a partir de um estado inicial de alta densidade."
                },
                "Equipe Beta": {
                    "tipo": "dissertativa",
                    "guia": "Aldebaran de Touro",
                    "enunciado": "Explique brevemente como a analogia do balão de festa preenchendo ar ajuda a entender a expansão do universo.",
                    "palavras_chave": ["balão", "superfície", "afastam", "espaço", "expansão", "pontos"],
                    "explicacao": "À medida que o balão infla, os pontos em sua superfície se afastam porque o próprio espaço da borracha se expande."
                },
                "Equipe Gama": {
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
                    "explicacao": "O redshift demonstra que as galáxias estão se afastando umas das outras."
                }
            }
        },
        # --- RODADA 2 ---
        {
            "rodada": 2,
            "questoes": {
                "Equipe Alfa": {
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
                    "explicacao": "A massa curva o tecido quadridimensional do espaço-tempo."
                },
                "Equipe Beta": {
                    "tipo": "dissertativa",
                    "guia": "Shaka de Virgem",
                    "enunciado": "O que indica a curvatura extrema do espaço-tempo em regiões de altíssima densidade, como buracos negros?",
                    "palavras_chave": ["curvatura", "massa", "gravidade", "luz", "espaço-tempo", "intensa"],
                    "explicacao": "Altas densidades geram gravidade capaz de aprisionar até mesmo a luz no horizonte de eventos."
                },
                "Equipe Gama": {
                    "tipo": "multipla",
                    "guia": "Milo de Escorpião",
                    "enunciado": "O que a Radiação Cósmica de Fundo em Micro-ondas (CMB) representa para a cosmologia?",
                    "opcoes": [
                        "A) O eco térmico remanescente dos primeiros momentos após o Big Bang.",
                        "B) A energia gerada pelas supernovas na Via Láctea.",
                        "C) O calor emitido pelo núcleo de buracos negros supermassivos.",
                        "D) Interferência de rádio gerada por civilizações alienígenas.",
                        "E) Luz refletida pela poeira interestelar."
                    ],
                    "correta": "A",
                    "explicacao": "A CMB é a radiação fóssil do universo primordial após o resfriamento inicial."
                }
            }
        },
        # --- RODADA 3 ---
        {
            "rodada": 3,
            "questoes": {
                "Equipe Alfa": {
                    "tipo": "dissertativa",
                    "guia": "Dohko de Libra",
                    "enunciado": "Qual é a função essencial da Matéria Escura na estruturação das grandes galáxias?",
                    "palavras_chave": ["matéria escura", "gravidade", "cola", "invisível", "massa", "atração", "galaxias"],
                    "explicacao": "A matéria escura atua como uma armação gravitacional invisível que mantém as galáxias coesas."
                },
                "Equipe Beta": {
                    "tipo": "multipla",
                    "guia": "Shura de Capricórnio",
                    "enunciado": "Qual é a diferença conceitual básica entre Matéria Escura e Energia Escura?",
                    "opcoes": [
                        "A) A matéria escura atrai (gravidade), enquanto a energia escura repele (acelera a expansão).",
                        "B) Ambas fazem exatamente a mesma coisa na estrutura cósmica.",
                        "C) A energia escura é visível em telescópios ópticos comuns.",
                        "D) A matéria escura acelera o universo para fora, enquanto a energia escura o comprime.",
                        "E) Não há diferença teórica entre ambas."
                    ],
                    "correta": "A",
                    "explicacao": "Matéria escura gera atração gravitacional, ao passo que a energia escura impulsiona a expansão acelerada."
                },
                "Equipe Gama": {
                    "tipo": "dissertativa",
                    "guia": "Camus de Aquário",
                    "enunciado": "Explique de forma resumida o conceito de singularidade cósmica associado ao início do universo.",
                    "palavras_chave": ["singularidade", "ponto", "densidade", "infinita", "quente", "inicio"],
                    "explicacao": "Estado de densidade e temperatura infinitas onde as leis físicas tradicionais deixam de funcionar antes da expansão."
                }
            }
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
st.markdown("### *Batalha em Rodadas Simultâneas: Cosmologia, Relatividade e Big Bang*")
st.markdown("---")

# ==========================================
# PAINEL DO ADMINISTRADOR & GABARITO
# ==========================================
st.sidebar.header("⚙️ Painel do Administrador")
with st.sidebar.expander("📚 Baixar Gabarito Oficial"):
    texto_gabarito = "# GABARITO OFICIAL - CDZ COSMOLOGIA\n\n"
    for r in st.session_state.banco_rodadas:
        texto_gabarito += f"=== RODADA {r['rodada']} ===\n"
        for eq, q in r['questoes'].items():
            texto_gabarito += f"[{eq}] Guia: {q['guia']}\nEnunciado: {q['enunciado']}\n"
            if q['tipo'] == 'multipla':
                texto_gabarito += f"Correta: {q['correta']}\n"
            else:
                texto_gabarito += f"Termos-chave: {', '.join(q['palavras_chave'])}\n"
            texto_gabarito += f"Explicação: {q['explicacao']}\n\n"
    
    st.download_button(
        label="📥 Baixar Gabarito (TXT)",
        data=texto_gabarito,
        file_name="gabarito_rodadas_cdz.txt",
        mime="text/plain"
    )

with st.sidebar.expander("🛠️ Histórico de Respostas"):
    if st.session_state.historico_respostas:
        for h in st.session_state.historico_respostas:
            st.text(f"[R{h['rodada']} - {h['equipe']}] {h['resposta'][:35]}...")
        if st.button("🗑️ Limpar Histórico"):
            st.session_state.historico_respostas = []
            st.rerun()
    else:
        st.info("Nenhuma resposta enviada ainda.")

# ==========================================
# SORTEIO DA ORDEM / INÍCIO DO JOGO
# ==========================================
if not st.session_state.jogo_iniciado:
    st.subheader("🎲 Início das Rodadas do Santuário")
    st.markdown("Neste modo, **todas as 3 equipes competem simultaneamente em cada rodada**, enfrentando desafios propostos pelos Cavaleiros de Ouro.")
    
    if st.button("Iniciar Batalha das Equipes"):
        st.session_state.jogo_iniciado = True
        st.rerun()
    st.stop()

# Placar lateral
st.sidebar.header("📊 Placar Geral")
st.sidebar.metric(label="🛡️ Equipe Alfa", value=st.session_state.pontos_alfa)
st.sidebar.metric(label="🛡️ Equipe Beta", value=st.session_state.pontos_beta)
st.sidebar.metric(label="🛡️ Equipe Gama", value=st.session_state.pontos_gama)
st.sidebar.metric(label="⚡ Estabilidade do Cosmo", value=f"{st.session_state.estabilidade}%")

# ==========================================
# EXECUÇÃO DAS RODADAS
# ==========================================
total_rodadas = len(st.session_state.banco_rodadas)
r_atual = st.session_state.rodada_atual

if r_atual <= total_rodadas:
    dados_rodada = st.session_state.banco_rodadas[r_atual - 1]
    
    st.subheader(f"⚔️ **RODADA {r_atual} DE {total_rodadas}**")
    st.markdown("Cada equipe deve responder ao seu desafio específico desta rodada abaixo:")
    st.markdown("---")
    
    # Formulário para capturar as respostas simultâneas da rodada
    with st.form(key=f"form_rodada_{r_atual}"):
        respostas_usuario = {}
        
        for equipe, questao in dados_rodada["questoes"].items():
            st.markdown(f"#### 🛡️ **{equipe}** (Guia: *{questao['guia']}*)")
            st.markdown(f"**Desafio:** {questao['enunciado']}")
            
            if questao['tipo'] == 'multipla':
                resp = st.radio(f"Escolha a alternativa ({equipe}):", questao['opcoes'], key=f"r{r_atual}_{equipe}")
                respostas_usuario[equipe] = resp
            else:
                resp_diss = st.text_area(f"Escreva a resposta conceitual ({equipe}):", key=f"d{r_atual}_{equipe}")
                respostas_usuario[equipe] = resp_diss
            st.markdown("---")
            
        enviado = st.form_submit_button("Submeter Respostas da Rodada")
        
        if enviado:
            # Processa a correção de cada equipe na rodada
            for equipe, questao in dados_rodada["questoes"].items():
                resp_dada = respostas_usuario[equipe]
                
                # Salva histórico
                st.session_state.historico_respostas.append({
                    "rodada": r_atual,
                    "equipe": equipe,
                    "resposta": resp_dada
                })
                
                if questao['tipo'] == 'multipla':
                    letra = resp_dada.split(")")[0].strip()
                    if letra == questao['correta']:
                        if equipe == "Equipe Alfa": st.session_state.pontos_alfa += 25
                        elif equipe == "Equipe Beta": st.session_state.pontos_beta += 25
                        else: st.session_state.pontos_gama += 25
                    else:
                        st.session_state.estabilidade -= 5
                else:
                    texto_l = resp_dada.lower()
                    acertos = sum(1 for p in questao['palavras_chave'] if p in texto_l)
                    if len(resp_dada.strip()) > 5 and acertos >= 2:
                        if equipe == "Equipe Alfa": st.session_state.pontos_alfa += 35
                        elif equipe == "Equipe Beta": st.session_state.pontos_beta += 35
                        else: st.session_state.pontos_gama += 35
                    else:
                        st.session_state.estabilidade -= 8
            
            st.success(f"✅ Rodada {r_atual} concluída e pontuações computadas com sucesso!")
            st.session_state.rodada_atual += 1
            st.rerun()

else:
    # FASE FINAL: CHEGADA AO TETO DE ATHENA
    st.balloons()
    st.subheader("🏛️ Chegada ao Templo de Athena!")
    st.markdown("""
    > Todas as rodadas foram concluídas! As equipes superaram os doze templos, decifrando os enigmas da física moderna. 
    > Athena surge no topo do santuário para abençoar os vencedores!
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
    maior_pts = pontuacoes[vencedor]
    
    vencedores = [eq for eq, pts in pontuacoes.items() if pts == maior_pts]
    if len(vencedores) > 1:
        st.success(f"🤝 **Empate Glorioso entre: {', '.join(vencedores)}! Salvaram o Santuário juntos!**")
    else:
        st.success(f"🥇 **A {vencedor} conquistou a vitória absoluta com {maior_pts} pontos junto a Athena!**")
    
    if st.button("🔄 Reiniciar Nova Batalha"):
        st.session_state.jogo_iniciado = False
        st.session_state.rodada_atual = 1
        st.session_state.pontos_alfa = 0
        st.session_state.pontos_beta = 0
        st.session_state.pontos_gama = 0
        st.session_state.estabilidade = 100
        st.rerun()

