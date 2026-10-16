import streamlit as st
import random
import urllib.request
import json
import urllib.parse
import html

# Configuração da página
st.set_page_config(
    page_title="Santuário da Cosmologia & Aetheris Web Pro", 
    page_icon="🌌", 
    layout="centered"
)

# Estilo visual limpo e escuro
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #ffffff; }
    .stButton>button {
        width: 100%; background-color: #1f4068; color: white;
        border-radius: 8px; font-weight: bold; border: 1px solid #00b4d8;
    }
    .stButton>button:hover { background-color: #00b4d8; color: black; }
    .card-resultado {
        background-color: #16213e; padding: 20px; border-radius: 10px;
        border: 1px solid #0f3460; margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

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
    idx = min(num_casa, len(CASAS_SANTUARIO) - 1)
    return CASAS_SANTUARIO[idx]

# ==========================================
# MOTOR DE PESQUISA WEB E CÁLCULOS COSMOLÓGICOS
# ==========================================
def pesquisar_na_web_avancado(termo):
    try:
        query_codificada = urllib.parse.quote(termo)
        url = f"https://pt.wikipedia.org/w/api.php?action=query&list=search&srsearch={query_codificada}&format=json&srlimit=5"
        
        req = urllib.request.Request(
            url, 
            headers={'User-Agent': 'Mozilla/5.0 (AetherisAstroResearchPro)'}
        )
        
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            search_results = data.get('query', {}).get('search', [])
            
            if search_results:
                artigos = []
                for item in search_results:
                    titulo = item['title']
                    snippet = html.unescape(item['snippet'].replace('<span class="searchmatch">', '').replace('</span>', ''))
                    artigos.append({"titulo": titulo, "resumo": f"{snippet}..."})
                return artigos
            else:
                return []
    except Exception as e:
        return [{"titulo": "Erro de Conexão", "resumo": f"Não foi possível conectar à rede de pesquisa: {e}"}]

def obter_equacoes_e_calculos_para_termo(termo):
    t = termo.lower()
    if "friedmann" in t or "expansão" in t or "big bang" in t:
        return {
            "titulo_eq": "Equações de Friedmann (Cosmologia Padrão)",
            "latex": r"\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G}{3}\rho - \frac{k}{a^2} + \frac{\Lambda}{3}",
            "explicacao": "Descrevem a expansão métrica do espaço em um universo homogêneo e isotrópico. Relacionam a taxa de expansão (Parâmetro de Hubble $H = \dot{a}/a$) com a densidade de energia $\\rho$, curvatura $k$ e constante cosmológica $\\Lambda$."
        }
    elif "relatividade" in t or "einstein" in t or "espaço-tempo" in t:
        return {
            "titulo_eq": "Equações de Campo de Einstein",
            "latex": r"R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R + g_{\mu\nu}\Lambda = \frac{8\pi G}{c^4} T_{\mu\nu}",
            "explicacao": "Conectam a geometria do espaço-tempo (tensor de curvatura de Ricci $R_{\mu\nu}$ e métrica $g_{\mu\nu}$) com a distribuição de matéria, momento e energia (tensor de energia-momento $T_{\mu\nu}$)."
        }
    elif "schwarzschild" in t or "buraco negro" in t or "horizonte" in t:
        return {
            "titulo_eq": "Raio de Schwarzschild (Horizonte de Eventos)",
            "latex": r"R_s = \frac{2GM}{c^2}",
            "explicacao": "Define o raio crítico em torno de uma massa $M$ onde a velocidade de escape atinge a velocidade da luz no vácuo ($c$), delimitando o horizonte de eventos de um buraco negro estático."
        }
    elif "hubble" in t or "redshift" in t or "galáxia" in t:
        return {
            "titulo_eq": "Lei de Hubble-Lemaître",
            "latex": r"v = H_0 \cdot d",
            "explicacao": "Estabelece que a velocidade de recessão $v$ de uma galáxia é proporcional à sua distância comensurável $d$, multiplicada pela Constante de Hubble atual $H_0$."
        }
    else:
        return {
            "titulo_eq": "Relação Geral de Massa-Energia e Dinâmica",
            "latex": r"E = mc^2 \quad \text{e} \quad ds^2 = -c^2 dt^2 + a(t)^2 d\Sigma^2",
            "explicacao": "Equivalência fundamental entre massa inercial e energia restrita, combinada com a métrica de Friedmann-Lemaître-Robertson-Walker (FLRW) para o estudo de métricas cósmicas."
        }

# ==========================================
# INICIALIZAÇÃO DO ESTADO GLOBAL
# ==========================================
if "modo_sistema" not in st.session_state:
    st.session_state.modo_sistema = "⚔️ Jogo: CDZ & Cosmologia"

if "jogo_iniciado" not in st.session_state:
    st.session_state.jogo_iniciado = False
if "indice_pergunta" not in st.session_state:
    st.session_state.indice_pergunta = 0
if "equipe_sub_idx" not in st.session_state:
    st.session_state.equipe_sub_idx = 0
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
if "historico_pesquisas" not in st.session_state:
    st.session_state.historico_pesquisas = []

# ==========================================
# BANCO DE 50 QUESTÕES (EQUILIBRADO A-E)
# ==========================================
if "banco_50" not in st.session_state:
    guias = [
        "Seiya de Pégaso", "Shiryu de Dragão", "Hyoga de Cisne", "Shun de Andrômeda", "Ikki de Fênix",
        "Mu de Áries", "Shaka de Virgem", "Aioria de Leão", "Dohko de Libra", "Camus de Aquário"
    ]
    
    dados_brutos = [
        # Bloco A (10 Questões)
        ("O astrofísico e padre belga Georges Lemaître foi o primeiro a propor que o universo começou a partir de um 'átomo primordial'.", "Georges Lemaître", "O que postula o modelo cosmológico do Big Bang?", ["A expansão métrica do espaço a partir de um estado inicial de altíssima densidade e temperatura.", "O universo surgiu estático e eterno.", "As galáxias formaram-se de colisões estáticas.", "O universo expande-se criando matéria.", "A origem cósmica é cíclica a cada 100 anos."], "A", "O Big Bang descreve a expansão métrica inicial."),
        ("Edwin Hubble analisou a luz enviada por galáxias distantes e notou o estiramento das ondas de luz.", "Edwin Hubble", "Qual a principal evidência da expansão do Universo?", ["O desvio para o vermelho (redshift) das galáxias distantes.", "A colisão de planetas no sistema solar.", "O resfriamento rápido do Sol.", "A ausência de radiação no espaço.", "A rotação estática das estrelas."], "A", "O redshift demonstra o estiramento das ondas de luz."),
        ("Penzias e Wilson detectaram um ruído de fundo persistente vindo de todas as direções do céu em 1964.", "Arno Penzias e Robert Wilson", "O que representa a Radiação Cósmica de Fundo (CMB)?", ["O eco térmico remanescente do Big Bang.", "A energia gerada por supernovas.", "O calor emitido por buracos negros.", "Interferência de rádio alienígena.", "Luz refletida por poeira."], "A", "A CMB é a radiação fóssil primordial."),
        ("A relação matemática entre a distância galáctica e a velocidade de afastamento.", "Edwin Hubble", "O que mede a Constante de Hubble?", ["A taxa atual de expansão do universo por unidade de distância.", "A velocidade de rotação da Terra.", "A distância até o centro galáctico.", "A massa total de hidrogênio.", "A gravidade solar."], "A", "Quantifica a taxa de expansão cósmica."),
        ("O Princípio Cosmológico estabelece propriedades fundamentais para o universo em larga escala.", "Alexander Friedmann", "O que significa o universo ser homogêneo e isotrópico?", ["Mesma aparência em qualquer lugar e em todas as direções.", "Ser totalmente plano e de ferro.", "Todas as estrelas terem mesma idade.", "Possuir um centro fixo no espaço.", "Temperatura zero absoluto."], "A", "Homogêneo e isotrópico definem o Princípio Cosmológico."),
        ("Durante o eclipse solar de 1919, astrônomos fotografaram estrelas próximas ao Sol.", "Arthur Eddington", "O que provou o eclipse de 1919?", ["A luz estelar sofre desvio ao passar perto do Sol devido à curvatura do espaço.", "A Lua é feita de rochas escuras.", "O universo tem matéria escura.", "O Sol colidiu com um buraco negro.", "A velocidade do som no espaço."], "A", "Confirmou a curvatura do espaço-tempo de Einstein."),
        ("Cem anos após Einstein, observatórios detectaram oscilações reais no tecido do espaço-tempo.", "Colaboração LIGO", "O que são Ondas Gravitacionais?", ["Perturbações no espaço-tempo geradas por eventos violentos como fusão de buracos negros.", "Ondas sonoras no vácuo.", "Ondas de rádio de pulsares.", "Raios cósmicos.", "Marés lunares."], "A", "São ondulações na geometria do espaço-tempo."),
        ("Vera Rubin mediu a rotação de estrelas em galáxias espirais e notou anomalias.", "Vera Rubin", "Qual a função da Matéria Escura?", ["Atuar como cola gravitacional invisível mantendo as galáxias coesas.", "Emitir luz intensa.", "Acelerar a expansão.", "Proteger contra raios gama.", "Absorver buracos negros."], "A", "Fornece a gravidade extra para unir as galáxias."),
        ("A cosmologia distingue dois componentes invisíveis dominantes.", "Saul Perlmutter", "Qual a diferença entre Matéria Escura e Energia Escura?", ["A matéria escura atrai (gravidade), enquanto a energia escura repele (acelera a expansão).", "Ambas fazem o mesmo.", "A energia escura é visível.", "A matéria escura empurra para fora.", "Não há diferença."], "A", "Atração vs Repulsão cósmica."),
        ("Estudos com supernovas Tipo Ia em 1998 surpreenderam a ciência.", "Saul Perlmutter", "O que provou a aceleração do universo?", ["A medição do brilho de supernovas distantes do tipo Ia.", "O cálculo da Lua.", "A colisão de Andrômeda.", "O campo magnético terrestre.", "Experimentos de laser."], "A", "Supernovas distantes comprovaram a aceleração."),

        # Bloco B (10 Questões)
        ("Físicos usam a analogia da borracha de um balão sendo inflada.", "Didática de Física", "Como o balão ajuda a entender a expansão?", ["Mostra a criação de ar interno.", "Ilustra como os pontos na superfície se afastam porque o próprio espaço da borracha se expande.", "Comprova o centro fixo.", "Indica paredes rígidas.", "Mostra que a luz viaja rápido."], "B", "O tecido do espaço que se estica."),
        ("Cerca de 380 mil anos após o Big Bang, prótons e elétrons formaram átomos.", "George Gamow", "O que foi a Era da Recombinação?", ["Buracos negros engoliram matéria.", "O período em que prótons e elétrons uniram-se em átomos neutros, libertando a luz.", "Colisão da Via Láctea.", "A gravidade cessou.", "Congelamento total."], "B", "Permitiu que a luz viajasse livremente."),
        ("Pontos de densidade extrema previstos pela relatividade.", "Stephen Hawking", "O que caracteriza uma singularidade?", ["Um planeta esférico.", "Um estado de densidade e temperatura infinitas onde as leis físicas param.", "Uma estrela hipergigante.", "O centro da órbita da Terra.", "Um cometa solitário."], "B", "Densidade infinita."),
        ("O espaço e o tempo surgiram juntos no evento inicial.", "Albert Einstein", "O que existia antes do Big Bang?", ["Um oceano de estrelas.", "O espaço e o tempo não existiam da forma atual, estando a matéria comprimida em singularidade.", "Um vácuo estático.", "Um buraco negro colossal.", "Matéria escura gasosa."], "B", "O tempo e o espaço iniciaram no Big Bang."),
        ("Karl Schwarzschild definiu o raio crítico de colapso.", "Karl Schwarzschild", "O que é o Horizonte de Eventos?", ["A borda de um planeta.", "O limite ao redor de um buraco negro além do qual nada, nem a luz, escapa.", "O limite do sistema solar.", "A distância de um telescópio.", "Nascimento de supernova."], "B", "Limite de escape gravitacional zero."),
        ("Alan Guth propôs uma fase de expansão exponencial ultrarrápida.", "Alan Guth", "O que foi a Teoria da Inflação?", ["Expansão lenta das estrelas.", "Um período de expansão exponencial ultrarrápida logo após o Big Bang.", "Brilho de supernovas.", "Inflação de massa.", "Vento solar."], "B", "Resolveu problemas de planura e homogeneidade."),
        ("Quando fontes de luz se afastam, as ondas chegam esticadas.", "Christian Doppler", "Por que ocorre o redshift?", ["Estrelas esfriando.", "O comprimento de onda da luz é esticado pela expansão do espaço.", "Fumaça cósmica.", "Rotação da Terra.", "Galáxias vermelhas velhas."], "B", "Estiramento do espaço estica o fóton."),
        ("Em 1915, Albert Einstein revolucionou a gravidade.", "Albert Einstein", "Como a Relatividade Geral explica a gravidade?", ["Atração magnética.", "Como a curvatura do espaço-tempo provocada por massa e energia.", "Atrito cósmico.", "Ilusão óptica.", "Grávitons empurrando."], "B", "Massa curva o espaço-tempo."),
        ("A Relatividade prevê alterações no ritmo dos relógios.", "Albert Einstein", "O que ocorre com o tempo sob forte gravidade?", ["Passa mais rápido.", "O tempo desacelera (dilatação temporal) em relação a um observador distante.", "Para totalmente.", "Corre para trás.", "Sem alteração."], "B", "Dilatação temporal gravitacional."),
        ("Satélites de GPS orbitam a alta velocidade e altitude.", "Engenharia Relativística", "O que a Relatividade prevê para o GPS?", ["Marcam o mesmo tempo.", "Necessitam de ajustes relativísticos de velocidade e gravidade para precisão.", "Param com o frio.", "Aceleram e quebram.", "Passam mais devagar."], "B", "Correções relativísticas evitam erros diários."),

        # Bloco C (10 Questões)
        ("Nos primeiros três minutos, a temperatura permitiu fusão nuclear primordial.", "Fred Hoyle", "Qual elemento leve predominou?", ["Ouro e Platina.", "Urânio e Plutônio.", "Hidrogênio e Hélio em vasta abundância.", "Ferro e Níquel.", "Silício e Carbono."], "C", "Predomínio de hidrogênio e hélio."),
        ("A composição do universo foi mapeada pelo satélite Planck.", "Missão Planck", "Qual a proporção aproximada no universo?", ["50% visível, 30% escura, 20% energia.", "90% ordinária.", "Cerca de 68% energia escura, 27% matéria escura e 5% ordinária.", "99% matéria escura.", "33% cada."], "C", "Domínio de componentes invisíveis."),
        ("Medições da CMB permitiram calcular a idade do cosmos.", "Equipe Planck", "Qual a idade estimada do universo?", ["6 mil anos.", "4,5 bilhões de anos.", "Cerca de 13,8 bilhões de anos.", "100 bilhões.", "500 milhões."], "C", "Aproximadamente 13,8 bilhões de anos."),
        ("Edwin Hubble mediu velocidades de afastamento das galáxias.", "Edwin Hubble", "Quem confirmou a expansão pelo redshift?", ["Isaac Newton.", "Galileo Galilei.", "Edwin Hubble ao analisar galáxias.", "Johannes Kepler.", "Nikola Tesla."], "C", "Hubble comprovou a expansão."),
        ("Einstein percebeu a equivalência entre aceleração e gravidade.", "Albert Einstein", "O que estabelece o Princípio da Equivalência?", ["Toda matéria tem mesma densidade.", "A gravidade é fraca.", "Efeitos de gravidade são localmente indistinguíveis de aceleração constante.", "A luz varia.", "Massa e energia não se convertem."], "C", "Aceleração equivale a campo gravitacional."),
        ("Minkowski uniu espaço e tempo em um contínuo.", "Hermann Minkowski", "O que é o espaço-tempo quadridimensional?", ["Uma sala com quatro paredes.", "Holograma.", "A união matemática das três dimensões espaciais com a temporal.", "Espaço interno de buracos negros.", "Dimensões paralelas."], "C", "3 dimensões espaciais + 1 temporal."),
        ("A equivalência entre massa e energia é dada por E=mc^2.", "Albert Einstein", "O que afirma a equivalência de massa e energia?", ["São independentes.", "Energia viaja devagar.", "Massa e energia são equivalentes e conversíveis entre si.", "Massa desaparece.", "Sem relação com gravidade."], "C", "Massa é energia concentrada."),
        ("O núcleo de estrelas massivas colapsa em estados ultradensos.", "Walter Baade", "O que caracteriza uma estrela de nêutrons?", ["Estrela de hidrogênio.", "Planeta gasoso.", "Cadáver superdenso onde elétrons e prótons fundiram-se em nêutrons.", "Galáxia espiral.", "Órbita de buraco negro."], "C", "Extrema densidade neutrônica."),
        ("O limite máximo de velocidade no universo.", "Albert Einstein", "Qual o limite máximo para matéria e informação?", ["Velocidade do som.", "Vento solar.", "A velocidade da luz no vácuo (c).", "1.000.000 km/s.", "Sem limite."], "C", "Nenhum corpo com massa supera c."),
        ("Físicos propõem partículas de matéria escura de interação fraca.", "Física de Partículas", "O que significa WIMP?", ["Waves In Microwave.", "Wormhole Plasma.", "Weakly Interacting Massive Particles.", "Water Isotope.", "White Dwarf."], "C", "Partículas massivas de interação fraca."),

        # Bloco D (10 Questões)
        ("Grandes massas curvam a luz de objetos ao fundo.", "Fritz Zwicky", "O que é a Lente Gravitacional?", ["Óculos astronômicos.", "Lupa de quartzo.", "Luz de Saturno.", "A curvatura e amplificação da luz estelar provocada por massas gigantescas.", "Brilho binário."], "D", "Desvio da luz por massa extrema."),
        ("Soluções das equações de Einstein sugerem atalhos cósmicos.", "Nathan Rosen", "O que são Buracos de Minhoca?", ["Túneis de insetos.", "Interior de anãs brancas.", "Partículas subatômicas.", "Atalhos hipotéticos conectando pontos distantes do espaço-tempo.", "Fumaça de supernova."], "D", "Pontes hipotéticas no espaço-tempo."),
        ("Estrelas de nêutrons magnetizadas em rotação.", "Jocelyn Bell", "O que são Pulsares?", ["Planetas que piscam.", "Galáxias oscilantes.", "Cometas caóticos.", "Estrelas de nêutrons em rotação rápida emitindo feixes regulares de radiação.", "Aglomerados."], "D", "Faróis cosmológicos naturais."),
        ("O termo original para manter o universo estático.", "Albert Einstein", "O que é a Constante Cosmológica?", ["Velocidade da luz.", "Peso do hidrogênio.", "Rotação solar.", "Termo matemático associado à energia do vácuo que impulsiona a expansão.", "Distância a Andrômeda."], "D", "Densidade de energia do vácuo."),
        ("A matéria distribui-se em uma grande rede tridimensional.", "Simulações N-Corpos", "Qual o papel dos Filamentos Cósmicos?", ["Conectar computadores.", "Conduzir raios solares.", "Trilhos de cometas.", "Formar pontes densas de matéria cercando vazios cósmicos.", "Emitir luz branca."], "D", "Estruturas que compõem a teia cósmica."),
        ("Regiões entre filamentos com baixíssima densidade.", "Mapeamento Profundo", "O que são os Vazios Cósmicos?", ["Lugares onde o tempo para.", "Centro de buracos negros.", "Espaço atômico.", "Enormes regiões com baixíssima densidade de galáxias.", "Regiões sem matéria escura."], "D", "Regiões de baixa densidade galáctica."),
        ("Partículas elementares leves propostas para simetria.", "Roberto Peccei", "O que são Axions?", ["Raios gama.", "Menor unidade temporal.", "Poeira de Júpiter.", "Partículas hipotéticas leves candidatas a matéria escura.", "Energia escura pura."], "D", "Candidatos leves a matéria escura."),
        ("Simulações computacionais recriam a evolução cósmica.", "Supercomputação", "Como simulações de N-corpos auxiliam a cosmologia?", ["Meteorologia da Terra.", "Traduzindo rádio alienígena.", "Mapas 2D.", "Simulando a gravidade de milhões de partículas para recriar a teia cósmica.", "Órbita lunar."], "D", "Recriação da teia cósmica via gravidade."),
        ("Modelos indicam o destino de longo prazo sob energia escura.", "Cosmologia Moderna", "Qual o destino final provável do universo?", ["Big Crunch.", "Explosão branca.", "Buracos brancos.", "Expansão eterna acelerada (Big Freeze), tornando-se frio e disperso.", "Reversão temporal."], "D", "Resfriamento e dispersão eterna."),
        ("Missões espaciais mapearam radiação fóssil com alta precisão.", "Agência ESA", "O que foi a missão Planck da ESA?", ["Viagem tripulada a Marte.", "Acelerador subterrâneo.", "Satélite solar.", "Telescópio que mapeou flutuações da Radiação Cósmica de Fundo.", "Estudo de Vênus."], "D", "Mapeamento da radiação de fundo."),

        # Bloco E (10 Questões)
        ("A energia do vácuo mantém propriedades distintas na expansão.", "Física Quântica", "Por que a Energia Escura não se dilui?", ["Fabricada por estrelas.", "Massa negativa.", "Viaja mais rápido que a luz.", "Interage com buracos negros.", "É propriedade do vácuo; mais espaço significa mais energia do vácuo."], "E", "Densidade de energia do vácuo constante por volume."),
        ("Divergências na taxa de expansão geram debates científicos.", "Cosmologia Moderna", "O que é a 'Crise na Cosmologia'?", ["Falta de verbas.", "Esgotamento de hidrogênio.", "Colisão iminente.", "Falta de computadores.", "Divergência entre medições locais da Constante de Hubble e do universo jovem."], "E", "Divergência entre dados locais e primordiais."),
        ("O objetivo da jornada une ciência e espírito.", "Ensinamento de Athena", "O que os aspirantes compreendem ao final?", ["Cosmo é ilusão.", "Força bruta resolve tudo.", "Ciência e mito são opostas.", "Universo feito por vilão.", "O verdadeiro cosmo une poder interior à compreensão racional das leis do universo."], "E", "Integração entre ciência, razão e cosmo."),
        ("Curvas de rotação espiral provam halos invisíveis.", "Vera Rubin", "O que revelaram as curvas de rotação?", ["Massa no núcleo.", "Galáxias paradas.", "Gravidade zero nas bordas.", "Buracos negros gêmeos.", "Estrelas periféricas giram rápido demais, indicando halo invisível."], "E", "Exigência de massa invisível periférica."),
        ("A matéria escura não interage com o eletromagnetismo.", "Fritz Zwicky", "Por que a Matéria Escura é 'escura'?", ["Bloqueia luz como tinta.", "Existe na sombra.", "Cor escura dos planetas.", "Descoberta à noite.", "Não emite, absorve ou reflete radiação eletromagnética."], "E", "Ausência de interação eletromagnética."),
        ("Aglomerados reúnem milhares de galáxias.", "Fritz Zwicky", "O que são Aglomerados de Galáxias?", ["Estrelas solitárias.", "Anéis de poeira.", "Nuvens de gás frio.", "Sistemas planetários caóticos.", "Vastas estruturas de centenas ou milhares de galáxias mantidas pela gravidade."], "E", "Maiores estruturas unidas pela gravidade."),
        ("O espaço reage ativamente à presença de massa.", "Albert Einstein", "O que significa o espaço ser dinâmico?", ["Muda de cor.", "Possui correntes de ar.", "Move-se de leste para oeste.", "Possui fricção mecânica.", "É um meio flexível que se curva, vibra e expande."], "E", "O espaço-tempo molda-se à matéria."),
        ("A luz não escapa do horizonte de eventos.", "Karl Schwarzschild", "Por que a luz não escapa de um buraco negro?", ["A luz desliga.", "Campo magnético repulsivo.", "Luz muito pesada.", "Vácuo absorve cor.", "A curvatura do espaço-tempo é tão extrema que todos os caminhos levam ao centro."], "E", "Geometria direcionada para a singularidade."),
        ("A expansão ultrarrápida inicial resolveu dilemas.", "Alan Guth", "Qual problema foi resolvido pela Inflação?", ["Cor de Marte.", "Face da Lua.", "Marés oceânicas.", "Oxigênio espacial.", "Problema do horizonte e da planura, explicando a homogeneidade da CMB."], "E", "Explicação da uniformidade térmica."),
        ("A cosmologia integra física, relatividade e astronomia.", "Georges Lemaître", "Qual a importância do estudo cosmológico?", ["Apenas memorizar fórmulas.", "Substituir ciência por mito.", "Provar que a Terra é o centro.", "Demonstrar que a física falha.", "Compreender a origem, evolução e leis fundamentais do espaço-tempo."], "E", "Compreensão ampla da história cósmica.")
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

def reiniciar_jogo():
    st.session_state.jogo_iniciado = False
    st.session_state.indice_pergunta = 0
    st.session_state.equipe_sub_idx = 0
    st.session_state.casas_alfa = 0
    st.session_state.casas_beta = 0
    st.session_state.casas_gama = 0
    st.session_state.ultimo_feedback = None

# ==========================================
# BARRA LATERAL: SELETOR DE MODO & PROFESSOR
# ==========================================
st.sidebar.header("🧭 Painel de Controle")
st.session_state.modo_sistema = st.sidebar.radio(
    "Escolha o Ambiente:",
    ["⚔️ Jogo: CDZ & Cosmologia", "✨ Aetheris: IA Cosmologia & Web Pro"]
)

st.sidebar.markdown("---")
st.sidebar.header("👨‍🏫 Área do Professor / Admin")

with st.sidebar.expander("🔑 Acesso Restrito"):
    if not st.session_state.prof_logado:
        login_input = st.text_input("Login")
        senha_input = st.text_input("Senha", type="password")
        if st.button("Entrar"):
            if login_input == "Felipe Ferreira" and senha_input == "Ff241198":
                st.session_state.prof_logado = True
                st.success("Logado com sucesso!")
                st.rerun()
            else:
                st.error("Credenciais inválidas.")
    else:
        st.success("Sessão Ativa: **Felipe Ferreira**")
        if st.button("Sair"):
            st.session_state.prof_logado = False
            st.rerun()

if st.session_state.prof_logado:
    st.sidebar.markdown("### 📄 Exportar Relatório")
    relatorio_txt = "====================================================\n"
    relatorio_txt += "RELATÓRIO DE RESPOSTAS - PROFESSOR FELIPE FERREIRA\n"
    relatorio_txt += "====================================================\n\n"
    
    if st.session_state.historico_professor:
        for idx, item in enumerate(st.session_state.historico_professor, 1):
            relatorio_txt += f"Registro #{idx} | Equipe: {item['equipe']} | Local: {item['casa_santuario']}\n"
            relatorio_txt += f"Guia: {item['guia']} | Cientista: {item['cientista']}\n"
            relatorio_txt += f"Enunciado: {item['enunciado']}\n"
            relatorio_txt += f"Resposta: {item['resposta']} | Status: {item['status']}\n"
            relatorio_txt += f"Justificativa: {item['por_que']}\n----------------------------------------------------\n"
    else:
        relatorio_txt += "Nenhum registro até o momento.\n"
        
    st.sidebar.download_button("📥 Baixar Relatório (.txt)", data=relatorio_txt, file_name="relatorio_desempenho.txt", mime="text/plain")
    if st.sidebar.button("🗑️ Limpar Relatório"):
        st.session_state.historico_professor = []
        st.sidebar.success("Limpo!")
        st.rerun()

# ==========================================
# MODO 1: JOGO CDZ & COSMOLOGIA
# ==========================================
if st.session_state.modo_sistema == "⚔️ Jogo: CDZ & Cosmologia":
    st.title("🏛️ CDZ: O Despertar do Cosmo - Rumo a Athena")
    st.markdown("### *Treinamento das Equipes: Domine o Cosmo, a Relatividade e o Big Bang!*")
    st.markdown("---")

    st.sidebar.markdown("---")
    st.sidebar.header("📊 Posição no Santuário (Meta: 12 Casas)")
    
    for nome_eq, casas_eq in [("Equipe Alfa", st.session_state.casas_alfa), 
                              ("Equipe Beta", st.session_state.casas_beta), 
                              ("Equipe Gama", st.session_state.casas_gama)]:
        c_str = obter_nome_casa(casas_eq)
        st.sidebar.markdown(f"🛡️ **{nome_eq}**\n*📍 {c_str}*")
        st.sidebar.progress(min(1.0, casas_eq / 12))
        st.sidebar.markdown("---")

    if st.sidebar.button("🔄 Reiniciar Partida do Jogo"):
        reiniciar_jogo()
        st.rerun()

    if not st.session_state.jogo_iniciado:
        st.subheader("🔥 Cerimônia de Abertura: O Despertar do Cosmo")
        st.markdown("""
        > Aspirantes reúnem-se no sopé do Santuário. Para se tornarem verdadeiros **Cavaleiros de Athena**, 
        > vocês avançarão pelas **12 Casas do Santuário** dominando a **sabedoria cosmológica** (Big Bang, Relatividade e Matéria Escura).
        > 
        > **Regras:**
        > * **Acerto:** Avança 1 Casa no Santuário!
        > * **Erro:** Não perde Casas, a questão muda imediatamente e a vez passa para a próxima equipe.
        > * **Vitória:** A primeira equipe a cruzar as 12 Casas e alcançar o Templo de Athena vence!
        """)
        if st.button("🌟 Iniciar Treinamento do Santuário"):
            st.session_state.jogo_iniciado = True
            st.rerun()
        st.stop()

    vencedor = None
    if st.session_state.casas_alfa >= 12: vencedor = "Equipe Alfa"
    elif st.session_state.casas_beta >= 12: vencedor = "Equipe Beta"
    elif st.session_state.casas_gama >= 12: vencedor = "Equipe Gama"

    if vencedor or st.session_state.indice_pergunta >= len(st.session_state.banco_50):
        st.balloons()
        st.subheader("🏛️ Chegada Gloriosa ao Templo de Athena!")
        if vencedor:
            st.success(f"🥇 **A {vencedor} atravessou as 12 Casas e conquistou a Armadura de Ouro no Templo de Athena!**")
        else:
            st.success("Fim das questões do Santuário! Todas as equipes demonstraram grande cosmo.")
        
        if st.button("🔄 Iniciar Novo Treinamento"):
            reiniciar_jogo()
            st.rerun()
        st.stop()

    lista_equipes = ["Equipe Alfa", "Equipe Beta", "Equipe Gama"]
    idx_p = st.session_state.indice_pergunta
    e_idx = st.session_state.equipe_sub_idx
    equipe_da_vez = lista_equipes[e_idx]

    if equipe_da_vez == "Equipe Alfa": casa_str = obter_nome_casa(st.session_state.casas_alfa)
    elif equipe_da_vez == "Equipe Beta": casa_str = obter_nome_casa(st.session_state.casas_beta)
    else: casa_str = obter_nome_casa(st.session_state.casas_gama)

    q_atual = st.session_state.banco_50[idx_p]

    chave_opcoes = f"opcoes_shuffled_{idx_p}"
    if chave_opcoes not in st.session_state:
        opcoes_copia = list(q_atual['opcoes_originais'])
        random.shuffle(opcoes_copia)
        opcoes_rotuladas = [f"{['A', 'B', 'C', 'D', 'E'][i]}) {t}" for i, t in enumerate(opcoes_copia)]
        st.session_state[chave_opcoes] = opcoes_rotuladas

    st.warning(f"📍 **{equipe_da_vez} encontra-se em:** {casa_str}")
    st.subheader(f"⚔️ Vez da: **{equipe_da_vez}**")
    st.markdown(f"**Guia da Casa:** *{q_atual['guia']}* ✨")
    st.markdown("---")
    
    st.info(f"📜 **Fala de {q_atual['guia']} sobre a História da Ciência:**\n\n\"{q_atual['texto_base']}\"\n\n🔬 **Cientista / Referência:** *{q_atual['cientista']}*")
    st.markdown(f"### **Enigma Cosmológico:**\n{q_atual['enunciado']}")

    escolha_usuario = st.radio("Selecione a alternativa:", st.session_state[chave_opcoes], key=f"radio_{idx_p}_{e_idx}")

    if st.button("Enviar Resposta e Elevar o Cosmo"):
        texto_selec = escolha_usuario.split(") ", 1)[1].strip()
        acertou = (texto_selec == q_atual['correta_texto'])
        status = "CORRETA" if acertou else "INCORRETA"

        if acertou:
            if equipe_da_vez == "Equipe Alfa": st.session_state.casas_alfa += 1
            elif equipe_da_vez == "Equipe Beta": st.session_state.casas_beta += 1
            else: st.session_state.casas_gama += 1

        st.session_state.indice_pergunta += 1
        st.session_state.equipe_sub_idx = (e_idx + 1) % 3

        st.session_state.historico_professor.append({
            "equipe": equipe_da_vez, "casa_santuario": casa_str,
            "guia": q_atual['guia'], "cientista": q_atual['cientista'],
            "enunciado": q_atual['enunciado'], "resposta": escolha_usuario,
            "status": status, "por_que": q_atual['por_que']
        })

        st.session_state.ultimo_feedback = {"status": status, "equipe": equipe_da_vez, "correta_texto": q_atual['correta_texto'], "por_que": q_atual['por_que']}
        st.rerun()

    if st.session_state.ultimo_feedback:
        st.markdown("---")
        fb = st.session_state.ultimo_feedback
        if fb['status'] == "CORRETA":
            st.success(f"🎉 Excelente! A **{fb['equipe']}** acertou e avançou no Santuário!")
        else:
            st.error(f"❌ Incorreta da **{fb['equipe']}**. A correta era: *\"{fb['correta_texto']}\"*. A vez passou!")
        st.info(f"💡 **Justificativa Pedagógica:**\n\n{fb['por_que']}")

# ==========================================
# MODO 2: IA AETHERIS COM WEB SEARCH PRO & EQUAÇÕES
# ==========================================
elif st.session_state.modo_sistema == "✨ Aetheris: IA Cosmologia & Web Pro":
    st.title("✨ Aetheris: Web Search Pro & Equações Físicas")
    st.markdown("### *Mecanismo de busca acadêmica avançada com extração automática de equações e cálculos.*")
    st.markdown("---")

    col_b1, col_b2 = st.columns([3, 1])
    with col_b1:
        termo_pesquisa = st.text_input("Pesquisar na Web por conceitos, cientistas ou teorias (ex: Friedmann equations, Dark Matter, James Webb):", placeholder="Digite o tema da pesquisa...")
    with col_b2:
        st.markdown("<br>", unsafe_allow_html=True)
        btn_buscar = st.button("🔍 Pesquisar na Web")

    if btn_buscar and termo_pesquisa.strip():
        with st.spinner("Varrendo bases públicas e estruturando equações..."):
            artigos_encontrados = pesquisar_na_web_avancado(termo_pesquisa)
            dados_mat = obter_equacoes_e_calculos_para_termo(termo_pesquisa)
            
            # Salva no histórico de pesquisas da sessão
            st.session_state.historico_pesquisas.insert(0, {
                "termo": termo_pesquisa,
                "artigos": artigos_encontrados,
                "matematica": dados_mat
            })

    # Botão para limpar o histórico de pesquisas
    if st.session_state.historico_pesquisas:
        if st.button("🗑️ Limpar Histórico de Pesquisas"):
            st.session_state.historico_pesquisas = []
            st.rerun()

    st.markdown("---")

    # Exibe as páginas de resultados organizadas
    if st.session_state.historico_pesquisas:
        st.markdown("## 📑 Páginas de Resultados da Pesquisa Web")
        
        for idx, pesquisa in enumerate(st.session_state.historico_pesquisas):
            with st.container():
                st.markdown(f"""
                <div class="card-resultado">
                    <h3>🔍 Pesquisa #{len(st.session_state.historico_pesquisas) - idx}: <em>{pesquisa['termo']}</em></h3>
                </div>
                """, unsafe_allow_html=True)
                
                # Bloco de Equações e Cálculos Físicos Extraídos
                st.markdown("#### 📐 Equações Fundamentais e Cálculos Associados:")
                eq = pesquisa['matematica']
                st.markdown(f"**{eq['titulo_eq']}**")
                st.latex(eq['latex'])
                st.markdown(f"*Análise Física:* {eq['explicacao']}")
                
                st.markdown("---")
                st.markdown("#### 🌐 Fontes e Artigos Encontrados na Varredura Web:")
                for art in pesquisa['artigos']:
                    st.markdown(f"* **{art['titulo']}**\n  > {art['resumo']}")
                
                st.markdown("---")
    else:
        st.info("Nenhuma pesquisa realizada ainda. Insira um termo acima e clique em 'Pesquisar na Web'.")
