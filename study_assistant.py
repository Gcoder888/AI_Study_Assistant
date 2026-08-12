from google import genai
from google.genai import types
from dotenv import load_dotenv
from pydantic import BaseModel
import os
import study_tutor

def main():
    # Load the variables stored in the .env file
    load_dotenv()

    # Create the Python schemas neccessary for the program
    study_response_class = study_tutor.create_study_class()

    # Create the client and the chat that will be used for the conversation
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    # Create the topic instructions
    topic_instructions = study_tutor.create_study_intructions(client)

    chat = client.chats.create(
        model = "gemini-3.6-flash",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=study_response_class,
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

        study_tutor.print_study_response(chat, question)

if __name__ == "__main__":
    main()