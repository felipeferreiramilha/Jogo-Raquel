import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="CDZ: Rumo a Athena - Modo Individual por Equipe", page_icon="🌌", layout="centered")

# ==========================================
# INICIALIZAÇÃO DO ESTADO GLOBAL
# ==========================================
if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False
if "rodada_atual" not in st.session_state:
    st.session_state.rodada_atual = 1
if "equipe_sub_idx" not in st.session_state:
    st.session_state.equipe_sub_idx = 0  # 0: Alfa, 1: Beta, 2: Gama
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
if "mensagem_feedback" not in st.session_state:
    st.session_state.mensagem_feedback = None

# Banco de questões organizadas por Rodada e Equipes
if "banco_rodadas" not in st.session_state:
    st.session_state.banco_rodadas = [
        # --- RODADA 1 ---
        {
            "rodada": 1,
            "questoes": [
                {
                    "equipe": "Equipe Alfa",
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
                    "porque": "O Big Bang não foi uma explosão no espaço, mas sim a expansão inicial do próprio espaço-tempo a partir de uma singularidade inicial quente e densa."
                },
                {
                    "equipe": "Equipe Beta",
                    "tipo": "dissertativa",
                    "guia": "Aldebaran de Touro",
                    "enunciado": "Explique brevemente como a analogia do balão de festa sendo inflado ajuda a entender a expansão do universo.",
                    "palavras_chave": ["balão", "superfície", "afastam", "espaço", "expansão", "pontos"],
                    "porque": "À medida que o balão enche, a borracha (o espaço) se estica, fazendo com que todos os pontos (galáxias) se afastem uns dos outros sem que exista um centro único de expansão."
                },
                {
                    "equipe": "Equipe Gama",
                    "tipo": "multipla",
                    "guia": "Saga de Gêmeos",
                    "enunciado": "Qual é a principal evidência observacional que comprova a expansão contínua do Universo?",
                    "opcoes": [
                        "A) O desvio para o vermelho (redshift) das galáxias distantes, formulado na Lei de Hubble.",
                        "B) A colisão frequente de planetas no sistema solar.",
                        "C) O resfriamento rápido do Sol observado por telescópios modernos.",
                        "D) A ausência completa de radiação no espaço interestelar.",
                        "E) A rotação estática das estrelas fixas na esfera celeste."
                    ],
                    "correta": "A",
                    "porque": "O 'redshift' ocorre porque as ondas de luz de galáxias distantes são esticadas pela expansão do espaço, deslocando seu espectro para o vermelho."
                }
            ]
        },
        # --- RODADA 2 ---
        {
            "rodada": 2,
            "questoes": [
                {
                    "equipe": "Equipe Alfa",
                    "tipo": "multipla",
                    "guia": "Aioria de Leão",
                    "enunciado": "Segundo a Teoria da Relatividade Geral de Einstein, como a gravidade é compreendida no cosmos?",
                    "opcoes": [
                        "A) Uma força magnética invisível emitida pelos planetas.",
                        "B) Uma atração mecânica instantânea entre corpos rígidos.",
                        "C) A curvatura do tecido do espaço-tempo provocada pela presença de massa e energia.",
                        "D) O atrito gerado pelo vento solar nas galáxias.",
                        "E) Uma ilusão óptica causada pela atmosfera terrestre."
                    ],
                    "porque": "Einstein demonstrou que objetos massivos deformam o tecido do espaço-tempo ao seu redor, e a gravidade é o efeito dessa curvatura na trajetória dos corpos."
                },
                {
                    "equipe": "Equipe Beta",
                    "tipo": "dissertativa",
                    "guia": "Shaka de Virgem",
                    "enunciado": "O que ocorre com a curvatura do espaço-tempo em regiões de altíssima densidade, como nos buracos negros?",
                    "palavras_chave": ["curvatura", "massa", "gravidade", "luz", "espaço-tempo", "intensa"],
                    "porque": "A concentração extrema de massa gera uma curvatura tão acentuada no espaço-tempo que cria o horizonte de eventos, de onde nem mesmo a luz consegue escapar."
                },
                {
                    "equipe": "Equipe Gama",
                    "tipo": "multipla",
                    "guia": "Milo de Escorpião",
                    "enunciado": "O que a Radiação Cósmica de Fundo em Micro-ondas (CMB) representa para a cosmologia?",
                    "opcoes": [
                        "A) O eco térmico remanescente dos primeiros momentos após o Big Bang.",
                        "B) A energia gerada pelas supernovas na Via Láctea.",
                        "C) O calor emitido pelo núcleo de buracos negros supermassivos.",
                        "D) Interferência de rádio gerada por estrelas de nêutrons.",
                        "E) Luz refletida pela poeira interestelar."
                    ],
                    "correta": "A",
                    "porque": "A CMB é a radiação fóssil emitida cerca de 380 mil anos após o Big Bang, quando o universo esfriou o suficiente para os fótons viajarem livremente."
                }
            ]
        },
        # --- RODADA 3 ---
        {
            "rodada": 3,
            "questoes": [
                {
                    "equipe": "Equipe Alfa",
                    "tipo": "dissertativa",
                    "guia": "Dohko de Libra",
                    "enunciado": "Qual é o papel fundamental da Matéria Escura na manutenção e estrutura das galáxias?",
                    "palavras_chave": ["matéria escura", "gravidade", "cola", "invisível", "massa", "atração", "galaxias"],
                    "porque": "Como a matéria visível não possui massa suficiente para manter as galáxias unidas em altas velocidades de rotação, a matéria escura fornece a atração gravitacional invisível necessária."
                },
                {
                    "equipe": "Equipe Beta",
                    "tipo": "multipla",
                    "guia": "Shura de Capricórnio",
                    "enunciado": "Qual é a principal diferença conceitual entre Matéria Escura e Energia Escura?",
                    "opcoes": [
                        "A) A matéria escura atrai (gravidade), enquanto a energia escura repele (acelera a expansão).",
                        "B) Ambas fazem exatamente a mesma coisa na estrutura cósmica.",
                        "C) A energia escura é visível em telescópios ópticos comuns.",
                        "D) A matéria escura acelera o universo para fora, enquanto a energia escura o comprime.",
                        "E) Não há diferença teórica entre ambas."
                    ],
                    "correta": "A",
                    "porque": "A matéria escura atua agrupando as galáxias através da gravidade, enquanto a energia escura é a força misteriosa que acelera a expansão do tecido do universo."
                },
                {
                    "equipe": "Equipe Gama",
                    "tipo": "dissertativa",
                    "guia": "Camus de Aquário",
                    "enunciado": "Explique resumidamente o conceito de singularidade cosmológica no contexto do Big Bang.",
                    "palavras_chave": ["singularidade", "ponto", "densidade", "infinita", "quente", "inicio"],
                    "porque": "A singularidade é um estado em que toda a matéria e energia do universo observável estavam concentradas em um ponto de densidade e temperatura infinitas."
                }
            ]
        }
    ]

# Estilo visual
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #ffffff; }
    .stButton>button {
        width: 100%; background-color: #1f4068; color: white;
        border-radius: 8px; font-weight: bold; border: 1px solid #00b4d8;
    }
    .stButton>button:hover { background-color: #00b4d8; color: black; }
    </style>
""", unsafe_allow_html=True)

st.title("🏛️ CDZ: A Ascensão ao Santuário de Athena")
st.markdown("### *Desafios Individuais por Equipe: Big Bang, Relatividade e Matéria Escura*")
st.markdown("---")

# ==========================================
# PAINEL DO ORGANIZADOR (EXPORTAÇÃO WORD / TXT)
# ==========================================
st.sidebar.header("⚙️ Painel do Organizador")

with st.sidebar.expander("📄 Exportar Respostas (Word / TXT)"):
    st.markdown("Baixe o relatório completo com todas as respostas das equipes enviadas durante a partida:")
    
    # Montagem do arquivo texto/word
    conteudo_doc = "====================================================\n"
    conteudo_doc += "RELATÓRIO DE RESPOSTAS DAS EQUIPES - CDZ COSMOLOGIA\n"
    conteudo_doc += "====================================================\n\n"
    
    if st.session_state.historico_respostas:
        for item in st.session_state.historico_respostas:
            conteudo_doc += f"RODADA {item['rodada']} | EQUIPE: {item['equipe']}\n"
            conteudo_doc += f"Guia: {item['guia']}\n"
            conteudo_doc += f"Questão: {item['enunciado']}\n"
            conteudo_doc += f"Resposta Enviada: {item['resposta']}\n"
            conteudo_doc += f"Resultado: {item['status']}\n"
            conteudo_doc += f"Explicação do Porquê: {item['porque']}\n"
            conteudo_doc += "----------------------------------------------------\n"
    else:
        conteudo_doc += "Nenhuma resposta registrada até o momento.\n"
        
    st.download_button(
        label="📥 Baixar Relatório (.doc / Word)",
        data=conteudo_doc,
        file_name="relatorio_respostas_equipes.doc",
        mime="application/msword"
    )
    
    st.download_button(
        label="📥 Baixar Relatório (.txt / Texto)",
        data=conteudo_doc,
        file_name="relatorio_respostas_equipes.txt",
        mime="text/plain"
    )

with st.sidebar.expander("🛠️ Histórico do Jogo"):
    if st.session_state.historico_respostas:
        for h in st.session_state.historico_respostas:
            st.text(f"[R{h['rodada']} - {h['equipe']}] {h['status']}")
        if st.button("🗑️ Limpar Histórico"):
            st.session_state.historico_respostas = []
            st.rerun()
    else:
        st.info("Nenhuma resposta enviada ainda.")

# Placar
st.sidebar.header("📊 Placar Geral")
st.sidebar.metric(label="🛡️ Equipe Alfa", value=st.session_state.pontos_alfa)
st.sidebar.metric(label="🛡️ Equipe Beta", value=st.session_state.pontos_beta)
st.sidebar.metric(label="🛡️ Equipe Gama", value=st.session_state.pontos_gama)
st.sidebar.metric(label="⚡ Estabilidade do Cosmo", value=f"{st.session_state.estabilidade}%")

# ==========================================
# INÍCIO DO JOGO
# ==========================================
if not st.session_state.jogo_iniciado:
    st.subheader("🎲 Sorteio e Início das Batalhas do Santuário")
    st.markdown("Cada pergunta será apresentada **individualmente para cada equipe**, uma por uma em suas respectivas rodadas.")
    
    if st.button("Iniciar Batalha do Conhecimento"):
        st.session_state.jogo_iniciado = True
        st.rerun()
    st.stop()

# ==========================================
# CONTROLE DE RODADAS E PERGUNTAS SEPARADAS
# ==========================================
total_rodadas = len(st.session_state.banco_rodadas)
r_idx = st.session_state.rodada_atual - 1
e_idx = st.session_state.equipe_sub_idx

if r_idx < total_rodadas:
    rodada_data = st.session_state.banco_rodadas[r_idx]
    q_atual = rodada_data["questoes"][e_idx]
    
    st.subheader(f"⚔️ **RODADA {st.session_state.rodada_atual}** | Vez de: **{q_atual['equipe']}**")
    st.markdown(f"**Guia da Casa:** *{q_atual['guia']}*")
    st.markdown("---")
    
    st.markdown(f"### **Desafio:** {q_atual['enunciado']}")
    
    # Exibe caixa de entrada dependendo do tipo da pergunta
    if q_atual['tipo'] == 'multipla':
        resposta_dada = st.radio("Selecione a opção correta:", q_atual['opcoes'], key=f"q_{r_idx}_{e_idx}")
    else:
        resposta_dada = st.text_area("✍️ Escreva a resposta da equipe:", key=f"q_{r_idx}_{e_idx}")

    if st.button("Submeter Resposta da Equipe"):
        status_resposta = ""
        acertou = False
        
        # Correção da resposta
        if q_atual['tipo'] == 'multipla':
            letra = resposta_dada.split(")")[0].strip()
            if letra == q_atual['correta']:
                acertou = True
                status_resposta = "CORRETA"
            else:
                status_resposta = "INCORRETA"
        else:
            texto_l = resposta_dada.lower()
            acertos = sum(1 for p in q_atual['palavras_chave'] if p in texto_l)
            if len(resposta_dada.strip()) > 5 and acertos >= 2:
                acertou = True
                status_resposta = "CORRETA"
            else:
                status_resposta = "INCORRETA"

        # Pontuação
        if acertou:
            if q_atual['equipe'] == "Equipe Alfa": st.session_state.pontos_alfa += 25
            elif q_atual['equipe'] == "Equipe Beta": st.session_state.pontos_beta += 25
            else: st.session_state.pontos_gama += 25
        else:
            st.session_state.estabilidade -= 8

        # Registra no histórico do organizador
        st.session_state.historico_respostas.append({
            "rodada": st.session_state.rodada_atual,
            "equipe": q_atual['equipe'],
            "guia": q_atual['guia'],
            "enunciado": q_atual['enunciado'],
            "resposta": resposta_dada,
            "status": status_resposta,
            "porque": q_atual['porque']
        })

        # Define mensagem de feedback com o "Porquê"
        st.session_state.mensagem_feedback = {
            "status": status_resposta,
            "porque": q_atual['porque'],
            "equipe": q_atual['equipe']
        }

        # Avança a sub-equipe (0 -> 1 -> 2) ou avança a rodada
        if e_idx < 2:
            st.session_state.equipe_sub_idx += 1
        else:
            st.session_state.equipe_sub_idx = 0
            st.session_state.rodada_atual += 1
            
        st.rerun()

    # Exibe o feedback e o "porquê" da última pergunta respondida
    if st.session_state.mensagem_feedback:
        st.markdown("---")
        fb = st.session_state.mensagem_feedback
        if fb['status'] == "CORRETA":
            st.success(f"🎉 Resposta da **{fb['equipe']}** foi **CORRETA**!")
        else:
            st.error(f"❌ Resposta da **{fb['equipe']}** foi **INCORRETA**.")
            
        st.info(f"💡 **O PORQUÊ DA RESPOSTA:**\n\n{fb['porque']}")

else:
    # FASE FINAL DO JOGO
    st.balloons()
    st.subheader("🏛️ Chegada ao Templo de Athena!")
    st.markdown("""
    > Todas as perguntas individuais foram concluídas! 
    > Os Cavaleiros guiaram as equipes com sabedoria, revelando a física por trás do cosmos!
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

    st.markdown("---")
    st.info("💡 **Dica para o Organizador:** Abra a barra lateral para baixar o relatório final com todas as respostas em arquivo Word (`.doc`) ou Texto (`.txt`).")

    if st.button("🔄 Reiniciar Nova Batalha"):
        st.session_state.jogo_iniciado = False
        st.session_state.rodada_atual = 1
        st.session_state.equipe_sub_idx = 0
        st.session_state.pontos_alfa = 0
        st.session_state.pontos_beta = 0
        st.session_state.pontos_gama = 0
        st.session_state.estabilidade = 100
        st.session_state.mensagem_feedback = None
        st.rerun()


