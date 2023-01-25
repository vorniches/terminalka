import openai
from authentication import authenticate
from chat import chat

if __name__ == "__main__":
    openai.api_key = authenticate()
    while True:
        try:
            chat()
        except Exception as e:
            print(f"An error occurred: {e}")
