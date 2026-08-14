import math

"""
Purpose: 
    Get the mode that the user decides they want to study with
Parameters:
    None
Return Value:
    mode: str
        The mode that the user wishes to use.
"""
def get_mode():
     mode = input("Enter 'quiz' for quiz mode and 'study' for study mode: ")
     return mode

"""
Purpose:
    Recieve the broad topic that the user wishes to study
Parameters:
    None
Return Value:
    topic: str
        Stores the topic that will be studied. 
"""
def get_topic():
     topic = input("What broad topic do you want to study (Ex. Math, English, Python, or Rocket League): ")
     return topic


"""
Purpose:    
    Get the question that will be passed to the AI and ensure that it passes a
    couple of checks. 
Parameters:
    None
Return Value:
    question: str
        Contains the question that the user is asking the AI
    "break" or "continue": str
        Tells the main program whether it should break or continue if the question
        doesn't pass the tests
"""
def get_question():
    question = input("\nYou: ")

    if question == "done":
        return question, "break"
    if len(question) > 2000:
        print("Enter a shorter question.")
        return  question, "continue"
    if question.strip() == "":
        print("Enter a response, Please.")
        return question, "continue"   

"""
Purpose:
    Gets the values that will be used to create the quiz. 
Parameters:
    None
Return Value:
    specific_topic: str
        Stores the sub-topic that this quiz will be on
    difficulty: str
        Stores the difficulty that the user wants the quiz to be at. 
    total_questions: str
        Stores the total amount of questions that the user wants the quiz
        to be. 
"""
def get_quiz_info():
    specific_topic = input("What specific topic should the quiz be about: ")
    difficulty = input("What difficulty do you want the quiz: ")
    total_questions = input("How many questions do you want in the quiz?: ")
    total_questions = int(total_questions)
    return specific_topic, difficulty, total_questions

"""
Purpose: 
    Get the students response to the question that has been posed
    by the AI
Parameters: 
    quiz_question: chat message
        A message from the chat that stores the schema for a quiz 
        question. 
Return Value: 
    student_answer: str
        A string with the students answer to the question. 
"""
def get_student_answer(quiz_question):
    print("\nQuestion: ", quiz_question.question)
    
    student_answer = input("Your answer: ")

    return student_answer

"""
Purpose: 
    Prints a message that tells the user that the api has 
    failed to work and to try again. 
Parameters: 
    None
Return Value: 
    None
"""
def print_api_error_message():
    print("Sorry I couldn't generate your feedback.\n Please try again.")

"""
Purpose:
    Prints the evaluation that tells the user if they were correct or wrong
    and prints feedback based on their response. Furthermore it creates a 
    int that is either 1 or 0 that will be added to the users score. 
Parameters: 
    evaluation: chat message
        Message from the chat that contains the feedback schema
Return Value:
    1 or 0: int
        A value that will be added to the score. 1 if they were correct
        0 if they were wrong. 
"""
def print_evaluation(evaluation):
    score = 0
    if evaluation.correct:
        print("Correct!")
        score = 1
    else:
        print("Not quite.")
        score = 0
    print("Feedback: ", evaluation.feedback)
    return score

"""
Purpose: 
    Print the final score and percentage of the quiz
Parameters:
    score: int
        This holds the score that the user achieved during the quiz
    total_questions: int
        This holds the total amount of questions
Return Value:
    None
"""
def print_final_score(score, total_questions):
    print(f"Score: {score}/{total_questions}")
    print(f"{math.floor((score/total_questions)*100)}%")

"""
Purpose: 
    Formats and prints the reponse that the AI created. 
Parameters: 
    chat: API chat
        The chat the connects with the AI cna gives it instructions on how to 
        respond
    question: str
        The question that the student provided and wants answered. 
Return Value:
    None
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
        print("Sorry I couldn't generate a response\n Please try again.")