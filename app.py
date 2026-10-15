import streamlit as st
import random

# Configuração da página
st.set_page_config(page_title="CDZ: O Despertar do Cosmo", page_icon="🌌", layout="centered")

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
if "historico" not in st.session_state:
    st.session_state.historico = []

# ==========================================
# BANCO COM 50 QUESTÕES DE MÚLTIPLA ESCOLHA (A a E)
# ==========================================
if "banco_50" not in st.session_state:
    guias = ["Seiya de Pégaso", "Shiryu de Dragão", "Hyoga de Cisne", "Shun de Andrômeda", "Ikki de Fênix", "Mu de Áries", "Shaka de Virgem", "Aioria de Leão", "Dohko de Libra", "Camus de Aquário"]
    
    dados_brutos = [
        ("O que postula o modelo cosmológico do Big Bang sobre a origem do Universo?", 
         ["A) O universo surgiu estático e eterno, sem alterações.", "B) O cosmos originou-se de uma singularidade extremamente densa e quente, expandindo-se desde então.", "C) As galáxias formaram-se de colisões de buracos negros estáticos.", "D) O universo expande-se porque estrelas criam matéria do nada.", "E) A origem cósmica é cíclica a cada 100 anos."], "B", 
         "O Big Bang descreve a expansão métrica do espaço a partir de um estado inicial de alta densidade e temperatura."),
        
        ("Como a analogia do balão de festa preenchendo ar ajuda a entender a expansão do universo?", 
         ["A) Mostra que o balão cria ar novo do interior.", "B) Ilustra como os pontos na superfície se afastam porque o próprio espaço da borracha se expande.", "C) Comprova que o centro do balão é a única parte que se move.", "D) Indica paredes rígidas contendo o calor.", "E) Demonstra que a luz viaja mais rápido que o som."], "B", 
         "Assim como no balão, as galáxias se afastam porque o próprio tecido do espaço se estica."),
        
        ("Qual é a principal evidência observacional que comprova a expansão contínua do Universo?", 
         ["A) O desvio para o vermelho (redshift) das galáxias distantes, formulado na Lei de Hubble.", "B) A colisão frequente de planetas no sistema solar.", "C) O resfriamento rápido do Sol.", "D) A ausência completa de radiação no espaço.", "E) A rotação estática das estrelas fixas."], "A", 
         "O redshift demonstra que as ondas de luz esticam devido à expansão do espaço."),
        
        ("O que foi a Era da Recombinação nos instantes iniciais do Big Bang?", 
         ["A) O momento em que buracos negros engoliram a matéria.", "B) O período em que prótons e elétrons combinaram-se para formar átomos neutros, libertando a luz.", "C) A colisão entre a Via Láctea e Andrômeda.", "D) A fase em que a gravidade deixou de existir.", "E) O congelamento total do universo."], "B", 
         "Com a formação de átomos neutros, os fótons libertaram-se, gerando a Radiação Cósmica de Fundo."),
        
        ("O que representa a Radiação Cósmica de Fundo em Micro-ondas (CMB)?", 
         ["A) O eco térmico remanescente dos primeiros momentos do Big Bang.", "B) A energia gerada por supernovas na Via Láctea.", "C) O calor emitido por buracos negros.", "D) Interferência de rádio alienígena.", "E) Luz refletida por poeira."], "A", 
         "A CMB é a radiação fóssil do universo primordial captada em todas as direções."),
        
        ("O que caracteriza uma singularidade no contexto cosmológico?", 
         ["A) Um planeta esférico perfeito.", "B) Um estado de densidade e temperatura infinitas onde as leis físicas conhecidas deixam de funcionar.", "C) Uma estrela hipergigante.", "D) O centro da órbita da Terra.", "E) Um cometa solitário."], "B", 
         "Na singularidade, grandezas físicas atingem valores infinitos antes da expansão."),
        
        ("Qual cientista formulou a teoria da expansão corroborada pelo desvio para o vermelho?", 
         ["A) Isaac Newton", "B) Galileo Galilei", "C) Edwin Hubble", "D) Johannes Kepler", "E) Nikola Tesla"], "C", 
         "Edwin Hubble descobriu que quanto mais distante a galáxia, mais rápido ela se afasta."),
        
        ("Antes do Big Bang, o que existia segundo a cosmologia padrão?", 
         ["A) Um oceano de estrelas.", "B) O espaço e o tempo não existiam da forma atual, estando toda matéria comprimida em singularidade.", "C) Um vácuo repleto de galáxias estáticas.", "D) Um buraco negro colossal.", "E) Matéria escura gasosa."], "B", 
         "O próprio espaço e o tempo surgiram com o evento do Big Bang."),
        
        ("O que é o Horizonte de Eventos em astrofísica?", 
         ["A) A borda de um planeta.", "B) O limite ao redor de um buraco negro além do qual nada, nem mesmo a luz, pode escapar.", "C) O limite do sistema solar.", "D) A distância máxima de um telescópio.", "E) O nascimento de uma supernova."], "B", 
         "O horizonte de eventos marca o ponto onde a gravidade impede qualquer escape."),
        
        ("O que foi a Teoria da Inflação Cósmica?", 
         ["A) A expansão lenta das estrelas.", "B) Um período de expansão exponencial ultrarrápida ocorrido logo após o Big Bang.", "C) O brilho de supernovas.", "D) A inflação de massa em buracos negros.", "E) A expansão do vento solar."], "B", 
         "A inflação cósmica resolveu problemas de homogeneidade e planura do universo."),
        
        ("Qual elemento químico leve predominou na nucleossíntese primordial?", 
         ["A) Ouro e Platina", "B) Urânio e Plutônio", "C) Hidrogênio e Hélio", "D) Ferro e Níquel", "E) Silício e Carbono"], "C", 
         "Formaram-se primordialmente núcleos de hidrogênio e hélio nos primeiros minutos."),
        
        ("Por que a luz de galáxias distantes sofre redshift?", 
         ["A) As estrelas estão esfriando.", "B) O comprimento de onda da luz é esticado pela expansão do espaço entre nós e a galáxia.", "C) Há fumaça cósmica bloqueando a luz.", "D) Devido à rotação terrestre.", "E) Porque galáxias vermelhas são antigas."], "B", 
         "O estiramento do espaço estica o comprimento de onda dos fótons."),
        
        ("O que mede a Constante de Hubble?", 
         ["A) A rotação da Terra.", "B) A taxa atual de expansão do universo.", "C) A distância até o centro da galáxia.", "D) A massa total de hidrogênio.", "E) A gravidade solar."], "B", 
         "Quantifica a velocidade de afastamento das galáxias em função de sua distância."),
        
        ("O que significa dizer que o universo é homogêneo e isotrópico?", 
         ["A) Ele é plano e feito de ferro.", "B) Tem a mesma aparência em qualquer lugar (homogêneo) e em todas as direções (isotrópico).", "C) Todas as estrelas têm a mesma idade.", "D) Possui um centro fixo.", "E) Temperatura zero absoluto."], "B", 
         "Este é o Princípio Cosmológico fundamental."),
        
        ("O que é a Nucleossíntese Primordial?", 
         ["A) Fusão em supernovas modernas.", "B) Criação dos primeiros núcleos atômicos leves durante os primeiros minutos do Big Bang.", "C) Formação de planetas rochosos.", "D) Destruição de átomos.", "E) Síntese de matéria escura."], "B", 
         "Processo em que a sopa primordial fundiu-se nos primeiros elementos químicos."),

        # Relatividade Geral (16 a 30)
        ("Segundo a Relatividade Geral de Einstein, como a gravidade é explicada?", 
         ["A) Atração magnética direta.", "B) Curvatura do espaço-tempo quadridimensional provocada por massa e energia.", "C) Atrito do vento cósmico.", "D) Ilusão óptica.", "E) Partículas chamadas grávitons empurrando objetos."], "B", 
         "Massa e energia dizem ao espaço-tempo como se curvar."),
        
        ("O que acontece com o tempo em campos gravitacionais intensos ou alta velocidade?", 
         ["A) O tempo passa mais rápido.", "B) O tempo desacelera (dilatação temporal) em relação a um observador distante.", "C) O tempo para totalmente.", "D) O tempo corre para trás.", "E) Não há alteração."], "B", 
         "A dilatação temporal é comprovada pela Relatividade."),
        
        ("O que foi o eclipse solar de 1919 que consagrou a Relatividade Geral?", 
         ["A) Prova de que a Lua é de queijo.", "B) A observação de que a luz estelar sofre desvio ao passar perto do Sol devido à curvatura do espaço.", "C) Escurecimento por matéria escura.", "D) Colisão do Sol com buraco negro.", "E) Medição da luz."], "B", 
         "O desvio da luz estelar confirmou a curvatura predita por Einstein."),
        
        ("O que são Ondas Gravitacionais?", 
         ["A) Ondas sonoras no vácuo.", "B) Perturbações no tecido do espaço-tempo geradas por eventos violentos como fusão de buracos negros.", "C) Ondas de rádio de pulsares.", "D) Raios cósmicos.", "E) Marés oceânicas."], "B", 
         "Viajam esticando e comprimindo o próprio tecido do espaço."),
        
        ("O princípio da equivalência de Einstein estabelece que:", 
         ["A) Toda matéria tem mesma massa.", "B) Efeitos gravitacionais são localmente indistinguíveis de aceleração constante.", "C) Massa e energia não se convertem.", "D) A velocidade da luz varia.", "E) A gravidade é fraca."], "B", 
         "Estar acelerando no espaço equivale a estar em campo gravitacional."),
        
        ("O que é o espaço-tempo quadridimensional?", 
         ["A) Uma sala com quatro paredes.", "B) A união matemática das três dimensões espaciais com a dimensão temporal.", "C) Um holograma.", "D) Espaço dentro de buracos negros.", "E) Dimensões paralelas."], "B", 
         "O universo físico é um contínuo onde eventos ocorrem em espaço e tempo."),
        
        ("Por que a luz não escapa de um buraco negro?", 
         ["A) A luz desliga.", "B) A curvatura do espaço-tempo é tão extrema que todos os caminhos apontam para o centro.", "C) Há campo magnético repulsivo.", "D) A luz é pesada.", "E) O vácuo absorve a cor."], "B", 
         "Dentro do horizonte de eventos, escapar geometricamente é impossível."),
        
        ("O que a Relatividade prevê sobre relógios em satélites GPS?", 
         ["A) Marcam o mesmo tempo.", "B) Sofrem ajustes relativísticos de velocidade e gravidade para funcionar com precisão.", "C) Param com o frio.", "D) Aceleram e quebram.", "E) O tempo passa mais devagar."], "B", 
         "Sem correções relativísticas, o GPS falharia."),
        
        ("O que é a Lente Gravitacional?", 
         ["A) Óculos de astrônomo.", "B) Efeito em que massas gigantescas curvam e amplificam a luz de objetos atrás delas.", "C) Lupa de quartzo.", "D) Luz estelar binária.", "E) Brilho de anéis planetários."], "B", 
         "A massa desvia a trajetória da luz de forma análoga a uma lente."),
        
        ("Qual é a relação em E=mc^2?", 
         ["A) Massa e energia são independentes.", "B) Massa e energia são equivalentes e convertíveis entre si.", "C) Energia é sempre maior.", "D) Massa viaja na velocidade da luz.", "E) Sem relação com gravidade."], "B", 
         "Massa é energia concentrada."),

        ("O que são buracos de minhoca (wormholes)?", 
         ["A) Túneis de minhocas.", "B) Atalhos hipotéticos conectando pontos distantes do espaço-tempo.", "C) Interior de estrelas de nêutrons.", "D) Partículas subatômicas.", "E) Fumaça de supernova."], "B", 
         "Permitidos matematicamente, mas sua existência real é especulativa."),

        ("O que caracteriza uma estrela de nêutrons?", 
         ["A) Estrela de hidrogênio.", "B) Cadáver superdenso onde elétrons e prótons fundiram-se em nêutrons.", "C) Planeta gasoso gigante.", "D) Galáxia espiral.", "E) Órbita de buraco negro."], "B", 
         "Sua densidade é extrema."),

        ("O que significa dizer que o espaço é dinâmico?", 
         ["A) Muda de cor.", "B) É um meio flexível que curva, vibra e expande-se.", "C) Tem correntes de ar.", "D) Move-se de leste a oeste.", "E) Tem fricção."], "B", 
         "O espaço-tempo reage à matéria e energia."),

        ("O que são pulsares?", 
         ["A) Planetas que piscam.", "B) Estrelas de nêutrons magnetizadas em rotação rápida emitindo feixes de radiação.", "C) Galáxias que pulsam.", "D) Cometas instáveis.", "E) Aglomerados globulares."], "B", 
         "Funcionam como relógios naturais precisos."),

        ("Qual é o limite máximo de velocidade para matéria e informação?", 
         ["A) Velocidade do som", "B) Velocidade da luz no vácuo (c)", "C) Gravidade quântica", "D) 1.000 km/s", "E) Sem limite"], "B", 
         "Nenhum objeto com massa supera a luz."),

        # Matéria Escura e Energia Escura (31 a 50)
        ("Qual é a função da Matéria Escura na estruturação cósmica?", 
         ["A) Emitir luz intensa.", "B) Atuar como cola gravitacional invisível mantendo galáxias coesas.", "C) Acelerar a expansão.", "D) Proteger contra raios gama.", "E) Absorver buracos negros."], "B", 
         "Fornece a atração gravitacional extra que segura as galáxias."),
        
        ("Qual a diferença entre Matéria Escura e Energia Escura?", 
         ["A) Matéria escura atrai (gravidade), energia escura repele (expansão acelerada).", "B) Fazem a mesma coisa.", "C) Energia escura é visível.", "D) Matéria escura empurra para fora.", "E) Sem diferença."], "A", 
         "Matéria escura aglutina; energia escura acelera a expansão."),
        
        ("Qual a proporção aproximada no universo entre Matéria Escura, Energia Escura e Matéria Ordinária?", 
         ["A) 50% / 30% / 20%", "B) 90% / 5% / 5%", "C) Cerca de 68% energia escura, 27% matéria escura e 5% matéria ordinária.", "D) 99% / 1%", "E) 33% cada."], "C", 
         "O universo é dominado por componentes invisíveis."),
        
        ("Por que a Matéria Escura é chamada de 'escura'?", 
         ["A) Bloqueia luz como tinta.", "B) Não emite, absorve ou reflete radiação eletromagnética detectável diretamente.", "C) Só existe na sombra.", "D) Cor escura dos planetas.", "E) Descoberta à noite."], "B", 
         "É detectada por efeitos gravitacionais indiretos."),
        
        ("O que as curvas de rotação de galáxias revelaram?", 
         ["A) Massa concentrada no centro.", "B) Estrelas periféricas giram rápido demais, indicando halo massivo invisível.", "C) Galáxias paradas.", "D) Gravidade zero nas bordas.", "E) Buracos negros gêmeos."], "B", 
         "Provam que há muito mais massa invisível no halo."),

        ("O que provou que a expansão do universo está acelerando?", 
         ["A) Supernovas distantes tipo Ia na década de 1990.", "B) Cálculo da Lua.", "C) Colisão de Andrômeda.", "D) Campo magnético terrestre.", "E) Experimentos de laboratório."], "A", 
         "Supernovas distantes indicaram aceleração na expansão."),

        ("O que é a Constante Cosmológica de Einstein?", 
         ["A) Velocidade da luz.", "B) Termo matemático original para universo estático, hoje associado à energia escura.", "C) Peso do hidrogênio.", "D) Rotação solar.", "E) Distância até Andrômeda."], "B", 
         "Hoje explica a energia escura."),

        ("O que são Aglomerados de Galáxias?", 
         ["A) Estrelas solitárias.", "B) Vastas estruturas de centenas ou milhares de galáxias mantidas pela gravidade.", "C) Anéis de poeira.", "D) Nuvens de gás frio.", "E) Sistemas planetários."], "B", 
         "Maiores laboratórios cósmicos para estudo gravitacional."),

        ("Qual o papel dos Filamentos Cósmicos?", 
         ["A) Conectar computadores.", "B) Formar pontes de matéria cercando vazios cósmicos.", "C) Conduzir raios solares.", "D) Trilhos de cometas.", "E) Luz pura."], "B", 
         "A teia cósmica organiza-se em filamentos e nós."),

        ("O que são Vazios Cósmicos?", 
         ["A) Lugares onde o tempo para.", "B) Regiões do espaço com baixa densidade de galáxias entre filamentos.", "C) Centro de buracos negros.", "D) Espaço dentro do átomo.", "E) Regiões sem matéria escura."], "B", 
         "Cobrem a maior parte do volume do universo."),

        ("O que significa WIMP em Matéria Escura?", 
         ["A) Weakly Interacting Massive Particles (Partículas Massivas de Interação Fraca).", "B) Waves in Microwave.", "C) White Dwarf.", "D) Wormhole Plasma.", "E) Water Isotope."], "A", 
         "Candidatos teóricos a partículas de matéria escura."),

        ("O que são Axions?", 
         ["A) Partículas elementares hipotéticas leves candidatas a matéria escura.", "B) Raios gama estelares.", "C) Menor unidade de tempo.", "D) Composição de Júpiter.", "E) Energia escura pura."], "A", 
         "Outra classe candidata a explicar matéria escura."),

        ("O que é Matéria Escura Fria (CDM)?", 
         ["A) Gelo no espaço.", "B) Partículas que se movem devagar em comparação à velocidade da luz, modelando estruturas.", "C) Planetas congelados.", "D) Gás superaquecido.", "E) Órbitas próximas."], "B", 
         "Modelo padrão para formação estrutural."),

        ("Como simulações de N-corpos ajudam a cosmologia?", 
         ["A) Meteorologia da Terra.", "B) Simulando gravidade de milhões de partículas para recriar a teia cósmica.", "C) Traduzindo rádio alienígena.", "D) Mapas 2D.", "E) Órbita lunar."], "B", 
         "Recriam a evolução das estruturas cósmicas."),

        ("Qual o destino final mais provável do universo?", 
         ["A) Big Crunch.", "B) Expansão eterna acelerada (Big Freeze / Morte Térmica), ficando frio e escuro.", "C) Explosão de luz.", "D) Buracos brancos.", "E) Reversão temporal."], "B", 
         "Caminha para dispersão eterna."),

        ("O que foi o experimento Planck da ESA?", 
         ["A) Viagem a Marte.", "B) Telescópio espacial que mapeou flutuações da Radiação Cósmica de Fundo.", "C) Acelerador subterrâneo.", "D) Satélite solar.", "E) Estudo de Vênus."], "B", 
         "Refinou parâmetros cosmológicos com precisão."),

        ("Por que a energia escura não se dilui com a expansão?", 
         ["A) Criada por estrelas.", "B) É propriedade inerente ao vácuo; mais espaço significa mais vácuo e energia escura.", "C) Massa negativa.", "D) Viagem rápida.", "E) Interage com buracos negros."], "B", 
         "A densidade de energia do vácuo permanece constante."),

        ("O que é a 'Crise na Cosmologia' recente?", 
         ["A) Falta de verbas.", "B) Discrepância entre medições locais da Constante de Hubble e do universo primordial.", "C) Esgotamento de hidrogênio.", "D) Colisão iminente.", "E) Falta de computadores."], "B", 
         "Divergência sobre a taxa exata de expansão."),

        ("Qual a idade estimada do universo?", 
         ["A) 6 mil anos", "B) 4,5 bilhões de anos", "C) Cerca de 13,8 bilhões de anos", "D) 100 bilhões", "E) 500 milhões"], "C", 
         "Confirmada por medições da radiação de fundo."),

        ("O que os participantes aprendem ao chegar ao topo do Santuário?", 
         ["A) O cosmo é ilusão.", "B) O verdadeiro cosmo une o poder interior à compreensão racional das leis do universo.", "C) Só força física importa.", "D) Ciência e mitologia são opostas.", "E) Universo feito por Makarius.", "F) A força bruta supera a razão."] , "B", 
         "O verdadeiro cosmo une o poder interior à compreensão racional das leis do universo.")
    ]

    # Formata com guias e IDs limpos sem numeração visível na interface
    lista_50 = []
    for i, q in enumerate(dados_brutos):
        guia = guias[i % len(guias)]
        lista_50.append({
            "guia": guia,
            "enunciado": q[0],
            "opcoes": q[1],
            "correta": q[2],
            "por_que": q[3]
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
# PAINEL DO ORGANIZADOR
# ==========================================
st.sidebar.header("⚙️ Painel do Organizador")

with st.sidebar.expander("📚 Baixar Relatório / Prova (Word / TXT)"):
    st.markdown("Baixe as 50 questões do treinamento com alternativas e justificativas completas:")
    
    texto_export = "====================================================\n"
    texto_export += "BANCO DE 50 QUESTÕES - CDZ COSMOLOGIA E O COSMO\n"
    texto_export += "====================================================\n\n"
    
    for idx, q in enumerate(st.session_state.banco_50, 1):
        texto_export += f"Guia do Templo: {q['guia']}\n"
        texto_export += f"Enunciado: {q['enunciado']}\n"
        for op in q['opcoes']:
            texto_export += f"   {op}\n"
        texto_export += f"-> Alternativa Correta: {q['correta']}\n"
        texto_export += f"-> Justificativa: {q['por_que']}\n"
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
    if st.session_state.historico:
        for h in st.session_state.historico:
            st.text(f"[{h['equipe']}] {h['status']}")
        if st.button("🗑️ Limpar Histórico"):
            st.session_state.historico = []
            st.rerun()
    else:
        st.info("Nenhuma resposta registrada ainda.")

# Placar Geral e Estabilidade na Barra Lateral
st.sidebar.header("📊 Placar & Estabilidade do Cosmo")
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
    > As três equipes enfrentam desafios em rodadas alternadas. Cada erro abala a **Estabilidade do Cosmo** individual da equipe!
    """)
    
    if st.button("🌟 Iniciar Jornada de Treinamento Rumo a Athena"):
        st.session_state.jogo_iniciado = True
        st.rerun()
    st.stop()

# ==========================================
# FLUXO DAS QUESTÕES
# ==========================================
total_questoes = len(st.session_state.banco_50)
idx_p = st.session_state.indice_pergunta
e_idx = st.session_state.equipe_sub_idx
equipe_da_vez = lista_equipes[e_idx]

# Define estabilidade atual da equipe
if equipe_da_vez == "Equipe Alfa":
    est_atual = st.session_state.est_alfa
elif equipe_da_vez == "Equipe Beta":
    est_atual = st.session_state.est_beta
else:
    est_atual = st.session_state.est_gama

if idx_p < total_questoes:
    q_atual = st.session_state.banco_50[idx_p]
    
    st.subheader(f"⚔️ Vez de: **{equipe_da_vez}**")
    st.markdown(f"**Guia do Templo:** *{q_atual['guia']}* (Estabilidade da Equipe: **{est_atual}%**) ✨")
    st.markdown("---")
    
    st.markdown(f"### **Enigma:** {q_atual['enunciado']}")
    
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

        st.session_state.historico.append({
            "equipe": equipe_da_vez,
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
            
        st.info(f"💡 **JUSTIFICATIVA (O PORQUÊ):**\n\n{fb['por_que']}")

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


