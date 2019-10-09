from openList import *
from gridFunc import *
from time import perf_counter

# global color, black
BLACK = (0, 0, 0)

# finds h value of a node
def findh(x, y, goalX, goalY):
    hx = abs(goalX - x)
    hy = abs(goalY - y)
    return hx + hy


# finds f value of a node
def findf(x, y, g, goalX, goalY):
    return g + findh(x, y, goalX, goalY)


# compare f values on openlist conflict
def comparef(x, y, node, openlist):
    for i in openlist:
        if i.coordinates == (x, y):
            # if node is less than, update it
            if node.f < i.f:
                i.f = node.f
                i.parent = node.parent
                i.g = node.g
                siftup(openlist)


def mainEventLoop(pygame):
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


# function checks the 4 directions on the grid and inserts if needed
def check_nodes(grid, openlist, closedlist, currentNode, x, y, goalX, goalY):
    # up node, check bounds of x-1 and then if unblocked=0, blocked=1
    if (x - 1) > -1:
        # create the node
        upNode = Treenode(findf(x - 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1,
                          findh(x - 1, y, goalX, goalY), currentNode, (x - 1, y))

        if grid[x - 1][y] == 0:
            # add to open list if not in closed list OR openlist already
            inclosed = False
            inopen = False
            for element in closedlist:
                if element.coordinates == (x - 1, y):
                    inclosed = True
                    break
            if inclosed is False:
                for e in openlist:
                    if e.coordinates == (x - 1, y):
                        inopen = True
                        break
            if inclosed is False:
                if inopen is False:
                   openlist = insert(upNode, openlist)
                # compare f values and resiftup()
                else:
                    comparef(x - 1, y, upNode)
        # goal node
        elif grid[x - 1][y] == 3:
           openlist = insert(upNode, openlist)

    # down node, check bounds of x+1 and then if unblocked=0, blocked=1
    if (x + 1) < 101:
        # create the node
        downNode = Treenode(findf(x + 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1,
                            findh(x + 1, y, goalX, goalY), currentNode, (x + 1, y))

        if grid[x + 1][y] == 0:
            # add to open list if not in closed list OR openlist already
            inclosed = False
            inopen = False
            for element in closedlist:
                if element.coordinates == (x + 1, y):
                    inclosed = True
                    break
            if inclosed is False:
                for e in openlist:
                    if e.coordinates == (x + 1, y):
                        inopen = True
                        break
            if inclosed is False:
                if inopen is False:
                    openlist = insert(downNode, openlist)
                # compare f values and resiftup()
                else:
                    comparef(x + 1, y, downNode)
        elif grid[x + 1][y] == 3:
            openlist = insert(downNode, openlist)

    # right node, check bounds of y+1 and then if unblocked=0, blocked=1
    if (y + 1) < 101:
        # create the node
        rightNode = Treenode(findf(x, y + 1, currentNode.g + 1, goalX, goalY), currentNode.g + 1,
                             findh(x, y + 1, goalX, goalY), currentNode, (x, y + 1))

        if grid[x][y + 1] == 0:
            # add to open list if not in closed list OR openlist already
            inclosed = False
            inopen = False
            for element in closedlist:
                if element.coordinates == (x, y + 1):
                    inclosed = True
                    break
            if inclosed is False:
                for e in openlist:
                    if e.coordinates == (x, y + 1):
                        inopen = True
                        break
            if inclosed is False:
                if inopen is False:
                    openlist = insert(rightNode, openlist)
                # compare f values and resiftup()
                else:
                    comparef(x, y + 1, rightNode)
        elif grid[x][y + 1] == 3:
            openlist = insert(rightNode, openlist)

    # left node, check bounds of y-1 and then if unblocked=0, blocked=1
    if (y - 1) > -1:
        # creates the node
        leftNode = Treenode(findf(x, y - 1, currentNode.g + 1, goalX, goalY), currentNode.g + 1,
                            findh(x, y - 1, goalX, goalY), currentNode, (x, y - 1))

        if grid[x][y - 1] == 0:
            # add to open list if not in closed list OR openlist already
            inclosed = False
            inopen = False
            for element in closedlist:
                if element.coordinates == (x, y - 1):
                    inclosed = True
                    break
            if inclosed is False:
                for e in openlist:
                    if e.coordinates == (x, y - 1):
                        inopen = True
                        break
            if inclosed is False:
                if inopen is False:
                    openlist = insert(leftNode, openlist)
                # compare f values and resiftup()
                else:
                    comparef(x, y - 1, leftNode)
        elif grid[x][y - 1] == 3:
            openlist = insert(leftNode, openlist)
    return openlist


# This will compute the current path by running Astar on the known world and will return
# the list of coordinates (from the goal state) for the repeated-forward algorithm to follow
#
# The goalCoord remains constant, but the startCoord must begin from the last blocked node from the
# previous call, which's coordinates will be passed in to this new call of astar as the startCoord
def astar(pygame, grid, startCoord, goalCoord, time):
    # create the openlist and the closedlists
    openlist = []
    closedlist = []

    # Set the width and height of the screen [width, height], clock and display grid (and counter for time elapsed)
    size = (505, 505)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("A* Grid")
    clock = pygame.time.Clock()
    a = perf_counter()

    # total time and shortest path
    shortest_path = 0
    total_time = 0

    # separate the goal coords for manipulation
    startX, startY = startCoord
    goalX, goalY = goalCoord
    print("start X is: " + str(startX) + "," + "start Y is : " + str(startY) + '\n')
    print("goal X is: " + str(goalX) + "," + "goal Y is : " + str(goalY) + '\n')

    # Initialize start node and if we find the goal state
    startNode = Treenode(0, 0, 0, None, startCoord)
    goalfound = False

    # insert starting node into openlist
    openlist = insert(startNode, openlist)

    # loop through the open list
    while (len(openlist) != 0) and (goalfound is False):
        # helps display the loop, fill initial screen black and update grid colors
        mainEventLoop(pygame)
        screen.fill(BLACK)
        gridColor(screen, grid)

        # assigns current node to the removed node and openlist to the modified openlist
        currentNode, openlist = pop(openlist)

        # get current x and y coords
        x, y = currentNode.coordinates
        if grid[x][y] == 3:
            print("FOUND GOAL")

        # now check the 4 different directions and add to open list if needed (update if there, skip if blocked)
        openlist = check_nodes(grid, openlist, closedlist, currentNode, x, y, goalX, goalY)

        # add current node to closed list and change color
        closedlist.append(currentNode)
        if grid[x][y] == 2:
            count = count + 1
            grid[x][y] = 2
        else:
            count = count + 1
            grid[x][y] = 4
        # if we hit the goal
        if (x == goalX) and (y == goalY):
            goalfound = True
            print('\n' + "Found GOAL" + '\n')
        # --- Limit to 60 frames per second
        clock.tick(120)

        # if openlist is 0, then we cannot find the goal and have exhausted all our options
        if len(openlist) == 0:
            print("Cannot find goal, path is blocked!")
            time.sleep(60)
        # else, we found the goal and we need to backtrack and return the list of coords
        elif goalfound is True:
            path_of_coordinates = []
            ptr = closedlist[-1]
            currX, currY = ptr.coordinates

            ###### backtrack begins here #########
            while ptr.coordinates != startCoord:

                # Screen things first: helps display the loop, make the node at ptr pink
                mainEventLoop(pygame)
                grid[currX][currY] = 9
                BLACK = (0, 0, 0)
                screen.fill(BLACK)
                # then, update grid colors and --- Limit to 60 frames per second
                gridColor(screen, grid)
                clock.tick(120)

                # now append the coords of the current node to the path_of_coordinates list
                path_of_coordinates.append(ptr.coordinates)

                # increment ptr
                ptr = ptr.parent
                currX, currY = ptr.coordinates
                shortest_path += 1

            # make the last point PINK (do all the grid/screen operations 1 last time)
            grid[startX][startY] = 9
            mainEventLoop(pygame)
            BLACK = (0, 0, 0)
            screen.fill(BLACK)
            gridColor(screen, grid)
            print('Path Found' + '\n')

            # this keeps track of the total time elapsed
            b = perf_counter()
            total_time = b - a
            print("The Total Time Elapsed is: " + total_time)

    # now keep remaining screen up for 60 seconds
    time.sleep(15)
    pygame.display.quit()
    print("shortest path is (forward): " + str(shortest_path))
    return path_of_coordinates.reverse()


# repeated forward A* algorithm
def repeatedForwardAstar(pygame, grid, startCoord, goalCoord, time):

    # forward_grid

    # astar_grid

    '''
    plan:

    so we want to run astar be the
    '''







    pass






