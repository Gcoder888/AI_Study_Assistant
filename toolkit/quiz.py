from toolkit import ai_creation
from toolkit import user_interface

"""
Purpose: 
    This runs the quiz. It prints each question takes in the answer and then provides feedback
    based on the answer. It runs until all the questions have been answered and then displays a
    score on the quiz and a percentage. 
Parameters: 
    quiz_chat: chat
        This is the chat that returns quiz questions about a certain topic. 
    evaluation_chat: chat
        This is the chat that returns a score and feedback about a question and answer. 
    topic: str
        This is the topic that quiz is going to be on. 
Return Value: 
    None
"""
def run_quiz(quiz_chat, evaluation_chat, topic):
    ai = ai_creation
    user = user_interface

    asked_questions = []

    try:
        response = ai.quiz_send_message(quiz_chat, topic, asked_questions)
    except:
        user.print_api_error_message()

    quiz_question = response.parsed
    asked_questions.append(quiz_question.question)

    # Print the question and take in the students answer
    student_answer = user.get_student_answer(quiz_question)

    try:
        evaluation_response = ai.evaluation_send_message(evaluation_chat, quiz_question, student_answer)
    except:
        user.print_api_error_message()

    evaluation = evaluation_response.parsed

    score = user.print_evaluation(evaluation)
    return score

