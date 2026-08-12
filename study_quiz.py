from pydantic import BaseModel

def create_quiz_schemas():
    class QuizQuestion(BaseModel):
       question: str
    return QuizQuestion

def create_evaluation_schema():
    class Evaluation(BaseModel):
        correct: bool
        score: int
        feedback: str
    return Evaluation 

def create_quiz_instructions(topic):
    topic_instructions = f"""You are a {topic} quiz generator
        Create one {topic} question at a time. 
        The question should match the requested topic
        and difficulty. 
        Do not provide the answer. 
        """
    return topic_instructions

def print_quiz():
    pass