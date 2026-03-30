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


import matplotlib.pyplot as plt

fig, axs = plt.subplots(1,2)

x = [i for i in range(1,4097)]
y = embeddings_deepseek

axs[0].bar(x,y,color='r')

y = embeddings_llama

axs[1].bar(x,y,color='b')

plt.show()