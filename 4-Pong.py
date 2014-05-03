# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True

# initialize ball_pos and ball_vel for new bal in middle of table
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [-3, -3]
paddle1_vel = 0
paddle2_vel = 0
paddle1_pos = 200
paddle2_pos = 200
score1 = 0
score2 = 0
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel# these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    
    if direction == 'Left':
        ball_vel = [-3, -3]
    else:
        ball_vel = [3, -3]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    spawn_ball('Right')
    score1 = 0
    score2 = 0
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    if ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] in range(paddle1_pos-PAD_HEIGHT, paddle1_pos):
            ball_vel[0] = -ball_vel[0]
        else:
            score2 += 1
            spawn_ball("Right")
    elif ball_pos[0] >= (WIDTH-BALL_RADIUS-PAD_WIDTH):
        if ball_pos[1] in range(paddle2_pos-PAD_HEIGHT, paddle2_pos):
            ball_vel[0] = - ball_vel[0]
        else:
            score1 += 1
            spawn_ball("Left")
            
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= (HEIGHT-BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    else:
        ball_vel[0] =  ball_vel[0]
        ball_vel[1] =  ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos ,BALL_RADIUS,2 ,  "White", "Red" )
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos > PAD_HEIGHT and paddle1_pos < HEIGHT:
        paddle1_pos += paddle1_vel
    elif paddle1_pos <= PAD_HEIGHT:
        paddle1_pos = paddle1_pos+1
    elif paddle1_pos >= HEIGHT:
        paddle1_pos = paddle1_pos-1
    else:
        pass
    
    if paddle2_pos > PAD_HEIGHT and paddle2_pos < HEIGHT:
        paddle2_pos += paddle2_vel
    elif paddle2_pos <= PAD_HEIGHT:
        paddle2_pos = paddle2_pos+1
    elif paddle2_pos >= HEIGHT:
        paddle2_pos = paddle2_pos-1
    else:
        pass
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos],  [0, paddle1_pos- PAD_HEIGHT],[PAD_WIDTH, paddle1_pos- PAD_HEIGHT],[PAD_WIDTH, paddle1_pos]], 1, 'White', 'Blue')
    #canvas.draw_polygon(point_list, line_width, line_color, fill_color = color)
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos],  [WIDTH - PAD_WIDTH, paddle2_pos- PAD_HEIGHT],[WIDTH, paddle2_pos- PAD_HEIGHT],[WIDTH, paddle2_pos]], 1, 'White', 'Purple')
    # draw scores
    canvas.draw_text(str(score1), (130, 100), 50, 'White')
    canvas.draw_text(str(score2), (450, 100), 50, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 4
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = -4
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 4
    elif key == simplegui.KEY_MAP['up']:
        paddle2_vel = -4
    else:
        pass
    
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel = 0
    paddle2_vel = 0
    
def restart():
    new_game()


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
button = frame.add_button('Restart', restart, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)


# start frame
new_game()
frame.start()
