pip install google-genai
import os
from google import genai
from google.genai import types

def criar_astronomia_para_criancas():
    """
    Inicializa o assistente 'Astronomia para Crianças' utilizando a API do Gemini.
    Garante que as respostas sejam lúdicas, educativas e tenham entre 1 e 5 parágrafos.
    """
    # Certifique-se de que sua chave de API está configurada no ambiente:
    # No terminal do seu computador, digite: export GEMINI_API_KEY="sua_chave_aqui"
    
    client = genai.Client()

    # Instrução de Sistema: A "regra de ouro" que define a personalidade e o limite de parágrafos da IA
    instrucao_sistema = (
        "Você é o assistente virtual 'Astronomia para Crianças', um guia espacial divertido, "
        "amigável e mágico que ensina os segredos do Universo para os pequenos. "
        "Regras estritas que você DEVE seguir:\n"
        "1. Responda a QUALQUER pergunta sobre planetas, estrelas, galáxias, foguetes ou espaço sideral.\n"
        "2. Use uma linguagem simples, mágica, acolhedora e com analogias fáceis de entender.\n"
        "3. O tamanho da sua resposta DEVE ter obrigatoriamente entre 1 e 5 parágrafos (nunca menos que 1 e nunca mais que 5 parágrafos).\n"
        "4. Nunca utilize termos técnicos complexos sem explicá-los de forma muito divertida."
    )

    # Configurações do modelo
    configuracao = types.GenerateContentConfig(
        system_instruction=instrucao_sistema,
        temperature=0.7, # Mantém a criatividade e o entusiasmo nas explicações
    )

    return client, configuracao

# ==========================================================
# FUNÇÃO PARA PROCESSAR A PERGUNTA DA CRIANÇA
# ==========================================================
def perguntar_ao_assistente(pergunta):
    client, configuracao = criar_astronomia_para_criancas()
    
    try:
        # Chamada ao modelo Gemini otimizado para respostas rápidas e inteligentes
        resposta = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=pergunta,
            config=configuracao,
        )
        return resposta.text
    except Exception as e:
        return f"Houston, tivemos um problema! O foguete encontrou um erro técnico: {e}"

# ==========================================================
# BLOCO DE EXECUÇÃO E TESTE
# ==========================================================
if __name__ == "__main__":
    print("🚀 Iniciando o sistema de 'Astronomia para Crianças'...\n")
    
    # Exemplo de pergunta feita por uma criança
    pergunta_crianca = "Por que os astronautas flutuam no espaço?"
    
    print(f"Criança pergunta: '{pergunta_crianca}'\n")
    
    # Gerando a resposta com a IA
    resposta_final = perguntar_ao_assistente(pergunta_crianca)
    
    print("Resposta do Assistente Espacial:")
    print("-" * 50)
    print(resposta_final)
    print("-" * 50)
