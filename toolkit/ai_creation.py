from pydantic import BaseModel

"""
Purpose:
    This function is used to create the schema that is 
    used to control the format of how the AI will respond if the user 
    choses a quiz. 
Parameters:
    None
Return Value:
    QuizQuestion: class
        This class holds the schema for a quiz question
"""
def create_quiz_schema():
    # Create the class used for the quiz
    class QuizQuestion(BaseModel):
       question: str
    return QuizQuestion

"""
Purpose: 
    Creates the schema that controls the format of the evaluation to the response
Parameters: 
    None
Return Value:
    Evaluation: class
        Holds the schema that controls the format of the answer evaluation
"""
def create_feedback_schema():
    # Create the class used to evaluate a questions answer
    class Feedback(BaseModel):
        correct: bool
        score: int
        feedback: str
    return Feedback

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