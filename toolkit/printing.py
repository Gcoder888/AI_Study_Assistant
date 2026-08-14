
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
    try:
        response = quiz_chat.send_message(question)
    except:
         print("Sorry I couldn't generate your quiz.\n Please try again.")

    quiz_question = response.parsed

    # Print the question and take in the students answer
    print("\nQuestion: ", quiz_question.question)

    student_answer = input("Your answer: ")

    if student_answer == "done":
         return

    # Craft an evaluation 
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
         print("Sorry I couldn't generate your feedback.\n Please try again.")

    # Change the score for the quiz and portray the evaluation
    evaluation = evaluation_response.parsed

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