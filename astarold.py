from openList import *
from gridFunc import *
from time import perf_counter

# finds h value of a node
def findh(x, y, goalX, goalY):
    hx = abs(goalX - x)
    hy = abs(goalY - y)
    return hx + hy


# finds h value of a node in Adaptive A*
def findh_adaptive(startX, startY, g, goalX, goalY):
    # take the g and the distance to the goal and subtract them
    gGoal = findh(startX, startY, goalX, goalY)
    return gGoal - g


# finds f value of a node
def findf(x, y, g, goalX, goalY):
    return g + findh(x, y, goalX, goalY)


def findf_backward(x, y, g, startX, startY):
    return g + findh(x, y, startX, startY)


# finds f value of a node in Adaptive A*
def findf_adaptive(x, y, g, goalX, goalY):
    return g + findh_adaptive(x, y, g, goalX, goalY)


# compare f values on openlist conflict
def comparef(x, y, node, openlist):
    for i in openlist:
        if i.coordinates == (x, y):
            # if node is less than, update it
            if node.f < i.f:
                i.f = node.f
                i.parent = node.parent
                i.g = node.g
                siftup()

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


def check_blocked(x, y, currentNode, grid, blocked_list):
    if (grid[x - 1][y] == 1) and (x - 1, y) not in blocked_list:
        blocked_list.append((x - 1, y))
        currentNode.g = 0
    elif (grid[x + 1][y] == 1) and (x + 1, y) not in blocked_list:
        blocked_list.append((x + 1, y))
        currentNode.g = 0
    elif (grid[x][y - 1] == 1) and (x, y - 1) not in blocked_list:
        blocked_list.append((x, y - 1))
        currentNode.g = 0
    elif (grid[x][y + 1] == 1) and (x, y + 1) not in blocked_list:
        blocked_list.append((x, y + 1))
        currentNode.g = 0


# repeated forward A* algorithm
def repeatedForwardAstar(pygame, grid, startCoord, goalCoord, time):

    openlist = []
    closedlist = []


    a = perf_counter()
    # Set the width and height of the screen [width, height], clock and display grid
    size = (505, 505)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("A* Grid")
    clock = pygame.time.Clock()

    # separate the goal coords for manipulation
    startX, startY = startCoord
    print("start X is: " + str(startX) + "," + "start Y is : " + str(startY) + '\n')
    goalX, goalY = goalCoord

    # Initialize start node
    startNode = Treenode(0, 0, 0, None, startCoord)

    # insert starting node into openlist
    insert(startNode)

    # if we find the goal state
    goalfound = False

    # if the screen has not been clicked
    done = False

    # counter for how many nodes have been seen (not necessarily expanded)
    count = 0
    total_time = 0
    shortest_path = 0

    # initialize blocked list
    blocked_list = []

    # while the open list is not empty and the goal state is not found
    while (len(openlist) != 0) and (goalfound is False) and (done is False):

        # helps display the loop
        mainEventLoop(pygame)

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

        # check to see if neighbors are blocked and not in blocked list already
        check_blocked(x, y, currentNode, grid, blocked_list)

        # up node, check bounds of x-1 and then if unblocked=0, blocked=1
        if (x - 1) > -1:
            # create the node
            upNode = Treenode(findf(x - 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x - 1, y, goalX, goalY), currentNode, (x - 1, y))

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
                        insert(upNode)
                    # compare f values and resiftup()
                    else:
                       comparef(x - 1, y, upNode)
            # goal node
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
                        insert(leftNode)
                    # compare f values and resiftup()
                    else:
                        comparef(x, y - 1, leftNode)
            elif grid[x][y - 1] == 3:
                insert(leftNode)

        # add current node to closed list and change color
        closedlist.append(currentNode)
        if grid[x][y] == 2:
            count = count + 1
            grid[x][y] = 2
        else:
            count = count + 1
            grid[x][y] = 4

        if x == goalX:
            if y == goalY:
                goalfound = True
                print('\n')
                print("GOAL STATE IS TRUE")
                print('\n')
        # --- Limit to 60 frames per second
        clock.tick(120)

    # if openlist is 0, then we cannot find the goal and have exhausted all our options
    if len(openlist) == 0:
        print("Cannot find goal, path is blocked!")
        time.sleep(60)

    # if we hit the goal, have to backtrack
    elif goalfound is True:
        ptr = closedlist[-1]
        currX, currY = ptr.coordinates

        ###### backtrack begins here #########
        while ptr.coordinates != startCoord:
            # helps display the loop
            mainEventLoop(pygame)

            # make it PINK
            grid[currX][currY] = 9

            # shortest path
            shortest_path = shortest_path + 1

            # fill initial screen black
            BLACK = (0, 0, 0)
            screen.fill(BLACK)

            # then, update grid colors
            gridColor(screen, grid)

            # --- Limit to 60 frames per second
            clock.tick(120)

            # increment ptr
            ptr = ptr.parent
            currX, currY = ptr.coordinates

        # make the last point PINK
        grid[startX][startY] = 9

        # shortest path
        shortest_path = shortest_path + 1

        # helps display the loop
        mainEventLoop(pygame)
        # fill initial screen black
        BLACK = (0, 0, 0)
        screen.fill(BLACK)
        # now fill the final color
        gridColor(screen, grid)
        print('Path Found')

        b = perf_counter()
        total_time = b - a
        # time elapsed is printed
        print(total_time)

    # now keep remaining screen up for 60 seconds
    time.sleep(15)
    pygame.display.quit()
    print("shortest path is (forward): " + str(shortest_path))
    return count, total_time, shortest_path


#
# # backward forward A* algorithm
# def repeatedBackwardAstar(pygame, grid, startCoord, goalCoord, time):
#
#     a = perf_counter()
#     # Set the width and height of the screen [width, height], clock and display grid
#     size = (505, 505)
#     screen = pygame.display.set_mode(size)
#     pygame.display.set_caption("A* Grid")
#     clock = pygame.time.Clock()
#
#     # separate the goal coords for manipulation
#     startX, startY = startCoord
#     print("start X is: " + str(startX) + "," + "start Y is : " + str(startY) + '\n')
#     goalX, goalY = goalCoord
#
#     # Initialize start node
#     startNode = Treenode(0, 0, 0, None, startCoord)
#
#     # insert starting node into openlist
#     insert(startNode)
#
#     # if we find the goal state
#     goalfound = False
#
#     # if the screen has not been clicked
#     done = False
#
#     # counter for how many nodes have been seen (not necessarily expanded)
#     count = 0
#     total_time = 0
#     shortest_path = 0
#
#     # blocked list
#     blocked_list = []
#
#     # while the open list is not empty and the goal state is not found
#     while (len(openlist) != 0) and (goalfound is False) and (done is False):
#
#         # helps display the loop
#         mainEventLoop(pygame)
#
#         # fill initial screen black
#         BLACK = (0, 0, 0)
#         screen.fill(BLACK)
#
#         # then, update grid colors
#         gridColor(screen, grid)
#
#         # pop from open list to expand first node
#         currentNode = pop()
#
#         # get current x and y coords
#         x, y = currentNode.coordinates
#         if grid[x][y] == 2:
#             print("FOUND GOAL")
#
#         # check to see if neighbors are blocked and not in blocked list already
#         check_blocked(x, y, currentNode, grid, blocked_list)
#
#         # up node, check bounds of x-1 and then if unblocked=0, blocked=1
#         if (x - 1) > -1:
#             # create the node
#             upNode = Treenode(findf(x - 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x - 1, y, goalX, goalY), currentNode, (x - 1, y))
#
#             if grid[x - 1][y] == 0:
#                 # add to open list if not in closed list OR openlist already
#                 inclosed = False
#                 inopen = False
#                 for element in closedlist:
#                     if element.coordinates == (x - 1, y):
#                         inclosed = True
#                         break
#                 if inclosed is False:
#                     for e in openlist:
#                         if e.coordinates == (x - 1, y):
#                             inopen = True
#                             break
#                 if inclosed is False:
#                     if inopen is False:
#                         insert(upNode)
#                     # compare f values and resiftup()
#                     else:
#                        comparef(x - 1, y, upNode)
#             elif grid[x - 1][y] == 2:
#                 insert(upNode)
#
#         # down node, check bounds of x+1 and then if unblocked=0, blocked=1
#         if (x + 1) < 101:
#             # create the node
#             downNode = Treenode(findf(x + 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x + 1, y, goalX, goalY), currentNode, (x + 1, y))
#
#             if grid[x + 1][y] == 0:
#                 # add to open list if not in closed list OR openlist already
#                 inclosed = False
#                 inopen = False
#                 for element in closedlist:
#                     if element.coordinates == (x + 1, y):
#                         inclosed = True
#                         break
#                 if inclosed is False:
#                     for e in openlist:
#                         if e.coordinates == (x + 1, y):
#                             inopen = True
#                             break
#                 if inclosed is False:
#                     if inopen is False:
#                         insert(downNode)
#                     # compare f values and resiftup()
#                     else:
#                         comparef(x + 1, y, downNode)
#             elif grid[x + 1][y] == 2:
#                 insert(downNode)
#
#         # right node, check bounds of y+1 and then if unblocked=0, blocked=1
#         if (y + 1) < 101:
#             # create the node
#             rightNode = Treenode(findf(x, y + 1, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x, y + 1, goalX, goalY), currentNode, (x, y + 1))
#
#             if grid[x][y + 1] == 0:
#                 # add to open list if not in closed list OR openlist already
#                 inclosed = False
#                 inopen = False
#                 for element in closedlist:
#                     if element.coordinates == (x, y + 1):
#                         inclosed = True
#                         break
#                 if inclosed is False:
#                     for e in openlist:
#                         if e.coordinates == (x, y + 1):
#                             inopen = True
#                             break
#                 if inclosed is False:
#                     if inopen is False:
#                         insert(rightNode)
#                     # compare f values and resiftup()
#                     else:
#                         comparef(x, y + 1, rightNode)
#             elif grid[x][y + 1] == 2:
#                 insert(rightNode)
#
#         # left node, check bounds of y-1 and then if unblocked=0, blocked=1
#         if (y - 1) > -1:
#             # creates the node
#             leftNode = Treenode(findf(x, y - 1, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh(x, y - 1, goalX, goalY), currentNode, (x, y - 1))
#
#             if grid[x][y - 1] == 0:
#                 # add to open list if not in closed list OR openlist already
#                 inclosed = False
#                 inopen = False
#                 for element in closedlist:
#                     if element.coordinates == (x, y - 1):
#                         inclosed = True
#                         break
#                 if inclosed is False:
#                     for e in openlist:
#                         if e.coordinates == (x, y - 1):
#                             inopen = True
#                             break
#                 if inclosed is False:
#                     if inopen is False:
#                         insert(leftNode)
#                     # compare f values and resiftup()
#                     else:
#                         comparef(x, y - 1, leftNode)
#             elif grid[x][y - 1] == 2:
#                 insert(leftNode)
#
#         # add current node to closed list and change color
#         closedlist.append(currentNode)
#         if grid[x][y] == 3:
#             count = count + 1
#             grid[x][y] = 3
#         else:
#             count = count + 1
#             grid[x][y] = 4
#
#         if x == goalX:
#             if y == goalY:
#                 goalfound = True
#                 print('\n')
#                 print("GOAL STATE IS TRUE")
#                 print('\n')
#         # --- Limit to 60 frames per second
#         clock.tick(120)
#
#     # if openlist is 0, then we cannot find the goal and have exhausted all our options
#     if len(openlist) == 0:
#         print("Cannot find goal, path is blocked!")
#         time.sleep(60)
#
#     # if we hit the goal, have to backtrack
#     elif goalfound is True:
#         ptr = closedlist[-1]
#         currX, currY = ptr.coordinates
#
#         ###### backtrack begins here #########
#         while ptr.coordinates != startCoord:
#             # helps display the loop
#             mainEventLoop(pygame)
#
#             # make it PINK
#             grid[currX][currY] = 9
#
#             # shortest path
#             shortest_path = shortest_path + 1
#
#             # fill initial screen black
#             BLACK = (0, 0, 0)
#             screen.fill(BLACK)
#
#             # then, update grid colors
#             gridColor(screen, grid)
#
#             # --- Limit to 60 frames per second
#             clock.tick(120)
#
#             # increment ptr
#             ptr = ptr.parent
#             currX, currY = ptr.coordinates
#
#         # make the last point PINK
#         grid[startX][startY] = 9
#
#         # shortest path
#         shortest_path = shortest_path + 1
#
#         # helps display the loop
#         mainEventLoop(pygame)
#         # fill initial screen black
#         BLACK = (0, 0, 0)
#         screen.fill(BLACK)
#         # now fill the final color
#         gridColor(screen, grid)
#         print('Path Found')
#
#         b = perf_counter()
#         total_time = b-a
#         print(total_time)
#         #time elapsed is printed
#
#
#     # now keep remaining screen up for 60 seconds
#     time.sleep(15)
#     #pygame.image.save(screen, "screenshot.jpg")
#     openlist = []
#     closedlist = []
#     pygame.display.quit()
#     print ("shortest path is (backward): " + str(shortest_path))
#     return (count, total_time, shortest_path)
#
#
#
# # repeated forward A* algorithm
# def adaptive_repeatedForwardAstar(pygame, grid, startCoord, goalCoord, time):
#
#     a = perf_counter()
#     # Set the width and height of the screen [width, height], clock and display grid
#     size = (505, 505)
#     screen = pygame.display.set_mode(size)
#     pygame.display.set_caption("A* Grid")
#     clock = pygame.time.Clock()
#
#     # separate the goal coords for manipulation
#     startX, startY = startCoord
#     print("start X is: " + str(startX) + "," + "start Y is : " + str(startY) + '\n')
#     goalX, goalY = goalCoord
#
#     # Initialize start node
#     startNode = Treenode(0, 0, 0, None, startCoord)
#
#     # insert starting node into openlist
#     insert(startNode)
#
#     # if we find the goal state
#     goalfound = False
#
#     # if the screen has not been clicked
#     done = False
#
#     # counter for how many nodes have been seen (not necessarily expanded)
#     count = 0
#     total_time = 0
#     shortest_path = 0
#
#     # blocked list
#     blocked_list = []
#
#     # while the open list is not empty and the goal state is not found
#     while (len(openlist) != 0) and (goalfound is False) and (done is False):
#
#         # helps display the loop
#         mainEventLoop(pygame)
#
#         # fill initial screen black
#         BLACK = (0, 0, 0)
#         screen.fill(BLACK)
#
#         # then, update grid colors
#         gridColor(screen, grid)
#
#         # pop from open list to expand first node
#         currentNode = pop()
#
#         # get current x and y coords
#         x, y = currentNode.coordinates
#         if grid[x][y] == 3:
#             print("FOUND GOAL")
#
#         # check to see if neighbors are blocked and not in blocked list already
#         check_blocked(x, y, currentNode, grid, blocked_list)
#
#         # up node, check bounds of x-1 and then if unblocked=0, blocked=1
#         if (x - 1) > -1:
#             # create the node
#             upNode = Treenode(findf(x - 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh_adaptive(startX, startY, currentNode.g + 1, goalX, goalY), currentNode, (x - 1, y))
#
#             if grid[x - 1][y] == 0:
#                 # add to open list if not in closed list OR openlist already
#                 inclosed = False
#                 #inclosed = any([element.coordinates == (x - 1, y) for element in closedlist])
#                 inopen = False
#                 for element in closedlist:
#                     if element.coordinates == (x - 1, y):
#                         inclosed = True
#                         break
#                 if inclosed is False:
#                     for e in openlist:
#                         if e.coordinates == (x - 1, y):
#                             inopen = True
#                             break
#                 if inclosed is False:
#                     if inopen is False:
#                         insert(upNode)
#                     # compare f values and resiftup()
#                     else:
#                        comparef(x - 1, y, upNode)
#             elif grid[x - 1][y] == 3:
#                 insert(upNode)
#
#         # down node, check bounds of x+1 and then if unblocked=0, blocked=1
#         if (x + 1) < 101:
#             # create the node
#             downNode = Treenode(findf(x + 1, y, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh_adaptive(startX, startY, currentNode.g + 1, goalX, goalY), currentNode, (x + 1, y))
#
#             if grid[x + 1][y] == 0:
#                 # add to open list if not in closed list OR openlist already
#                 inclosed = False
#                 inopen = False
#                 for element in closedlist:
#                     if element.coordinates == (x + 1, y):
#                         inclosed = True
#                         break
#                 if inclosed is False:
#                     for e in openlist:
#                         if e.coordinates == (x + 1, y):
#                             inopen = True
#                             break
#                 if inclosed is False:
#                     if inopen is False:
#                         insert(downNode)
#                     # compare f values and resiftup()
#                     else:
#                         comparef(x + 1, y, downNode)
#             elif grid[x + 1][y] == 3:
#                 insert(downNode)
#
#         # right node, check bounds of y+1 and then if unblocked=0, blocked=1
#         if (y + 1) < 101:
#             # create the node
#             rightNode = Treenode(findf(x, y + 1, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh_adaptive(startX, startY, currentNode.g + 1, goalX, goalY), currentNode, (x, y + 1))
#
#             if grid[x][y + 1] == 0:
#                 # add to open list if not in closed list OR openlist already
#                 inclosed = False
#                 inopen = False
#                 for element in closedlist:
#                     if element.coordinates == (x, y + 1):
#                         inclosed = True
#                         break
#                 if inclosed is False:
#                     for e in openlist:
#                         if e.coordinates == (x, y + 1):
#                             inopen = True
#                             break
#                 if inclosed is False:
#                     if inopen is False:
#                         insert(rightNode)
#                     # compare f values and resiftup()
#                     else:
#                         comparef(x, y + 1, rightNode)
#             elif grid[x][y + 1] == 3:
#                 insert(rightNode)
#
#         # left node, check bounds of y-1 and then if unblocked=0, blocked=1
#         if (y - 1) > -1:
#             # creates the node
#             leftNode = Treenode(findf(x, y - 1, currentNode.g + 1, goalX, goalY), currentNode.g + 1, findh_adaptive(startX, startY, currentNode.g + 1, goalX, goalY), currentNode, (x, y - 1))
#
#             if grid[x][y - 1] == 0:
#                 # add to open list if not in closed list OR openlist already
#                 inclosed = False
#                 inopen = False
#                 for element in closedlist:
#                     if element.coordinates == (x, y - 1):
#                         inclosed = True
#                         break
#                 if inclosed is False:
#                     for e in openlist:
#                         if e.coordinates == (x, y - 1):
#                             inopen = True
#                             break
#                 if inclosed is False:
#                     if inopen is False:
#                         insert(leftNode)
#                     # compare f values and resiftup()
#                     else:
#                         comparef(x, y - 1, leftNode)
#             elif grid[x][y - 1] == 3:
#                 insert(leftNode)
#
#         # add current node to closed list and change color
#         closedlist.append(currentNode)
#         if grid[x][y] == 2:
#             count = count + 1
#             grid[x][y] = 2
#         else:
#             count = count + 1
#             grid[x][y] = 4
#
#         if x == goalX:
#             if y == goalY:
#                 goalfound = True
#                 print('\n')
#                 print("GOAL STATE IS TRUE")
#                 print('\n')
#         # --- Limit to 60 frames per second
#         clock.tick(120)
#
#     # if openlist is 0, then we cannot find the goal and have exhausted all our options
#     if len(openlist) == 0:
#         print("Cannot find goal, path is blocked!")
#         time.sleep(60)
#
#     # if we hit the goal, have to backtrack
#     elif goalfound is True:
#         ptr = closedlist[-1]
#         currX, currY = ptr.coordinates
#
#         ###### backtrack begins here #########
#         while ptr.coordinates != startCoord:
#             # helps display the loop
#             mainEventLoop(pygame)
#
#             # make it PINK
#             grid[currX][currY] = 9
#
#             # shortest path
#             shortest_path = shortest_path + 1
#
#             # fill initial screen black
#             BLACK = (0, 0, 0)
#             screen.fill(BLACK)
#
#             # then, update grid colors
#             gridColor(screen, grid)
#
#             # --- Limit to 60 frames per second
#             clock.tick(120)
#
#             # increment ptr
#             ptr = ptr.parent
#             currX, currY = ptr.coordinates
#
#         # make the last point PINK
#         grid[startX][startY] = 9
#
#         # shortest path
#         shortest_path = shortest_path + 1
#
#         # helps display the loop
#         mainEventLoop(pygame)
#         # fill initial screen black
#         BLACK = (0, 0, 0)
#         screen.fill(BLACK)
#         # now fill the final color
#         gridColor(screen, grid)
#         print('Path Found')
#
#         b = perf_counter()
#         total_time = b - a
#         print(total_time)
#         #time elapsed is printed
#
#
#     # now keep remaining screen up for 60 seconds
#     time.sleep(15)
#     #pygame.image.save(screen, "screenshot.jpg")
#     openlist = []
#     closedlist = []
#     pygame.display.quit()
#     return (count, total_time, shortest_path)













