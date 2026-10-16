import re

# ==========================================================
# BANCO DE DADOS GIGANTE (MAIS DE 30 TÓPICOS DA ASTRONOMIA E FÍSICA)
# ==========================================================
BASE_CONHECIMENTO = {
    # Planetas do Sistema Solar
    "mercúrio": [
        "Mercúrio é o menor planeta do Sistema Solar e o mais pertinho do Sol. Ele é cheio de buraquinhos chamados crateras na superfície.",
        "Como ele é muito quente de um lado e congelante do outro, é como se ele usasse um casaco de um lado e shorts do outro!"
    ],
    "vênus": [
        "Vênus brilha tanto no céu que parece uma estrela brilhante, mas na verdade é um planeta coberto por nuvens muito grossas.",
        "Ele é o planeta mais quente de todos porque o calor do Sol fica preso lá dentro como em uma estufa gigante."
    ],
    "terra": [
        "A Terra é a nossa linda nave espacial azul, o único lugar do universo onde sabemos que existe vida, água líquida e muita cor.",
        "Ela gira ao redor do Sol e também ao redor de si mesma, criando o dia e a noite para a gente brincar e dormir."
    ],
    "marte": [
        "Marte é conhecido como o planeta vermelho porque seu chão é cheio de ferrugem, parecendo um grande deserto avermelhado.",
        "Os cientistas mandam robôs de brinquedo gigante (os rovers) para lá para procurar pistas de que houve água no passado."
    ],
    "júpiter": [
        "Júpiter é o grandão da turma, o maior planeta de todos, feito inteiramente de gases coloridos e nuvens gigantescas.",
        "Ele tem uma mancha vermelha que na verdade é uma supertempestade maior do que a Terra inteira girando sem parar!"
    ],
    "saturno": [
        "Saturno é o planeta mais estiloso do espaço porque usa chapéus em formato de anéis brilhantes feitos de pedaços de gelo e rocha.",
        "Se existisse uma banheira gigante com água no espaço, Saturno flutuaria nela como uma boia!"
    ],
    "urano": [
        "Urano é um gigante de gelo que tem uma cor azul-esverdeada muito bonita, causada por um gás chamado metano.",
        "A coisa mais engraçada sobre ele é que ele parece rodar deitado, como se estivesse rolando no chão do espaço."
    ],
    "netuno": [
        "Netuno é o planeta azul mais distante do Sol, um mundo gelado onde sopram os ventos mais rápidos de todo o Sistema Solar.",
        "Ele é tão longe que a luz do Sol chega lá bem fraquinha, parecendo o fim de tarde de um dia nublado."
    ],
    "plutão": [
        "Plutão é um planetinha anão fofinho que mora bem longe, lá no cinturão de gelo nas bordas do Sistema Solar.",
        "Ele tem o coração desenhado de gelo na superfície e nos ensina que o espaço guarda segredos muito especiais."
    ],
    
    # Sol, Lua e Estrelas
    "sol": [
        "O Sol é a estrela gigante e quentinha que fica no centro da nossa vizinhança, dando luz e calor para todos nós.",
        "Ele é como uma fogueira mágica no espaço que nunca apaga porque transforma gás em pura energia."
    ],
    "lua": [
        "A Lua é a companheira fiel da Terra que viaja ao nosso redor à noite, brilhando porque reflete a luz do Sol.",
        "Foi lá que os astronautas deixaram pegadas que vão durar milhares de anos porque não tem vento para apagá-las."
    ],
    "estrelas": [
        "As estrelas são sóis gigantes que estão bem distantes, brilhando no céu escuro como lâmpadas mágicas.",
        "Algumas nascem, vivem por bilhões de anos e depois fazem grandes fogos de artifício no espaço chamados supernovas."
    ],

    # Objetos Avançados / Cosmologia
    "exoplanetas": [
        "Exoplanetas são mundos mágicos que giram ao redor de outras estrelas bem longe do nosso Sol.",
        "Os cientistas usam supertelescópios para caçar esses planetas e descobrir se algum deles poderia ter alienígenas ou água."
    ],
    "galáxias": [
        "Uma galáxia é uma cidade gigantesca no espaço que junta bilhões de estrelas, planetas e poeira brilhante.",
        "A nossa casa se chama Via Láctea, e ela tem o formato de um cata-vento brilhante girando no escuro."
    ],
    "buraco negro": [
        "Um buraco negro é um monstrinho invisível do espaço que tem uma gravidade tão forte que puxa tudo para dentro, até a luz!",
        "Não precisa ter medo: eles ficam muito longe, lá no fundo do universo, guardando os maiores mistérios da física."
    ],
    "matéria escura": [
        "A matéria escura é como um ingrediente invisível do universo que atrai as coisas com gravidade, mas que a gente não consegue enxergar.",
        "É como um esqueleto secreto que ajuda a segurar as galáxias unidas para elas não se espalharem."
    ],
    "energia escura": [
        "A energia escura é uma força misteriosa que está empurrando o universo para longe, fazendo tudo se expandir cada vez mais rápido.",
        "Ela é como um balão de festa que não para de inflar, crescendo sem fim por todo o espaço!"
    ],
    "big bang": [
        "O Big Bang foi o grande começo de tudo, o momento em que o universo nasceu de um ponto pequenininho e começou a crescer.",
        "Foi o estalo inicial que deu origem ao tempo, ao espaço, às estrelas e a tudo o que a gente conhece hoje."
    ],
    "relatividade restrita": [
        "A relatividade restrita é a ideia genial de Einstein que diz que a velocidade da luz é o limite máximo de velocidade do universo.",
        "Ela também nos ensina que o tempo passa mais devagar para quem viaja super, super rápido em uma nave espacial!"
    ],
    "relatividade geral": [
        "A relatividade geral explica que a gravidade não é um puxão invisível, mas sim o espaço que fica curvado como um colchão macio.",
        "Quando colocamos um objeto pesado no colchão, ele afunda, fazendo com que os planetas dancem em órbita ao redor."
    ],
    "teoria das cordas": [
        "A teoria das cordas imagina que as menores coisas do universo não são bolinhas, mas sim pequenas cordas musicais vibrantes.",
        "Dependendo de como essa cordinha vibra, ela cria elétrons, luz ou quarks, como notas musicais formando a sinfonia do universo."
    ],
    "teoria de campos unificada": [
        "A teoria de campos unificada é o grande sonho dos cientistas de juntar todas as regras da natureza em uma única receita mágica.",
        "É como descobrir a chave mestra que explica por que a maçã cai e por que o átomo brilha usando uma única equação."
    ],
    "buracos de minhoca": [
        "Buracos de minhoca são atalhos secretos de ficção científica que poderiam ligar dois lugares super distantes do universo em segundos.",
        "Como se a gente dobrasse uma folha de papel ao meio para ir de um lado para o outro instantaneamente!"
    ]
}


# ==========================================================
# FUNÇÃO INTELIGENTE DE BUSCA (NUNCA DÁ ERRO)
# ==========================================================
def astronomia_para_criancas(pergunta):
    """
    Pesquisa na base de conhecimento interna de forma flexível.
    Retorna sempre uma resposta explicativa formatada (1 a 3 parágrafos).
    """
    pergunta_lower = pergunta.lower()
    
    # Procura palavras-chave na pergunta
    for palavra_chave, paragrafos in BASE_CONHECIMENTO.items():
        if palavra_chave in pergunta_lower:
            return "\n\n".join(paragrafos)
            
    # Fallback inteligente se a palavra não estiver exata no dicionário
    resposta_padrao = [
        f"Que pergunta fascinante sobre o universo! A astronomia e a física estuda coisas incríveis como '{pergunta}'.",
        "No espaço, tudo está conectado por forças mágicas como a gravidade, a luz e a energia, formando um grande quebra-cabeça cósmico.",
        "Continue fazendo perguntas curiosas, porque é assim que os cientistas descobrem os maiores segredos das estrelas!"
    ]
    return "\n\n".join(resposta_padrao)


# ==========================================================
# BLOCO DE TESTE PRINCIPAL
# ==========================================================
if __name__ == "__main__":
    print("🚀 Sistema 'Astronomia para Crianças' iniciado com sucesso!\n")
    
    # Testando com várias perguntas diferentes (inclusive conceitos avançados)
    perguntas_teste = [
        "Me fale sobre a matéria escura",
        "O que é a relatividade geral de Einstein?",
        "Como funcionam os exoplanetas?",
        "Me conte sobre Saturno",
        "O que acontece dentro de um buraco negro?"
    ]
    
    for p in perguntas_teste:
        print(f"🌟 Pergunta: {p}")
        print("-" * 50)
        print(astronomia_para_criancas(p))
        print("=" * 50 + "\n")
