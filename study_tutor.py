from pydantic import BaseModel

"""
Purpose: 
    Creates the schema that controls how the AI helps
    a student study. 
Parameters:
    None
Return Value:
    StudyResponse: class
        Crafts how the AI will respond to the questions of
        the student. 
"""
def create_study_schema():   
    # Create the Python schemas neccessary for the program
    class StudyReponse(BaseModel):
        topic: str
        difficulty: str
        explanation: str
        example: str
        practice_question: str
    return StudyReponse

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
    Formats and prints the reponse that the AI created. 
Parameters: 
    chat: API chat
        The chat the connects with the AI cna gives it instructions on how to 
        respond
    question: str
        The question that the student provided and wants answered. 
"""
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
