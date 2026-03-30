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
            {"role": "system", "content": "Eres un asistente útil que hace muchas referencias a gatos y usa emojis."},
            {"role": "user", "content": "Escribe un haiku sobre un gato hambriento que quiere atún"}
        ])
    print(response.choices[0].message.content)

    