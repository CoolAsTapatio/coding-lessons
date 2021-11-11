# Untitled 2.py
# Created by Kids on 9/16/21.
# 99
# 64
#
def base_10_to_binary(base_ten):
	print(base_ten)
	binary = ""
	largest_binary = biggest_binary(base_ten) #to find so that it can be added in binary and subtracted from the base ten number
	print(largest_binary)
	while largest_binary >= 1.0:
		if base_ten >= largest_binary:
			binary += "1"
			base_ten -= largest_binary
			largest_binary /= 2
		else:
			binary += "0"
			largest_binary /= 2
	return binary
			 
def biggest_binary(base_10):
	starter = 1
	while starter <= int(base_10):
		starter *= 2
	return starter/2
def binary_to_base_10(binary):
	base_ten_number = 0
	what_to_add = 1
	for i in range(len(binary)-1, -1, -1):
		if binary[i] == "0":
			what_to_add *= 2
		else:
			base_ten_number += what_to_add
			what_to_add *= 2
	return base_ten_number

def binary_to_b10_unit_test1():
	string_ = "11101"
	expected = 	29
	result = binary_to_base_10(string_)
	assert(expected == result)
	
def binary_to_b10_unit_test2():
	string_ = "01101"
	expected = 	13
	result = binary_to_base_10(string_)
	assert(expected == result)
	
def b10_to_binary_unit_test1():
	b10_number_ = 35
	expected = 	"100011"
	result = base_10_to_binary(b10_number_)
	assert(expected == result)
	
def b10_to_binary_unit_test2():
	b10_number = 100
	expected = 	"1100100"
	result = base_10_to_binary(b10_number)
	assert(expected == result)
def unit_test_runner():
	binary_to_b10_unit_test_runner()
	b10_to_binary_unit_test_runner()
	
def b10_to_binary_unit_test_runner():
	b10_to_binary_unit_test1()
	b10_to_binary_unit_test2()
	
def binary_to_b10_unit_test_runner():
	binary_to_b10_unit_test1()
	binary_to_b10_unit_test2()

def main():
	addend_subtractee = int(input(("what number would you like to have added to or subtracted from?\n")))
	operation = input("would you like to add or subtract?\n")
	addend_subtractor = int(input(("what number would you like to have added to or subtracted by?\n")))
	final_b10_number = operator_(operation, addend_subtractee, addend_subtractor)
	finished = final_b10_number
	print(final_b10_number)
	return finished
def operator_(operation, st_number, nd_number):
	if operation == "add":
		operated_on_number = st_number + nd_number
		return base_10_to_binary(st_number) + " + " + base_10_to_binary(nd_number) + " = " + base_10_to_binary(operated_on_number)   
	elif operation == "subtract":
		operated_on_number = st_number - nd_number
		return base_10_to_binary(st_number) + " - " + base_10_to_binary(nd_number) + " = " + base_10_to_binary(operated_on_number)   
	elif operation == "multiply":
		operated_on_number = st_number * nd_number
		return base_10_to_binary(st_number) + " * " + base_10_to_binary(nd_number) + " = " + base_10_to_binary(operated_on_number)   
if __name__ == "__main__":
	#unit_test_runner()
	main()
	#answer = int(input("what binary number would you like to have turned into a base 10 number?"))
#	binary_to_base_10(binary)
	
	
	
	'''
	1 0 0 1 1 1
	          
	32 16 8 4 2 1
	
	     32 + 0  +   0+ 4 + 2 +1
	
	
	
	'''