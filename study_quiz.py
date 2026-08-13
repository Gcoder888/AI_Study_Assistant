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
def create_quiz_schemas():
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
def create_evaluation_schema():
    # Create the class used to evaluate a questions answer
    class Evaluation(BaseModel):
        correct: bool
        score: int
        feedback: str
    return Evaluation 

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
def create_quiz_instructions(topic: str):
    # Create specificed quiz instructions for a topic
    topic_instructions = f"""You are a {topic} quiz generator
        Create one {topic} question at a time. 
        The question should match the requested topic
        and difficulty. 
        Do not provide the answer. 
        """
    return topic_instructions

"""
Purpose: 
    Print the quiz question and the evaluation response that the AI provides. 
Parameters: 
    quiz_chat: API chat
        Creates the quiz questions
    evaluation_chat: API chat
        Creates the evaluation reponse to student answer
    question: str
        Holds what the question should be about
    score: int
        Holds the score that the student gets on the quiz
"""
def print_quiz(quiz_chat, evaluation_chat, question, score):
    # Print out the results of a quiz question and the evaluation of a response
    response = quiz_chat.send_message(question)

    quiz_question = response.parsed

    # Print the question and take in the students answer
    print("\nQuestion: ", quiz_question.question)

    student_answer = input("Your answer: ")

    # Craft an evaluation 
    evaluation_response = evaluation_chat.send_message(
        f"""
        Question:
        {quiz_question.question}

        Student answer:
        {student_answer}
        """
    )

    # Change the score for the quiz and portray the evaluation
    evaluation = evaluation_response.parsed

    if evaluation.correct:
        score += 1
        print("Correct!")
    else:
        print("Not quite.")

    print("Feedback: ", evaluation.feedback)