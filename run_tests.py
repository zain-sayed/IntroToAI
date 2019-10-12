import astar
import pygame
import gridFunc
import xlwt
import time
import random

NUM_TIMES = 1

def write_row(sheet, row, row_list):
	for i in range(len(row_list)):
		sheet.write(row, i, row_list[i])

def main():
	book = xlwt.Workbook()
	fwd_sheet = book.add_sheet("Foward")
	bwd_sheet = book.add_sheet("Backward")
	adpt_sheet = book.add_sheet("Adaptive")
	sheets = [fwd_sheet, bwd_sheet, adpt_sheet]
	columns = ["Observation", "StartX", "StartY", "EndX", "EndY", "Time", "Cells Expanded"]
	for i in range(len(columns)):
		for sheet in sheets:
			sheet.write(0, i, columns[i])

	"""
	fwd_sheet.write(0, 0, "Observation")
	fwd_sheet.write(0, 1, "StartX")
	fwd_sheet.write(0, 2, "StartY")
	fwd_sheet.write(0, 3, "EndX")
	fwd_sheet.write(0, 4, "EndY")	
	fwd_sheet.write(0, 5, "Time")
	fwd_sheet.write(0, 6, "Cells Expanded")
	fwd_sheet.write(0, 7, "Shortest Path Found")

	bwd_sheet.write(0, 0, "Observation")
	bwd_sheet.write(0, 1, "StartX")
	bwd_sheet.write(0, 2, "StartY")
	bwd_sheet.write(0, 3, "EndX")
	bwd_sheet.write(0, 4, "EndY")
	bwd_sheet.write(0, 5, "Time")
	bwd_sheet.write(0, 6, "Cells Expanded")
	bwd_sheet.write(0, 7, "Shortest Path Found")

	adpt_sheet.write(0, 0, "Observation")
	adpt_sheet.write(0, 1, "StartX")
	adpt_sheet.write(0, 2, "StartY")
	adpt_sheet.write(0, 3, "EndX")
	adpt_sheet.write(0, 4, "EndY")
	adpt_sheet.write(0, 5, "Time")
	adpt_sheet.write(0, 6, "Cells Expanded")
	adpt_sheet.write(0, 7, "Shortest Path Found")
	"""

	random.seed(5)

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
		forward_grid = gridFunc.grid_init(startCoord, goalCoord)
		astar_grid = gridFunc.grid_init_white(startCoord, goalCoord)

		# initialize grid for backward
		backward_grid = gridFunc.grid_copy(forward_grid)
		backward_astar_grid = gridFunc.grid_init_white(startCoord, goalCoord)

		# initialize grid for adaptive
		adaptive_grid = gridFunc.grid_copy(forward_grid)
		adaptive_astar_grid = gridFunc.grid_init_white(startCoord, goalCoord)

		fwd_results = astar.repeated_astar(pygame, forward_grid, astar_grid, startCoord, goalCoord, time, 3)
		write_row(fwd_sheet, i + 1, [i + 1] + list(fwd_results))
		bwd_results = astar.repeated_astar(pygame, backward_grid, backward_astar_grid, startCoord, goalCoord, time, 2)
		write_row(bwd_sheet, i + 1, [i + 1] + list(bwd_results))
		adpt_results = astar.adaptive_astar(pygame, adaptive_grid, adaptive_astar_grid, startCoord, goalCoord, time, 8)
		write_row(adpt_sheet, i + 1, [i + 1] + list(adpt_results))
		
		"""
		# forward
		cells_explored, time_stamp = astar.repeated_astar(pygame, forward_grid, astar_grid, startCoord, goalCoord, time, 3)
		fwd_sheet.write(i + 1, 0, i + 1)
		fwd_sheet.write(i + 1, 1, time_stamp)
		fwd_sheet.write(i + 1, 2, cells_explored)

		# backward
		cells_explored, time_stamp = astar.repeated_astar(pygame, backward_grid, backward_astar_grid, startCoord, goalCoord, time, 2)
		bwd_sheet.write(i + 1, 0, i + 1)
		bwd_sheet.write(i + 1, 1, time_stamp)
		bwd_sheet.write(i + 1, 2, cells_explored)

		# adaptive
		cells_explored, time_stamp = astar.adaptive_astar(pygame, adaptive_grid, adaptive_astar_grid, startCoord, goalCoord, time, 8)
		adpt_sheet.write(i + 1, 0, i + 1)
		adpt_sheet.write(i + 1, 1, time_stamp)
		adpt_sheet.write(i + 1, 2, cells_explored)
		"""

		pygame.quit()
	book.save("Results.xls")


main()