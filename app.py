import streamlit as st
import sympy as sp
import math

# Configuração da página
st.set_page_config(
    page_title="Aetheris - IA de Cosmologia e Cálculo Avançado", 
    page_icon="✨", 
    layout="centered"
)

# Estilo visual focado em um ambiente científico / cósmico
st.markdown("""
    <style>
    .main { background-color: #070913; color: #f0f6fc; }
    .stButton>button {
        width: 100%; background-color: #2b3a67; color: white;
        border-radius: 8px; font-weight: bold; border: 1px solid #00d2ff;
    }
    .stButton>button:hover { background-color: #00d2ff; color: black; }
    </style>
""", unsafe_allow_html=True)

st.title("✨ Aetheris: IA de Cosmologia & Cálculo Avançado")
st.markdown("### *Sua assistente inteligente para desvendar o tecido do espaço-tempo e resolver equações matemáticas complexas.*")
st.markdown("---")

# ==========================================
# INICIALIZAÇÃO DO ESTADO DA IA
# ==========================================
if "historico_chat" not in st.session_state:
    st.session_state.historico_chat = [
        {"role": "ia", "texto": "Saudações, pesquisador. Sou a Aetheris, uma inteligência artificial sintonizada com as leis da astrofísica e do cálculo avançado. Como posso auxiliar nos seus estudos ou nas equações da sua tese hoje?"}
    ]

# Seletor de Modo na Barra Lateral
st.sidebar.header("⚙️ Módulos de Operação")
modo_ia = st.sidebar.selectbox(
    "Selecione a especialidade da IA:",
    ["🤖 Chat Geral & Cosmologia", "∫ Calculadora de Derivadas e Integrais", "🌌 Simulado / Dúvidas de Relatividade"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🔬 Sobre o Sistema")
st.sidebar.markdown("Esta IA combina conhecimentos de relatividade geral, cosmologia observacional e um motor simbólico em Python (`SymPy`) para processamento analítico rigoroso.")

if st.sidebar.button("🧹 Limpar Histórico da Conversa"):
    st.session_state.historico_chat = [
        {"role": "ia", "texto": "Memória limpa. Sistema pronto para novos cálculos e questionamentos cosmológicos."}
    ]
    st.rerun()

# ==========================================
# MÓDULO 1: CHAT GERAL & COSMOLOGIA
# ==========================================
if modo_ia == "🤖 Chat Geral & Cosmologia":
    st.subheader("💬 Diálogo com Aetheris (Cosmologia e Astrofísica)")
    
    # Exibe o histórico do chat
    for msg in st.session_state.historico_chat:
        if msg["role"] == "usuario":
            st.markdown(f"**🧑‍💻 Você:** {msg['texto']}")
        else:
            st.markdown(f"**✨ Aetheris:** {msg['texto']}")
        st.markdown("")

    # Caixa de entrada do usuário
    pergunta_usuario = st.text_input("Digite sua dúvida sobre o universo, buracos negros, Big Bang ou física:")
    
    if st.button("Enviar para Aetheris"):
        if pergunta_usuario.strip() != "":
            st.session_state.historico_chat.append({"role": "usuario", "texto": pergunta_usuario})
            
            p_lower = pergunta_usuario.lower()
            resposta_ia = ""
            
            if "big bang" in p_lower:
                resposta_ia = "O Big Bang não foi uma explosão no espaço, mas sim a expansão métrica rápida do próprio espaço-tempo a partir de uma singularidade inicial densa e quente, há cerca de 13,8 bilhões de anos."
            elif "relatividade" in p_lower or "einstein" in p_lower:
                resposta_ia = "A Relatividade Geral de Einstein substitui a visão newtoniana da gravidade: a massa e a energia curvam a geometria quadridimensional do espaço-tempo, ditando como os corpos e a luz devem se mover."
            elif "materia escura" in p_lower or "matéria escura" in p_lower:
                resposta_ia = "A matéria escura compõe cerca de 27% do universo. Ela não interage com a luz (eletromagnetismo), mas exerce atração gravitacional, funcionando como uma 'cola invisível' que mantém as galáxias espirais coesas."
            elif "energia escura" in p_lower:
                resposta_ia = "A energia escura representa cerca de 68% do cosmos. É uma propriedade inerente ao vácuo quântico que atua de forma repulsiva, sendo a principal responsável pela aceleração da expansão do universo."
            elif "hubble" in p_lower:
                resposta_ia = "A Lei de Hubble estabelece que a velocidade de recessão das galáxias é diretamente proporcional à sua distância até nós (v = H_0 * d), provando que o cosmos está em expansão contínua."
            else:
                resposta_ia = f"Análise concluída sobre '{pergunta_usuario}'. No contexto da cosmologia padrão (Lambda-CDM), esse fenômeno relaciona-se diretamente com a curvatura do espaço-tempo e a dinâmica de fluidos cosmológicos. Deseja aprofundar com alguma equação matemática específica?"

            st.session_state.historico_chat.append({"role": "ia", "texto": resposta_ia})
            st.rerun()

# ==========================================
# MÓDULO 2: CÁLCULO AVANÇADO (DERIVADAS E INTEGRAIS)
# ==========================================
elif modo_ia == "∫ Calculadora de Derivadas e Integrais":
    st.subheader("📐 Laboratório de Cálculo Simbólico Avançado")
    st.markdown("Insira uma função matemática e a variável para realizar operações analíticas exatas.")

    col1, col2 = st.columns(2)
    with col1:
        expressao_str = st.text_input("Função f(x):", value="x**3 * sin(x)")
    with col2:
        var_str = st.text_input("Variável:", value="x")

    operacao = st.selectbox("Escolha a operação matemática:", ["Derivada (d/dx)", "Integral Indefinida (∫ f(x) dx)"])

    if st.button("Executar Cálculo Analítico"):
        try:
            x = sp.Symbol(var_str)
            expr = sp.sympify(expressao_str)
            
            st.markdown("---")
            st.markdown(f"### **Resultado do Processamento:**")
            
            latex_expr = sp.latex(expr)
            
            if "Derivada" in operacao:
                resultado = sp.diff(expr, x)
                latex_res = sp.latex(resultado)
                st.latex(r"\frac{d}{d" + var_str + r"} \left( " + latex_expr + r" \right) = " + latex_res)
            else:
                resultado = sp.integrate(expr, x)
                latex_res = sp.latex(resultado)
                st.latex(r"\int \left( " + latex_expr + r" \right) d" + var_str + r" = " + latex_res + r" + C")
                
            st.success("Cálculo efetuado com rigor analítico pelo motor SymPy.")
        except Exception as e:
            st.error(f"Erro ao processar a expressão matemática. Verifique a sintaxe (ex: use `x**2` para potências, `sin(x)`, `cos(x)`). Detalhe: {e}")

# ==========================================
# MÓDULO 3: SIMULADO / DÚVIDAS DE RELATIVIDADE
# ==========================================
elif modo_ia == "🌌 Simulado / Dúvidas de Relatividade":
    st.subheader("🎯 Desafios de Astrofísica Relativística")
    st.markdown("Teste seus conhecimentos ou explore problemas clássicos da gravitação einsteiniana.")

    pergunta_quiz = st.radio(
        "Selecione um tópico avançado para análise da IA:",
        [
            "Dilatação Temporal Gravitacional",
            "Métrica de Schwarzschild e Buracos Negros",
            "Equações de Friedmann na Cosmologia"
        ]
    )

    if pergunta_quiz == "Dilatação Temporal Gravitacional":
        st.info("""
        **Conceito:** O tempo passa mais devagar em locais onde o campo gravitacional é mais intenso.
        
        **Fórmula Clássica de Aproximação:**
        $$t_0 = t_f \\sqrt{1 - \\frac{2GM}{rc^2}}$$
        
        *Aetheris:* Isso significa que relógios próximos a objetos supermassivos (como estrelas de nêutrons ou buracos negros) atrasam significativamente em relação a observadores distantes no espaço plano.
        """)
    elif pergunta_quiz == "Métrica de Schwarzschild":
        st.info("""
        **Conceito:** Descreve o campo gravitacional fora de uma massa esférica, estática e sem carga elétrica.
        
        **Elemento de Linha ($ds^2$):**
        $$ds^2 = -\\left(1 - \\frac{2GM}{rc^2}\\right) c^2 dt^2 + \\left(1 - \\frac{2GM}{rc^2}\\right)^{-1} dr^2 + r^2 (d\\theta^2 + \\sin^2\\theta d\\phi^2)$$
        
        *Aetheris:* Note que quando $r$ atinge o raio de Schwarzschild ($R_s = \\frac{2GM}{c^2}$), o termo temporal zera e o termo radial diverge, marcando o famigerado horizonte de eventos.
        """)
    else:
        st.info("""
        **Conceito:** Descrevem a expansão do espaço-tempo em modelos homogêneos e isotrópicos na Relatividade Geral.
        
        **Primeira Equação de Friedmann:**
        $$\\left(\\frac{\\dot{a}}{a}\\right)^2 = \\frac{8\\pi G}{3}\\rho - \\frac{k}{a^2} + \\frac{\\Lambda}{3}$$
        
        *Aetheris:* Onde $a(t)$ é o fator de escala do universo, $\\rho$ é a densidade de energia, $k$ é a curvatura espacial e $\\Lambda$ é a constante cosmológica.
        """)
       
