import openai
from lunr import lunr
import csv
import os
from pathlib import Path

CSV_PATH = Path(__file__).with_name("hybridos.csv")
with CSV_PATH.open(newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    rows = list(reader)
documents = [{"id": (i + 1), "body": " ".join(row)} for i, row in enumerate(rows[1:])]
index = lunr(ref="id", fields=["body"], documents=documents)


def search(query):
    # Buscar en el índice la pregunta del usuario
    results = index.search(query)
    matching_rows = [rows[int(result["ref"])] for result in results]

    # Formatear como una tabla markdown, ya que los modelos de lenguaje entienden markdown
    matches_table = (
        " | ".join(rows[0])
        + "\n"
        + " | ".join(" --- " for _ in range(len(rows[0])))
        + "\n"
    )
    matches_table += "\n".join(" | ".join(row) for row in matching_rows)
    return matches_table


QUERY_REWRITE_SYSTEM_MESSAGE = """
Eres un asistente útil que reescribe preguntas de usuarios a consultas de alta calidad de tipo keyword
para un índice de filas CSV con estas columnas: vehículo,año,precio,aceleración,consumo,clase.
Consultas de alta calidad de keyword no tienen puntuación y están en minúsculas.
Se te proporcionará la nueva pregunta del usuario y el historial de conversación.
Responde SÓLO con la consulta de keyword sugerida, sin texto adicional.
"""

SYSTEM_MESSAGE = """
Eres un asistente útil que responde preguntas sobre automóviles basándose en un conjunto de datos de coches híbridos.
Debes utilizar el conjunto de datos para responder las preguntas, no debes proporcionar información que no
esté en las fuentes proporcionadas.
"""

MODEL_NAME = "llama3.2:3b"

messages = [{"role": "system", "content": SYSTEM_MESSAGE}]

while True:
    question = input("\nTu pregunta sobre coches eléctricos: ")

    client = openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded",
    )

    # Reescribir la consulta para corregir errores tipográficos e incorporar contexto pasado
    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.05,
        messages=[
            {"role": "system", "content": QUERY_REWRITE_SYSTEM_MESSAGE},
            {
                "role": "user",
                "content": f"Nueva pregunta del usuario:{question}\n\nHistorial de conversación:{messages}",
            },
        ],
    )
    search_query = response.choices[0].message.content
    print(f"Consulta reescrita: {search_query}")

    # Buscar en el CSV la pregunta
    matches = search(search_query)
    print("Coincidencias encontradas:\n", matches)

    # Usar las coincidencias para generar una respuesta
    messages.append({"role": "user", "content": f"{question}\nFuentes: {matches}"})
    response = client.chat.completions.create(
        model=MODEL_NAME, temperature=0.3, messages=messages
    )

    bot_response = response.choices[0].message.content
    messages.append({"role": "assistant", "content": bot_response})

    print(bot_response)
