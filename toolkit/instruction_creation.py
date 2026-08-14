
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
    This creates the instructions that the evaluation chat needs to work 
    effectively. 
Parameters:
    topic: str
        Provides the topic that is related to the question and answer. 
Return Value: 
    topic_instructions:
        Includes the instructions for the evaluation chat. 
"""
def create_evaluation_instructions(topic: str):
    # Create specificed evaluation instructions
    topic_instructions = f"""You are a answer evaluator for
    topic: {topic}. Understand that the student is learning and 
    needs feedback that is constructice and helps the student 
    learn.
    """
    return topic_instructions

"""
Purpose: 
    Creates the instructions that tell the AI how to act 
    when responding to the students queries
Parameters: 
    topic: str
        Holds the topic that the student wishes to study. 
Return Value: 
    topic_instructions: str
        Holds the instructions that are used when creating the chat.
"""
def create_study_intructions(topic):
    # Create the system_instructions based on what topic that user wants to study
    topic_instructions = f"""You are a patient {topic} tutor. 
        The user is learning and wants to understand the concepts. 
        Follow these rules when answering their questions
        - Explain concepts clearly
        - Use simple examples
        - Ask the student questions to check understanding.
        - Give practice problems when appropriate.
        - Don't assume advanced knowledge.
        """
    return topic_instructions