import streamlit as st

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="O Universo Maluco das Crianças",
    page_icon="🚀",
    layout="centered"
)

# Estilização visual futurista e divertida
st.markdown(
    """
    <style>
    .main {
        background-color: #0b0f19;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #161b22;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        border: 1px solid #30363d;
    }
    .resposta-box {
        background-color: #161b22;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #30363d;
        margin-top: 20px;
        font-size: 16px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🚀 O Universo Maluco das Crianças 🌌")
st.markdown("### Digite qualquer pergunta maluca sobre o espaço, multiverso, alienígenas ou viagens no tempo!")

# ==========================================================
# 2. BANCO DE CONHECIMENTO (TEORIAS MALUCAS E PERGUNTAS DE CRIANÇA)
# ==========================================================
BASE_CONHECIMENTO = {
    # VIAGEM NO TEMPO E PARADOXOS
    "viagem no tempo": (
        "Viajar para o futuro a ciência diz que é possível se você andar muito rápido numa nave espacial! "
        "Mas para o passado... os cientistas acham que é proibido pelas regras da física, para não criar confusão com o avô!"
    ),
    "passado": (
        "Voltar no tempo para ver os dinossauros é o sonho de todo mundo! Mas a física acha que isso é bem difícil "
        "porque o tempo só anda para a frente, como um rio que nunca corre para trás."
    ),
    "paradoxo": (
        "Imagine que você volta no tempo e esbarra sem querer nos seus avós antes de eles se conhecerem. "
        "Se eles não se casarem, você existiria para voltar no tempo? É por isso que o universo parece proibir viagens ao passado!"
    ),

    # MULTIVERSO E UNIVERSOS PARALELOS
    "multiverso": (
        "O multiverso é a ideia maluca de que o nosso universo não está sozinho. "
        "Podem existir infinitos outros universos paralelos lá fora, alguns parecidos com o nosso e outros totalmente esquisitos!"
    ),
    "outro universo": (
        "Será que em outro universo existe uma versão sua que come pizza de chocolate no café da manhã? "
        "Na teoria dos universos paralelos, tudo o que poderia acontecer de jeito diferente aconteceu em outro lugar!"
    ),
    "clones": (
        "Não são clones exatos como robôs, mas a teoria do multiverso diz que, com infinitos universos espalhados por aí, "
        "poderia existir alguém muito parecido com você em outro canto do cosmos!"
    ),

    # BURACOS DE MINHOCA E ATALHOS
    "buraco de minhoca": (
        "Um buraco de minhoca é como um túnel secreto ou um atalho mágico no espaço. "
        "Na ficção, as naves entram nele de um lado e saem na outra ponta da galáxia em um piscar de olhos!"
    ),
    "atalho": (
        "Se o universo é uma folha de papel gigante, um buraco de minhoca seria como dobrar a folha e enfiar um lápis de um lado ao outro "
        "para viajar rápido sem precisar atravessar todo o papel!"
    ),

    # ALIENÍGENAS E ETs
    "alienígenas": (
        "Os cientistas ainda não encontraram ETs de verdade, mas como o universo é gigantesco e tem trilhões de estrelas, "
        "muita gente acha que deve existir algum tipo de vidinha espalhada por aí!"
    ),
    "et": (
        "Procurar ETs é como pescar em um oceano infinito. Por enquanto só achamos peixinhos virtuais, mas a busca continua!"
    ),
    "civilização": (
        "Cientistas imaginam civilizações superavançadas que conseguem construir estruturas gigantescas ao redor de sóis inteiros "
        "para capturar toda a energia das estrelas!"
    ),

    # PLANETAS MALUCOS E EXÓTICOS
    "diamante": (
        "Sim! No planeta 55 Cancri e, e também nas tempestades de Júpiter e Saturno, a pressão é tão gigante "
        "que transforma carbono em verdadeiras pedras de diamante brilhantes caindo do céu!"
    ),
    "chuva de vidro": (
        "No planeta HD 189733b, venta a impressionantes 8 mil quilômetros por hora e chove vidro derretido... mas de lado! "
        "Um lugar bem pouco recomendável para um piquenique."
    ),
    "dois sóis": (
        "Existem exoplanetas no universo que têm dois ou três sóis no céu ao mesmo tempo, igualzinho ao planeta Tatooine do filme Star Wars!"
    ),
    "invisivel": (
        "Existe um planeta chamado TrES-2b que é mais negro que carvão: ele absorve quase 99% de toda a luz que bate nele, "
        "sendo o mundo mais escuro já descoberto."
    ),

    # SIMULAÇÃO E COMPUTADOR
    "simulação": (
        "Algumas pessoas muito inteligentes, como cientistas e criadores de tecnologia, brincam dizendo que o nosso universo "
        "poderia ser um jogo de computador gigante criado por uma civilização superinteligente do futuro."
    ),
    "jogo": (
        "Se o universo fosse um jogo de videogame cósmico, as leis da física seriam as regras de programação, "
        "e a velocidade da luz seria o limite de velocidade que o processador aguenta rodar!"
    ),

    # FIM DO MUNDO E CENÁRIOS LOUCOS
    "fim do mundo": (
        "O fim do universo vai demorar trilhões de anos! Os cientistas acham que as estrelas vão apagando uma por uma "
        "até tudo ficar escuro e congelado, num evento chamado Grande Congelação."
    ),
    "rasgar": (
        "Outra teoria maluca é o 'Grande Rasgo', onde a energia escura empurra tudo com tanta força no futuro distante "
        "que até os átomos do universo se desmancham!"
    ),

    # BURACOS NEGROS E ESPAGUETE
    "buraco negro": (
        "Um buraco negro tem uma gravidade tão forte que nem a luz escapa. Se você chegasse perto demais, "
        "ela puxaria seus pés com mais força que sua cabeça, esticando você igualzinho a um fio de espaguete!"
    ),
    "buraco branco": (
        "O buraco branco é o oposto do buraco negro: na teoria, em vez de puxar tudo, ele cuspiria matéria e luz sem parar. "
        "Mas ele é só uma ideia no papel; ninguém nunca viu um de verdade!"
    ),

    # PERGUNTAS "E SE...?"
    "terra parar": (
        "Se a Terra parasse de girar de uma vez só, tudo o que não estivesse preso ao chão continuaria voando em alta velocidade "
        "por causa da inércia. Seria uma grande bagunça cósmica!"
    ),
    "duas luas": (
        "Se tivéssemos duas luas no céu, as marés dos oceanos seriam gigantescas e as nossas noites seriam tããão claras "
        "que pareceria quase dia!"
    ),
    "gritar no espaço": (
        "No espaço não dá para ouvir ninguém gritar porque o som precisa de ar para viajar, e lá fora é um vácuo sem som nenhum!"
    ),
}

# ==========================================================
# 3. CAMPO DE PESQUISA E BUSCA INTELIGENTE
# ==========================================================
pergunta = st.text_input(
    "O que você quer descobrir no universo hoje?",
    placeholder="Ex: Viagem no tempo, Multiverso, Chuva de diamante, Simulação, ETs..."
)

if st.button("🌟 Decolar Pesquisa Cósmica!", type="primary"):
    if pergunta.strip() != "":
        pergunta_lower = pergunta.lower()
        encontrou = False
        
        # Procura por palavras-chave na base de conhecimento
        for chave, texto in BASE_CONHECIMENTO.items():
            if chave in pergunta_lower or any(p in pergunta_lower for p in chave.split()):
                st.markdown(f"### 🔭 Resposta Mágica:")
                st.markdown(f'<div class="resposta-box">{texto}</div>', unsafe_allow_html=True)
                encontrou = True
                break
        
        # Se não achar exatamente na lista, exibe uma resposta animada para crianças
        if not encontrou:
            resposta_padrao = (
                f"🌟 Uau, que pergunta super criativa sobre '{pergunta}'! No universo das crianças curiosas, "
                "tudo é possível de imaginar.\n\n"
                "Os cientistas adoram pensar em teorias malucas como essa. Continue com essa imaginação gigante "
                "porque você pensa igualzinho a um verdadeiro cientista espacial!"
            )
            st.markdown(f"### 🔭 Resposta Mágica:")
            st.markdown(f'<div class="resposta-box">{resposta_padrao}</div>', unsafe_allow_html=True)
            
    else:
        st.warning("⚠️ Digite uma pergunta maluca na caixa acima para o foguete poder decolar!")

# Rodapé
st.markdown("---")
st.markdown("💡 **Dica para sua Live / OBS:** Adicione uma fonte de **Captura de Janela** no seu OBS selecionando esta aba do navegador. Vai rodar perfeito!")
