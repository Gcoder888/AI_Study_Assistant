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
        if mode == "quiz":
            topic = input("What broad topic do you want to study (Ex. Math, English, Python, or Rocket League): ")
            score = 0
            specific_topic = input("What specifc topic should the quiz be about\n")
            total_questions = input("How many questions do you want in the quiz?\n")
            total_questions = int(total_questions)
            quiz_schema = create_quiz_schema()
            feedback_schema = create_feedback_schema()
            quiz_instructions = create_quiz_instructions(topic)
            evaluation_instructions = create_evaluation_instructions(topic)
            quiz_chat = create_quiz_chat(client, quiz_schema, quiz_instructions)
            evaluation_chat = create_evaluation_chat(client, feedback_schema, evaluation_instructions)
            increment = 0
            while increment < total_questions:
                print_quiz(quiz_chat, evaluation_chat, specific_topic, score)
                increment += 1
        elif mode == "study":
            topic = input("What broad topic do you want to study (Ex. Math, English, Python, or Rocket League): ")
            study_schema = create_study_schema()
            topic_instructions = create_study_intructions(topic)
            study_chat = create_study_chat(client, study_schema, topic_instructions)
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
        else:
            print("Enter a valid mode")

if __name__ == "__main__":
    main()