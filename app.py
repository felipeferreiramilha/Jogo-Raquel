import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="CDZ: O Despertar do Cosmo - Rumo a Athena", page_icon="🌌", layout="centered")

# ==========================================
# MAPEAMENTO DAS IMAGENS DOS CAVALEIROS
# ==========================================
IMAGENS_CAVALEIROS = {
    "Seiya de Pégaso": "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/Pegasus_Seiya.jpg/220px-Pegasus_Seiya.jpg",
    "Shiryu de Dragão": "https://upload.wikimedia.org/wikipedia/en/thumb/8/87/Dragon_Shiryu.jpg/220px-Dragon_Shiryu.jpg",
    "Hyoga de Cisne": "https://upload.wikimedia.org/wikipedia/en/thumb/7/7f/Cygnus_Hyoga.jpg/220px-Cygnus_Hyoga.jpg",
    "Shun de Andrômeda": "https://upload.wikimedia.org/wikipedia/en/thumb/7/7b/Andromeda_Shun.jpg/220px-Andromeda_Shun.jpg",
    "Ikki de Fênix": "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Phoenix_Ikki.jpg/220px-Phoenix_Ikki.jpg",
    "Mu de Áries": "https://upload.wikimedia.org/wikipedia/it/thumb/a/a2/Mu_di_Aries.jpg/200px-Mu_di_Aries.jpg",
    "Shaka de Virgem": "https://upload.wikimedia.org/wikipedia/it/thumb/e/e6/Virgo_Shaka.jpg/200px-Virgo_Shaka.jpg",
    "Aioria de Leão": "https://upload.wikimedia.org/wikipedia/it/thumb/c/c3/Aioria_di_Leo.jpg/200px-Aioria_di_Leo.jpg",
    "Dohko de Libra": "https://upload.wikimedia.org/wikipedia/it/thumb/d/d1/Dohko_di_Libra.jpg/200px-Dohko_di_Libra.jpg",
    "Camus de Aquário": "https://upload.wikimedia.org/wikipedia/it/thumb/0/03/Camus_di_Aquarius.jpg/200px-Camus_di_Aquarius.jpg"
}

# ==========================================
# INICIALIZAÇÃO DO ESTADO GLOBAL
# ==========================================
if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False
if "indice_pergunta" not in st.session_state:
    st.session_state.indice_pergunta = 0
if "equipe_sub_idx" not in st.session_state:
    st.session_state.equipe_sub_idx = 0  # 0: Alfa, 1: Beta, 2: Gama
if "pontos_alfa" not in st.session_state:
    st.session_state.pontos_alfa = 0
if "pontos_beta" not in st.session_state:
    st.session_state.pontos_beta = 0
if "pontos_gama" not in st.session_state:
    st.session_state.pontos_gama = 0
if "est_alfa" not in st.session_state:
    st.session_state.est_alfa = 100
if "est_beta" not in st.session_state:
    st.session_state.est_beta = 100
if "est_gama" not in st.session_state:
    st.session_state.est_gama = 100
if "ultimo_feedback" not in st.session_state:
    st.session_state.ultimo_feedback = None
if "historico_professor" not in st.session_state:
    st.session_state.historico_professor = []
if "prof_logado" not in st.session_state:
    st.session_state.prof_logado = False

# ==========================================
# BANCO COM 50 QUESTÕES DE MÚLTIPLA ESCOLHA
# ==========================================
if "banco_50" not in st.session_state:
    guias = ["Seiya de Pégaso", "Shiryu de Dragão", "Hyoga de Cisne", "Shun de Andrômeda", "Ikki de Fênix", "Mu de Áries", "Shaka de Virgem", "Aioria de Leão", "Dohko de Libra", "Camus de Aquário"]
    
    dados_brutos = [
        ("O astrofísico e padre belga Georges Lemaître foi o primeiro a propor que o universo começou a partir de um 'átomo primordial'. Décadas depois, astrônomos confirmaram que o espaço não é estático, mas está se expandindo continuamente a partir desse estado denso e quente inicial.",
         "Georges Lemaître",
         "O que postula o modelo cosmológico do Big Bang sobre a origem do Universo?", 
         ["A) O universo surgiu estático e eterno, sem alterações.", "B) O cosmos originou-se de uma singularidade extremamente densa e quente, expandindo-se desde então.", "C) As galáxias formaram-se de colisões de buracos negros estáticos.", "D) O universo expande-se porque estrelas criam matéria do nada.", "E) A origem cósmica é cíclica a cada 100 anos."], "B", 
         "O Big Bang descreve a expansão métrica do espaço a partir de um estado inicial de alta densidade e temperatura."),
        
        ("Para nos ajudar a visualizar o tecido do espaço se esticando, os físicos costumam usar a analogia de uma bexiga de aniversário. Quando desenhamos pontos na borracha e a enchemos de ar, percebemos que não são as marcas que caminham sozinhos, mas sim a borracha que se estica entre eles.",
         "Didática de Física Cosmológica",
         "Como a analogia do balão de festa preenchendo ar ajuda a entender a expansão do universo?", 
         ["A) Mostra que o balão cria ar novo do interior.", "B) Ilustra como os pontos na superfície se afastam porque o próprio espaço da borracha se expande.", "C) Comprova que o centro do balão é a única parte que se move.", "D) Indica paredes rígidas contendo o calor.", "E) Demonstra que a luz viaja mais rápido que o som."], "B", 
         "Assim como no balão, as galáxias se afastam porque o próprio tecido do espaço se estica."),
        
        ("Na década de 1920, no Observatório do Monte Wilson, o astrônomo norte-americano Edwin Hubble analisou a luz enviada por galáxias distantes. Ele notou que os comprimentos de onda de luz dessas galáxias estavam 'esticados', deslocados em direção à cor vermelha do espectro visível.",
         "Edwin Hubble",
         "Qual é a principal evidência observacional que comprova a expansão contínua do Universo?", 
         ["A) O desvio para o vermelho (redshift) das galáxias distantes, formulado na Lei de Hubble.", "B) A colisão frequente de planetas no sistema solar.", "C) O resfriamento rápido do Sol.", "D) A ausência completa de radiação no espaço.", "E) A rotação estática das estrelas fixas."], "A", 
         "O redshift demonstra que as ondas de luz esticam devido à expansão do próprio espaço."),
        
        ("Nos primeiros minutos após o Big Bang, o universo era um plasma denso e opaco de partículas carregadas. Cerca de 380 mil anos depois, com o resfriamento cósmico, os prótons e elétrons finalmente se uniram em átomos neutros de hidrogênio e hélio.",
         "George Gamow",
         "O que foi a Era da Recombinação nos instantes iniciais do Big Bang?", 
         ["A) O momento em que buracos negros engoliram a matéria.", "B) O período em que prótons e elétrons combinaram-se para formar átomos neutros, libertando a luz.", "C) A colisão entre a Via Láctea e Andrômeda.", "D) A fase em que a gravidade deixou de existir.", "E) O congelamento total do universo."], "B", 
         "Com a formação de átomos neutros, os fótons libertaram-se, tornando o universo transparente."),
        
        ("Em 1964, Arno Penzias e Robert Wilson testavam uma grande antena de rádio nos Estados Unidos quando detectaram um ruído de fundo persistente vindo de todas as direções do céu. Eles descobriram sem querer a radiação fóssil gerada no início do universo.",
         "Arno Penzias e Robert Wilson",
         "O que representa a Radiação Cósmica de Fundo em Micro-ondas (CMB)?", 
         ["A) O eco térmico remanescente dos primeiros momentos do Big Bang.", "B) A energia gerada por supernovas na Via Láctea.", "C) O calor emitido por buracos negros.", "D) Interferência de rádio alienígena.", "E) Luz refletida por poeira."], "A", 
         "A CMB é a radiação fóssil do universo primordial captada em todas as direções."),
        
        ("A matemática das equações da cosmologia prevê pontos teóricos onde a curvatura do espaço e a densidade da matéria atingem valores matematicamente infinitos, fazendo com que as leis físicas convencionais percam a capacidade de previsão.",
         "Stephen Hawking e Roger Penrose",
         "O que caracteriza uma singularidade no contexto cosmológico?", 
         ["A) Um planeta esférico perfeito.", "B) Um estado de densidade e temperatura infinitas onde as leis físicas conhecidas deixam de funcionar.", "C) Uma estrela hipergigante.", "D) O centro da órbita da Terra.", "E) Um cometa solitário."], "B", 
         "Na singularidade, grandezas físicas atingem valores infinitos antes da expansão."),
        
        ("Edwin Hubble mediu as velocidades de recessão e as distâncias das galáxias mais próximas. Suas observações demonstraram que quanto mais distante uma galáxia se encontra da Terra, mais rápido ela parece se afastar de nós.",
         "Edwin Hubble",
         "Qual cientista formulou a teoria da expansão corroborada pelo desvio para o vermelho?", 
         ["A) Isaac Newton", "B) Galileo Galilei", "C) Edwin Hubble", "D) Johannes Kepler", "E) Nikola Tesla"], "C", 
         "Edwin Hubble descobriu que quanto mais distante a galáxia, mais rápido ela se afasta."),
        
        ("A física moderna compreende que o tecido do espaço e a linha do tempo não eram recipientes vazios aguardando a matéria. Ambos foram criados e estruturados simultaneamente junto com o próprio Big Bang.",
         "Albert Einstein e Alexander Friedmann",
         "Antes do Big Bang, o que existia segundo a cosmologia padrão?", 
         ["A) Um oceano de estrelas.", "B) O espaço e o tempo não existiam da forma atual, estando toda matéria comprimida em singularidade.", "C) Um vácuo repleto de galáxias estáticas.", "D) Um buraco negro colossal.", "E) Matéria escura gasosa."], "B", 
         "O próprio espaço e o tempo surgiram com o evento do Big Bang."),
        
        ("Karl Schwarzschild resolveu as equações de Einstein para encontrar a geometria de um corpo denso no espaço. Ele definiu o raio crítico a partir do qual a velocidade de escape supera a velocidade da luz.",
         "Karl Schwarzschild",
         "O que é o Horizonte de Eventos em astrofísica?", 
         ["A) A borda de um planeta.", "B) O limite ao redor de um buraco negro além do qual nada, nem mesmo a luz, pode escapar.", "C) O limite do sistema solar.", "D) A distância máxima de um telescópio.", "E) O nascimento de uma supernova."], "B", 
         "O horizonte de eventos marca o ponto onde a gravidade impede qualquer escape."),
        
        ("Em 1980, o físico Alan Guth propôs que, uma fração minúscula de segundo após o Big Bang, o universo passou por uma fase de expansão exponencial extremamente rápida, resolvendo o mistério de como a temperatura do cosmos se tornou tão uniforme.",
         "Alan Guth",
         "O que foi a Teoria da Inflação Cósmica?", 
         ["A) A expansão lenta das estrelas.", "B) Um período de expansão exponencial ultrarrápida ocorrido logo após o Big Bang.", "C) O brilho de supernovas.", "D) A inflação de massa em buracos negros.", "E) A expansão do vento solar."], "B", 
         "A inflação cósmica resolveu problemas de homogeneidade e planura do universo."),
        
        ("Nos primeiros três minutos de existência do cosmos, a temperatura extrema permitiu que prótons e nêutrons se colidissem e se fundissem, dando origem aos primeiros e mais leves elementos químicos do universo.",
         "Fred Hoyle e Ralph Alpher",
         "Qual elemento químico leve predominou na nucleossíntese primordial?", 
         ["A) Ouro e Platina", "B) Urânio e Plutônio", "C) Hidrogênio e Hélio", "D) Ferro e Níquel", "E) Silício e Carbono"], "C", 
         "Formaram-se primordialmente núcleos de hidrogênio e hélio nos primeiros minutos."),
        
        ("Quando uma fonte de luz está se afastando do observador, as ondas emitidas chegam mais espaçadas. No espectro luminoso das galáxias, esse estiramento do comprimento de onda desloca a luz recebida em direção à cor vermelha.",
         "Christian Doppler e Vesto Slipher",
         "Por que a luz de galáxias distantes sofre redshift?", 
         ["A) As estrelas estão esfriando.", "B) O comprimento de onda da luz é esticado pela expansão do espaço entre nós e a galáxia.", "C) Há fumaça cósmica bloqueando a luz.", "D) Devido à rotação terrestre.", "E) Porque galáxias vermelhas são antigas."], "B", 
         "O estiramento do espaço estica o comprimento de onda dos fótons."),
        
        ("A relação matemática entre a distância de uma galáxia e sua velocidade de afastamento utiliza uma taxa proporcional de expansão fundamental para a cosmologia.",
         "Edwin Hubble e Georges Lemaître",
         "O que mede a Constante de Hubble?", 
         ["A) A rotação da Terra.", "B) A taxa atual de expansão do universo.", "C) A distância até o centro da galáxia.", "D) A massa total de hidrogênio.", "E) A gravidade solar."], "B", 
         "Quantifica a velocidade de afastamento das galáxias em função de sua distância."),
        
        ("O Princípio Cosmológico postula que, em escalas suficientemente grandes, o universo não possui lugares privilegiados ou direções preferenciais no espaço.",
         "Alexander Friedmann",
         "O que significa dizer que o universo é homogêneo e isotrópico?", 
         ["A) Ele é plano e feito de ferro.", "B) Tem a mesma aparência em qualquer lugar (homogêneo) e em todas as direções (isotrópico).", "C) Todas as estrelas têm a mesma idade.", "D) Possui um centro fixo.", "E) Temperatura zero absoluto."], "B", 
         "Este é o Princípio Cosmológico fundamental que rege os modelos cosmológicos."),
        
        ("Através da física nuclear aplicada ao início do cosmos, os astrônomos conseguem prever a abundância exata dos elementos leves primordiais e comparar com as medições feitas em estrelas antigas.",
         "George Gamow e Hans Bethe",
         "O que é a Nucleossíntese Primordial?", 
         ["A) Fusão em supernovas modernas.", "B) Criação dos primeiros núcleos atômicos leves durante os primeiros minutos do Big Bang.", "C) Formação de planetas rochosos.", "D) Destruição de átomos.", "E) Síntese de matéria escura."], "B", 
         "Processo em que a sopa primordial fundiu-se nos primeiros elementos químicos."),

        # Relatividade Geral (16 a 30)
        ("Em 1915, Albert Einstein revolucionou a física ao mostrar que o espaço e o tempo não são um palco fixo. Ele provou que objetos massivos como estrelas e planetas deformam a geometria ao seu redor.",
         "Albert Einstein",
         "Segundo a Relatividade Geral de Einstein, como a gravidade é explicada?", 
         ["A) Atração magnética direta.", "B) Curvatura do espaço-tempo quadridimensional provocada por massa e energia.", "C) Atrito do vento cósmico.", "D) Ilusão óptica.", "E) Partículas chamadas grávitons empurrando objetos."], "B", 
         "Massa e energia dizem ao espaço-tempo como se curvar."),
        
        ("Uma das previsões mais surpreendentes da Relatividade é que o tempo flui a ritmos diferentes dependendo da velocidade e da intensidade do campo gravitacional ao qual o relógio está submetido.",
         "Albert Einstein",
         "O que acontece com o tempo em campos gravitacionais intensos ou alta velocidade?", 
         ["A) O tempo passa mais rápido.", "B) O tempo desacelera (dilatação temporal) em relação a um observador distante.", "C) O tempo para totalmente.", "D) O tempo corre para trás.", "E) Não há alteração."], "B", 
         "A dilatação temporal é comprovada experimentalmente pela física moderna."),
        
        ("Durante o eclipse solar de 1919, a equipe liderada pelo astrofísico Arthur Eddington fotografou estrelas próximas ao bordo do Sol a partir da Ilha de Príncipe e de Sobral, no Brasil, comprovando a teoria de Einstein.",
         "Sir Arthur Eddington e Albert Einstein",
         "O que foi o eclipse solar de 1919 que consagrou a Relatividade Geral?", 
         ["A) Prova de que a Lua é de queijo.", "B) A observação de que a luz estelar sofre desvio ao passar perto do Sol devido à curvatura do espaço.", "C) Escurecimento por matéria escura.", "D) Colisão do Sol com buraco negro.", "E) Medição da luz."], "B", 
         "O desvio da luz estelar confirmou a curvatura do espaço predita por Einstein."),
        
        ("Cem anos após a previsão teórica de Einstein, os observatórios LIGO e VIRGO conseguiram detectar minúsculas oscilações na estrutura do espaço provocadas pela colisão catastrófica de dois buracos negros distantes.",
         "Albert Einstein e Colaboração LIGO",
         "O que são Ondas Gravitacionais?", 
         ["A) Ondas sonoras no vácuo.", "B) Perturbações no tecido do espaço-tempo geradas por eventos violentos como fusão de buracos negros.", "C) Ondas de rádio de pulsares.", "D) Raios cósmicos.", "E) Marés oceânicas."], "B", 
         "Ondas gravitacionais viajam esticando e comprimindo o próprio tecido do espaço."),
        
        ("Einstein percebeu em um 'pensamento feliz' que uma pessoa em queda livre não sente o próprio peso. Ele usou esse fato para deduzir que a gravidade e a aceleração provocam os mesmos efeitos físicos.",
         "Albert Einstein",
         "O princípio da equivalência de Einstein estabelece que:", 
         ["A) Toda matéria tem mesma massa.", "B) Efeitos gravitacionais são localmente indistinguíveis de aceleração constante.", "C) Massa e energia não se convertem.", "D) A velocidade da luz varia.", "E) A gravidade é fraca."], "B", 
         "Estar acelerando no espaço equivale a estar submetido a um campo gravitacional."),
        
        ("Hermann Minkowski, antigo professor de Einstein, percebeu que as três dimensões do espaço e a dimensão do tempo deviam ser fundidas em um único contínuo flexível quadridimensional.",
         "Hermann Minkowski",
         "O que é o espaço-tempo quadridimensional?", 
         ["A) Uma sala com quatro paredes.", "B) A união matemática das três dimensões espaciais com a dimensão temporal.", "C) Um holograma.", "D) Espaço dentro de buracos negros.", "E) Dimensões paralelas."], "B", 
         "O universo físico é um contínuo quadridimensional onde eventos ocorrem no espaço e tempo."),
        
        ("A gravidade ao redor de um objeto extremamente denso pode se tornar tão intensa que a velocidade necessária para escapar de seu campo atinge e supera a velocidade máxima do universo.",
         "John Wheeler e Karl Schwarzschild",
         "Por que a luz não escapa de um buraco negro?", 
         ["A) A luz desliga.", "B) A curvatura do espaço-tempo é tão extrema que todos os caminhos apontam para o centro.", "C) Há campo magnético repulsivo.", "D) A luz é pesada.", "E) O vácuo absorve a cor."], "B", 
         "Dentro do horizonte de eventos, escapar geometricamente do espaço curvado é impossível."),
        
        ("Os relógios atômicos a bordo dos satélites do sistema de navegação por satélite orbitam a milhares de quilômetros da Terra e em alta velocidade. Sem correções da física de Einstein, os mapas errariam a posição em quilômetros todos os dias.",
         "Engenharia e Física Relativística",
         "O que a Relatividade prevê sobre relógios em satélites GPS?", 
         ["A) Marcam o mesmo tempo.", "B) Sofrem ajustes relativísticos de velocidade e gravidade para funcionar com precisão.", "C) Param com o frio.", "D) Aceleram e quebram.", "E) O tempo passa mais devagar."], "B", 
         "Sem correções da Relatividade Geral e Especial, os mapas do GPS falhariam."),
        
        ("Quando a luz vinda de uma galáxia muito distante passa perto de um aglomerado galáctico massivo no meio do caminho, a massa do aglomerado funciona como uma lupa natural gigantesca no espaço.",
         "Fritz Zwicky e Albert Einstein",
         "O que é a Lente Gravitacional?", 
         ["A) Óculos de astrônomo.", "B) Efeito em que massas gigantescas curvam e amplificam a luz de objetos atrás delas.", "C) Lupa de quartzo.", "D) Luz estelar binária.", "E) Brilho de anéis planetários."], "B", 
         "A massa concentrada desvia a trajetória da luz de forma análoga a uma lente óptica."),
        
        ("A equação mais famosa da ciência moderna mostrou que uma quantidade minúscula de matéria contém uma quantidade colossal de energia concentrada.",
         "Albert Einstein",
         "Qual é a relação em E=mc^2?", 
         ["A) Massa e energia são independentes.", "B) Massa e energia são equivalentes e convertíveis entre si.", "C) Energia é sempre maior.", "D) Massa viaja na velocidade da luz.", "E) Sem relação com gravidade."], "B", 
         "Massa é uma forma de energia altamente concentrada."),

        ("Nas soluções matemáticas das equações de campo da gravidade, surgem pontes teóricas capazes de conectar dois pontos imensamente distantes do universo através do tecido dobrado do espaço-tempo.",
         "Albert Einstein e Nathan Rosen",
         "O que são buracos de minhoca (wormholes)?", 
         ["A) Túneis de minhocas.", "B) Atalhos hipotéticos conectando pontos distantes do espaço-tempo.", "C) Interior de estrelas de nêutrons.", "D) Partículas subatômicas.", "E) Fumaça de supernova."], "B", 
         "Permitidos matematicamente, sua existência real no cosmos permanece especulativa."),

        ("Quando uma estrela massiva esgota seu combustível nuclear e colapsa, os prótons e elétrons de seu núcleo são espremidos juntos com tanta força que formam um corpo superdenso de puro nêutron.",
         "Subrahmanyan Chandrasekhar e Walter Baade",
         "O que caracteriza uma estrela de nêutrons?", 
         ["A) Estrela de hidrogênio.", "B) Cadáver superdenso onde elétrons e prótons fundiram-se em nêutrons.", "C) Planeta gasoso gigante.", "D) Galáxia espiral.", "E) Órbita de buraco negro."], "B", 
         "Sua densidade é tão extrema que uma colher de chá pesaria bilhões de toneladas na Terra."),

        ("Ao contrário das teorias de Newton, a física moderna revelou que a geometria do espaço reage continuamente às mudanças e ao movimento da matéria.",
         "Albert Einstein",
         "O que significa dizer que o espaço é dinâmico?", 
         ["A) Muda de cor.", "B) É um meio flexível que curva, vibra e expande-se.", "C) Tem correntes de ar.", "D) Move-se de leste a oeste.", "E) Tem fricção."], "B", 
         "O tecido do espaço-tempo reage diretamente à presença de massa e energia."),

        ("A astrofísica Jocelyn Bell descobriu sinais periódicos de rádio extremamente precisos vindos do espaço. Mais tarde, confirmou-se que eram emitidos por estrelas de nêutrons em rápida rotação.",
         "Jocelyn Bell Burnell",
         "O que são pulsares?", 
         ["A) Planetas que piscam.", "B) Estrelas de nêutrons magnetizadas em rotação rápida emitindo feixes de radiação.", "C) Galáxias que pulsam.", "D) Cometas instáveis.", "E) Aglomerados globulares."], "B", 
         "Os feixes de varredura dos pulsares funcionam como relógios cosmológicos precisos."),

        ("A Teoria da Relatividade Especial demonstrou que, conforme um objeto com massa acelera, sua energia aumenta e impede que ele atinja ou supere a velocidade fundamental dos fótons no vácuo.",
         "Albert Einstein",
         "Qual é o limite máximo de velocidade para matéria e informação?", 
         ["A) Velocidade do som", "B) Velocidade da luz no vácuo (c)", "C) Gravidade quântica", "D) 1.000 km/s", "E) Sem limite"], "B", 
         "Nenhum corpo com massa de repouso consegue superar a velocidade da luz no vácuo."),

        # Matéria Escura e Energia Escura (31 a 50)
        ("Na década de 1970, a astrônoma Vera Rubin mediu as velocidades de rotação das estrelas nas bordas externas das galáxias espirais. Ela descobriu que as estrelas giravam rápido demais e deveriam ser arremessadas ao espaço, a menos que existisse muita matéria invisível ao redor.",
         "Vera Rubin e Kent Ford",
         "Qual é a função da Matéria Escura na estruturação cósmica?", 
         ["A) Emitir luz intensa.", "B) Atuar como cola gravitacional invisível mantendo galáxias coesas.", "C) Acelerar a expansão.", "D) Proteger contra raios gama.", "E) Absorver buracos negros."], "B", 
         "Fornece a atração gravitacional extra que mantém as galáxias unidas."),
        
        ("A cosmologia atual distingue dois grandes mistérios invisíveis no universo: um atua agregando a matéria por gravidade, enquanto o outro atua esticando o espaço cada vez mais rápido.",
         "Saul Perlmutter, Brian Schmidt e Adam Riess",
         "Qual a diferença entre Matéria Escura e Energia Escura?", 
         ["A) Matéria escura atrai (gravidade), energia escura repele (expansão acelerada).", "B) Fazem a mesma coisa.", "C) Energia escura é visível.", "D) Matéria escura empurra para fora.", "E) Sem diferença."], "A", 
         "Matéria escura aglutina a matéria visível; energia escura acelera a expansão."),
        
        ("Mapeamentos cosmológicos de alta precisão feitos por satélites espaciais revelaram que os átomos que compõem todas as estrelas, planetas e seres vivos formam apenas uma pequena fração de tudo o que existe no cosmos.",
         "Missão Espacial Planck (ESA)",
         "Qual a proporção aproximada no universo entre Matéria Escura, Energia Escura e Matéria Ordinária?", 
         ["A) 50% / 30% / 20%", "B) 90% / 5% / 5%", "C) Cerca de 68% energia escura, 27% matéria escura e 5% matéria ordinária.", "D) 99% / 1%", "E) 33% cada."], "C", 
         "O universo é amplamente dominado por componentes invisíveis de natureza desconhecida."),
        
        ("Diferente de nuvens de poeira ou gás interstelatório, a matéria escura não reflete luz, não brilha e não absorve radiação em nenhum comprimento de onda do espectro eletromagnético.",
         "Fritz Zwicky",
         "Por que a Matéria Escura é chamada de 'escura'?", 
         ["A) Bloqueia luz como tinta.", "B) Não emite, absorve ou reflete radiação eletromagnética detectável diretamente.", "C) Só existe na sombra.", "D) Cor escura dos planetas.", "E) Descoberta à noite."], "B", 
         "Ela é 'escura' porque não interage com a força eletromagnética, apenas com a gravidade."),
        
        ("Nos anos 1930, Fritz Zwicky observou o Aglomerado de Coma e percebeu que as galáxias se moviam rápido demais. Décadas depois, as curvas de rotação de Vera Rubin confirmaram que o mesmo acontecia dentro de galáxias individuais.",
         "Fritz Zwicky e Vera Rubin",
         "O que as curvas de rotação de galáxias revelaram?", 
         ["A) Massa concentrada no centro.", "B) Estrelas periféricas giram rápido demais, indicando halo massivo invisível.", "C) Galáxias paradas.", "D) Gravidade zero nas bordas.", "E) Buracos negros gêmeos."], "B", 
         "Provaram que existe muito mais massa invisível no halo galáctico do que matéria brilhante."),

        ("Ao estudar explosões de estrelas supernovas do Tipo Ia em galáxias muito distantes, duas equipes independentes de astrônomos descobriram em 1998 que a expansão do universo não está desacelerando, mas sim acelerando.",
         "Saul Perlmutter e Brian Schmidt",
         "O que provou que a expansão do universo está acelerando?", 
         ["A) Supernovas distantes tipo Ia na década de 1990.", "B) Cálculo da Lua.", "C) Colisão de Andrômeda.", "D) Campo magnético terrestre.", "E) Experimentos de laboratório."], "A", 
         "A medição do brilho de supernovas distantes comprovou a aceleração da expansão."),

        ("Ao formular a Relatividade Geral, Einstein adicionou um termo às suas equações para evitar que o universo colapsasse pela gravidade. Mais tarde, esse termo foi reescrito como a densidade de energia do próprio vácuo.",
         "Albert Einstein",
         "O que é a Constante Cosmológica de Einstein?", 
         ["A) Velocidade da luz.", "B) Termo matemático original para universo estático, hoje associado à energia escura.", "C) Peso do hidrogênio.", "D) Rotação solar.", "E) Distância até Andrômeda."], "B", 
         "Hoje a constante cosmológica representa a densidade constante de energia do vácuo."),

        ("Analisando imagens do espaço profundo, os astrônomos observam grupos contendo centenas de galáxias mergulhadas em gigantescas nuvens de gás quente e imensos halos de matéria escura.",
         "Fritz Zwicky",
         "O que são Aglomerados de Galáxias?", 
         ["A) Estrelas solitárias.", "B) Vastas estruturas de centenas ou milhares de galáxias mantidas pela gravidade.", "C) Anéis de poeira.", "D) Nuvens de gás frio.", "E) Sistemas planetários."], "B", 
         "Aglomerados galácticos são as maiores estruturas mantidas juntas pela atração gravitacional."),

        ("Computadores de alto desempenho simulam a gravidade atuando ao longo de bilhões de anos, mostrando que as galáxias se distribuem no espaço formando uma imensa teia tridimensional.",
         "Simulações de N-Corpos",
         "Qual o papel dos Filamentos Cósmicos?", 
         ["A) Conectar computadores.", "B) Formar pontes de matéria cercando vazios cósmicos.", "C) Conduzir raios solares.", "D) Trilhos de cometas.", "E) Luz pura."], "B", 
         "A teia cósmica organiza a matéria ao longo de pontes e filamentos densos."),

        ("Entre as grandes pontes de galáxias e matéria escura, existem imensas bolhas no universo onde quase não existem estrelas ou galáxias presentes.",
         "Mapeamento da Teia Cósmica",
         "O que são Vazios Cósmicos?", 
         ["A) Lugares onde o tempo para.", "B) Regiões do espaço com baixa densidade de galáxias entre filamentos.", "C) Centro de buracos negros.", "D) Espaço dentro do átomo.", "E) Regiões sem matéria escura."], "B", 
         "Os vazios cósmicos ocupam a maior parte do volume do universo observável."),

        ("Físicos de partículas propõem que a matéria escura pode ser formada por partículas elementares ainda não descobertas que possuem massa, mas interagem muito fracamente com a matéria comum.",
         "Física de Partículas",
         "O que significa WIMP em Matéria Escura?", 
         ["A) Weakly Interacting Massive Particles (Partículas Massivas de Interação Fraca).", "B) Waves in Microwave.", "C) White Dwarf.", "D) Wormhole Plasma.", "E) Water Isotope."], "A", 
         "WIMPs são as principais candidatas teóricas a compor a matéria escura fria."),

        ("Outra classe teórica promissora de partículas muito leves foi proposta originalmente para resolver um problema de simetria na força nuclear forte, podendo responder também pelo mistério da matéria escura.",
         "Roberto Peccei e Helen Quinn",
         "O que são Axions?", 
         ["A) Partículas elementares hipotéticas leves candidatas a matéria escura.", "B) Raios gama estelares.", "C) Menor unidade de tempo.", "D) Composição de Júpiter.", "E) Energia escura pura."], "A", 
         "Axions são hipotéticas partículas de baixa massa pesquisadas por detectores sensíveis."),

        ("Para permitir que as galáxias se formassem nos primeiros bilhões de anos após o Big Bang, as partículas invisíveis precisavam estar se movendo devagar em relação à velocidade da luz.",
         "Modelo Cosmológico Padrão (Lambda-CDM)",
         "O que é Matéria Escura Fria (CDM)?", 
         ["A) Gelo no espaço.", "B) Partículas que se movem devagar em comparação à velocidade da luz, modelando estruturas.", "C) Planetas congelados.", "D) Gás superaquecido.", "E) Órbitas próximas."], "B", 
         "O modelo de Matéria Escura Fria é o mais bem-sucedido na explicação das estruturas universais."),

        ("Com o avanço dos supercomputadores, físicos conseguem recriar a evolução gravitacional de bilhões de partículas virtuais desde os primeiros instantes após o Big Bang até os dias de hoje.",
         "Supercomputação Cosmológica",
         "Como simulações de N-corpos ajudam a cosmologia?", 
         ["A) Meteorologia da Terra.", "B) Simulando gravidade de milhões de partículas para recriar a teia cósmica.", "C) Traduzindo rádio alienígena.", "D) Mapas 2D.", "E) Órbita lunar."], "B", 
         "Recriam a evolução das estruturas cósmicas a partir de flutuações primordiais."),

        ("Considerando que a energia escura continue a acelerar a expansão do tecido do espaço, as galáxias distantes se afastarão tanto que suas luzes não alcançarão mais as vizinhas ao longo dos éons.",
         "Cosmologia do Futuro",
         "Qual o destino final mais provável do universo?", 
         ["A) Big Crunch.", "B) Expansão eterna acelerada (Big Freeze / Morte Térmica), ficando frio e escuro.", "C) Explosão de luz.", "D) Buracos brancos.", "E) Reversão temporal."], "B", 
         "O universo caminha para um resfriamento e isolamento gradual de suas galáxias."),

        ("O telescópio espacial da Agência Espacial Europeia mapeou a radiação infravermelha e de micro-ondas com sensibilidade milimétrica, revelando detalhes das flutuações do universo jovem.",
         "Agência Espacial Europeia (ESA)",
         "O que foi o experimento Planck da ESA?", 
         ["A) Viagem a Marte.", "B) Telescópio espacial que mapeou flutuações da Radiação Cósmica de Fundo.", "C) Acelerador subterrâneo.", "D) Satélite solar.", "E) Estudo de Vênus."], "B", 
         "Refinou a precisão da idade e da composição do cosmos."),

        ("Enquanto a matéria visível se dilui conforme o volume do espaço aumenta, a energia associada ao próprio vácuo mantém uma densidade constante por unidade de volume.",
         "Física do Vácuo Quântico",
         "Por que a energia escura não se dilui com a expansão?", 
         ["A) Criada por estrelas.", "B) É propriedade inerente ao vácuo; mais espaço significa mais vácuo e energia escura.", "C) Massa negativa.", "D) Viagem rápida.", "E) Interage com buracos negros."], "B", 
         "À medida que mais espaço surge, mais energia do vácuo passa a existir proporcionalmente."),

        ("Atualmente, as medições da taxa de expansão feitas observando supernovas locais discordam levemente dos valores obtidos ao analisar a radiação cósmica de fundo do universo jovem.",
         "Cosmologia Observacional Moderna",
         "O que é a 'Crise na Cosmologia' recente?", 
         ["A) Falta de verbas.", "B) Discrepância entre medições locais da Constante de Hubble e do universo primordial.", "C) Esgotamento de hidrogênio.", "D) Colisão iminente.", "E) Falta de computadores."], "B", 
         "Essa divergência nas medições instiga os astrônomos a revisarem os modelos cosmológicos."),

        ("Ao combinar as medições da radiação cósmica de fundo com a taxa de expansão e a abundância de elementos leves, os astrofísicos determinaram a idade do cosmos com margem de erro pequena.",
         "Equipe do Satélite WMAP e Planck",
         "Qual a idade estimada do universo?", 
         ["A) 6 mil anos", "B) 4,5 bilhões de anos", "C) Cerca de 13,8 bilhões de anos", "D) 100 bilhões", "E) 500 milhões"], "C", 
         "O universo possui aproximadamente 13,8 bilhões de anos de evolução."),

        ("Ao vencerem todos os desafios cosmológicos do Santuário, os aspirantes a Cavaleiro descobrem que dominar o Cosmo não é usar força destrutiva, mas harmonizar o espírito com a razão e as leis que regem a matéria e o espaço.",
         "O Ensinamento de Athena",
         "O que os participantes aprendem ao chegar ao topo do Santuário?", 
         ["A) O cosmo é ilusão.", "B) O verdadeiro cosmo une o poder interior à compreensão racional das leis do universo.", "C) Só força física importa.", "D) Ciência e mitologia são opostas.", "E) Universo feito por Makarius."], "B", 
         "O verdadeiro cosmo une o poder interior à compreensão racional das leis do universo.")
    ]

    lista_50 = []
    for i, q in enumerate(dados_brutos):
        guia = guias[i % len(guias)]
        lista_50.append({
            "guia": guia,
            "texto_base": q[0],
            "cientista": q[1],
            "enunciado": q[2],
            "opcoes": q[3],
            "correta": q[4],
            "por_que": q[5]
        })
    st.session_state.banco_50 = lista_50

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
        st.success("Sessão do Professor Ativa: **Felipe Ferreira**")
        if st.button("Sair da Conta"):
            st.session_state.prof_logado = False
            st.rerun()

# Conteúdo exclusivo para o Professor Logado
if st.session_state.prof_logado:
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📄 Exportar Relatório de Alunos")
    
    relatorio_txt = "====================================================\n"
    relatorio_txt += "RELATÓRIO DE RESPOSTAS DAS EQUIPES - PROFESSOR FELIPE FERREIRA\n"
    relatorio_txt += "====================================================\n\n"
    
    if st.session_state.historico_professor:
        for idx, item in enumerate(st.session_state.historico_professor, 1):
            relatorio_txt += f"Registro #{idx} | Equipe: {item['equipe']}\n"
            relatorio_txt += f"Guia: {item['guia']} | Cientista Relacionado: {item['cientista']}\n"
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

# Placar Geral e Estabilidade na Barra Lateral
st.sidebar.header("📊 Placar & Estabilidade")
st.sidebar.metric(label="🛡️ Equipe Alfa (Pontos)", value=st.session_state.pontos_alfa)
st.sidebar.text(f"⚡ Estabilidade Alfa: {st.session_state.est_alfa}%")
st.sidebar.markdown("---")
st.sidebar.metric(label="🛡️ Equipe Beta (Pontos)", value=st.session_state.pontos_beta)
st.sidebar.text(f"⚡ Estabilidade Beta: {st.session_state.est_beta}%")
st.sidebar.markdown("---")
st.sidebar.metric(label="🛡️ Equipe Gama (Pontos)", value=st.session_state.pontos_gama)
st.sidebar.text(f"⚡ Estabilidade Gama: {st.session_state.est_gama}%")

# ==========================================
# INÍCIO DO JOGO
# ==========================================
lista_equipes = ["Equipe Alfa", "Equipe Beta", "Equipe Gama"]

if not st.session_state.jogo_iniciado:
    st.subheader("🔥 Cerimônia de Abertura: O Despertar do Cosmo")
    st.markdown("""
    > Jovens aspirantes reúnem-se no sopé do Santuário. Para se tornarem verdadeiros **Cavaleiros de Athena**, 
    > vocês precisam dominar a **sabedoria cosmológica** — compreendendo o Big Bang, a Relatividade Geral e a Matéria Escura.
    > 
    > Em cada templo, um **Cavaleiro lendário** apresentará um texto sobre a história da física e o cientista por trás da descoberta antes da questão!
    """)
    
    if st.button("🌟 Iniciar Treinamento do Santuário"):
        st.session_state.jogo_iniciado = True
        st.rerun()
    st.stop()

# ==========================================
# FLUXO DAS QUESTÕES COM IMAGENS E NARRATIVA
# ==========================================
total_questoes = len(st.session_state.banco_50)
idx_p = st.session_state.indice_pergunta
e_idx = st.session_state.equipe_sub_idx
equipe_da_vez = lista_equipes[e_idx]

# Define estabilidade da equipe
if equipe_da_vez == "Equipe Alfa": est_atual = st.session_state.est_alfa
elif equipe_da_vez == "Equipe Beta": est_atual = st.session_state.est_beta
else: est_atual = st.session_state.est_gama

if idx_p < total_questoes:
    q_atual = st.session_state.banco_50[idx_p]
    
    st.subheader(f"⚔️ Vez de: **{equipe_da_vez}**")
    st.markdown(f"**Guia da Casa:** *{q_atual['guia']}* (Estabilidade da Equipe: **{est_atual}%**) ✨")
    
    # EXIBIÇÃO CENTRALIZADA DA IMAGEM DO CAVALEIRO
    if q_atual['guia'] in IMAGENS_CAVALEIROS:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image(IMAGENS_CAVALEIROS[q_atual['guia']], width=220, caption=f"Cavaleiro Guia: {q_atual['guia']}")

    st.markdown("---")
    
    # NARRATIVA DO CAVALEIRO + CIENTISTA
    st.info(f"📜 **Fala de {q_atual['guia']} sobre a História da Ciência:**\n\n\"{q_atual['texto_base']}\"\n\n🔬 **Cientista / Referência:** *{q_atual['cientista']}*")
    
    st.markdown(f"### **Enigma Cosmológico:**\n{q_atual['enunciado']}")
    
    escolha_usuario = st.radio("Selecione a alternativa correta:", q_atual['opcoes'], key=f"radio_{idx_p}_{e_idx}")

    if st.button("Enviar Resposta e Elevar o Cosmo"):
        letra_escolhida = escolha_usuario.split(")")[0].strip()
        acertou = (letra_escolhida == q_atual['correta'])
        
        status = "CORRETA" if acertou else "INCORRETA"
        
        if acertou:
            if equipe_da_vez == "Equipe Alfa": st.session_state.pontos_alfa += 20
            elif equipe_da_vez == "Equipe Beta": st.session_state.pontos_beta += 20
            else: st.session_state.pontos_gama += 20
        else:
            if equipe_da_vez == "Equipe Alfa": st.session_state.est_alfa = max(0, st.session_state.est_alfa - 10)
            elif equipe_da_vez == "Equipe Beta": st.session_state.est_beta = max(0, st.session_state.est_beta - 10)
            else: st.session_state.est_gama = max(0, st.session_state.est_gama - 10)

        # Envia para o relatório do professor
        st.session_state.historico_professor.append({
            "equipe": equipe_da_vez,
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
            "correta_letra": q_atual['correta'],
            "por_que": q_atual['por_que']
        }

        if e_idx < 2:
            st.session_state.equipe_sub_idx += 1
        else:
            st.session_state.equipe_sub_idx = 0
            st.session_state.indice_pergunta += 1
            
        st.rerun()

    if st.session_state.ultimo_feedback:
        st.markdown("---")
        fb = st.session_state.ultimo_feedback
        if fb['status'] == "CORRETA":
            st.success(f"🎉 Excelente! A **{fb['equipe']}** acertou e elevou seu cosmo ao sétimo sentido!")
        else:
            st.error(f"❌ Resposta Incorreta da **{fb['equipe']}**. A alternativa correta era a letra **{fb['correta_letra']}**.")
            
        st.info(f"💡 **JUSTIFICATIVA PEDAGÓGICA (O PORQUÊ):**\n\n{fb['por_que']}")

else:
    st.balloons()
    st.subheader("🏛️ Chegada Gloriosa ao Templo de Athena!")
    st.markdown("""
    > As estações do Santuário foram vencidas! As equipes provaram seu valor, compreenderam o Big Bang, 
    > a Relatividade Geral e a Matéria Escura, despertando o verdadeiro Cosmo supremo. 
    > Athena desce do altar principal para condecorar os novos Cavaleiros!
    """)
    
    st.markdown("---")
    st.markdown("### 🏆 **Placar Final dos Aspirantes a Cavaleiro**")
    st.markdown(f"* **🛡️ Equipe Alfa:** {st.session_state.pontos_alfa} pontos | Estabilidade: {st.session_state.est_alfa}%")
    st.markdown(f"* **🛡️ Equipe Beta:** {st.session_state.pontos_beta} pontos | Estabilidade: {st.session_state.est_beta}%")
    st.markdown(f"* **🛡️ Equipe Gama:** {st.session_state.pontos_gama} pontos | Estabilidade: {st.session_state.est_gama}%")
    
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
        st.session_state.indice_pergunta = 0
        st.session_state.equipe_sub_idx = 0
        st.session_state.pontos_alfa = 0
        st.session_state.pontos_beta = 0
        st.session_state.pontos_gama = 0
        st.session_state.est_alfa = 100
        st.session_state.est_beta = 100
        st.session_state.est_gama = 100
        st.session_state.ultimo_feedback = None
        st.rerun()
