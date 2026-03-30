import openai

MODEL_NAME = "llama3.2:3b"

RAG_CONTENT = """
vehicle | year | msrp | acceleration |
Prius (1st Gen) | 1997 | 24509.74 | 7.46 |
Prius (2nd Gen) | 2000 | 26832.25 | 7.97 |
Prius (3rd Gen) | 2009 | 24641.18 | 9.6 |
Prius V | 2011 | 27272.28 | 9.51 |
Prius C | 2012 | 19006.62 | 9.35 |
Prius PHV | 2012 | 32095.61 | 8.82 |
Prius C | 2013 | 19080.0 | 8.7 |
Prius | 2013 | 24200.0 | 10.2 |
Prius Plug-in | 2013 | 32000.0 | 9.17 |
"""


client= openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)
user_query = "¿qué tan rápido es el Prius v?"
response= client.chat.completions.create(
    model=MODEL_NAME,
    temperature=0.7,
    messages= [
        {
        "role": "system",
        "content": "Debes utilizar el conjunto de datos para responder las preguntas"
        },
        {
        "role": "user",
        "content": user_query+"\n Sources: \n" +RAG_CONTENT
        }]
)
print(response.choices[0].message.content)

    