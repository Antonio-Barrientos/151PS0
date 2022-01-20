#====================================================
# Filename: Karel_Painting.py
# 
# Your name:Antonio Barrientos
# Who did you work with (if anyone)?: N/A
# Estimate for time spent (in hrs)?: 1 hr?
#====================================================

# I've just laid out a basic starting function below, but remember that you
# absolutely should define more helping functions to decompose the problem
# into smaller pieces! Here I'm leaving those pieces (and helper functions)
# up to you to design and name as you see fit

import karel

def main():
    """ Function to cause Karel to paint 3 sides of its house and then go indoors. """
    # You can add your code below
    turn_around()
    paint_one_side()
    turn_left()
    move()
    paint_one_side()
    turn_left()
    move()
    paint_one_side()
    go_inside()
    
    

def paint_one_side():
    while left_is_blocked():
        if left_is_blocked():
            put_beeper()
        move()
        


def go_inside():
    """ Tells Karel to head indoors"""
    turn_left()
    move()
    move()
    turn_left()
    move()


def turn_right():
    """ Helping function to turn Karel 90 degrees to the right"""
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    """ Helping function to turn Karel 180 degrees"""
    turn_left()
    turn_left()

