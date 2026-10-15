import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="CDZ: O Despertar do Cosmo - Rumo a Athena", page_icon="🌌", layout="centered")

# ==========================================
# INICIALIZAÇÃO DO ESTADO GLOBAL
# ==========================================
if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False
if "rodada_atual" not in st.session_state:
    st.session_state.rodada_atual = 1
if "equipe_sub_idx" not in st.session_state:
    st.session_state.equipe_sub_idx = 0  # 0: Alfa, 1: Beta, 2: Gama
if "pontos_alfa" not in st.session_state:
    st.session_state.pontos_alfa = 0
if "pontos_beta" not in st.session_state:
    st.session_state.pontos_beta = 0
if "pontos_gama" not in st.session_state:
    st.session_state.pontos_gama = 0

# Estabilidade individual por equipe
if "estabilidade_alfa" not in st.session_state:
    st.session_state.estabilidade_alfa = 100
if "estabilidade_beta" not in st.session_state:
    st.session_state.estabilidade_beta = 100
if "estabilidade_gama" not in st.session_state:
    st.session_state.estabilidade_gama = 100

if "historico_respostas" not in st.session_state:
    st.session_state.historico_respostas = []
if "ultimo_feedback" not in st.session_state:
    st.session_state.ultimo_feedback = None

# ==========================================
# BANCO COM 50 QUESTÕES DE MÚLTIPLA ESCOLHA (A a E) + JUSTIFICATIVA
# ==========================================
if "banco_50_questoes" not in st.session_state:
    guias_cdz = ["Seiya de Pégaso", "Shiryu de Dragão", "Hyoga de Cisne", "Shun de Andrômeda", "Ikki de Fênix", "Mu de Áries", "Shaka de Virgem", "Aioria de Leão", "Dohko de Libra", "Camus de Aquário"]
    
    # Geramos uma lista fixa e rica de 50 questões conceituais cobrindo Big Bang, Relatividade e Matéria Escura
    questoes_base = [
        # Bloco 1: Big Bang e Expansão (1 a 15)
        ("O que postula o modelo cosmológico do Big Bang sobre a origem do Universo?", 
         ["A) O universo surgiu estático e eterno, sem nenhuma alteração temporal.", 
          "B) O cosmos originou-se de uma singularidade extremamente densa e quente, expandindo-se desde então.", 
          "C) As galáxias formaram-se instantaneamente a partir de colisões de buracos negros estáticos.", 
          "D) O universo expande-se porque as estrelas criam matéria nova do nada.", 
          "E) A origem cósmica é cíclica, colapsando exatamente a cada 100 anos."], "B", 
         "O Big Bang descreve a expansão métrica do espaço a partir de um estado inicial de altíssima densidade e temperatura."),
        
        ("Como a analogia do balão de festa sendo inflado ajuda a compreender a expansão do universo?", 
         ["A) Mostra que o balão cria ar novo do nada em seu interior.", 
          "B) Ilustra como os pontos na superfície do balão se afastam porque o próprio espaço da borracha se expande.", 
          "C) Comprova que o centro do balão é a única parte que se move.", 
          "D) Indica que o universo possui paredes rígidas que contêm o calor.", 
          "E) Demonstra que a luz viaja mais rápido que o som."], "B", 
         "Assim como no balão, as galáxias não correm pelo espaço; é o próprio tecido do espaço que se estica, afastando-as."),
        
        ("Qual é a principal evidência observacional que comprova a expansão contínua do Universo?", 
         ["A) O desvio para o vermelho (redshift) das galáxias distantes, formulado na Lei de Hubble.", 
          "B) A colisão frequente de planetas no sistema solar.", 
          "C) O resfriamento rápido do Sol observado por telescópios modernos.", 
          "D) A ausência completa de radiação no espaço interestelar.", 
          "E) A rotação estática das estrelas fixas na esfera celeste."], "A", 
         "O redshift demonstra que as ondas de luz esticam devido à expansão do espaço, provando que o universo está se expandindo."),
        
        ("O que foi a 'Era da Recombinação' nos instantes iniciais do Big Bang?", 
         ["A) O momento em que os buracos negros engoliram toda a matéria.", 
          "B) O período em que os prótons e elétrons puderam se combinar para formar átomos neutros, permitindo que a luz viajasse livremente.", 
          "C) A colisão entre a Via Láctea e Andrômeda.", 
          "D) A fase em que a gravidade deixou de existir no cosmos.", 
          "E) O congelamento total do universo."], "B", 
         "Com a formação de átomos neutros, os fótons libertaram-se, gerando a Radiação Cósmica de Fundo."),
        
        ("O que representa a Radiação Cósmica de Fundo em Micro-ondas (CMB)?", 
         ["A) O eco térmico remanescente dos primeiros momentos do Big Bang.", 
          "B) A energia gerada pelas supernovas na Via Láctea.", 
          "C) O calor emitido pelo núcleo de buracos negros supermassivos.", 
          "D) Interferência de rádio gerada por estrelas de nêutrons.", 
          "E) Luz refletida pela poeira interestelar."], "A", 
         "A CMB é a radiação fóssil do universo primordial, captada em todas as direções do céu."),
        
        ("O que caracteriza uma 'singularidade' no contexto cosmológico?", 
         ["A) Um planeta com formato perfeitamente esférico.", 
          "B) Um estado de densidade e temperatura infinitas onde as leis físicas conhecidas deixam de funcionar.", 
          "C) Uma estrela que brilha mais que um milhão de sóis.", 
          "D) O ponto exato onde a Terra orbita o Sol.", 
          "E) Um cometa que cruza o sistema solar uma única vez."], "B", 
         "Na singularidade, como no centro de buracos negros ou no início do Big Bang, as grandezas físicas atingem valores infinitos."),
        
        ("Qual cientista formulou a teoria da expansão do universo corroborada pelo desvio para o vermelho das galáxias?", 
         ["A) Isaac Newton", "B) Galileo Galilei", "C) Edwin Hubble", "D) Johannes Kepler", "E) Nikola Tesla"], "C", 
         "Edwin Hubble descobriu que quanto mais distante uma galáxia está, mais rápido ela se afasta de nós (Lei de Hubble)."),
        
        ("Antes do Big Bang, o que existia segundo a cosmologia padrão?", 
         ["A) Um vasto oceano de estrelas congeladas.", 
          "B) O conceito de espaço e tempo não existia da forma atual, estando toda matéria comprimida em singularidade.", 
          "C) Um vácuo repleto de galáxias espirais estáticas.", 
          "D) Um buraco negro colossal que engolia planetas.", 
          "E) Matéria escura em estado gasoso."], "B", 
         "O próprio espaço e o tempo surgiram com o evento do Big Bang, não havendo um 'antes' no espaço convencional."),
        
        ("O que é o 'Horizonte de Eventos' em astrofísica?", 
         ["A) A borda visível de um planeta rochoso.", 
          "B) O limite ao redor de um buraco negro além do qual nada, nem mesmo a luz, pode escapar.", 
          "C) O limite do sistema solar onde o vento solar cessa.", 
          "D) A distância máxima que um telescópio pode enxergar.", 
          "E) O momento em que uma estrela se transforma em supernova."], "B", 
         "O horizonte de eventos marca o ponto de gravidade extrema de onde a velocidade de escape supera a da luz."),
        
        ("O que foi a Teoria da Inflação Cósmica proposta por Alan Guth?", 
         ["A) A expansão lenta e gradual das estrelas ao longo de trilhões de anos.", 
          "B) Um período de expansão exponencial ultrarrápida ocorrido numa fração minúscula de segundo logo após o Big Bang.", 
          "C) O aumento do brilho das supernovas.", 
          "D) A inflação da massa dos buracos negros.", 
          "E) A expansão do sistema solar devido ao vento estelar."], "B", 
         "A inflação cósmica resolveu problemas clássicos do Big Bang, como a homogeneidade e a planura do universo observável."),
        
        ("Qual elemento químico leve foi predominante na nucleossíntese primordial logo após o Big Bang?", 
         ["A) Ouro e Platina", "B) Urânio e Plutônio", "C) Hidrogênio e Hélio", "D) Ferro e Níquel", "E) Silício e Carbono"], "C", 
         "Nos primeiros minutos do universo, formaram-se primordialmente os núcleos de hidrogênio e hélio, além de vestígios de lítio."),
        
        ("Por que a luz das estrelas distantes sofre o desvio para o vermelho (redshift)?", 
         ["A) Porque as estrelas estão esfriando e emitindo luz vermelha.", 
          "B) Porque o comprimento de onda da luz é esticado pela expansão do espaço entre a galáxia e nós.", 
          "C) Porque há fumaça cósmica bloqueando a luz azul.", 
          "D) Devido à rotação rápida da Terra em torno do Sol.", 
          "E) Porque as galáxias vermelhas são mais antigas."], "B", 
         "O estiramento do espaço estica o comprimento de onda dos fótons, deslocando-os para o espectro vermelho."),
        
        ("O que mede a chamada 'Constante de Hubble'?", 
         ["A) A velocidade com que a Terra gira em torno do seu eixo.", 
          "B) A taxa atual de expansão do universo.", 
          "C) A distância exata entre a Terra e o centro da Via Láctea.", 
          "D) A massa total de hidrogênio no cosmos.", 
          "E) A força da gravidade na superfície do Sol."], "B", 
         "A constante de Hubble quantifica a velocidade de afastamento das galáxias em função de sua distância."),
        
        ("O que significa dizer que o universo é 'homogêneo e isotrópico' em grande escala?", 
         ["A) Que ele é totalmente plano e feito apenas de ferro.", 
          "B) Que, em grande escala, ele tem a mesma aparência em qualquer lugar (homogêneo) e em todas as direções (isotrópico).", 
          "C) Que todas as estrelas possuem exatamente a mesma idade e tamanho.", 
          "D) Que o universo possui um centro fixo e bem definido.", 
          "E) Que a temperatura é zero absoluto em todo o cosmo."], "B", 
         "Este é o Princípio Cosmológico fundamental que rege os modelos padrão do universo."),
        
        ("O que é a Nucleossíntese Primordial?", 
         ["A) A fusão de elementos pesados dentro de supernovas modernas.", 
          "B) A criação dos primeiros núcleos atômicos leves durante os primeiros minutos do Big Bang.", 
          "C) A formação de planetas rochosos em discos protoplanetários.", 
          "D) A destruição de átomos por radiação gama.", 
          "E) A síntese de matéria escura em aceleradores de partículas."], "B", 
         "Processo em que a sopa primordial de prótons e nêutrons fundiu-se nos primeiros elementos químicos do universo."),

        # Bloco 2: Relatividade Geral e Espaço-Tempo (16 a 30)
        ("Segundo a Teoria da Relatividade Geral de Einstein, como a gravidade é explicada?", 
         ["A) Como uma atração magnética direta entre os corpos.", 
          "B) Como a curvatura do tecido quadridimensional do espaço-tempo provocada por massa e energia.", 
          "C) Como o atrito gerado pelo vento cósmico.", 
          "D) Como uma ilusão óptica sem efeitos físicos reais.", 
          "E) Como partículas quânticas chamadas grávitons que empurram os objetos."], "B", 
         "Massa e energia dizem ao espaço-tempo como se curvar, e o espaço-tempo diz à massa como se mover."),
        
        ("O que acontece com a passagem do tempo em campos gravitacionais muito intensos ou a velocidades próximas à da luz?", 
         ["A) O tempo passa mais rápido para o observador.", 
          "B) O tempo desacelera (dilatação temporal) em relação a um observador distante.", 
          "C) O tempo para completamente e nunca mais avança.", 
          "D) O tempo passa a correr de trás para frente.", 
          "E) Não há alteração alguma na contagem temporal."], "B", 
         "A dilatação temporal é uma consequência comprovada da Relatividade Especial e Geral."),
        
        ("O que foi o famoso eclipse solar de 1919 que consagrou a Relatividade Geral?", 
         ["A) A prova de que a Lua é feita de queijo.", 
          "B) A observação de que a luz das estrelas ao passar perto do Sol sofria desvio previsto pela curvatura do espaço.", 
          "C) O escurecimento total do universo por matéria escura.", 
          "D) A colisão entre o Sol e um buraco negro.", 
          "E) A medição exata da velocidade da luz no vácuo."], "B", 
         "O desvio da luz estelar pela gravidade solar confirmou a curvatura do espaço-tempo predita por Einstein."),
        
        ("O que são Ondas Gravitacionais preditas por Einstein e detectadas recentemente?", 
         ["A) Ondas sonoras que viajam através do vácuo intergaláctico.", 
          "B) Perturbações ou ondulações no tecido do espaço-tempo geradas por eventos cósmicos violentos (como fusão de buracos negros).", 
          "C) Ondas de rádio emitidas por pulsares.", 
          "D) Raios cosmicos de alta energia.", 
          "E) Marés oceânicas causadas pela lua e sol."], "B", 
         "As ondas gravitacionais viajam pelo cosmos esticando e comprimindo o próprio tecido do espaço."),
        
        ("O princípio da equivalência de Einstein estabelece que:", 
         ["A) Toda matéria tem exatamente a mesma massa.", 
          "B) Os efeitos de um campo gravitacional são localmente indistinguíveis dos efeitos de uma aceleração constante.", 
          "C) A energia e a massa nunca se convertem uma na outra.", 
          "D) A velocidade da luz varia dependendo de quem a observa.", 
          "E) A gravidade é mais fraca que o eletromagnetismo."], "B", 
         "Estar em um elevador fechado acelerando no espaço é fisicamente equivalente a estar parado em um campo gravitacional."),
        
        ("O que é o espaço-tempo quadridimensional?", 
         ["A) Uma sala com quatro paredes e teto.", 
          "B) A união matemática das três dimensões espaciais (comprimento, largura, altura) com a dimensão temporal.", 
          "C) Um holograma gerado por supercomputadores.", 
          "D) O espaço que existe apenas dentro de buracos negros.", 
          "E) As dimensões paralelas onde habitam os deuses."], "B", 
         "O universo físico é descrito como um contínuo quadridimensional onde eventos ocorrem em coordenadas de espaço e tempo."),
        
        ("Por que a luz não consegue escapar de um buraco negro?", 
         ["A) Porque a luz desliga sua energia ao se aproximar.", 
          "B) Porque a curvatura do espaço-tempo é tão extrema que todos os caminhos possíveis apontam para o centro.", 
          "C) Porque o buraco negro possui um campo magnético que repele fótons.", 
          "D) Porque a luz é mais pesada que o buraco negro.", 
          "E) Porque o vácuo ao redor absorve a cor da luz."], "B", 
         "Dentro do horizonte de eventos, a geometria do espaço-tempo é curvada para dentro de tal forma que escapar é geometricamente impossível."),
        
        ("O que prediz a Relatividade sobre o movimento de relógios em satélites GPS orbitando a Terra?", 
         ["A) Eles marcam exatamente o mesmo tempo que os relógios na Terra.", 
          "B) Eles sofrem ajustes relativísticos (devido à velocidade e à gravidade menor) para funcionar com precisão milimétrica.", 
          "C) Eles param de funcionar devido ao frio do espaço.", 
          "D) Eles aceleram tanto que quebram em poucos dias.", 
          "E) O tempo neles passa mais devagar que na superfície terrestre."], "B", 
         "Sem correções da Relatividade Geral e Especial, o GPS acumularia erros de quilômetros por dia."),
        
        ("O que é a 'Lente Gravitacional'?", 
         ["A) Um óculos especial usado por astrônomos.", 
          "B) O efeito em que massas gigantescas (como aglomerados de galáxias) curvam a luz de objetos situados atrás delas, amplificando-a ou distorcendo-a.", 
          "C) Uma lupa feita de cristal de quartzo no espaço.", 
          "D) A luz emitida por estrelas binárias.", 
          "E) O brilho refletido pelos anéis de Saturno."], "B", 
         "A massa desvia a trajetória da luz de forma análoga a uma lente óptica comum."),
        
        ("Qual é a relação entre massa e energia expressa na famosa equação $E=mc^2$?", 
         ["A) Massa e energia são totalmente independentes.", 
          "B) Massa e energia são formas equivalentes da mesma grandeza física, convertíveis entre si.", 
          "C) A energia é sempre maior que a massa em qualquer objeto.", 
          "D) A massa viaja sempre na velocidade da luz.", 
          "E) A energia não possui relação com a gravidade."], "B", 
         "A energia em repouso ($E$) é igual à massa ($m$) multiplicada pelo quadrado da velocidade da luz ($c^2$); massa é energia concentrada."),

        ("O que os buracos de minhoca (wormholes) representam na física teórica?", 
         ["A) Túnel criados por minhocas espaciais gigantes.", 
          "B) Atalhos hipotéticos através do espaço-tempo conectando dois pontos distantes do universo.", 
          "C) O interior de estrelas de nêutrons.", 
          "D) Partículas subatômicas que viajam no tempo.", 
          "E) A fumaça gerada por supernovas."], "B", 
         "Embora permitidos matematicamente pela Relatividade Geral, sua existência física real permanece altamente especulativa e instável."),

        ("O que caracteriza uma estrela de nêutrons?", 
         ["A) Uma estrela composta inteiramente de gás hidrogênio.", 
         "B) O cadáver superdenso de uma estrela massiva onde os elétrons e prótons fundiram-se em nêutrons.", 
         "C) Um planeta gasoso gigante sem núcleo sólido.", 
         "D) Uma galáxia espiral em miniatura.", 
         "E) Uma estrela que orbita um buraco negro de perto."], "B", 
         "Uma colher de chá de matéria de estrela de nêutrons pesaria bilhões de toneladas na Terra devido à sua extrema densidade."),

        ("O que significa dizer que o espaço é dinâmico na Relatividade Geral?", 
         ["A) Que ele muda de cor dependendo da estação do ano.", 
          "B) Que o espaço não é um palco rígido e imóvel, mas sim um meio flexível que pode curvar-se, vibrar e expandir-se.", 
          "C) Que ele possui correntes de ar invisíveis.", 
          "D) Que ele se move de leste para oeste como a Terra.", 
          "E) Que ele possui fricção mecânica."], "B", 
         "O espaço-tempo reage à presença de matéria e energia, alterando sua geometria constantemente."),

        ("O que são pulsares?", 
         ["A) Planetas que piscam no céu noturno.", 
          "B) Estrelas de nêutrons altamente magnetizadas que giram rapidamente, emitindo feixes de radiação eletromagnética como um farol.", 
          "C) Galáxias que pulsam expandindo e contraindo.", 
          "D) Cometas com órbitas instáveis.", 
          "E) Aglomerados globulares de estrelas jovens."], "B", 
         "Seus pulsos de radiação são extremamente regulares, funcionando como relógios naturais precisos no cosmos."),

        ("Qual é o limite máximo de velocidade para a transmissão de informações e movimento de matéria no universo?", 
         ["A) A velocidade do som no ar", "B) A velocidade da luz no vácuo ($c$)", "C) A velocidade da gravidade quântica", "D) 1.000 km/s", "E) Não existe limite de velocidade."], "B", 
         "Nenhum sinal ou objeto com massa pode ultrapassar a velocidade da luz no vácuo de acordo com a Relatividade."),

        # Bloco 3: Matéria Escura, Energia Escura e Estrutura do Universo (31 a 50)
        ("Qual é a principal função da Matéria Escura na estruturação em grande escala do cosmos?", 
         ["A) Emitir luz intensa para iluminar o espaço profundo.", 
          "B) Atuar como uma 'cola gravitacional' invisível que mantém as galáxias coesas em alta velocidade.", 
          "C) Acelerar a expansão do universo para longe.", 
          "D) Proteger as estrelas contra radiação gama.", 
          "E) Absorver buracos negros antigos."], "B", 
         "A matéria visível não tem massa suficiente; a matéria escura fornece a atração gravitacional extra que segura as galáxias."),
        
        ("Qual é a diferença conceitual fundamental entre Matéria Escura e Energia Escura?", 
         ["A) A matéria escura atrai (gravidade), enquanto a energia escura repele (acelera a expansão).", 
          "B) Ambas fazem exatamente a mesma coisa na estrutura cósmica.", 
          "C) A energia escura é visível em telescópios ópticos comuns.", 
          "D) A matéria escura acelera o universo para fora, enquanto a energia escura o comprime.", 
          "E) Não há diferença teórica entre ambas."], "A", 
         "Enquanto a matéria escura age aglutinando estruturas via gravidade, a energia escura impulsiona a expansão acelerada do cosmos."),
        
        ("Aproximadamente, qual é a porcentagem da composição do universo entre Matéria Escura, Energia Escura e Matéria Ordinária (visível)?", 
         ["A) 50% matéria visível, 30% escura, 20% energia escura", 
          "B) 90% matéria ordinária, 5% matéria escura, 5% energia escura", 
          "C) Cerca de 68% energia escura, 27% matéria escura e apenas 5% de matéria ordinária.", 
          "D) 99% matéria escura e 1% de todo o resto.", 
          "E) 33% para cada uma das três categorias."], "C", 
         "O universo é dominado por componentes misteriosos e invisíveis (energia escura e matéria escura), sendo a matéria comum apenas uma fração menor."),
        
        ("Por que a Matéria Escura é chamada de 'escura'?", 
         ["A) Porque ela bloqueia a luz como tinta preta.", 
          "B) Porque ela não emite, absorve ou reflete luz nem qualquer outra radiação eletromagnética detectável diretamente.", 
          "C) Porque ela só existe nas regiões mais sombrias do espaço.", 
          "D) Devido à cor escura dos planetas que a compõem.", 
          "E) Porque foi descoberta durante a noite."], "B", 
         "Sua detecção é feita exclusivamente através dos seus efeitos gravitacionais indiretos sobre a matéria visível e a luz."),
        
        ("O que as curvas de rotação das galáxias espirais revelaram sobre a massa galáctica?", 
         ["A) Que a massa está concentrada unicamente no centro brilhante.", 
          "B) Que as estrelas nas bordas giram rápido demais para a massa visível, indicando a presença de um halo massivo invisível (matéria escura).", 
          "C) Que as galáxias estão paradas no espaço.", 
          "D) Que a gravidade diminui a zero nas bordas.", 
          "E) Que todas as galáxias possuem buracos negros gêmeos."], "B", 
         "As velocidades das estrelas periféricas provaram que há muito mais massa no halo do que aquela que conseguimos enxergar."),

        ("O que causou a descoberta de que a expansão do universo está *acelerando* em vez de desacelerar?", 
         ["A) A observação de supernovas distantes do tipo Ia na década de 1990.", 
          "B) O cálculo da massa da Lua.", 
          "C) A colisão entre a Via Láctea e a Grande Nuvem de Magalhães.", 
          "D) A medição do campo magnético da Terra.", 
          "E) Experimentos de laboratório com laser."], "A", 
         "Supernovas distantes pareciam mais fracas (mais distantes) do que o esperado, provando que a expansão acelerou ao longo do tempo cosmológico."),

        ("O que é a Constante Cosmológica ($\Lambda$) introduzida originalmente por Einstein?", 
         ["A) A velocidade exata da luz.", 
          "B) Um termo matemático adicionado por Einstein às suas equações para tentar manter um universo estático, mais tarde associado à energia escura.", 
          "C) O peso de um átomo de hidrogênio.", 
          "D) A taxa de rotação do Sol.", 
          "E) A distância entre a Terra e Andrômeda."], "B", 
         "Embora Einstein a tenha chamado de seu 'maior erro' ao pensar que o universo era estático, hoje ela reaparece explicada pela energia escura."),

        ("O que são Aglomerados de Galáxias?", 
         ["A) Estrelas solitárias vagando entre galáxias.", 
          "B) Vastas estruturas formadas por centenas ou milhares de galáxias mantidas juntas pela gravidade.", 
          "C) Anéis de poeira ao redor do Sol.", 
          "D) Nuvens de gás frio sem estrelas.", 
          "E) Sistemas planetários em rotação caótica."], "B", 
         "Aglomerados são os maiores laboratórios cósmicos para estudar matéria escura e lentes gravitacionais."),

        ("Qual é o papel dos 'Filamentos Cósmicos' na teia cósmica do universo?", 
         ["A) Conectar os computadores da NASA aos telescópios.", 
          "B) Formar enormes pontes de matéria (visível e escura) que cercam vastas regiões vazias (vazios cósmicos).", 
          "C) Conduzir raios solares entre sistemas planetários.", 
          "D) Servir de trilho para cometas interestelares.", 
          "E) Serem formados puramente por luz pura."], "B", 
         "A grande teia cósmica do universo organiza-se em filamentos, nós e grandes vazios espaciais."),

        ("O que são os 'Vazios Cósmicos' (Cosmic Voids)?", 
         ["A) Lugares onde o tempo para completamente.", 
          "B) Enormes regiões do espaço com baixa densidade de galáxias, separando os filamentos da teia cósmica.", 
          "C) O centro exato de cada buraco negro.", 
          "D) O espaço vazio dentro de um átomo.", 
          "E) Regiões sem nenhuma partícula de matéria escura."], "B", 
         "Os vazios cobrem a maior parte do volume do universo, enquanto a matéria concentra-se nos filamentos e nós."),

        ("O que significa WIMP no contexto da pesquisa de Matéria Escura?", 
         ["A) Weakly Interacting Massive Particles (Partículas Massivas de Interação Fraca), candidatos teóricos a matéria escura.", 
          "B) Waves in Microwave Pulses.", 
          "C) White Dwarf Interstellar Matter Photon.", 
          "D) Wormhole Integrated Mass Plasma.", 
          "E) Water Isotope Molecular Process."], "A", 
         "WIMPs são partículas hipotéticas que interagem apenas pela gravidade e força nuclear fraca, sendo principais alvos de buscas laboratoriais."),

        ("O que são Axions?", 
         ["A) Partículas elementares hipotéticas leves propostas para resolver problemas de simetria e candidatas a matéria escura.", 
          "B) Raios gama emitidos por estrelas jovens.", 
          "C) A menor unidade de tempo possível.", 
          "D) Composição química dos anéis de Júpiter.", 
          "E) O nome dado à energia escura pura."], "A", 
         "Axions são outra classe de partículas candidatas a explicar a natureza da matéria escura fria."),

        ("O que é a Matéria Escura 'Quente' (Hot Dark Matter) em contraste com a 'Fria'?", 
         ["A) Matéria escura que emite calor infravermelho.", 
          "B) Partículas de matéria escura que se movem a velocidades relativísticas (próximas à da luz), como neutrinos massivos.", 
          "C) Lava derretida no núcleo de planetas exóticos.", 
          "D) O gás superaquecido entre aglomerados galácticos.", 
          "E) Matéria escura que orbita muito perto de estrelas."], "B", 
         "A cosmologia moderna aponta para a Matéria Escura Fria (CDM) como o modelo dominante para a formação das estruturas do universo."),

        ("Como as simulações computacionais de N-corpos ajudam a entender a formação do universo?", 
         ["A) Calculando a meteorologia da Terra em tempo real.", 
          "B) Simulando a gravidade e interação de milhões de partículas de matéria escura para recriar a teia cósmica.", 
          "C) Traduzindo sinais de rádio extraterrestres.", 
          "D) Desenhando mapas estelares bidimensionais.", 
          "E) Calculando a órbita da Lua."], "B", 
         "Essas supercomputações mostram como pequenas flutuações primordiais evoluem para os aglomerados de galáxias atuais."),

        ("Qual é o destino final mais provável do universo segundo os dados atuais sobre a Energia Escura?", 
         ["A) O Big Crunch (colapso total em um ponto).", 
          "B) A expansão eterna acelerada (Big Freeze / Morte Térmica), onde as galáxias se afastarão tanto que o cosmos ficará frio e escuro.", 
          "C) Uma grande explosão de luz branca constante.", 
          "D) A transformação de todas as estrelas em buracos brancos.", 
          "E) A reversão do tempo."], "B", 
         "Com a aceleração impulsionada pela energia escura, o universo caminha para uma dispersão eterna e resfriamento gradual."),

        ("O que foi o experimento Planck da Agência Espacial Europeia (ESA)?", 
         ["A) Uma missão tripulada a Marte.", 
          "B) Um telescópio espacial que mapeou com precisão sem precedentes as flutuações da Radiação Cósmica de Fundo (CMB).", 
          "C) Um acelerador de partículas subterrâneo.", 
          "D) O primeiro satélite a orbitar o Sol.", 
          "E) Um estudo sobre a atmosfera de Vênus."], "B", 
         "Os dados do Planck refinaram os parâmetros cosmológicos da idade do universo, matéria escura e energia escura com altíssima precisão."),

        ("Por que a energia escura não se dilui da mesma forma que a matéria comum ou escura durante a expansão do universo?", 
         ["A) Porque ela é criada constantemente pelas estrelas.", 
          "B) Porque ela é uma propriedade inerente ao próprio vácuo do espaço; à medida que o espaço cresce, há mais vácuo e, portanto, mais energia escura.", 
          "C) Porque ela possui massa negativa infinita.", 
          "D) Porque ela viaja mais rápido que o universo.", 
          "E) Porque ela interage fortemente com buracos negros."], "B", 
         "Como a densidade de energia do vácuo permanece constante, sua influência domina o universo em eras de grande expansão."),

        ("O que os astrônomos querem dizer quando falam em 'Crise na Cosmologia' recente?", 
         ["A) A falta de verbas para a pesquisa espacial.", 
          "B) A discrepância persistente entre as medições da Constante de Hubble obtidas pelo universo local (supernovas) e pelo universo primordial (CMB).", 
          "C) O esgotamento do hidrogênio em todas as estrelas.", 
          "D) A colisão iminente entre galáxias e a Terra.", 
          "E) A impossibilidade de usar computadores na astronomia."], "B", 
         "Essa divergência em torno da taxa exata de expansão do universo desafia e instiga os físicos modernos."),

        ("Qual é a idade estimada do nosso universo atualmente aceita pela comunidade científica?", 
         ["A) Cerca de 6 mil anos", "B) 4,5 bilhões de anos", "C) Cerca de 13,8 bilhões de anos", "D) 100 bilhões de anos", "E) 500 milhões de anos"], "C", 
         "Medições precisas da radiação de fundo confirmam que o Big Bang ocorreu há aproximadamente 13,8 bilhões de anos."),

        ("Ao final desta jornada pelo Santuário, o que os participantes (futuros Cavaleiros de Athena) compreendem sobre o Cosmo?", 
         ["A) Que o cosmo é apenas uma ilusão sem leis físicas.", 
          "B) Que o verdadeiro cosmo está em harmonizar o poder interior com a compreensão racional das leis que regem a expansão, a gravidade e a estrutura do universo.", 
          "C) Que apenas a força física bruta resolve qualquer batalha.", 
          "D) Que a ciência e a mitologia são totalmente opostas e incompatíveis.", 
          "E) Que o universo foi construído por Makarius."], "B", 
         "A elevação do cosmo e o aprendizado científico unem-se para formar cavaleiros sábios, guardiões da justiça e da verdade no universo."]
    ]

    # Monta o banco estruturado com guia aleatório e limpo
    lista_formatada = []
    for i, q in enumerate(questoes_base):
        guia_escolhido = guias_cdz[i % len(guias_cdz)]
        lista_formatada.append({
            "id": i + 1,
            "guia": guia_escolhido,
            "enunciado": q[0],
            "opcoes": q[1],
            "correta": q[2],
            "por_que": q[3]
        })
    st.session_state.banco_50_questoes = lista_formatada

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
st.markdown("### *Treinamento das Equipes: Domine o Cosmo, a Relatividade e o Big Bang para se tornar Cavaleiro!*")
st.markdown("---")

# ==========================================
# PAINEL DO ORGANIZADOR (EXPORTAÇÃO WORD / TXT)
# ==========================================
st.sidebar.header("⚙️ Painel do Organizador")

with st.sidebar.expander("📚 Baixar Relatório / Prova (Word / TXT)"):
    st.markdown("Baixe todas as 50 questões do treinamento com alternativas e justificativas completas para usar em sala de aula, provas ou word:")
    
    texto_export = "====================================================\n"
    texto_export += "BANCO DE 50 QUESTÕES - CDZ COSMOLOGIA E O COSMO\n"
    texto_export += "====================================================\n\n"
    
    for q in st.session_state.banco_50_questoes:
        texto_export += f"Questão {q['id']} [Guia: {q['guia']}]\n"
        texto_export += f"Enunciado: {q['enunciado']}\n"
        for op in q['opcoes']:
            texto_export += f"   {op}\n"
        texto_export += f"-> Alternativa Correta: {q['correta']}\n"
        texto_export += f"-> Justificativa (O Porquê): {q['por_que']}\n"
        texto_export += "----------------------------------------------------\n\n"
        
    st.download_button(
        label="📥 Baixar Questões (.doc / Word)",
        data=texto_export,
        file_name="questoes_cdz_cosmologia.doc",
        mime="application/msword"
    )
    
    st.download_button(
        label="📥 Baixar Questões (.txt / Texto)",
        data=texto_export,
        file_name="questoes_cdz_cosmologia.txt",
        mime="text/plain"
    )

with st.sidebar.expander("🛠️ Histórico de Partidas"):
    if st.session_state.historico_respostas:
        for h in st.session_state.historico_respostas:
            st.text(f"[Q{h['questao']} - {h['equipe']}] {h['status']}")
        if st.button("🗑️ Limpar Histórico"):
            st.session_state.historico_respostas = []
            st.rerun()
    else:
        st.info("Nenhuma resposta registrada ainda.")

# Placar Geral das 3 Equipes na Barra Lateral
st.sidebar.header("📊 Placar & Estabilidade do Cosmo")
st.sidebar.metric(label="🛡️ Equipe Alfa (Pontos)", value=st.session_state.pontos_alfa)
st.sidebar.text(f"⚡ Estabilidade Alfa: {st.session_state.estabilidade_alfa}%")
st.sidebar.markdown("---")
st.sidebar.metric(label="🛡️ Equipe Beta (Pontos)", value=st.session_state.pontos_beta)
st.sidebar.text(f"⚡ Estabilidade Beta: {st.session_state.estabilidade_beta}%")
st.sidebar.markdown("---")
st.sidebar.metric(label="🛡️ Equipe Gama (Pontos)", value=st.session_state.pontos_gama)
st.sidebar.text(f"⚡ Estabilidade Gama: {st.session_state.estabilidade_gama}%")

# ==========================================
# INÍCIO DO JOGO
# ==========================================
lista_equipes = ["Equipe Alfa", "Equipe Beta", "Equipe Gama"]

if not st.session_state.jogo_iniciado:
    st.subheader("🔥 Cerimônia de Abertura: O Despertar do Cosmo")
    st.markdown("""
    > Jovens aspirantes de bronze reúnem-se no sopé do Santuário. Para se tornarem verdadeiros **Cavaleiros de Athena**, 
    > vocês não precisam apenas de força física, mas de **sabedoria cosmológica** — compreendendo o Big Bang, a Relatividade Geral de Einstein e a Matéria Escura.
    > 
    > As três equipes enfrentam agora os desafios em rodadas alternadas. Cada erro abala a **Estabilidade do Cosmo** individual da sua equipe!
    """)
    
    if st.button("🌟 Iniciar Jornada de Treinamento Rumo a Athena"):
        st.session_state.jogo_iniciado = True
        st.rerun()
    st.stop()

# ==========================================
# FLUXO DAS QUESTÕES DE MÚLTIPLA ESCHOLE (RODADAS)
# ==========================================
total_questoes = len(st.session_state.banco_50_questoes)
r_idx = st.session_state.rodada_atual - 1
e_idx = st.session_state.equipe_sub_idx
equipe_da_vez = lista_equipes[e_idx]

# Verifica estabilidade da equipe da vez
if equipe_da_vez == "Equipe Alfa":
    est_atual = st.session_state.estabilidade_alfa
elif equipe_da_vez == "Equipe Beta":
    est_atual = st.session_state.estabilidade_beta
else:
    est_atual = st.session_state.estabilidade_gama

if r_idx < total_questoes:
    q_atual = st.session_state.banco_questoes[r_idx]
    
    st.subheader(f"⚔️ **DESAFIO {st.session_state.rodada_atual} de {total_questoes}** | Vez de: **{equipe_da_vez}**")
    st.markdown(f"**Guia do Templo:** *{q_atual['guia']}* (Estabilidade da Equipe: **{est_atual}%**) ✨")
    st.markdown("---")
    
    st.markdown(f"### **Enigma:** {q_atual['enunciado']}")
    
    # Exibe as opções de múltipla escolha (A a E)
    escolha_usuario = st.radio("Selecione a alternativa correta:", q_atual['opcoes'], key=f"q_{r_idx}_{e_idx}")

    if st.button("Enviar Resposta e Elevar o Cosmo"):
        letra_escolhida = escolha_usuario.split(")")[0].strip()
        acertou = (letra_escolhida == q_atual['correta'])
        
        status = "CORRETA" if acertou else "INCORRETA"
        
        # Computa pontos e estabilidade por equipe
        if acertou:
            if equipe_da_vez == "Equipe Alfa": st.session_state.pontos_alfa += 20
            elif equipe_da_vez == "Equipe Beta": st.session_state.pontos_beta += 20
            else: st.session_state.pontos_gama += 20
        else:
            if equipe_da_vez == "Equipe Alfa": st.session_state.estabilidade_alfa = max(0, st.session_state.estabilidade_alfa - 10)
            elif equipe_da_vez == "Equipe Beta": st.session_state.estabilidade_beta = max(0, st.session_state.estabilidade_beta - 10)
            else: st.session_state.estabilidade_gama = max(0, st.session_state.estabilidade_gama - 10)

        # Salva histórico
        st.session_state.historico_respostas.append({
            "rodada": st.session_state.rodada_atual,
            "questao": q_atual['id'],
            "equipe": equipe_da_vez,
            "resposta": escolha_usuario,
            "status": status,
            "por_que": q_atual['por_que']
        })

        # Define feedback visual com a justificativa
        st.session_state.ultimo_feedback = {
            "status": status,
            "equipe": equipe_da_vez,
            "correta_letra": q_atual['correta'],
            "por_que": q_atual['por_que']
        }

        # Avança a sub-equipe (0 -> 1 -> 2) ou avança a rodada de questão
        if e_idx < 2:
            st.session_state.equipe_sub_idx += 1
        else:
            st.session_state.equipe_sub_idx = 0
            st.session_state.rodada_atual += 1
            
        st.rerun()

    # Mostra feedback e justificativa detalhada se houver resposta recente
    if st.session_state.ultimo_feedback:
        st.markdown("---")
        fb = st.session_state.ultimo_feedback
        if fb['status'] == "CORRETA":
            st.success(f"🎉 Excelente! A **{fb['equipe']}** acertou em cheio e elevou seu cosmo ao sétimo sentido!")
        else:
            st.error(f"❌ Resposta Incorreta da **{fb['equipe']}**. A alternativa correta era a letra **{fb['correta_letra']}**.")
            
        st.info(f"💡 **JUSTIFICATIVA (O PORQUÊ):**\n\n{fb['por_que']}")

else:
    # FASE FINAL: CHEGADA AO TETO DE ATHENA
    st.balloons()
    st.subheader("🏛️ Chegada Gloriosa ao Templo de Athena!")
    st.markdown("""
    > As 50 estações do Santuário foram vencidas! As equipes provaram seu valor, compreenderam as leis do Big Bang, 
    > da Relatividade Geral e da Matéria Escura, despertando o verdadeiro Cosmo supremo. 
    > Athena desce do altar principal para condecorar os novos Cavaleiros!
    """)
    
    st.markdown("---")
    st.markdown("### 🏆 **Placar Final dos Aspirantes a Cavaleiro**")
    st.markdown(f"* **🛡️ Equipe Alfa:** {st.session_state.pontos_alfa} pontos | Estabilidade: {st.session_state.estabilidade_alfa}%")
    st.markdown(f"* **🛡️ Equipe Beta:** {st.session_state.pontos_beta} pontos | Estabilidade: {st.session_state.estabilidade_beta}%")
    st.markdown(f"* **🛡️ Equipe Gama:** {st.session_state.pontos_gama} pontos | Estabilidade: {st.session_state.estabilidade_gama}%")
    
    pontuacoes = {
        "Equipe Alfa": st.session_state.pontos_alfa,
        "Equipe Beta": st.session_state.pontos_beta,
        "Equipe Gama": st.session_state.pontos_gama
    }
    vencedor = max(pontuacoes, key=pontuacoes.get)
    maior_pts = pontuacoes[vencedor]
    
    vencedores = [eq for eq, pts in pontuacoes.items() if pts == maior_pts]
    if len(vencedores) > 1:
        st.success(f"🤝 **Empate Lendário entre: {', '.join(vencedores)}! Todos tornaram-se Cavaleiros de Athena juntos!**")
    else:
        st.success(f"🥇 **A {vencedor} sagrou-se campeã com {maior_pts} pontos e recebeu o título supremo de Cavaleiros de Athena!**")

    st.markdown("---")
    if st.button("🔄 Reiniciar Novo Treinamento do Santuário"):
        st.session_state.jogo_iniciado = False
        st.session_state.rodada_atual = 1
        st.session_state.equipe_sub_idx = 0
        st.session_state.pontos_alfa = 0
        st.session_state.pontos_beta = 0
        st.session_state.pontos_gama = 0
        st.session_state.estabilidade_alfa = 100
        st.session_state.estabilidade_beta = 100
        st.session_state.estabilidade_gama = 100
        st.session_state.ultimo_feedback = None
        st.rerun()


