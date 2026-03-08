from openai import OpenAI

client = OpenAI()

# response = client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages=[
#         {"role": "system", "content": "Explain microservices in simple terms."}
#     ])

# ai_answer = response.choices[0].message.content
# print("AI Answer:")
# print(ai_answer)

messages = [{"role": "system", "content": "You are a helpful assistant that answers questions about programming."}]

while True:
    user_input = input("Ask something (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        messages.append({"role": "user", "content": user_input})
        stream = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages= messages,
        stream = True
    )
        print("\nAI:", end=" ")
        full_response = ""
        for chunk in stream:
            token = chunk.choices[0].delta.content
            if token:
                print(token, end= " ",flush=True)
                full_response += token

        print("\n" + "-"*40)

        messages.append({"role": "assistant", "content": full_response})

    except Exception as e:
        print(f"An error occurred: {e}")