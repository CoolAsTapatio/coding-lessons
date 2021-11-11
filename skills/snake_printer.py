# Untitled.py
# Created by Kids on 11/17/20.
'''def snake_printer(number, snake):
	if len(snake) == number:
		return snake + ":"
	else:
		if len(snake) % 2:
			new_snake = snake + "\\"
			a  = snake_printer(number, new_snake) 
			return a
		else:
			new_snake =snake + "/"
			b = snake_printer(number, new_snake)
			return b'''
def snake_printer(number, snake):
	if number == 0:
		return snake + ":"
	else:
		if len(snake) % 2:
			new_snake = snake + "\\"
			new_number = number - 1
			a  = snake_printer(new_number, new_snake) 
			return a
		else:
			new_snake = snake + "/"
			new_number = number - 1
			b = snake_printer(new_number, new_snake) 
			return b	
if __name__ == "__main__":
	answer = int(input("please give the number of slashes that you would like the snake to have\n"))
	# /\/\/\/\:   --> length of snake 8
	#/\/\/:		--> length of snake 5
	print(snake_printer(answer, ""))
	