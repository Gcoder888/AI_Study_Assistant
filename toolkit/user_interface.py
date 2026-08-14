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
    print(f"{math.floor(score/total_questions)}%")

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
Return Value:
    None
"""
def print_quiz(quiz_chat, evaluation_chat, question, score):
    # Print out the results of a quiz question and the evaluation of a response
    asked_questions = []
    # AI
    try:
        response = quiz_chat.send_message(
             f"""
             {question}. Please don't repeat these previous questions.
             Previous Questions: \n
             {"\n".join(asked_questions)}
             """)
    except:
         # Print
         print("Sorry I couldn't generate your quiz.\n Please try again.")

    quiz_question = response.parsed

    asked_questions.append(quiz_question.question)

    # Print the question and take in the students answer
    # Print
    print("\nQuestion: ", quiz_question.question)

    student_answer = input("Your answer: ")

    if student_answer == "done":
         return

    # Craft an evaluation 
    # AI
    try:
        evaluation_response = evaluation_chat.send_message(
            f"""
            Question:
            {quiz_question.question}

            Student answer:
            {student_answer}
            """
        )
    except:
         # Print
         print("Sorry I couldn't generate your feedback.\n Please try again.")

    # Change the score for the quiz and portray the evaluation
    evaluation = evaluation_response.parsed

    # Print
    if evaluation.correct:
        score += 1
        print("Correct!")
    else:
        print("Not quite.")

    print("Feedback: ", evaluation.feedback)

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
    specific_topic = input("What specifc topic should the quiz be about\n")
    difficulty = input("What difficulty do you want the quiz\n")
    total_questions = input("How many questions do you want in the quiz?\n")
    total_questions = int(total_questions)
    return specific_topic, difficulty, total_questions
     