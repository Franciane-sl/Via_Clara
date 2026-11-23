from agents.orchestrator import orchestrator


def main():
    print("=" * 45)
    print("       VIA CLARA - ATENDIMENTO")
    print(" Atendimento inteligente para quem está na estrada")
    print("=" * 45)

    print("\nOlá! Sou o assistente virtual do Via Clara.")
    print("Posso ajudar com dúvidas, contestações e consultas financeiras.")
    print("\nPara consultas financeiras, utilize um ID demonstrativo.")
    print("IDs disponíveis para demonstração: 1, 2 e 3.")
    print("\nDigite 'sair' para encerrar o atendimento.")

    customer_id = None

    while True:
        user_message = input("\nVocê: ").strip()

        if user_message.lower() == "sair":
            print("\nVia Clara: Atendimento encerrado. Até logo!")
            break

        if not user_message:
            print("\nVia Clara: Digite uma pergunta para continuar.")
            continue

        print("\nVia Clara: ", end="")

       
        try:
            response = orchestrator(
                user_message=user_message,
                customer_id=customer_id
            )

            if "é necessário informar o ID demonstrativo" in response:
                customer_input = input("\nVia Clara: Informe seu ID demonstrativo: ")

                try:
                    customer_id = int(customer_input)
                except ValueError:
                    print("Via Clara: ID inválido. Informe um número.")
                    continue

                response = orchestrator(
                    user_message=user_message,
                    customer_id=customer_id
                )

            print(response)

        except Exception as error:
            print("Não foi possível processar sua pergunta.")
            print(f"Detalhes do erro: {error}")

if __name__ == "__main__":
    main()
