import openai


def authenticate():
    return input("Please enter your OpenAI API key: ")


def chat():
    prompt = input("You can now enter your prompt: ")
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


if __name__ == "__main__":
    openai.api_key = authenticate()
    while True:
        chat()