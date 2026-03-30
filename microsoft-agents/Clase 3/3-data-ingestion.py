from langchain_text_splitters import RecursiveCharacterTextSplitter
import pymupdf4llm
import os
from pathlib import Path
import openai
from lunr import lunr
import json

filenames = ["resolucion.pdf"]
MODEL_NAME = "llama3.2:3b"

client = openai.OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)

all_chunks = []

for filename in filenames:
    pdf = Path(__file__).with_name(filename)
    md_text = pymupdf4llm.to_markdown(pdf)

    md_text = md_text[:5000]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=500, chunk_overlap=50
    )

    texts = text_splitter.create_documents([md_text])
    print(len(texts))
    file_chunks = [
        {"id": f"{filename}-{(i+1)}", "text": text.page_content}
        for i, text in enumerate(texts)
    ]

    for chunk in file_chunks:
        embedding = (
            client.embeddings.create(
                model=MODEL_NAME, input=chunk["text"], dimensions=256
            )
            .data[0]
            .embedding
        )
        print(chunk["id"])
        chunk["embeddings"] = embedding

all_chunks.extend(file_chunks)

with open("resolucion_chunks.json", "w") as f:
    json.dump(all_chunks, f, indent=4)
