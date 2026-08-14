import toolkit.schema_creation
import toolkit.user_interface
import toolkit.ai_creation
import toolkit.quiz

"""
Purpose:
    This runs the AI chatbot which asks what topic you want to 
    study and then if you want to study with a chat or a quiz. 
Parameters:
    None
Return Value:
    None
"""
def main():
    schema = toolkit.schema_creation
    user = toolkit.user_interface
    ai = toolkit.ai_creation
    quiz = toolkit.quiz
    while(True):
        client = ai.create_client()
        # Decide whether the AI will be in quiz mode or study mode
        mode = user.get_mode()

        # Control how the program will run if the quiz mode is selected
        if mode == "quiz":
            # Find out what topic the quiz will be on
            topic = user.get_topic()

            # Create variables that will store information about how long the quiz is and what the results are
            score = 0
            specific_topic, difficulty, total_questions = user.get_quiz_info()

            # Set all the variables needed to createthe chats that will run the quiz and feedback
            quiz_schema = schema.create_quiz_schema()
            feedback_schema = schema.create_feedback_schema()
            quiz_instructions = ai.create_quiz_instructions(topic, difficulty)
            evaluation_instructions = ai.create_evaluation_instructions(topic)

            # Create the chats necessary to run the quiz
            quiz_chat = ai.create_quiz_chat(client, quiz_schema, quiz_instructions)
            evaluation_chat = ai.create_evaluation_chat(client, feedback_schema, evaluation_instructions)

            # Run the quiz until the required questions have been reached
            increment = 0
            while increment < total_questions:
                score += quiz.run_quiz(quiz_chat, evaluation_chat, specific_topic)
                increment += 1
            user.print_final_score(score, total_questions)

        # Control how the program will be run if the study mode is selected
        elif mode == "study":
            topic = user.get_topic()

            # Create the necessary variables that will be used to create the required chat
            study_schema = schema.create_study_schema()
            topic_instructions = ai.create_study_intructions(topic)

            # Create the chat that will be interacted with for this program
            study_chat = ai.create_study_chat(client, study_schema, topic_instructions)

            # The loop that will be run until the user decides they are done studying
            while(True):
                question, check = user.get_question()

                if check == "break":
                    break
                if check == "continue":
                    continue
                user.print_study_response(study_chat, question)
            break

        # If user enters done end the program
        elif mode == "done":
            break

        # Make sure a valid mode is selected
        else:
            print("Enter a valid mode")

if __name__ == "__main__":
    main()