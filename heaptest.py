import openList
import globalvars
import random

SIZE = 5000
NUM_TESTS = 10
REPLACEMENT = True

def main():
	my_list = random.choices(list(range(SIZE)), k = SIZE) if REPLACEMENT else random.sample(list(range(SIZE)), SIZE)
	for i in range(NUM_TESTS):
		for number in my_list:
			openList.insert(openList.Treenode(number, 0, None, None, None))
		while len(globalvars.openlist) > 0:
			vals = [Treenode.f for Treenode in globalvars.openlist]
			if vals[0] != min(vals):
				print("Bad heap")
				return
			openList.pop()
		print("Passed test {}".format(i + 1))
	print("Heap passed test")
main()