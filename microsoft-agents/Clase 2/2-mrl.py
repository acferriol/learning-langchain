import openai

MODEL_NAME = "llama3.2:3b"
              
client= openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded",
    )

embeddings_response_llama = client.embeddings.create(
    model=MODEL_NAME,
    input="Hola Mundo",
    dimensions=256 #Dimension
)

embeddings_llama = embeddings_response_llama.data[0].embedding

print(len(embeddings_llama))