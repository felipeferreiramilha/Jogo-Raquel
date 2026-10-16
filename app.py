import streamlit as st

# ==========================================================
# 1. CONFIGURAÇÃO DA PÁGINA
# ==========================================================
st.set_page_config(
    page_title="Astronomia para Crianças",
    page_icon="🚀",
    layout="centered"
)

# Estilização visual amigável e limpa para Live / OBS
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
# 2. BANCO DE CONHECIMENTO COMPLETO (TODAS AS PERGUNTAS)
# ==========================================================
BASE_CONHECIMENTO = {
    # SISTEMA SOLAR E MUNDOS ALIENÍGENAS
    "júpiter mancha": "A Grande Mancha Vermelha de Júpiter é, na verdade, uma tempestade gigante e furiosa, maior do que a Terra inteira, que está girando sem parar há centenas de anos!",
    "saturno anéis": "Saturno não é o único planeta com anéis — Júpiter, Urano e Netuno também têm os seus! Mas os de Saturno são os mais brilhantes e formados por bilhões de pedacinhos de gelo e rocha.",
    "anéis de saturno feitos": "Os anéis de Saturno são feitos principalmente de pedaços de gelo de água pura, variando desde grãozinhos de poeira até pedregulhos do tamanho de uma casa.",
    "chove diamante": "Sim! Em Júpiter e Saturno, tempestades transformam o metano em fuligem de carbono que cai como rochas sólidas, derretendo e virando verdadeiras chuvas de diamantes no interior dos planetas gasosos!",
    "planeta mais quente": "O planeta mais quente é Vênus, e não Mercúrio! Mesmo Vênus estando mais longe do Sol, sua atmosfera grossa de gás carbônico cria um efeito estufa monstruoso que prende o calor para sempre.",
    "vênus ao contrário": "Sim! Vênus gira de cabeça para baixo em comparação com a maioria dos outros planetas, o que significa que lá o Sol nasce no oeste e se põe no leste.",
    "marte planeta vermelho": "Marte é conhecido como o Planeta Vermelho porque o seu chão é coberto por uma poeira fina cheia de óxido de ferro, que é basicamente ferrugem.",
    "água em marte": "Hoje em dia não existem rios correndo em Marte, mas os cientistas descobriram água congelada em suas calotas polares e embaixo do solo.",
    "monte olimpo": "Sim! O Monte Olimpo em Marte é um vulcão gigantesco que é quase três vezes mais alto que o Monte Everest, a montanha mais alta da Terra.",
    "plutão rebaixado": "Plutão foi rebaixado a planeta anão porque os astrônomos descobriram vários outros objetos parecidos com ele na mesma região e decidiram que um planeta de verdade precisa 'limpar' sua órbita de outros corpos.",
    "urano deitado": "Urano gira completamente deitado de lado, como uma bola rolando, muito provavelmente porque levou uma pancada cósmica gigantesca no passado.",
    "ventos de netuno": "Sim! Netuno tem os ventos mais rápidos e violentos de todo o Sistema Solar, ultrapassando facilmente a velocidade do som.",
    "terra parar de girar": "Se a Terra parasse de girar por um segundo, tudo o que não estivesse preso ao chão continuaria voando em alta velocidade por causa da inércia!",
    "lua mesma face": "A Lua sempre mostra a mesma face para nós porque ela leva o mesmo tempo exato para dar uma volta em torno de si mesma (rotação) e uma volta ao redor da Terra (translação).",
    "lua afastando": "Sim! A Lua está se afastando bem devagarinho da Terra, cerca de 3 centímetros por ano, mas fique tranquilo: ela nunca vai embora de vez.",
    "crateras da lua": "As crateras da Lua foram formadas por impactos violentos de meteoritos e asteroides ao longo de bilhões de anos, e não por vulcões.",
    "sol estrela grande": "O Sol é uma estrela de tamanho médio. Existem estrelas milhares de vezes maiores que ele, chamadas supergigantes, e outras bem menores, chamadas anãs vermelhas.",
    "sol faz barulho": "O Sol faz muito barulho em seu interior por causa das reações nucleares, mas o som não viaja no espaço porque o espaço é um vácuo onde não há ar para o som se propagar.",
    "cometas": "Cometas são bolas de neve cósmica feitas de gelo, poeira e rocha que vêm dos confins do Sistema Solar e ganham caudas brilhantes quando passam perto do Sol.",
    "meteoro meteorito asteróide": "Asteroide é uma rocha grande vagando no espaço; meteoro é quando esse pedacinho entra na atmosfera e brilha como estrela cadente; e meteorito é o pedaço que sobrevive à queda e chega ao chão.",
    "extinção dinossauros": "Sim, a extinção dos dinossauros há 66 milhões de anos foi causada pela queda de um asteroide gigante na região de Chicxulub, na península de Yucatán, no México.",
    "planeta nove": "O Planeta Nove é um mundo hipotético e gigante que os cientistas acham que pode estar escondido nos confins gelados do Sistema Solar, explicando a órbita de alguns asteroides distantes.",
    "gravidade colados": "A gravidade da Terra nos puxa firmemente para o seu centro, agindo como um abraço invisível que nos mantém seguros no chão enquanto o planeta gira.",
    "planetas redondos": "Os planetas são redondos porque a gravidade puxa a matéria igualmente de todas as direções em direção ao centro, espremendo tudo no formato de uma esfera.",
    "mercúrio atmosfera céu": "Mercúrio quase não tem atmosfera, então o céu lá durante o dia é totalmente preto, e é possível ver as estrelas ao lado do Sol.",
    "temperatura mercúrio": "Como Mercúrio não tem atmosfera para segurar o calor, o lado virado para o Sol ferve, enquanto o lado na sombra congela completamente.",
    "luas de gelo oceanos": "Sim! Mundos como Europa (de Júpiter) e Encélado (de Saturno) escondem oceanos líquidos gigantescos debaixo de cascas grossas de gelo.",
    "vida luas de gelo": "Os cientistas acham que sim, pois esses oceanos subterrâneos recebem calor do interior das luas e podem ter condições para abrigar micróbios e formas simples de vida.",
    "nuvem de oort": "A Nuvem de Oort é uma gigantesca casca esférica de cometas e gelo que envolve todo o Sistema Solar lá nos confins mais distantes.",
    "bola de beisebol espaço": "Se você jogar uma bola de beisebol no espaço vazio, ela continuará viajando em linha reta para sempre até bater em algum obstáculo, porque não há atrito para pará-la.",

    # ESTRELAS E COSMOS
    "estrela morre": "Quando uma estrela morre, ela pode se transformar em uma anã branca pacífica, numa estrela de nêutrons densa, ou explodir como uma supernova espetacular.",
    "supernova": "Uma supernova é a explosão colossal de uma estrela no fim da vida, brilhando mais do que galáxias inteiras por alguns dias.",
    "estrela de nêutrons colher": "Sim! Uma estrela de nêutrons é tão espremida e densa que uma única colherzinha dela pesaria bilhões de toneladas na Terra.",
    "pulsar": "Um pulsar é uma estrela de nêutrons que gira rapidamente emitindo feixes de luz como um farol cósmico gigante.",
    "nebulosas nascem": "As estrelas nascem dentro de imensas nuvens de gás e poeira chamadas nebulosas, onde a gravidade junta a matéria até acender a fogueira nuclear.",
    "cor estrela quente": "A estrela mais quente do universo brilha em uma cor azul intensa, enquanto as mais frias brilham em vermelho.",
    "sol anã branca": "Sim, daqui a bilhões de anos, quando o Sol terminar seu combustível, ele vai se expandir e depois encolher, virando uma anã branca fria e brilhante.",
    "gigante vermelha": "Uma gigante vermelha é a fase em que uma estrela envelhece, incha e fica gigantesca e avermelhada antes de morrer.",
    "estrelas vagam": "Sim, existem estrelas órfãs que foram expulsas de suas galáxias e vagam sozinhas na imensidão escura do espaço intergaláctico.",
    "magnetares": "Magnetares são estrelas de nêutrons com campos magnéticos absurdamente fortes, capazes de apagar todos os cartões de crédito da Terra a uma distância enorme.",
    "estrelas mortas céu": "Sim! Como a luz demora anos para viajar das estrelas até nós, algumas estrelas que vemos no céu podem já ter morrido, mas ainda vemos a luz delas chegando.",
    "constelação órion": "Órion é uma das constelações mais famosas do céu noturno, e dentro dela fica a deslumbrante Grande Nebulosa de Órion, um berçário de estrelas.",
    "medir distância estrelas": "Os astrônomos usam um método chamado paralaxe, medindo como a posição da estrela muda no céu conforme a Terra se move ao redor do Sol.",
    "aglomerado estelar": "Um aglomerado estelar é um grupo de milhares de estrelas unidas pela gravidade que nasceram juntas da mesma nebulosa.",
    "estrelas binárias": "São sistemas onde duas estrelas orbitam uma à outra em uma dança cósmica em dupla.",
    "hidrogênio hélio sol": "No centro do Sol, a pressão e a temperatura esmagam átomos de hidrogênio, fundindo-os em hélio e liberando uma energia monstruosa.",
    "vento solar auroras": "O vento solar é um fluxo de partículas carregadas liberadas pelo Sol que, ao bater no campo magnético da Terra, criam as lindas auroras boreais nos polos.",
    "sol virar buraco negro": "Não, o Sol não tem massa suficiente para virar um buraco negro; ele vai terminar sua vida de forma bem mais calma como uma anã branca.",
    "estrela mais brilhante": "A estrela mais brilhante do céu noturno da Terra é Sirius, localizada na constelação do Cão Maior.",
    "nebulosas planetárias": "Apesar do nome, nebulosas planetárias não têm nada a ver com planetas; são apenas as capas de gás que uma estrela moribunda solta no espaço.",
    "diagrama hertzsprung russell": "É um gráfico famoso que os astrônomos usam para classificar as estrelas de acordo com seu brilho e temperatura.",
    "matéria escura antimatéria estrelas": "Não existem estrelas feitas de matéria escura ou antimatéria de forma estável; as estrelas comuns são feitas de matéria normal.",
    "luz passar perto gravidade": "A luz sofre um desvio em sua trajetória quando passa perto de um objeto com gravidade muito forte, fenômeno chamado lente gravitacional.",
    "céu povos antigos": "Para os povos antigos, o céu era um grande mapa sagrado cheio de histórias, mitos e calendários para orientar a agricultura e a navegação.",
    "via láctea nome": "A Via Láctea tem esse nome porque, vista de um lugar escuro, ela parece um caminho leitoso espalhado pelo céu noturno.",

    # BURACOS NEGROS E MISTÉRIOS
    "buraco negro aspirador": "Um buraco negro não é um aspirador de pó cósmico; ele só atrai o que chega perfeitamente perto dele, mantendo os planetas seguros em órbita se estiverem distantes.",
    "horizonte de eventos": "O Horizonte de Eventos é o 'ponto sem retorno' de um buraco negro: cruzou essa linha, nem a luz consegue escapar.",
    "singularidade": "A singularidade é o centro exato de um buraco negro, onde toda a matéria está espremida em um ponto de tamanho zero e densidade infinita.",
    "espaguetificação": "Se você caísse em um buraco negro, a gravidade na sua cabeça seria diferente da gravidade nos seus pés, fazendo você ser esticado como um fio de espaguete!",
    "tempo devagar buraco negro": "Sim! Perto de um buraco negro, a gravidade é tão extrema que o tempo passa muito mais devagar para quem está lá do que para quem está longe.",
    "dentro de buraco negro": "Ninguém sabe com certeza o que há dentro de um buraco negro, pois as leis da física atual param de funcionar na singularidade.",
    "buracos negros supermassivos": "Sim, os cientistas acreditam que há um buraco negro supermassivo escondido no centro de quase todas as grandes galáxias do universo, inclusive a nossa.",
    "foto buraco negro": "Os cientistas tiraram a foto de um buraco negro fotografando a 'sombra' dele contra o anel brilhante de gás quente ao seu redor usando uma rede global de telescópios.",
    "buracos brancos": "Buracos brancos são objetos teóricos que fariam o oposto de um buraco negro, cuspindo matéria em vez de atraí-la, mas nunca foram encontrados.",
    "radiação de hawking": "É um brilho teórico descoberto por Stephen Hawking que faz com que os buracos negros evaporen bem devagarinho ao longo de eras cósmicas.",
    "sol virar buraco negro terra": "Se o Sol magicamente virasse um buraco negro com a mesma massa, a Terra continuaria orbitando normalmente, mas ficaria congelada e escura.",
    "buraco de minhoca": "Um buraco de minhoca é um atalho teórico através do espaço-tempo que, na ficção científica, permite viajar grandes distâncias em segundos.",
    "criar buraco negro laboratório": "Não é possível criar buracos negros perigosos em laboratórios na Terra; se diminutos buracos quânticos fossem criados, eles evaporariam instantaneamente.",
    "jatos relativísticos": "São jatos potentes de partículas que alguns buracos negros cospem a quase a velocidade da luz.",
    "como buracos negros crescem": "Eles crescem engolindo gás, poeira estelar e fundindo-se com outros buracos negros.",
    "buraco negro perto terra": "O buraco negro conhecido mais próximo da Terra fica a cerca de 1.500 anos-luz de distância, o que é muito seguro para nós.",
    "curvatura espaço tempo": "Einstein explicou que o espaço e o tempo formam um tecido elástico que se curva e deforma na presença de massas pesadas, criando a gravidade.",
    "gravidade força ou deformação": "Na teoria de Einstein, a gravidade não é uma força invisível tradicional, mas sim a curvatura do tecido do espaço-tempo.",
    "relatividade geral": "É a fantástica teoria de Einstein que revolucionou nossa compreensão do universo, explicando como a gravidade governa o cosmos.",
    "relógios satélites gps": "Como os satélites de GPS estão no espaço e sentem menos gravidade, seus relógios precisam ser corrigidos constantemente para que o GPS da Terra funcione direito.",

    # BIG BANG E ORIGEM
    "como universo começou": "O universo começou com o Big Bang, a rápida expansão de um ponto minúsculo, quente e denso, há 13,8 bilhões de anos.",
    "big bang explosão espaço": "O Big Bang não aconteceu *no* espaço; ele foi a expansão do próprio espaço criando o universo inteiro.",
    "antes do big bang": "Antes do Big Bang, o tempo e o espaço como conhecemos simplesmente não existiam, então não havia um 'antes'.",
    "universo quente denso": "No comecinho, o universo era uma sopa tão quente e densa de energia que nem os átomos podiam se formar.",
    "radiação cósmica fundo": "É o eco fóssil do Big Bang, um mar de micro-ondas invisíveis que preenche todo o universo e pode ser detectado em todas as direções.",
    "primeiros átomos": "Milhares de anos depois do Big Bang, o universo esfriou o suficiente para os prótons e elétrons se unirem, formando os primeiros átomos de hidrogênio e hélio.",
    "primeiras estrelas": "As primeiras estrelas nasceram centenas de milhões de anos após o Big Bang, acendendo o universo com sua luz pela primeira vez.",
    "centro do universo": "O universo não tem um centro; como tudo está se expandindo em todas as direções, qualquer ponto pode parecer o centro.",
    "universo infinito borda": "Os cientistas não sabem se o universo é infinito ou se tem uma borda, mas até onde conseguimos enxergar, ele continua se estendendo sem fim.",
    "universo expandindo rápido": "O universo está se expandindo cada vez mais rápido por causa da misteriosa energia escura.",
    "big crunch": "O Big Crunch era uma teoria de que o universo pararia de crescer um dia e encolheria de volta, mas hoje sabemos que a expansão está acelerando.",
    "big rip": "O Big Rip é um cenário em que a energia escura cresce tanto que rasgaria galáxias, planetas e até os átomos no fim dos tempos.",
    "formato do universo": "As medições mostram que o nosso universo visível é incrivelmente plano.",
    "telescópio james webb passado": "O Telescópio James Webb consegue enxergar a luz de galáxias tão antigas que estamos vendo o universo como ele era há bilhões de anos.",
    "longe olhamos passado": "Sim! Como a luz demora tempo para viajar pelo espaço, quanto mais longe olhamos, mais no passado estamos enxergando.",
    "inflação cósmica início": "Foi um estiramento relâmpago do espaço logo no início do Big Bang, fazendo o cosmos crescer mais rápido que a luz.",
    "elementos químicos estrelas": "Os elementos químicos mais pesados foram forjados no interior das estrelas e em explosões cósmicas.",
    "quantidade materia constante": "No universo visível, a quantidade total de matéria e energia se mantém constante, apenas mudando de forma.",
    "princípio cosmológico": "É a ideia de que o universo é parecido em qualquer lugar que você olhe, não tendo um lugar especial.",
    "idade exata universo": "A idade calculada pela ciência moderna para o nosso universo é de aproximadamente 13,8 bilhões de anos.",

    # MATÉRIA ESCURA E ENERGIA ESCURA
    "materia escura o que e": "É um ingrediente invisível que não emite luz, mas usa sua gravidade para segurar as galáxias unidas.",
    "como sabemos materia escura": "Sabemos que ela existe porque as estrelas giram rápido demais nas galáxias e voariam para longe sem a gravidade extra dela.",
    "cola galaxias": "Exatamente! Ela funciona como uma cola cósmica invisível.",
    "particulas materia escura": "Os cientistas acham que ela é feita de partículas exóticas que ainda não conseguimos detectar em laboratório.",
    "energia escura o que e": "É a força misteriosa que empurra o universo para fora, acelerando sua expansão.",
    "95 porcento universo": "Sim! Cerca de 95% do cosmos é formado por matéria escura e energia escura, e só 5% é matéria comum.",
    "materia escura corpo": "Sim, trilhões de partículas de matéria escura passam pelo nosso corpo a cada segundo sem interagir com a gente.",
    "lentes gravitacionais": "Os cientistas mapeiam a matéria escura vendo como ela entorta a luz das galáxias ao fundo, como uma lente gigante.",
    "energia escura enfraquece": "As observações mostram que a energia escura continua forte e constante, vencendo a gravidade a longas distâncias.",
    "energia escura vence": "Se ela vencer totalmente, o universo continuará se expandindo até que tudo fique isolado e frio no futuro distante.",

    # DIMENSÕES EXTRAS E MULTIVERSO
    "dimensoes extras": "Na física, além das três dimensões espaciais e do tempo, algumas teorias dizem que podem existir dimensões extras escondidas.",
    "teoria das cordas dimensoes": "A Teoria das Cordas sugere que nosso universo tem 10 ou 11 dimensões para funcionar direitinho.",
    "onde estao dimensoes extras": "Elas estariam compactadas e enroladas em tamanhos subatômicos tão minúsculos que não conseguimos enxergar.",
    "gravidade fraca dimensoes": "Algumas ideias sugerem que a gravidade é fraca porque ela 'vaza' para essas dimensões extras.",
    "multiverso": "O multiverso é a fascinante ideia de que nosso universo pode ser apenas um entre infinitos outros universos paralelos.",
    "outra versao de mim": "Essa é uma ideia clássica de ficção científica inspirada na mecânica quântica, mas a ciência real ainda estuda se isso é possível.",
    "interpretacao muitos mundos": "É uma interpretação quântica que diz que cada escolha cria ramificações em universos paralelos diferentes.",
    "branas": "Na cosmologia moderna, branas são membranas tridimensionais onde nosso universo flutua em um espaço maior.",
    "teoria de tudo fisica": "Busca unificar a relatividade geral e a mecânica quântica em uma única grande teoria.",
    "gravidade quantica": "É a tentativa de entender a gravidade na menor escala dos átomos.",
    "principio holografico": "Sugere que toda a informação do nosso universo tridimensional pode estar codificada em uma borda bidimensional.",

    # VIDA EXTRATERRESTRE E FUTURO
    "sozinhos universo": "Ainda não sabemos se estamos sozinhos, mas o universo é gigantesco e cheio de possibilidades.",
    "equacao de drake": "É uma fórmula matemática usada para estimar quantas civilizações inteligentes podem existir na nossa galáxia.",
    "paradoxo de fermi": "É a famosa pergunta: 'Se há tantas estrelas, onde está todo mundo?'",
    "zona habitavel": "É a faixa ao redor de uma estrela onde a temperatura é perfeita para existir água líquida.",
    "exoplanetas": "Exoplanetas são mundos que orbitam outras estrelas além do nosso Sol.",
    "telescopio kepler": "Foi um telescópio espacial que descobriu milhares de exoplanetas ao observar a sombra deles passando na frente de suas estrelas.",
    "esfera de dyson": "É uma megaestrutura hipotética que uma civilização superavançada poderia construir ao redor de uma estrela para capturar toda a sua energia.",
    "viagem velocidade luz": "De acordo com a física atual, nada com massa pode alcançar ou ultrapassar a velocidade da luz no vácuo.",
    "programa artemis": "É o programa espacial moderno que está levando a humanidade de volta à Lua para criar bases permanentes.",
    "lixo espacial": "São pedaços de satélites antigos e foguetes que orbitam a Terra em alta velocidade, representando perigo para novas missões.",
    "estacao espacial internacional iss": "É um laboratório flutuante onde astronautas moram e trabalham em gravidade zero.",
    "por do sol marte": "Em Marte, o pôr do sol tem uma cor azulada fascinante por causa de como a poeira espalha a luz solar.",

    # CURIOSIDADES E "E SE...?"
    "duas luas": "Se a Terra tivesse duas luas, teríamos marés muito mais fortes e noites bem mais brilhantes.",
    "gritar espaco": "No espaço você não conseguiria ouvir um grito, pois o som precisa de ar para viajar.",
    "vela gravidade zero": "Em gravidade zero, a chama de uma vela fica com um formato perfeitamente redondo em vez de pontiagudo.",
    "chuva de ouro": "Um asteroide de ouro seria extremamente pesado e rico em minérios valiosos, mas a queda causaria um estrago gigantesco.",
    "soltar pipa martes": "Seria muito difícil soltar pipa em Marte porque a atmosfera de lá é muito fina para gerar sustentação no ar.",
    "buraco cavado terra": "Se você pulasse em um buraco que atravessasse a Terra inteira, você balançaria de um lado para o outro por causa da gravidade.",
    "espaco cheira": "Astronautas dizem que o espaço e a poeira da Lua cheiram a carne grelhada, metal quente e pólvora queimada.",
    "astronautas mais altos": "Sim, sem a gravidade puxando a coluna para baixo, os astronautas crescem alguns centímetros enquanto estão no espaço.",
    "idade terra anos galacticos": "O Sistema Solar já deu cerca de 18 voltas completas ao redor do centro da Via Láctea desde que nasceu.",
}

# ==========================================================
# 3. CAMPO DE PESQUISA E BUSCA INTELIGENTE
# ==========================================================
pergunta = st.text_input(
    "O que você quer descobrir no universo hoje?",
    placeholder="Ex: Mercúrio, Júpiter, Buraco negro, Matéria escura, Big Bang, Cometas, Multiverso..."
)

if st.button("🌟 Decolar Pesquisa Cósmica!", type="primary"):
    if pergunta.strip() != "":
        pergunta_lower = pergunta.lower()
        encontrou = False
        
        # Procura por palavras-chave em todo o banco gigante
        for chave, texto in BASE_CONHECIMENTO.items():
            # Se encontrar partes da chave ou palavras importantes na pergunta
            palavras_chave = chave.split()
            if any(p in pergunta_lower for p in palavras_chave) or chave in pergunta_lower:
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

# Rodapé otimizado para Live
st.markdown("---")
st.markdown("💡 **Dica para sua Live / OBS:** Adicione uma fonte de **Captura de Janela** no seu OBS selecionando esta aba do navegador. Vai rodar liso, perfeito e sem erros!")
