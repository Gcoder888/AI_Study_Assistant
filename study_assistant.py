from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model = "gemini-3.6-flash"
)

first_time = True
while(True):
    if first_time:
        text = "What do you want to learn: "
        first_time = False
    else:
        text = "\nYou: "
    question = input(text)

    if question.lower() == "done":
        print("Goodbye")
        break

    reponse = chat.send_message(question)

    print("\nAI Tutor: ")
    print(reponse.text)