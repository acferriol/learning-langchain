from langchain_ollama import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import OpenSearchVectorSearch
from langchain_text_splitters import CharacterTextSplitter
import dotenv
import os

dotenv.load_dotenv()
os_key = os.getenv("OPENSEARCH_INITIAL_ADMIN_PASSWORD")


embeddings = OllamaEmbeddings(
    base_url="http://127.0.0.1:11434", model="deepseek-r1:1.5b"
)


loader = TextLoader("./data/test.txt")
documents = loader.load()
text_splitter = CharacterTextSplitter(chunk_size=10, chunk_overlap=3)
docs = text_splitter.split_documents(documents)

docsearch = OpenSearchVectorSearch.from_documents(
    docs,
    embeddings,
    opensearch_url="https://localhost:9200",
    http_auth=("admin", os_key),
    use_ssl=False,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
    engine="faiss",
)

query = "What did the president say about Ketanji Brown Jackson"
docs = docsearch.similarity_search(query, k=1)

print(docs[0].page_content)
