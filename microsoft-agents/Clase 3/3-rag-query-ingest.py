import openai
from lunr import lunr
import csv
import os
from pathlib import Path
import json

client = openai.OpenAI(base_url="http://localhost:11434/v1", api_key="nokeyneeded")
MODEL_NAME = "llama3.2:3b"

with open("resolucion_chunks.json") as file:
    documents = json.load(file)
    documents_by_id = {doc["id"]: doc for doc in documents}
index = lunr(ref="id", fields=["text"], documents=documents)

# Get the user question
user_question = "Cómo obtener el título de oro"

# Search the index for the user question
results = index.search(user_question)
retrieved_documents = [documents_by_id[result["ref"]] for result in results]
print(
    f"Retrieved {len(retrieved_documents)} matching documents, only sending the first."
)
context = "\n".join([f"{doc['id']}: {doc['text']}" for doc in retrieved_documents[0:1]])

print("--------------------Genera")

# Now we can use the matches to generate a response
SYSTEM_MESSAGE = """
Eres un asistente que responde acerca de procedimientos
Debes utilizar el conjunto de datos para responder la pregunta
No debes utilizar ninguna información que no aparezca en las fuentes proporcionadas
Cita las fuentes que utilizaste para responder las preguntas dentro de corchetes
Las fuentes están en formato: <id>: <text>.
"""

response = client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.3,
    messages=[
        {"role": "system", "content": SYSTEM_MESSAGE},
        {"role": "user", "content": f"{user_question}\nSources: {context}"},
    ],
)

print(response.choices[0].message.content)
