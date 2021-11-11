# Untitled 2.py
# Created by Kids on 11/17/20.

def recursive_factorial(number, the_fact):
	if number == 0:
		print("if")
		return the_fact
	else:
		print("else")
		new_fact = the_fact * number
		new_number = number - 1
		a = recursive_factorial(new_number, new_fact)
		return a
if __name__ == "__main__":
	print(recursive_factorial(4, 1))
		