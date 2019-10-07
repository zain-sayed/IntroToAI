import openList
import globalvars
import random

SIZE = 5000

def main():
	my_list = random.sample(list(range(SIZE)), SIZE)
	for number in my_list:
		openList.insert(openList.Treenode(number, 0, None, None, None))
	while len(my_list) > 0:
		if globalvars.openlist[0] != min(globalvars.openlist):
			print("Bad heap")
			return
		pop()
	print("Heap passed test")
main()