from openList import *

# finds g value of a node
'''def findg(x, y):
    gx = abs(globalvars.rand_start_x - x)
    gy = abs(globalvars.rand_start_y - y)
    return gx + gy
'''


# finds h value of a node
def findh(x, y):
    hx = abs(globalvars.rand_goal_x - x)
    hy = abs(globalvars.rand_goal_y - y)
    return hx + hy


# finds f value of a node
def findf(x, y, g):
    #return g + findh(x, y)
    return findh(x, y)


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
def repeatedForwardAstar():

    # if we find the goal state
    #goalfound = False

    # while the open list is not empty and the goal state is not found
    #while (len(openlist) != 0) and (goalfound == False):

    # pop from open list to expand first node
    currentNode = pop()
    #print (currentNode.f)
    #print('\n')

    # get current x and y coords
    x, y = currentNode.coordinates
    if globalvars.grid[x][y] == 3:
        print("FOUND GOAL")

    # up node, check bounds of x-1 and then if unblocked=0, blocked=1
    if (x - 1) > -1:
        # create the node
        upNode = Treenode(findf(x - 1, y, currentNode.g + 1), currentNode.g + 1, findh(x - 1, y), currentNode, (x - 1, y))

        if globalvars.grid[x - 1][y] == 0:
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
        elif globalvars.grid[x - 1][y] == 3:
            insert(upNode)

    # down node, check bounds of x+1 and then if unblocked=0, blocked=1
    if (x + 1) < 101:
        # create the node
        downNode = Treenode(findf(x + 1, y, currentNode.g + 1), currentNode.g + 1, findh(x + 1, y), currentNode, (x + 1, y))

        if globalvars.grid[x + 1][y] == 0:
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
        elif globalvars.grid[x + 1][y] == 3:
            insert(downNode)

    # right node, check bounds of y+1 and then if unblocked=0, blocked=1
    if (y + 1) < 101:
        # create the node
        rightNode = Treenode(findf(x, y + 1, currentNode.g + 1), currentNode.g + 1, findh(x, y + 1), currentNode, (x, y + 1))

        if globalvars.grid[x][y + 1] == 0:
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
        elif globalvars.grid[x][y + 1] == 3:
            insert(rightNode)

    # left node, check bounds of y-1 and then if unblocked=0, blocked=1
    if (y - 1) > -1:
        # creates the node
        leftNode = Treenode(findf(x, y - 1, currentNode.g + 1), currentNode.g + 1, findh(x, y - 1), currentNode, (x, y - 1))

        if globalvars.grid[x][y - 1] == 0:
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
        elif globalvars.grid[x][y - 1] == 3:
            insert(leftNode)


    # add currnode to closed list and change color
    globalvars.closedlist.append(currentNode)
    globalvars.grid[x][y] = 4
    globalvars.currentX = x
    globalvars.currentY = y
    #if globalvars.goalCord == currentNode.coordinates:
    if x == globalvars.rand_goal_x:
        if y == globalvars.rand_goal_y:
            print("in goal state")
            print("Found Goal, exiting...")
            globalvars.goalState = True





