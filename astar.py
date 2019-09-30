from openList import *

# finds g value of a node
def findg(x, y):
    gx = abs(globalvars.rand_start_x - x)
    gy = abs(globalvars.rand_start_y - y)
    return gx + gy


# finds h value of a node
def findh(x, y):
    hx = abs(globalvars.rand_goal_x - x)
    hy = abs(globalvars.rand_goal_y - y)
    return hx + hy


# finds f value of a node
def findf(x, y):
    return findg(x, y) + findh(x, y)
    #return findg(x, y)


# compare f values on openlist conflict
def comparef(x, y, node):
    for i in globalvars.openlist:
        if i.coordinates == (x, y):
            # if node is less than, update it
            if node.f < i.f:
                i.f = node.f
                i.parent = node.parent
                siftup()


# repeated forward A* algorithm
def repeatedForwardAstar():

    # if we find the goal state
    #goalfound = False

    # while the open list is not empty and the goal state is not found
    #while (len(openlist) != 0) and (goalfound == False):

    # pop from open list to expand first node
    currentNode = pop()
    print (currentNode.f)
    print('\n')

    # get current x and y coords
    x, y = currentNode.coordinates

    # up node, check bounds of x-1 and then if unblocked=0, blocked=1
    if (x - 1) > -1:
        if globalvars.grid[x - 1][y] == 0:
            upNode = Treenode(findf(x - 1,y), currentNode, (x - 1,y))

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

    # down node, check bounds of x+1 and then if unblocked=0, blocked=1
    if (x + 1) < 101:
        if globalvars.grid[x + 1][y] == 0:
            downNode = Treenode(findf(x + 1, y), currentNode, (x + 1, y))

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

    # right node, check bounds of y+1 and then if unblocked=0, blocked=1
    if (y + 1) < 101:
        if globalvars.grid[x][y + 1] == 0:
            rightNode = Treenode(findf(x, y + 1), currentNode, (x, y + 1))

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

    # left node, check bounds of y-1 and then if unblocked=0, blocked=1
    if (y - 1) > -1:
        if globalvars.grid[x][y - 1] == 0:
            leftNode = Treenode(findf(x,y - 1), currentNode, (x,y - 1))

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

    # add currnode to closed list and change color
    globalvars.closedlist.append(currentNode)
    globalvars.grid[x][y] = 4
    globalvars.currentX = x
    globalvars.currentY = y
    print(globalvars.currentX)
    print(globalvars.currentY)
    if globalvars.goalCord == currentNode.coordinates:
        goalState = True





