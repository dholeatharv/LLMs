from openai import OpenAI
import json

client = OpenAI()

prompt = """
Explain microservices and return the result in JSON format with:

definition
advantages
disadvantages
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a backend architecture expert. Return valid JSON only."},
        {"role": "user", "content": prompt}
    ]
)

result = response.choices[0].message.content

print("Raw AI output:")
print(result)
# Remove markdown code fences if present
cleaned = result.strip()

if cleaned.startswith("```json"):
    cleaned = cleaned.removeprefix("```json").strip()
elif cleaned.startswith("```"):
    cleaned = cleaned.removeprefix("```").strip()

if cleaned.endswith("```"):
    cleaned = cleaned.removesuffix("```").strip()

data = json.loads(cleaned)

print("\nParsed JSON:")
print("Definition:", data["microservices"]["definition"])
print("Advantages:", data["microservices"]["advantages"])
print("Disadvantages:", data["microservices"]["disadvantages"])