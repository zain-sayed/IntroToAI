"""
 @author:zain
"""
import random
import pygame
import time
from astar import *
from openList import *
from gridFunc import *

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
LBLUE = (3, 232, 252)

#setting height and width of cells
BLOCK_WIDTH = 5
BLOCK_HEIGHT = 5
#Setting margin
MARGIN = 0

# start coords
rand_start_x = random.randint(0, 100)
rand_start_y = random.randint(0, 100)
startCoord = (rand_start_x, rand_start_y)

# goal coords
rand_goal_x = random.randint(0, 100)
rand_goal_y = random.randint(0, 100)
goalCoord = (rand_goal_x, rand_goal_y)

# initialize grid
random.seed(1)
grid = gridInit(startCoord, goalCoord)
random.seed(1)
grid2 = gridInit(startCoord, goalCoord)
random.seed(1)
grid3 = gridInit(startCoord, goalCoord)

        #The zero/one here is appending a cell

# initialize the game (grid)
pygame.init()

# call the forward Astar algorithm
repeatedForwardAstar(pygame, grid, startCoord, goalCoord, time)

# call the backward Astar algorithm
repeatedBackwardAstar(pygame, grid2, goalCoord, startCoord, time)

# call the adaptive astar algorithm
#adaptive_repeatedForwardAstar(pygame, grid3, startCoord, goalCoord, time)

# Close the window and quit.
pygame.quit()

