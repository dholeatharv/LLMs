documents = [
    "Spring Boot is a Java framework used to build microservices.",
    "Docker is a containerization platform used to package applications.",
    "Kubernetes is used to orchestrate containers in large systems."
]

from openai import OpenAI
import math
client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

def cosine_similarity(a, b):
    dot_product = sum(x*y for x, y in zip(a, b))
    
    magnitude_a = math.sqrt(sum(x*x for x in a))
    magnitude_b = math.sqrt(sum(x*x for x in b))
    
    return dot_product / (magnitude_a * magnitude_b)

doc_embeddings = [get_embedding(doc) for doc in documents]

query = input("Enter your query: ")
query_embedding = get_embedding(query)

scores = []

for i, doc_emb in enumerate(doc_embeddings):
    similarity = cosine_similarity(query_embedding, doc_emb)
    scores.append((documents[i], similarity))
scores.sort(key=lambda x: x[1], reverse=True)

top_docs = scores[0][0]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
        {"role": "user", "content": f"Context: {top_docs}\n\nQuestion: {query}"}
    ])

answer = response.choices[0].message.content
print("\nAI Answer:")
print(answer)