import openai

MODEL_NAME = "llama3.2:3b"

if __name__=='__main__':
    client= openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded",
    )

    response= client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.7,
        max_tokens=30,
        n=1,
        messages=[
{"role": "system", "content": "Eres un tutor que da pistas, no respuestas."},
{"role": "user", "content": "¿Cual es la capital de Francia?"},
{"role": "assistant", "content": "¿Puedes pensar en la ciudad conocidaporla Torre Eiffel?"},
{"role": "user", "content": "¿Cuáles la raíz cuadrada de 144?"},
{"role": "assistant", "content": "¿Qué número multiplicado por sí mismo es igual a 144?"},
{"role": "user", "content": "¿Cuál es el número atómico del oxígeno?"},
{"role": "assistant", "content": "¿Cuántos protones tiene un átomo de oxígeno?"},
{"role": "user", "content": "¿Cuál es el planeta más grande del sistema solar?"},
])
    print(response.choices[0].message.content)

    