from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

"""
Purpose: 
    Create the client that uses my api key to connect to the gemini AI that is being 
    used for this program
Parameters:
    None
Return Value:
    client: genai.Client()
        The connection to the api and AI that allows me to build chats. 
"""
def create_client():
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client

"""
Purpose: 
    Creates the chat that is used to create quiz questions.
Parameters:
    client: genai_Client()
        How I connect to the api and AI
    quiz_schema: QuizQuestion
        Details how the chat is going to format its respoonse
    quiz_instructions: str
        Details how the chat should act. 
Return Value: 
    quiz_chat: chat
        Takes in messages from the user and gives the to the AI and gets a response back.
"""
def create_quiz_chat(client, quiz_schema, quiz_instructions):
    quiz_chat = client.chats.create(
        model="gemini-3.6-flash", 
        config=types.GenerateContentConfig(
            response_mime_type="application/json", 
            response_schema=quiz_schema, 
            system_instruction=quiz_instructions
        )
    )
    return quiz_chat

"""
Purpose: 
    Creates the chat that is used to create question and answer evaluations.
Parameters:
    client: genai_Client()
        How I connect to the api and AI
    feedback_schema: Feedback
        Details how the chat is going to format its respoonse
    evaluation_instructions: str
        Details how the chat should act. 
Return Value: 
    evaluation_chat: chat
        Takes in messages from the user and gives the to the AI and gets a response back.
"""
def create_evaluation_chat(client, feedback_schema, evaluation_instructions):
    evaluation_chat = client.chats.create(
        model="gemini-3.6-flash", 
        config=types.GenerateContentConfig(
            response_mime_type="application/json", 
            response_schema=feedback_schema, 
            system_instruction=evaluation_instructions
        )
    )
    return evaluation_chat

"""
Purpose: 
    Creates the chat that is used to study and interact with.
Parameters:
    client: genai_Client()
        How I connect to the api and AI
    study_schema: QuizQuestion
        Details how the chat is going to format its respoonse
    study_instructions: str
        Details how the chat should act. 
Return Value: 
    study_chat: chat
        Takes in messages from the user and gives the to the AI and gets a response back.
"""
def create_study_chat(client, study_schema, study_instructions):
    study_chat = client.chats.create(
        model = "gemini-3.6-flash",
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=study_schema,
            system_instruction=study_instructions
        )
    )
    return study_chat
