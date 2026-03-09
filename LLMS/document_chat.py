from openai import OpenAI
client = OpenAI()
import math

document = """
Spring Boot is a Java framework that simplifies backend development.
It is commonly used to build REST APIs and microservices.

Docker is a containerization platform.
It helps package applications with their dependencies.

Kubernetes is a container orchestration system.
It helps manage containers across multiple servers.

JWT stands for JSON Web Token.
It is commonly used for stateless authentication in APIs.
"""

chunks = [
    "Spring Boot is a Java framework that simplifies backend development. It is commonly used to build REST APIs and microservices.",
    "Docker is a containerization platform. It helps package applications with their dependencies.",
    "Kubernetes is a container orchestration system. It helps manage containers across multiple servers.",
    "JWT stands for JSON Web Token. It is commonly used for stateless authentication in APIs."
]

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

chunk_embeddings = [get_embedding(chunk) for chunk in chunks]

query = input("Enter your question about the document: ")
query_embedding = get_embedding(query)

scores = []

for i, chunk_emb in enumerate(chunk_embeddings):
    similarity = cosine_similarity(query_embedding, chunk_emb)
    scores.append((chunks[i], similarity))
scores.sort(key=lambda x: x[1], reverse=True)

best_chunk = scores[0][0]

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
        {"role": "user", "content": f"Context: {best_chunk}\n\nQuestion: {query}"}
    ])  
answer = response.choices[0].message.content
print("\nMost relevant chunk:")
print(best_chunk)

print("\nAnswer:")
print(answer)