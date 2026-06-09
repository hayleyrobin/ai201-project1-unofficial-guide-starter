import chromadb
from sentence_transformers import SentenceTransformer

def get_collection():
    client = chromadb.PersistentClient(path="./chroma_db")
    return client.get_collection("professor_reviews")

def retrieve(query, k=4):
    model = SentenceTransformer("all-MiniLM-L6-v2")
    collection = get_collection()
    
    query_embedding = model.encode(query).tolist()
    
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k
    )
    
    chunks = []
    for i in range(len(results["documents"][0])):
        chunks.append({
            "text": results["documents"][0][i],
            "source": results["metadatas"][0][i]["source"],
            "distance": results["distances"][0][i]
        })
    
    return chunks

if __name__ == "__main__":
    query = "What do students say about exams?"
    print(f"Query: {query}\n")
    results = retrieve(query)
    for r in results:
        print(f"Source: {r['source']}")
        print(f"Distance: {r['distance']:.3f}")
        print(f"Text: {r['text']}")
        print("---")