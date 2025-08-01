from opensearchpy import OpenSearch
import dotenv
import os

dotenv.load_dotenv()
os_key = os.getenv("OPENSEARCH_INITIAL_ADMIN_PASSWORD")

# Connect to local OpenSearch instance
client = OpenSearch(
    hosts=["localhost:9200"],
    http_auth=("admin", os_key),
    use_ssl=True,
    verify_certs=False,  # Only for dev
)

# Test connection
if client.ping():
    print("✅ Connected to OpenSearch successfully!")
    info = client.info()
    print("🔍 Cluster info:", info)
else:
    print("❌ Could not connect to OpenSearch")


index_name = "test-index"

# Create index
client.indices.create(
    index=index_name, ignore=400
)  # Ignore 400 if index already exists

# Index a document
doc = {
    "title": "Test Document",
    "content": "Hello OpenSearch!",
    "timestamp": "2025-04-05T10:00:00",
}
response = client.index(index=index_name, body=doc, refresh=True)
print("📄 Document indexed:", response)

# Search for document
result = client.search(index=index_name, body={"query": {"match_all": {}}})
print("🔍 Search result:", result["hits"]["hits"])
