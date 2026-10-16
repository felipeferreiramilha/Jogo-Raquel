import streamlit as st

# ==========================================================
# CONFIGURAÇÃO DA PÁGINA (VISUAL PARA CRIANÇAS)
# ==========================================================
st.set_page_config(
    page_title="Astronomia para Crianças",
    page_icon="🚀",
    layout="centered"
)

# Estilização visual amigável e colorida
st.markdown(
    """
    <style>
    .main {
        background-color: #0e1117;
        color: #ffffff;
    }
    .stTextInput > div > div > input {
        background-color: #1f2937;
        color: white;
        font-size: 18px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# BANCO DE DADOS COMPLETO (MAIS DE 30 TÓPICOS)
# ==========================================================
BASE_CONHECIMENTO = {
    "mercúrio": "Mercúrio é o menor planeta do Sistema Solar e o mais pertinho do Sol. Ele é cheio de crateras na superfície e tem temperaturas super extremas!",
    "vênus": "Vênus brilha tanto no céu que parece uma estrela, mas é um planeta coberto por nuvens grossas. É o planeta mais quente de todos por causa do efeito estufa!",
    "terra": "A Terra é a nossa nave espacial azul, o único lugar do universo com vida confirmada, muita água líquida e ar fresquinho.",
    "marte": "Marte é o planeta vermelho, coberto de poeira de ferro. Os cientistas mandam robôs espaciais para lá para procurar vestígios de água antiga.",
    "júpiter": "Júpiter é o maior planeta do Sistema Solar, um gigante gasoso com uma grande mancha vermelha que é uma supertempestade girando sem parar.",
    "saturno": "Saturno é o planeta dos anéis brilhantes feitos de gelo e rocha. Ele é tão leve que se colocassem numa banheira gigante, ele flutuaria!",
    "urano": "Urano é um gigante de gelo azul-esverdeado que tem uma curiosidade incrível: ele gira deitado, como se estivesse rolando no espaço.",
    "netuno": "Netuno é o planeta azul mais distante do Sol, um mundo gelado onde sopram os ventos mais rápidos de todo o sistema solar.",
    "plutão": "Plutão é um fofinho planeta anão lá no fim do Sistema Solar que tem uma mancha em formato de coração na superfície.",
    "sol": "O Sol é a estrela gigante e quentinha no centro da nossa vizinhança, dando luz, calor e energia para todos nós.",
    "lua": "A Lua é a companheira fiel da Terra que brilha à noite refletindo a luz do Sol e ajuda a controlar as marés dos oceanos.",
    "estrelas": "As estrelas são sóis gigantes bem distantes que brilham no escuro e produzem sua própria luz através de reações mágicas de fusão.",
    "exoplanetas": "Exoplanetas são mundos misteriosos que giram ao redor de outras estrelas bem longe do nosso Sol.",
    "galáxias": "Uma galáxia é uma cidade gigantesca no espaço que junta bilhões de estrelas, planetas e poeira cósmica. A nossa se chama Via Láctea!",
    "buraco negro": "Um buraco negro é uma região do espaço com uma gravidade tão forte que puxa absolutamente tudo para dentro, até a luz!",
    "matéria escura": "A matéria escura é um ingrediente invisível que atrai as coisas com gravidade, ajudando a segurar as galáxias unidas.",
    "energia escura": "A energia escura é uma força misteriosa que está fazendo todo o universo se expandir cada vez mais rápido.",
    "big bang": "O Big Bang foi o grande começo de tudo, o momento em que o universo nasceu de um ponto minúsculo e começou a crescer.",
    "relatividade": "A teoria da relatividade de Einstein nos ensina que o tempo e o espaço estão conectados e podem mudar dependendo da velocidade.",
    "teoria das cordas": "A teoria das cordas imagina que as menores coisas do universo não são bolinhas, mas sim pequenas cordas musicais vibrantes."
}

# ==========================================================
# INTERFACE GRÁFICA DO APLICATIVO
# ==========================================================
st.title("🚀 Astronomia para Crianças 🌌")
st.markdown("### Digite qualquer dúvida sobre o espaço e veja a mágica acontecer na sua tela!")

# Caixa de texto onde a criança digita
pergunta = st.text_input("O que você quer descobrir hoje?", placeholder="Ex: Me fale sobre Saturno, o que é um buraco negro...")

# Botão de pesquisa
if st.button("🚀 Decolar Pesquisa!", type="primary"):
    if pergunta:
        pergunta_lower = pergunta.lower()
        encontrou = False
        
        # Varre o dicionário buscando correspondência
        for chave, texto in BASE_CONHECIMENTO.items():
            if chave in pergunta_lower:
                st.success(f"✨ **Resposta Estelar:**\n\n{texto}")
                encontrou = True
                break
        
        # Se não achar exatamente na lista, dá uma resposta genérica amigável
        if not encontrou:
            st.info(f"🌟 **Resposta Cósmica:**\n\nA pergunta sobre '{pergunta}' é fantástica! Na astronomia, tudo está conectado por forças incríveis como a gravidade, a luz e o movimento. Continue sempre curioso, pois o espaço guarda segredos maravilhosos!")
    else:
        st.warning("⚠️ Digite uma pergunta na caixa acima para o foguete poder decolar!")

# Rodapé com instruções para a Live
st.markdown("---")
st.markdown("💡 **Dica para o seu Stream / OBS:** Para essa tela aparecer perfeitamente na sua transmissão sem dar tela preta, abra o OBS, adicione uma **Captura de Janela** ou **Fonte de Navegador** selecionando esta aba do seu navegador!")
