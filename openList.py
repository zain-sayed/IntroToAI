class Treenode:
    # initialize values
    def __init__(self, f, parent, coordinates):
        self.f = f
        self.parent = parent
        self.coordinates = coordinates


# global openlist
openlist = []


###################################### have to do an equal g value condition  ######################################  
# siftup to sort after insert
def siftup():
    k = len(openlist) - 1
    while k > 0:
        p = (k-1) // 2
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
        exit()
    # if size is 1, remove the first element
    if len(openlist) == 1:
        return openlist.remove(0)
    # now delete the root and replace it with the right most node, then siftdown
    todelete = openlist[0]
    last = len(openlist) - 1
    openlist[0] = openlist[last]
    del openlist[-1]
    siftdown()
    return todelete

# print the openlist
def printList():
    # print list
    i = 0
    while i < len(openlist):
        node = openlist[i]
        print(node.f)
        i = i + 1


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





