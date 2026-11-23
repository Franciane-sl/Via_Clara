import json
from pathlib import Path


DATA_PATH = Path(__file__).resolve().parent.parent / "data"


def load_json(filename: str) -> dict:

    file_path = DATA_PATH / filename

    with open(file_path, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def get_customer(customer_id: int) -> dict | None:

    dados = load_json("customers.json")

    for cliente in dados["clientes"]:
        if cliente["id"] == customer_id:
            return cliente

    return None


def get_customer_debts(customer_id: int) -> list:

    cliente = get_customer(customer_id)

    if cliente is None:
        return []

    return [
        debito for debito in cliente["debitos"]
        if debito["status"] == "pendente"
    ]


def get_customer_payments(customer_id: int) -> list:
 
    cliente = get_customer(customer_id)

    if cliente is None:
        return []

    return [
        debito for debito in cliente["debitos"]
        if debito["status"] == "pago"
    ]


def get_total_debts(customer_id: int) -> float:
   
    debitos = get_customer_debts(customer_id)

    return sum(debito["valor"] for debito in debitos)


def get_tariffs() -> list:

    dados = load_json("tariffs.json")

    return dados["tarifas"]
