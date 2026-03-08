from openai import OpenAI
import math

client = OpenAI()

sentences = [
    "Spring Boot security",
    "How to secure a Spring Boot API",
    "Cooking pasta recipe"
]

# Function to get embedding
def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Function to calculate cosine similarity
def cosine_similarity(a, b):
    dot_product = sum(x*y for x, y in zip(a, b))
    
    magnitude_a = math.sqrt(sum(x*x for x in a))
    magnitude_b = math.sqrt(sum(x*x for x in b))
    
    return dot_product / (magnitude_a * magnitude_b)

embeddings = [get_embedding(sentence) for sentence in sentences]

query = "How do I secure my Spring Boot service?"

query_embedding = get_embedding(query)

scores = []

for i, emb in enumerate(embeddings):
    similarity = cosine_similarity(query_embedding, emb)
    scores.append((sentences[i], similarity))

scores.sort(key=lambda x: x[1], reverse=True)

print("Query:", query)
print("\nMost similar sentences:")

for sentence, score in scores:
    print(f"{sentence} -> {score:.3f}")