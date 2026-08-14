import math
from schema_creation import create_feedback_schema, create_quiz_schema, create_study_schema
from instruction_creation import create_evaluation_instructions, create_quiz_instructions, create_study_intructions
from printing import print_quiz, print_study_response
from chat_creation import create_client, create_quiz_chat, create_evaluation_chat, create_study_chat

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
    while(True):
        client = create_client()
        # Decide whether the AI will be in quiz mode or study mode
        mode = input("Enter 'quiz' for quiz mode and 'study' for study mode: ")

        # Control how the program will run if the quiz mode is selected
        if mode == "quiz":
            # Find out what topic the quiz will be on
            topic = input("What broad topic do you want to study (Ex. Math, English, Python, or Rocket League): ")

            # Create variables that will store information about how long the quiz is and what the results are
            score = 0
            specific_topic = input("What specifc topic should the quiz be about\n")
            total_questions = input("How many questions do you want in the quiz?\n")
            total_questions = int(total_questions)

            # Set all the variables needed to createthe chats that will run the quiz and feedback
            quiz_schema = create_quiz_schema()
            feedback_schema = create_feedback_schema()
            quiz_instructions = create_quiz_instructions(topic)
            evaluation_instructions = create_evaluation_instructions(topic)

            # Create the chats necessary to run the quiz
            quiz_chat = create_quiz_chat(client, quiz_schema, quiz_instructions)
            evaluation_chat = create_evaluation_chat(client, feedback_schema, evaluation_instructions)

            # Run the quiz until the required questions have been reached
            increment = 0
            while increment < total_questions:
                print_quiz(quiz_chat, evaluation_chat, specific_topic, score)
                increment += 1
            print(f"Score: {score}/{total_questions}")
            print(f"{math.floor(score/total_questions)}%")

        # Control how the program will be run if the study mode is selected
        elif mode == "study":
            topic = input("What broad topic do you want to study (Ex. Math, English, Python, or Rocket League): ")

            # Create the necessary variables that will be used to create the required chat
            study_schema = create_study_schema()
            topic_instructions = create_study_intructions(topic)

            # Create the chat that will be interacted with for this program
            study_chat = create_study_chat(client, study_schema, topic_instructions)

            # The loop that will be run until the user decides they are done studying
            while(True):
                question = input("\nYou: ")

                if question == "done":
                    break
                if len(question) > 2000:
                    print("Enter a shorter question.")
                    continue
                if question.strip() == "":
                    print("Enter a response, Please.")
                    continue

                print_study_response(study_chat, question)
            break

        # If user enters done end the program
        elif mode == "done":
            break

        # Make sure a valid mode is selected
        else:
            print("Enter a valid mode")

if __name__ == "__main__":
    main()