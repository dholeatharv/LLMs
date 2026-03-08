from openai import OpenAI

client = OpenAI()
text = "I am learing about neuron networks and how they can be used for image recognition."
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=text
)

embedding = response.data[0].embedding
print("Embedding Length:", len(embedding))
print("First 10 values of the embedding:", embedding[:10])