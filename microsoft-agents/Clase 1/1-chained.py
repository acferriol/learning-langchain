import openai

MODEL_NAME = "llama3.2:3b"

if __name__=='__main__':
    client= openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded",
    )

    response= client.chat.completions.create(model=MODEL_NAME,
        messages=[{"role": "user",
        "content": "Explica cómo funcionan los LLM en un solo párrafo."}])
    explanation= response.choices[0].message.content
    print(explanation)

    response= client.chat.completions.create(model=MODEL_NAME,
    messages=[{"role": "user",
        "content": f"Eres un editor. Revisa la siguiente explicación y proporcionac omentarios detallados sobre claridad, coherencia y cautivación. \n Explicación:\n{explanation}"}])
    feedback= response.choices[0].message.content
    print(feedback)
    response= client.chat.completions.create(model=MODEL_NAME,
    messages=[{"role": "user",
        "content": f"Revisa el articulo usando los comentarios siguientes pero mantenlo a un solo párrafo. \n Explicación:\n {explanation} \n\n Comentarios:\n{feedback}"}])
    final_article= response.choices[0].message.content
    print(response.choices[0].message.content)

    