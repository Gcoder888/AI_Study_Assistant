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

"""
Purpose: 
    Creates the intructions that controls how the AI thinks
    about the inputs. 
Parameters: 
    topic: str
        This holds the topic that the student chose to study
Return Value:
    topic_instructions: str
        This holds the instructions that control how an AI acts
"""
def create_quiz_instructions(topic, difficulty):
    # Create specificed quiz instructions for a topic
    topic_instructions = f"""You are a {topic} quiz generator
        Create one {topic} question at a time. 
        Make the question match a {difficulty} difficulty.
        Do not provide the answer. 
        """
    return topic_instructions

"""
Purpose: 
    This creates the instructions that the evaluation chat needs to work 
    effectively. 
Parameters:
    topic: str
        Provides the topic that is related to the question and answer. 
Return Value: 
    topic_instructions:
        Includes the instructions for the evaluation chat. 
"""
def create_evaluation_instructions(topic):
    # Create specificed evaluation instructions
    topic_instructions = f"""You are a answer evaluator for
    topic: {topic}. Understand that the student is learning and 
    needs feedback that is constructice and helps the student 
    learn.
    """
    return topic_instructions

"""
Purpose: 
    Creates the instructions that tell the AI how to act 
    when responding to the students queries
Parameters: 
    topic: str
        Holds the topic that the student wishes to study. 
Return Value: 
    topic_instructions: str
        Holds the instructions that are used when creating the chat.
"""
def create_study_intructions(topic):
    # Create the system_instructions based on what topic that user wants to study
    topic_instructions = f"""You are a patient {topic} tutor. 
        The user is learning and wants to understand the concepts. 
        Follow these rules when answering their questions
        - Explain concepts clearly
        - Use simple examples
        - Ask the student questions to check understanding.
        - Give practice problems when appropriate.
        - Don't assume advanced knowledge.
        """
    return topic_instructions

"""
Purpose: 
    Take in a chat, a question, and previous questions then create a new 
    question. 
Parameters:    
    quiz_chat: chat
        The chat that will be used to respond to the user.
    topic: str
        The topic that the quiz is to be based on
    asked_questions: list
        A list that stores all previous questions. 
Return Value: 
    response: chat message
        The message that contains info based on the schema
"""
def quiz_send_message(quiz_chat, topic, asked_questions):
    response = quiz_chat.send_message(
        f"""
        {topic}. Please don't repeat these previous questions.
        Previous Questions: \n
        {"\n".join(asked_questions)}
        """)
    return response

"""
Purpose: 
    Craft an evaluation response to the question and student answer.
Parameters: 
    evaluation_chat: chat
        The chat the includes a schema to craft a score and feedback
    question: chat message
        The message the quiz chat produced which contains the question the
        student answers
    student_answer: str
        The answer the student gave to the question the AI had proposed
Return Value: 
    evaluation_response: chat message
        The message that contains info based on the evaluation schema
"""
def evaluation_send_message(evaluation_chat, question, student_answer):
    evaluation_response = evaluation_chat.send_message(
        f"""
        Question:
        {question.question}
    
        Student answer:
        {student_answer}
        """
        )
    return evaluation_response

"""
Purpose: 
    Craft a study response that will answer the students question and give examples
Parameters: 
    study_chat: chat
        The chat the includes the schema that helps a student study.
    question: str
        The question that the student wishes to have answerd. 
Return Value:
    response: chat message
        The message that contains info based on the study schema
"""
def study_send_message(study_chat, question):
    response = study_chat.send_message(question)
    return response