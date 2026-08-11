from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel
import os

# Load the variables stored in the .env file
load_dotenv()

# Create the Python schema that will structure the reponse
class StudyReponse(BaseModel):
    topic: str
    difficulty: str
    explanation: str
    example: str
    practice_question: str

# Create the client and the chat that will be used for the conversation
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

chat = client.chats.create(
    model = "gemini-3.6-flash",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=StudyReponse,
        system_instruction="""
        You are a patient and encouraging Python programming tutor. 
                
        The user is learning Python and wants to understand
        programming concepts rather than simple recieve answers.config=
                
        When teaching:
        - Explain concepts clearly
        - Use simple examples
        - Explain code when necessary. 
        - Ask the student questions to check understanding.
        - Give practice problems when appropriate.
        - Don't assume advanced programming knowledge. 
        """
        )
)

# The loop that will run until the user tells it to stop by saying "done"
while(True): 
    text = "\nYou: "
    question = input(text)

    if question.lower() == "done":
        print("Goodbye")
        break

    response = chat.send_message(question)

    result = response.parsed

    print(f"\nTopic: {result.topic}")
    print(f"\nDifficulty: {result.difficulty}")
    print("\nExplanation: ")
    print(result.explanation)

    print("\nExample: ")
    print(result.example)

    print("\nPractice")
    print(result.practice_question)