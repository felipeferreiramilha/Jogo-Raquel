
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
st.markdown("### Digite qualquer tema sobre o espaço para ver explicações claras e divertidas!")

# ==========================================================
# 2. BANCO DE CONHECIMENTO (RESPOSTAS PRONTAS E REVISADAS)
# ==========================================================
BASE_CONHECIMENTO = {
    "mercúrio": (
        "Mercúrio é o planeta mais próximo do Sol e também o menorzinho de todos os oito planetas do Sistema Solar. "
        "Como ele fica bem colado ao Sol, a parte dele que fica virada para a luz é tããão quente que poderia derreter metais, "
        "enquanto o outro lado é super congelante!\n\n"
        "Ele é um planeta rochoso, cheio de buraquinhos na superfície chamados crateras, parecendo uma grande lua cinzenta."
    ),
    "vênus": (
        "Vênus é o segundo planeta a partir do Sol e brilha tanto no nosso céu noturno que muita gente acha que é uma estrela. "
        "Apesar de ter um tamanho parecido com o da Terra, ele é o planeta mais quente de todo o Sistema Solar!\n\n"
        "Isso acontece porque Vênus tem uma camada de nuvens muito grossa que prende o calor lá dentro, fazendo um efeito estufa gigante."
    ),
    "terra": (
        "A Terra é a nossa linda nave espacial azul, o único lugar em todo o universo onde sabemos com certeza que existe vida, "
        "água líquida em abundância e ar fresquinho para respirar.\n\n"
        "Ela viaja ao redor do Sol em uma dança perfeita e também gira em torno de si mesma, criando o dia e a noite para a gente brincar e descansar."
    ),
    "marte": (
        "Marte é conhecido como o planeta vermelho porque o seu chão é coberto por uma poeira cheia de ferro enferrujado, "
        "dando a ele essa cor avermelhada super charmosa.\n\n"
        "Ele é um mundo rochoso com vulcões gigantes e vales profundos. Os cientistas mandam robôs chamados rovers para lá "
        "para procurar pistas de que Marte já teve rios e lagos no passado."
    ),
    "júpiter": (
        "Júpiter é o grandão da turma, o maior planeta do Sistema Solar. Ele é um gigante feito inteiramente de gases e nuvens coloridas, "
        "o que significa que ele nem tem chão sólido para pisar!\n\n"
        "A coisa mais famosa dele é a Grande Mancha Vermelha, que na verdade é uma tempestade gigante, maior do que a Terra inteira, "
        "que está girando sem parar há centenas de anos."
    ),
    "saturno": (
        "Saturno é o planeta mais estiloso do espaço porque ele usa chapéus gigantes em formato de anéis brilhantes. "
        "Esses anéis não são sólidos: eles são formados por bilhões de pedacinhos de gelo e rocha que ficam orbitando o planeta.\n\n"
        "Uma curiosidade divertida é que Saturno é tão leve que, se existisse uma banheira gigante com água no espaço, ele flutuaria como uma boia!"
    ),
    "sol": (
        "O Sol é a estrela gigante e superquente que fica no centro da nossa vizinhança cósmica. "
        "Ele é como uma fogueira mágica que nunca apaga, produzindo energia através de um processo chamado fusão nuclear no seu interior.\n\n"
        "Sem o Sol, a Terra seria escura, congelada e a vida não existiria. Ele nos dá luz, calor e segura todos os planetas com sua gravidade."
    ),
    "lua": (
        "A Lua é a companheira fiel da Terra, brilhando no céu noturno porque reflete a luz do Sol para nós. "
        "Ela realiza uma viagem ao redor do nosso planeta e ajuda a controlar as marés dos oceanos.\n\n"
        "Foi lá que os astronautas pisaram pela primeira vez na história, deixando pegadas que vão durar para sempre porque não há vento na Lua para apagá-las."
    ),
    "buraco negro": (
        "Um buraco negro é uma região do espaço onde a matéria ficou espremida de um jeito tão apertado que gerou uma gravidade monstruosa! "
        "Essa gravidade é tão forte que nem mesmo a luz consegue escapar se chegar perto demais.\n\n"
        "Mas calma: eles não ficam sugando as coisas como aspiradores de pó gigantes. Eles ficam muito distantes e ajudam os cientistas "
        "a entenderem as regras mais profundas de como o universo funciona."
    ),
    "matéria escura": (
        "A matéria escura é como um ingrediente invisível do universo. A gente não consegue enxergar ela com telescópios comuns "
        "porque ela não emite luz e nem brilha.\n\n"
        "No entanto, sabemos que ela existe porque a sua gravidade ajuda a segurar as galáxias unidas, funcionando como um esqueleto secreto "
        "que impede as estrelas de voarem para longe."
    )
}

# ==========================================================
# 3. CAMPO DE PESQUISA E BUSCA INTELIGENTE
# ==========================================================
pergunta = st.text_input(
    "O que você quer descobrir no universo hoje?",
    placeholder="Ex: Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Sol, Lua, Buraco negro..."
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
st.markdown("💡 **Dica para sua Live / OBS:** Adicione uma fonte de **Captura de Janela** no seu OBS selecionando esta aba do navegador. Vai rodar liso e sem erros!")
