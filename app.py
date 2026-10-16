import streamlit as st

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Astronomia para Crianças",
    page_icon="🚀",
    layout="centered"
)

# Estilização visual amigável e limpa
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

st.title("🚀 Astronomia para Crianças 🌌")
st.markdown("### Digite qualquer dúvida sobre o espaço para ver explicações mágicas e corretas!")

# ==========================================================
# 2. BANCO DE CONHECIMENTO GIGANTE (LISTA COMPLETA)
# ==========================================================
BASE_CONHECIMENTO = {
    "mercúrio": (
        "Mercúrio é o planeta mais próximo do Sol e o menorzinho de todos. "
        "Como ele fica bem colado ao Sol, o lado virado para a luz é tããão quente que derreteria metais, "
        "enquanto o lado escuro é super congelante! Ele é rochoso e cheio de crateras."
    ),
    "vênus": (
        "Vênus é o segundo planeta e brilha tanto no céu que muita gente acha que é uma estrela. "
        "Apesar de não ser o mais perto do Sol, ele é o planeta mais quente de todos! "
        "Isso acontece porque suas nuvens grossas prendem o calor em um efeito estufa gigante."
    ),
    "terra": (
        "A Terra é a nossa linda nave espacial azul, o único lugar do universo onde sabemos com certeza que existe vida, "
        "água líquida e ar fresquinho. Ela gira ao redor do Sol criando os dias e as noites."
    ),
    "marte": (
        "Marte é o planeta vermelho porque o seu chão é coberto por uma poeira cheia de ferro enferrujado. "
        "Ele tem vulcões gigantes e os cientistas mandam robôs chamados rovers para lá para procurar pistas de rios antigos."
    ),
    "júpiter": (
        "Júpiter é o grandão da turma, o maior planeta do Sistema Solar, feito inteiramente de gases. "
        "A sua famosa Mancha Vermelha é uma tempestade gigante, maior que a Terra, que gira há séculos!"
    ),
    "saturno": (
        "Saturno é o planeta dos anéis brilhantes, formados por bilhões de pedacinhos de gelo e rocha. "
        "Ele é tão leve que, se existisse uma banheira gigante com água no espaço, ele flutuaria como uma boia!"
    ),
    "urano": (
        "Urano é um gigante de gelo azul-esverdeado que tem uma mania bem maluca: ele gira completamente deitado de lado, "
        "como se estivesse rolando no espaço como uma bola de gude!"
    ),
    "netuno": (
        "Netuno é um mundo azul, gelado e muito distante, onde sopram os ventos mais rápidos de todo o Sistema Solar. "
        "Por estar tãão longe do Sol, lá parece sempre o fim de tarde de um dia nublado."
    ),
    "sol": (
        "O Sol é a estrela gigante e superquente no centro do nosso sistema. "
        "Ele funciona como uma fogueira mágica que nunca apaga, dando luz, calor e segurando todos os planetas com sua gravidade."
    ),
    "lua": (
        "A Lua é a companheira fiel da Terra. Ela brilha à noite refletindo a luz do Sol e ajuda a controlar as marés dos oceanos. "
        "Como não tem vento, as pegadas dos astronautas lá vão durar para sempre!"
    ),
    "buraco negro": (
        "Um buraco negro é uma região do espaço com uma gravidade monstruosa! É tão forte que nem a luz consegue escapar se chegar perto. "
        "Mas calma: eles não saem sugando tudo como aspiradores de pó; ficam bem quietinhos no espaço."
    ),
    "matéria escura": (
        "A matéria escura é como um esqueleto invisível do cosmos. Não conseguimos vê-la porque ela não emite luz, "
        "mas sabemos que ela existe porque sua gravidade gigante age como uma cola, impedindo que as galáxias se desmanchem."
    ),
    "energia escura": (
        "A energia escura é uma força misteriosa que faz o oposto da gravidade: ela empurra o universo para fora, "
        "fazendo com que ele se espalhe e cresça cada vez mais rápido, como um balão inflando."
    ),
    "big bang": (
        "O Big Bang não foi uma explosão comum no espaço, mas sim a expansão repentina do próprio espaço a partir de um ponto "
        "minúsculo e superquente, há 13,8 bilhões de anos, dando início ao tempo e ao universo."
    ),
    "inflação cósmica": (
        "A inflação cósmica foi um crescimento relâmpago que aconteceu em uma fração minúscula de segundo logo no comecinho do Big Bang, "
        "esticando o espaço a uma velocidade muito maior que a da luz."
    ),
    "teoria de tudo": (
        "A teoria de tudo é o grande sonho dos físicos de criar uma única equação perfeita que una a gravidade dos planetas "
        "com as regras invisíveis dos átomos."
    ),
    "mecânica quântica": (
        "A mecânica quântica é a ciência que estuda o mundo microscópico dos átomos. Lá, as partículas fazem coisas mágicas: "
        "podem estar em vários lugares ao mesmo tempo e agir como ondas de luz!"
    ),
    "cometas": (
        "Cometas são como bolas de neve cósmicas feitas de gelo, poeira e rocha. Quando passam perto do Sol, o gelo derrete e "
        "cria uma cauda brilhante espetacular no céu."
    ),
    "meteoro": (
        "Um meteoro é o famoso 'estrela cadente'! É um pedacinho de rocha espacial que entra na atmosfera da Terra correndo tanto "
        "que pega fogo e brilha no céu."
    ),
    "asteróide": (
        "Asteroides são grandes pedaços de rocha e metal que sobraram da formação do Sistema Solar e viajam pelo espaço, "
        "muitos deles morando em um cinturão entre Marte e Júpiter."
    ),
    "estrelas": (
        "As estrelas são fornalhas gigantes de gás que produzem sua própria luz e calor através da fusão nuclear em seus centros, "
        "brilhando por bilhões de anos."
    ),
    "supernova": (
        "Uma supernova é a explosão espetacular de uma estrela gigante no fim da vida, brilhando mais do que galáxias inteiras "
        "e espalhando poeira estelar pelo universo."
    ),
    "via láctea": (
        "A Via Láctea é a nossa galáxia! É uma cidade gigante com bilhões de estrelas em formato de espiral, e o nosso Sistema Solar "
        "fica em um dos seus braços."
    )
}

# ==========================================================
# 3. CAMPO DE PESQUISA E BUSCA INTELIGENTE
# ==========================================================
pergunta = st.text_input(
    "O que você quer descobrir no universo hoje?",
    placeholder="Ex: Mercúrio, Júpiter, Buraco negro, Matéria escura, Big Bang, Cometas..."
)

if st.button("🌟 Decolar Pesquisa Cósmica!", type="primary"):
    if pergunta.strip() != "":
        pergunta_lower = pergunta.lower()
        encontrou = False
        
        # Procura se alguma palavra-chave da base está na pergunta
        for chave, texto in BASE_CONHECIMENTO.items():
            if chave in pergunta_lower:
                st.markdown(f"### 🔭 Resposta sobre **{chave.capitalize()}**:")
                st.markdown(f'<div class="resposta-box">{texto}</div>', unsafe_allow_html=True)
                encontrou = True
                break
        
        # Se não achar exatamente na lista, exibe uma resposta padrão carinhosa
        if not encontrou:
            resposta_padrao = (
                f"🌟 Que pergunta maravilhosa sobre '{pergunta}'! No universo, tudo está conectado por leis mágicas "
                "como a gravidade, a luz e o movimento das estrelas.\n\n"
                "Continue sempre com essa curiosidade gigante, pois os cientistas passam a vida inteira estudando "
                "novos mistérios do espaço exatamente como você está fazendo agora!"
            )
            st.markdown("### 🔭 Resposta do Explorador Espacial:")
            st.markdown(f'<div class="resposta-box">{resposta_padrao}</div>', unsafe_allow_html=True)
            
    else:
        st.warning("⚠️ Digite um tema ou pergunta na caixa acima para o foguete poder decolar!")

# Rodapé
st.markdown("---")
st.markdown("💡 **Dica para sua Live / OBS:** Adicione uma fonte de **Captura de Janela** no seu OBS selecionando esta aba do navegador. Vai rodar perfeito!")
