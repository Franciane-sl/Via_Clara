from utils.ollama_client import ask_model
from tools.knowledge_base import search_contestation

SYSTEM_PROMPT = """
Você é o agente de contestações do Via Clara,
um sistema de atendimento para usuários de rodovias e pedágios.

Regras obrigatórias:
1. Responda sempre em português brasileiro.
2. Seja educado, claro e objetivo.
3. Utilize as orientações fornecidas pela base de conhecimento.
4. Não invente informações, prazos ou protocolos.
5. Não prometa reembolso ou cancelamento de cobranças.
6. Não afirme que uma contestação foi registrada.
7. Oriente o usuário a procurar os canais oficiais
   da concessionária responsável.
8. Nunca solicite senhas ou dados bancários.
"""

def contestation_agent(user_message: str) -> str:
    resultados = search_contestation(user_message)

    if not resultados:
        return (
            "Não encontrei informações suficientes para identificar "
            "o motivo da contestação. Recomendo procurar os canais "
            "oficiais da concessionária responsável."
        )

    contexto = ""

    for item in resultados:
        contexto += (
            f"\nMotivo: {item['motivo']}"
            f"\nOrientação: {item['orientacao']}\n"
        )

    user_prompt = f"""
    Relato do usuário:
    {user_message}

    Informações encontradas na base de conhecimento:
    {contexto}

    Oriente o usuário utilizando as informações fornecidas.
    Não acrescente informações que não estejam na base.
    """

    return ask_model(
        system_prompt=SYSTEM_PROMPT,
        user_prompt=user_prompt
    )
