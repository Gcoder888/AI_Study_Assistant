from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

first_time = True
while(True):
    if first_time:
        text = "What do you want to learn: "
        first_time = False
    else:
        text = "Do you have any follow up questions? \n"
    question = input(text)

    if question == "exit":
        break

    reponse = client.models.generate_content(
        model="gemini-3.6-flash", 
        contents=f"Explain this topic to me like a beginner: {question}"
    )

    print(reponse.text)