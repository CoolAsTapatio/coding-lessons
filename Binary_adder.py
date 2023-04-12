# Untitled.py
# Created by Kids on 4/20/22.
def main():
	return binary_adder()
	
def binary_adder():
	final_number_list = []
	first_number = input("what is the first binary number that you would like to add: ")
	second_number = input("what is the second binary number that you would like to add: ")
	first_number, second_number = while_function(first_number, second_number)	
	for i in first_number:
		final_number_list.append(0)
	final_number_list.append(0)
	for i in range(0, len(first_number)):
		final_number_list[i] += int(first_number[i]) + int(second_number[i])
		if i > 1:
			final_number_list[i+1] = final_number_list[i]-1
	final_number = ""
	for i in final_number_list:
		final_number += str(i)
	print(final_number)
	return final_number

def while_function(first_number, second_number):	
	while len(first_number) != len(second_number):
		if len(first_number) <= len(second_number):
			first_number = "0" + first_number
		elif len(first_number) >= len(second_number):
			second_number = "0" + second_number
	return first_number, second_number
def while_function_UT():
	v1 = "101010"
	v2 = "lololololol"
	expected_result = "00000101010", "lololololol"
	result = while_function(v1, v2)
	assert(expected_result == result)
	
if __name__ == "__main__":
	main()