from openai import OpenAI
from retrieve import retrieve

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)

def ask(question):
    chunks = retrieve(question)
    
    context = "\n\n".join([
        f"Source: {c['source']}\n{c['text']}" 
        for c in chunks
    ])
    
    sources = list(set([c['source'] for c in chunks]))
    
    prompt = f"""You are a helpful assistant that answers questions about UCLA professors based on student reviews.

Answer the question using ONLY the information in the provided reviews below.
If the reviews don't contain enough information to answer, say "I don't have enough information on that."
Always mention which professor(s) the information comes from.

Reviews:
{context}

Question: {question}
"""
    
    response = client.chat.completions.create(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000
    )
    
    return {
        "answer": response.choices[0].message.content,
        "sources": sources
    }

if __name__ == "__main__":
    result = ask("What do students say about exams?")
    print("Answer:", result["answer"])
    print("\nSources:", result["sources"])