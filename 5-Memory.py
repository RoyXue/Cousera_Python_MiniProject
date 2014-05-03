# implementation of card game - Memory

import simplegui
import random

a = []
b = []
exposed = []
state = 0
turns = 0

# helper function to initialize globals
def new_game():
     global a, b, exposed, turns
     exposed = [False]*16
     a = range(0, 8)
     b = range(0, 8)
     a.extend(b)
     random.shuffle(a)
     state = 0

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, exposed, turns, c, d
    i = pos[0] / 50
    if exposed[i] == True:
        pass
    else:
        if state == 0:
            exposed[i] = True
            c = i
            state = 1
        elif state == 1:
            exposed[i] = True
            if a[i] == a[c]:
                state = 0
            else:
                d = i
                state = 2
        else:
            exposed[c] = False
            exposed[d] = False
            exposed[i] = True
            c = i
            state = 1
            turns += 1
            turn = "Turns = " + str(turns)
            label.set_text(turn)
        
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    for i in range(0, 16):
        if exposed[i]:
            canvas.draw_text(str(a[i]), [50*i+20, 60], 30, 'white')
        else:
            canvas.draw_polygon([[50*i, 0], [50*i, 100], [50*(i+1), 100], [50*(i+1), 0]], 2, 'White', 'Purple')


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric
