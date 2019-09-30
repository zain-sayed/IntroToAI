"""
 @author:zain
"""
#from openList import *
from astar import *
import random
import pygame
import time

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

grid = []
grid_height = 101
    #int(input("Input a grid height: "))
grid_width = 101
    #int(input("Input a grid width:  "))

for row in range(grid_height):
    grid.append([])
    for column in range(grid_width):
        coinFlip = random.randint(0, 100)
        if(coinFlip>24):
            grid[row].append(0)
        else:
            grid[row].append(1)

rand_start_x = random.randint(0,100)
rand_start_y = random.randint(0,100)
rand_goal_x = random.randint(0,100)
rand_goal_y = random.randint(0,100)

print(rand_start_x,  rand_start_y)
print(rand_goal_x,rand_goal_y)

grid[rand_start_x][rand_start_y] = 2
grid[rand_goal_x][rand_goal_y] = 3

startCord = (rand_start_x,rand_start_y)
goalCord =  (rand_goal_x,rand_goal_y)

startNode = Treenode(0,None,startCord)


        #The zero/one here is appending a cell



pygame.init()

# Set the width and height of the screen [width, height]
size = (505, 505)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("A* Grid")


done = False
clock = pygame.time.Clock()


# insert starting node into openlist
insert(startNode)


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0]
            row = pos[1]
            print(pos)
            done = True


    screen.fill(BLACK)

    for row in range(grid_height):
        for column in range(grid_width):

            if (grid[row][column] == 0):
                color = WHITE
            elif (grid[row][column] == 2):
                color = GREEN
                #Starting point is GREEN
            elif (grid[row][column] == 3):
                color = RED
                #Goal is RED

            elif (grid[row][column] == 4):
                color = LBLUE
                #Path is LIGHT BLUE
            else:
                color = BLACK

            pygame.draw.rect(screen,color,[BLOCK_WIDTH*column,BLOCK_HEIGHT*row,BLOCK_WIDTH,BLOCK_HEIGHT])


    # A* algorithm will go here
    goalState = False
    if (len(openlist) != 0) and (goalState is False):
        repeatedForwardAstar()
    #elif goalState is True:
        # backtrack

    elif len(openlist) == 0:
        print("Cannot find goal, path is blocked!")
        time.sleep(60)
        done = True


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.


    # --- Drawing code should go here

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(30)

# Close the window and quit.
pygame.quit()