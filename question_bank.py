#---------------------------------------
#  Question Bank
#    Student B
#---------------------------------------

import random

# Simplified example with one category. Expand as needed.
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O"),
        ("What is the chemical symbol for sugar?", "C12H22O11"),
        ("Which planet is also known as Swift Planet?", "Mercury"),
        ("What process do plants use to create energy?", "Photosynthesis"),
        ("Is the speed of lightning's light greater than the speed of its thunder?", "Light"),
        # Add more questions as tuples (question, answer)
    ],
    "Math": [
        ("What is 2 + 2 * 0?", "2"),
        ("What is (5 x 6 *0 *1) / 0?", "Math Error"),
        ("What is 11^3 ?", "1221"),
        ("What is 12324354546 / 2?", "6162177273"),
        ("What is the value of x in 2x + 5 = 11?", "3"),
    ]
}

hints = {
    "Science": [
        "It's a compound made of hydrogen and oxygen.",
        "It contains a specific number of Carbon,Hydrogen,Oxygen atoms.",
        "This planet is the closest to the sun and has a fast orbit.",
        "It involves sunlight, water, and CO2 to produce glucose.",
        "One is visible, the other is audible, and they travel at different speeds.",
        # Pair each question with a corresponding hint.
    ],
    "Math": [
        "Multiplication comes before addition",
        "Any number multiplied by 0 is 0, but division by 0 is a problem",
        "Cube of 11",
        "Just divide the big number by 2",
        "Its algebra it is supposed to be easy",
    ],
    # Repeat for other categories as needed.
}

#---------------------------------------

def select_random_question(category):
    """
    Selects a random question from the specified category.

    Parameters:
    - category (str): The category from which to select a question.

    Returns:
    - tuple: A tuple containing the selected question (str) and its corresponding answer (str).
    """
    #------------------------
    if category in questions:
        return random.choice(questions[category])
    else:
        return None
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def check_answer(player_answer, correct_answer):
    """
    Checks if the player's answer matches the correct answer.

    Parameters:
    - player_answer (str): The answer provided by the player.
    - correct_answer (str): The correct answer to the question.

    Returns:
    - bool: True if the answers match, False otherwise.
    """
    #------------------------
    return player_answer.strip().upper() == correct_answer.strip().upper()
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def remove_question(category, question):
    """
    Removes a question from the list once it has been asked.

    Parameters:
    - category (str): The category from which to remove the question.
    - question (str): The question to be removed.

    Returns:
    - None
    """
    #------------------------
    if category in questions:
        i = 0
        while i < len(questions[category]):
            if questions[category][i][0] == question:
                del questions[category][i]
                break
            i += 1
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_question_and_accept_answer(question):
    """
    Displays a question to the player and accepts their answer via input.

    Parameters:
    - question (str): The question to be displayed.

    Returns:
    - str: The player's answer to the question.
    """
    #------------------------
    print(question)
    player_answer = input("Your answer: ")
    return player_answer.strip()
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def provide_hint(category, question):
    """
    Provides a hint for the given question based on its category.

    Parameters:
    - category (str): The category of the question.
    - question (str): The question for which to provide a hint.

    Returns:
    - str: The hint for the given question.
    """
    #------------------------
    if category in hints and category in questions:
        for i in range(len(questions[category])):
            if questions[category][i][0] == question:
                return hints[category][i]
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------

def display_correct_answer(correct_answer):
    """
    Displays the correct answer if the player's answer is incorrect.

    Parameters:
    - correct_answer (str): The correct answer to the question.

    Returns:
    - None
    """
    #------------------------
    print(f"The correct answer is: {correct_answer}")
    #------------------------
    raise NotImplementedError("This function is not implemented yet.")
    #------------------------

#---------------------------------------




