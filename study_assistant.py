from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import study_tutor
import study_quiz

"""
Purpose:
    This runs the AI chatbot which asks what topic you want to 
    study and then if you want to study with a chat or a quiz. 
Parameters:
    None
Return Value:
    None
"""
def main():
    # Load the variables stored in the .env file
    load_dotenv()

    while(True):
        # Decide whether the AI will be in quiz mode or study mode
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        mode = input("Enter 'quiz' for quiz mode and 'study' for study mode")
        topic = input("What topic do you want to study (Ex. Math, English, Python, or Rocket League): ")
        if mode == "quiz":
            quiz_schema = study_quiz.create_quiz_schema()
            quiz_instructions = study_quiz.create_quiz_instructions(topic)
            chat = client.chats.create(
                model="gemini-3.6-flash", 
                config=types.GenerateContentConfig(
                    response_mime_type="application/json", 
                    response_schema=quiz_schema, 
                    system_instruction=quiz_instructions
                )
            )
            while(True):
                pass
            break

        elif mode == "study":
            study_schema = study_tutor.create_study_schema()
            topic_instructions = study_tutor.create_study_intructions(topic)
            chat = client.chats.create(
                model = "gemini-3.6-flash",
                config=types.GenerateContentConfig(
                    response_mime_type="application/json",
                    response_schema=study_schema,
                    system_instruction=topic_instructions
                    )
                )
            while(True):
                pass
            break
        else:
            print("Enter a valid mode")

if __name__ == "__main__":
    main()