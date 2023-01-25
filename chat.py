import openai


def chat():
    prompt = input("You can now enter your prompt: ")
    print("Waiting for response...")
    completions = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    print(message)
