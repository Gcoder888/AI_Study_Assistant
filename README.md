# AI Study Assistant
    An AI-powered study assistant built with Python and the Google Gemini API. The goal of this project is to create a helpful tutor that can explain concepts, generate quizzes, evaluate answers, and provide feedback. 

## Features

---

    - AI-powered tutoring
    - Conversational chat
    - Structured JSON responses
    - AI-generated quiz questions
    - AI evaluation of answers
    - Quiz scoring
    - Input validation
    - Error handling
    - Secure API key management
    - Modular Python code

---

## Technologies

---

    - Python
    - Google Gemimi API
    - Pydantic
    - python-dotenv

---

## Installation

---

    1. Clone the repository

        ```bash
        git clone https://github.com/Gcoder888/AI_Study_Assistant
        cd AI-Study-Assistant
        ```
    2. Create a virtual environment

        ```bash
        python -m venv .venv
        ```
        Activate it
            Windows: 

            ```bash
            .venv\Scripts\activate
            ```
            macOS/Linux

            ```bash
            source .venv/bin/activate
            ```
    3. Install dependencies

        ```bash
        pip install -r requirements.txt
        ```

---

## Python Structure

---

|
|
|______ai_env
|
|______toolkit
|      |
|      |______ai_creation.py
|      |
|      |______quiz.py
|      |
|      |______schema_creation.py
|      |
|      |______study.py
|      |
|      |______user_interface.py
|
|______.env
|
|______.gitignore
|
|______README.md
|
|______study_assistant.py

study_assistant.py
    The main entry point for the application. It connects the different parts of the program. 

ai_creation.py
    Handles communication with the Google Gemini API, including creating chats and sending requests.

quiz.py
    Contains the logic for generating questions, evaluation answers, and tracking scores. 

schema_creation.py
    Contains the Pydantic schemas used to structure Gemini's responses. 

study.py
    Contains the logic for crafting the setup for the study version

user_interface.py
    Handles user input and displaying information to the user. 

---

## Example Output

---

### Quiz
Enter 'quiz' for quiz mode and 'study' for study mode: quiz
What broad topic do you want to study (Ex. Math, English, Python, or Rocket League): python
What specific topic should the quiz be about: lists
What difficulty do you want the quiz: beginner
How many questions do you want in the quiz?: 2

Question:  Which built-in list method is used to add an element to the end of a list in Python?
Your answer: append()
Correct!
Feedback:  Great job! The append() method is indeed used toadd an element to the end of a list in Python.

Question:  What index value is used to access the very lastelement of a non-empty list in Python?
Your answer: 2
Not quite.
Feedback:  Not quite. In Python, negative indexing is used to access elements from the end of a list. The index -1 always refers to the very last element of a non-empty list. Index 2 refers to the third element (since indexing starts at 0).
Score: 1/2
50%
Enter 'quiz' for quiz mode and 'study' for study mode: done

### Study
Enter 'quiz' for quiz mode and 'study' for study mode: study

What broad topic do you want to study (Ex. Math, English, Python, or Rocket League): python

You: What are lists

Topic: Python Lists

Difficulty: Beginner

Explanation: 
A list in Python is used to store multiple items in a single variable. Think of it like a digital shopping list or a container where you can hold a collection of things, like numbers or words. You create a list by putting items inside square brackets [], separated by commas. Lists stay in the order you create them, and you can add, remove, or change items at any time.

Example: 
fruits = ['apple', 'banana', 'cherry']; print(fruits[0]); fruits.append('orange'); print(fruits)

Practice
How would you write a line of Python code to create a list named 'colors' that contains three color names as strings: 'red', 'green', and 'blue'?

You: done

---

## Future Improvements

---

    - Multiple-choice quizzes
    - Adaptive difficulty
    - Progress tracking
    - Flashcards
    - Study history
    - More detailed statistics
    - Improved user interface
    - Web interface

---

## Learning Process

---

This project was developed as part of a structured Python and AI application development learning journey.

Rather than following a traditional tutorial or simply copying a finished project, I built the application side by side with ChatGPT, introducing new concepts as they became relevant to the project. I implemented the code, tested features, worked through errors, and gradually refactored the application as the architecture became more complex.

Throughout the project, I learned and applied concepts including:

Python project structure and modular design
Virtual environments and package management
APIs and how applications communicate with AI services
API requests and responses
JSON and structured data
Google Gemini API integration
API keys and environment variables
.env files and .gitignore for security
Prompt engineering and system instructions
Conversational AI and chat history
Structured AI responses using Pydantic schemas
Type validation and predictable data structures
Separating AI logic, UI, schemas, and application logic
Python modules, imports, and functions
Input validation
Error handling
AI-generated quiz questions
AI evaluation and feedback
Score tracking and application state
The distinction between AI reasoning and traditional program logic

A major part of the learning process was understanding why each component was designed the way it was rather than simply making the application work. ChatGPT served as a coding tutor and development partner, helping me understand unfamiliar concepts, debug problems, and make architectural decisions while I remained responsible for implementing and testing the project.

The goal of the project was therefore not just to create an AI study assistant, but to develop the skills needed to design, build, debug, and expand Python applications independently while effectively using AI as a development tool.

---

## About This Project

---

This repository represents my progression from learning Python fundamentals to building a practical AI-powered application. It emphasizes learning both Python programming and modern AI application development, including API integration, structured data, prompt engineering, modular design, error handling, secure API key management, and building reusable components. The project also demonstrates how traditional Python logic can work alongside AI to create a functional and extensible application.

---

## License

MIT License