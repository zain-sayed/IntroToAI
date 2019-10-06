import astar
import pygame
import gridFunc
import xlwt
import time
import random

NUM_TIMES = 10

def main():
	book = xlwt.Workbook()
	fwd_sheet = book.add_sheet("Foward")
	fwd_sheet.write(0, 0, "Observation")
	fwd_sheet.write(0, 1, "Time")
	fwd_sheet.write(0, 2, "Cells Expanded")
	random.seed(0)
	for i in range(NUM_TIMES):
		pygame.init()
		# start coords
		rand_start_x = random.randint(0, 100)
		rand_start_y = random.randint(0, 100)
		startCoord = (rand_start_x, rand_start_y)

		# goal coords
		rand_goal_x = random.randint(0, 100)
		rand_goal_y = random.randint(0, 100)
		goalCoord =  (rand_goal_x, rand_goal_y)

		# initialize grid
		grid = gridFunc.gridInit(startCoord, goalCoord)

		cells_explored, time_stamp = astar.repeatForwardAStar(pygame, grid, startCoord, goalCoord, time)
		fwd_sheet.write(i + 1, 0, i + 1)
		fwd_sheet.write(i + 1, 1, time_stamp)
		fwd_sheet.write(i + 1, 2, cells_explored)
		pygame.quit()
	book.save("Results.xlsx")


main()