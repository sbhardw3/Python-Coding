# Filename: RPS_game_modified.py
# Purpose: To design a game of rock, paper and scissors between user and computer
# Author: Shiven Bhardwaj
# Date: Nov. 24, 2020



import random


def is_valid(value_string):
    ''' Check if the user enters a valid input.
    return -- A string value that can be rock paper or scissors'''
    


    return (value_string == "rock") or (value_string == "paper") or (value_string == "scissors")





def read_user_choice():
    ''' Reading the validated value from the user. Which can be Rock Paper or Scissors'''

    valid = False # The input is false now


    
    # While the input is not valid the user has to again enter the input
    while (not valid):
        user_input = input("Choose Rock, Paper or Scissors: ")

        # Check if the input is valid or not
        valid = is_valid(user_input)
        
        # If the input is invalid then print a error statement 
        if (not valid):
            print("Error! You can only choose between Rock, Paper or Scissors")


            

    return user_input






def generate_computer_choice():
    ''' It generates the computer output i.e, computer can randomly choose between
    Rock, Paper or Scissors
    Return -- an integer value which in return is converted into a string value''' 

    # Generating random numbers 
    number_int =  random.randrange(3)

     
    # Giving each number a string value
    if number_int == 0:
        print("Computer: Rock")

    elif number_int == 1:
        print("Computer: Paper")

    else:
        print("Computer: Scissors")




    return number_int







def determine_winner(user_input, computer_output):
    ''' Printing the winner of the game played
    user_input -- A string value entered by the user
    computer_output -- an integer value which is converted into string'''

    
    # Cases for how the match can be tied
    if (user_input == "rock" and computer_output == 0) or \
    (user_input == "paper" and computer_output == 1) or \
    (user_input == "scissors" and computer_output == 2 ):
        
        result_of_game = "tied"
        print ("Match tied.")
        
        
    
    # Cases where the user losses the match 
    elif user_input == "rock" and computer_output == 1:

        result_of_game = "loss"
        print("You lose")
        

    elif user_input == "paper" and computer_output == 2:

        result_of_game = "loss"
        print("You lose")
        

    elif user_input == "scissors" and computer_output == 0:

        result_of_game = "loss"
        print("You lose")
        
    # The leftover cases where user wins the match
    else:

        result_of_game = "win"
        print("You win")


    return result_of_game
        




    

def update_stat(winner_update):
    ''' To print and increment the number of matches won, loss or tied
    winner_update -- a string value that tells if you loss or won or tie the match
    Return -- three values that are integers which are number of ties, wins and losses'''


    
    # The match has not started so, the wins, losses and ties are 0
    tie_int = 0
    win_int = 0
    loss_int = 0

    

    
    if (winner_update == "loss"):
        
        loss_int += 1
        print("Your win:", win_int,  "Your Loss:", loss_int, "Tie:", tie_int)

    elif (winner_update == "win"):
        
        win_int += 1
        print("Your win:", win_int, "Your Loss:", loss_int, "Tie:", tie_int)

    elif (winner_update == "tied"):

        tie_int += 1
        print("Your win:", win_int, "Your Loss:", loss_int, "Tie:", tie_int)


    return tie_int, win_int, loss_int

    


    

    
# Main program
# Input(from the user): Choice of ther user: Rock , Paper or Scissors
# Output(on the screen): Choice of the computer, Winner and the number of wins, losses and ties
# Assumption: The user enters a valid input i.e, Rock, Paper or Scissors



def main():

    print(" If you choose 1: player vs player")
    print(" If you choose 2: player vs computer") 
    print(" If you choose 3: computer vs player")
    print(" If you choose 4: computer vs computer")

    print()
    print()
          


    continue_str = "Yes"

    while (continue_str == "Yes"):
        
        # Asking the user to enter a number between 1 to 4 which means
        # 1 is player vs player
        # 2 is player vs computer
        # 3 is computer vs player
        # 4 is computer vs computer

        
        # Assumption that the player will enter a number between
        choice_int = int(input("Enter a number between 1 to 4: "))

        # Updating the winner and stats according to the number entered by the user
        if (choice_int == 1):
            read_input1 = read_user_choice()

            read_input2 = read_user_choice()

            winner_update = determine_winner(read_input1, read_input2)

            update_stat(winner_update)

        elif (choice_int == 2):
            read_input = read_user_choice()

            computer_output = generate_computer_choice()
        
            winner_update = determine_winner(read_input, computer_output)

            update_stat(winner_update)

        elif (choice_int == 3):
            computer_output = generate_computer_choice()
        
            read_input = read_user_choice()
        
            winner_update = determine_winner(read_input, computer_output)

            update_stat(winner_update)

        elif (choice_int == 4):
            computer_output = generate_computer_choice()
        
            computer_output = generate_computer_choice()
        
            print("Computer wins")
        else:
            print("Error! Enter a valid choice")


        # Ask the user to play again
        # Assuming that player will anwer in Yes and No
        continue_str = input("Do you want to play again? Type Yes or No: ")

    print("Game Over")

    
    
                     




#Calling out main function


main()




