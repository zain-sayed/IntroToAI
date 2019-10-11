#import globalvars

class Treenode:
    # initialize values
    def __init__(self, f, g, h, parent, coordinates):
        self.f = f
        self.g = g
        self.h = h
        self.parent = parent
        self.coordinates = coordinates


###################################### have to do an equal g value condition  ######################################  
# siftup to sort after insert
def siftup(openlist):
    k = len(openlist) - 1
    while k > 0:
        p = (k-1) // 2
        current = openlist[k]
        parent = openlist[p]

        # g value check, take the smaller one
        if current.f == parent.f:
            if current.g < parent.g:
                # swap the current and parent
                temp = openlist[p]
                openlist[p] = openlist[k]
                openlist[k] = temp
                # move p to next level
                k = p

        # if the current is less than the parent, switch them as we bubble up
        if current.f < parent.f:
            # swap the current and parent
            temp = openlist[p]
            openlist[p] = openlist[k]
            openlist[k] = temp
            # move p to next level
            k = p
        else:
            break
    return openlist


# siftdown to sort after delete
def siftdown(openlist):
    k = 0
    left = 2 * k + 1
    # while the left is less than the size of the open list
    while left < len(openlist):
        min = left
        right = left + 1

        # if the right is less than the total size, check if the right is less than the left
        if right < len(openlist):
            if openlist[right].f < openlist[left].f:
                min = right
        # if the k is greater than the min, grab the
        if openlist[k].f > openlist[min].f:
            temp = openlist[k]
            openlist[k] = openlist[min]
            openlist[min] = temp
            # increment k to the min and the left to the 2k+1 new left
            k = min
            left = 2 * k + 1
        else:
            break
    return openlist


# insert to place into the openlist
def insert(toinsert, openlist):
    openlist.append(toinsert)
    siftup(openlist)
    return openlist


# pop to remove out of the openlist
def pop(openlist):
    # base case, if size is 0 then we have an exception
    if len(openlist) == 0:
        print("Error, cannot pop an empty list. Exiting...")
        exit()
    # if size is 1, remove the first element
    if len(openlist) == 1:
        firstElement = openlist[0]
        del openlist[-1]
        return firstElement, openlist
    # now delete the root and replace it with the right most node, then siftdown
    todelete = openlist[0]
    last = len(openlist) - 1
    openlist[0] = openlist[last]
    del openlist[-1]
    openlist = siftdown(openlist)
    return todelete, openlist


# print the openlist
def printList(openlist):
    # print list
    i = 0
    while i < len(openlist):
        node = openlist[i]
        print(node.f)
        i = i + 1

