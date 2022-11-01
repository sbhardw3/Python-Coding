# Filename: guess_the_word.py
# Purpose: User guessing a word by entering aplahbets 
# Author: Shiven Bhardwaj
# Date: Nov. 20, 2020
# Version 2 resolves the defect in the previous version.


import random

def pick_random_word(word_list):
    ''' Randomly picking number from word_list
    Parameter:
    word_list -- a string list
    Returns: a random number from the word_list using the predefined function'''

    return random.choice(word_list)
    


    
def update_known_letters(target_str, known_letters, letter_guessed):
    '''Compute and return an update of known_letters based on the target_str and letter_guessed.
    Parameters:
    target_str -- a String, the word we are trying to guess. 
    known_letters -- a String, what we know about the target, containing letters of the target
                     (that we correctly guessed previously) and underscores in positions where the letter is unknown.
    letter_guessed -- a String, the current letter guessed.
    Return a String -- an updated version of known_letters, containing the letter_guessed if it is in the target_str.
    '''
    
    # Initialize the result to the empty String.
    result_str = ""
    
    # for each index i between 0 and the last index of the target String...
    for i in range(0, len(target_str)):

        # If there is already a letter at index i of known_letters (due to an earlier guess being correct),
        # keep it in the same position of the result.
        if (known_letters[i].isalpha()):
            result_str += known_letters[i]
            
        # Otherwise, if the letter guessed matches the letter of the target String at the corresponding index,
        # then the guess was correct so append it to the result.
        elif (letter_guessed == target_str[i]):
            # known_letters[index] = target_str[index] is not allowed -- Strings are immutable!
            result_str += target_str[i]
            
        # Otherwise, there was no match between letter_guessed and target_str[index]
        # so append an underscore to the result, indicating that the letter at index i is still unknown.
        else:
            result_str += '_'

    return result_str

def display_known_letters(known_letters):
    ''' Print each character of known_letters separated by a space.
    Parameter:
    known_letters -- a String, containing the letters correctly guessed and/or underscores for unknown letters.
    '''
    for each_char in known_letters:
        print(each_char, end = ' ')

    print() # Go to next line.

# Main function.
# Input (from the user): The aplhabet entered by the user
# Output (to the screen): If the aplhabet entered is correct or not  
# Assumptions: Case will be used consistently (lower). The target_str has no spaces nor special characters. 

def main():

    word_list = ["computer", "science", "intelligence", "software"]

    target_str = pick_random_word(word_list)
    
    known_letters = "_" * len(target_str) # Initially, we don't know any of the letters in the target String.

    turns = 10


    letter_guessed = "e"

    known_letters = update_known_letters(target_str, known_letters, letter_guessed)

    display_known_letters(known_letters)

  


    for i in range(0,turns):

        letter_guessed = input("Enter an alphabet: ")

        known_letters = update_known_letters(target_str, known_letters, letter_guessed)

        final_letters = display_known_letters(known_letters)

        turns -= 1
        

        print("Number of chances left: ", turns)

        if (known_letters == target_str):
            print("You guessed the word correctly " + known_letters)
            break
        

        if turns == 0:
             print("You are out of chances")
             print("The word was: ", target_str)

        if letter_guessed.upper():
            print("Error! The input contains letters in lower case")


        
        
           

# Call/invoke the main function.
main()

