from agents.doubts_agent import doubts_agent
from agents.contestation_agent import contestation_agent
from agents.billing_agent import billing_agent


def identify_intent(user_message: str) -> str:

    mensagem = user_message.lower()

    contestation_keywords = [
        "contestar",
        "contestação",
        "cobrança duplicada",
        "cobrado duas vezes",
        "não reconheço",
        "não reconhecida",
        "cobrança indevida",
        "valor divergente",
        "falha na tag"
    ]

    billing_keywords = [
        "débito",
        "débitos",
        "pendente",
        "devendo",
        "pagamento realizado",
        "pagamentos",
        "paguei",
        "tarifa",
        "tarifas",
        "valor do pedágio",
        "quanto custa"
    ]

    if any(
        palavra in mensagem
        for palavra in contestation_keywords
    ):
        return "contestation"

    if any(
        palavra in mensagem
        for palavra in billing_keywords
    ):
        return "billing"

    return "doubts"


def orchestrator(
    user_message: str,
    customer_id: int | None = None
) -> str:

    intent = identify_intent(user_message)

    if intent == "contestation":
        return contestation_agent(user_message)

    if intent == "billing":
        if customer_id is None:
            return (
                "Para consultar informações financeiras, "
                "é necessário informar o ID demonstrativo do cliente."
            )

        return billing_agent(user_message, customer_id)

    return doubts_agent(user_message)
