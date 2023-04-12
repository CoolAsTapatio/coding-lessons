# Untitled 2.py
# Created by Kids on 12/2/21.
'''
>>> def x1 7
>>> def x2 x1
>>> get x2
7
>>>

'''
def paren_check(string, should_be_zero=0):
	if len(string) == 0:
		if should_be_zero == 0:
			return True
		else:
			return False
	else:
		if string[0] == "(":
			should_be_zero += 1
			new_string = string[1: ]
			return paren_check(new_string, should_be_zero)
		elif string[0] == ")":
			if should_be_zero == 0:
				return False 
			else:
				should_be_zero -= 1
				new_string = string[1: ]
				return paren_check(new_string, should_be_zero)
		else:
			new_string = string[1: ]
			return paren_check(new_string, should_be_zero)
def driver():
	library = {}	
	is_user_done = False
	while is_user_done == False:
		current_request = input(">>> ")
		if current_request == "exit":
			is_user_done == True
		else:
			print(parse(current_request, library))
	return
	
'''
parse("(add 3 1)", lib)
	reqquest = "(add 3 (mult 2 4))"
	tbe = ""
	0 -- 17
	i = 0
	result = 
		i = 0
		tbe = ""
		request = "add 3 (mult 2 4))"
		
		tbe = "a"
		i = 1
		tbe = "add"
		i = 2
		tbe = "add "
		i = 3
		tbe = "add 3"
		i = 4
		tbe = "add 3 "
		i = 5
			i = 0
			tbe = ""
			request = "mult 2 4))"
			tbe = "m"
			tbe = "mu"
			.
			.
			.
			tbe = "mult 2 4"
			return "8", 8
		
		tbe = "add 3 8"
		i = 14
		
		return "4", 7
	result = "4", 7
	tbe = "4"
	i = 8
		
		
		
	

'''

def parse(request, library, l=0):
	to_be_executed = ""
	print(request)
	i = 0
	l = 0

	while i < len(request):
		print("l: " + str(l))
		print("i: " + str(i))
		print(to_be_executed)
		if request[i] == "(":
			print("requdst: " + str(request))
			result = parse(request[i+1:], library, l)
			print("result: " + str(result))
			to_be_executed += result[0]
			print("type of l: " + str(type(l)))
			l += result[1] + 1
			print("i: "+ str(type(i)))
			i += l
			print("i after adding: " + str(i))
		elif request[i] == ")":
			print("len : " + str(len(to_be_executed)))
			li = l + len(to_be_executed)
			return str(execute_math(library, to_be_executed)), li
		else:
			to_be_executed += request[i]
		i += 1
		
	return result[0]
		
	#		command_set = current_request.split(" ")
def execute_math(library, to_be_executed):
	print("e: " + to_be_executed)
	command_set = to_be_executed.split(" ")
	if command_set[0] == "def":
		return execute_def_command(library, command_set)
	elif command_set[0] == "get":
		return execute_get_command(library, command_set)
	elif command_set[0] == "add":
		return execute_add_command(library, command_set)
	elif command_set[0] == "sub":
		return execute_sub_command(library, command_set)
	elif command_set[0] == "mult":
		return execute_mult_command(library, command_set)
	elif command_set[0] == "div":
		return execute_div_command(library, command_set)
def execute_add_command(library, command_set):
	if command_set[2] in library and command_set[1] in library:
		return int(library[command_set[1]]) + int(library[command_set[2]])
	elif command_set[2] in library:
		return int(command_set[1]) + int(library[command_set[2]])
	elif command_set[1] in library:
		return int(library[command_set[1]]) + int(command_set[2])
	else:
		return int(command_set[1]) + int(command_set[2])
def execute_sub_command(library, command_set):
	if command_set[2] in library and command_set[1] in library:
		return int(float(library[command_set[1]])) - int(float(library[command_set[2]]))
	elif command_set[2] in library:
		return int(float(command_set[1])) - int(float(library[command_set[2]]))
	elif command_set[1] in library:
		return int(float(library[command_set[1]])) - int(float(command_set[2]))
	else:
		return int(float(command_set[1])) - int(float(command_set[2]))
def execute_mult_command(library, command_set):
	if command_set[2] in library and command_set[1] in library:
		return int(library[command_set[1]]) * int(library[command_set[2]])
	elif command_set[2] in library:
		return int(command_set[1]) * int(library[command_set[2]])
	elif command_set[1] in library:
		return int(library[command_set[1]]) * int(command_set[2])
	else:
		return int(command_set[1]) * int(command_set[2])
def execute_div_command(library, command_set):
	if command_set[2] == 0:
		print("math don't work")
	elif command_set[2] in library and command_set[1] in library:
		return int(library[command_set[1]]) / int(library[command_set[2]])
	elif command_set[2] in library:
		return int(command_set[1]) / int(library[command_set[2]])
	elif command_set[1] in library:
		return int(library[command_set[1]]) / int(command_set[2])
	else:
		return int(command_set[1]) / int(command_set[2])
def execute_def_command(library, command_set):
	if command_set[2] in library:
		library[command_set[1]] = library[command_set[2]]
	else:
		library[command_set[1]] = command_set[2]
	return library[command_set[1]]
def execute_get_command(library, command_set):
	print(library[command_set[1]])
	return 
def main():
	driver()
if __name__ == "__main__":
	main()