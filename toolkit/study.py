from toolkit import ai_creation
from toolkit import user_interface

"""
Purpose: 
    Runs the loop that controls the study mode that a user will use to study. 
Parameters: 
    study_chat: chat
        This is the chat that is used to send messages and get responses from the
        AI so that the user can study a certain topic. 
Return Value: 
    None
"""
def run_study(study_chat):
    while(True):
        user = user_interface
        ai = ai_creation

        question, check = user.get_question()

        if check == "break":
            break
        if check == "continue":
            continue

        try:
            response = ai.study_send_message(study_chat, question)
        except:
            user.print_api_error_message()

        result = response.parsed

        user.print_study_response(result)