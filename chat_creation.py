from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

def create_client():
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    return client

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
