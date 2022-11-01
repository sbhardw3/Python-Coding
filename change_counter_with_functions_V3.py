# Filename: change_counter_with_functions_V3.py
# Purpose: Compute the total value of a collection of coins (quarters, dimes, nickels, pennies).
# Author: D. Chays
# Date: Sept. 29, 2020
# Version: 3 ( refactor: read_coins(coin_type_str) replaces read_quarters(),
# read_dimes(), read_nickels(), read_pennies())

def read_coins(coin_type_str):
    ''' Read the number of the given coin type from the user.
    Parameters:
    coin_type_str -- a string containing one of the following values: "quarters", "dimes", "nickels", "pennies"
    Return an integer -- the number of the given coin type.
    '''
    coins_str = input("Enter a number of " + coin_type_str + " (an integer >= 0): ")
    coins_int = int(coins_str)
    return coins_int

def read_num_of_coins():
    ''' Read the number of quarters, dimes, nickels and pennies from the user.
    Return 4 integers -- the number of quarters, dimes, nickels and pennies.
    '''
    return read_coins("quarters"), read_coins("dimes"), read_coins("nickels"), read_coins("pennies")

def compute_num_of_cents(q_int, d_int, n_int, p_int):
    ''' Compute and return the total number of cents equivalent to the given numbers of coins.
    Parameters:
    q_int -- an integer at least 0, the number of quarters
    d_int -- an integer at least 0, the number of dimes
    n_int -- an integer at least 0, the number of nickels
    p_int -- an integer at least 0, the number of pennies
    Return an integer -- the total number of cents equivalent to the given coins.
    '''
    
    # Define constants.
    VALUE_OF_QUARTER = 25;
    VALUE_OF_DIME = 10;
    VALUE_OF_NICKEL = 5;
    
    return q_int * VALUE_OF_QUARTER + \
           d_int * VALUE_OF_DIME + \
           n_int * VALUE_OF_NICKEL + p_int

#----------------------------------------------------------------------------------------------------------
# Main part of the program
# Input (from the user): number of coins (quarters, dimes, nickels and pennies).
# Output (to the screen): total value of the coins in dollars and cents.
# Assumptions: The user will enter valid input, i.e. integers that are at least 0 for the numbers of coins.
#----------------------------------------------------------------------------------------------------------

# Define constant.
CENTS_PER_DOLLAR = 100;

# Read the number of coins from the user.
num_quarters_int, num_dimes_int, num_nickels_int, num_pennies_int = read_num_of_coins()
    
# Echo the inputs.
print ("You entered %d quarters, %d dimes, %d nickels and %d pennies." % \
       (num_quarters_int, num_dimes_int, num_nickels_int, num_pennies_int))

# Calculate the total value of the coins.
total_cents_int = compute_num_of_cents(num_quarters_int, num_dimes_int, num_nickels_int, num_pennies_int)

total_value_float = float(total_cents_int) / CENTS_PER_DOLLAR

# Print the total value of the coins.
print ("Total value: $%0.2f" % total_value_float)

# End of main.
