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

# Create the system_instructions based on what topic that user wants to study
topic = input("What topic do you want to study (Ex. Math, English, Python, or Rocket League): ")
topic_instructions = client.models.generate_content(
        model="gemini-3.6-flash", 
        contents=f"""Create system instructions for a tutor on {topic} that include the AI's behavior
                    as a patient tutor, an explanation that the audience is learning and wants to understand
                    concepts, and these rules:
                    - Explain concepts clearly
                    - Use simple examples
                    - Ask the student questions to check understanding.
                    - Give practice problems when appropriate.
                    - Don't assume advanced knowledge.
                    """)

chat = client.chats.create(
    model = "gemini-3.6-flash",
    config=types.GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=StudyReponse,
        system_instruction=topic_instructions
        )
)

# The loop that will run until the user tells it to stop by saying "done"
while(True): 
    text = "\nYou: "
    question = input(text)

    # The input barriers that block certain inputs.
    if question.strip() == "":
        print("Please enter a question.")
        continue
    if len(question) > 2000:
        print("Please enter a shorter question.")
        continue
    if question.lower() == "done":
        print("Goodbye")
        break

    # Ensure that the errors don't shut down the program. 
    try:
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
    except:
        print("Sorry I couldn't generate your quiz\n Please try again.")