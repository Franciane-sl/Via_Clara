from agents.doubts_agent import doubts_agent


def main():
    print("=" * 45)
    print("       VIA CLARA - ATENDIMENTO")
    print(" Atendimento inteligente para quem está na estrada")
    print("=" * 45)

    print("\nOlá! Sou o assistente virtual do Via Clara.")
    print("Posso ajudar com dúvidas sobre rodovias e pedágios.")
    print("\nDigite 'sair' para encerrar o atendimento.")

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
            response = doubts_agent(user_message)
            print(response)

        except Exception as error:
            print("Não foi possível processar sua pergunta.")
            print(f"Detalhes do erro: {error}")


if __name__ == "__main__":
    main()
