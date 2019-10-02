from openList import *
from gridFunc import *

# finds g value of a node
'''def findg(x, y):
    gx = abs(globalvars.rand_start_x - x)
    gy = abs(globalvars.rand_start_y - y)
    return gx + gy
'''

# finds h value of a node
def findh(x, y, goalX, goalY):
    hx = abs(goalX - x)
    hy = abs(goalY - y)
    return hx + hy


# finds f value of a node
def findf(x, y, g, goalX, goalY):
    return g + findh(x, y, goalX, goalY)


# compare f values on openlist conflict
def comparef(x, y, node):
    for i in globalvars.openlist:
        if i.coordinates == (x, y):
            # if node is less than, update it
            if node.f < i.f:
                i.f = node.f
                i.parent = node.parent
                i.g = node.g
                siftup()


# repeated forward A* algorithm
def repeatedForwardAstar(pygame, grid, startCoord, goalCoord, time):

    # Set the width and height of the screen [width, height], clock and display grid
    size = (505, 505)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("A* Grid")
    clock = pygame.time.Clock()

    # separate the goal coords for manipulation
    startX, startY = startCoord
    print(str(startX) + "," + str(startY) + '\n')
    goalX, goalY = goalCoord

    # Initialize start node
    startNode = Treenode(0, 0, 0, None, startCoord)

    # insert starting node into openlist
    insert(startNode)

    # if we find the goal state
    goalfound = False

    # if the screen has not been clicked
    done = False

    # while the open list is not empty and the goal state is not found
    while (len(globalvars.openlist) != 0) and (goalfound is False) and (done is False):

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

        # fill initial screen black
        BLACK = (0, 0, 0)
        screen.fill(BLACK)

        # then, update grid colors
        gridColor(screen, grid)

        # pop from open list to expand first node
        currentNode = pop()

        # get current x and y coords
        x, y = currentNode.coordinates
        if grid[x][y] == 3:
            print("FOUND GOAL")

        # up node, check bounds of x-1 and then if unblocked=0, blocked=1
        if (x - 1) > -1:
            # create the node
            upNode = Treenode(findf(x - 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x - 1, y, goalX, goalY), currentNode, (x - 1, y))

            if grid[x - 1][y] == 0:
                # add to open list if not in closed list OR openlist already
                inclosed = False
                inopen = False
                for element in globalvars.closedlist:
                    if element.coordinates == (x - 1, y):
                        inclosed = True
                        break
                if inclosed is False:
                    for e in globalvars.openlist:
                        if e.coordinates == (x - 1, y):
                            inopen = True
                            break
                if inclosed is False:
                    if inopen is False:
                        insert(upNode)
                    # compare f values and resiftup()
                    else:
                       comparef(x - 1, y, upNode)
            elif grid[x - 1][y] == 3:
                insert(upNode)

        # down node, check bounds of x+1 and then if unblocked=0, blocked=1
        if (x + 1) < 101:
            # create the node
            downNode = Treenode(findf(x + 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x + 1, y, goalX, goalY), currentNode, (x + 1, y))

            if grid[x + 1][y] == 0:
                # add to open list if not in closed list OR openlist already
                inclosed = False
                inopen = False
                for element in globalvars.closedlist:
                    if element.coordinates == (x + 1, y):
                        inclosed = True
                        break
                if inclosed is False:
                    for e in globalvars.openlist:
                        if e.coordinates == (x + 1, y):
                            inopen = True
                            break
                if inclosed is False:
                    if inopen is False:
                        insert(downNode)
                    # compare f values and resiftup()
                    else:
                        comparef(x + 1, y, downNode)
            elif grid[x + 1][y] == 3:
                insert(downNode)

        # right node, check bounds of y+1 and then if unblocked=0, blocked=1
        if (y + 1) < 101:
            # create the node
            rightNode = Treenode(findf(x, y + 1, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x, y + 1, goalX, goalY), currentNode, (x, y + 1))

            if grid[x][y + 1] == 0:
                # add to open list if not in closed list OR openlist already
                inclosed = False
                inopen = False
                for element in globalvars.closedlist:
                    if element.coordinates == (x, y + 1):
                        inclosed = True
                        break
                if inclosed is False:
                    for e in globalvars.openlist:
                        if e.coordinates == (x, y + 1):
                            inopen = True
                            break
                if inclosed is False:
                    if inopen is False:
                        insert(rightNode)
                    # compare f values and resiftup()
                    else:
                        comparef(x, y + 1, rightNode)
            elif grid[x][y + 1] == 3:
                insert(rightNode)

        # left node, check bounds of y-1 and then if unblocked=0, blocked=1
        if (y - 1) > -1:
            # creates the node
            leftNode = Treenode(findf(x, y - 1, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x, y - 1, goalX, goalY), currentNode, (x, y - 1))

            if grid[x][y - 1] == 0:
                # add to open list if not in closed list OR openlist already
                inclosed = False
                inopen = False
                for element in globalvars.closedlist:
                    if element.coordinates == (x, y - 1):
                        inclosed = True
                        break
                if inclosed is False:
                    for e in globalvars.openlist:
                        if e.coordinates == (x, y - 1):
                            inopen = True
                            break
                if inclosed is False:
                    if inopen is False:
                        insert(leftNode)
                    # compare f values and resiftup()
                    else:
                        comparef(x, y - 1, leftNode)
            elif grid[x][y - 1] == 3:
                insert(leftNode)

        # add current node to closed list and change color
        globalvars.closedlist.append(currentNode)
        if grid[x][y] == 2:
            grid[x][y] = 2
        else:
            grid[x][y] = 4

        if x == goalX:
            if y == goalY:
                print("in goal state")
                print("Found Goal, exiting...")
                goalfound = True

                ###### backtrack here #########

                print('\n')
                print('\n')
                print("GOAL STATE IS TRUE")
                print('\n')
                print('\n')

        # --- Limit to 60 frames per second
        clock.tick(60)

    # if openlist is 0, then we cannot find the goal and have exhausted all our options
    if len(globalvars.openlist) == 0:
        print("Cannot find goal, path is blocked!")
        time.sleep(60)

    # if we hit the goal, have to backtrack
    elif goalfound is True:
        ptr = globalvars.closedlist[-1]
        currX, currY = ptr.coordinates
        while (ptr.coordinates != startCoord):
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

            grid[currX][currY] = 9

            # fill initial screen black
            BLACK = (0, 0, 0)
            screen.fill(BLACK)

            # then, update grid colors
            gridColor(screen, grid)

            # --- Limit to 60 frames per second
            clock.tick(60)

            # increment ptr
            ptr = ptr.parent
            currX, currY = ptr.coordinates
            print(ptr.f)
            print('\n')
            print(str(currX) + "," + str(currY) + '\n')

        print('Path Found')

    # now keep remaining screen up for 60 seconds
    time.sleep(60)












