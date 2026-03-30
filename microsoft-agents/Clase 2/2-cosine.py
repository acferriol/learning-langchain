def cosine_similarity(v1, v2):
    dot_product = sum(
        [a * b for a, b in zip(v1, v2)])
    magnitude = (
        sum([a**2 for a in v1]) *
        sum([a**2 for a in v2])) ** 0.5
    return dot_product / magnitude

import openai

MODEL_NAME = ["deepseek-r1:8b", "codellama:7b"]
              
client= openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded",
    )

embeddings_response_deepseek = client.embeddings.create(
    model=MODEL_NAME[0],
    input="Hola Mundo"
)
embeddings_deepseek = embeddings_response_deepseek.data[0].embedding

print(len(embeddings_deepseek))

print("----------------------------------------------------")

embeddings_response_llama = client.embeddings.create(
    model=MODEL_NAME[1],
    input="Hola Mundo"
)
embeddings_llama = embeddings_response_llama.data[0].embedding

print(len(embeddings_llama))

print(cosine_similarity(embeddings_deepseek,embeddings_llama))