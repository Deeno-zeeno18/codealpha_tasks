"""
CREATING A CHATBOT THAT REPLIES TO OUR GREETINGS
"""

import random

"""
CODE FOR ASKING FOR THE GREETING
"""
def ask_for_your_greeting():
    your_greeting = input("GREET:").strip().rstrip("?")
    while not all(c.isalpha() or c.isspace() for c in your_greeting):
        print(f"Please enter characters")
        your_greeting = input("GREET:").strip().rstrip("?")
    return your_greeting.lower()

your_expression = ask_for_your_greeting()

"""
LIST OF PREDEFINED GREETINGS
"""
def return_expressions_dict():
    expressions = {
        "WELCOMING EXPRESSIONS": ["hello", "hi", "hey", "welcome"],
        "WELCOMING QUESTIONS": ["how are you", "how are you doing"],
        "MORNING EXPRESSIONS": ["good morning", "new day"],
        "MORNING QUESTIONS": ["how was your sleep"],
        "AFTERNOON EXPRESSIONS": ["good afternoon"],
        "AFTERNOON QUESTIONS": ["how was school", "how was work"],
        "EVENING EXPRESSIONS": ["good evening", "good night"],
        "EVENING QUESTIONS": ["how was your day"],
        "GOODBYE MESSAGES": ["goodbye", "Bye", "see you next time", "see you soon", "See you later"]
    }
    return expressions


expression_list = return_expressions_dict()

"""
REPLYING TO MESSAGES
"""
def return_responses_dict():
    return {
        "WELCOME EXPRESSIONS REPS": ["Hey there", "Welcome too", "Nice meeting you", "Hi there"],
        "WELCOME QUESTIONS REPS": ["I am doing well", "I am doing great", "Excellently well"],
        "MORNING EXPRESSIONS REPS": ["Good morning", "Good day"],
        "MORNING QUESTIONS REPS": ["Sleep was good"],
        "AFTERNOON EXPRESSIONS REPS": ["Good afternoon", "Noon already?"],
        "AFTERNOON QUESTIONS REPS": ["Everything is fine"],
        "EVENING EXPRESSIONS REPS": ["Good evening", "Good night"],
        "EVENING QUESTIONS REPS": ["My day was good"],
        "GOODBYE MESSAGES": ["goodbye", "bye", "see you next time", "see you soon", "see you later"]
        }

responses = return_responses_dict()


"""
THIS MATCHES THE STRINGS OF THE WELCOMING EXPRESSIONS TO THE ANSWERS WHERE
THE VALUES SERVE AS A LOOKUP KEY FOR VALUES IN ANOTHER DICTIONARY
"""
def reply_a_message():
    category_map = {
        "WELCOMING EXPRESSIONS": "WELCOME EXPRESSIONS REPS",
        "WELCOMING QUESTIONS": "WELCOME QUESTIONS REPS",
        "MORNING EXPRESSIONS": "MORNING EXPRESSIONS REPS",
        "MORNING QUESTIONS": "MORNING QUESTIONS REPS",
        "AFTERNOON EXPRESSIONS": "AFTERNOON EXPRESSIONS REPS",
        "AFTERNOON QUESTIONS": "AFTERNOON QUESTIONS REPS",
        "EVENING EXPRESSIONS": "EVENING EXPRESSIONS REPS",
        "EVENING QUESTIONS": "EVENING QUESTIONS REPS",
        "GOODBYE MESSAGES": "GOODBYE MESSAGES REPS",
    }

    for greeting, phrases in expression_list.items():
        if your_expression in phrases:
            reply_category = category_map[greeting]
            return random.choice(responses[reply_category])
    return f"Response not found for {your_expression}"

