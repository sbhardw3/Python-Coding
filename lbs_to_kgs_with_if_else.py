#********************************************************************
# Filename: lbs_to_kgs.py
# Purpose: Convert a weight in pounds to a weight in kilograms.
# Author: David Chays
# Date: September 3, 2019
#********************************************************************

#----------------------------------------------------------------------------------
# Input (from the user): weight in pounds.
# Output (to the screen): weight in kilograms.
# Assumptions:
# 1) 2.2 lbs = 1 kg
# 2) The user will enter valid input, i.e. a non-negative number of pounds.
#----------------------------------------------------------------------------------

# main program:

# Define constant
LBS_PER_KG = 2.2

# Read the weight in pounds from the user.
lbs_str = input("Enter a weight in pounds: ")

# Convert the string to a floating point number.
lbs_float = float(lbs_str)

# Check if lbs_float is valid.
if (lbs_float >= 0.0):
    # Calculate the weight in kilograms.
    kgs_float = lbs_float / LBS_PER_KG

    # Print the weight in pounds and kilograms.
    print("The given weight in pounds is ", lbs_float)
    print("The equivalent weight in kilograms is ", kgs_float)
else:
    print("Error: ", lbs_float, " is invalid.")

# Alternative way to print the error message:    
# print("Error: %f is invalid." % lbs_float)

# End of main program.
