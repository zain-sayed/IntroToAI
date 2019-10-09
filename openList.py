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

        # # g value check, take the smaller one
        # if current.f == parent.f:
        #     if current.g < parent.g:
        #         # swap the current and parent
        #         temp = openlist[p]
        #         openlist[p] = openlist[k]
        #         openlist[k] = temp
        #         # move p to next level
        #         k = p

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
        return firstElement
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

'''
def main():
    # insert 3 elements
    n1 = Treenode(41, 2, 2, None, (0,0))
    n2 = Treenode(43, 3, 3, None, (0,1))
    n3 = Treenode(43, 3, 4, None, (0,2))
    n4 = Treenode(43, 2, 5, None, (0, 0))
    n5 = Treenode(43, 3, 7,None, (0, 1))
    n6 = Treenode(43, 7, 0, None, (0, 2))
    n7 = Treenode(43, 8, 0, None, (0, 0))
    n8 = Treenode(43, 0, 0, None, (0, 1))
    n9 = Treenode(43, 0, 0, None, (0, 2))
    n10 = Treenode(43, 0, 0, None, (0, 2))

    # n11 = Treenode(43, 0, 0, None, (0, 0))
    # n12 = Treenode(43, 0, 0, None, (0, 1))
    #
    # n13 = Treenode(41, 0, 0, None, (0, 2))
    # n14 = Treenode(43, 0, 0, None, (0, 0))
    # n15 = Treenode(43, 0, 0, None, (0, 1))
    # n16 = Treenode(43, 0, 0, None, (0, 2))
    # n17 = Treenode(43, 0, 0, None, (0, 0))
    # n18 = Treenode(43, 0, 0, None, (0, 1))
    #
    # n19 = Treenode(41, 0, 0, None, (0, 2))
    # n20 = Treenode(41, 0, 0, None, (0, 2))
    n21 = Treenode(41, 0, 0, None, (0, 0))
    #
    n22 = Treenode(3, 0, 0, None, (0, 1))
    n23 = Treenode(2, 0, 0, None, (0, 2))
    n24 = Treenode(42, 0, 0, None, (0, 0))
    n25 = Treenode(100, 0, 0, None, (0, 1))
    # n26 = Treenode(43, 0, 0, None, (0, 2))
    # n27 = Treenode(43, 0, 0, None, (0, 0))
    # n28 = Treenode(43, 0, 0, None, (0, 1))
    # n29 = Treenode(43, 0, 0, None, (0, 2))
    # n30 = Treenode(43, 0, 0, None, (0, 2))
    # n31 = Treenode(43, 0, 0, None, (0, 0))
    # n32 = Treenode(43, 0, 0, None, (0, 1))
    # n33 = Treenode(43, 0, 0, None, (0, 2))
    # n34 = Treenode(43, 0, 0, None, (0, 0))
    # n35 = Treenode(43, 0, 0, None, (0, 1))
    # n36 = Treenode(43, 0, 0, None, (0, 2))



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
    #
    # insert(n11)
    # insert(n12)
    # insert(n13)
    # insert(n14)
    # insert(n15)
    # insert(n16)
    # insert(n17)
    # insert(n18)
    # insert(n19)
    # insert(n20)
    #insert(n21)
    # insert(n22)
    # insert(n23)
    # insert(n24)
    # insert(n25)
    # insert(n26)
    # insert(n27)
    # insert(n28)
    # insert(n29)
    # insert(n30)
    # insert(n31)
    # insert(n32)
    # insert(n33)
    # insert(n34)
    # insert(n35)
    # insert(n36)




    printList()
    print('\n')

    # delete element
    deleted = pop()
    print ("deleted = " + str(deleted.f))
    printList()

    print('\n')
    insert(n21)
    printList()

    print('\n')
    # delete element
    deleted = pop()
    print("deleted = " + str(deleted.f))
    printList()

    print('\n')
    insert(n22)
    printList()

    print('\n')
    # delete element
    deleted = pop()
    print("deleted = " + str(deleted.f))
    printList()

    print('\n')
    insert(n23)
    printList()

    print('\n')
    # delete element
    deleted = pop()
    print("deleted = " + str(deleted.f))
    printList()

    print('\n')
    insert(n24)
    printList()

    print('\n')
    insert(n25)
    printList()

    print('\n')
    # delete element
    deleted = pop()
    print("deleted = " + str(deleted.f))
    printList()

    print('\n')
    # delete element
    deleted = pop()
    print("deleted = " + str(deleted.f))
    printList()


if __name__ == '__main__':
    main()
'''

