from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

question = input("What do you want to learn")

reponse = client.models.generate_content(
    model="gemini-3.6-flash", 
    contents=f"Explain this topic to me like a beginner: {question}"
)

print(reponse.text)