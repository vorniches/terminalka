import os
from dotenv import load_dotenv


def authenticate():
    if os.path.exists('.env'):
        load_dotenv()
        return os.getenv("OPENAI_API_KEY")
    else:
        return input("Please enter your OpenAI API key: ")
