import openai
import sys

def chat():
    while True:
        prompt = input("You can now enter your prompt: ")
        if prompt.lower() == "exit()":
            print("Closing the app...")
            sys.exit()  # Terminate the program
        print("Waiting for response...")
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0301",
            messages=[{"role": "user", "content": prompt}]
        )

        message = completion.choices[0].message.content
        print(message)
