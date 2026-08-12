from google import genai
from google.genai import types
from pydantic import BaseModel

def create_study_class():   
    # Create the Python schemas neccessary for the program
    class StudyReponse(BaseModel):
        topic: str
        difficulty: str
        explanation: str
        example: str
        practice_question: str
    return StudyReponse

def create_study_intructions(client):
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
    return topic_instructions


def print_study_response(chat, question):
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
