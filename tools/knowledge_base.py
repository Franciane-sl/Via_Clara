import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "data"


def load_data(filename: str, key: str) -> list:

    file_path = DATA_PATH / filename

    with open(file_path, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados[key]


def search_data(user_message: str, filename: str, key: str) -> list:
   
    items = load_data(filename, key)
    mensagem = user_message.lower()

    resultados = []

    for item in items:
        termos = [
            item.get("pergunta", "").lower(),
            item.get("motivo", "").lower(),
            *[palavra.lower() for palavra in item.get("palavras_chave", [])]
        ]

        if any(termo and termo in mensagem for termo in termos):
            resultados.append(item)

    return resultados


def load_faq() -> list:
    return load_data("faq.json", "perguntas_frequentes")


def search_faq(user_message: str) -> list:
    return search_data(
        user_message,
        "faq.json",
        "perguntas_frequentes"
    )


def search_contestation(user_message: str) -> list:
    return search_data(
        user_message,
        "contestation_reasons.json",
        "motivos_contestacao"
    )
