import globalvars

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
def siftup():
    k = len(globalvars.openlist) - 1
    while k > 0:
        p = (k-1) // 2
        current = globalvars.openlist[k]
        parent = globalvars.openlist[p]

        # g value check, take the smaller one
        if current.f == parent.f:
            if current.g < parent.g:
                # swap the current and parent
                temp = globalvars.openlist[p]
                globalvars.openlist[p] = globalvars.openlist[k]
                globalvars.openlist[k] = temp
                # move p to next level
                k = p

        # if the current is less than the parent, switch them as we bubble up
        if current.f < parent.f:
            # swap the current and parent
            temp = globalvars.openlist[p]
            globalvars.openlist[p] = globalvars.openlist[k]
            globalvars.openlist[k] = temp
            # move p to next level
            k = p
        else:
            break


# siftdown to sort after delete
def siftdown():
    k = 0
    left = 2 * k + 1
    # while the left is less than the size of the open list
    while left < len(globalvars.openlist):
        min = left
        right = left + 1

        # if the right is less than the total size, check if the right is less than the left
        if right < len(globalvars.openlist):
            if globalvars.openlist[right].f < globalvars.openlist[left].f:
                min = right
        # if the k is greater than the min, grab the
        if globalvars.openlist[k].f > globalvars.openlist[min].f:
            temp = globalvars.openlist[k]
            globalvars.openlist[k] = globalvars.openlist[min]
            globalvars.openlist[min] = temp
            # increment k to the min and the left to the 2k+1 new left
            k = min
            left = 2 * k + 1
        else:
            break


# insert to place into the globalvars.openlist
def insert(toinsert):
    globalvars.openlist.append(toinsert)
    siftup()


# pop to remove out of the globalvars.openlist
def pop():
    # base case, if size is 0 then we have an exception
    if len(globalvars.openlist) == 0:
        print("Error, cannot pop an empty list. Exiting...")
        exit()
    # if size is 1, remove the first element
    if len(globalvars.openlist) == 1:
        firstElement = globalvars.openlist[0]
        del globalvars.openlist[-1]
        return firstElement
    # now delete the root and replace it with the right most node, then siftdown
    todelete = globalvars.openlist[0]
    last = len(globalvars.openlist) - 1
    globalvars.openlist[0] = globalvars.openlist[last]
    del globalvars.openlist[-1]
    siftdown()
    return todelete

# print the globalvars.openlist
def printList():
    # print list
    i = 0
    while i < len(globalvars.openlist):
        node = globalvars.openlist[i]
        print(node.f)
        i = i + 1

'''
def main():
    # insert 3 elements
    n1 = Treenode(3, None, (0,0))
    n2 = Treenode(5, None, (0,1))
    n3 = Treenode(9, None, (0,2))
    n4 = Treenode(6, None, (0, 0))
    n5 = Treenode(8, None, (0, 1))
    n6 = Treenode(20, None, (0, 2))
    n7 = Treenode(10, None, (0, 0))
    n8 = Treenode(12, None, (0, 1))
    n9 = Treenode(18, None, (0, 2))
    n10 = Treenode(9, None, (0, 2))
    insert(n1)
    insert(n2)
    insert(n3)
    insert(n4)
    insert(n5)
    insert(n6)
    insert(n7)
    insert(n8)
    insert(n9)
    insert(n10)

    printList()
    print('\n')

    # delete element
    deleted = pop()
    deleted = pop()
    deleted = pop()
    print ("deleted = " + str(deleted.f))
    printList()


if __name__ == '__main__':
    main()
'''




