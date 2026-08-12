from pydantic import BaseModel

def create_study_schema():   
    # Create the Python schemas neccessary for the program
    class StudyReponse(BaseModel):
        topic: str
        difficulty: str
        explanation: str
        example: str
        practice_question: str
    return StudyReponse

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
