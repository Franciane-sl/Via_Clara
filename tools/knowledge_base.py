import json
from pathlib import Path

FAQ_PATH = Path(__file__).resolve().parent.parent / "data" / "faq.json"


def load_faq() -> list:

    with open(FAQ_PATH, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    return dados["perguntas_frequentes"]


def search_faq(user_message: str) -> list:
    
    perguntas = load_faq()
    mensagem = user_message.lower()

    resultados = []

    for item in perguntas:
        termos = [
            item["pergunta"].lower(),
            *[palavra.lower() for palavra in item["palavras_chave"]]
        ]

        if any(termo in mensagem for termo in termos):
            resultados.append(item)

    return resultados
