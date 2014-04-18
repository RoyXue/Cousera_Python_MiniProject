# template for "Stopwatch: The Game"
import simplegui
# define global variables
interval = 100
time = 0
status = 0 
#define watch status 0 for hold 1 for run
success = 0
attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    a = t / 1000
    b = (t %1000) / 100
    c = (t % 100) / 10
    d = t % 10
    return '%d:%d%d.%d' %(a, b, c, d)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global status
    status = 1
    
def stop():
    global status
    global success
    global attempts
    global time
    status = 0
    attempts += 1
    if time % 10 == 0:
        success += 1
    
def reset():
    global time
    global success
    global attempts
    time = 0
    success = 0
    attempts = 0
    
# define event handler for timer with 0.1 sec interval
def tick():
    global time
    global status
    if status == 1:
        time += 1
    else:
        pass

# define draw handler
def draw(canvas):
    global time
    global success
    global attempts    
    text = format(time)
    score = str(success) + '/' + str(attempts)
    canvas.draw_text(text, [70, 110], 40, 'Blue')
    canvas.draw_text(score,[175, 25], 20,'Red')
                            
# create frame
frame = simplegui.create_frame("Stop Watch", 200, 200)
timer = simplegui.create_timer(interval, tick)

# register event handlers
frame.add_button('Start', start, 50)
frame.add_button('Stop', stop, 50)
frame.add_button('Reset', reset, 50)
frame.set_draw_handler(draw)

# start frame
frame.start()
timer.start()
# Please remember to review the grading rubric
