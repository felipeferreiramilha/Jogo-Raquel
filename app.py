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
st.markdown("### Digite qualquer dúvida sobre o espaço: buracos negros, planetas, multiverso e viagens no tempo!")

# ==========================================================
# 2. BANCO DE CONHECIMENTO GIGANTE (AS 100 PERGUNTAS)
# ==========================================================
BASE_CONHECIMENTO = {
    # 1. O Sistema Solar, Planetas e Mundos Exóticos
    "sol fogo": "Não! O Sol não tem fogo. Ele é uma gigantesca bola de gás superaquecido (plasma) onde acontece uma usina nuclear natural chamada fusão nuclear, transformando hidrogênio em hélio.",
    "chove diamante": "Sim! O metano na atmosfera desses gigantes gasosos é esmagado por tempestades e pressões gigantescas, transformando-se em carbono puro que cai na forma de chuva de diamantes sólidos.",
    "vênus quente": "Por causa do efeito estufa descontrolado. Vênus tem uma atmosfera muito grossa de gás carbônico que prende o calor do Sol lá dentro como um cobertor térmico gigante.",
    "planeta negro": "São exoplanetas como o TrES-2b, cujas atmosferas contêm substâncias químicas que absorvem até 99% da luz que bate neles, fazendo-os parecer carvão puro e superescuro flutuando no espaço.",
    "exoplanetas invisíveis": "Eles usam o Método do Trânsito: observam a estrela e esperam o planeta passar na frente dela, causando uma pequena 'piscada' ou queda no brilho da luz estelar.",

    # 2. Estrelas, Constelações e a Fábrica do Cosmos
    "estrelas mortas": "Sim! Como a luz demora anos para viajar pelo espaço até chegar aos nossos olhos, olhar para estrelas distantes é literalmente olhar para o passado delas.",
    "constelações": "Não são reais fisicamente. As constelações são apenas linhas imaginárias que os povos antigos traçaram ligando estrelas distantes no céu como se fossem pontos de ligar os pontos.",
    "sol morrer": "Ele vai inchar virando uma gigante vermelha, engolir os planetas mais próximos e depois encolher até virar uma estrela pequenininha, fria e densa chamada anã branca.",
    "estrela de nêutrons": "Sim! É o resto supercompacto de uma estrela morta. Uma colherinha de chá de matéria de uma estrela de nêutrons pesaria bilhões de toneladas na Terra.",
    "corpo poeira estrelas": "Eles foram fabricados no coração de estrelas massivas que explodiram em supernovas bilhões de anos atrás. Nós literalmente somos feitos de 'poeira de estrelas'!",

    # 3. Buracos Negros, Buracos de Minhoca e Relatividade
    "buraco negro aspirador": "Não exatamente. Se o Sol virasse um buraco negro do mesmo peso, a Terra continuaria orbitando do mesmo jeito. Ele só engole o que chega perigosamente perto, além do seu 'Horizonte de Eventos'.",
    "horizonte de eventos": "É o ponto sem retorno. É a borda invisível onde a gravidade se torna tão forte que nem a luz consegue escapar de lá de dentro.",
    "cair buraco negro": "A gravidade puxaria seus pés com muito mais força do que a sua cabeça, esticando você como se fosse um macarrão espaguete (um efeito que os físicos chamam de espaguetificação).",
    "tempo devagar buraco": "Sim! A gravidade extrema distorce o espaço-tempo. Se você passasse um tempo perto de um buraco negro e voltasse para a Terra, seus amigos estariam muito mais velhos que você.",
    "buraco de minhoca": "É uma ponte teórica que liga dois lugares distantes do universo (ou até universos diferentes) através de um atalho no espaço-tempo. Na ciência real, nunca vimos um funcionando.",

    # 4. O Big Bang e a Idade do Universo
    "big bang": "Não foi uma explosão no espaço, mas sim a expansão rápida do próprio espaço a partir de um ponto extremamente minúsculo, quente e denso, há cerca de 13,8 bilhões de anos.",
    "idade universo": "Cerca de 13,8 bilhões de anos (com uma margem de erro muito pequena calculada pelos cientistas estudando o eco do Big Bang).",
    "antes do big bang": "A física atual diz que o próprio tempo não existia antes do Big Bang. Perguntar o que havia antes é como perguntar o que fica 'ao norte do Polo Norte'.",
    "radiação cósmica fundo": "É o eco luminoso e térmico do Big Bang. Se pudéssemos ver micro-ondas com os olhos, o céu inteiro brilharia com o calor remanescente da criação do universo.",
    "borda infinito": "Nós não sabemos ao certo. O universo observável tem um limite porque a luz de mais longe ainda não deu tempo de chegar até nós, mas o universo como um todo pode ser infinito.",

    # 5. Matéria Escura e Energia Escura
    "matéria escura": "É uma matéria misteriosa e invisível que não emite nem reflete luz, mas sabemos que ela existe porque a sua gravidade funciona como uma 'cola' segurando as galáxias unidas para elas não se despedaçarem.",
    "energia escura": "É uma força misteriosa que está fazendo o universo se expandir cada vez mais rápido, empurrando as galáxias umas das outras para longe em vez de deixá-las juntas.",
    "95 porcento universo": "Sim! Tudo o que conseguimos ver (estrelas, planetas, árvores, nós mesmos) forma apenas 5% do universo. Os outros 95% são formados por Matéria Escura e Energia Escura.",
    "corpo matéria escura": "Sim! Milhões de partículas de matéria escura podem estar atravessando o seu corpo neste exato segundo sem que você sinta absolutamente nada, porque elas quase não interagem com a matéria comum.",
    "antimatéria": "É o 'espelho' da matéria normal. Cada partícula tem uma antipartícula gêmea; se a matéria tocar na antimatéria, elas se destroem instantaneamente gerando uma explosão pura de energia.",

    # 6. Viagem no Tempo e Superpoderes
    "viagem futuro": "Sim! A Teoria da Relatividade de Einstein prova que se você viajar em uma nave espacial em uma velocidade próxima à da luz, o tempo passa mais devagar para você do que para quem ficou na Terra.",
    "viagem passado": "A física atual diz que quase certamente não, pois isso quebraria as leis da causa e efeito e criaria paradoxos insolúveis (como o paradoxo de voltar e impedir seu próprio nascimento).",
    "táquions": "São partículas hipotéticas criadas na imaginação da física que andariam sempre mais rápido que a luz e, por causa disso, viajariam para trás no tempo. Elas nunca foram encontradas.",
    "efeito zeno quântico": "É uma lei esquisita da mecânica quântica que diz que um sistema quântico não muda de estado se você ficar 'olhando' (medindo) para ele o tempo todo.",
    "gato de schrödinger": "É uma experiência mental famosa que mostra que, no mundo microscópico da física quântica, as coisas podem ficar em dois estados ao mesmo tempo (como um gato vivo e morto) até que alguém olhe para abrir a caixa.",

    # 7. Dimensões Extras, Multiverso e Unificação
    "dimensões extras": "Nós vivemos em três dimensões espaciais (frente/trás, cima/baixo, esquerda/direita) mais o tempo. A Teoria das Cordas diz que o universo pode ter 10 ou 11 dimensões, mas as outras são microscópicas e enroladas.",
    "gravidade fraca": "A Teoria das Cordas sugere que a gravidade é fraca porque ela 'vaza' para dimensões extras que não conseguimos enxergar, enquanto as outras forças ficam presas no nosso mundo 3D.",
    "multiverso": "É a ideia científica de que o nosso universo pode não ser o único, mas sim um entre infinitos outros universos paralelos que existem separados uns dos outros.",
    "teoria de tudo": "É o grande sonho dos cientistas de juntar a Mecânica Quântica (a física do muito pequeno) com a Relatividade Geral (a física do muito grande e da gravidade) em uma única e bela equação matemática.",
    "universo holograma": "O Princípio Holográfico sugere que toda a informação tridimensional do nosso universo pode ser apenas uma projeção codificada em uma borda bidimensional distante.",

    # 8. Curiosidades e "E Se...?"
    "terra parar girar": "Tudo o que não está preso ao chão (pessoas, carros, prédios) continuaria voando para o leste na velocidade em que a Terra girava (mais de 1.600 km/h no Equador).",
    "fogueira espaço": "Não. Sem oxigênio e sem gravidade para fazer o ar quente subir e o oxigênio fresco chegar, o fogo não consegue se sustentar e a chama morre na hora.",
    "astronautas flutuam": "Eles não flutuam porque não há gravidade lá em cima (a gravidade da Terra lá é de cerca de 90%). Eles flutuam porque estão em queda livre eterna junto com a estação ao orbitarem a Terra.",
    "lixo sol": "O Sol é tão gigantesco que qualquer lixo que jogássemos lá (até a Terra inteira) seria desintegrado e evaporado instantaneamente sem nem fazer cócegas nele.",
    "céu escuro paradoxo": "Esse é o Paradoxo de Olbers. O céu é escuro porque o universo tem uma idade finita (cerca de 13,8 bilhões de anos) e a luz das estrelas mais distantes ainda não teve tempo de chegar até nós.",

    # 9. Buracos Brancos, Fim do Universo e Extremos
    "buraco branco": "É o oposto teórico de um buraco negro: um objeto cósmico de onde tudo é expelido com força e no qual nada consegue entrar. Até hoje, eles existem apenas no papel da matemática.",
    "universo acabar": "Existem vários cenários: o Big Freeze (as estrelas morrem, o universo esfria e apaga), o Big Rip (a energia escura rasga até os átomos) ou o Big Crunch (o universo para de crescer e encolhe de volta).",
    "quasares": "São os núcleos mais brilhantes do universo, alimentados por buracos negros supermassivos no centro de galáxias jovens que devoram matéria vorazmente e cospem jatos de luz e radiação.",
    "raios gama": "São as explosões mais violentas do universo, geradas pela morte de estrelas gigantescas. Se uma delas acontecesse perto de nós, poderia destruir a camada de ozônio da Terra.",
    "espuma quântica": "É como o espaço-tempo se comporta na menor escala possível (Escala de Planck): em vez de ser liso, ele é um oceano fervilhante, caótico e cheio de bolhas microscópicas de energia.",

    # 10. Vida Extraterrestre e o Futuro
    "sozinhos universo": "Matematicamente, com trilhões de planetas por aí, os cientistas acham improvável estarmos sozinhos, mas ainda não encontramos nenhuma prova de vida inteligente fora da Terra.",
    "paradoxo de fermi": "É a grande pergunta: 'Se o universo é gigantesco e antigo, cheio de chances para a vida surgir, onde é que está todo mundo? Por que nunca vimos alienígenas?'",
    "escala de kardashev": "É uma forma de medir quão avançada é uma civilização baseada em quanta energia ela consegue usar (uma civilização Tipo I usa a energia do seu planeta, Tipo II usa a da sua estrela e Tipo III usa a de toda a galáxia).",
    "esfera de dyson": "É uma megaestrutura teórica que uma civilização muito avançada poderia construir ao redor de uma estrela inteira para capturar toda a energia e luz que ela produz.",
    "sinal wow": "Foi um sinal de rádio forte e misterioso vindo do espaço profundo que durou apenas um minuto e intrigou os cientistas. Até hoje ninguém sabe com certeza se foi gerado por alienígenas ou por interferência natural.",

    # 11. Segredos Extras de Buracos Negros e Estrelas
    "colisão buracos negros": "Eles se fundem em um buraco negro maior e sacodem o próprio tecido do espaço, criando ondas invisíveis chamadas ondas gravitacionais que viajam pelo universo.",
    "buracos negros minúsculos": "Sim! Os cientistas acham que, logo no início do Big Bang, podem ter se formado buracos negros microscópicos do tamanho de um grão de poeira ou de uma montanha.",
    "estrela de quarks": "É uma estrela hipotética ainda mais densa que a estrela de nêutrons, onde até os nêutrons se esmagam e viram uma sopa de partículas fundamentais chamadas quarks.",
    "estrelas piscam": "As estrelas piscam porque a luz delas viaja pela atmosfera da Terra e se mexe com o vento. Os planetas não piscam porque estão mais perto e parecem discos maiores aos nossos olhos.",
    "anãs marrons": "São as chamadas 'estrelas fracassadas': astros grandões como planetas gasosos, mas que não conseguiram juntar massa suficiente para acender a fogueira nuclear no centro.",

    # 12. Dimensões e Física Quântica
    "tecido espaço tempo": "É uma forma de imaginar o espaço e o tempo juntos como um lençol elástico invisível onde os planetas e as estrelas se apoiam e fazem curvas.",
    "emaranhamento quântico": "É quando duas partículas ficam tão ligadas que, se você muda uma na Terra, a outra muda instantaneamente na outra ponta do universo, desafiando a velocidade da luz.",
    "princípio incerteza": "É a regra da mecânica quântica que diz que você nunca consegue saber com total exatidão a velocidade e a posição de uma partícula ao mesmo tempo.",
    "universos paralelos quânticos": "A ideia de que, no mundo subatômico, cada escolha ou evento pode criar mundos diferentes para cada resultado possível.",
    "vácuo quântico": "Um espaço que parece totalmente vazio para nós, mas que na verdade está fervilhando de energia e partículas que aparecem e somem em frações de segundo.",

    # 13. Mais Matéria Escura e Energia Escura
    "pesar matéria escura": "Olhando para a velocidade com que as galáxias giram. Se não houvesse matéria escura, elas girariam tão rápido que voariam em pedaços.",
    "energia escura enfraquecer": "A maioria das teorias diz que não; ela parece estar ficando cada vez mais forte, acelerando a expansão do cosmos para sempre.",
    "lentes gravitacionais": "Quando a gravidade de uma galáxia ou de matéria escura é tão forte que entorta a luz de estrelas que estão atrás dela, funcionando como uma lente de óculos cósmica gigante.",
    "antimatéria terra": "Sim! Raios cósmicos que chegam do espaço geram pequenas quantidades de antimatéria na nossa atmosfera o tempo todo.",
    "sol matéria escura": "Algumas teorias sugerem que partículas de matéria escura podem ficar presas no centro do Sol e esquentá-lo levemente por dentro.",

    # 14. Viagens Espaciais e Ficção vs Realidade
    "ultrapassar velocidade luz": "Não. No espaço normal, nada com massa pode ir mais rápido do que a luz no vácuo.",
    "propulsão antimatéria": "Um motor futurista onde a reação entre matéria e antimatéria geraria a energia mais poderosa do universo para viagens interestelares rápidas.",
    "velas solares": "São grandes espelhos feitos de material superleve que usam o 'vento' de luz do Sol para empurrar a nave espacial pelo espaço sem gastar combustível.",
    "tempo estação espacial": "Sim! Por causa da velocidade e da gravidade mais fraca lá em cima, os astronautas envelhecem frações de segundo mais devagar do que nós na Terra.",
    "criogenia": "É a ideia de congelar pessoas no futuro para tentar ressuscitá-las em viagens espaciais de séculos — algo que hoje só funciona com pequenos insetos e plantas, não com humanos.",

    # 15. Inflação Cósmica e Início
    "inflação cósmica": "Um momento logo depois do Big Bang em que o universo cresceu de tamanho bilhões de vezes mais rápido que a luz em uma fração minúscula de segundo.",
    "temperatura uniforme": "A inflação cósmica explicou isso, esticando um pedacinho superpequeno e quentinho do início para formar todo o universo uniformemente.",
    "primeiros átomos formaram": "Cerca de 380 mil anos após o Big Bang, quando o universo esfriou o suficiente para os prótons conseguirem segurar os elétrons.",
    "primeiro elemento químico": "Principalmente hidrogênio, seguido por um pouco de hélio e traços de lítio.",
    "som no começo": "Sim! No início, o universo era um plasma denso onde ondas de som viajavam, deixando marcas impressas na luz que vemos hoje.",

    # 16. Exoplanetas e Mundos Oceânicos
    "zona goldilocks": "É a distância perfeita ao redor de uma estrela onde não é nem muito quente nem muito frio, permitindo que exista água líquida.",
    "planetas órfãos": "Sim! São os chamados planetas órfãos, que foram expulsos de seus sistemas e viajam na mais completa escuridão pelo espaço.",
    "planeta oceano": "Um mundo misterioso onde a superfície inteira é coberta por um oceano de água líquida com centenas de quilômetros de profundidade, sem nenhum pedaço de terra seca.",
    "luas gigantes exoplanetas": "Sim! Astrônomos já encontraram mundos distantes com sistemas de anéis que deixariam Saturno parecendo pequeno.",
    "kepler 186f": "Foi um dos primeiros exoplanetas do tamanho da Terra descoberto na zona habitável de sua estrela, gerando esperanças sobre mundos parecidos com o nosso.",

    # 17. Constelações e Astronomia Antiga
    "estrela sirius": "É Sirius, que fica na constelação do Cão Maior e brilha com muita força para quem olha da Terra.",
    "estrela polar": "É a estrela que aponta quase exatamente para o Polo Norte da Terra, usada por marinheiros e viajantes há séculos para se orientar sem bússola.",
    "constelações vizinhas": "Não! Elas parecem desenhar figuras juntas para nós, mas no espaço tridimensional estão a distâncias totalmente diferentes.",
    "via láctea fora": "Ela se parece com um disco espiral brilhante, semelhante a um cata-vento gigante com bilhões de estrelas.",
    "braços espirais": "São ondas de densidade onde o gás se acumula e nascem muitas estrelas novas e jovens.",

    # 18. Unificação e Gravidade
    "difícil unificar gravidade": "Porque a gravidade de Einstein trata o espaço como algo liso e contínuo, enquanto a quântica trata o mundo como pulos e pacotes caóticos.",
    "teoria das cordas": "A ideia de que todas as partículas do universo são formadas por cordas de energia vibrantes, como cordas invisíveis de um violão cósmico.",
    "gravidade quântica loop": "Outra tentativa de unificação que diz que o próprio espaço é feito de pequenos laços entreligados como uma rede microscópica.",
    "tempo pedacinhos": "Os físicos acham que sim: existe um limite mínimo chamado Tempo de Planck abaixo do qual o tempo não se divide mais.",
    "constante cosmológica": "O número que Einstein colocou em suas equações para tentar equilibrar o universo, que hoje usamos para explicar a energia escura.",

    # 19. Curiosidades Finais
    "sol buraco negro": "Não! Ele não tem massa suficiente para isso; ele vai se transformar em uma pacífica anã branca.",
    "grande rasgo": "O cenário apocalíptico onde a energia escura fica tão forte que rasga galáxias, planetas e até os átomos no fim dos tempos.",
    "morte térmica": "O final em que todas as estrelas apagam, o universo esfria completamente e fica totalmente escuro, vazio e imóvel.",
    "ano luz": "Não é tempo, é distância: a distância que a luz viaja em um ano inteiro — cerca de 9,5 trilhões de quilômetros!",
    "planetas giram": "Por causa da inércia (eles querem seguir em linha reta) combinada com a gravidade do Sol (que os puxa para o centro), fazendo-os cair em um círculo eterno.",

    # 20. Outras Perguntas Incríveis
    "luz rápido demoramos": "Porque o universo é gigantesco e as galáxias estão a milhões ou bilhões de anos-luz de distância de nós!",
    "raios cósmicos": "Partículas atômicas invisíveis que viajam pelo espaço quase na velocidade da luz e atingem a atmosfera da Terra o tempo todo.",
    "som espaço sideral": "No vácuo não há ar, então o som comum não viaja. Mas em nuvens de gás gigantes de galáxias existem ondas de som ultrabaixas.",
    "lua crateras terra": "A Terra tem atmosfera, vento e água que apagam as marcas de impactos antigos com a erosão. A Lua não tem nada disso, guardando tudo na superfície.",
    "voar em linha reta": "Você viajaria por todo o Sistema Solar, sairia da Via Láctea e entraria no oceano infinito de galáxias do universo!",

    # CLÁSSICOS ANTERIORES (PLANETAS E GERAL)
    "mercúrio": "Mercúrio é o menorzinho e mais perto do Sol. O lado virado para a luz ferve a metais, enquanto o lado da sombra congela. E o céu dele é totalmente preto!",
    "vênus": "Vênus é o planeta mais quente de todos por causa de seu efeito estufa gigante, e ele gira ao contrário dos outros!",
    "terra": "A Terra é a nossa nave espacial azul, o único lugar do universo com água líquida em abundância e vida.",
    "marte": "Marte é o planeta vermelho por causa da ferrugem no chão. Ele tem o Monte Olimpo, o maior vulcão do Sistema Solar.",
    "júpiter": "Júpiter é o grandão gasoso do grupo. Sua Grande Mancha Vermelha é uma tempestade maior que a Terra.",
    "saturno": "Saturno usa anéis fabulosos feitos de bilhões de pedacinhos de gelo. Ele flutuaria em uma banheira de água!",
    "urano": "Urano é um gigante de gelo azul que gira completamente deitado de lado.",
    "netuno": "Netuno é um mundo azul e gelado onde sopram os ventos mais violentos de todo o Sistema Solar.",
    "lua": "A Lua é a companheira da Terra que controla as marés e guarda pegadas de astronautas para sempre."
}

# ==========================================================
# 3. CAMPO DE PESQUISA E BUSCA INTELIGENTE
# ==========================================================
pergunta = st.text_input(
    "O que você quer descobrir no universo hoje?",
    placeholder="Ex: Sol fogo, Chove diamante, Vênus, Buraco negro, Matéria escura, Multiverso..."
)

if st.button("🌟 Decolar Pesquisa Cósmica!", type="primary"):
    if pergunta.strip() != "":
        pergunta_lower = pergunta.lower()
        encontrou = False
        
        # Procura por correspondências no banco gigante de 100+ perguntas
        for chave, texto in BASE_CONHECIMENTO.items():
            # Verifica se palavras da chave estão na pergunta do usuário
            palavras = chave.split()
            if chave in pergunta_lower or all(p in pergunta_lower for p in palavras):
                st.markdown(f"### 🔭 Resposta Mágica:")
                st.markdown(f'<div class="resposta-box">{texto}</div>', unsafe_allow_html=True)
                encontrou = True
                break
        
        # Se não achar por correspondência exata, busca por palavras soltas
        if not encontrou:
            for chave, texto in BASE_CONHECIMENTO.items():
                if any(p in pergunta_lower for p in chave.split() if len(p) > 3):
                    st.markdown(f"### 🔭 Resposta Mágica:")
                    st.markdown(f'<div class="resposta-box">{texto}</div>', unsafe_allow_html=True)
                    encontrou = True
                    break

        # Resposta padrão mágica caso nenhum termo combine
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

# Rodapé otimizado para Live / OBS
st.markdown("---")
st.markdown("💡 **Dica para sua Live / OBS:** Adicione uma fonte de **Captura de Janela** no seu OBS selecionando esta aba do navegador. Vai rodar perfeito, sem erros e com todas as respostas!")
