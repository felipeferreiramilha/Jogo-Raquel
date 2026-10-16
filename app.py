def montar_explicacao_astronomia(pergunta, resultados):
    """
    Gera uma resposta com EXATAMENTE 3 PARÁGRAFOS.
    A resposta é adaptada para crianças e usa os resultados
    encontrados na pesquisa para complementar a explicação.
    """

    pergunta_lower = pergunta.lower()

    # ==========================================================
    # IDENTIFICAÇÃO DO TEMA
    # ==========================================================

    aspectos = []

    temas = {
        "mercúrio": "Mercúrio",
        "venus": "Vênus",
        "vênus": "Vênus",
        "terra": "Terra",
        "marte": "Marte",
        "júpiter": "Júpiter",
        "jupiter": "Júpiter",
        "saturno": "Saturno",
        "urano": "Urano",
        "netuno": "Netuno",
        "netuno": "Netuno",
        "plutão": "Plutão",
        "plutao": "Plutão",
        "lua": "Lua",
        "sol": "Sol",
        "estrela": "Estrelas",
        "estrelas": "Estrelas",
        "buraco negro": "Buracos negros",
        "buracos negros": "Buracos negros",
        "exoplaneta": "Exoplanetas",
        "exoplanetas": "Exoplanetas",
        "galáxia": "Galáxias",
        "galaxia": "Galáxias",
        "galáxias": "Galáxias",
        "galaxias": "Galáxias",
        "via láctea": "Via Láctea",
        "via lactea": "Via Láctea",
        "big bang": "Big Bang",
        "matéria escura": "Matéria escura",
        "materia escura": "Matéria escura",
        "energia escura": "Energia escura",
        "buraco de minhoca": "Buracos de minhoca",
        "buracos de minhoca": "Buracos de minhoca",
        "colisão": "Colisões planetárias",
        "colisões": "Colisões planetárias",
        "colisao": "Colisões planetárias",
        "colisoes": "Colisões planetárias",
        "supernova": "Supernovas",
        "supernovas": "Supernovas",
        "estrela de nêutrons": "Estrelas de nêutrons",
        "estrelas de nêutrons": "Estrelas de nêutrons",
        "asteroide": "Asteroides",
        "asteroides": "Asteroides",
        "cometa": "Cometas",
        "cometas": "Cometas",
        "eclipse": "Eclipses",
        "eclipses": "Eclipses",
        "telescópio": "Telescópios",
        "telescopios": "Telescópios",
        "vida extraterrestre": "Vida fora da Terra",
        "vida alienígena": "Vida fora da Terra",
        "vida em outros planetas": "Vida fora da Terra",
        "gravidade": "Gravidade",
        "newton": "Newton e a gravidade",
        "kepler": "Leis de Kepler",
        "teoria das cordas": "Teoria das cordas",
        "cordas": "Teoria das cordas",
    }

    for palavra, tema in temas.items():
        if palavra in pergunta_lower and tema not in aspectos:
            aspectos.append(tema)

    # ==========================================================
    # BANCO DE EXPLICAÇÕES
    # ==========================================================

    respostas = {

        "Mercúrio": [
            "Mercúrio é o planeta mais próximo do Sol e também o menor dos oito planetas do Sistema Solar. Ele é um planeta rochoso, parecido com a Terra em sua composição geral, mas possui uma superfície cheia de crateras. Como está muito perto do Sol, sua superfície recebe uma grande quantidade de energia solar.",
            
            "Mercúrio completa uma volta ao redor do Sol em apenas 88 dias terrestres. Porém, isso não significa que seus dias sejam curtos: ele gira lentamente em torno de seu próprio eixo. A temperatura de sua superfície também varia bastante entre regiões iluminadas pelo Sol e regiões que estão na escuridão.",
            
            "Uma curiosidade é que Mercúrio não é o planeta mais quente do Sistema Solar. Esse título pertence a Vênus, principalmente por causa de sua atmosfera muito espessa. Mercúrio, por outro lado, possui uma atmosfera extremamente fina, chamada de exosfera."
        ],

        "Vênus": [
            "Vênus é o segundo planeta a partir do Sol e tem tamanho parecido com o da Terra, por isso às vezes é chamado de planeta irmão da Terra. Apesar dessa semelhança de tamanho, os dois mundos são muito diferentes. Vênus possui uma atmosfera extremamente espessa formada principalmente por dióxido de carbono.",
            
            "Essa atmosfera provoca um forte efeito estufa. O calor recebido do Sol fica preso próximo à superfície, fazendo de Vênus o planeta mais quente do Sistema Solar. A temperatura na superfície é tão alta que pode derreter alguns metais.",
            
            "Uma curiosidade interessante é que Vênus gira ao contrário da maioria dos planetas do Sistema Solar. Além disso, ele gira tão lentamente que seu dia, medido em relação às estrelas, dura mais tempo do que seu ano."
        ],

        "Terra": [
            "A Terra é o terceiro planeta a partir do Sol e, até onde sabemos, é o único lugar do Universo onde existe vida confirmada. Ela possui água líquida em grande quantidade, uma atmosfera adequada para a vida e temperaturas que permitem a existência de diferentes ambientes.",
            
            "A Terra gira em torno de seu próprio eixo, produzindo a sucessão entre dia e noite, e também realiza uma órbita ao redor do Sol. Seu eixo de rotação é inclinado, e essa inclinação está relacionada às estações do ano.",
            
            "Uma das coisas mais interessantes sobre a Terra é que ela faz parte de um sistema muito maior. Nosso planeta está dentro do Sistema Solar, que está dentro da Via Láctea, uma galáxia que contém uma enorme quantidade de estrelas."
        ],

        "Marte": [
            "Marte é o quarto planeta a partir do Sol e é conhecido como planeta vermelho por causa dos minerais ricos em ferro presentes em sua superfície. Ele é um planeta rochoso e possui montanhas, vales, crateras e regiões que mostram sinais de que água líquida existiu em sua superfície no passado.",
            
            "A atmosfera de Marte é muito mais fina que a da Terra e é composta principalmente por dióxido de carbono. Marte também possui calotas polares formadas principalmente por gelo de água e dióxido de carbono congelado.",
            
            "Marte é um dos principais alvos das missões espaciais porque os cientistas querem descobrir mais sobre sua história e saber se ele já teve condições favoráveis à existência de vida microscópica no passado."
        ],

        "Júpiter": [
            "Júpiter é o maior planeta do Sistema Solar e pertence ao grupo dos gigantes gasosos. Ele é formado principalmente por hidrogênio e hélio e não possui uma superfície sólida como a Terra. Seu tamanho é tão grande que todos os outros planetas poderiam ser colocados dentro dele em um modelo de comparação de volume.",
            
            "Júpiter possui uma atmosfera cheia de nuvens e tempestades. Uma das estruturas mais famosas é a Grande Mancha Vermelha, uma gigantesca tempestade observada há muito tempo pelos astrônomos. O planeta também possui um sistema de anéis e muitas luas.",
            
            "Entre suas luas estão Io, Europa, Ganimedes e Calisto. Europa chama especialmente a atenção dos cientistas porque existem fortes evidências de que ela possui um oceano de água líquida abaixo de sua superfície congelada."
        ],

        "Saturno": [
            "Saturno é o sexto planeta a partir do Sol e é famoso por seu enorme sistema de anéis. Assim como Júpiter, ele é um gigante gasoso formado principalmente por hidrogênio e hélio. Seus anéis são compostos principalmente por partículas de gelo e pequenos fragmentos rochosos.",
            
            "Os anéis de Saturno não são uma única estrutura sólida. Eles são formados por uma enorme quantidade de partículas que orbitam o planeta. Algumas dessas partículas são muito pequenas, enquanto outras podem ter tamanhos muito maiores.",
            
            "Saturno também possui muitas luas. Uma das mais conhecidas é Titã, que possui uma atmosfera espessa e lagos e mares de hidrocarbonetos líquidos em sua superfície. Por isso, Titã é um dos mundos mais interessantes para a exploração espacial."
        ],

        "Urano": [
            "Urano é o sétimo planeta a partir do Sol e pertence ao grupo dos gigantes de gelo. Ele possui uma atmosfera formada principalmente por hidrogênio, hélio e metano. O metano ajuda a dar ao planeta sua aparência azul-esverdeada.",
            
            "Uma característica muito diferente de Urano é sua inclinação. Seu eixo de rotação está extremamente inclinado, fazendo com que o planeta pareça girar quase de lado enquanto realiza sua órbita ao redor do Sol.",
            
            "Urano também possui anéis e várias luas. Como está muito distante da Terra, ainda existem muitas perguntas sobre sua atmosfera, seu interior e sua formação que os cientistas continuam investigando."
        ],

        "Netuno": [
            "Netuno é o planeta mais distante do Sol entre os oito planetas do Sistema Solar. Ele também é um gigante de gelo e possui uma atmosfera composta principalmente por hidrogênio, hélio e metano. A presença de metano contribui para sua coloração azulada.",
            
            "Apesar de receber pouca energia do Sol por estar muito distante, Netuno apresenta ventos extremamente rápidos. Sua atmosfera possui grandes tempestades e estruturas que mudam com o tempo.",
            
            "Netuno também possui anéis e várias luas. Tritão é sua maior lua e possui características muito interessantes, incluindo sinais de atividade geológica. Por ser tão distante, Netuno ainda é um dos planetas menos explorados de perto."
        ],

        "Plutão": [
            "Plutão é um planeta anão localizado em uma região distante do Sistema Solar chamada Cinturão de Kuiper. Ele é muito menor que a Terra e está tão distante do Sol que recebe apenas uma pequena quantidade de luz solar.",
            
            "Mesmo sendo pequeno, Plutão possui uma paisagem surpreendentemente variada. A missão New Horizons mostrou montanhas de gelo, planícies e outras estruturas em sua superfície. Ele também possui uma atmosfera muito fina que pode mudar conforme Plutão se aproxima ou se afasta do Sol.",
            
            "Plutão deixou de ser classificado como planeta em 2006 e passou a ser considerado um planeta anão. Isso não significa que ele deixou de ser importante: estudar Plutão ajuda os cientistas a compreender melhor os objetos que existem nas regiões externas do Sistema Solar."
        ],

        "Lua": [
            "A Lua é o satélite natural da Terra e está muito mais próxima de nós do que qualquer outro corpo celeste importante. Ela não possui luz própria: o brilho que vemos durante a noite acontece porque sua superfície reflete a luz do Sol.",
            
            "A Lua realiza movimentos de rotação e de translação ao redor da Terra. O tempo que ela leva para completar uma rotação é aproximadamente igual ao tempo necessário para completar uma volta ao redor da Terra. Por isso, normalmente vemos praticamente o mesmo lado da Lua.",
            
            "A Lua também influencia as marés dos oceanos terrestres principalmente por causa de sua gravidade. Ela é o único corpo celeste, além da Terra, onde seres humanos já caminharam diretamente."
        ],

        "Sol": [
            "O Sol é uma estrela localizada no centro do Sistema Solar. Ele é uma enorme esfera de plasma extremamente quente e contém a maior parte da massa de todo o Sistema Solar. Sua gravidade mantém os planetas e outros objetos presos em órbitas ao seu redor.",
            
            "A energia do Sol é produzida em seu interior por um processo chamado fusão nuclear. Nesse processo, núcleos de hidrogênio participam de reações que liberam uma enorme quantidade de energia. Essa energia viaja pelo espaço e é fundamental para a vida na Terra.",
            
            "Apesar de parecer enorme no céu, o Sol é apenas uma das incontáveis estrelas existentes na nossa galáxia. Existem estrelas muito maiores e também muito menores que ele. Estudar o Sol ajuda os cientistas a entender melhor como outras estrelas funcionam."
        ],

        "Estrelas": [
            "Estrelas são enormes objetos celestes formados principalmente por gases muito quentes. Elas produzem sua própria energia e luz por meio de processos que acontecem em seu interior. O Sol é a estrela mais próxima da Terra.",
            
            "Durante grande parte de suas vidas, as estrelas produzem energia por meio da fusão nuclear. A massa de uma estrela influencia sua temperatura, seu brilho e também o modo como ela evolui ao longo do tempo.",
            
            "Quando estrelas muito massivas chegam ao fim de suas vidas, podem ocorrer explosões chamadas supernovas. Esses eventos podem espalhar elementos químicos pelo espaço, contribuindo para a formação de novas estrelas, planetas e outros objetos."
        ],

        "Buracos negros": [
            "Um buraco negro é uma região do espaço onde a gravidade é extremamente forte. Ele pode se formar, por exemplo, quando uma estrela muito massiva chega ao final de sua vida e seu núcleo sofre um colapso gravitacional. A região central fica extremamente compacta.",
            
            "Existe uma região chamada horizonte de eventos. Depois que algo ultrapassa esse limite, não consegue voltar para fora do buraco negro. Isso acontece porque a gravidade nessa região é tão intensa que nem mesmo a luz consegue escapar.",
            
            "Os cientistas não conseguem observar diretamente o interior de um buraco negro, mas conseguem estudar seus efeitos sobre o ambiente ao redor. Gás aquecido, estrelas próximas e ondas gravitacionais podem fornecer pistas sobre esses objetos misteriosos."
        ],

        "Exoplanetas": [
            "Exoplanetas são planetas que orbitam estrelas diferentes do Sol. Os astrônomos já descobriram milhares deles, mostrando que os sistemas planetários são muito comuns no Universo. Alguns são pequenos e rochosos, enquanto outros são gigantes gasosos.",
            
            "Uma das maneiras de descobrir um exoplaneta é observar pequenas mudanças no brilho de sua estrela. Quando o planeta passa na frente da estrela, ele pode bloquear uma pequena parte da luz. Esse método é chamado de método do trânsito.",
            
            "Uma das grandes perguntas é se algum desses mundos possui condições adequadas para a vida. Estar na chamada zona habitável pode ser interessante, mas isso não significa automaticamente que exista vida. Os cientistas precisam estudar muitos outros fatores."
        ],

        "Galáxias": [
            "Galáxias são enormes sistemas formados por estrelas, gás, poeira, planetas e outros componentes ligados principalmente pela gravidade. Existem galáxias de diferentes formas e tamanhos, como espirais, elípticas e irregulares.",
            
            "A Via Láctea é a galáxia onde está localizado o nosso Sistema Solar. Ela possui uma enorme quantidade de estrelas e também contém regiões onde novas estrelas estão nascendo. Nosso Sistema Solar fica em uma das regiões espirais da galáxia.",
            
            "Os cientistas estudam galáxias muito distantes porque observar objetos muito longe também significa observar o Universo em épocas antigas. A luz pode levar milhões ou bilhões de anos para chegar até nós."
        ],

        "Via Láctea": [
            "A Via Láctea é a galáxia que abriga o Sistema Solar. Ela é uma galáxia espiral formada por uma enorme quantidade de estrelas, além de gás, poeira e outros objetos. Quando observamos um céu muito escuro, podemos perceber uma faixa esbranquiçada atravessando o céu.",
            
            "O Sistema Solar está localizado em uma região da Via Láctea chamada Braço de Órion. Estamos muito longe do centro da galáxia. No centro da Via Láctea existe um buraco negro supermassivo chamado Sagittarius A*.",
            
            "A Via Láctea não está sozinha. Ela faz parte de um conjunto de galáxias chamado Grupo Local. A galáxia de Andrômeda é uma das grandes galáxias vizinhas e está entre os objetos mais importantes para estudar a evolução das galáxias."
        ],

        "Big Bang": [
            "O Big Bang é o nome dado ao modelo científico que descreve a evolução inicial do Universo. Ele não deve ser imaginado simplesmente como uma explosão acontecendo em um ponto vazio do espaço. A ideia principal é que o próprio Universo esteve em um estado muito mais quente e denso no passado e passou a se expandir.",
            
            "Com o passar do tempo, o Universo foi ficando mais frio e estruturas começaram a surgir. Formaram-se partículas, átomos, estrelas e galáxias. A expansão do Universo continua sendo observada atualmente.",
            
            "Uma das evidências importantes para esse modelo é a radiação cósmica de fundo, uma espécie de sinal remanescente do Universo muito jovem. Os cientistas estudam essa radiação para descobrir como o Universo era em seus primeiros momentos."
        ],

        "Matéria escura": [
            "Matéria escura é o nome dado a uma forma de matéria que não conseguimos observar diretamente pela luz. Ela não parece emitir ou refletir luz de maneira detectável, mas existem evidências de seus efeitos gravitacionais sobre outros objetos.",
            
            "Os astrônomos perceberam que algumas galáxias se movimentam de uma maneira que não pode ser explicada facilmente apenas pela matéria que conseguimos enxergar. A ideia de matéria escura ajuda a explicar esses movimentos e também outros fenômenos cosmológicos.",
            
            "Até hoje, os cientistas ainda não sabem exatamente do que a matéria escura é feita. Por isso, ela continua sendo uma das grandes perguntas da Física e da Astronomia moderna."
        ],

        "Energia escura": [
            "Energia escura é o nome usado pelos cientistas para representar algo associado à expansão acelerada do Universo. Quando os astrônomos estudaram a expansão cósmica, descobriram que ela não estava simplesmente desacelerando por causa da gravidade.",
            
            "A ideia é que existe algum componente do Universo relacionado a essa aceleração. Entretanto, energia escura não é simplesmente uma substância comum que podemos pegar ou observar diretamente.",
            
            "Ainda não sabemos exatamente o que é a energia escura. Por isso, ela é uma das grandes questões abertas da Cosmologia e é estudada por observatórios e missões espaciais."
        ],

        "Buracos de minhoca": [
            "Buracos de minhoca são estruturas hipotéticas que aparecem em algumas soluções matemáticas da Física. Eles são imaginados como possíveis caminhos que conectariam regiões diferentes do espaço-tempo, como se fossem uma espécie de atalho.",
            
            "Uma maneira simples de imaginar isso é pensar em uma folha de papel. Se dois pontos estiverem muito distantes na folha, podemos aproximá-los dobrando o papel. Um buraco de minhoca seria uma ideia matemática parecida, mas aplicada à geometria do espaço-tempo.",
            
            "É importante lembrar que nunca observamos um buraco de minhoca na natureza. Portanto, eles continuam sendo uma possibilidade teórica estudada pela Física, e não objetos astronômicos comprovadamente existentes."
        ],

        "Colisões planetárias": [
            "Colisões entre corpos do Sistema Solar realmente podem acontecer. Durante a formação dos planetas, muitos objetos rochosos colidiram entre si. Essas colisões ajudaram a construir os planetas que conhecemos atualmente.",
            
            "Quando dois corpos muito grandes colidem, o resultado depende de suas massas, velocidades e composição. Uma colisão pode destruir parte dos objetos, produzir enormes quantidades de fragmentos ou até formar um corpo maior.",
            
            "Os cientistas acreditam que a própria Lua pode ter surgido depois de uma grande colisão envolvendo a jovem Terra e outro corpo celeste. Essa é uma das principais hipóteses científicas para explicar a origem da Lua."
        ],

        "Supernovas": [
            "Uma supernova é um evento extremamente energético relacionado ao fim da vida de algumas estrelas. Dependendo da massa e das características da estrela, diferentes processos podem levar a uma explosão ou a uma transformação muito intensa.",
            
            "Durante uma supernova, uma enorme quantidade de energia pode ser liberada em pouco tempo. O material lançado para o espaço pode conter elementos químicos que foram produzidos durante a vida da estrela ou durante a própria explosão.",
            
            "Esses eventos são importantes para o Universo porque ajudam a espalhar elementos químicos pelo espaço. Muitos elementos presentes em planetas e seres vivos tiveram sua origem em estrelas que viveram antes do nascimento do nosso Sistema Solar."
        ],

        "Estrelas de nêutrons": [
            "Uma estrela de nêutrons é um objeto extremamente compacto que pode surgir depois do colapso de uma estrela massiva. Ela possui uma quantidade enorme de massa concentrada em uma região relativamente pequena.",
            
            "A matéria dentro de uma estrela de nêutrons está submetida a condições extremas. Esses objetos possuem campos gravitacionais e magnéticos muito intensos, tornando-os importantes laboratórios naturais para estudar a Física.",
            
            "Algumas estrelas de nêutrons giram rapidamente e emitem feixes de radiação. Quando esses feixes passam pela direção da Terra de maneira regular, podemos observar um objeto chamado pulsar."
        ],

        "Asteroides": [
            "Asteroides são corpos rochosos ou metálicos que orbitam o Sol. Muitos deles estão concentrados no cinturão de asteroides localizado entre Marte e Júpiter, embora existam asteroides em várias regiões do Sistema Solar.",
            
            "Os asteroides são restos importantes da formação do Sistema Solar. Por isso, estudá-los ajuda os cientistas a descobrir como era o ambiente que existia há bilhões de anos, quando os planetas estavam se formando.",
            
            "Alguns asteroides passam relativamente perto da órbita da Terra. Os cientistas acompanham esses objetos para compreender suas trajetórias e avaliar possíveis riscos no futuro."
        ],

        "Cometas": [
            "Cometas são corpos formados principalmente por gelo, poeira e materiais rochosos. Muitos deles possuem órbitas bastante alongadas e passam grande parte do tempo em regiões muito distantes do Sol.",
            
            "Quando um cometa se aproxima do Sol, seu gelo começa a aquecer e liberar gases e poeira. Isso pode formar uma atmosfera ao redor do núcleo chamada coma e também produzir uma cauda que pode ser observada da Terra.",
            
            "As caudas dos cometas não ficam simplesmente apontadas para trás durante todo o movimento. A influência do vento solar e da radiação faz com que elas geralmente apontem para longe do Sol."
        ],

        "Eclipses": [
            "Um eclipse acontece quando um corpo celeste passa de uma maneira que bloqueia ou reduz a luz recebida por outro corpo. Na Terra, podemos observar principalmente eclipses solares e lunares envolvendo o Sol, a Terra e a Lua.",
            
            "No eclipse solar, a Lua passa entre a Terra e o Sol e pode bloquear parte da luz solar para determinadas regiões da Terra. No eclipse lunar, a Terra fica entre o Sol e a Lua, fazendo com que a Lua atravesse a sombra da Terra.",
            
            "Os eclipses não acontecem todos os meses porque a órbita da Lua é inclinada em relação à órbita da Terra ao redor do Sol. É necessário que os corpos estejam alinhados de uma maneira adequada para ocorrer um eclipse."
        ],

        "Gravidade": [
            "A gravidade é uma interação que faz com que corpos com massa exerçam atração uns sobre os outros. É ela que ajuda a manter nossos pés no chão, mantém a Lua em órbita da Terra e mantém os planetas em órbita do Sol.",
            
            "Quanto maior a massa de um objeto, maior pode ser sua influência gravitacional. A distância também é importante: quanto mais afastados dois corpos estão, menor é a força gravitacional entre eles.",
            
            "A gravidade é uma das forças mais importantes para compreender o Universo. Sem ela, estrelas, planetas, luas e galáxias não poderiam formar os sistemas que observamos atualmente."
        ],

        "Teoria das cordas": [
            "A teoria das cordas é uma proposta teórica da Física que tenta descrever as partículas fundamentais como pequenos objetos semelhantes a cordas. Dependendo de como essas cordas vibrariam, diferentes propriedades poderiam aparecer.",
            
            "Uma das ideias interessantes é que a teoria das cordas tenta encontrar uma descrição que conecte diferentes partes da Física fundamental. Algumas versões também envolvem dimensões extras além das dimensões que percebemos diretamente.",
            
            "É importante destacar que a teoria das cordas ainda é uma proposta teórica e não possui confirmação experimental definitiva. Por isso, ela deve ser apresentada como uma possibilidade estudada pelos físicos, e não como uma teoria experimentalmente comprovada."
        ]
    }

    # ==========================================================
    # SE ENCONTROU UM TEMA ESPECÍFICO
    # ==========================================================

    if aspectos:
        tema_principal = aspectos[0]

        if tema_principal in respostas:
            paragrafos = respostas[tema_principal]

            # Garante EXATAMENTE 3 PARÁGRAFOS
            return "\n\n".join(paragrafos[:3])

    # ==========================================================
    # RESPOSTA PARA PERGUNTAS SOBRE CURIOSIDADES
    # ==========================================================

    if any(
        palavra in pergunta_lower
        for palavra in [
            "curiosidade",
            "curiosidades",
            "fato interessante",
            "coisa interessante",
            "sabia que"
        ]
    ):
        return (
            "O Universo é cheio de coisas surpreendentes. Existem planetas com temperaturas extremas, estrelas muito maiores que o Sol, galáxias contendo bilhões de estrelas e objetos tão densos que possuem gravidade extremamente forte. A Astronomia estuda justamente esses objetos e fenômenos para tentar entender como o Universo funciona.",
            
            "Uma das coisas mais legais da Astronomia é que podemos estudar objetos que estão muito longe da Terra. Os telescópios conseguem captar a luz desses objetos e, analisando essa luz, os cientistas conseguem descobrir informações sobre temperatura, composição química, movimento, distância e até sobre a história desses objetos.",
            
            "E existe uma curiosidade ainda maior: quando olhamos para objetos muito distantes, estamos olhando para o passado. A luz demora para viajar pelo espaço, então uma galáxia localizada a milhões de anos-luz pode ser observada como ela era há milhões de anos. Dessa forma, os telescópios também funcionam como uma espécie de máquina do tempo astronômica."
        )

    # ==========================================================
    # RESPOSTA GENÉRICA COM BASE NA PESQUISA
    # ==========================================================

    textos_pesquisa = []

    for fonte in resultados:
        texto = fonte.get("texto", "").strip()

        if texto:
            textos_pesquisa.append(texto)

    if textos_pesquisa:
        base = " ".join(textos_pesquisa[:3])

        return (
            f"A pergunta está relacionada à Astronomia e envolve um fenômeno ou objeto que pode ser estudado cientificamente. A Astronomia utiliza observações feitas por telescópios, sondas espaciais e outros instrumentos para descobrir como os corpos celestes se comportam. A pesquisa realizada encontrou informações relacionadas ao tema perguntado.",
            
            f"De maneira simples, podemos entender esse assunto observando como os objetos do Universo interagem entre si. A gravidade, a luz, o movimento e as características físicas dos corpos celestes ajudam os cientistas a explicar muitos dos fenômenos que observamos no céu. As informações encontradas na pesquisa também ajudam a complementar essa explicação.",
            
            f"Uma coisa muito interessante é que ainda existem muitas perguntas sem resposta na Astronomia. {base[:500]}"
        )

    # ==========================================================
    # FALLBACK
    # ==========================================================

    return (
        "Essa é uma pergunta interessante sobre o Universo. A Astronomia estuda planetas, estrelas, luas, galáxias, buracos negros e muitos outros objetos e fenômenos que existem no espaço. Para responder perguntas como essa, os cientistas usam observações, telescópios, sondas espaciais e modelos matemáticos.",
        
        "Mesmo quando um objeto está muito distante da Terra, podemos aprender sobre ele analisando a luz que chega até nossos telescópios. Essa luz carrega informações importantes sobre temperatura, composição, movimento e outras características do objeto observado.",
        
        "A Astronomia ainda possui muitos mistérios. Por isso, algumas perguntas já possuem respostas bastante conhecidas, enquanto outras continuam sendo investigadas pelos cientistas. É justamente isso que torna o estudo do Universo tão interessante."
    )
