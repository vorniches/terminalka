import openai


def chat():
    prompt = input("You can now enter your prompt: ")
    print("Waiting for response...")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    message = completion.choices[0].message.content
    print(message)
