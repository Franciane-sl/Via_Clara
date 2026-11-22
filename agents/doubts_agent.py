from utils.ollama_client import ask_model
from tools.knowledge_base import search_faq


SYSTEM_PROMPT = """
Você é o agente de dúvidas do Via Clara,
um sistema de atendimento para usuários de rodovias e pedágios.

Regras obrigatórias:
1. Responda sempre em português brasileiro.
2. Seja educado, claro e objetivo.
3. Utilize as informações da base de conhecimento
   para responder às perguntas.
4. Não invente tarifas, regras ou informações.
5. Não contradiga as informações fornecidas pela base.
6. Se a base não fornecer informações suficientes,
   informe que não possui dados suficientes e recomende
   consultar os canais oficiais da concessionária.
7. Não responda assuntos fora do seu escopo.
8. Não invente informações para completar respostas.
"""


def doubts_agent(user_message: str) -> str:
    resultados = search_faq(user_message)

    if not resultados:
        return (
            "Não encontrei informações suficientes na minha "
            "base de conhecimento para responder a essa pergunta. "
            "Recomendo consultar os canais oficiais da concessionária."
        )

    contexto = ""

    for item in resultados:
        contexto += (
            f"\nPergunta: {item['pergunta']}"
            f"\nResposta: {item['resposta']}\n"
        )

    user_prompt = f"""
    Pergunta do usuário:
    {user_message}

    Informações encontradas na base de conhecimento:
    {contexto}

    Responda utilizando as informações fornecidas.
    Não acrescente informações que não estejam na base.
    """

    return ask_model(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt
    )
