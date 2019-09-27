class Treenode:
    # initialize values
    def __init__(self, f, parent, coordinates):
        self.f = f
        self.parent = parent
        self.coordinates = coordinates

# global openlist
openlist = []

# siftup to sort after insert
def siftup():
    k = len(openlist) - 1
    while k > 0:
        p = (k-1) / 2
        current = openlist[k]
        parent = openlist[p]

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

# siftdown to sort after delete
def siftdown():
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

# insert to place into the openlist
def insert(toinsert):
    openlist.append(toinsert)
    siftup()

# pop to remove out of the openlist
def pop():
    # base case, if size is 0 then we have an exception
    if len(openlist) == 0:
        print("Error, cannot pop an empty list. Exiting...")
        return
    #try:
    #    if len(openlist) == 0:
    #except ValueError as error:
    #    print(error.args)
    # if size is 1, remove the first element
    if len(openlist) == 1:
        return openlist.remove(0)
    # now delete the root and replace it with the right most node, then siftdown
    todelete = openlist[0]
    openlist[0] = openlist[len(openlist) - 1]
    openlist.remove(len(openlist) - 1)
    siftdown()
    return todelete


