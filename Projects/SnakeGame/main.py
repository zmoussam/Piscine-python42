#import modules necessary for the game
import random
import curses

# Initialize the curses library to create our screen
screen = curses.initscr()

# Hide the mouse cursor
curses.curs_set(0)

# Getmax screen height and width
screen_height, screen_width = screen.getmaxyx()

# Create a new window
window = curses.newwin(screen_height, screen_width, 0, 0)

# Allow window to receive input from the keyboard
window.keypad(1)

# Set the delay for updating the screen
window.timeout(30)

# Set the x,y coordinates of the initial position of snake's head
__snkX = screen_width // 4
__snkY = screen_height // 2 

# define the initial position of the snake body
__snake = [
    [__snkY, __snkX],
    [__snkY, __snkX - 1],
    [__snkY, __snkX - 2]
]

# Create the food in the middle of window
food = [screen_height // 2, screen_width // 2]

window.addch(food[0], food[1], curses.ACS_BLOCK)
 
 # Set initial movement direction to right
key = curses.KEY_RIGHT

 # Create game loop that loops forever until player loses or quits the game

while True:
    #get the next key that will be pressed by user
    next_key = window.getch()
    #If user doesn't input anything, key remains same, else key will be set to the new pressed key
    key = key if next_key == -1 else next_key
    # Check if snake collided with the walls or itself
    if __snake[0][0] in [0, screen_height] or __snake[0][1] in [0, screen_width] or __snake[0] in __snake[1:]:
        curses.endwin()
        quit()
# Set the new poisition of the snake head based on te direction 
    new_head = [__snake[0][0], __snake[0][1]]
    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1 
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    __snake.insert(0, new_head)
# Check if snake ate the food     
    if __snake[0] == food:
        food = None # Remove food if snake ate it
        while food is None:
            new_food = [
                random.randint(1, screen_height - 1),
                random.randint(1, screen_width - 1)
            ]
            food = new_food if new_food not in __snake else None
        window.addch(food[0], food[1], curses.ACS_BLOCK)
    else:
        # Otherwise remove the last segment of snake body
        tail = __snake.pop()
        window.addch(tail[0], tail[1], ' ')
    window.addch(__snake[0][0], __snake[0][1], curses.ACS_CKBOARD)



