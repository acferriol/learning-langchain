import openai

def quantizacion(v):
    ma = max(v)
    mi = min(v)
    print(ma)
    print(mi)
    norm_v = [(x-mi)/(ma-mi) for x in v] #[0,1]
    print(max(norm_v))
    print(min(norm_v))
    quan_v = [int(z*255-128) for z in norm_v] #[-128,127]
    print(max(quan_v))
    print(min(quan_v))
    return quan_v


MODEL_NAME = "llama3.2:3b"
              
client= openai.OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="nokeyneeded",
    )

embeddings_response_llama = client.embeddings.create(
    model=MODEL_NAME,
    input="Hola Mundo"
)
embeddings_llama = embeddings_response_llama.data[0].embedding

print(len(embeddings_llama))

import matplotlib.pyplot as plt
fig, axs = plt.subplots(1,2)

x = [i for i in range(1,3073)]
axs[0].bar(x,embeddings_llama,color='r')
axs[1].bar(x,quantizacion(embeddings_llama),color='b')

plt.show()