import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="CDZ: O Despertar do Cosmo - Rumo a Athena", page_icon="🌌", layout="centered")

# ==========================================
# LISTA DAS 12 CASAS DO SANTUÁRIO
# ==========================================
CASAS_SANTUARIO = [
    "1ª Casa: Templo de Áries ♈",
    "2ª Casa: Templo de Touro ♉",
    "3ª Casa: Templo de Gêmeos ♊",
    "4ª Casa: Templo de Câncer ♋",
    "5ª Casa: Templo de Leão ♌",
    "6ª Casa: Templo de Virgem ♍",
    "7ª Casa: Templo de Libra ♎",
    "8ª Casa: Templo de Escorpião ♏",
    "9ª Casa: Templo de Sagitário ♐",
    "10ª Casa: Templo de Capricórnio ♑",
    "11ª Casa: Templo de Aquário ♒",
    "12ª Casa: Templo de Peixes ♓",
    "🏛️ Salão do Mestre / Templo de Athena 🏛️"
]

def obter_nome_casa(num_casa):
    # Garante que não ultrapasse o índice máximo da lista
    idx = min(num_casa, len(CASAS_SANTUARIO) - 1)
    return CASAS_SANTUARIO[idx]

# ==========================================
# INICIALIZAÇÃO DO ESTADO GLOBAL
# ==========================================
if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False
if "indice_pergunta" not in st.session_state:
    st.session_state.indice_pergunta = 0
if "equipe_sub_idx" not in st.session_state:
    st.session_state.equipe_sub_idx = 0  # 0: Alfa, 1: Beta, 2: Gama
if "casas_alfa" not in st.session_state:
    st.session_state.casas_alfa = 0
if "casas_beta" not in st.session_state:
    st.session_state.casas_beta = 0
if "casas_gama" not in st.session_state:
    st.session_state.casas_gama = 0
if "ultimo_feedback" not in st.session_state:
    st.session_state.ultimo_feedback = None
if "historico_professor" not in st.session_state:
    st.session_state.historico_professor = []
if "prof_logado" not in st.session_state:
    st.session_state.prof_logado = False

# ==========================================
# BANCO DE 50 QUESTÕES COM GABARITO BALANCEADO (A, B, C, D, E)
# ==========================================
if "banco_50" not in st.session_state:
    guias = [
        "Seiya de Pégaso", "Shiryu de Dragão", "Hyoga de Cisne", "Shun de Andrômeda", "Ikki de Fênix",
        "Mu de Áries", "Shaka de Virgem", "Aioria de Leão", "Dohko de Libra", "Camus de Aquário"
    ]
    
    dados_brutos = [
        # Bloco A (10 Questões)
        ("O astrofísico e padre belga Georges Lemaître foi o primeiro a propor que o universo começou a partir de um 'átomo primordial'. Décadas depois, astrônomos confirmaram a expansão cósmica.",
         "Georges Lemaître",
         "O que postula o modelo cosmológico do Big Bang sobre a origem do Universo?",
         ["A expansão métrica do espaço a partir de um estado inicial de altíssima densidade e temperatura.",
          "O universo surgiu estático, eterno e sem alterações temporais.",
          "As galáxias formaram-se de colisões de buracos negros estáticos.",
          "O universo expande-se porque estrelas criam matéria do nada.",
          "A origem cósmica é cíclica ocorrendo exatamente a cada 100 anos."], "A",
         "O Big Bang descreve a expansão do espaço a partir de um estado inicial denso e quente."),

        ("Na década de 1920, Edwin Hubble analisou a luz enviada por galáxias distantes e notou o estiramento das ondas de luz.",
         "Edwin Hubble",
         "Qual é a principal evidência observacional da expansão contínua do Universo?",
         ["O desvio para o vermelho (redshift) das galáxias distantes, formulado na Lei de Hubble.",
          "A colisão frequente de planetas no sistema solar interior.",
          "O resfriamento rápido do Sol observado por telescópios modernos.",
          "A ausência completa de radiação no espaço interestelar.",
          "A rotação estática das estrelas fixas na esfera celeste."], "A",
         "O redshift demonstra que as ondas de luz esticam devido à expansão do próprio espaço."),

        ("Em 1964, Penzias e Wilson detectaram um ruído de fundo persistente vindo de todas as direções do céu.",
         "Arno Penzias e Robert Wilson",
         "O que representa a Radiação Cósmica de Fundo em Micro-ondas (CMB)?",
         ["O eco térmico remanescente dos primeiros momentos do Big Bang.",
          "A energia gerada por supernovas na Via Láctea.",
          "O calor emitido por buracos negros supermassivos.",
          "Interferência de rádio alienígena captada por antenas.",
          "Luz refletida pela poeira interstelatória."], "A",
         "A CMB é a radiação fóssil do universo primordial captada em todas as direções."),

        ("A relação matemática entre a distância de uma galáxia e sua velocidade de afastamento determina uma taxa proporcional.",
         "Edwin Hubble e Georges Lemaître",
         "O que mede a Constante de Hubble?",
         ["A taxa atual de expansão do universo por unidade de distância.",
          "A velocidade com que a Terra gira em torno do seu próprio eixo.",
          "A distância exata entre a Terra e o centro da galáxia.",
          "A massa total de hidrogênio presente no cosmos.",
          "A força da gravidade na superfície do Sol."], "A",
         "Quantifica a velocidade de afastamento das galáxias em função de sua distância."),

        ("O Princípio Cosmológico estabelece propriedades fundamentais para o universo em grande escala.",
         "Alexander Friedmann",
         "O que significa dizer que o universo é homogêneo e isotrópico?",
         ["Que ele possui a mesma aparência em qualquer lugar (homogêneo) e em todas as direções (isotrópico).",
          "Que ele é totalmente plano e feito de ferro puro.",
          "Que todas as estrelas possuem exatamente a mesma idade e tamanho.",
          "Que o universo possui um centro fixo e bem definido no espaço.",
          "Que a temperatura é zero absoluto em todo o cosmo."], "A",
         "Homogêneo indica igualdade de densidade em larga escala e isotrópico indica ausência de direção privilegiada."),

        ("Durante o eclipse solar de 1919, astrônomos fotografaram estrelas próximas ao Sol em Sobral (Brasil) e Príncipe.",
         "Arthur Eddington e Albert Einstein",
         "O que foi o eclipse solar de 1919 que consagrou a Relatividade Geral?",
         ["A observação de que a luz estelar sofre desvio ao passar perto do Sol devido à curvatura do espaço.",
          "A prova irrefutável de que a Lua é feita de rochas vulcânicas escuras.",
          "O escurecimento do universo causado por um halo de matéria escura.",
          "A colisão do Sol com um buraco negro de massa intermediária.",
          "A medição da velocidade do som na atmosfera terrestre."], "A",
         "O desvio da luz estelar confirmou a curvatura da geometria do espaço-tempo prevista por Einstein."),

        ("Cem anos após a previsão de Einstein, observatórios detectaram oscilações reais no tecido do espaço-tempo.",
         "Colaboração LIGO e VIRGO",
         "O que são Ondas Gravitacionais?",
         ["Perturbações no tecido do espaço-tempo geradas por eventos violentos como a fusão de buracos negros.",
          "Ondas sonoras de alta frequência viajando no vácuo intergaláctico.",
          "Ondas de rádio emitidas por pulsares em rotação rápida.",
          "Raios cósmicos de alta energia vindos do centro galáctico.",
          "Marés oceânicas geradas pela atração gravitacional da Lua."], "A",
         "Ondas gravitacionais são marés na própria geometria do espaço-tempo geradas por aceleração de massas extremas."),

        ("Vera Rubin mediu a rotação de estrelas em galáxias espirais e notou algo inesperado nas bordas externas.",
         "Vera Rubin e Kent Ford",
         "Qual é a função da Matéria Escura na estruturação cósmica?",
         ["Atuar como cola gravitacional invisível mantendo as galáxias coesas em alta velocidade.",
          "Emitir luz intensa para iluminar as regiões mais escuras do espaço.",
          "Acelerar a expansão do universo para longe de nós.",
          "Proteger os planetas contra radiação gama destrutiva.",
          "Absorver buracos negros antigos no centro das galáxias."], "A",
         "A matéria visível não tem massa suficiente; a matéria escura fornece a atração gravitacional extra que segura as galáxias."),

        ("A cosmologia moderna distingue dois componentes invisíveis que dominam a dinâmica do cosmos.",
         "Saul Perlmutter e Brian Schmidt",
         "Qual a diferença fundamental entre Matéria Escura e Energia Escura?",
         ["A matéria escura atrai (gravidade), enquanto a energia escura repele (acelera a expansão).",
          "Ambas fazem exatamente a mesma coisa na estrutura cósmica.",
          "A energia escura é visível em telescópios, enquanto a matéria escura é invisível.",
          "A matéria escura acelera o universo para fora, enquanto a energia escura o comprime.",
          "Não há diferença teórica entre ambas segundo a física moderna."], "A",
         "A matéria escura atua via atração gravitacional e a energia escura impulsiona a expansão acelerada."),

        ("Estudos com supernovas do Tipo Ia em 1998 surpreenderam a comunidade científica mundial.",
         "Saul Perlmutter, Brian Schmidt e Adam Riess",
         "O que provou que a expansão do universo está acelerando?",
         ["A medição do brilho de supernovas distantes do tipo Ia.",
          "O cálculo da distância exata entre a Terra e a Lua.",
          "A colisão iminente entre a Via Láctea e Andrômeda.",
          "A medição do campo magnético da Terra por satélites.",
          "Experimentos de laboratório com feixes de laser no vácuo."], "A",
         "Supernovas distantes pareciam mais fracas do que o esperado, provando que a expansão acelerou com a energia escura."),

        # Bloco B (10 Questões)
        ("Físicos usam a analogia da borracha de um balão sendo inflada para explicar o movimento galáctico.",
         "Didática de Física",
         "Como a analogia do balão de festa preenchendo ar ajuda a entender a expansão do universo?",
         ["Mostra que o balão cria ar novo em seu interior à medida que cresce.",
          "Ilustra como os pontos na superfície se afastam porque o próprio espaço da borracha se expande.",
          "Comprova que o centro do balão é a única parte que se move no espaço.",
          "Indica que o universo possui paredes rígidas que contêm o calor.",
          "Demonstra que a luz viaja mais rápido do que o som no vácuo."], "B",
         "As galáxias não correm pelo espaço; é o tecido do espaço que se estica entre elas."),

        ("Cerca de 380 mil anos após o Big Bang, prótons e elétrons formaram átomos neutros.",
         "George Gamow",
         "O que foi a Era da Recombinação nos instantes iniciais do Big Bang?",
         ["O momento em que os buracos negros engoliram toda a matéria circundante.",
          "O período em que prótons e elétrons uniram-se em átomos neutros, permitindo que a luz viajasse livremente.",
          "A colisão violenta entre a Via Láctea e a galáxia de Andrômeda.",
          "A fase em que a força da gravidade deixou de existir no universo.",
          "O congelamento absoluto de todas as partículas do cosmos."], "B",
         "Com a recombinação, os fótons desacoplaram-se da matéria e a luz pôde se propagar livremente."),

        ("Pontos de densidade extrema são previstos pelas equações da gravidade relativística.",
         "Stephen Hawking e Roger Penrose",
         "O que caracteriza uma singularidade no contexto cosmológico?",
         ["Um planeta com formato perfeitamente esférico no espaço.",
          "Um estado de densidade e temperatura infinitas onde as leis físicas conhecidas deixam de funcionar.",
          "Uma estrela hipergigante que brilha mais que um milhão de sóis.",
          "O ponto exato onde a Terra orbita em volta do Sol.",
          "Um cometa solitário que cruza o sistema solar uma única vez."], "B",
         "Na singularidade, grandezas físicas atingem valores infinitos antes da expansão."),

        ("A física moderna compreende que o tecido do espaço e o tempo surgiram juntos.",
         "Albert Einstein e Alexander Friedmann",
         "Antes do Big Bang, o que existia segundo a cosmologia padrão?",
         ["Um vasto oceano de estrelas congeladas e estáticas.",
          "O espaço e o tempo não existiam da forma atual, estando toda matéria concentrada em uma singularidade.",
          "Um vácuo infinito repleto de galáxias espirais em repouso.",
          "Um buraco negro colossal que engolia todos os planetas.",
          "Matéria escura espalhada sob a forma de gás frio."], "B",
         "O próprio espaço e o tempo surgiram com o evento do Big Bang, não havendo um 'antes' convencional."),

        ("Karl Schwarzschild definiu o raio crítico em torno de massas altamente concentradas.",
         "Karl Schwarzschild",
         "O que é o Horizonte de Eventos em astrofísica?",
         ["A borda visível da superfície de um planeta rochoso.",
          "O limite ao redor de um buraco negro além do qual nada, nem mesmo a luz, pode escapar.",
          "O limite onde o vento solar deixa de afetar os cometas.",
          "A distância máxima que um telescópio óptico consegue enxergar.",
          "O momento exato em que uma estrela massiva se transforma em supernova."], "B",
         "O horizonte de eventos marca o limite de onde a velocidade de escape supera a velocidade da luz."),

        ("Alan Guth propôs um mecanismo para explicar a homogeneidade de temperatura do cosmos.",
         "Alan Guth",
         "O que foi a Teoria da Inflação Cósmica?",
         ["A expansão lenta e gradual das estrelas ao longo de bilhões de anos.",
          "Um período de expansão exponencial ultrarrápida ocorrido logo após o Big Bang.",
          "O aumento gradual do brilho de supernovas distantes.",
          "A inflação da massa dos buracos negros em galáxias ativas.",
          "A expansão do vento solar pelo meio interestelar."], "B",
         "A inflação cósmica expandiu o universo em um fator colossal numa fração de segundo."),

        ("Quando uma fonte de luz se afasta do observador, suas ondas chegam esticadas.",
         "Christian Doppler e Vesto Slipher",
         "Por que a luz de galáxias distantes sofre o desvio para o vermelho (redshift)?",
         ["Porque as estrelas estão esfriando e emitindo luz avermelhada.",
          "Porque o comprimento de onda da luz é esticado pela expansão do espaço entre nós e a galáxia.",
          "Porque existe poeira e fumaça cósmica bloqueando a luz azul.",
          "Devido à rotação rápida da Terra em torno do seu próprio eixo.",
          "Porque as galáxias vermelhas são muito mais antigas."], "B",
         "O estiramento do espaço estica o comprimento de onda dos fótons rumo ao vermelho."),

        ("Em 1915, Albert Einstein revolucionou nossa visão sobre a gravidade.",
         "Albert Einstein",
         "Segundo a Relatividade Geral de Einstein, como a gravidade é explicada?",
         ["Como uma atração magnética direta entre corpos com massa.",
          "Como a curvatura do tecido do espaço-tempo provocada pela presença de massa e energia.",
          "Como o atrito gerado pelo vento cósmico nas galáxias.",
          "Como uma ilusão óptica sem nenhuma consequência física real.",
          "Como partículas quânticas que empurram os objetos para baixo."], "B",
         "Massa e energia dizem ao espaço-tempo como se curvar, e o espaço-tempo diz à matéria como se mover."),

        ("A Relatividade Geral prevê alterações no ritmo dos relógios sob gravidade ou velocidade.",
         "Albert Einstein",
         "O que acontece com a passagem do tempo em campos gravitacionais muito intensos?",
         ["O tempo passa mais rápido para o observador submetido ao campo.",
          "O tempo desacelera (dilatação temporal) em relação a um observador distante.",
          "O tempo para completamente e nunca mais avança no universo.",
          "O tempo passa a correr de trás para frente instantaneamente.",
          "Não há alteração alguma na contagem temporal do sistema."], "B",
         "A dilatação temporal é uma consequência direta e comprovada da física de Einstein."),

        ("Satélites de GPS orbitam a Terra a alta velocidade e a milhares de quilômetros de altitude.",
         "Engenharia Relativística",
         "O que a Relatividade prevê sobre os relógios dos satélites GPS?",
         ["Que eles marcam exatamente o mesmo tempo que os relógios na superfície.",
          "Que eles necessitam de ajustes relativísticos de tempo devido à velocidade e gravidade para garantir precisão.",
          "Que eles param de funcionar devido ao frio extremo do espaço.",
          "Que eles aceleram tanto que se quebram em poucos dias.",
          "Que o tempo neles passa imensamente mais devagar que na Terra."], "B",
         "Sem correções relativísticas diárias, o sistema GPS acumularia erros de quilômetros por dia."),

        # Bloco C (10 Questões)
        ("Nos primeiros três minutos de existência do universo, a temperatura permitiu a fusão nuclear.",
         "Fred Hoyle e Ralph Alpher",
         "Qual elemento químico leve foi predominantemente formado na nucleossíntese primordial?",
         ["Ouro e Platina em grande escala.",
          "Urânio e Plutônio superaquecidos.",
          "Hidrogênio e Hélio em vasta abundância.",
          "Ferro e Níquel no núcleo das estrelas.",
          "Silício e Carbono na poeira cósmica."], "C",
         "Formaram-se primordialmente núcleos de hidrogênio (~75%) e hélio (~25%) nos primeiros minutos."),

        ("A composição total de massa e energia do universo foi mapeada pela missão espacial Planck.",
         "Missão Espacial Planck (ESA)",
         "Qual é a proporção aproximada no universo entre Energia Escura, Matéria Escura e Matéria Ordinária?",
         ["50% matéria visível, 30% matéria escura e 20% energia escura.",
          "90% matéria ordinária, 5% matéria escura e 5% energia escura.",
          "Cerca de 68% energia escura, 27% matéria escura e apenas 5% de matéria ordinária.",
          "99% matéria escura e 1% de todo o resto do cosmos.",
          "33% para cada uma das três categorias listadas."], "C",
         "A matéria ordinária (da qual somos feitos) corresponde a apenas ~5% do cosmos."),

        ("Medições combinadas da CMB e supernovas permitiram determinar a idade do cosmos.",
         "Equipe dos Satélites WMAP e Planck",
         "Qual é a idade estimada do nosso universo atualmente aceita pela comunidade científica?",
         ["Cerca de 6 mil anos de existência.",
          "Aproximadamente 4,5 bilhões de anos.",
          "Cerca de 13,8 bilhões de anos de evolução.",
          "Cerca de 100 bilhões de anos estáticos.",
          "Aproximadamente 500 milhões de anos."], "C",
         "A idade cosmológica aceita é de aproximadamente 13,8 bilhões de anos."),

        ("Edwin Hubble mediu as velocidades de afastamento das galáxias e formulou sua lei observacional.",
         "Edwin Hubble",
         "Qual cientista confirmou empiricamente a expansão do universo pelo desvio para o vermelho?",
         ["Isaac Newton ao estudar a gravitação universal.",
          "Galileo Galilei ao apontar o telescópio para Júpiter.",
          "Edwin Hubble ao analisar galáxias no Observatório do Monte Wilson.",
          "Johannes Kepler ao formular as leis do movimento planetário.",
          "Nikola Tesla ao estudar ondas eletromagnéticas."], "C",
         "Hubble usou o desvio para o vermelho para provar a expansão do espaço."),

        ("Einstein percebeu em um 'pensamento feliz' a relação entre aceleração e gravidade.",
         "Albert Einstein",
         "O que estabelece o Princípio da Equivalência de Einstein?",
         ["Que toda matéria no universo tem exatamente a mesma densidade.",
          "Que a gravidade é mais fraca que a força eletromagnética.",
          "Que os efeitos de um campo gravitacional são localmente indistinguíveis dos efeitos de uma aceleração constante.",
          "Que a velocidade da luz varia dependendo do movimento do observador.",
          "Que massa e energia não podem se converter uma na outra."], "C",
         "Estar acelerando no espaço em um foguete equivale a estar sob a atração de um campo gravitacional."),

        ("A união entre geometria espacial e tempo foi formulada por Minkowski.",
         "Hermann Minkowski",
         "O que representa o conceito de espaço-tempo quadridimensional?",
         ["Uma sala tridimensional acrescida de quatro paredes externas.",
          "Um holograma gerado por supercomputadores astronômicos.",
          "A união matemática das três dimensões espaciais com a dimensão temporal.",
          "O espaço que existe exclusivamente no interior de buracos negros.",
          "Dimensões paralelas invisíveis onde habitam outros universos."], "C",
         "Eventos ocorrem em coordenadas contínuas de 3 dimensões de espaço e 1 de tempo."),

        ("A relação entre massa e energia em repouso é expressa na famosa fórmula $E=mc^2$.",
         "Albert Einstein",
         "O que afirma a equivalência entre massa e energia na física relativística?",
         ["Que a massa e a energia são grandezas totalmente independentes.",
          "Que a energia viaja sempre mais devagar do que a matéria.",
          "Que massa e energia são formas equivalentes da mesma grandeza física, podendo se converter entre si.",
          "Que a massa de um corpo desaparece ao ser acelerada.",
          "Que a gravidade não possui nenhuma relação com a massa dos corpos."], "C",
         "Massa é uma forma extremamente concentrada de energia."),

        ("Ao final da vida de uma estrela massiva, seu núcleo atinge um estado denso de matéria de nêutrons.",
         "Walter Baade e Fritz Zwicky",
         "O que caracteriza uma estrela de nêutrons?",
         ["Uma estrela formada puramente de gás hidrogênio frio.",
          "Um planeta gigante gasoso que não conseguiu fundir deutério.",
          "O cadáver superdenso onde elétrons e prótons fundiram-se em nêutrons após o colapso.",
          "Uma galáxia espiral comprimida em escala menor.",
          "Uma estrela que orbita um buraco negro muito de perto."], "C",
         "Uma colher de chá de matéria de estrela de nêutrons pesaria bilhões de toneladas."),

        ("O limite máximo de velocidade no universo rege a transmissão de informação.",
         "Albert Einstein",
         "Qual é o limite máximo de velocidade para matéria e informação no universo?",
         ["A velocidade do som na atmosfera terrestre.",
          "A velocidade do vento solar no espaço interplanetário.",
          "A velocidade da luz no vácuo ($c \\approx 300.000$ km/s).",
          "Uma velocidade arbitrária de 1.000.000 km/s.",
          "Não existe nenhum limite de velocidade na física moderna."], "C",
         "Nada com massa de repouso pode atingir ou ultrapassar a velocidade da luz no vácuo."),

        ("Físicos teóricos propõem candidatos a partículas de matéria escura de interação fraca.",
         "Física de Partículas",
         "O que significa a sigla WIMP no contexto da Matéria Escura?",
         ["Waves In Microwave Pulses (Ondas em Pulsos de Micro-ondas).",
          "Wormhole Integrated Mass Plasma (Plasma Integrado de Buraco de Minhoca).",
          "Weakly Interacting Massive Particles (Partículas Massivas de Interação Fraca).",
          "Water Isotope Molecular Process (Processo Molecular de Isótopos de Água).",
          "White Dwarf Interstellar Matter Photon (Fóton de Matéria Interestelar)."], "C",
         "WIMPs são partículas hipotéticas massivas que interagem apenas via gravidade e força fraca."),

        # Bloco D (10 Questões)
        ("Grandes concentrações de massa curvam a trajetória da luz de objetos distantes atrás delas.",
         "Fritz Zwicky e Albert Einstein",
         "O que é o efeito de Lente Gravitacional?",
         ["Um óculos especial desenvolvido por astrônomos para observar o Sol.",
          "Uma lupa de cristal de quartzo colocada em órbita espacial.",
          "A luz refletida diretamente pelos anéis do planeta Saturno.",
          "A curvatura e amplificação da luz de objetos distantes provocada por massas gigantescas no caminho.",
          "O brilho emitido por estrelas binárias em colisão."], "D",
         "Grandes massas atuam como lentes ópticas naturais curvando o tecido do espaço."),

        ("Na física teórica, soluções das equações de Einstein sugerem atalhos no espaço-tempo.",
         "Albert Einstein e Nathan Rosen",
         "O que representam os Buracos de Minhoca (wormholes)?",
         ["Túneis escavados por organismos em asteroides rochosos.",
          "O interior de estrelas de nêutrons em rápida rotação.",
          "Partículas subatômicas que viajam para o passado.",
          "Atalhos hipotéticos através do espaço-tempo conectando dois pontos distantes.",
          "A fumaça expandida gerada por supernovas antigas."], "D",
         "Buracos de minhoca são pontes teóricas conectando regiões distintas do espaço-tempo."),

        ("Estrelas de nêutrons altamente magnetizadas giram rapidamente emitindo feixes de radiação.",
         "Jocelyn Bell Burnell",
         "O que são Pulsares na astrofísica observacional?",
         ["Planetas rochosos que piscam no céu noturno.",
          "Galáxias espirais que expandem e contraem ritmicamente.",
          "Cometas com órbitas caóticas ao redor de estrelas.",
          "Estrelas de nêutrons em rápida rotação que emitem feixes regulares de radiação como um farol.",
          "Aglomerados globulares de estrelas jovens e brilhantes."], "D",
         "Seus feixes de radiação varrem o espaço em intervalos regulares ultraprecisos."),

        ("O termo introduzido por Einstein para manter o universo estático ganhou novo significado.",
         "Albert Einstein",
         "O que é a Constante Cosmológica ($\Lambda$)?",
         ["A velocidade exata da luz no vácuo.",
          "O peso de um átomo de hidrogênio no espaço.",
          "A taxa de rotação do Sol em torno de seu eixo.",
          "Um termo matemático associado à densidade de energia do vácuo que impulsiona a expansão.",
          "A distância exata entre a Terra e a Galáxia de Andrômeda."], "D",
         "Hoje a constante cosmológica representa a energia do vácuo associada à energia escura."),

        ("Galáxias e matéria no universo distribuem-se em uma grande rede tridimensional.",
         "Simulações Cosmológicas de N-Corpos",
         "Qual é o papel dos Filamentos Cósmicos na teia do universo?",
         ["Conectar os computadores da NASA aos telescópios espaciais.",
          "Conduzir raios solares diretamente entre os sistemas planetários.",
          "Servir de trilho para a passagem de cometas interestelares.",
          "Formar pontes densas de matéria (visível e escura) que cercam vastos vazios cósmicos.",
          "Emitir feixes de luz branca constante pelo espaço."], "D",
         "Os filamentos concentram a maior parte da matéria do cosmos organizando a teia cósmica."),

        ("Entre os filamentos densos da teia cósmica existem imensas regiões de baixa densidade.",
         "Mapeamento Cosmológico do Espaço Profundo",
         "O que são os Vazios Cósmicos (Cosmic Voids)?",
         ["Regiões onde o tempo para completamente segundo a relatividade.",
          "O centro exato de cada buraco negro supermassivo.",
          "O espaço vazio existente no interior de um átomo.",
          "Enormes regiões do espaço com baixíssima densidade de galáxias entre os filamentos.",
          "Regiões totalmente desprovidas de qualquer partícula de matéria escura."], "D",
         "Os vazios cósmicos ocupam a maior parte do volume do universo observável."),

        ("Partículas elementares hipotéticas leves foram propostas para resolver problemas da física forte.",
         "Roberto Peccei e Helen Quinn",
         "O que são Axions nas pesquisas sobre Matéria Escura?",
         ["Raios gama emitidos durante a explosão de estrelas jovens.",
          "A menor unidade temporal calculada pela física quântica.",
          "A composição química dos anéis de poeira de Júpiter.",
          "Partículas elementares hipotéticas de baixa massa consideradas candidatas à matéria escura.",
          "O nome dado ao fluxo de energia escura pura."], "D",
         "Axions são partículas leves e neutras pesquisadas por detectores de alta sensibilidade."),

        ("Simulações computacionais de N-corpos ajudam a entender a evolução gravitacional do universo.",
         "Supercomputação Cosmológica",
         "Como as simulações computacionais de N-corpos auxiliam a cosmologia?",
         ["Prevendo a meteorologia diária da Terra com precisão.",
          "Traduzindo sinais hipotéticos de rádio vindo de outras estrelas.",
          "Desenhando mapas estelares bidimensionais para navegação.",
          "Simulando a gravidade de milhões de partículas para recriar a evolução da teia cósmica.",
          "Calculando a órbita exata da Lua em relação à Terra."], "D",
         "Elas mostram como flutuações primordiais evoluíram para a estrutura de galáxias atual."),

        ("Modelos cosmológicos indicam o destino de longo prazo do cosmos sob a energia escura.",
         "Cosmologia do Futuro",
         "Qual é o destino final mais provável do universo segundo os dados atuais?",
         ["O Big Crunch (colapso de toda a matéria de volta a um ponto).",
          "Uma grande explosão de luz branca constante em todas as galáxias.",
          "A transformação de todas as estrelas em buracos brancos.",
          "A expansão eterna acelerada (Big Freeze), tornando o universo cada vez mais frio e disperso.",
          "A reversão espontânea do fluxo do tempo."], "D",
         "A aceleração causada pela energia escura caminha para o resfriamento e dispersão eterna."),

        ("Satélites de alta precisão mapearam as flutuações de radiação fóssil do universo jovem.",
         "Agência Espacial Europeia (ESA)",
         "O que foi a missão do telescópio espacial Planck da ESA?",
         ["Uma missão espacial tripulada enviada à superfície de Marte.",
          "Um acelerador de partículas subterrâneo construído na Europa.",
          "O primeiro satélite construído para entrar na atmosfera do Sol.",
          "Um telescópio que mapeou com alta precisão as flutuações da Radiação Cósmica de Fundo.",
          "Um estudo robótico sobre a atmosfera densa do planeta Vênus."], "D",
         "O Planck forneceu os dados mais precisos sobre a idade e composição do cosmos."),

        # Bloco E (10 Questões)
        ("A energia do vácuo possui propriedades distintas da matéria ordinária durante a expansão.",
         "Física do Vácuo Quântico",
         "Por que a Energia Escura não se dilui à medida que o universo se expande?",
         ["Porque ela é fabricada continuamente pelo núcleo de estrelas massivas.",
          "Porque possui massa negativa infinita que repele a gravidade.",
          "Porque ela viaja mais rápido do que a própria luz pelo espaço.",
          "Porque ela interage fortemente com os horizontes de buracos negros.",
          "Porque é uma propriedade do próprio vácuo; quanto mais o espaço expande, mais energia do vácuo existe."], "E",
         "A densidade de energia do vácuo permanece constante por unidade de volume."),

        ("Telescópios modernos encontram divergências sutis na medição da taxa de expansão cósmica.",
         "Cosmologia Observacional Moderna",
         "O que os cientistas chamam de 'Crise na Cosmologia' recente?",
         ["A falta de verbas públicas para o financiamento de pesquisas espaciais.",
          "O esgotamento completo do gás hidrogênio nas galáxias vizinhas.",
          "A colisão iminente entre a Via Láctea e buracos negros próximos.",
          "A impossibilidade técnica de utilizar computadores na astronomia.",
          "A divergência entre as medições da Constante de Hubble no universo local e no universo primordial."], "E",
         "Essa discrepância entre dados locais e primordiais desafia os modelos atuais."),

        ("O objetivo central da jornada dos aspirantes através do Santuário une ciência e espírito.",
         "Ensinamento Supremo de Athena",
         "Ao final desta jornada pelo Santuário, o que os novos Cavaleiros compreendem sobre o Cosmo?",
         ["Que o cosmo é apenas uma ilusão sem nenhuma lei física real.",
          "Que a força física bruta é a única coisa que resolve uma batalha.",
          "Que a ciência e a mitologia são totalmente incompatíveis.",
          "Que o universo foi construído por um vilão cósmico.",
          "Que o verdadeiro cosmo une o poder interior à compreensão racional das leis do universo."], "E",
         "O verdadeiro domínio do cosmo une a elevação espiritual ao conhecimento científico."),

        ("Medições da rotação de galáxias espirais demonstraram a presença de massa invisível nos halos.",
         "Vera Rubin e Fritz Zwicky",
         "O que as curvas de rotação das galáxias espirais revelaram sobre a massa galáctica?",
         ["Que a massa está concentrada unicamente no núcleo brilhante.",
          "Que as galáxias estão totalmente paradas no espaço intergaláctico.",
          "Que a força da gravidade diminui a zero na borda das galáxias.",
          "Que todas as galáxias possuem buracos negros gêmeos no centro.",
          "Que as estrelas periféricas giram rápido demais, indicando a presença de um halo invisível de matéria escura."], "E",
         "As estrelas periféricas giram a velocidades altas que exigem massa invisível extra para não se dispersarem."),

        ("A matéria escura recebeu esse nome devido às suas propriedades de interação eletromagnética.",
         "Fritz Zwicky",
         "Por que a Matéria Escura é chamada de 'escura'?",
         ["Porque ela bloqueia a luz como tinta preta no espaço.",
          "Porque ela só existe nas regiões sombrias atrás dos planetas.",
          "Devido à cor escura dos rochedos dos planetas que a compõem.",
          "Porque foi descoberta durante observações noturnas de telescópio.",
          "Porque não emite, absorve ou reflete luz nem qualquer radiação eletromagnética."], "E",
         "Ela é chamada de escura porque não interage com a luz, apenas com a gravidade."),

        ("Aglomerados galácticos são formados por vastos grupos mantidos pela gravidade.",
         "Fritz Zwicky",
         "O que são Aglomerados de Galáxias na hierarquia das estruturas do cosmos?",
         ["Estrelas solitárias vagando no espaço intergaláctico.",
          "Anéis de poeira e rochas orbitando ao redor do Sol.",
          "Nuvens de gás frio desprovidas de qualquer estrela.",
          "Sistemas planetários em rotação caótica ao redor de pulsares.",
          "Vastas estruturas de centenas ou milhares de galáxias mantidas juntas pela atração gravitacional."], "E",
         "Aglomerados galácticos são as maiores estruturas unidas pela gravidade."),

        ("Na física do espaço-tempo, objetos massivos alteram a trajetória de corpos em movimento.",
         "Albert Einstein",
         "O que significa dizer que o espaço é dinâmico na Relatividade Geral?",
         ["Que ele muda de cor dependendo das estações do ano.",
          "Que ele possui correntes de ar invisíveis soprando no vácuo.",
          "Que ele se move de leste para oeste junto com a Terra.",
          "Que ele possui fricção mecânica que desacelera os planetas.",
          "Que o espaço não é um palco imóvel, mas um meio flexível que se curva, vibra e expande."], "E",
         "O tecido do espaço-tempo molda-se e reage ativamente à presença de matéria e energia."),

        ("A luz não consegue escapar do interior do horizonte de eventos de um buraco negro.",
         "John Wheeler e Karl Schwarzschild",
         "Por que a luz não consegue escapar de um buraco negro supermassivo?",
         ["Porque a luz desliga sua energia ao se aproximar do centro.",
          "Porque o buraco negro possui um campo magnético que repele fótons.",
          "Porque a luz é mais pesada do que a matéria do buraco negro.",
          "Porque o vácuo ao redor absorve toda a cor da luz.",
          "Porque a curvatura do espaço-tempo é tão extrema que todos os caminhos possíveis apontam para o centro."], "E",
         "A geometria do espaço fica curvada de forma que todas as trajetórias futuras levam à singularidade."),

        ("A expansão exponencial ultrarrápida do cosmos primordial resolveu dilemas clássicos.",
         "Alan Guth",
         "Qual problema clássico da cosmologia foi resolvido pela Teoria da Inflação Cósmica?",
         ["A origem da cor vermelha do planeta Marte.",
          "O motivo pelo qual a Lua sempre mostra a mesma face para a Terra.",
          "A causa das marés oceânicas nos planetas rochosos.",
          "A falta de oxigênio no espaço interplanetário.",
          "O problema do horizonte e da planura, explicando a homogeneidade da temperatura da CMB."], "E",
         "A inflação expandiu regiões em equilíbrio térmico antes que perdessem contato causa-efeito."),

        ("A busca por compreender o Big Bang combina física teórica e observações astronômicas.",
         "Georges Lemaître e Albert Einstein",
         "Qual é a importância pedagógica do estudo da cosmologia moderna?",
         ["Apenas memorizar fórmulas matemáticas sem aplicação real.",
          "Substituir o método científico por especulações fantásticas.",
          "Provar que a Terra é o centro imóvel de todo o universo.",
          "Demonstrar que a física não consegue explicar o mundo natural.",
          "Compreender a origem, evolução e leis fundamentais que regem o tecido do espaço-tempo."], "E",
         "A cosmologia integra a relatividade, mecânica quântica e astronomia para explicar a história do universo.")
    ]

    lista_50 = []
    for i, q in enumerate(dados_brutos):
        guia = guias[i % len(guias)]
        lista_50.append({
            "guia": guia,
            "texto_base": q[0],
            "cientista": q[1],
            "enunciado": q[2],
            "opcoes_originais": q[3],
            "correta_texto": q[3][ord(q[4]) - ord('A')],
            "por_que": q[5]
        })
    st.session_state.banco_50 = lista_50

# Função para reiniciar
def reiniciar_jogo():
    st.session_state.jogo_iniciado = False
    st.session_state.indice_pergunta = 0
    st.session_state.equipe_sub_idx = 0
    st.session_state.casas_alfa = 0
    st.session_state.casas_beta = 0
    st.session_state.casas_gama = 0
    st.session_state.ultimo_feedback = None

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

st.title("🏛️ CDZ: O Despertar do Cosmo - Rumo a Athena")
st.markdown("### *Treinamento das Equipes: Domine o Cosmo, a Relatividade e o Big Bang!*")
st.markdown("---")

# ==========================================
# PAINEL DO PROFESSOR (COM LOGIN E SENHA)
# ==========================================
st.sidebar.header("👨‍🏫 Área do Professor")

with st.sidebar.expander("🔑 Acesso do Professor"):
    if not st.session_state.prof_logado:
        login_input = st.text_input("Login do Professor")
        senha_input = st.text_input("Senha", type="password")
        if st.button("Entrar no Painel"):
            if login_input == "Felipe Ferreira" and senha_input == "Ff241198":
                st.session_state.prof_logado = True
                st.success("Login efetuado com sucesso!")
                st.rerun()
            else:
                st.error("Login ou senha incorretos.")
    else:
        st.success("Sessão Ativa: **Felipe Ferreira**")
        if st.button("Sair da Conta"):
            st.session_state.prof_logado = False
            st.rerun()

# Conteúdo do Professor
if st.session_state.prof_logado:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📄 Exportar Relatório de Alunos")
    
    relatorio_txt = "====================================================\n"
    relatorio_txt += "RELATÓRIO DE RESPOSTAS DAS EQUIPES - PROFESSOR FELIPE FERREIRA\n"
    relatorio_txt += "====================================================\n\n"
    
    if st.session_state.historico_professor:
        for idx, item in enumerate(st.session_state.historico_professor, 1):
            relatorio_txt += f"Registro #{idx} | Equipe: {item['equipe']}\n"
            relatorio_txt += f"Local na Pergunta: {item['casa_santuario']}\n"
            relatorio_txt += f"Guia do Templo: {item['guia']} | Cientista Relacionado: {item['cientista']}\n"
            relatorio_txt += f"Enunciado: {item['enunciado']}\n"
            relatorio_txt += f"Resposta Escolhida: {item['resposta']}\n"
            relatorio_txt += f"Resultado: {item['status']}\n"
            relatorio_txt += f"Justificativa Pedagógica: {item['por_que']}\n"
            relatorio_txt += "----------------------------------------------------\n"
    else:
        relatorio_txt += "Nenhuma resposta registrada no sistema até o momento.\n"
        
    st.sidebar.download_button(
        label="📥 Baixar Respostas das Equipes (.doc / Word)",
        data=relatorio_txt,
        file_name="relatorio_respostas_alunos.doc",
        mime="application/msword"
    )
    
    st.sidebar.download_button(
        label="📥 Baixar Respostas das Equipes (.txt / Texto)",
        data=relatorio_txt,
        file_name="relatorio_respostas_alunos.txt",
        mime="text/plain"
    )

    if st.sidebar.button("🗑️ Limpar Histórico de Respostas"):
        st.session_state.historico_professor = []
        st.sidebar.success("Histórico limpo!")
        st.rerun()

# ==========================================
# PLACAR NA BARRA LATERAL (COM A CASA EXATA ACIMA DE CADA EQUIPE)
# ==========================================
st.sidebar.header("📊 Posição no Santuário (Meta: 12 Casas)")

# Equipe Alfa
casa_alfa_str = obter_nome_casa(st.session_state.casas_alfa)
st.sidebar.markdown(f"🛡️ **Equipe Alfa**\n*📍 Localização: {casa_alfa_str}*")
st.sidebar.progress(min(1.0, st.session_state.casas_alfa / 12))
st.sidebar.markdown("---")

# Equipe Beta
casa_beta_str = obter_nome_casa(st.session_state.casas_beta)
st.sidebar.markdown(f"🛡️ **Equipe Beta**\n*📍 Localização: {casa_beta_str}*")
st.sidebar.progress(min(1.0, st.session_state.casas_beta / 12))
st.sidebar.markdown("---")

# Equipe Gama
casa_gama_str = obter_nome_casa(st.session_state.casas_gama)
st.sidebar.markdown(f"🛡️ **Equipe Gama**\n*📍 Localização: {casa_gama_str}*")
st.sidebar.progress(min(1.0, st.session_state.casas_gama / 12))

# BOTÃO DE REINICIAR PERMANENTE
st.sidebar.markdown("---")
if st.sidebar.button("🔄 Reiniciar Partida"):
    reiniciar_jogo()
    st.rerun()

# ==========================================
# INÍCIO DO JOGO
# ==========================================
lista_equipes = ["Equipe Alfa", "Equipe Beta", "Equipe Gama"]

if not st.session_state.jogo_iniciado:
    st.subheader("🔥 Cerimônia de Abertura: O Despertar do Cosmo")
    st.markdown("""
    > Jovens aspirantes reúnem-se no sopé do Santuário. Para se tornarem verdadeiros **Cavaleiros de Athena**, 
    > vocês avançarão pelas **12 Casas do Santuário** dominando a **sabedoria cosmológica** (Big Bang, Relatividade Geral e Matéria Escura).
    > 
    > **Regras da Competição:**
    > * **Acerto:** Avança 1 Casa no Santuário!
    > * **Erro:** **Não perde Casas**, mas a questão muda imediatamente e a vez passa para a próxima equipe!
    > * **Meta de Vitória:** A primeira equipe a atravessar as **12 Casas** e alcançar o **Templo de Athena** vence o jogo!
    """)
    
    if st.button("🌟 Iniciar Treinamento do Santuário"):
        st.session_state.jogo_iniciado = True
        st.rerun()
    st.stop()

# ==========================================
# VERIFICAÇÃO DE FIM DE JOGO
# ==========================================
vencedor_instantaneo = None
if st.session_state.casas_alfa >= 12: vencedor_instantaneo = "Equipe Alfa"
elif st.session_state.casas_beta >= 12: vencedor_instantaneo = "Equipe Beta"
elif st.session_state.casas_gama >= 12: vencedor_instantaneo = "Equipe Gama"

if vencedor_instantaneo or st.session_state.indice_pergunta >= len(st.session_state.banco_50):
    st.balloons()
    st.subheader("🏛️ Chegada Gloriosa ao Templo de Athena!")
    
    if vencedor_instantaneo:
        st.success(f"🥇 **A {vencedor_instantaneo} atravessou as 12 Casas do Santuário e conquistou a Armadura de Ouro no Templo de Athena!**")
    else:
        pontuacoes = {
            "Equipe Alfa": st.session_state.casas_alfa,
            "Equipe Beta": st.session_state.casas_beta,
            "Equipe Gama": st.session_state.casas_gama
        }
        maior_pts = max(pontuacoes.values())
        vencedores = [eq for eq, pts in pontuacoes.items() if pts == maior_pts]
        
        if len(vencedores) > 1:
            st.success(f"🤝 **Empate Lendário alcançando a {obter_nome_casa(maior_pts)} entre: {', '.join(vencedores)}! Todos tornaram-se Cavaleiros de Athena juntos!**")
        else:
            st.success(f"🥇 **A {vencedores[0]} avançou mais longe no Santuário, chegando até a {obter_nome_casa(maior_pts)}, e sagrou-se campeã!**")
            
    st.markdown("---")
    st.markdown("### 🏆 **Posição Final das Equipes**")
    st.markdown(f"* **🛡️ Equipe Alfa:** {obter_nome_casa(st.session_state.casas_alfa)}")
    st.markdown(f"* **🛡️ Equipe Beta:** {obter_nome_casa(st.session_state.casas_beta)}")
    st.markdown(f"* **🛡️ Equipe Gama:** {obter_nome_casa(st.session_state.casas_gama)}")
    
    st.markdown("---")
    if st.button("🔄 Iniciar Novo Treinamento do Santuário"):
        reiniciar_jogo()
        st.rerun()
    st.stop()

# ==========================================
# FLUXO DAS QUESTÕES
# ==========================================
total_questoes = len(st.session_state.banco_50)
idx_p = st.session_state.indice_pergunta
e_idx = st.session_state.equipe_sub_idx
equipe_da_vez = lista_equipes[e_idx]

# Define a casa atual da equipe que está jogando na rodada
if equipe_da_vez == "Equipe Alfa": casa_equipe_str = obter_nome_casa(st.session_state.casas_alfa)
elif equipe_da_vez == "Equipe Beta": casa_equipe_str = obter_nome_casa(st.session_state.casas_beta)
else: casa_equipe_str = obter_nome_casa(st.session_state.casas_gama)

q_atual = st.session_state.banco_50[idx_p]

# Embaralha as alternativas dinamicamente
chave_opcoes = f"opcoes_shuffled_{idx_p}"
if chave_opcoes not in st.session_state:
    opcoes_copia = list(q_atual['opcoes_originais'])
    random.shuffle(opcoes_copia)
    
    opcoes_rotuladas = []
    letras = ["A", "B", "C", "D", "E"]
    for i, texto in enumerate(opcoes_copia):
        opcoes_rotuladas.append(f"{letras[i]}) {texto}")
    st.session_state[chave_opcoes] = opcoes_rotuladas

# EXIBE A LOCALIZAÇÃO DA EQUIPE NA TELA PRINCIPAL
st.warning(f"📍 **{equipe_da_vez} encontra-se atualmente em:** {casa_equipe_str}")

st.subheader(f"⚔️ Vez da: **{equipe_da_vez}**")
st.markdown(f"**Guia da Casa:** *{q_atual['guia']}* ✨")
st.markdown("---")

# NARRATIVA DO CAVALEIRO + CIENTISTA
st.info(f"📜 **Fala de {q_atual['guia']} sobre a História da Ciência:**\n\n\"{q_atual['texto_base']}\"\n\n🔬 **Cientista / Referência:** *{q_atual['cientista']}*")

st.markdown(f"### **Enigma Cosmológico:**\n{q_atual['enunciado']}")

# Exibe as alternativas embaralhadas
escolha_usuario = st.radio("Selecione a alternativa correta:", st.session_state[chave_opcoes], key=f"radio_{idx_p}_{e_idx}")

if st.button("Enviar Resposta e Elevar o Cosmo"):
    texto_selecionado = escolha_usuario.split(") ", 1)[1].strip()
    acertou = (texto_selecionado == q_atual['correta_texto'])
    
    status = "CORRETA" if acertou else "INCORRETA"
    
    # Atualização por avanço de Casas sem perda
    if acertou:
        if equipe_da_vez == "Equipe Alfa": st.session_state.casas_alfa += 1
        elif equipe_da_vez == "Equipe Beta": st.session_state.casas_beta += 1
        else: st.session_state.casas_gama += 1
        
        st.session_state.indice_pergunta += 1
        st.session_state.equipe_sub_idx = (e_idx + 1) % 3
    else:
        # Errou: Não perde casas, apenas muda a questão e passa a vez
        st.session_state.indice_pergunta += 1
        st.session_state.equipe_sub_idx = (e_idx + 1) % 3

    # Registra no relatório do professor
    st.session_state.historico_professor.append({
        "equipe": equipe_da_vez,
        "casa_santuario": casa_equipe_str,
        "guia": q_atual['guia'],
        "cientista": q_atual['cientista'],
        "enunciado": q_atual['enunciado'],
        "resposta": escolha_usuario,
        "status": status,
        "por_que": q_atual['por_que']
    })

    st.session_state.ultimo_feedback = {
        "status": status,
        "equipe": equipe_da_vez,
        "correta_texto": q_atual['correta_texto'],
        "por_que": q_atual['por_que']
    }
        
    st.rerun()

# Feedback da última jogada
if st.session_state.ultimo_feedback:
    st.markdown("---")
    fb = st.session_state.ultimo_feedback
    if fb['status'] == "CORRETA":
        st.success(f"🎉 Excelente! A **{fb['equipe']}** acertou e avançou para a próxima Casa do Santuário!")
    else:
        st.error(f"❌ Resposta Incorreta da **{fb['equipe']}**. A opção correta era: *\"{fb['correta_texto']}\"*. A questão mudou e a vez passou para a próxima equipe!")
        
    st.info(f"💡 **JUSTIFICATIVA PEDAGÓGICA (O PORQUÊ):**\n\n{fb['por_que']}")
