from openList import *
import random

openlist = []
for i in range(10):
	openlist = insert(Treenode(random.randint(0, 3), random.randint(0, 3), None, None, None), openlist)

while len(openlist) != 0:
	node, openlist = pop(openlist)
	print("({}, {})".format(node.f, node.g))