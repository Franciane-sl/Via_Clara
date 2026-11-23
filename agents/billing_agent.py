from tools.operations import (
    get_customer,
    get_customer_debts,
    get_customer_payments,
    get_total_debts,
    get_tariffs
)


def billing_agent(user_message: str, customer_id: int) -> str:

    cliente = get_customer(customer_id)

    if cliente is None:
        return (
            "Não encontrei um cliente com o ID informado. "
            "Verifique o identificador e tente novamente."
        )

    mensagem = user_message.lower()

    resposta = [
        f"Olá, {cliente['nome']}!",
        "Estas informações são demonstrativas."
    ]

    if any(
        termo in mensagem
        for termo in ["débito", "débitos", "pendente", "devendo"]
    ):
        debitos = get_customer_debts(customer_id)
        total = get_total_debts(customer_id)

        resposta.append("\nDébitos pendentes:")

        if debitos:
            for debito in debitos:
                resposta.append(
                    f"- {debito['descricao']}: "
                    f"R$ {debito['valor']:.2f} "
                    f"(Data: {debito['data']})"
                )
        else:
            resposta.append("Não existem débitos pendentes.")

        resposta.append(f"Total pendente: R$ {total:.2f}")

    if any(
        termo in mensagem
        for termo in ["pagamento", "pagamentos", "paguei", "pago"]
    ):
        pagamentos = get_customer_payments(customer_id)

        resposta.append("\nPagamentos realizados:")

        if pagamentos:
            for pagamento in pagamentos:
                resposta.append(
                    f"- {pagamento['descricao']}: "
                    f"R$ {pagamento['valor']:.2f} "
                    f"(Data: {pagamento['data']})"
                )
        else:
            resposta.append("Não existem pagamentos registrados.")

    if any(
        termo in mensagem
        for termo in ["tarifa", "tarifas", "valor do pedágio"]
    ):
        tarifas = get_tariffs()

        resposta.append("\nTarifas cadastradas:")

        for tarifa in tarifas:
            resposta.append(
                f"- {tarifa['rodovia']} | "
                f"{tarifa['praca']} | "
                f"{tarifa['categoria_veiculo']}: "
                f"R$ {tarifa['valor']:.2f}"
            )

    if len(resposta) == 2:
        return (
            "Não consegui identificar o tipo de consulta financeira. "
            "Você pode perguntar sobre débitos, pagamentos ou tarifas."
        )

    return "\n".join(resposta)
