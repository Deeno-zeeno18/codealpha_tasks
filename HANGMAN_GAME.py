"""
CREATING A GUESSING GAME THAT ALLOWS THE USER TO GUESS A WORD
"""
import random

#1. Creating the list of predefined words
def create_the_word_list():
    the_words_are = ["Joy", "Acrimony", "Playing", "War", "Subtle"]
    return the_words_are

#2. Sending them to lowercase
def make_the_words_lowercase():
    your_words_are = []
    for a_word in create_the_word_list():
        your_words_are.append(a_word.lower())
    return your_words_are

#3. Picking a random
def select_the_word():
    your_word_is = random.choice(make_the_words_lowercase())
    return your_word_is

#4.Storing the letters in a string list
def make_it_a_string():
    word_in_parts = []
    your_word_is = select_the_word()
    main_word = your_word_is.strip()
    for letter in main_word:
        word_in_parts.append(letter)
    return word_in_parts


#5. Logic for guessing the word
def guess_the_word(word_in_parts):
    no_chances = 6
    correct_word = []
    incorrect_words = []
    limit_to_guesses = 0
    guessed_so_far = ["_"] * len(word_in_parts)
    x = 0
    while x < len(word_in_parts):
        print("Word:", " ".join(guessed_so_far))
        print(f"Chances left: {no_chances - limit_to_guesses}")

        the_letter = (input("Make the guess:")).strip().lower()
        if the_letter == word_in_parts[x]:
            guessed_so_far[x] = the_letter
            correct_word.append(the_letter)
            x += 1
        else:
            print("WRONG LETTER")
            incorrect_words.append(the_letter)
            limit_to_guesses += 1
            if limit_to_guesses == no_chances:
                print("OUT OF GUESSES")
                break


    if x == len(word_in_parts):
        print("YOU WIN! The word was:", "".join(word_in_parts))



    return guessed_so_far

print(guess_the_word(make_it_a_string()))






