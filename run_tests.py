import astar
import pygame
import gridFunc
import xlwt
import time
import random

NUM_TIMES = 1

def main():
	book = xlwt.Workbook()
	fwd_sheet = book.add_sheet("Foward")
	bwd_sheet = book.add_sheet("Backward")
	adpt_sheet = book.add_sheet("Adaptive")
	fwd_sheet.write(0, 0, "Observation")
	fwd_sheet.write(0, 1, "Time")
	fwd_sheet.write(0, 2, "Cells Expanded")
	bwd_sheet.write(0, 0, "Observation")
	bwd_sheet.write(0, 1, "Time")
	bwd_sheet.write(0, 2, "Cells Expanded")
	adpt_sheet.write(0, 0, "Observation")
	adpt_sheet.write(0, 1, "Time")
	adpt_sheet.write(0, 2, "Cells Expanded")
	random.seed(1)
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

		cells_explored, time_stamp = astar.repeatedForwardAstar(pygame, grid, startCoord, goalCoord, time)
		fwd_sheet.write(i + 1, 0, i + 1)
		fwd_sheet.write(i + 1, 1, time_stamp)
		fwd_sheet.write(i + 1, 2, cells_explored)

		cells_explored, time_stamp = astar.repeatedBackwardAstar(pygame, grid, startCoord, goalCoord, time)
		bwd_sheet.write(i + 1, 0, i + 1)
		bwd_sheet.write(i + 1, 1, time_stamp)
		bwd_sheet.write(i + 1, 2, cells_explored)

		cells_explored, time_stamp = astar.adaptive_repeatedForwardAstar(pygame, grid, startCoord, goalCoord, time)
		adpt_sheet.write(i + 1, 0, i + 1)
		adpt_sheet.write(i + 1, 1, time_stamp)
		adpt_sheet.write(i + 1, 2, cells_explored)


		pygame.quit()
	book.save("Results.xls")


main()