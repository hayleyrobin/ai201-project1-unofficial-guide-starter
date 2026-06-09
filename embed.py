import chromadb
from sentence_transformers import SentenceTransformer
from ingest import ingest

def build_vector_store():
    # Load chunks from ingest pipeline
    chunks = ingest()
    
    # Load embedding model
    print("Loading embedding model...")
    model = SentenceTransformer("all-MiniLM-L6-v2")
    
    # Set up ChromaDB
    client = chromadb.PersistentClient(path="./chroma_db")
    
    # Delete existing collection if it exists
    try:
        client.delete_collection("professor_reviews")
    except:
        pass
    
    collection = client.create_collection("professor_reviews")
    
    # Embed and store chunks
    print("Embedding chunks...")
    for i, chunk in enumerate(chunks):
        embedding = model.encode(chunk["text"]).tolist()
        collection.add(
            ids=[f"chunk_{i}"],
            embeddings=[embedding],
            documents=[chunk["text"]],
            metadatas=[{"source": chunk["source"], "chunk_index": chunk["chunk_index"]}]
        )
    
    print(f"Stored {len(chunks)} chunks in ChromaDB")
    return collection

if __name__ == "__main__":
    build_vector_store()