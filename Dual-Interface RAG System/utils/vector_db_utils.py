from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
VECTOR_DB_DIR = BASE_DIR / "doc_vector_db"

embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

vector_db = Chroma(
    persist_directory=str(VECTOR_DB_DIR),
    embedding_function=embedding
)

# Acess a collection
collection = vector_db._collection

# See what documents were processed
data = collection.get()

# Extract all sources
all_sources = [meta.get('source') for meta in data['metadatas']]

# Get unique sources
unique_sources = set(all_sources)

print("Unique sources in the vector database:")
for src in unique_sources:
    print("-", src)
