#Contains all global variables in the code
import random

# global openlist
openlist = []

# closedlist and globals for currx and curry (printing purposes)
closedlist = []
currentX = 0
currentY = 0

# grid
grid = []

# start coords
rand_start_x = random.randint(0,100)
rand_start_y = random.randint(0,100)

# goal coords
rand_goal_x = random.randint(0,100)
rand_goal_y = random.randint(0,100)
goalCord = (100, 100)
goalState = False
