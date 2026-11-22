from ollama import Client
from config.settings import OLLAMA_HOST, OLLAMA_MODEL

client = Client(host=OLLAMA_HOST)

#Função para interagir com o modelo
def ask_model(system_prompt: str, user_prompt: str) -> str:
    response = client.chat(
        model=OLLAMA_MODEL,
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        options={
            "temperature": 0.2,
            "num_ctx": 1024,
            "num_predict": 120,
            "num_batch": 128,
            "num_thread": 4
        }
    )

    return response.message.content.strip()