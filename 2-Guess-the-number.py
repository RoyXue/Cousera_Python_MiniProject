# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

# initialize global variables used in your code

aim = 0
time = 0
status = 0

# helper function to start and restart the game
def new_game():
    global status
    global time
    global aim
    print    
    print 'New Game Start!' 
    if status == 0:
        time = 7
        aim = random.randrange(0, 101)
        print 'Range is from 0 to 100'
        print 'Remaining guesses is', time
    else:
        time = 10
        aim = random.randrange(0, 1001)
        print 'Range is from 0 to 1000'
        print 'Remaining guesses is', time


# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts     
    global status
    status = 0
    new_game()
    
def range1000():
    # button that changes range to range [0,1000) and restarts 
    global status 
    status = 1
    new_game()
    
def input_guess(guess):
    # main game logic goes here
    global aim
    global time
    comp = int(guess)
    print
    print "Guess number is", comp
    time -= 1
    if time == 0:
        print "You have run out of guesses"
        new_game()
    else:
        print "Remaining guesses is", time
        if (comp > aim):
            print "Lower!"   
        elif (comp < aim):
            print "Higher!"
        else:
            print "Correct!"
            new_game()
    
    
    
    
       
    
# create frame
frame = simplegui.create_frame("Guess the number!", 200, 200)


# register event handlers for control elements
frame.add_button('range100', range100, 200)
frame.add_button('range1000', range1000, 200)
frame.add_input('Input num', input_guess, 200)


# call new_game and start frame
frame.start()
new_game()


# always remember to check your completed program against the grading rubric
