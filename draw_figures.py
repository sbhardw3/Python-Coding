# Filename: draw_figures_w_functions_v2.py
# Purpose: Define our own functions that are called/invoked by the main program.
# Author: D. Chays
# Date: Sept. 17, 2020
# Version: 3

# Define functions that draw primitive shapes.

def draw_cone():
    ''' Draw a cone. '''
    print ("  /\\ ")
    print (" /  \\")

def draw_v():
    ''' Draw a V. '''
    print (" \\  /")
    print ("  \\/ ")

def draw_box():
    ''' Draw a box. '''
    print ("+----+")
    print ("|    |")
    print ("|    |")
    print ("+----+")  

# Define functions that draw pictures, using the primitive shapes.

def draw_house():
    ''' Draw a House. '''
    draw_cone()
    draw_box()
    
def draw_diamond():
    ''' Draw a diamond. '''
    draw_cone()
    draw_v()

def draw_x():
    ''' Draw an X. '''
    draw_v()
    draw_cone()

def draw_rocket(label_str, country_str):
    ''' Draw a rocket with a label.
    Parameter:
    label -- a String representing a label to print below the rocket.
    '''
    draw_cone()
    draw_box()
    print (  " |"  + country_str +  "|")
    draw_box()
    draw_cone()
    print(label_str)

# main program:

# Draw a House.
draw_house()
print()

# Draw a diamond.
draw_diamond()
print()

# Draw an X.
draw_x()
print()

# Draw a rocket.
draw_rocket("This is our first rocket.\n", "US")
draw_rocket("This is our second rocket.\n", "RU")
print()

# end of main
