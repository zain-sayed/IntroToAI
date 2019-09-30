from openList import *
#import pygameBase
#from pygameBase import *

# closedlist and globals
closedlist = []
currentX = -1
currentY = -1

# finds g value of a node
def findg(x, y):
    gx = abs(rand_start_x - x)
    gy = abs(rand_start_y - y)
    return gx + gy


# finds h value of a node
def findh(x, y):
    hx = abs(rand_goal_x - x)
    hy = abs(rand_goal_y - y)
    return hx + hy


# finds f value of a node
def findf(x, y):
    return findg(x, y) + findh(x, y)


# compare f values on openlist conflict
def comparef(x, y, node):
    for i in openlist:
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

    # get current x and y coords
    x, y = currentNode.coordinates

    # up node, check bounds of x-1 and then if unblocked=0, blocked=1
    if (x - 1) > -1:
        if grid[x - 1][y] == 0:
            upNode = Treenode(findf(x - 1,y), currentNode, (x - 1,y))

            # add to open list if not in closed list OR openlist already
            if (x - 1, y) not in closedlist.coordinates:
                if (x - 1, y) not in openlist.coordinates:
                    insert(upNode)
                # compare f values and resiftup()
                else:
                    comparef(x - 1, y, upNode)

    # down node, check bounds of x+1 and then if unblocked=0, blocked=1
    if (x + 1) < 101:
        if grid[x + 1][y] == 0:
            downNode = Treenode(findf(x + 1, y), currentNode, (x + 1, y))

            # add to open list if not in closed list OR openlist already
            if (x + 1, y) not in closedlist.coordinates:
                if (x + 1, y) not in openlist.coordinates:
                    insert(downNode)
                # compare f values and resiftup()
                else:
                    comparef(x + 1, y, downNode)

    # right node, check bounds of y+1 and then if unblocked=0, blocked=1
    if (y + 1) < 101:
        if grid[x][y + 1] == 0:
            rightNode = Treenode(findf(x, y + 1), currentNode, (x, y + 1))

            # add to open list if not in closed list OR openlist already
            if (x, y + 1) not in closedlist.coordinates:
                if (x, y + 1) not in openlist.coordinates:
                    insert(rightNode)
                # compare f values and resiftup()
                else:
                    comparef(x, y + 1, rightNode)

    # left node, check bounds of y-1 and then if unblocked=0, blocked=1
    if (y - 1) > -1:
        if grid[x][y - 1] == 0:
            leftNode = Treenode(findf(x,y - 1), currentNode, (x,y - 1))

            # add to open list if not in closed list OR openlist already
            if (x, y - 1) not in closedlist.coordinates:
                if (x, y - 1) not in openlist.coordinates:
                    insert(leftNode)
                # compare f values and resiftup()
                else:
                    comparef(x, y - 1, leftNode)

    # add currnode to closed list and change color
    closedlist.append(currentNode)
    grid[x][y] = 4
    currentX = x
    currentY = y




