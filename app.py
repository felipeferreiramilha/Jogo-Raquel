import streamlit as st

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Super Enciclopédia Cósmica",
    page_icon="🚀",
    layout="centered"
)

# Estilização visual futurista, limpa e perfeita para Lives / OBS
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

st.title("🚀 Super Enciclopédia Cósmica das Crianças 🌌")
st.markdown("### Digite qualquer dúvida sobre buracos negros, estrelas, multiverso, física maluca e planetas do espaço!")

# ==========================================================
# 2. BANCO DE CONHECIMENTO VASTO E COMPLETO
# ==========================================================
BASE_CONHECIMENTO = {
    # BURACOS NEGROS E MISTÉRIOS EXTREMOS
    "buraco negro": (
        "Um buraco negro é uma região do espaço onde a matéria ficou espremida de um jeito tão apertado que gerou uma gravidade monstruosa! "
        "Essa gravidade é tão forte que nem mesmo a luz consegue escapar se chegar perto demais.\n\n"
        "Mas calma: eles não ficam sugando as coisas como aspiradores de pó gigantes. Eles ficam bem distantes e ajudam os cientistas "
        "a entenderem as regras mais profundas de como o universo funciona."
    ),
    "horizonte de eventos": (
        "O Horizonte de Eventos é o 'ponto sem retorno' ao redor de um buraco negro. "
        "Se você cruzar essa linha invisível, nem a luz e nem a nave mais rápida do universo conseguem voltar para trás!"
    ),
    "singularidade": (
        "A singularidade é o centro exato de um buraco negro. Lá, toda a matéria do mundo está espremida em um ponto "
        "com tamanho zero e densidade infinita, onde as regras da física que conhecemos simplesmente param de funcionar!"
    ),
    "espaguete": (
        "Se você caísse em um buraco negro, a gravidade puxaria seus pés com muito mais força do que a sua cabeça, "
        "fazendo você ser esticado igualzinho a um fio de macarrão espaguete! Na ciência, chamamos isso de espaguetificação."
    ),
    "tempo devagar": (
        "Sim! Perto de um buraco negro, a gravidade é tão extrema que o tempo passa muito mais devagar para você do que para quem está longe. "
        "Se você passasse um tempinho lá perto e voltasse para a Terra, seus amigos estariam muito mais velhos que você!"
    ),
    "buraco branco": (
        "O buraco branco é o oposto do buraco negro: na teoria da física, em vez de atrair tudo, ele cuspiria matéria e luz sem parar. "
        "Mas ele é só uma ideia no papel; ninguém nunca encontrou um de verdade!"
    ),
    "sol virar buraco negro": (
        "O Sol nunca vai virar um buraco negro porque ele não tem massa suficiente para isso! "
        "Ele vai terminar sua vida de bilhões de anos bem calmamente como uma estrela anã branca."
    ),
    "buraco de minhoca": (
        "Um buraco de minhoca é como um túnel secreto ou um atalho no espaço. Na ficção científica, as naves entram nele "
        "e saem na outra ponta do universo em um piscar de olhos!"
    ),

    # VIAGEM NO TEMPO E FÍSICA RELATIVISTA
    "viagem no tempo": (
        "Viajar para o futuro a ciência diz que é totalmente possível se você voar numa nave super-rápida! "
        "Mas viajar para o passado é bem mais complicado, pois o tempo só anda para a frente, como um rio."
    ),
    "paradoxo do avô": (
        "Imagine que você volta no tempo e impede seus avós de se conhecerem. Se eles não se casarem, você nunca nasce para voltar no tempo! "
        "É por causa desse nó na cabeça que a física acha que o passado não pode ser mudado."
    ),
    "relatividade": (
        "Einstein descobriu que o espaço e o tempo formam um tecido elástico. Quando coisas pesadas como planetas se apoiam nele, "
        "o tecido entorta, criando aquilo que chamamos de gravidade."
    ),

    # MULTIVERSO E TEORIAS MIRABOLANTES
    "multiverso": (
        "O multiverso é a ideia fascinante de que o nosso universo não está sozinho. "
        "Podem existir infinitos outros universos paralelos lá fora, cada um com regras e mundos diferentes!"
    ),
    "outro universo": (
        "Se o multiverso for real, pode existir um universo onde os dinossauros nunca foram extintos "
        "e outro onde você come pizza de chocolate todos os dias!"
    ),
    "simulação": (
        "Alguns cientistas brincam com a teoria de que o nosso universo inteiro poderia ser um jogo de computador gigante "
        "criado por uma civilização superinteligente do futuro."
    ),

    # PLANETAS EXÓTICOS E LOUCURAS CÓSMICAS
    "diamante": (
        "Sim! Nas profundezas e tempestades de Júpiter e Saturno, a pressão é tão gigante que esmaga o gás e "
        "cria verdadeiras chuvas de pedras de diamante brilhantes!"
    ),
    "chuva de vidro": (
        "No planeta exótico HD 189733b, venta a impressionantes 8 mil quilômetros por hora e chove vidro derretido... mas de lado! "
        "Um lugar bem perigoso para passear."
    ),
    "dois sóis": (
        "Existem planetas no espaço que têm dois ou três sóis no céu ao mesmo tempo, igualzinho ao planeta Tatooine do filme Star Wars!"
    ),
    "planeta negro": (
        "Existe um mundo chamado TrES-2b que é mais escuro que carvão: ele absorve 99% de toda a luz que bate nele, "
        "sendo o planeta mais escuro já encontrado."
    ),

    # O SISTEMA SOLAR (PLANETAS E LUA)
    "mercúrio": (
        "Mercúrio é o menorzinho e mais perto do Sol. O lado virado para a luz ferve a metais, "
        "enquanto o lado da sombra congela. E o céu dele é totalmente preto!"
    ),
    "vênus": (
        "Vênus é o planeta mais quente de todos por causa de seu efeito estufa gigante, "
        "e ele gira ao contrário dos outros, fazendo o sol nascer no oeste!"
    ),
    "terra": (
        "A Terra é a nossa nave espacial azul, o único lugar do universo com água líquida em abundância "
        "e vida pulando por todos os lados."
    ),
    "marte": (
        "Marte é o planeta vermelho por causa da ferrugem no chão. Ele tem o Monte Olimpo, "
        "o maior vulcão de todo o Sistema Solar."
    ),
    "júpiter": (
        "Júpiter é o grandão gasoso do grupo. Sua Grande Mancha Vermelha é uma tempestade maior que a Terra "
        "que gira sem parar há centenas de anos."
    ),
    "saturno": (
        "Saturno usa anéis fabulosos feitos de bilhões de pedacinhos de gelo. "
        "Ele é tão leve que flutuaria em uma banheira gigante de água!"
    ),
    "urano": (
        "Urano é um gigante de gelo azul que tem a mania maluca de girar completamente deitado de lado, "
        "como uma bola rolando no espaço."
    ),
    "netuno": (
        "Netuno é um mundo azul e gelado onde sopram os ventos mais violentos e rápidos de todo o Sistema Solar."
    ),
    "sol": (
        "O Sol é a estrela fogueira no centro da nossa vizinhança, gerando energia mágica através da fusão nuclear."
    ),
    "lua": (
        "A Lua é a companheira da Terra que controla as marés e guarda pegadas de astronautas que durarão para sempre."
    ),

    # ESTRELAS E FENÔMENOS
    "estrelas": (
        "As estrelas são fornalhas gigantes de gás que produzem sua própria luz e calor através da fusão nuclear em seus centros, "
        "brilhando por bilhões de anos."
    ),
    "supernova": (
        "Uma supernova é a explosão colossal de uma estrela no fim da vida, brilhando mais que galáxias inteiras."
    ),
    "estrela de nêutrons": (
        "Estrelas de nêutrons são tão apertadas e densas que uma colherzinha delas pesaria bilhões de toneladas na Terra!"
    ),
    "pulsar": (
        "Um pulsar é uma estrela de nêutrons que gira velozmente emitindo feixes de luz como um farol cósmico."
    ),
    "nebulosas": (
        "Nebulosas são berçários gigantescos de gás e poeira onde novas estrelas nascem."
    ),

    # BIG BANG E ORIGEM
    "big bang": (
        "O Big Bang não foi uma explosão comum no espaço, mas sim a expansão rápida do próprio espaço a partir de um ponto minúsculo, "
        "quente e denso, há 13,8 bilhões de anos, dando início ao tempo."
    ),
    "inflação cósmica": (
        "Foi um estiramento relâmpago do espaço em uma fração microscópica de segundo logo no início do Big Bang."
    ),
    "matéria escura": (
        "É um esqueleto invisível que usa sua gravidade gigante para segurar as galáxias unidas sem emitir luz."
    ),
    "energia escura": (
        "É a força misteriosa que empurra o universo para fora, fazendo-o se expandir cada vez mais rápido."
    ),

    # VIDA E EXTRATERRESTRES
    "alienígenas": (
        "Ainda não encontramos ETs, mas como o universo é gigantesco e tem trilhões de estrelas, "
        "muitos cientistas acham que a vida pode existir em outros lugares!"
    ),
    "zona habitável": (
        "É a faixa perfeita ao redor de uma estrela onde a temperatura permite a existência de água líquida."
    ),

    # CURIOSIDADES "E SE...?"
    "terra parar": (
        "Se a Terra parasse de girar de uma vez, tudo o que estivesse solto voaria em alta velocidade por causa da inércia!"
    ),
    "duas luas": (
        "Com duas luas no céu, teríamos marés gigantes e noites bem mais brilhantes."
    ),
    "gritar no espaço": (
        "Ninguém ouviria seu grito no espaço porque o vácuo não tem ar para o som se propagar."
    ),
}

# ==========================================================
# 3. CAMPO DE PESQUISA E BUSCA INTELIGENTE
# ==========================================================
pergunta = st.text_input(
    "O que você quer descobrir no universo hoje?",
    placeholder="Ex: Buraco negro, Singularidade, Espaguete, Viagem no tempo, Multiverso, Chuva de diamante..."
)

if st.button("🌟 Decolar Pesquisa Cósmica!", type="primary"):
    if pergunta.strip() != "":
        pergunta_lower = pergunta.lower()
        encontrou = False
        
        # Procura por correspondências no banco vasto
        for chave, texto in BASE_CONHECIMENTO.items():
            if chave in pergunta_lower or any(p in pergunta_lower for p in chave.split()):
                st.markdown(f"### 🔭 Resposta sobre **{chave.capitalize()}**:")
                st.markdown(f'<div class="resposta-box">{texto}</div>', unsafe_allow_html=True)
                encontrou = True
                break
        
        # Resposta padrão mágica caso o tema não esteja cadastrado
        if not encontrou:
            resposta_padrao = (
                f"🌟 Que pergunta fascinante sobre '{pergunta}'! No vasto oceano do universo, "
                "existem mistérios incríveis esperando para serem desvendados.\n\n"
                "Continue sempre com essa curiosidade gigante, pois os maiores cientistas do mundo "
                "também começam fazendo exatamente as mesmas perguntas que você!"
            )
            st.markdown(f"### 🔭 Resposta do Explorador Espacial:")
            st.markdown(f'<div class="resposta-box">{resposta_padrao}</div>', unsafe_allow_html=True)
            
    else:
        st.warning("⚠️ Digite um tema ou pergunta na caixa acima para o foguete poder decolar!")

# Rodapé otimizado para Live
st.markdown("---")
st.markdown("💡 **Dica para sua Live / OBS:** Adicione uma fonte de **Captura de Janela** no seu OBS selecionando esta aba do navegador. Vai rodar perfeito e sem erros!")
