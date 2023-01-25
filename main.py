import openai
import os
from dotenv import load_dotenv


def authenticate():
    if os.path.exists('.env'):
        load_dotenv()
        return os.getenv("API_KEY")
    else:
        return input("Please enter your OpenAI API key: ")


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


if __name__ == "__main__":
    openai.api_key = authenticate()
    while True:
        chat()
