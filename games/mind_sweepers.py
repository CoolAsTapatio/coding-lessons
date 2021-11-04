import math
import random
import copy
def setup(grid_creator_list_2d):
	grid_creator_list_2d_copy = copy.deepcopy(grid_creator_list_2d)
	number_copy = copy.deepcopy(grid_creator_list_2d)
	user_grid = grid_creator_list_2d_copy
	true_grid = assign_bombs(grid_creator_list_2d)
	print("\n\n\n")
	assign_numbers(true_grid)
	test_driver(user_grid, true_grid, number_copy)
'''
def driver(user_grid, true_grid):
	lost = False
	while lost == False:
		count_win_check = 0
		for i in user_grid:
			for i2 in i:
				if i2 == "__":
					count_win_check += 1
		if count_win_check == 0:
			winner_sequence()
		else:				
			print("the current grid is:")
			print_grid(user_grid)	
			coordinate = input("what coordinate _, _ would you like to look up?\n")
			lost = coordinate_guess_responder(coordinate, true_grid, user_grid)
'''
def test_driver(user_grid, true_grid, number_copy):
	lost = False
	while lost == False:
		count_win_check_user_grid = 0
		count_win_check_true_grid = 0
		for i in user_grid:
			for i2 in i:
				if i2 == "__" or i2 == "bb":
					count_win_check_user_grid += 1
		for f in true_grid:
			for f2 in f:
				if f2 == "xx":
					count_win_check_true_grid += 1
		if count_win_check_user_grid == count_win_check_true_grid:
			winner_sequence()
		else:				
			print("the current grid is:")
			print_grid(user_grid)	
			print("\n")
			coordinate = input("what coordinate _, _ would you like to reveal?\n")
			lost = coordinate_guess_responder(coordinate, true_grid, user_grid, number_copy)
	

def coordinate_guess_responder(coordinate, true_grid, user_grid, number_copy):
	if coordinate == "r":
		bomb_marker_input = input("what coordinate _, _ would you like to unmark as a bomb?\n")
		confirmation = input("are you sure that you would like to unmark this as a bomb?\n")
		if confirmation == "yes":
			row_column = bomb_marker_input.split(", ")
			transformed_coodinates = coordinate_transformer(row_column, user_grid)
			user_grid[transformed_coodinates[0]][transformed_coodinates[1]] = "__"
		return False
	elif coordinate == "b":
		bomb_marker_input = input("what coordinate _, _ would you like to mark as a bomb?\n")
		confirmation = input("are you sure that you would like to mark this as a bomb?\n")
		if confirmation == "yes":
			row_column = bomb_marker_input.split(", ")
			transformed_coodinates = coordinate_transformer(row_column, user_grid)
			user_grid[transformed_coodinates[0]][transformed_coodinates[1]] = "bb"
		else:
			pass
		return False
	else:	
		coordinate_set = coordinate.split(", ")
		transformed_coordinates = coordinate_transformer(coordinate_set, user_grid)
#		print("transformed_coordinates:", str(transformed_coordinates))
		t_column = transformed_coordinates[0]
		t_row = transformed_coordinates[1]
#		true_grid[t_column][t_row] = "$$"
#		print_grid(true_grid)
		if true_grid[t_column][t_row] == "xx":
			bomb_handler()
			return True
		else:
			number_handler(user_grid, true_grid, t_row, t_column, number_copy)
			return False
def bomb_handler():
	loser_sequence()

def winner_sequence():
	play_again = input("you won! ould you like to play again?\n")
	if play_again == "yes":
		reset()
	else:
		print("thank you for playing.")
		exit()
def loser_sequence():
	play_again = input("oops, you landed on a bomb, would you like to play again?\n")
	if play_again == "yes":
		reset()
	else:
		print("thank you for playing.")
		exit()
		
def reset():
	main()
	
def number_handler(user_grid, true_grid, t_row, t_column, number_copy):
	coordinate_val = true_grid[t_column][t_row]
	user_grid[t_column][t_row] = true_grid[t_column][t_row]
	number_copy[t_column][t_row] = true_grid[t_column][t_row]
	if coordinate_val == 0:
		zero_handler(user_grid, true_grid, t_row, t_column, number_copy)
	else:
		non_zero_handler(user_grid, true_grid, t_row, t_column)
	return
		
def zero_handler(user_grid, true_grid, t_row, t_column, number_copy):
	#user_grid[t_column][t_row] = true_grid[t_column][t_row]
	
	neighboring_coordinates = []
	neighboring_coordinates.append((t_column-1,t_row-1))
	neighboring_coordinates.append((t_column-1,t_row))
	neighboring_coordinates.append((t_column-1,t_row+1))
	neighboring_coordinates.append((t_column,t_row-1))
	neighboring_coordinates.append((t_column,t_row+1))
	neighboring_coordinates.append((t_column+1,t_row-1))
	neighboring_coordinates.append((t_column+1,t_row))
	neighboring_coordinates.append((t_column+1,t_row+1))
	final_neighboring_coordinates = []
	for i in neighboring_coordinates:
		if i[0] <= -1 or i[1] <= -1 or i[0] >= len(true_grid) or i[1] >= len(true_grid):
			#invalid case
			pass
		else:
			final_neighboring_coordinates.append(i)
	
#	print("final neighbors: " + str(final_neigh12boring_coordinates))
	for f in final_neighboring_coordinates:
		if user_grid[f[0]][f[1]] == "__":
#			print("the coord we are on is " + str(f))
			number_handler(user_grid, true_grid, f[1], f[0], number_copy)
#		else:
#			print("it's not blank\n\n")
	
	return		
	
def non_zero_handler(user_grid, true_grid, t_row, t_column):
#	user_grid[t_column][t_row] = true_grid[t_column][t_row]
	
#	print("we're in the non-zero handler")
#	print_grid(user_grid)
	return
	
def coordinate_transformer(coordinates, user_grid):
	row = int(coordinates[0])-1 
	column = int(coordinates[1])
	column = len(user_grid[0]) - column
	return column,row
#this function assigns numbers based on the surrounding amount of bombs
#(1, 1) (2, 1) (3, 1)  (-1, -1) (0, -1) (+1, -1)
#(1, 2) (2, 2) (3, 2)  (-1, = ) (0 , 0) (+1,  =)
#(1, 3) (2, 3, (3, 3)  (-1, +1) (0, +1) (+1, +1)
def assign_numbers(true_grid):
	for row in range(0, len(true_grid)):
		for column in range(0, len(true_grid[row])):
			how_many = 0 #counts surrounding bombs
			x,y = row, column 
			if true_grid[x][y] != "xx":
				try:		
					if true_grid[x-1][y-1] == "xx" and x>0 and y>0:
						how_many += 1
				except:
					pass
				try:
					if true_grid[x][y-1] == "xx" and y>0:
						how_many += 1
				except:
					pass
				try:
					if true_grid[x+1][y-1] == "xx" and x<len(true_grid) and y>0:
						how_many += 1
				except:
					pass
				try:
					if true_grid[x-1][y] == "xx" and x>0:
						how_many += 1
				except:
					pass
				try:		
					if true_grid[x+1][y] == "xx" and x<len(true_grid):
						how_many += 1
				except:
					pass
				try:
					if true_grid[x-1][y+1] == "xx" and x>0 and y<len(true_grid):
						how_many += 1
				except:
					pass
				try:
					if true_grid[x][y+1] == "xx" and y<len(true_grid):
						how_many += 1
				except:
					pass
				try:
					if true_grid[x+1][y+1] == "xx" and x<len(true_grid) and y<len(true_grid):
						how_many += 1
				except:
					pass
				true_grid[x][y] = how_many

#this function prints out the grid that the users can see (without the bombs)
def print_grid(list_of_individual_lines):
	print("\n")
	for t in list_of_individual_lines:
		one_line_string = ""
		for t2 in t:
			if t2 != "xx" and t2 != "__" and t2 != "bb":
				one_line_string += " " + str(t2) + "  "
				
			else:
				one_line_string += str(t2) + "  "
		print(one_line_string) 
		
#functions finds thirty percent (rounded up) this number of location in the grid and randomly places bombs
def assign_bombs(grid):
	number_of_bombs_to_find_thirty_percent_of = len(grid[0])* len(grid[0])
	one_tenth = number_of_bombs_to_find_thirty_percent_of / 10 # one_tenth_of_total_locations_to_then_multiply_by_three
	thirty_percent = one_tenth * 3 #30 percent of the locations
	thirty_percent_rounded_up = math.ceil(thirty_percent)
	bomb_countdown = thirty_percent_rounded_up # how many bombs are left to assign
	while bomb_countdown > 0:
		grid_ = where_does_bomb_go(grid)
		grid = grid_
		bomb_countdown -= 1
	return grid
	
	
#this functional places bombs in certain coordinates
def where_does_bomb_go(grid):
	size_for_grid_input = len(grid[0])
	x_coordinate = random.randint(0, size_for_grid_input-1)
	y_coordinate = random.randint(0, size_for_grid_input-1)
	grid_y = grid[y_coordinate]
	grid_xy = grid_y[x_coordinate] = "xx"
	return grid
	
	
def main():
	#dimensions are? 15x15
	grid_creator_list_2d = create_grid()
	setup(grid_creator_list_2d)
def create_grid():
	#this list is the grid being made
	grid_creator_list_2d = []
	#stores one line of the grid to be looped
	one_line_string_single_interval_list = []
	size_for_grid_input = int(input("what size would you like your mind sweepers™ grid to be?\n"))
	for i in range(0, size_for_grid_input):
		one_line_string_single_interval_list.append("__")
	for s in range(0, size_for_grid_input):
		copy_of = copy.copy(one_line_string_single_interval_list)
		grid_creator_list_2d.append(copy_of)
	return grid_creator_list_2d
if __name__ == "__main__":
	main()
	#bombed_grid(grid_creator_list_2d, size_for_grid_input)