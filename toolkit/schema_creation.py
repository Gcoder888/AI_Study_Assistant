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